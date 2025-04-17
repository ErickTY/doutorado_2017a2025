# Preparador de Dados para CNN 1D com Séries Temporais

Este projeto tem como objetivo preparar os dados de sensores de pressão, extraídos de diferentes circuitos (com e sem vazamentos), para uso em modelos de Deep Learning baseados em redes neurais convolucionais (CNN 1D). A preparação inclui extração de janelas normalizadas dos sinais e codificação dos rótulos, com exportação dos dados em formato `.npy`.

---

## 🚀 Objetivo

- Extrair janelas de 100 amostras dos sinais de pressão com passo de 10.
- Aplicar normalização **z-score** individual por janela.
- Codificar os rótulos usando `LabelEncoder`.
- Gerar arquivos `X_cnn.npy`, `y_cnn.npy` e `labels_encoded.npy` prontos para treinamento de CNN 1D.

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
!pip install pandas numpy scikit-learn tensorflow
```

### 3. Execute o script `preparar_dados_cnn.py`

```python
%run /content/doutorado2025/code/Preparador\ de\ Dados\ para\ CNN\ 1D/preparar_dados_cnn.py
```

Isso irá gerar três arquivos:
- `X_cnn.npy`: Dados de entrada para CNN com shape (amostras, time steps, 1)
- `y_cnn.npy`: Rótulos codificados em one-hot encoding
- `labels_encoded.npy`: Vetor com os rótulos inteiros codificados

---

## 🔍 Descrição Técnica

- **Entrada**: arquivos CSV contendo sinais de pressão (`Pressure (bar)`)
- **Processo**:
  - Recorte de janelas com tamanho 100 e passo 10
  - Normalização z-score por janela
  - Codificação dos rótulos com `LabelEncoder`
- **Saída**:
  - `X`: tensor (amostras, 100, 1) prontos para CNN 1D
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
