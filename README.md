# 📌 Manutenção Prescritiva em Sistemas Eletropneumáticos utilizando Inteligência Artificial

Este repositório contém o código, os datasets e o artigo relacionados à pesquisa de doutorado sobre **Manutenção Prescritiva em Sistemas Eletropneumáticos utilizando Inteligência Artificial**. O estudo envolve a aplicação de **Machine Learning** para análise de falhas em sistemas industriais.

## 📂 Estrutura do Repositório

```plaintext
📦 NomeDoRepositorio
 ├── 📁 docs/               # Documentação geral
 │   ├── artigo_publicado.pdf   # Artigo publicado na conferência
 │   ├── metodologia.md    # Metodologia utilizada na pesquisa
 │   ├── referencias.md    # Referências bibliográficas
 │   ├── cronograma.md     # Planejamento das atividades
 │
 ├── 📁 datasets/         # Dados coletados nos circuitos eletropneumáticos
 │   ├── sensor_data_cVaz_circuito1_avanço_0.6mm.csv
 │   ├── sensor_data_cVaz_circuito1_recuo_0.6mm.csv
 │   ├── sensor_data_cVaz_circuito2_avanço_0.6mm.csv
 │   ├── sensor_data_cVaz_circuito2_recuo_0.6mm.csv
 │   ├── sensor_data_sVaz_circuito1.csv
 │   ├── sensor_data_sVaz_circuito2.csv
 │   ├── sensor_data_sVaz_circuito31_coleta1.csv
 │   ├── sensor_data_sVaz_circuito31_coleta2.csv
 │   ├── sensor_data_sVaz_circuito32_coleta1.csv
 │   ├── sensor_data_sVaz_circuito32_coleta2.csv
 │
 ├── 📁 code/             # Códigos e experimentos
 │   ├── codigo_doutorado_tsfel_pycaret.ipynb  # Jupyter Notebook com o código principal
 │
 ├── README.md            # Apresentação do repositório
 ├── LICENSE              # Licença do projeto
 ├── .gitignore           # Arquivos a serem ignorados pelo Git
 ```

## 📜 Descrição dos Arquivos

- **`docs/artigo_publicado.pdf`**: Artigo publicado apresentando os resultados do estudo.
- **`datasets/`**: Contém os dados coletados dos sensores em diferentes circuitos eletropneumáticos.
- **`code/codigo_doutorado_tsfel_pycaret.ipynb`**: Notebook com a implementação dos algoritmos de Machine Learning, extração de features com TSFEL e modelagem com PyCaret.

## 📊 Principais Resultados
- Foram extraídas **200 características** dos dados usando **TSFEL**.
- Modelos testados:
  - **Random Forest**: Melhor desempenho, com acurácia de **96,83% no treino** e **94,06% no teste**.
  - **Decision Tree**: Acurácia de **92,30% no teste**.
  - **MLP**: Desempenho abaixo dos outros modelos.
- O estudo mostrou que **modelos baseados em árvores (RF e DT) são os mais adequados para classificação de falhas**.

## 🚀 Como Executar o Projeto
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o notebook `code/codigo_doutorado_tsfel_pycaret.ipynb` para reproduzir os resultados.

## 📌 Referências
- TSFEL: [Time Series Feature Extraction Library](https://doi.org/10.1016/j.softx.2020.100387)
- PyCaret: [Documentação Oficial](https://pycaret.gitbook.io/docs)
- FluidSIM: Software utilizado para simulação dos circuitos.

---
Este repositório é parte do doutorado no programa de pós-graduação em engenharia da informação da **Universidade Federal do ABC (UFABC)**. Para mais informações, entre em contato: **erick.yamamoto@ufabc.edu.br**.

📢 Se você achou este projeto útil, deixe uma ⭐ no repositório!
