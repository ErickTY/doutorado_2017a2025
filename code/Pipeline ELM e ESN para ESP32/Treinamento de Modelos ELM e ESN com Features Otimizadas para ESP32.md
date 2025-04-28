# Treinamento de Modelos ELM e ESN com Features Otimizadas para ESP32

Este repositório descreve passo a passo como treinar classificadores leves (ELM e ESN) com features selecionadas, visando a futura implantação embarcada no ESP32. O processo contempla seleção de atributos, normalização, treino e exportação dos parâmetros do modelo.

---

## 🧠 Etapa 1 – Pré-requisitos

Instale as dependências básicas:
```bash
pip install numpy pandas scikit-learn matplotlib
```
Opcional para ESN:
```bash
pip install git+https://github.com/cknd/pyESN.git
```

---

## 📂 Etapa 2 – Carregamento dos Dados
```python
import numpy as np
X = np.load("X_cnn.npy").squeeze()        # shape: (amostras, time_steps)
y = np.load("labels_encoded.npy")         # shape: (amostras,)
```

---

## 📊 Etapa 3 – Seleção das Top 10 Features com Random Forest
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_scaled, y)

importances = rf.feature_importances_
top_idx = np.argsort(importances)[-10:]
X_selected = X_scaled[:, top_idx]

np.save("selected_features_idx.npy", top_idx)  # salvar para embarcar no ESP32
```

---

## 🔁 Etapa 4 – Treinamento com MLP (Simulação do ELM)
```python
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, stratify=y)
mlp = MLPClassifier(hidden_layer_sizes=(10,), max_iter=300, random_state=42)
mlp.fit(X_train, y_train)
print(classification_report(y_test, mlp.predict(X_test)))
```

---

## ⚡ Etapa 5 – Treinamento com ESN (Opcional)
```python
from pyESN import ESN

esn = ESN(n_inputs=10, n_outputs=len(np.unique(y)), n_reservoir=200, sparsity=0.1, random_state=42)
y_onehot = np.eye(len(np.unique(y)))[y_train]
esn.fit(X_train, y_onehot)

pred = esn.predict(X_test)
y_pred = np.argmax(pred, axis=1)
print(classification_report(y_test, y_pred))
```

---

## 💾 Etapa 6 – Exportação dos Pesos para Embedding no ESP32
```python
np.savetxt("W_elm.csv", mlp.coefs_[0], delimiter=",")     # pesos da entrada para camada oculta
np.savetxt("Wout_elm.csv", mlp.coefs_[1], delimiter=",")  # pesos da camada oculta para saída
np.savetxt("means.csv", scaler.mean_[top_idx], delimiter=",")
np.savetxt("stds.csv", scaler.scale_[top_idx], delimiter=",")
```
Para o ESN:
```python
np.savetxt("Win_esn.csv", esn.Win, delimiter=",")
np.savetxt("W_esn.csv", esn.W, delimiter=",")
np.savetxt("Wout_esn.csv", esn.Wout, delimiter=",")
```

---

## ✅ Conclusão
Este pipeline reduz a dimensionalidade dos dados com base na importância das features, o que permite a execução eficiente do modelo ELM ou ESN no ESP32. Os arquivos exportados em `.csv` poderão ser convertidos para `.h` e integrados ao firmware da aplicação embarcada.

