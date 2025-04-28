# README.md - Deploy do Projeto ESP32_Model_Deployment

## 🚀 Visão Geral
Este projeto permite:
- Leitura de um sensor de pressão analógico.
- Pré-processamento com normalização z-score.
- Classificação de estado normal ou vazamento via ELM ou ESN.
- Alarme com LED e Buzzer em caso de vazamento detectado.
- Uso de dois núcleos do ESP32 para processamento paralelo.

---

## 📚 Estrutura do Projeto

```
ESP32_Model_Deployment/
├── include/
│   ├── features.h
│   ├── normalization.h
│   ├── elm_model.h
│   └── esn_model.h
├── src/
│   └── main_elm_esn_example.ino
├── data/
│   └── model_config.json (opcional)
├── platformio.ini
└── README.md
```

---

## ⚙️ Configurações Iniciais

### Definições no Código
```cpp
#define LOAD_MODEL_FROM_FLASH 1 // 1 = carregar .h, 0 = carregar model_config.json
#define MODEL_TYPE "ELM"         // "ELM" ou "ESN"

#define SENSOR_PIN 34            // Pino de leitura analógica
#define LED_PIN 2                // Pino do LED de alarme
#define BUZZER_PIN 15            // Pino do Buzzer
```

### Configuração do PlatformIO (`platformio.ini`)
```ini
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200
upload_speed = 921600
```

---

## 🔄 Fluxo de Deploy

1. **Importar o projeto** no PlatformIO.
2. **Verificar porta** do ESP32 (`COMx` ou `/dev/ttyUSBx`).
3. **Build** ✅ e **Upload** ➡️.
4. **Abrir Serial Monitor** para acompanhar a execução.
5. **Testar o sensor**:
   - Sem vazamento: LED/Buzzer desligados.
   - Com vazamento: LED acende e Buzzer apita.

---

## 🔍 Funções Importantes

- `normalize_input()` - Aplica normalização z-score nas features.
- `predict_model()` - Decide entre `predict_elm()` ou `predict_esn()`.
- `PreProcessTask()` - Lê sensor e monta janela de amostras.
- `ClassifyTask()` - Classifica e aciona alarmes.

---

## 🔄 Atualização do Modelo OTA (Opcional)

1. Coloque `model_config.json` na pasta `data/`.
2. Use `Upload File System Image` do PlatformIO.
3. Mude no código para carregar do arquivo:
```cpp
#define LOAD_MODEL_FROM_FLASH 0
```

---

## 📚 Checklist de Teste

- [ ] Upload realizado com sucesso
- [ ] Sensor respondendo no Serial Monitor
- [ ] LED e Buzzer funcionando em casos de vazamento
- [ ] Mudança de MODEL_TYPE testada ("ELM" / "ESN")
- [ ] (Opcional) model_config.json carregado via SPIFFS

---

## 🔍 Futuras Melhorias
- Integração com MQTT
- Criação de um WebServer de status
- Atualização automática de modelos via rede
- Otimização da filtragem e extração de features

---

# 📈 Status: Pronto para Deploy!

Deploy realizado corretamente no ESP32! ✨

---
