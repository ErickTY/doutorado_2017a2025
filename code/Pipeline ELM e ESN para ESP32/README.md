# 🧠 Classificação com ELM no ESP32

Este repositório apresenta uma abordagem completa para treinar e embarcar modelos de classificação usando o algoritmo ELM (Extreme Learning Machine) no microcontrolador ESP32. O pipeline abrange desde a extração de atributos, seleção de features, treinamento do modelo e integração dual-core para inferência em tempo real.

---

## 🎯 Objetivo

Implementar um sistema embarcado inteligente para:
- Detectar padrões em séries temporais (ex: pressão pneumática);
- Executar classificação local via ELM;
- Utilizar dois núcleos do ESP32: um para pré-processamento e outro para inferência;
- Exportar resultados em `.json` e via protocolo industrial (MQTT/Modbus).

---

## 📁 Estrutura do Projeto

```
.
├── treino_modelo/             # Pipeline de treinamento com seleção de features
│   ├── treino_elm.py
│   └── selected_features_idx.npy
│   └── W_elm.csv / Wout.csv / mean.csv / std.csv
├── esp32_firmware/           # Código C++ para Arduino IDE
│   ├── classificador_elm.ino
│   └── pesos_elm.h
├── utils/
│   └── converter_csv_para_h.py
├── README.md
```

---

## 🔁 Pipeline de Treinamento (Python)

1. **Pré-processamento e extração de features** com TSFEL.
2. **Seleção das top 10 features** com Random Forest.
3. **Treinamento do ELM** via MLPClassifier.
4. **Exportação dos pesos** para `.csv`.
5. **Conversão para `.h`** usando `converter_csv_para_h.py`.

---

## ⚙️ Firmware ESP32

- `classificador_elm.ino`:
  - Leitura de dados do sensor;
  - Normalização com Z-Score embarcado;
  - Classificação via ELM;
  - Serial print e exportação JSON.

- `pesos_elm.h`: contém os pesos e parâmetros embarcados.

---

## 🔌 Comunicação
- Resultado da inferência exportado em JSON:
```json
{
  "timestamp": "2025-04-22T14:33:01Z",
  "classe": "vazamento_recuo",
  "probabilities": [0.01, 0.03, 0.02, 0.94]
}
```
- Suporte a MQTT ou Modbus TCP (implementação futura).

---

## 🧪 Exemplo de Uso

1. Execute `treino_elm.py` para gerar pesos otimizados.
2. Execute `converter_csv_para_h.py` para criar `pesos_elm.h`.
3. Compile `classificador_elm.ino` na Arduino IDE.
4. Veja a saída no monitor serial ou exporte para broker MQTT.

---

## 📚 Referências
- Huang et al., "Extreme Learning Machine: Theory and Applications," 2006.
- Barandas et al., "TSFEL: Time Series Feature Extraction Library," SoftwareX, 2020.
- ESP32 Dual Core Programming: https://docs.espressif.com/

---

## ✅ Licença
Este projeto é de uso livre para fins acadêmicos, educacionais e projetos embarcados open-source.

---

Para dúvidas, contribuições ou sugestões, abra uma issue ou envie um pull request 🚀

