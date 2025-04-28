import numpy as np

def save_array_to_header(array, filename, var_name):
    """Salva um array numpy em formato de arquivo .h para C/C++"""
    with open(filename, 'w') as f:
        f.write(f"// {filename} - Gerado automaticamente\n")
        f.write(f"const float {var_name}[{array.shape[0]}][{array.shape[1]}] = {{\n")
        for row in array:
            row_str = ", ".join(f"{v:.6f}" for v in row)
            f.write(f"  {{{row_str}}},\n")
        f.write("};\n")
    print(f"Arquivo {filename} gerado com sucesso!")

# --- Exemplo de uso para ELM ---

# Carregar pesos salvos
elm_input_weights = np.load("elm_input_weights.npy")  # shape: (n_hidden, n_features)
elm_output_weights = np.load("elm_output_weights.npy")  # shape: (n_hidden, n_outputs)

# Gerar headers
save_array_to_header(elm_input_weights, "elm_input_weights_data.h", "elm_input_weights")
save_array_to_header(elm_output_weights, "elm_output_weights_data.h", "elm_output_weights")

# --- Exemplo de uso para ESN ---

# Carregar pesos salvos
esn_Win = np.load("esn_Win.npy")  # shape: (n_reservoir, n_inputs)
esn_W = np.load("esn_W.npy")      # shape: (n_reservoir, n_reservoir)
esn_Wout = np.load("esn_Wout.npy")  # shape: (n_reservoir + n_inputs, n_outputs)

# Gerar headers
save_array_to_header(esn_Win, "esn_Win_data.h", "esn_Win")
save_array_to_header(esn_W, "esn_W_data.h", "esn_W")
save_array_to_header(esn_Wout, "esn_Wout_data.h", "esn_Wout")
