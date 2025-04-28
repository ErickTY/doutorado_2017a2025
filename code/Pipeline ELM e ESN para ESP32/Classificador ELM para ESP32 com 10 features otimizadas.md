// Classificador ELM para ESP32 com 10 features otimizadas
// Pré-requisitos: arquivos convertidos para float[] a partir de CSV

#include <Arduino.h>
#include "pesos_elm.h" // arquivos gerados com W[10][HIDDEN] e Wout[HIDDEN][CLASSES]

#define FEATURES 10
#define HIDDEN 10
#define CLASSES 4

float input[FEATURES];
float hidden[HIDDEN];
float output[CLASSES];

// Simples aproximação de tanh
float tanh_approx(float x) {
  if (x < -3) return -1;
  if (x > 3) return 1;
  return x * (27 + x*x) / (27 + 9 * x*x);
}

// Normalização Z-Score local (valores fixos embarcados)
float mean[FEATURES] = { /* inseridos via Python */ };
float stddev[FEATURES] = { /* inseridos via Python */ };

void normalize_input(float raw[FEATURES]) {
  for (int i = 0; i < FEATURES; i++) {
    input[i] = (raw[i] - mean[i]) / stddev[i];
  }
}

int classify_elm() {
  for (int i = 0; i < HIDDEN; i++) {
    hidden[i] = 0;
    for (int j = 0; j < FEATURES; j++) {
      hidden[i] += W[i][j] * input[j];
    }
    hidden[i] = tanh_approx(hidden[i]);
  }

  for (int i = 0; i < CLASSES; i++) {
    output[i] = 0;
    for (int j = 0; j < HIDDEN; j++) {
      output[i] += Wout[i][j] * hidden[j];
    }
  }

  int argmax = 0;
  for (int i = 1; i < CLASSES; i++) {
    if (output[i] > output[argmax]) argmax = i;
  }
  return argmax;
}

void setup() {
  Serial.begin(115200);
  // Exemplo: valores simulados de sensor já reduzidos para 10 features
  float raw_sensor_data[FEATURES] = {0.32, 0.44, 0.12, 0.89, ...};
  normalize_input(raw_sensor_data);
  int result = classify_elm();
  Serial.print("Classe detectada: ");
  Serial.println(result);
}

void loop() {
  // Adicione leitura contínua aqui
  delay(1000);
}
