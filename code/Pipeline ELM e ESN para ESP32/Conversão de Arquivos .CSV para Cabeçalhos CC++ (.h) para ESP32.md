# Conversão de Arquivos .CSV para Cabeçalhos C/C++ (.h) para ESP32

Este guia explica como converter os arquivos `.csv` contendo pesos treinados de modelos ELM (ou ESN) para arquivos `.h` compatíveis com projetos C/C++ no ESP32, especialmente quando utilizados no Arduino IDE ou com ESP-IDF.

---

## 📦 Arquivos de entrada
- `W_elm.csv`: matriz de pesos da entrada para a camada oculta – shape: `[HIDDEN][FEATURES]`
- `Wout_elm.csv`: matriz da camada oculta para a saída – shape: `[CLASSES][HIDDEN]`
- `means.csv` e `stds.csv`: médias e desvios padrão para normalização Z-score – shape: `[FEATURES]`

Exemplo de conteúdo de um `W_elm.csv`:
```csv
0.52,-0.41,0.23,...
-0.16,0.88,-0.05,...
...
```

---

## 🛠️ Etapa 1 – Conversão com Python

Use o script abaixo para gerar um `.h` estruturado contendo os arrays de pesos em formato `float`:

```python
import numpy as np

# Carregar os arquivos CSV
W = np.loadtxt("W_elm.csv", delimiter=",")
Wout = np.loadtxt("Wout_elm.csv", delimiter=",")
mean = np.loadtxt("means.csv", delimiter=",")
std = np.loadtxt("stds.csv", delimiter=",")

with open("pesos_elm.h", "w") as f:
    f.write("#ifndef PESOS_ELM_H\n#define PESOS_ELM_H\n\n")
    f.write(f"#define FEATURES {W.shape[1]}\n")
    f.write(f"#define HIDDEN {W.shape[0]}\n")
    f.write(f"#define CLASSES {Wout.shape[0]}\n\n")

    def write_array(name, array):
        f.write(f"const float {name}[{array.shape[0]}][{array.shape[1]}] = {{\n")
        for row in array:
            f.write("  {" + ", ".join(f"{v:.6f}" for v in row) + "},\n")
        f.write("};\n\n")

    write_array("W", W)
    write_array("Wout", Wout)

    f.write(f"const float mean[FEATURES] = {{ {', '.join(f'{v:.6f}' for v in mean)} }};\n")
    f.write(f"const float stddev[FEATURES] = {{ {', '.join(f'{v:.6f}' for v in std)} }};\n")
    f.write("\n#endif // PESOS_ELM_H\n")
```

---

## 📁 Resultado gerado – exemplo do `.h`
```cpp
#define FEATURES 10
#define HIDDEN 10
#define CLASSES 4

const float W[10][10] = {
  {0.52, -0.41, ...},
  {-0.16, 0.88, ...},
  ...
};

const float Wout[4][10] = {
  {0.32, -0.91, ...},
  ...
};

const float mean[FEATURES] = {0.34, 0.76, ...};
const float stddev[FEATURES] = {0.23, 0.41, ...};
```

---

## ✅ Dicas finais
- Substitua `float` por `PROGMEM` se quiser armazenar os dados na Flash do ESP32;
- Certifique-se de usar `#include "pesos_elm.h"` no sketch principal;
- Utilize `normalize_input()` para aplicar `Z-score` aos dados de entrada antes da inferência.
