// elm_model.h - Pesos do modelo ELM (Extreme Learning Machine)
// Este arquivo contém os pesos necessários para realizar a inferência utilizando ELM no ESP32.

#ifndef ELM_MODEL_H
#define ELM_MODEL_H

// Definições do modelo ELM
#define ELM_INPUT_SIZE 10   // Número de entradas (features)
#define ELM_HIDDEN_SIZE 200 // Número de neurônios na camada escondida
#define ELM_OUTPUT_SIZE 4   // Número de classes (avanço normal, recuo normal, vazamento avanço, vazamento recuo)

// Pesos da entrada para a camada escondida (Input -> Hidden)
const float elm_input_weights[ELM_HIDDEN_SIZE][ELM_INPUT_SIZE] = {
  // Pesos reais do seu modelo serão inseridos aqui
  #include "elm_input_weights_data.h" // Arquivo gerado separadamente para organização
};

// Pesos da camada escondida para a camada de saída (Hidden -> Output)
const float elm_output_weights[ELM_HIDDEN_SIZE][ELM_OUTPUT_SIZE] = {
  // Pesos reais do seu modelo serão inseridos aqui
  #include "elm_output_weights_data.h" // Arquivo gerado separadamente para organização
};

#endif // ELM_MODEL_H
