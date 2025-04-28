// esn_model.h - Pesos do modelo ESN (Echo State Network)
// Este arquivo contém os pesos necessários para realizar a inferência utilizando ESN no ESP32.

#ifndef ESN_MODEL_H
#define ESN_MODEL_H

// Definições do modelo ESN
#define ESN_INPUT_SIZE 10    // Número de entradas (features)
#define ESN_RESERVOIR_SIZE 200 // Número de neurônios no reservatório
#define ESN_OUTPUT_SIZE 4    // Número de classes

// Pesos da entrada para o reservatório (Input -> Reservoir)
const float esn_Win[ESN_RESERVOIR_SIZE][ESN_INPUT_SIZE] = {
  // Pesos reais serão inseridos aqui
  #include "esn_Win_data.h"
};

// Pesos de conexões internas no reservatório (Reservoir -> Reservoir)
const float esn_W[ESN_RESERVOIR_SIZE][ESN_RESERVOIR_SIZE] = {
  // Pesos reais serão inseridos aqui
  #include "esn_W_data.h"
};

// Pesos do reservatório para a saída (Reservoir -> Output)
const float esn_Wout[ESN_RESERVOIR_SIZE + ESN_INPUT_SIZE][ESN_OUTPUT_SIZE] = {
  // Pesos reais serão inseridos aqui
  #include "esn_Wout_data.h"
};

#endif // ESN_MODEL_H
