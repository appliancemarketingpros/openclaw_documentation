---
title: Пошук Exa
source_url: https://docs.openclaw.ai/uk/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw підтримує [Exa AI](<https://exa.ai/>) як постачальника `web_search`. Exa пропонує нейронний, ключовий і гібридний режими пошуку з вбудованим витягуванням вмісту (виділення, текст, резюме).

## Отримання ключа API

* ### Створіть обліковий запис

Зареєструйтеся на [exa.ai](<https://exa.ai/>) і згенеруйте ключ API на своїй панелі керування.

* ### Збережіть ключ

Установіть `EXA_API_KEY` у середовищі Gateway або налаштуйте через:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Конфігурація

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**Альтернатива через середовище:** установіть `EXA_API_KEY` у середовищі Gateway. Для встановленого gateway помістіть його в `~/.openclaw/.env`.

## Перевизначення базової URL-адреси

Установіть `plugins.entries.exa.config.webSearch.baseUrl`, коли пошукові запити Exa мають проходити через сумісний проксі або альтернативну кінцеву точку Exa. OpenClaw нормалізує голі імена хостів, додаючи на початок `https://`, і додає `/search`, якщо шлях ще не завершується ним. Розв’язана кінцева точка включається в ключ кешу пошуку, тому результати з різних кінцевих точок Exa не спільно використовуються.

## Параметри інструмента

Пошуковий запит.

Кількість результатів для повернення (1–100).

Режим пошуку.

Фільтр часу.

Результати після цієї дати (`YYYY-MM-DD`).

Результати до цієї дати (`YYYY-MM-DD`).

Параметри витягування вмісту (див. нижче).

### Витягування вмісту

Exa може повертати витягнутий вміст разом із результатами пошуку. Передайте об’єкт `contents`, щоб увімкнути:

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

Параметр contents | Тип | Опис  
---|---|---  
`text` | `boolean | { maxCharacters }` | Витягнути повний текст сторінки  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | Витягнути ключові речення  
`summary` | `boolean | { query }` | Згенероване ШІ резюме  
  
### Режими пошуку

Режим | Опис  
---|---  
`auto` | Exa вибирає найкращий режим (типово)  
`neural` | Семантичний пошук на основі значення  
`fast` | Швидкий пошук за ключовими словами  
`deep` | Ретельний глибокий пошук  
`deep-reasoning` | Глибокий пошук із міркуванням  
`instant` | Найшвидші результати  
  
## Примітки

  * Якщо параметр `contents` не надано, Exa типово використовує `{ highlights: true }`, тож результати містять уривки ключових речень
  * Результати зберігають поля `highlightScores` і `summary` з відповіді Exa API, якщо вони доступні
  * Описи результатів визначаються спочатку з виділень, потім із резюме, а потім із повного тексту — залежно від того, що доступно
  * `freshness` і `date_after`/`date_before` не можна поєднувати — використовуйте один режим фільтрації за часом
  * За один запит можна повернути до 100 результатів (з урахуванням обмежень типу пошуку Exa)
  * Результати типово кешуються на 15 хвилин (налаштовується через `cacheTtlMinutes`)
  * Exa — це офіційна інтеграція API зі структурованими відповідями JSON


## Пов’язане

  * [Огляд вебпошуку](</uk/tools/web>) \-- усі постачальники й автовиявлення
  * [Brave Search](</uk/tools/brave-search>) \-- структуровані результати з фільтрами країни/мови
  * [Perplexity Search](</uk/tools/perplexity-search>) \-- структуровані результати з фільтрацією за доменом


Was this useful?YesNo