# AI Model Pipeline - README

Este repositório contém uma classe Python que implementa um pipeline completo de pré-processamento e treinamento de modelos de Inteligência Artificial (IA), incluindo redes neurais, árvores de decisão, modelos ensemble, e modelos avançados como Extreme Learning Machine (ELM) e Echo State Network (ESN).

---

## 🔧 Funcionalidades

### 📉 Pré-processamento:

| Técnica                  | Método Aplicado                        | Objetivo |
|---------------------------|------------------------------------------|---------|
| **Normalização**          | `MinMaxScaler()`                         | Escala os dados para o intervalo [0,1] |
| **PCA**                   | `PCA(n_components=n)`                    | Reduz a dimensionalidade mantendo a maior variância |
| **Importância de Features**| `RandomForestClassifier().feature_importances_` | Mede a relevância de cada atributo |
| **Extração de Features** | `SelectKBest(score_func=f_classif, k=k)` | Seleciona as *k* melhores features com ANOVA F |

### 🧠 Modelos de IA:

| Modelo                  | Método | Descrição |
|-------------------------|--------|-----------|
| **MLP (Rede Neural)**   | `train_mlp()` | Rede com camadas ocultas (classificação geral) |
| **Árvore de Decisão (DT)** | `train_dt()` | Modelo baseado em regras if-then |
| **Random Forest (RF)**  | `train_rf()` | Conjunto de árvores para melhorar performance |
| **RNA RAM**             | `train_ram()` | Simula rede baseada em RAM com baixa profundidade |
| **ELM**                 | `train_elm()` | Rede neural com camada única e pesos aleatórios |
| **ESN**                 | `train_esn()` | Rede neural recorrente com reservatório fixo |

---

## 🔍 Observação sobre Feature Importance e Feature Extraction

### Feature Importance e Feature Extraction são pré-processamentos ou análise exploratória?

#### 🔹 Feature Importance
- É usada para medir a relevância de variáveis para predição.
- Pode ser:
  - **Análise exploratória**: quando usada para interpretar e compreender os dados.
  - **Pré ou pós-processamento**: quando os resultados são usados para ajustar o modelo (ex: eliminar variáveis).

#### 🔹 Feature Extraction
- Cria novas variáveis a partir das existentes (ex: PCA).
- É classificada como:
  - **Pré-processamento**: altera os dados antes do treinamento do modelo.
  - Raramente é considerada parte da análise exploratória (exceto para visualização dimensional).

#### 📄 Resumo

| Técnica             | EDA? | Pré-processamento? | Pós-processamento? |
|---------------------|------|----------------------|--------------------|
| Feature Importance  | ✅  | ✅                   | ✅                 |
| Feature Extraction  | ❌  | ✅                   | ❌                 |

---

## ⚖️ Requisitos

```bash
pip install numpy pandas scikit-learn hpelm easyesn
```

Obs: Se não for utilizar ELM ou ESN, pode remover `hpelm` e `easyesn`.

---

## 📚 Como Usar

```python
from sklearn.datasets import load_iris
from ai_pipeline import AIModelPipeline

# Carregar dataset
data = load_iris()
X, y = data.data, data.target

# Criar pipeline
pipeline = AIModelPipeline(X, y)

# Etapas de pré-processamento
pipeline.normalize()
pipeline.apply_pca(n_components=3)
pipeline.feature_importance()
pipeline.feature_extraction(k=3)

# Treinamento dos modelos
pipeline.train_mlp()
pipeline.train_dt()
pipeline.train_rf()
pipeline.train_elm()
pipeline.train_esn()
pipeline.train_ram()

# Sumário de resultados
pipeline.summary()
```

---

## 🌐 Estrutura do Projeto

```
.
├── ai_pipeline.py       # Classe principal com pré-processamentos e modelos
├── codigo_doutorado_tsfel_pycaret.ipynb  # Jupyter Notebook com o código principal
├── README.md            # Este arquivo
```

---

## 🚀 Objetivo

Este projeto visa fornecer uma ferramenta simples e modular para experimentação com diferentes técnicas de pré-processamento e modelos de IA, sendo útil para fins educacionais e prototipagem rápida.

---

## ✅ Licença

Este projeto é de uso livre para fins acadêmicos e educacionais.

---

## 🚑 Suporte

Para dúvidas, entre em contato via [Issues](https://github.com/seu-usuario/seu-repositorio/issues) ou envie um pull request!


