---
title: Plugin‌های ابزار
source_url: https://docs.openclaw.ai/fa/plugins/tool-plugins
scraped_at: 2026-06-29
---

CapabilitiesBuilding plugins

Pluginهای ابزار، ابزارهای قابل‌فراخوانی توسط عامل را بدون افزودن کانال، ارائه‌دهندهٔ مدل، قلاب، سرویس، یا بک‌اند راه‌اندازی به OpenClaw اضافه می‌کنند. زمانی از `defineToolPlugin` استفاده کنید که Plugin مالک فهرست ثابتی از ابزارها است و می‌خواهید OpenClaw فرادادهٔ manifest را تولید کند که آن ابزارها را بدون بارگذاری کد runtime قابل کشف نگه می‌دارد.

جریان پیشنهادی این است:

  1. یک package را با `openclaw plugins init` scaffold کنید.
  2. ابزارها را با `defineToolPlugin` بنویسید.
  3. JavaScript را build کنید.
  4. فرادادهٔ `openclaw.plugin.json` و `package.json` را با `openclaw plugins build` تولید کنید.
  5. فرادادهٔ تولیدشده را پیش از انتشار یا نصب اعتبارسنجی کنید.


برای Pluginهای ارائه‌دهنده، کانال، قلاب، سرویس، یا دارای قابلیت‌های ترکیبی، به‌جای آن از [ساخت Pluginها](</fa/plugins/building-plugins>)، [Pluginهای کانال](</fa/plugins/sdk-channel-plugins>)، یا [Pluginهای ارائه‌دهنده](</fa/plugins/sdk-provider-plugins>) شروع کنید.

## الزامات

  * Node >= 22.
  * خروجی package از نوع TypeScript ESM.
  * `typebox` برای schemaهای پیکربندی و پارامترهای ابزار.
  * `openclaw >=2026.5.17`، نخستین نسخهٔ OpenClaw که `openclaw/plugin-sdk/tool-plugin` را export می‌کند.
  * ریشهٔ package که بتواند `dist/`، `openclaw.plugin.json`، و `package.json` را منتشر کند.


Plugin تولیدشده در runtime، `typebox` را import می‌کند، بنابراین `typebox` را در `dependencies` نگه دارید، نه فقط در `devDependencies`.

## شروع سریع

یک package جدید برای Plugin بسازید:

bashCopy code
[code]
    openclaw plugins init stock-quotes --name "Stock Quotes"cd stock-quotesnpm installnpm run plugin:buildnpm run plugin:validatenpm test
[/code]

scaffold این موارد را ایجاد می‌کند:

  * `src/index.ts`: یک entry از نوع `defineToolPlugin` با ابزار `echo`.
  * `src/index.test.ts`: یک test کوچک برای فراداده.
  * `tsconfig.json`: خروجی TypeScript با NodeNext به `dist/`.
  * `package.json`: scriptها، وابستگی‌های runtime، و `openclaw.extensions: ["./dist/index.js"]`.
  * `openclaw.plugin.json`: فرادادهٔ manifest تولیدشده برای ابزار اولیه.


خروجی اعتبارسنجی مورد انتظار:

textCopy code
[code]
    Plugin stock-quotes is valid.
[/code]

## نوشتن یک ابزار

`defineToolPlugin` هویت Plugin، یک schema اختیاری برای پیکربندی، و یک فهرست ایستای ابزارها را می‌گیرد. نوع‌های پارامتر و پیکربندی از schemaهای TypeBox استنتاج می‌شوند.

typescriptCopy code
[code]
      export default defineToolPlugin({  id: "stock-quotes",  name: "Stock Quotes",  description: "Fetch stock quote snapshots.",  configSchema: Type.Object({    apiKey: Type.Optional(Type.String({ description: "Quote API key." })),    baseUrl: Type.Optional(Type.String({ description: "Quote API base URL." })),  }),  tools: (tool) => [    tool({      name: "stock_quote",      label: "Stock Quote",      description: "Fetch a stock quote snapshot.",      parameters: Type.Object({        symbol: Type.String({ description: "Ticker symbol, for example OPEN." }),      }),      async execute({ symbol }, config, context) {        context.signal?.throwIfAborted();        return {          symbol: symbol.toUpperCase(),          configured: Boolean(config.apiKey),          baseUrl: config.baseUrl ?? "https://api.example.com",        };      },    }),  ],});
[/code]

نام ابزارها API پایدار هستند. نام‌هایی انتخاب کنید که یکتا، با حروف کوچک، و به‌اندازهٔ کافی مشخص باشند تا با ابزارهای core یا Pluginهای دیگر تداخل نداشته باشند.

## ابزارهای اختیاری و factory

وقتی کاربران باید ابزار را صراحتا در allowlist قرار دهند تا پیش از ارسال به مدل فعال شود، `optional: true` را تنظیم کنید:

typescriptCopy code
[code]
    tool({  name: "workflow_run",  description: "Run an external workflow.",  parameters: Type.Object({ goal: Type.String() }),  optional: true,  execute: ({ goal }) => ({ queued: true, goal }),});
[/code]

`openclaw plugins build` entry متناظر `toolMetadata.<tool>.optional` را در manifest می‌نویسد، تا OpenClaw بتواند ابزار را بدون بارگذاری کد runtime Plugin کشف کند.

وقتی یک ابزار پیش از ساخته‌شدن به context ابزار در runtime نیاز دارد، از `factory` استفاده کنید. factory فراداده را ایستا نگه می‌دارد، در حالی که به ابزار اجازه می‌دهد برای یک اجرای خاص انصراف دهد، وضعیت sandbox را بررسی کند، یا helperهای runtime را bind کند.

typescriptCopy code
[code]
    tool({  name: "local_workflow",  description: "Run a local workflow outside sandboxed sessions.",  parameters: Type.Object({ goal: Type.String() }),  optional: true,  factory({ api, toolContext }) {    if (toolContext.sandboxed) {      return null;    }    return createLocalWorkflowTool(api);  },});
[/code]

factoryها همچنان برای نام‌های ثابت ابزار هستند. وقتی Plugin نام ابزارها را به‌صورت پویا محاسبه می‌کند یا ابزارها را با قلاب‌ها، سرویس‌ها، ارائه‌دهنده‌ها، commandها، یا سطح‌های runtime دیگر ترکیب می‌کند، مستقیما از `definePluginEntry` استفاده کنید.

## مقدارهای بازگشتی

`defineToolPlugin` مقدارهای بازگشتی ساده را در قالب نتیجهٔ ابزار OpenClaw wrap می‌کند:

  * وقتی مدل باید همان متن دقیق را ببیند، یک رشته برگردانید.
  * وقتی می‌خواهید مدل JSON قالب‌بندی‌شده را ببیند و OpenClaw مقدار اصلی را در `details` نگه دارد، یک مقدار سازگار با JSON برگردانید.

typescriptCopy code
[code]
    tool({  name: "echo_text",  description: "Echo input text.",  parameters: Type.Object({    input: Type.String(),  }),  execute: ({ input }) => input,});
[/code]

typescriptCopy code
[code]
    tool({  name: "echo_json",  description: "Echo input as structured JSON.",  parameters: Type.Object({    input: Type.String(),  }),  execute: ({ input }) => ({ input, length: input.length }),});
[/code]

وقتی باید یک `AgentToolResult` سفارشی برگردانید یا از یک پیاده‌سازی موجود `api.registerTool` دوباره استفاده کنید، از ابزار factory استفاده کنید. وقتی به ابزارهای کاملا پویا یا قابلیت‌های ترکیبی Plugin نیاز دارید، به‌جای `defineToolPlugin` از `definePluginEntry` استفاده کنید.

## پیکربندی

`configSchema` اختیاری است. اگر آن را حذف کنید، OpenClaw از یک schema سخت‌گیرانهٔ شیء خالی استفاده می‌کند و manifest تولیدشده همچنان شامل `configSchema` خواهد بود.

typescriptCopy code
[code]
    export default defineToolPlugin({  id: "no-config-tools",  name: "No Config Tools",  description: "Adds tools that do not need configuration.",  tools: () => [],});
[/code]

وقتی `configSchema` را اضافه می‌کنید، آرگومان دوم `execute` از روی schema نوع‌دهی می‌شود:

typescriptCopy code
[code]
    const configSchema = Type.Object({  apiKey: Type.String(),}); export default defineToolPlugin({  id: "configured-tools",  name: "Configured Tools",  description: "Adds configured tools.",  configSchema,  tools: (tool) => [    tool({      name: "configured_ping",      description: "Check whether configuration is available.",      parameters: Type.Object({}),      execute: (_params, config) => ({ hasKey: config.apiKey.length > 0 }),    }),  ],});
[/code]

OpenClaw پیکربندی Plugin را از entry مربوط به Plugin در پیکربندی Gateway می‌خواند. secretها را در source یا نمونه‌های مستندات hard-code نکنید. مطابق مدل امنیتی Plugin از پیکربندی، متغیرهای محیطی، یا SecretRefها استفاده کنید.

## فرادادهٔ تولیدشده

OpenClaw، Pluginهای نصب‌شده را از فرادادهٔ سرد کشف می‌کند. باید بتواند manifest مربوط به Plugin را پیش از import کردن کد runtime آن Plugin بخواند. بنابراین `defineToolPlugin` فرادادهٔ ایستا را expose می‌کند، و `openclaw plugins build` آن فراداده را در package می‌نویسد.

پس از تغییر id، name، description، schema پیکربندی، activation، یا نام ابزارهای Plugin، generator را اجرا کنید:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js
[/code]

برای یک Plugin تک‌ابزاری، manifest تولیدشده شبیه این است:

jsonCopy code
[code]
    {  "id": "stock-quotes",  "name": "Stock Quotes",  "description": "Fetch stock quote snapshots.",  "version": "0.1.0",  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {}  },  "activation": {    "onStartup": true  },  "contracts": {    "tools": ["stock_quote"]  }}
[/code]

`contracts.tools` قرارداد مهم کشف است. این به OpenClaw می‌گوید کدام Plugin مالک هر ابزار است، بدون اینکه runtime همهٔ Pluginهای نصب‌شده را بارگذاری کند. اگر manifest stale باشد، ممکن است ابزار در کشف دیده نشود یا Plugin اشتباهی برای خطای registration مقصر شناخته شود.

## فرادادهٔ package

برای جریان سادهٔ tool-plugin، `openclaw plugins build`، `package.json` را با entry واحد runtime انتخاب‌شده همسو می‌کند:

jsonCopy code
[code]
    {  "type": "module",  "files": ["dist", "openclaw.plugin.json", "README.md"],  "dependencies": {    "typebox": "^1.1.38"  },  "peerDependencies": {    "openclaw": ">=2026.5.17"  },  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

برای packageهای نصب‌شده از JavaScript ساخته‌شده مانند `./dist/index.js` استفاده کنید. entryهای source در توسعهٔ workspace مفید هستند، اما packageهای منتشرشده نباید به بارگذاری runtime TypeScript وابسته باشند.

## اعتبارسنجی در CI

از `plugins build --check` استفاده کنید تا وقتی فرادادهٔ تولیدشده stale است، CI بدون بازنویسی فایل‌ها fail شود:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js --checkopenclaw plugins validate --entry ./dist/index.jsnpm test
[/code]

`plugins validate` بررسی می‌کند که:

  * `openclaw.plugin.json` وجود دارد و از loader معمول manifest عبور می‌کند.
  * entry فعلی فرادادهٔ `defineToolPlugin` را export می‌کند.
  * فیلدهای manifest تولیدشده با فرادادهٔ entry مطابقت دارند.
  * `contracts.tools` با نام ابزارهای اعلام‌شده مطابقت دارد.
  * `package.json` مقدار `openclaw.extensions` را به entry runtime انتخاب‌شده اشاره می‌دهد.


## نصب و بررسی محلی

از یک checkout جداگانهٔ OpenClaw یا CLI نصب‌شده، مسیر package را نصب کنید:

bashCopy code
[code]
    openclaw plugins install ./stock-quotesopenclaw plugins inspect stock-quotes --runtime
[/code]

برای smoke مربوط به package، ابتدا pack کنید و tarball را نصب کنید:

bashCopy code
[code]
    npm packopenclaw plugins install npm-pack:./openclaw-plugin-stock-quotes-0.1.0.tgzopenclaw plugins inspect stock-quotes --runtime --json
[/code]

پس از نصب، Gateway را شروع یا restart کنید و از عامل بخواهید از ابزار استفاده کند. اگر در حال اشکال‌زدایی visibility ابزار هستید، پیش از تغییر کد، runtime Plugin و catalog مؤثر ابزار را بررسی کنید.

## انتشار

وقتی package آماده است، آن را از طریق ClawHub منتشر کنید:

bashCopy code
[code]
    clawhub package publish your-org/stock-quotes --dry-runclawhub package publish your-org/stock-quotes
[/code]

با یک locator صریح ClawHub نصب کنید:

bashCopy code
[code]
    openclaw plugins install clawhub:your-org/stock-quotes
[/code]

مشخصات خام package در npm در زمان گذار launch همچنان پشتیبانی می‌شوند، اما ClawHub سطح ترجیحی کشف و توزیع برای Pluginهای OpenClaw است.

## عیب‌یابی

### `plugin entry not found: ./dist/index.js`

فایل entry انتخاب‌شده وجود ندارد. `npm run build` را اجرا کنید، سپس دوباره `openclaw plugins build --entry ./dist/index.js` یا `openclaw plugins validate --entry ./dist/index.js` را اجرا کنید.

### `plugin entry does not expose defineToolPlugin metadata`

entry مقداری را که با `defineToolPlugin` ساخته شده باشد export نکرده است. بررسی کنید که default export ماژول نتیجهٔ `defineToolPlugin(...)` باشد، یا entry درست را با `--entry` ارسال کنید.

### `openclaw.plugin.json generated metadata is stale`

manifest دیگر با فرادادهٔ entry مطابقت ندارد. اجرا کنید:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js
[/code]

تغییرات `openclaw.plugin.json` و `package.json` را commit کنید.

### `package.json openclaw.extensions must include ./dist/index.js`

فرادادهٔ package به entry runtime متفاوتی اشاره می‌کند. اجرا کنید: `openclaw plugins build --entry ./dist/index.js` تا generator فرادادهٔ package را با entryای که قصد انتشار آن را دارید همسو کند.

### `Cannot find package 'typebox'`

Plugin ساخته‌شده در runtime، `typebox` را import می‌کند. `typebox` را در `dependencies` نگه دارید، وابستگی‌های package را دوباره نصب کنید، دوباره build کنید، و اعتبارسنجی را دوباره اجرا کنید.

### ابزار پس از نصب ظاهر نمی‌شود

این موارد را به‌ترتیب بررسی کنید:

  1. `openclaw plugins inspect <plugin-id> --runtime`
  2. `openclaw plugins validate --root <plugin-root> --entry ./dist/index.js`
  3. `openclaw.plugin.json` دارای `contracts.tools` با نام‌های ابزار مورد انتظار است.
  4. `package.json` دارای `openclaw.extensions: ["./dist/index.js"]` است.
  5. Gateway پس از نصب Plugin restart یا reload شده است.


## همچنین ببینید

  * [ساخت Pluginها](</fa/plugins/building-plugins>)
  * [نقاط entry Plugin](</fa/plugins/sdk-entrypoints>)
  * [زیرمسیرهای SDK Plugin](</fa/plugins/sdk-subpaths>)
  * [manifest Plugin](</fa/plugins/manifest>)
  * [CLI Pluginها](</fa/cli/plugins>)
  * [انتشار در ClawHub](</fa/clawhub/publishing>)


Was this useful?YesNo

Open issue