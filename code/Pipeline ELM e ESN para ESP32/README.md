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
│   ├── features.h         // Lista de features selecionadas
│   ├── normalization.h    // Vetores de médias e desvios padrão
│   ├── elm_model.h        // Pesos do modelo ELM
│   └── esn_model.h        // Pesos do modelo ESN
├── src/
│   └── main_elm_esn_example.ino // Código principal
├── data/
│   └── model_config.json  // Arquivo de modelo para OTA
├── platformio.ini            // Configuração para PlatformIO
└── README.md                  // Este documento
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
#define MODEL_TYPE "ELM"         // "ELM" ou "ESN"

#define SENSOR_PIN 34            // Pino do sensor analógico
#define LED_PIN 2                // LED de aviso de vazamento
#define BUZZER_PIN 15            // Buzzer de aviso sonoro
```

- **LOAD_MODEL_FROM_FLASH**: Define se vai usar os pesos embarcados nos headers ou carregar dinamicamente.
- **MODEL_TYPE**: Escolhe qual modelo usar na inferência ("ELM" ou "ESN").


### Tarefas nos Núcleos:
- **Core 0**: Lê sensor e normaliza
- **Core 1**: Classifica e aciona alarmes


---

## Funções Principais

- `normalize_input(window[], normalized_output[])`
  - Aplica z-score utilizando as médias e desvios salvos para cada feature.

- `predict_model(normalized_input[], model_type)`
  - Encaminha a inferência para o ELM ou ESN conforme o modelo escolhido.

- `PreProcessTask()`
  - Lê valores do sensor, monta a janela de 100 amostras e normaliza os dados.

- `ClassifyTask()`
  - Utiliza os dados normalizados para realizar classificação e acionar LED/Buzzer se vazamento for detectado.


---

## Exemplo de Uso

```cpp
// Dentro da tarefa de classificacao
float resultado = predict_model(input_normalized, MODEL_TYPE);
int classe_prevista = (int)resultado;

if (classe_prevista == VAZAMENTO_AVANCO || classe_prevista == VAZAMENTO_RECUO) {
  digitalWrite(LED_PIN, HIGH);  // Liga o LED
  tone(BUZZER_PIN, 1000);       // Liga o buzzer
} else {
  digitalWrite(LED_PIN, LOW);   // Desliga o LED
  noTone(BUZZER_PIN);           // Desliga o buzzer
}
```


---

## Observações
- O sensor deve estar corretamente calibrado para gerar pressão entre 0 e 12 bar.
- A leitura é feita via `analogRead()` considerando resolução de 12 bits.
- Para atualizações de modelo futuras, basta trocar o `model_config.json` e recarregar no SPIFFS.


---

## Futuras Expansões
- Atualização OTA automática de modelos.
- Adição de WebServer para monitoramento em tempo real.
- Integração com MQTT para alertas remotos.
- Otimização de pré-processamento local adaptando TSFEL em C++.
