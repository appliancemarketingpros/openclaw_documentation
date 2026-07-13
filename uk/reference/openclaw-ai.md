---
title: пакет @openclaw/ai
source_url: https://docs.openclaw.ai/uk/reference/openclaw-ai
scraped_at: 2026-07-13
---

ReferenceTechnical reference

`@openclaw/ai` — це придатна для публікації бібліотечна форма рівня виконання моделей OpenClaw: незалежні від провайдера контракти повідомлень, інструментів і потоків, валідація, діагностика, потоки подій, ізольований реєстр середовища виконання та адаптери з відкладеним завантаженням для восьми вбудованих сімейств API (Anthropic Messages, OpenAI Completions, OpenAI Responses, Azure OpenAI Responses, ChatGPT/Codex Responses, Google Generative AI, Google Vertex, Mistral Conversations).

Вона публікується разом із кореневим пакетом `openclaw` у кожному випуску, прив’язана до тієї самої версії та має власний `npm-shrinkwrap.json`, щоб дерево транзитивних залежностей фіксувалося під час установлення. Установлення `openclaw` автоматично встановлює відповідну версію `@openclaw/ai`; споживачі бібліотеки можуть залежати від неї безпосередньо, не використовуючи код застосунку OpenClaw.

## Швидкий початок

jsCopy code
[code]
      const runtime = createLlmRuntime();registerBuiltInApiProviders(runtime.registry); const stream = runtime.streamSimple(model, { messages }, { apiKey });for await (const event of stream) {  if (event.type === "text_delta") process.stdout.write(event.delta);}const result = await stream.result();
[/code]

Готова до запуску версія міститься в репозиторії за шляхом `examples/ai-chat`.

## Контракт проєктування

  * **За замовчуванням область дії обмежена екземпляром.** Імпортування пакета нічого не реєструє глобально. `createApiRegistry()` / `createLlmRuntime()` повертають ізольовані екземпляри; `registerBuiltInApiProviders(registry)` явно підключає вбудовані транспорти до одного реєстру. Модулі SDK провайдерів завантажуються відкладено під час першого використання.
  * **Політика хоста впроваджується, а не вбудовується.** Захист запитів `fetch` (наприклад, політика SSRF), приховування секретів у тексті повторного відтворення результатів інструментів, стандартні налаштування строгого режиму інструментів OpenAI та журналювання діагностики — це порти `AiTransportHost`, налаштовані за допомогою `configureAiTransportHost`. Стандартні реалізації бібліотеки неактивні; OpenClaw установлює власні робочі реалізації у своєму потоковому фасаді.
  * **Єдина ідентичність потоку подій.** `@openclaw/ai/event-stream` — це канонічний конструктор `EventStream`, спільний для ядра OpenClaw, agent-core і зовнішніх споживачів.
  * **Підшляхи`internal/*` не є API.** Вони існують для самого застосунку OpenClaw і не мають гарантій семантичного версіонування.
  * Ідентифікатори провайдерів, облікові дані, каталоги моделей, повторні спроби та перемикання після відмови залишаються відповідальністю застосунку. OpenClaw додає ці рівні навколо цього пакета; споживач бібліотеки безпосередньо надає об’єкт `Model` і параметри.


## Експорти підшляхів

Підшлях | Вміст  
---|---  
`.` | Контракти, `createApiRegistry`, `createLlmRuntime`, `configureAiTransportHost`  
`./providers` | `registerBuiltInApiProviders`, `resetApiProviders`  
`./types` | Типи моделей, повідомлень, інструментів і потоків  
`./validation` | Валідація аргументів інструментів  
`./diagnostics` | Контракти діагностики  
`./event-stream` | Спільна реалізація `EventStream`  
`./internal/*` | Внутрішнє для OpenClaw, без гарантій семантичного версіонування  
  
Was this useful?YesNo

Open issue