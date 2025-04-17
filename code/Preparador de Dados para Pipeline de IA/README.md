# Preparador de Dados para CNN 1D e IA Clássico (DT, RF e MLP) com Séries Temporais

Este projeto tem como objetivo preparar os dados de sensores de pressão, extraídos de diferentes circuitos (com e sem vazamentos), para uso em modelos de Deep Learning baseados em redes neurais convolucionais (CNN 1D), bem como para extração de atributos com TSFEL para modelos não convolucionais. A preparação inclui extração de janelas normalizadas, extração de atributos e codificação dos rótulos.

---

## 🚀 Objetivo

- Extrair janelas de 100 amostras dos sinais de pressão com passo de 10.
- Aplicar normalização **z-score** individual por janela.
- Codificar os rótulos usando `LabelEncoder`.
- Gerar arquivos `X_cnn.npy`, `y_cnn.npy` e `labels_encoded.npy` para CNN 1D.
- Extrair atributos com TSFEL para uso em modelos clássicos de Machine Learning.

---

## 💻 Execução no Google Colab

### 1. Clone este repositório (ou envie o script para o Colab)

```python
!git clone https://github.com/ErickTY/doutorado2025.git
```
```python
%cd doutorado2025
```

### 2. Instale as bibliotecas necessárias

```python
!pip install pandas numpy scikit-learn tensorflow tsfel
```

### 3. Execute o script `preparar_dados_cnn.py`

```python
%run /content/doutorado2025/code/Preparador\ de\ Dados\ para\ CNN\ 1D/preparar_dados_cnn.py
```

### 4. Executar extração de atributos com TSFEL

```python
import numpy as np
import pandas as pd
import tsfel
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carregar os dados pré-processados
X = np.load("X_cnn.npy")
y_cat = np.load("y_cnn.npy")
y_encoded = np.load("labels_encoded.npy")

# Redimensionar para modelos não convolucionais
X_flat = X.squeeze()  # (amostras, time_steps)

cfg = tsfel.get_features_by_domain()

# Extrair características com TSFEL
X_tsfel = []
for janela in X_flat:
    extractor = tsfel.time_series_features_extractor(cfg, janela, fs=100, verbose=0)
    X_tsfel.append(extractor)

X_tsfel = pd.concat(X_tsfel, ignore_index=True)

# Separar treino e teste
X_train, X_test, y_train, y_test = train_test_split(X_tsfel, y_encoded, test_size=0.2, random_state=42, stratify=y_encoded)

# Padronização para modelos baseados em distância
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## 🔍 Descrição Técnica

- **Entrada**: arquivos CSV contendo sinais de pressão (`Pressure (bar)`)
- **Processo**:
  - Recorte de janelas com tamanho 100 e passo 10
  - Normalização z-score por janela
  - Codificação dos rótulos com `LabelEncoder`
  - Extração de atributos com TSFEL
- **Saída**:
  - `X`: tensor (amostras, 100, 1) para CNN 1D
  - `X_tsfel`: atributos para modelos clássicos
  - `y_cat`: rótulos em one-hot
  - `y_encoded`: vetor de rótulos inteiros

---

## 📁 Estrutura do Projeto

```
.
├── preparar_dados_cnn.py          # Script principal de processamento para CNN
├── X_cnn.npy                      # Dados normalizados prontos para CNN 1D
├── y_cnn.npy                      # Rótulos em one-hot encoding
├── labels_encoded.npy             # Vetor de rótulos codificados
├── X_tsfel.csv (opcional)        # Dados com features TSFEL (se exportado)
├── README.md                      # Este arquivo
```

---

## 🚗 Integração com TensorFlow/Keras

```python
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

X = np.load("X_cnn.npy")
y = np.load("y_cnn.npy")

model = Sequential([
    Conv1D(64, kernel_size=3, activation='relu', input_shape=(X.shape[1], 1)),
    MaxPooling1D(pool_size=2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(y.shape[1], activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)
```

---

## 🚑 Suporte

Em caso de dúvidas, envie uma issue neste repositório ou entre em contato com os desenvolvedores.

---

## ✅ Licença

Este projeto é de uso livre para fins acadêmicos e educacionais.

