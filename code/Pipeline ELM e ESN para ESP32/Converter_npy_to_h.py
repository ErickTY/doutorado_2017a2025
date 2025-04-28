# ESP32_Weight_Converter
# Script para converter arquivos .npy de pesos treinados (ELM e ESN) em arquivos .h para ESP32
# Opcionalmente também gera um model_config.json para atualizações OTA

import numpy as np
import json
import os

# Pasta de destino para salvar os arquivos gerados
output_folder = "generated_weights"
os.makedirs(output_folder, exist_ok=True)

# Função para salvar arrays como .h (C/C++)
def save_array_to_header(array, filename, var_name):
    header_path = os.path.join(output_folder, filename)
    with open(header_path, 'w') as f:
        f.write(f"// {filename} - Gerado automaticamente\n")
        f.write(f"const float {var_name}[{array.shape[0]}][{array.shape[1]}] = {{\n")
        for row in array:
            row_str = ", ".join(f"{v:.6f}" for v in row)
            f.write(f"  {{{row_str}}},\n")
        f.write("};\n")
    print(f"Arquivo {filename} salvo em {output_folder}/")

# Função para salvar o model_config.json
def save_model_json(features, means, stds, elm_input, elm_output, esn_Win, esn_W, esn_Wout):
    model = {
        "features": features,
        "normalization": {
            "means": means.tolist(),
            "stds": stds.tolist()
        },
        "elm": {
            "input_weights": elm_input.tolist(),
            "output_weights": elm_output.tolist()
        },
        "esn": {
            "Win": esn_Win.tolist(),
            "W": esn_W.tolist(),
            "Wout": esn_Wout.tolist()
        }
    }
    with open(os.path.join(output_folder, "model_config.json"), "w") as f:
        json.dump(model, f, indent=2)
    print("Arquivo model_config.json salvo em", output_folder)

# --- Exemplo de uso ---

# Carregar pesos salvos (.npy)
elm_input_weights = np.load("elm_input_weights.npy")
elm_output_weights = np.load("elm_output_weights.npy")
esn_Win = np.load("esn_Win.npy")
esn_W = np.load("esn_W.npy")
esn_Wout = np.load("esn_Wout.npy")

# Carregar normalização (exemplo de médias e desvios)
feature_means = np.array([0.015, 0.020, 5.312, 0.018, 45.7, 6.85, 2.11, 0.89, 3.02, 0.75])
feature_stds = np.array([0.012, 0.015, 2.89, 0.011, 25.4, 2.15, 0.35, 0.28, 1.45, 0.24])

# Features selecionadas
features = [
    "0_MFCC_3",
    "0_MFCC_4",
    "0_Negative turning points",
    "0_MFCC_2",
    "0_ECDF Percentile_1",
    "0_Max",
    "0_Entropy",
    "0_Mean absolute deviation",
    "0_Kurtosis",
    "0_Median absolute deviation"
]

# Gerar arquivos .h para ELM
save_array_to_header(elm_input_weights, "elm_input_weights_data.h", "elm_input_weights")
save_array_to_header(elm_output_weights, "elm_output_weights_data.h", "elm_output_weights")

# Gerar arquivos .h para ESN
save_array_to_header(esn_Win, "esn_Win_data.h", "esn_Win")
save_array_to_header(esn_W, "esn_W_data.h", "esn_W")
save_array_to_header(esn_Wout, "esn_Wout_data.h", "esn_Wout")

# Gerar model_config.json para OTA
save_model_json(features, feature_means, feature_stds, elm_input_weights, elm_output_weights, esn_Win, esn_W, esn_Wout)

print("\nConversão completa!")
