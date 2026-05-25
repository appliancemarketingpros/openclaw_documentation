---
title: Метрики Prometheus
source_url: https://docs.openclaw.ai/uk/gateway/prometheus
scraped_at: 2026-05-25
---

OpenClaw може надавати діагностичні метрики через офіційний Plugin `diagnostics-prometheus`. Він слухає довірені внутрішні діагностичні події та формує текстову кінцеву точку Prometheus за адресою:

textCopy code
[code]
    GET /api/diagnostics/prometheus
[/code]

Тип вмісту: `text/plain; version=0.0.4; charset=utf-8`, стандартний формат експозиції Prometheus.

Для трасувань, журналів, OTLP push та семантичних атрибутів OpenTelemetry GenAI див. [експорт OpenTelemetry](</uk/gateway/opentelemetry>).

## Швидкий старт

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/diagnostics-prometheus
[/code]

* ### Enable the plugin

### Config

json5Copy code
[code]
    {  plugins: {    allow: ["diagnostics-prometheus"],    entries: {      "diagnostics-prometheus": { enabled: true },    },  },  diagnostics: {    enabled: true,  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw plugins enable diagnostics-prometheus
[/code]

* ### Restart the Gateway

HTTP-маршрут реєструється під час запуску Plugin, тому перезавантажте після ввімкнення.

* ### Scrape the protected route

Надішліть ту саму автентифікацію Gateway, яку використовують ваші клієнти оператора:

bashCopy code
[code]
    curl -H "Authorization: Bearer $OPENCLAW_GATEWAY_TOKEN" \  http://127.0.0.1:18789/api/diagnostics/prometheus
[/code]

* ### Wire Prometheus

yamlCopy code
[code]
    # prometheus.ymlscrape_configs:  - job_name: openclaw    scrape_interval: 30s    metrics_path: /api/diagnostics/prometheus    authorization:      credentials_file: /etc/prometheus/openclaw-gateway-token    static_configs:      - targets: ["openclaw-gateway:18789"]
[/code]

## Експортовані метрики

Метрика | Тип | Мітки  
---|---|---  
`openclaw_run_completed_total` | counter | `channel`, `model`, `outcome`, `provider`, `trigger`  
`openclaw_run_duration_seconds` | histogram | `channel`, `model`, `outcome`, `provider`, `trigger`  
`openclaw_model_call_total` | counter | `api`, `error_category`, `model`, `outcome`, `provider`, `transport`  
`openclaw_model_call_duration_seconds` | histogram | `api`, `error_category`, `model`, `outcome`, `provider`, `transport`  
`openclaw_model_tokens_total` | counter | `agent`, `channel`, `model`, `provider`, `token_type`  
`openclaw_gen_ai_client_token_usage` | histogram | `model`, `provider`, `token_type`  
`openclaw_model_cost_usd_total` | counter | `agent`, `channel`, `model`, `provider`  
`openclaw_tool_execution_total` | counter | `error_category`, `outcome`, `params_kind`, `tool`  
`openclaw_tool_execution_duration_seconds` | histogram | `error_category`, `outcome`, `params_kind`, `tool`  
`openclaw_harness_run_total` | counter | `channel`, `error_category`, `harness`, `model`, `outcome`, `phase`, `plugin`, `provider`  
`openclaw_harness_run_duration_seconds` | histogram | `channel`, `error_category`, `harness`, `model`, `outcome`, `phase`, `plugin`, `provider`  
`openclaw_message_processed_total` | counter | `channel`, `outcome`, `reason`  
`openclaw_message_processed_duration_seconds` | histogram | `channel`, `outcome`, `reason`  
`openclaw_message_delivery_started_total` | counter | `channel`, `delivery_kind`  
`openclaw_message_delivery_total` | counter | `channel`, `delivery_kind`, `error_category`, `outcome`  
`openclaw_message_delivery_duration_seconds` | histogram | `channel`, `delivery_kind`, `error_category`, `outcome`  
`openclaw_talk_event_total` | counter | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_talk_event_duration_seconds` | histogram | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_talk_audio_bytes` | histogram | `brain`, `event_type`, `mode`, `provider`, `transport`  
`openclaw_queue_lane_size` | gauge | `lane`  
`openclaw_queue_lane_wait_seconds` | histogram | `lane`  
`openclaw_session_state_total` | counter | `reason`, `state`  
`openclaw_session_queue_depth` | gauge | `state`  
`openclaw_session_recovery_total` | counter | `action`, `active_work_kind`, `state`, `status`  
`openclaw_session_recovery_age_seconds` | histogram | `action`, `active_work_kind`, `state`, `status`  
`openclaw_memory_bytes` | gauge | `kind`  
`openclaw_memory_rss_bytes` | histogram | немає  
`openclaw_memory_pressure_total` | counter | `level`, `reason`  
`openclaw_telemetry_exporter_total` | counter | `exporter`, `reason`, `signal`, `status`  
`openclaw_prometheus_series_dropped_total` | counter | немає  
  
## Політика міток

Bounded, low-cardinality labels

Мітки Prometheus залишаються обмеженими та з низькою кардинальністю. Експортер не видає сирі діагностичні ідентифікатори, як-от `runId`, `sessionKey`, `sessionId`, `callId`, `toolCallId`, ідентифікатори повідомлень, ідентифікатори чатів або ідентифікатори запитів провайдера.

Значення міток редагуються та мають відповідати політиці OpenClaw щодо символів із низькою кардинальністю. Значення, які не відповідають політиці, замінюються на `unknown`, `other` або `none`, залежно від метрики.

Обмеження рядів і облік переповнення

Експортер обмежує збережені часові ряди в пам’яті **2048** рядами сукупно для лічильників, вимірювачів і гістограм. Нові ряди понад це обмеження відкидаються, а `openclaw_prometheus_series_dropped_total` збільшується на одиницю щоразу.

Відстежуйте цей лічильник як чіткий сигнал, що атрибут вище за потоком пропускає значення з високою кардинальністю. Експортер ніколи не підвищує обмеження автоматично; якщо лічильник зростає, виправте джерело, а не вимикайте обмеження.

Що ніколи не з’являється у виводі Prometheus

  * текст промпта, текст відповіді, вхідні дані інструментів, вихідні дані інструментів, системні промпти
  * стенограми розмов, аудіо payloads, ідентифікатори викликів, ідентифікатори кімнат, токени передавання, ідентифікатори ходів і необроблені ідентифікатори сеансів
  * необроблені ідентифікатори запитів провайдера (лише обмежені хеші, де застосовно, на spans — ніколи в метриках)
  * ключі сеансів і ідентифікатори сеансів
  * імена хостів, шляхи до файлів, секретні значення


## Рецепти PromQL

promqlCopy code
[code]
    # Tokens per minute, split by providersum by (provider) (rate(openclaw_model_tokens_total[1m])) # Spend (USD) over the last hour, by modelsum by (model) (increase(openclaw_model_cost_usd_total[1h])) # 95th percentile model run durationhistogram_quantile(  0.95,  sum by (le, provider, model)    (rate(openclaw_run_duration_seconds_bucket[5m]))) # Queue wait time SLO (95p under 2s)histogram_quantile(  0.95,  sum by (le, lane) (rate(openclaw_queue_lane_wait_seconds_bucket[5m]))) < 2 # Dropped Prometheus series (cardinality alarm)increase(openclaw_prometheus_series_dropped_total[15m]) > 0
[/code]

## Вибір між експортом Prometheus і OpenTelemetry

OpenClaw підтримує обидві поверхні незалежно. Ви можете запускати одну з них, обидві або жодну.

### diagnostics-prometheus

  * Модель **pull** : Prometheus зчитує `/api/diagnostics/prometheus`.
  * Зовнішній колектор не потрібен.
  * Автентифікація через звичайну автентифікацію Gateway.
  * Поверхня містить лише метрики (без трасувань або логів).
  * Найкраще підходить для стеків, уже стандартизованих на Prometheus + Grafana.


### diagnostics-otel

  * Модель **push** : OpenClaw надсилає OTLP/HTTP до колектора або OTLP-сумісного бекенда.
  * Поверхня містить метрики, трасування й логи.
  * Підключається до Prometheus через OpenTelemetry Collector (експортер `prometheus` або `prometheusremotewrite`), коли потрібні обидва варіанти.
  * Див. [Експорт OpenTelemetry](</uk/gateway/opentelemetry>) для повного каталогу.


## Усунення несправностей

Порожнє тіло відповіді

  * Перевірте `diagnostics.enabled: true` у конфігурації.
  * Підтвердьте, що Plugin увімкнено й завантажено, за допомогою `openclaw plugins list --enabled`.
  * Згенеруйте трохи трафіку; лічильники й гістограми виводять рядки лише після принаймні однієї події.

401 / не авторизовано

Ендпоінт потребує області оператора Gateway (`auth: "gateway"` з `gatewayRuntimeScopeSurface: "trusted-operator"`). Використовуйте той самий токен або пароль, який Prometheus використовує для будь-якого іншого операторського маршруту Gateway. Публічного режиму без автентифікації немає.

`openclaw_prometheus_series_dropped_total` зростає

Новий атрибут перевищує обмеження в **2048** рядів. Перегляньте останні метрики на наявність неочікувано висококардинальної мітки та виправте її в джерелі. Експортер навмисно відкидає нові ряди замість того, щоб непомітно переписувати мітки.

Prometheus показує застарілі ряди після перезапуску

Plugin зберігає стан лише в пам’яті. Після перезапуску Gateway лічильники скидаються до нуля, а вимірювачі починають знову з наступного повідомленого значення. Використовуйте PromQL `rate()` і `increase()`, щоб коректно обробляти скидання.

## Пов’язане

  * [Експорт діагностики](</uk/gateway/diagnostics>) — локальний zip-архів діагностики для пакетів підтримки
  * [Справність і готовність](</uk/gateway/health>) — проби `/healthz` і `/readyz`
  * [Журналювання](</uk/logging>) — файлове журналювання
  * [Експорт OpenTelemetry](</uk/gateway/opentelemetry>) — надсилання OTLP для трасувань, метрик і журналів


Was this useful?YesNo