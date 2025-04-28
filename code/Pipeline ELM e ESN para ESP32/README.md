# ESP32_Model_Deployment

## Visão Geral
Projeto para realizar inferência de detecção de vazamentos em sistemas pneumáticos usando um ESP32:
- Lê dados de um sensor analógico de pressão.
- Faz pré-processamento (normalização z-score).
- Classifica usando ELM ou ESN.
- Rodando com tarefas separadas nos núcleos 0 e 1.

---

## Estrutura de Pastas

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
│   └── model_config.json
├── platformio.ini
└── README.md
```

---

## Dependências
- ESP32 Board (na Arduino IDE ou PlatformIO)
- Biblioteca padrão do ESP32 (analogRead, Serial, etc)

---

## Configurações Principais

### Definições no código:
```cpp
#define LOAD_MODEL_FROM_FLASH 1 // 1 = carregar de .h; 0 = carregar de model_config.json
#define MODEL_TYPE "ELM" // "ELM" ou "ESN"

#define SENSOR_PIN 34
#define LED_PIN 2
#define BUZZER_PIN 15
```

- **LOAD_MODEL_FROM_FLASH**: Define se vai usar os pesos embarcados nos headers ou carregar dinamicamente.
- **MODEL_TYPE**: Escolhe qual modelo usar na inferência ("ELM" ou "ESN").


### Tarefas nos Núcleos:
- **Core 0**: Lê sensor e normaliza
- **Core 1**: Classifica e aciona alarmes


---

## Funções Principais

- `normalize_input(window[], normalized_output[])`
  - Aplica z-score utilizando as médias e desvios salvos.

- `predict_model(normalized_input[], model_type)`
  - Chama `predict_elm()` ou `predict_esn()` baseado no tipo escolhido.

- `PreProcessTask()`
  - Captura sensor, monta janela de 100 amostras, normaliza.

- `ClassifyTask()`
  - Classifica usando o modelo selecionado, aciona LED e Buzzer em caso de vazamento.


---

## Exemplo de Uso

```cpp
// Dentro da tarefa de classificacao
float resultado = predict_model(input_normalized, MODEL_TYPE);
int classe_prevista = (int)resultado;

if (classe_prevista == VAZAMENTO_AVANCO || classe_prevista == VAZAMENTO_RECUO) {
  digitalWrite(LED_PIN, HIGH);
  tone(BUZZER_PIN, 1000);
} else {
  digitalWrite(LED_PIN, LOW);
  noTone(BUZZER_PIN);
}
```


---

## Observações
- O sensor deve estar corretamente calibrado para gerar pressão entre 0 e 12 bar.
- A leitura é feita via `analogRead()` considerando resolução de 12 bits.
- Para atualizações de modelo futuras, basta trocar o `model_config.json` e recarregar no SPIFFS.


---

## Futuras Expansões
- Atualização OTA automática de modelos
- Adição de WebServer para monitoramento
- Integração com MQTT para alertas remotos
