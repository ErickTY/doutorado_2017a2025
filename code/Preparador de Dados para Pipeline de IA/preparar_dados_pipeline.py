
import pandas as pd
import os
import tsfel
from sklearn.preprocessing import LabelEncoder

# Caminho base para os arquivos
base_path = '/datasets/'

# Lista de arquivos enviados (com nomes e rótulos atribuídos manualmente)
arquivos = [
    ("sensor_data_sVaz_circuito1.csv", "normal"),
    ("sensor_data_sVaz_circuito2.csv", "normal"),
    ("sensor_data_sVaz_circuito31_coleta1.csv", "normal"),
    ("sensor_data_sVaz_circuito31_coleta2.csv", "normal"),
    ("sensor_data_sVaz_circuito32_coleta1.csv", "normal"),
    ("sensor_data_sVaz_circuito32_coleta2.csv", "normal"),
    ("sensor_data_cVaz_circuito1_avanço_0.6mm.csv", "vazamento_avanco"),
    ("sensor_data_cVaz_circuito1_recuo_0.6mm.csv", "vazamento_recuo"),
    ("sensor_data_cVaz_circuito2_avanço_0.6mm.csv", "vazamento_avanco"),
    ("sensor_data_cVaz_circuito2_recuo_0.6mm.csv", "vazamento_recuo")
]

# Função para extrair janelas (intervalos) do sinal
def extrair_janelas(signal, tamanho=100, passo=10):
    janelas = []
    for i in range(0, len(signal) - tamanho, passo):
        janelas.append(signal[i:i + tamanho].values)
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

# Converter em DataFrame com TSFEL
df_series = pd.DataFrame({"signal": dados_janelas, "label": rotulos})

# Extração de features com TSFEL
cfg = tsfel.get_features_by_domain()
features = tsfel.time_series_features_extractor(cfg, df_series['signal'], verbose=0)

# Codificar os rótulos
le = LabelEncoder()
y = le.fit_transform(df_series['label'])

# Salvar para uso no AIModelPipeline
features.to_csv("/mnt/data/X_tsfel.csv", index=False)
pd.DataFrame({"label": y}).to_csv("/mnt/data/y_tsfel.csv", index=False)

print("✔️ Dados preparados e salvos: X_tsfel.csv e y_tsfel.csv")
