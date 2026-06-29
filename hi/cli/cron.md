---
title: Cron
source_url: https://docs.openclaw.ai/hi/cli/cron
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw cron`

Gateway शेड्यूलर के लिए cron जॉब्स प्रबंधित करें.

## जॉब्स जल्दी बनाएँ

`openclaw cron create`, `openclaw cron add` का alias है. नई जॉब्स के लिए, पहले शेड्यूल रखें और दूसरा प्रॉम्प्ट:

bashCopy code
[code]
    openclaw cron create "0 7 * * *" \  "Summarize overnight updates." \  --name "Morning brief" \  --agent ops
[/code]

जब जॉब को चैट लक्ष्य तक डिलीवर करने के बजाय पूरा पेलोड POST करना हो, तो `--webhook <url>` का उपयोग करें:

bashCopy code
[code]
    openclaw cron create "0 18 * * 1-5" \  "Summarize today's deploys as JSON." \  --name "Deploy digest" \  --webhook "https://example.invalid/openclaw/cron"
[/code]

नियतात्मक shell-शैली की जॉब्स के लिए `--command` का उपयोग करें, जिन्हें अलग agent/model run शुरू किए बिना OpenClaw cron के अंदर चलना चाहिए:

bashCopy code
[code]
    openclaw cron create "*/15 * * * *" \  --name "Queue depth probe" \  --command "scripts/check-queue.sh" \  --command-cwd "/srv/app" \  --announce \  --channel telegram \  --to "-1001234567890"
[/code]

`--command <shell>` `argv: ["sh", "-lc", <shell>]` संग्रहित करता है. सटीक argv execution के लिए `--command-argv '["node","scripts/report.mjs"]'` का उपयोग करें. Command jobs stdout/stderr कैप्चर करती हैं, सामान्य cron history दर्ज करती हैं, और output को isolated jobs जैसे ही `announce`, `webhook`, या `none` delivery modes के माध्यम से route करती हैं. केवल `NO_REPLY` print करने वाली command suppress की जाती है.

## Sessions

`--session` `main`, `isolated`, `current`, या `session:<id>` स्वीकार करता है.

Session keys

  * `main` agent के main session से bind करता है.
  * `isolated` हर run के लिए नया transcript और session id बनाता है.
  * `current` creation time पर active session से bind करता है.
  * `session:<id>` किसी स्पष्ट persistent session key से pin करता है.

Isolated session semantics

Isolated runs ambient conversation context को reset करते हैं. नए run के लिए channel और group routing, send/queue policy, elevation, origin, और ACP runtime binding reset होते हैं. Safe preferences और स्पष्ट user-selected model या auth overrides runs के बीच carry हो सकते हैं.

## Delivery

`openclaw cron list` और `openclaw cron show <job-id>` resolved delivery route का preview दिखाते हैं. `channel: "last"` के लिए, preview दिखाता है कि route main या current session से resolve हुआ, या fail closed होगा.

Provider-prefixed targets unresolved announce channels को स्पष्ट कर सकते हैं. उदाहरण के लिए, `to: "telegram:123"` Telegram चुनता है जब `delivery.channel` छोड़ा गया हो या `last` हो. केवल loaded plugin द्वारा advertised prefixes ही provider selectors हैं. यदि `delivery.channel` स्पष्ट है, तो prefix को उस channel से match करना होगा; `channel: "whatsapp"` के साथ `to: "telegram:123"` reject किया जाता है. `imessage:` और `sms:` जैसे service prefixes channel-owned target syntax बने रहते हैं.

### Delivery ownership

Isolated cron chat delivery agent और runner के बीच साझा होती है:

  * Chat route उपलब्ध होने पर agent `message` tool का उपयोग करके सीधे भेज सकता है.
  * `announce` अंतिम reply को fallback-deliver केवल तब करता है जब agent ने resolved target पर सीधे नहीं भेजा हो.
  * `webhook` पूरा payload किसी URL पर post करता है.
  * `none` runner fallback delivery को disable करता है.


Webhook delivery set करने के लिए `cron add|create --webhook <url>` या `cron edit <job-id> --webhook <url>` का उपयोग करें. `--webhook` को `--announce`, `--no-deliver`, `--channel`, `--to`, `--thread-id`, या `--account` जैसे chat delivery flags के साथ combine न करें.

`cron edit <job-id>` `--clear-channel`, `--clear-to`, `--clear-thread-id`, और `--clear-account` से अलग-अलग delivery routing fields unset कर सकता है (प्रत्येक अपने matching set flag के साथ combine होने पर reject किया जाता है). `--no-deliver` के विपरीत, जो केवल runner fallback delivery disable करता है, ये stored field हटाते हैं ताकि job अपने route के उस हिस्से को फिर defaults से resolve करे.

`--announce` अंतिम reply के लिए runner fallback delivery है. `--no-deliver` उस fallback को disable करता है लेकिन chat route उपलब्ध होने पर agent का `message` tool नहीं हटाता.

Active chat से बनाए गए reminders fallback announce delivery के लिए live chat delivery target preserve करते हैं. Internal session keys lowercase हो सकती हैं; Matrix room IDs जैसे case-sensitive provider IDs के लिए इन्हें source of truth के रूप में उपयोग न करें.

### Failure delivery

Failure notifications इस क्रम में resolve होते हैं:

  1. job पर `delivery.failureDestination`.
  2. Global `cron.failureDestination`.
  3. job का primary announce target (जब कोई explicit failure destination set नहीं है).


Note: isolated cron runs run-level agent failures को job errors मानते हैं, भले ही कोई reply payload न बना हो, इसलिए model/provider failures फिर भी error counters increment करते हैं और failure notifications trigger करते हैं.

Command cron jobs isolated agent turn शुरू नहीं करतीं. Zero exit code `ok` दर्ज करता है; non-zero exit, signal, timeout, या no-output timeout `error` दर्ज करता है और वही failure notification path trigger कर सकता है.

यदि isolated run पहले model request से पहले time out हो जाता है, तो `openclaw cron show` और `openclaw cron runs` phase-specific error शामिल करते हैं, जैसे `setup timed out before runner start` या `stalled before first model call (last phase: context-engine)`. CLI-backed providers के लिए, pre-model watchdog external CLI turn शुरू होने तक active रहता है, इसलिए session lookup, hook, auth, prompt, और CLI setup stalls pre-model cron failures के रूप में report होते हैं.

## Scheduling

### One-shot jobs

`--at <datetime>` one-shot run schedule करता है. Offset-less datetimes को UTC माना जाता है, जब तक आप `--tz <iana>` भी pass न करें, जो दिए गए timezone में wall-clock time interpret करता है.

### Recurring jobs

Recurring jobs consecutive errors के बाद exponential retry backoff का उपयोग करती हैं: 30s, 1m, 5m, 15m, 60m. अगले successful run के बाद schedule सामान्य हो जाता है.

Skipped runs execution errors से अलग track किए जाते हैं. वे retry backoff को प्रभावित नहीं करते, लेकिन `openclaw cron edit <job-id> --failure-alert-include-skipped` failure alerts को repeated skipped-run notifications में opt कर सकता है.

Local configured model provider को target करने वाली isolated jobs के लिए, cron agent turn शुरू करने से पहले lightweight provider preflight चलाता है. Loopback, private-network, और `.local` `api: "ollama"` providers को `/api/tags` पर probe किया जाता है; vLLM, SGLang, और LM Studio जैसे local OpenAI-compatible providers को `/models` पर probe किया जाता है. यदि endpoint unreachable है, तो run `skipped` के रूप में record होता है और बाद के schedule पर retry किया जाता है; matching dead endpoints को 5 मिनट के लिए cache किया जाता है ताकि कई jobs उसी local server पर hammer न करें.

Note: cron jobs, pending runtime state, और run history shared SQLite state database में रहती हैं. Legacy `jobs.json`, `jobs-state.json`, और `runs/*.jsonl` files एक बार import होती हैं और `.migrated` suffix के साथ rename होती हैं. Import के बाद, JSON files edit करने के बजाय `openclaw cron add|edit|remove` से schedules edit करें.

### Manual runs

`openclaw cron run <job-id>` default रूप से force-runs करता है और manual run queue होते ही return करता है. Successful responses में `{ ok: true, enqueued: true, runId }` शामिल होता है. बाद का result inspect करने के लिए returned `runId` का उपयोग करें:

bashCopy code
[code]
    openclaw cron run <job-id>openclaw cron runs --id <job-id> --run-id <run-id>
[/code]

जब script को तब तक block करना हो जब तक वही exact queued run terminal status record न करे, तो `--wait` जोड़ें:

bashCopy code
[code]
    openclaw cron run <job-id> --wait --wait-timeout 10m --poll-interval 2s
[/code]

`--wait` के साथ, CLI फिर भी पहले `cron.run` call करता है, फिर returned `runId` के लिए `cron.runs` poll करता है. Command केवल तब `0` exit करती है जब run status `ok` के साथ finish हो. Run `error` या `skipped` के साथ finish होने पर, Gateway response में `runId` शामिल न होने पर, या `--wait-timeout` expire होने पर यह non-zero exit करती है. `--poll-interval` zero से बड़ा होना चाहिए.

## Models

`cron add|edit --model <ref>` job के लिए allowed model चुनता है. `cron add|edit --fallbacks <list>` per-job fallback models set करता है, उदाहरण के लिए `--fallbacks openrouter/gpt-4.1-mini,openai/gpt-5`; कोई fallbacks न रखने वाले strict run के लिए `--fallbacks ""` pass करें. `cron edit <job-id> --clear-fallbacks` per-job fallback override हटाता है. `cron edit <job-id> --clear-model` per-job model override हटाता है ताकि job normal cron model-selection precedence follow करे (यदि मौजूद हो तो stored cron-session override, अन्यथा agent/default model); इसे `--model` के साथ combine नहीं किया जा सकता.

Cron `--model` एक **job primary** है, chat-session `/model` override नहीं. इसका अर्थ है:

  * Selected job model fail होने पर configured model fallbacks अभी भी apply होते हैं.
  * Per-job payload `fallbacks` मौजूद होने पर configured fallback list को replace करता है.
  * Empty per-job fallback list (`--fallbacks ""` या job payload/API में `fallbacks: []`) cron run को strict बनाती है.
  * जब job में `--model` है लेकिन कोई fallback list configured नहीं है, OpenClaw explicit empty fallback override pass करता है ताकि agent primary hidden retry target के रूप में append न हो.
  * Cron run को `skipped` mark करने से पहले local-provider preflight checks configured fallbacks walk करते हैं.


`openclaw doctor` उन jobs की report करता है जिनमें पहले से `payload.model` set है, जिसमें provider namespace counts और `agents.defaults.model` के विरुद्ध mismatches शामिल हैं. जब auth, provider, या billing behavior live chat और scheduled jobs के बीच अलग दिखे, तो उस check का उपयोग करें.

### Isolated cron model precedence

Isolated cron active model को इस क्रम में resolve करता है:

  1. Gmail-hook override.
  2. Per-job `--model`.
  3. Stored cron-session model override (जब user ने कोई चुना हो).
  4. Agent या default model selection.


### Fast mode

Isolated cron fast mode resolved live model selection follow करता है. Model config `params.fastMode` default रूप से apply होता है, लेकिन stored session `fastMode` override अब भी config पर wins करता है. जब resolved mode `auto` हो, cutoff selected model के `params.fastAutoOnSeconds` value का उपयोग करता है, default 60 seconds है.

### Live model switch retries

यदि isolated run `LiveSessionModelSwitchError` throw करता है, तो cron retry करने से पहले active run के लिए switched provider और model (और मौजूद होने पर switched auth profile override) persist करता है. Outer retry loop initial attempt के बाद दो switch retries तक bounded है, फिर हमेशा loop करने के बजाय abort करता है.

## Run output and denials

### Stale acknowledgement suppression

Isolated cron turns stale acknowledgement-only replies को suppress करते हैं. यदि पहला result केवल interim status update है और eventual answer के लिए कोई descendant subagent run responsible नहीं है, तो cron delivery से पहले real result के लिए एक बार फिर prompt करता है.

### Silent token suppression

यदि isolated cron run केवल silent token (`NO_REPLY` या `no_reply`) return करता है, तो cron direct outbound delivery और fallback queued summary path दोनों suppress करता है, इसलिए chat पर कुछ भी वापस post नहीं होता.

### Structured denials

पृथक Cron रन एम्बेडेड रन से संरचित निष्पादन-अस्वीकृति मेटाडेटा को आधिकारिक अस्वीकृति संकेत के रूप में इस्तेमाल करते हैं। जब नेस्टेड संरचित त्रुटि संदेश `SYSTEM_RUN_DENIED` या `INVALID_REQUEST` से शुरू होता है, तो वे node-host `UNAVAILABLE` रैपर का भी सम्मान करते हैं।

Cron अंतिम-आउटपुट गद्य या अनुमोदन-जैसे दिखने वाले अस्वीकृति वाक्यांशों को अस्वीकृति के रूप में वर्गीकृत नहीं करता, जब तक कि एम्बेडेड रन संरचित अस्वीकृति मेटाडेटा भी उपलब्ध न कराए, इसलिए सामान्य सहायक टेक्स्ट को अवरुद्ध कमांड नहीं माना जाता।

`cron list` और रन इतिहास अवरुद्ध कमांड को `ok` के रूप में रिपोर्ट करने के बजाय अस्वीकृति कारण दिखाते हैं।

## रखरखाव

रखरखाव और pruning को config में नियंत्रित किया जाता है:

  * `cron.sessionRetention` (डिफॉल्ट `24h`) पूर्ण हो चुके पृथक रन सेशन को prunes करता है।
  * `cron.runLog.keepLines` प्रति जॉब रखी गई SQLite रन-इतिहास पंक्तियों को prunes करता है। `cron.runLog.maxBytes` पुराने file-backed रन लॉग के साथ compatibility के लिए स्वीकार्य रहता है।


## पुराने जॉब माइग्रेट करना

## सामान्य edits

message बदले बिना delivery settings update करें:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel telegram --to "123456789"
[/code]

किसी पृथक job के लिए delivery disable करें:

bashCopy code
[code]
    openclaw cron edit <job-id> --no-deliver
[/code]

किसी पृथक job के लिए lightweight bootstrap context enable करें:

bashCopy code
[code]
    openclaw cron edit <job-id> --light-context
[/code]

किसी specific channel में announce करें:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel slack --to "channel:C1234567890"
[/code]

Telegram forum topic में announce करें:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel telegram --to "-1001234567890" --thread-id 42
[/code]

lightweight bootstrap context के साथ एक पृथक job बनाएं:

bashCopy code
[code]
    openclaw cron create "0 7 * * *" \  "Summarize overnight updates." \  --name "Lightweight morning brief" \  --session isolated \  --light-context \  --no-deliver
[/code]

`--light-context` केवल isolated agent-turn jobs पर लागू होता है। Cron runs के लिए, lightweight mode पूरे workspace bootstrap set को inject करने के बजाय bootstrap context खाली रखता है।

exact argv, cwd, env, stdin, और output limits के साथ command job बनाएं:

bashCopy code
[code]
    openclaw cron create "*/30 * * * *" \  --name "Position export" \  --command-argv '["node","scripts/export-position.mjs"]' \  --command-cwd "/srv/app" \  --command-env "NODE_ENV=production" \  --command-input '{"mode":"summary"}' \  --timeout-seconds 120 \  --no-output-timeout-seconds 30 \  --output-max-bytes 65536 \  --webhook "https://example.invalid/openclaw/cron"
[/code]

## सामान्य admin commands

Manual run और inspection:

bashCopy code
[code]
    openclaw cron listopenclaw cron list --agent opsopenclaw cron get <job-id>openclaw cron show <job-id>openclaw cron run <job-id>openclaw cron run <job-id> --dueopenclaw cron run <job-id> --wait --wait-timeout 10mopenclaw cron run <job-id> --wait --wait-timeout 10m --poll-interval 2sopenclaw cron runs --id <job-id> --limit 50openclaw cron runs --id <job-id> --run-id <run-id>
[/code]

`openclaw cron list` डिफॉल्ट रूप से सभी matching jobs दिखाता है। केवल वे jobs दिखाने के लिए `--agent <id>` pass करें जिनकी effective normalized agent id match करती है; stored agent id के बिना jobs configured default agent के रूप में गिने जाते हैं।

`openclaw cron get <job-id>` stored job JSON सीधे लौटाता है। जब आपको delivery-route preview के साथ human-readable view चाहिए, तो `cron show <job-id>` इस्तेमाल करें।

`cron list --json` और `cron show <job-id> --json` प्रत्येक job पर top-level `status` field शामिल करते हैं, जिसे `enabled`, `state.runningAtMs`, और `state.lastRunStatus` से compute किया जाता है। Values: `disabled`, `running`, `ok`, `error`, `skipped`, या `idle`। यह human-readable status column को mirror करता है ताकि external tooling job state को फिर से derive किए बिना पढ़ सके।

`cron runs` entries में intended Cron target, resolved target, message-tool sends, fallback use, और delivered state के साथ delivery diagnostics शामिल होते हैं।

Agent और session retargeting:

bashCopy code
[code]
    openclaw cron edit <job-id> --agent opsopenclaw cron edit <job-id> --clear-agentopenclaw cron edit <job-id> --session currentopenclaw cron edit <job-id> --session "session:daily-brief"
[/code]

`openclaw cron add` agent-turn jobs पर `--agent` omit होने पर warning देता है और default agent (`main`) पर fallback करता है। specific agent pin करने के लिए create time पर `--agent <id>` pass करें।

Delivery tweaks:

bashCopy code
[code]
    openclaw cron edit <job-id> --announce --channel slack --to "channel:C1234567890"openclaw cron edit <job-id> --webhook "https://example.invalid/openclaw/cron"openclaw cron edit <job-id> --best-effort-deliveropenclaw cron edit <job-id> --no-best-effort-deliveropenclaw cron edit <job-id> --no-deliver
[/code]

## संबंधित

  * [CLI reference](</hi/cli>)
  * [Scheduled tasks](</hi/automation/cron-jobs>)


Was this useful?YesNo

Open issue