import pandas as pd
import os
import tsfel
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Caminho base para os arquivos
base_path = './datasets/'

# Lista de arquivos enviados (com nomes e rótulos atribuídos manualmente)
arquivos = [
    #("sensor_data_sVaz_circuito1.csv", "normal"),
    ("sensor_data_sVaz_circuito2.csv", "normal"),
    #("sensor_data_sVaz_circuito31_coleta1.csv", "normal"),
    #("sensor_data_sVaz_circuito31_coleta2.csv", "normal"),
    #("sensor_data_sVaz_circuito32_coleta1.csv", "normal"),
    #("sensor_data_sVaz_circuito32_coleta2.csv", "normal"),
    #("sensor_data_cVaz_circuito1_avanço_0.6mm.csv", "vazamento_avanco"),
    #("sensor_data_cVaz_circuito1_recuo_0.6mm.csv", "vazamento_recuo"),
    ("sensor_data_cVaz_circuito2_avanço_0.6mm.csv", "vazamento_avanco"),
    ("sensor_data_cVaz_circuito2_recuo_0.6mm.csv", "vazamento_recuo")
]

# Função para extrair janelas (intervalos) do sinal
def extrair_janelas(signal, tamanho=100, passo=10):
    janelas = []
    for i in range(0, len(signal) - tamanho, passo):
        janelas.append(signal[i:i + tamanho].values.flatten())  # Ensure each window is a flat array
    return janelas

# Carregar e processar todos os arquivos
dados_janelas = []
rotulos = []

for nome_arquivo, rotulo in arquivos:
    df = pd.read_csv(os.path.join(base_path, nome_arquivo))
    if "Pressure (bar)" not in df.columns:
        continue
    janelas = extrair_janelas(df["Pressure (bar)"])
    dados_janelas.extend(janelas)
    rotulos.extend([rotulo] * len(janelas))

# Reshape data for TSFEL -  create a DataFrame where each column is a time step
num_time_steps = len(dados_janelas[0])  # Assuming all windows have the same length
print(num_time_steps)
all_windows = np.array(dados_janelas)  # Convert list of windows to a 2D array
print(all_windows)
df_tsfel_input = pd.DataFrame(all_windows) 

# Add labels as a separate column
df_tsfel_input['label'] = rotulos

# Extração de features com TSFEL
cfg = tsfel.get_features_by_domain()
# Now pass the DataFrame without the 'label' column to the extractor
features = tsfel.time_series_features_extractor(cfg, df_tsfel_input.drop(columns=['label']), window_size=100, verbose=0)

# Codificar os rótulos
le = LabelEncoder()
y = le.fit_transform(df_tsfel_input['label'])

# Salvar para uso no AIModelPipeline
features.to_csv("./datasets/X_tsfel.csv", index=False)
pd.DataFrame({"label": y}).to_csv("./datasets/y_tsfel.csv", index=False)

print("✔️ Dados preparados e salvos: X_tsfel.csv e y_tsfel.csv")
