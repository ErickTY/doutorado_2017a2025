import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical

# Caminho base dos arquivos
base_path = './datasets/'

# Lista de arquivos e seus rótulos
arquivos = [
    ("sensor_data_sVaz_circuito2.csv", "normal"),
    ("sensor_data_cVaz_circuito2_avanço_0.6mm.csv", "vazamento_avanco"),
    ("sensor_data_cVaz_circuito2_recuo_0.6mm.csv", "vazamento_recuo")
]

# Parâmetros de janela
tamanho_janela = 100
passo = 10

# Função para extrair janelas com normalização z-score
def extrair_janelas(signal, tamanho=100, passo=10, rotulo=""):
    janelas = []
    rotulos_janela = []
    for i in range(0, len(signal) - tamanho, passo):
        janela = signal[i:i + tamanho].values.flatten()
        # Normalização z-score por janela
        if np.std(janela) > 0:
            janela = (janela - np.mean(janela)) / np.std(janela)
        else:
            janela = np.zeros_like(janela)  # Prevenir divisão por zero
        janelas.append(janela)
        rotulos_janela.append(rotulo)
    return janelas, rotulos_janela

# Listas para armazenar os dados
dados_janelas = []
rotulos = []

# Loop para processar os arquivos
for nome_arquivo, rotulo in arquivos:
    caminho = os.path.join(base_path, nome_arquivo)
    df = pd.read_csv(caminho)

    if "Pressure (bar)" not in df.columns:
        print(f"Coluna 'Pressure (bar)' não encontrada em {nome_arquivo}")
        continue

    janelas, rotulos_janela = extrair_janelas(df["Pressure (bar)"], tamanho_janela, passo, rotulo)
    dados_janelas.extend(janelas)
    rotulos.extend(rotulos_janela)

# Converter para array e formato CNN 1D
X = np.array(dados_janelas)
X = X[:, :, np.newaxis]  # shape (amostras, time steps, 1)

# Codificar rótulos
le = LabelEncoder()
y_encoded = le.fit_transform(rotulos)
y_cat = to_categorical(y_encoded)

# Exibir resultados
print("Shape X:", X.shape)
print("Shape y (categorical):", y_cat.shape)
print("Classes:", le.classes_)

# Salvar para reuso
np.save("X_cnn.npy", X)
np.save("y_cnn.npy", y_cat)
np.save("labels_encoded.npy", y_encoded)
