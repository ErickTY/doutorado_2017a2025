# Preparador de Dados para Pipeline de IA com Séries Temporais

Este projeto tem como objetivo preparar os dados de sensores de pressão, extraídos de diferentes circuitos (com e sem vazamentos), para uso em um pipeline de Inteligência Artificial (AIModelPipeline). A preparação inclui extração de janelas, extração de atributos e exportação final de dados prontos para modelagem.

---

## 🚀 Objetivo

- Extrair janelas de 100 amostras dos sinais de pressão.
- Usar a biblioteca **TSFEL** para extrair atributos estatísticos, temporais e espectrais dessas janelas.
- Gerar arquivos `X_tsfel.csv` e `y_tsfel.csv` prontos para serem utilizados no `AIModelPipeline`.

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
!pip install tsfel
```

### 3. Execute o script `preparar_dados_pipeline.py`

```python
%run /content/doutorado2025/code/Preparador\ de\ Dados\ para\ Pipeline\ de\ IA/preparar_dados_pipeline.py
```

Isso irá gerar dois arquivos:
- `X_tsfel.csv`: Dados de entrada com atributos extraídos
- `y_tsfel.csv`: Rótulos codificados (normal ou vazamento)

---

## 🔍 Descrição Técnica

- **Entrada**: arquivos CSV contendo sinais de pressão (`Pressure (bar)`)
- **Processo**:
  - Recorte de janelas com tamanho 100 e passo 10
  - Extração de atributos com TSFEL (automática por domínio)
  - Codificação dos rótulos com `LabelEncoder`
- **Saída**:
  - DataFrame `X` com atributos para modelagem
  - Vetor `y` com classes (0 = normal, 1 = vazamento)

---

## 📁 Estrutura do Projeto

```
.
├── preparar_dados_pipeline.py     # Script principal de processamento
├── X_tsfel.csv                    # Dados prontos com features extraídas
├── y_tsfel.csv                    # Rótulos codificados
├── README.md                      # Este arquivo
```

---

## ✅ Exemplo de Integração com AIModelPipeline

```python
import pandas as pd
from ai_pipeline import AIModelPipeline

X = pd.read_csv("X_tsfel.csv")
y = pd.read_csv("y_tsfel.csv")["label"]

pipeline = AIModelPipeline(X, y)
pipeline.normalize()
pipeline.apply_pca(n_components=5)
pipeline.feature_extraction(k=10)
pipeline.train_rf()
pipeline.train_mlp()
pipeline.summary()
```

---

## 🚑 Suporte

Em caso de dúvidas, envie uma issue neste repositório ou entre em contato com os desenvolvedores.

---

## ✅ Licença

Este projeto é de uso livre para fins acadêmicos e educacionais.

