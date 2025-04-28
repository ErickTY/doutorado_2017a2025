// main_elm_esn_example.ino - Código principal do ESP32
// Realiza leitura do sensor, pré-processamento e inferência com ELM ou ESN

#include <Arduino.h>
#include "features.h"
#include "normalization.h"
#include "elm_model.h"
#include "esn_model.h"

// Definições principais
#define LOAD_MODEL_FROM_FLASH 1
#define MODEL_TYPE "ELM" // "ELM" ou "ESN"

#define SENSOR_PIN 34
#define LED_PIN 2
#define BUZZER_PIN 15

#define WINDOW_SIZE 100

// Variáveis globais
float input_raw[WINDOW_SIZE];
float input_normalized[10];

TaskHandle_t TaskPreProcess;
TaskHandle_t TaskClassify;

// Funções auxiliares
void normalize_input(float* window, float* normalized_output) {
  for (int i = 0; i < 10; i++) {
    normalized_output[i] = (window[i] - feature_means[i]) / feature_stds[i];
  }
}

float predict_elm(float* input_features) {
  float hidden[ELM_HIDDEN_SIZE];
  float output[ELM_OUTPUT_SIZE] = {0};

  for (int i = 0; i < ELM_HIDDEN_SIZE; i++) {
    float sum = 0;
    for (int j = 0; j < ELM_INPUT_SIZE; j++) {
      sum += elm_input_weights[i][j] * input_features[j];
    }
    hidden[i] = 1.0 / (1.0 + exp(-sum)); // Ativação sigmoid
  }

  for (int i = 0; i < ELM_HIDDEN_SIZE; i++) {
    for (int j = 0; j < ELM_OUTPUT_SIZE; j++) {
      output[j] += hidden[i] * elm_output_weights[i][j];
    }
  }

  int predicted_class = 0;
  float max_val = output[0];
  for (int i = 1; i < ELM_OUTPUT_SIZE; i++) {
    if (output[i] > max_val) {
      max_val = output[i];
      predicted_class = i;
    }
  }
  return predicted_class;
}

float predict_esn(float* input_features) {
  float state[ESN_RESERVOIR_SIZE] = {0};

  // Atualiza o estado interno
  for (int t = 0; t < 1; t++) { // Apenas uma atualização pois temos uma janela já processada
    float new_state[ESN_RESERVOIR_SIZE] = {0};
    for (int i = 0; i < ESN_RESERVOIR_SIZE; i++) {
      float sum_in = 0;
      for (int j = 0; j < ESN_INPUT_SIZE; j++) {
        sum_in += esn_Win[i][j] * input_features[j];
      }
      float sum_res = 0;
      for (int j = 0; j < ESN_RESERVOIR_SIZE; j++) {
        sum_res += esn_W[i][j] * state[j];
      }
      new_state[i] = tanh(sum_in + sum_res);
    }
    memcpy(state, new_state, sizeof(state));
  }

  // Extensão do estado
  float extended_state[ESN_RESERVOIR_SIZE + ESN_INPUT_SIZE];
  memcpy(extended_state, state, sizeof(state));
  memcpy(extended_state + ESN_RESERVOIR_SIZE, input_features, sizeof(float) * ESN_INPUT_SIZE);

  // Inferência
  float output[ESN_OUTPUT_SIZE] = {0};
  for (int i = 0; i < ESN_RESERVOIR_SIZE + ESN_INPUT_SIZE; i++) {
    for (int j = 0; j < ESN_OUTPUT_SIZE; j++) {
      output[j] += extended_state[i] * esn_Wout[i][j];
    }
  }

  int predicted_class = 0;
  float max_val = output[0];
  for (int i = 1; i < ESN_OUTPUT_SIZE; i++) {
    if (output[i] > max_val) {
      max_val = output[i];
      predicted_class = i;
    }
  }
  return predicted_class;
}

float predict_model(float* input_features, const char* model_type) {
  if (strcmp(model_type, "ELM") == 0) {
    return predict_elm(input_features);
  } else if (strcmp(model_type, "ESN") == 0) {
    return predict_esn(input_features);
  } else {
    Serial.println("Modelo desconhecido.");
    return -1.0;
  }
}

void PreProcessTask(void *pvParameters) {
  int idx = 0;
  for (;;) {
    int sensorValue = analogRead(SENSOR_PIN);
    float pressure = map(sensorValue, 0, 4095, 0, 1200) / 100.0;
    input_raw[idx++] = pressure;

    if (idx >= WINDOW_SIZE) {
      idx = 0;
      normalize_input(input_raw, input_normalized);
    }

    vTaskDelay(10 / portTICK_PERIOD_MS); // Frequência de amostragem
  }
}

void ClassifyTask(void *pvParameters) {
  for (;;) {
    float resultado = predict_model(input_normalized, MODEL_TYPE);
    int classe_prevista = (int)resultado;

    if (classe_prevista == 2 || classe_prevista == 3) { // Vazamentos
      digitalWrite(LED_PIN, HIGH);
      tone(BUZZER_PIN, 1000);
      Serial.println("\u26a0\ufe0f Vazamento detectado!");
    } else {
      digitalWrite(LED_PIN, LOW);
      noTone(BUZZER_PIN);
    }

    vTaskDelay(100 / portTICK_PERIOD_MS);
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);

  xTaskCreatePinnedToCore(PreProcessTask, "PreProcess", 10000, NULL, 1, &TaskPreProcess, 0);
  xTaskCreatePinnedToCore(ClassifyTask, "Classify", 10000, NULL, 1, &TaskClassify, 1);
}

void loop() {
  // Nada aqui! Todas as tarefas estão nos núcleos.
}
