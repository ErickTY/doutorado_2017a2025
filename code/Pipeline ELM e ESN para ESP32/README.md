# 🤖 Classificação Embarcada com ELM e ESN no ESP32

Este repositório apresenta uma solução completa para implantação de algoritmos de classificação baseados em redes neurais leves — **ELM (Extreme Learning Machine)** e **ESN (Echo State Network)** — embarcados no microcontrolador **ESP32**, com foco em aplicações de manutenção preditiva e IoT industrial.

---

## 🎯 Objetivo

Implementar classificadores eficientes e de baixo custo computacional que possam ser executados localmente no ESP32, utilizando:
- 🧠 **ELM**: rede neural com treinamento instantâneo e inferência leve.
- 🌊 **ESN**: rede recorrente baseada em reservatório com excelente modelagem temporal.

Ambos os modelos são treinados com **features extraídas de sinais de sensores (como pressão)** e implementados com **uso otimizado de memória e tempo de inferência**.

---

## 🗂 Estrutura do Projeto

```
.
├── treinamento/              # Scripts Python de pré-processamento e treino
│   ├── seletor_features.py
│   ├── treinar_elm.py
│   ├── treinar_esn.py
│   └── exportar_para_esp32.py
│
├── firmware_esp32/          # Código C++ para execução embarcada no ESP32
│   ├── classificador_elm.ino
│   ├── classificador_esn.ino
│   └── pesos_elm.h / pesos_esn.h
│
├── datasets/                # Dados simulados ou reais para teste
│   ├── X_cnn.npy
│   ├── labels_encoded.npy
│   └── X_tsfel.csv
│
└── README.md
```

---

## 🔁 Modelos Utilizados

### 🧠 Extreme Learning Machine (ELM)
- Rede neural feedforward com uma camada oculta.
- Os pesos de entrada são aleatórios e fixos.
- O único peso treinado é a saída, via pseudoinversa.
- Vantagens: alta velocidade de treinamento e inferência embarcada simples.

### 🌊 Echo State Network (ESN)
- Rede recorrente com estado interno dinâmico.
- Apenas a saída é treinada.
- Ideal para capturar **padrões temporais em séries de sensores**.
- Vantagens: baixo custo de treinamento, bom desempenho para séries temporais.

---

## ⚙️ Execução no ESP32

- Núcleo 0: responsável pela aquisição e normalização das entradas (pré-processamento).
- Núcleo 1: realiza a classificação usando os pesos carregados e escreve os resultados em um arquivo `.json` ou envia via MQTT/Modbus.

### Comunicação Industrial (opcional):
- ✅ MQTT (comunicador leve em tempo real)
- ✅ Modbus TCP (para CLPs)
- ✅ HTTP REST (integração com APIs)

---

## 📥 Exportação dos Pesos

Após o treinamento em Python:
- `W_elm.csv`, `Wout_elm.csv` → convertidos para `pesos_elm.h`
- `Win_esn.csv`, `W_esn.csv`, `Wout_esn.csv` → convertidos para `pesos_esn.h`

Utilize `scripts/exportar_para_esp32.py` para automatizar a conversão para cabeçalhos C++.

---

## 📊 Resultados Esperados
- Acurácia acima de 95% para problemas de detecção de falhas com features TSFEL.
- Tempo de inferência médio por amostra: `~70 µs` (ELM) e `~70–100 µs` (ESN).
- Executável em dispositivos de baixo consumo e memória limitada.

---

## 📚 Referências
- Huang, G.-B., et al. "Extreme learning machine: theory and applications." *Neurocomputing*, 2006.
- Lukosevicius, M. and Jaeger, H. "Reservoir computing approaches to recurrent neural network training." *Computer Science Review*, 2009.
- Barandas, M., et al. "TSFEL: Time Series Feature Extraction Library." *SoftwareX*, 2020.

