# Preparador de Dados para Pipeline de IA

Este repositório contém um script Python que realiza o pré-processamento de dados brutos de sensores de pressão para aplicação em modelos de Inteligência Artificial, como MLP, Random Forest, ELM, ESN, entre outros.

Os dados correspondem a leituras de sensores em diferentes circuitos pneumáticos ou hidráulicos, com e sem vazamentos, capturando eventos de avanço e recuo dos atuadores.

---

## 🔧 Funcionalidades do Script

- Leitura de arquivos CSV contendo sinais de pressão.
- Extração de janelas temporais de tamanho fixo.
- Etiquetagem de cada janela com base na origem do dado (normal, vazamento avanço, vazamento recuo).
- Extração de atributos com **TSFEL** (Time Series Feature Extraction Library).
- Codificação dos rótulos com `LabelEncoder`.
- Gera dois arquivos de saída:
  - `X_tsfel.csv`: atributos extraídos.
  - `y_tsfel.csv`: rótulos correspondentes.

---

## 🚀 Objetivo

O objetivo é transformar os dados brutos de sensores em um conjunto estruturado de atributos que possa ser usado diretamente no `AIModelPipeline` para tarefas como classificação, detecção de anomalias ou clustering.

---

## 🔍 Detalhes do Processo

### 1. **Arquivos de Entrada**

Os arquivos devem conter ao menos a coluna:
```
"Pressure (bar)"
```

### 2. **Extração de Janelas**

Cada sinal é dividido em janelas de 100 amostras com passo de 10:
```python
extrair_janelas(signal, tamanho=100, passo=10)
```

### 3. **Extração de Atributos com TSFEL**

TSFEL é utilizado para extrair atributos no domínio do tempo, frequência e estatística.

```python
cfg = tsfel.get_features_by_domain()
tsfel.time_series_features_extractor(cfg, lista_de_sinais)
```

### 4. **Codificação de Rótulos**

```python
LabelEncoder().fit_transform(rotulos)
```

### 5. **Saídas**

- `X_tsfel.csv`: matriz de atributos para cada janela.
- `y_tsfel.csv`: vetor com rótulos (ex: 0=normal, 1=vazamento avanço, 2=vazamento recuo).

---

## 🌐 Estrutura do Projeto

```
.
├── preparar_dados_pipeline.py    # Script de extração e preparo dos dados
├── X_tsfel.csv                   # Atributos extraídos
├── y_tsfel.csv                   # Rótulos codificados
├── README.md                     # Este documento
```

---

## 🚑 Requisitos

```bash
pip install pandas tsfel scikit-learn
```

---

## ✅ Uso

```bash
python preparar_dados_pipeline.py
```

Ao executar, os arquivos `X_tsfel.csv` e `y_tsfel.csv` serão gerados e poderão ser utilizados diretamente no `AIModelPipeline`.

---

## 📅 Autor

Projeto elaborado para estudos de IA aplicada a sinais de sensores com foco em detecção de vazamentos.

---

## 💪 Contribuições

Sugestões, melhorias ou novos tipos de sensores são bem-vindos via Pull Request ou Issues.

---

