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
    rotulos_janela = [] # Lista para armazenar os rótulos correspondentes às janelas
    for i in range(0, len(signal) - tamanho, passo):
        janelas.append(signal[i:i + tamanho].values.flatten())
        # Atribuir o rótulo da janela com base no rótulo original do arquivo
        rotulos_janela.append(rotulo)  
    return janelas, rotulos_janela

# Carregar e processar todos os arquivos
dados_janelas = []
rotulos = []

for nome_arquivo, rotulo in arquivos:
    df = pd.read_csv(os.path.join(base_path, nome_arquivo))
    if "Pressure (bar)" not in df.columns:
        continue
    janelas, rotulos_janela = extrair_janelas(df["Pressure (bar)"]) # Obter janelas e rótulos
    dados_janelas.extend(janelas)
    rotulos.extend(rotulos_janela) # Usar os rótulos correspondentes às janelas

dados = {
    "janelas": dados_janelas,
    "rotulos": rotulos
}
dados_tsfel = pd.DataFrame(dados)
# Convert the 'janelas' column to a 2D NumPy array
janelas_np = np.vstack(dados_tsfel['janelas'].values)
# Extração de features com TSFEL
cfg = tsfel.get_features_by_domain()
# Now pass the DataFrame without the 'label' column to the extractor

features = []
for i in range(len(janelas_np)):
    # Extrair as features e converter para array NumPy, removendo o índice
    extracted_features = tsfel.time_series_features_extractor(cfg, janelas_np[i], verbose=0)
    features.append(extracted_features)

features = pd.concat(features, ignore_index=True)
# Codificar os rótulos
le = LabelEncoder()
y = le.fit_transform(dados_tsfel['rotulos'])
features['label'] = y
features['rotulos'] = dados_tsfel['rotulos']
features.to_csv('/content/doutorado2025/datasets/dataset.csv', index=False)
