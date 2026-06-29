---
title: स्लैश कमांड
source_url: https://docs.openclaw.ai/hi/tools/slash-commands
scraped_at: 2026-06-29
---

CapabilitiesSkills

Gateway उन commands को संभालता है जो `/` से शुरू होने वाले standalone messages के रूप में भेजे जाते हैं। Host-only bash commands `! <cmd>` का उपयोग करते हैं (`/bash <cmd>` alias के रूप में)।

जब कोई conversation किसी ACP session से bound होती है, सामान्य text ACP harness को route होता है। Gateway management commands local रहते हैं: `/acp ...` हमेशा OpenClaw command handler तक पहुंचता है, और `/status` तथा `/unfocus` surface के लिए command handling enabled होने पर local रहते हैं।

## तीन command प्रकार

**Commands** Gateway द्वारा संभाले जाने वाले standalone `/...` messages। इन्हें message में केवल content के रूप में भेजना चाहिए। **Directives** `/think`, `/fast`, `/verbose`, `/trace`, `/reasoning`, `/elevated`, `/exec`, `/model`, `/queue` — model के देखने से पहले message से हटा दिए जाते हैं। अकेले भेजे जाने पर session settings persist करते हैं; अन्य text के साथ भेजे जाने पर inline hints की तरह काम करते हैं। **Inline shortcuts** `/help`, `/commands`, `/status`, `/whoami` — तुरंत run होते हैं और remaining text model के देखने से पहले हटा दिए जाते हैं। केवल authorized senders।

Directive behavior details

  * Directives को model के देखने से पहले message से हटा दिया जाता है।
  * **directive-only** messages में (message केवल directives है), वे session में persist होते हैं और acknowledgement के साथ reply करते हैं।
  * अन्य text वाले **normal chat** messages में, वे inline hints की तरह काम करते हैं और session settings persist **नहीं** करते।
  * Directives केवल **authorized senders** के लिए apply होते हैं। यदि `commands.allowFrom` set है, तो वही एकमात्र allowlist used होती है; अन्यथा authorization channel allowlists/pairing और `commands.useAccessGroups` से आता है। Unauthorized senders के लिए directives plain text की तरह treat होते हैं।


## Configuration

json5Copy code
[code]
    {  commands: {    native: "auto",    nativeSkills: "auto",    text: true,    bash: false,    bashForegroundMs: 2000,    config: false,    mcp: false,    plugins: false,    debug: false,    restart: true,    ownerAllowFrom: ["discord:123456789012345678"],    ownerDisplay: "raw",    ownerDisplaySecret: "${OWNER_ID_HASH_SECRET}",    allowFrom: {      "*": ["user1"],      discord: ["user:123"],    },    useAccessGroups: true,  },}
[/code]

chat messages में `/...` parsing enabled करता है। Native commands के बिना surfaces (WhatsApp, WebChat, Signal, iMessage, Google Chat, Microsoft Teams) पर, text commands `false` set होने पर भी काम करते हैं।

native commands register करता है। Auto: Discord/Telegram के लिए on; Slack के लिए off; native support के बिना providers के लिए ignored। Per-channel override `channels.<provider>.commands.native` से करें। Discord पर, `false` slash-command registration skip करता है; पहले registered commands हटाए जाने तक visible रह सकते हैं।

Supported होने पर skill commands को natively register करता है। Auto: Discord/Telegram के लिए on; Slack के लिए off। Override `channels.<provider>.commands.nativeSkills` से करें।

host shell commands run करने के लिए `! <cmd>` enabled करता है (`/bash <cmd>` alias)। इसके लिए `tools.elevated` allowlists चाहिए।

background mode पर switch करने से पहले bash कितनी देर wait करता है (`0` तुरंत background में भेजता है)।

`/config` enabled करता है (`openclaw.json` पढ़ता/लिखता है)। Owner-only।

`/mcp` enabled करता है (`mcp.servers` के तहत OpenClaw-managed MCP config पढ़ता/लिखता है)। Owner-only।

`/plugins` enabled करता है (plugin discovery/status और install + enable/disable)। Writes के लिए owner-only।

`/debug` enabled करता है (runtime-only config overrides)। Owner-only।

`/restart` और gateway restart tool actions enabled करता है।

owner-only command surfaces के लिए explicit owner allowlist। यह `commands.allowFrom` और DM pairing access से separate है।

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImNoYW5uZWxzLjxjaGFubmVs .commands.enforceOwnerForCommands" type="boolean" default="false"> Per-channel: owner-only commands के लिए owner identity required करता है। `true` होने पर, sender को `commands.ownerAllowFrom` से match करना चाहिए या internal `operator.admin` scope रखना चाहिए। Wildcard `allowFrom` entry **पर्याप्त नहीं** है।

system prompt में owner ids कैसे appear होते हैं, इसे control करता है।

`commands.ownerDisplay: "hash"` होने पर used HMAC secret।

command authorization के लिए per-provider allowlist। Configured होने पर, यह commands और directives के लिए **एकमात्र** authorization source है। Global default के लिए `"*"` का उपयोग करें; provider-specific keys इसे override करती हैं।

`commands.allowFrom` set न होने पर commands के लिए allowlists/policies enforce करता है।

## Command सूची

Commands तीन sources से आते हैं:

  * **Core built-ins:** `src/auto-reply/commands-registry.shared.ts`
  * **Generated dock commands:** `src/auto-reply/commands-registry.data.ts`
  * **Plugin commands:** plugin `registerCommand()` calls


Availability config flags, channel surface, और installed/enabled plugins पर depend करती है।

### Core commands

Sessions and runs

Command | विवरण  
---|---  
`/new [model]` | current session archive करें और fresh session शुरू करें  
`/reset [soft [message]]` | current session को in place reset करें। `soft` transcript रखता है, reused CLI backend session ids drop करता है, और startup फिर से run करता है  
`/name <title>` | current session को name या rename करें। current name और suggestion देखने के लिए title omit करें  
`/compact [instructions]` | session context compact करें। [Compaction](</hi/concepts/compaction>) देखें  
`/stop` | current run abort करें  
`/session idle <duration|off>` | thread-binding idle expiry manage करें  
`/session max-age <duration|off>` | thread-binding max-age expiry manage करें  
`/export-session [path]` | current session को HTML में export करें। Alias: `/export`  
`/export-trajectory [path]` | current session के लिए JSONL trajectory bundle export करें। Alias: `/trajectory`  
  
Model and run controls

Command | विवरण  
---|---  
`/think <level|default>` | thinking level set करें या session override clear करें। Aliases: `/thinking`, `/t`  
`/verbose on|off|full` | verbose output toggle करें। Alias: `/v`  
`/trace on|off` | current session के लिए plugin trace output toggle करें  
`/fast [status|auto|on|off|default]` | fast mode show, set, या clear करें  
`/reasoning [on|off|stream]` | reasoning visibility toggle करें। Alias: `/reason`  
`/elevated [on|off|ask|full]` | elevated mode toggle करें। Alias: `/elev`  
`/exec host=<auto|sandbox|gateway|node> security=<deny|allowlist|full> ask=<off|on-miss|always> node=<id>` | exec defaults show या set करें  
`/model [name|#|status]` | model show या set करें  
`/models [provider] [page] [limit=<n>|all]` | configured/auth-available providers या models list करें  
`/queue <mode>` | active-run queue behavior manage करें। [Queue](</hi/concepts/queue>) और [Queue steering](</hi/concepts/queue-steering>) देखें  
`/steer <message>` | active run में guidance inject करें। Alias: `/tell`। [Steer](</hi/tools/steer>) देखें  
  
verbose / trace / fast / reasoning safety

  * `/verbose` debugging के लिए है — normal use में इसे **off** रखें।
  * `/trace` केवल plugin-owned trace/debug lines reveal करता है; normal verbose chatter off रहता है।
  * `/fast auto|on|off` session override persist करता है; इसे clear करने के लिए Sessions UI `inherit` option का उपयोग करें।
  * `/fast` provider-specific है: OpenAI/Codex इसे `service_tier=priority` से map करते हैं; direct Anthropic requests इसे `service_tier=auto` या `standard_only` से map करते हैं।
  * `/reasoning`, `/verbose`, और `/trace` group settings में risky हैं — वे internal reasoning या plugin diagnostics reveal कर सकते हैं। Group chats में इन्हें off रखें।

Model switching details

  * `/model` new model को तुरंत session में persist करता है।
  * यदि agent idle है, तो next run इसे तुरंत use करता है।
  * यदि run active है, तो switch pending marked होता है और अगले clean retry point पर apply होता है।


Discovery and status

Command | विवरण  
---|---  
`/help` | short help summary show करें  
`/commands` | generated command catalog show करें  
`/tools [compact|verbose]` | current agent अभी क्या use कर सकता है, यह show करें  
`/status` | execution/runtime status, Gateway और system uptime, plugin health, plus provider usage/quota show करें  
`/status plugins` | detailed plugin health show करें: load errors, quarantines, channel failures, dependency issues, compatibility notices  
`/goal [status|start|pause|resume|complete|block|clear] ...` | current session का durable [goal](</hi/tools/goal>) manage करें  
`/diagnostics [note]` | Owner-only support-report flow। हर बार exec approval मांगता है  
`/crestodian <request>` | owner DM से Crestodian setup और repair helper run करें  
`/tasks` | current session के active/recent background tasks list करें  
`/context [list|detail|map|json]` | context कैसे assembled होता है, explain करें  
`/whoami` | आपका sender id show करें। Alias: `/id`  
`/usage off|tokens|full|reset|cost` | per-response usage footer control करें (`reset`/`inherit`/`clear`/`default` session override को clear करके configured default को फिर से inherit करता है) या local cost summary print करें  
  
Skills, allowlists, approvals

Command | विवरण  
---|---  
`/skill <name> [input]` | name से skill run करें  
`/allowlist [list|add|remove] ...` | allowlist entries manage करें। Text-only  
`/approve <id> <decision>` | exec या plugin approval prompts resolve करें  
`/btw <question>` | session context बदले बिना side question पूछें। Alias: `/side`। [BTW](</hi/tools/btw>) देखें  
  
Subagents और ACP

कमांड | विवरण  
---|---  
`/subagents list|log|info` | वर्तमान सत्र के लिए sub-agent रन जांचें  
`/acp spawn|cancel|steer|close|sessions|status|set-mode|set|cwd|permissions|timeout|model|reset-options|doctor|install|help` | ACP सत्र और runtime विकल्प प्रबंधित करें  
`/focus <target>` | वर्तमान Discord थ्रेड या Telegram विषय को किसी सत्र लक्ष्य से बांधें  
`/unfocus` | वर्तमान थ्रेड बाइंडिंग हटाएं  
`/agents` | वर्तमान सत्र के लिए थ्रेड-बाउंड agents सूचीबद्ध करें  
  
केवल स्वामी लेखन और admin

कमांड | आवश्यक | विवरण  
---|---|---  
`/config show|get|set|unset` | `commands.config: true` | `openclaw.json` पढ़ें या लिखें। केवल स्वामी  
`/mcp show|get|set|unset` | `commands.mcp: true` | OpenClaw-प्रबंधित MCP server config पढ़ें या लिखें। केवल स्वामी  
`/plugins list|inspect|show|get|install|enable|disable` | `commands.plugins: true` | Plugin स्थिति जांचें या बदलें। लिखने के लिए केवल स्वामी। उपनाम: `/plugin`  
`/debug show|set|unset|reset` | `commands.debug: true` | केवल runtime config overrides। केवल स्वामी  
`/restart` | `commands.restart: true` (डिफ़ॉल्ट) | OpenClaw फिर से शुरू करें  
`/send on|off|inherit` | स्वामी | send policy सेट करें  
  
आवाज़, TTS, channel नियंत्रण

कमांड | विवरण  
---|---  
`/tts on|off|status|chat|latest|provider|limit|summary|audio|help` | TTS नियंत्रित करें। देखें [TTS](</hi/tools/tts>)  
`/activation mention|always` | group activation mode सेट करें  
`/bash <command>` | host shell command चलाएं। उपनाम: `! <command>`। `commands.bash: true` आवश्यक  
`!poll [sessionId]` | background bash job जांचें  
`!stop [sessionId]` | background bash job रोकें  
  
### Dock कमांड

Dock कमांड सक्रिय सत्र के reply route को किसी दूसरे linked channel पर स्विच करते हैं। सेटअप और troubleshooting के लिए [Channel docking](</hi/concepts/channel-docking>) देखें।

native-command support वाले channel plugins से जनरेट किए गए:

  * `/dock-discord` (उपनाम: `/dock_discord`)
  * `/dock-mattermost` (उपनाम: `/dock_mattermost`)
  * `/dock-slack` (उपनाम: `/dock_slack`)
  * `/dock-telegram` (उपनाम: `/dock_telegram`)


Dock कमांड के लिए `session.identityLinks` आवश्यक है। source sender और target peer एक ही identity group में होने चाहिए।

### Bundled plugin कमांड

कमांड | विवरण  
---|---  
`/dreaming [on|off|status|help]` | memory dreaming टॉगल करें। देखें [Dreaming](</hi/concepts/dreaming>)  
`/pair [qr|status|pending|approve|cleanup|notify]` | device pairing प्रबंधित करें। देखें [Pairing](</hi/channels/pairing>)  
`/phone status|arm ...|disarm` | high-risk phone node कमांड को अस्थायी रूप से arm करें  
`/voice status|list|set <voiceId>` | Talk voice config प्रबंधित करें। Discord native नाम: `/talkvoice`  
`/card ...` | LINE rich card presets भेजें। देखें [LINE](</hi/channels/line>)  
`/codex status|models|threads|resume|compact|review|diagnostics|account|mcp|skills` | Codex app-server harness नियंत्रित करें। देखें [Codex harness](</hi/plugins/codex-harness>)  
  
केवल QQBot: `/bot-ping`, `/bot-version`, `/bot-help`, `/bot-upgrade`, `/bot-logs`

### Skill कमांड

User-invocable skills slash commands के रूप में उपलब्ध हैं:

  * `/skill <name> [input]` generic entrypoint के रूप में हमेशा काम करता है।
  * Skills direct commands के रूप में register हो सकती हैं (जैसे OpenProse के लिए `/prose`)।
  * Native skill-command registration `commands.nativeSkills` और `channels.<provider>.commands.nativeSkills` से नियंत्रित होती है।
  * नामों को `a-z0-9_` में sanitize किया जाता है (अधिकतम 32 अक्षर); collisions को numeric suffixes मिलते हैं।


Skill command dispatch

डिफ़ॉल्ट रूप से, skill commands सामान्य request की तरह model तक route होते हैं।

Skills सीधे किसी tool तक route करने के लिए `command-dispatch: tool` declare कर सकती हैं (deterministic, model involvement नहीं)। उदाहरण: `/prose` (OpenProse plugin) — देखें [OpenProse](</hi/prose>).

Native command arguments

Discord dynamic options और button menus के लिए autocomplete का उपयोग करता है, जब required args छोड़े जाते हैं। Telegram और Slack choices वाले commands के लिए button menu दिखाते हैं। Dynamic choices target session model के विरुद्ध resolve होते हैं, इसलिए model- specific options जैसे `/think` levels session के `/model` override का पालन करते हैं।

## `/tools` — agent अभी क्या उपयोग कर सकता है

`/tools` एक runtime question का उत्तर देता है: **यह agent अभी इस conversation में क्या उपयोग कर सकता है** — static config catalog नहीं।

textCopy code
[code]
    /tools         # compact view/tools verbose # with short descriptions
[/code]

Results session-scoped हैं। agent, channel, thread, sender authorization, या model बदलने से output बदल सकता है। profile और override editing के लिए, Control UI Tools panel या config surfaces का उपयोग करें।

## `/model` — model चयन

textCopy code
[code]
    /model             # show model picker/model list        # same/model 3           # select by number from picker/model openai/gpt-5.4/model opus@anthropic:default/model default     # clear the session model selection/model status      # detailed view with endpoint and API mode
[/code]

Discord पर, `/model` और `/models` provider और model dropdowns के साथ interactive picker खोलते हैं। picker `agents.defaults.models` का सम्मान करता है, जिसमें `provider/*` entries शामिल हैं।

## `/config` — on-disk config writes

textCopy code
[code]
    /config show/config show messages.responsePrefix/config get messages.responsePrefix/config set messages.responsePrefix="[openclaw]"/config unset messages.responsePrefix
[/code]

Config को write से पहले validate किया जाता है। invalid changes reject किए जाते हैं। `/config` updates restarts के बाद भी persist रहते हैं।

## `/mcp` — MCP server config

textCopy code
[code]
    /mcp show/mcp show context7/mcp set context7={"command":"uvx","args":["context7-mcp"]}/mcp unset context7
[/code]

`/mcp` config को embedded-agent project settings में नहीं, OpenClaw config में store करता है।

## `/debug` — केवल runtime overrides

textCopy code
[code]
    /debug show/debug set messages.responsePrefix="[openclaw]"/debug set channels.whatsapp.allowFrom=["+1555","+4477"]/debug unset messages.responsePrefix/debug reset
[/code]

## `/plugins` — plugin प्रबंधन

textCopy code
[code]
    /plugins/plugins list/plugin show context7/plugins enable context7/plugins disable context7/plugins install ./path/to/plugin
[/code]

`/plugins enable|disable` plugin config update करता है और नए agent turns के लिए Gateway plugin runtime को hot-reload करता है। `/plugins install` managed Gateways को अपने आप restart करता है क्योंकि plugin source modules बदल गए हैं।

## `/trace` — plugin trace output

textCopy code
[code]
    /trace          # show current trace state/trace on/trace off
[/code]

`/trace` full verbose mode के बिना session-scoped plugin trace/debug lines दिखाता है। यह `/debug` (runtime overrides) या `/verbose` (normal tool output) की जगह नहीं लेता।

## `/btw` — side questions

`/btw` current session context के बारे में quick side question है। उपनाम: `/side`.

textCopy code
[code]
    /btw what are we doing right now?/side what changed while the main run continued?
[/code]

सामान्य message के विपरीत:

  * current session को background context के रूप में उपयोग करता है।
  * Codex harness sessions में, ephemeral Codex side thread के रूप में चलता है।
  * future session context नहीं बदलता।
  * transcript history में नहीं लिखा जाता।


पूर्ण behavior के लिए [BTW side questions](</hi/tools/btw>) देखें।

## Surface notes

Session scoping per surface

  * **Text commands:** normal chat session में चलते हैं (DMs `main` share करते हैं, groups का अपना session होता है)।
  * **Native Discord commands:** `agent:<agentId>:discord:slash:<userId>`
  * **Native Slack commands:** `agent:<agentId>:slack:slash:<userId>` (prefix `channels.slack.slashCommand.sessionPrefix` के जरिए configurable)
  * **Native Telegram commands:** `telegram:slash:<userId>` (`CommandTargetSessionKey` के जरिए chat session को target करता है)
  * **`/stop`** current run को abort करने के लिए active chat session को target करता है।

Slack specifics

`channels.slack.slashCommand` single `/openclaw`-style command support करता है। `commands.native: true` के साथ, हर built-in command के लिए एक Slack slash command बनाएं। `/agentstatus` (`/status` नहीं) register करें क्योंकि Slack `/status` reserve करता है। Text `/status` अब भी Slack messages में काम करता है।

Fast path and inline shortcuts

  * allowlisted senders के command-only messages तुरंत handle किए जाते हैं (queue + model bypass)।
  * Inline shortcuts (`/help`, `/commands`, `/status`, `/whoami`) normal messages में embedded होने पर भी काम करते हैं और बाकी text model को दिखने से पहले strip कर दिए जाते हैं।
  * Unauthorized command-only messages silently ignored होते हैं; inline `/...` tokens plain text की तरह treat किए जाते हैं।

Argument notes

  * Commands command और args के बीच optional `:` स्वीकार करते हैं (`/think: high`, `/send: on`)।
  * `/new <model>` model alias, `provider/model`, या provider name (fuzzy match) स्वीकार करता है; अगर कोई match नहीं है, तो text को message body माना जाता है।
  * `/allowlist add|remove` के लिए `commands.config: true` आवश्यक है और यह channel `configWrites` का सम्मान करता है।


## Provider usage और status

  * **Provider usage/quota** (जैसे, "Claude 80% left") current model provider के लिए `/status` में दिखता है, जब usage tracking enabled हो।
  * **Token/cache lines** `/status` में latest transcript usage entry पर fall back कर सकती हैं, जब live session snapshot sparse हो।
  * **Execution बनाम runtime:** `/status` effective sandbox path के लिए `Execution` और session कौन चला रहा है इसके लिए `Runtime` report करता है: `OpenClaw Default`, `OpenAI Codex`, कोई CLI backend, या ACP backend।
  * **Per-response tokens/cost:** `/usage off|tokens|full` से controlled।
  * `/model status` models/auth/endpoints के बारे में है, usage के बारे में नहीं।


## संबंधित

[**Skills** Skill slash commands कैसे registered और gated होते हैं। ](</hi/tools/skills>) [**Skills बनाना** ऐसी skill बनाएं जो अपना slash command register करती है। ](</hi/tools/creating-skills>) [**BTW** Session context बदले बिना side questions। ](</hi/tools/btw>) [**Steer** `/steer` से mid-run agent को guide करें। ](</hi/tools/steer>)

Was this useful?YesNo

Open issue