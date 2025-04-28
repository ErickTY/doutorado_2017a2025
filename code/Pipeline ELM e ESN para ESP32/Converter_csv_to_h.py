import numpy as np
import os

# Diretório de saída para os arquivos .h
output_dir = "generated_weights"
os.makedirs(output_dir, exist_ok=True)

def csv_to_header(csv_file, header_file, var_name):
    data = np.loadtxt(csv_file, delimiter=",")
    with open(os.path.join(output_dir, header_file), 'w') as f:
        f.write(f"// {header_file} - Gerado automaticamente\n")
        if data.ndim == 1:
            f.write(f"const float {var_name}[{data.shape[0]}] = {{\n")
            row_str = ", ".join(f"{v:.6f}" for v in data)
            f.write(f"  {row_str}\n")
            f.write("};\n")
        else:
            f.write(f"const float {var_name}[{data.shape[0]}][{data.shape[1]}] = {{\n")
            for row in data:
                row_str = ", ".join(f"{v:.6f}" for v in row)
                f.write(f"  {{{row_str}}},\n")
            f.write("};\n")
    print(f"Arquivo {header_file} gerado com sucesso!")

# Converter arquivos ELM
csv_to_header("W_elm.csv", "elm_input_weights_data.h", "elm_input_weights")
csv_to_header("Wout_elm.csv", "elm_output_weights_data.h", "elm_output_weights")

# Converter arquivos ESN
csv_to_header("Win_esn.csv", "esn_Win_data.h", "esn_Win")
csv_to_header("Wres_esn.csv", "esn_W_data.h", "esn_W")
csv_to_header("Wout_esn.csv", "esn_Wout_data.h", "esn_Wout")

# Converter arquivos de normalização
csv_to_header("means_selected.csv", "means_data.h", "feature_means")
csv_to_header("stds_selected.csv", "stds_data.h", "feature_stds")
