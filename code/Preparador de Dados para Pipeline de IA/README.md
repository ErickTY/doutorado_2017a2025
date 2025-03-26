# Preparar Dados para AIModelPipeline - README

Este repositório contém um script Python que prepara dados de sensores de pressão, coletados em diferentes circuitos com e sem vazamentos, para posterior uso em um pipeline de modelos de inteligência artificial (IA).

A preparação inclui:
- Leitura dos arquivos CSV de sensores
- Extração de janelas de tempo (slices)
- Extração de atributos com a biblioteca **TSFEL**
- Geração dos arquivos `X_tsfel.csv` (features) e `y_tsfel.csv` (rótulos) para treinamento e análise com o `AIModelPipeline`

---

## 🚀 Como Executar no Google Colab

### 1. Suba os arquivos CSV para o ambiente do Colab:

Inclua os seguintes arquivos no diretório do Colab (via upload ou Google Drive):
- `sensor_data_sVaz_circuito1.csv`
- `sensor_data_sVaz_circuito2.csv`
- `sensor_data_sVaz_circuito31_coleta1.csv`
- `sensor_data_sVaz_circuito31_coleta2.csv`
- `sensor_data_sVaz_circuito32_coleta1.csv`
- `sensor_data_sVaz_circuito32_coleta2.csv`
- `sensor_data_cVaz_circuito1_avanço_0.6mm.csv`
- `sensor_data_cVaz_circuito1_recuo_0.6mm.csv`
- `sensor_data_cVaz_circuito2_avanço_0.6mm.csv`
- `sensor_data_cVaz_circuito2_recuo_0.6mm.csv`

### 2. Instale as bibliotecas necessárias:
```python
!pip install tsfel
!pip install scikit-learn pandas
```

### 3. Execute o script `preparar_dados_pipeline.py`:
Copie o conteúdo do script e cole em uma célula do Colab. O script:
- Carrega os arquivos
- Divide os sinais em janelas de 100 amostras
