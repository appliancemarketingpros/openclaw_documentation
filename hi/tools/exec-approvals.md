---
title: Exec अनुमोदन
source_url: https://docs.openclaw.ai/hi/tools/exec-approvals
scraped_at: 2026-06-29
---

CapabilitiesTools

Exec अनुमोदन **companion app / node host guardrail** हैं, जो किसी sandboxed agent को वास्तविक host (`gateway` या `node`) पर commands चलाने देते हैं। एक सुरक्षा interlock: commands केवल तब अनुमत होते हैं जब policy + allowlist + (वैकल्पिक) user approval सभी सहमत हों। Exec approvals, tool policy और elevated gating के **ऊपर** stack होते हैं (जब तक elevated को `full` पर सेट न किया गया हो, जो approvals को छोड़ देता है)।

`deny`, `allowlist`, `ask`, `auto`, `full`, Codex Guardian mapping, और ACPX harness permissions के mode-first overview के लिए, देखें [Permission modes](</hi/tools/permission-modes>)।

## प्रभावी policy की जांच करना

Command | यह क्या दिखाता है  
---|---  
`openclaw approvals get` / `--gateway` / `--node <id|name|ip>` | Requested policy, host policy sources, और effective result।  
`openclaw exec-policy show` | Local-machine merged view।  
`openclaw exec-policy set` / `preset` | Local requested policy को local host approvals file के साथ एक step में synchronize करें।  
  
जब कोई local scope `host=node` request करता है, तो `exec-policy show` उस scope को runtime पर node-managed के रूप में report करता है, बजाय इसके कि local approvals file को source of truth बताया जाए।

यदि companion app UI **उपलब्ध नहीं** है, तो कोई भी request जो सामान्यतः prompt करेगी, **ask fallback** (default: `deny`) द्वारा resolve की जाती है।

## यह कहां लागू होता है

Exec approvals execution host पर locally enforce किए जाते हैं:

  * **Gateway host** → gateway machine पर `openclaw` process।
  * **Node host** → node runner (macOS companion app या headless node host)।


### Trust model

  * Gateway-authenticated callers उस Gateway के लिए trusted operators होते हैं।
  * Paired nodes उस trusted operator capability को node host तक extend करते हैं।
  * Exec approvals accidental execution risk को घटाते हैं, लेकिन **न तो** per-user auth boundary हैं और न filesystem read-only policy।
  * एक बार approved होने के बाद, command selected host या sandbox filesystem permissions के अनुसार files mutate कर सकता है।
  * Approved node-host runs canonical execution context bind करते हैं: canonical cwd, exact argv, env binding जब मौजूद हो, और applicable होने पर pinned executable path।
  * Shell scripts और direct interpreter/runtime file invocations के लिए, OpenClaw एक concrete local file operand bind करने की भी कोशिश करता है। यदि वह bound file approval के बाद लेकिन execution से पहले बदल जाती है, तो drifted content execute करने के बजाय run deny कर दिया जाता है।
  * File binding जानबूझकर best-effort है, हर interpreter/runtime loader path का complete semantic model **नहीं** । यदि approval mode bind करने के लिए exactly one concrete local file identify नहीं कर सकता, तो वह full coverage का दिखावा करने के बजाय approval-backed run mint करने से इंकार करता है।


### macOS split

  * **node host service** local IPC पर `system.run` को **macOS app** तक forward करता है।
  * **macOS app** approvals enforce करता है और UI context में command execute करता है।


## Settings और storage

Approvals execution host पर local JSON file में रहते हैं। जब `OPENCLAW_STATE_DIR` set होता है, तो file उस state directory का अनुसरण करती है; अन्यथा यह default OpenClaw state directory उपयोग करती है:

textCopy code
[code]
    $OPENCLAW_STATE_DIR/exec-approvals.json# otherwise~/.openclaw/exec-approvals.json
[/code]

Default approval socket समान root का अनुसरण करता है: `$OPENCLAW_STATE_DIR/exec-approvals.sock`, या variable unset होने पर `~/.openclaw/exec-approvals.sock`।

Example schema:

jsonCopy code
[code]
    {  "version": 1,  "socket": {    "path": "~/.openclaw/exec-approvals.sock",    "token": "base64url-token"  },  "defaults": {    "security": "deny",    "ask": "on-miss",    "askFallback": "deny",    "autoAllowSkills": false  },  "agents": {    "main": {      "security": "allowlist",      "ask": "on-miss",      "askFallback": "deny",      "autoAllowSkills": true,      "allowlist": [        {          "id": "B0C8C0B3-2C2D-4F8A-9A3C-5A4B3C2D1E0F",          "pattern": "~/Projects/**/bin/rg",          "source": "allow-always",          "commandText": "rg -n TODO",          "lastUsedAt": 1737150000000,          "lastUsedCommand": "rg -n TODO",          "lastResolvedPath": "/Users/user/Projects/.../bin/rg"        }      ]    }  }}
[/code]

## Policy knobs

### `tools.exec.mode`

`tools.exec.mode` host exec के लिए preferred normalized policy surface है। Values हैं:

  * `deny` \- host exec को block करें।
  * `allowlist` \- केवल allowlisted commands बिना पूछे चलाएं।
  * `ask` \- allowlist policy उपयोग करें और misses पर पूछें।
  * `auto` \- allowlist policy उपयोग करें, deterministic matches सीधे चलाएं, और approval misses को human approval route पर fallback करने से पहले OpenClaw के native auto reviewer के माध्यम से भेजें।
  * `full` \- approval prompts के बिना host exec चलाएं।


Legacy `tools.exec.security` / `tools.exec.ask` supported रहते हैं और अभी भी तब win करते हैं जब narrower session या agent scope पर set हों।

### `exec.security`

  * `deny` \- सभी host exec requests block करें।
  * `allowlist` \- केवल allowlisted commands allow करें।
  * `full` \- सब कुछ allow करें (elevated के equivalent)।


### `exec.ask`

Host exec के लिए configured ask policy। `tools.exec.ask` और host approvals defaults से baseline approval prompt behavior control करता है। Per-call `ask` tool parameter (देखें [Exec tool](</hi/tools/exec#parameters>)) उस baseline को केवल harden कर सकता है, और channel-origin model calls इसे ignore करते हैं जब effective host ask `off` हो।

  * `off` \- कभी prompt न करें।
  * `on-miss` \- केवल तब prompt करें जब allowlist match नहीं करता।
  * `always` \- हर command पर prompt करें। `allow-always` durable trust prompts को **suppress नहीं करता** जब effective ask mode `always` हो।


### `askFallback`

Resolution जब prompt required हो लेकिन कोई UI reachable न हो। यदि यह field छोड़ी गई है, तो OpenClaw default रूप से `deny` उपयोग करता है।

  * `deny` \- block करें।
  * `allowlist` \- केवल allowlist match होने पर allow करें।
  * `full` \- allow करें।


### `tools.exec.strictInlineEval`

जब `true`, OpenClaw inline code-eval forms को approval-only मानता है, भले ही interpreter binary स्वयं allowlisted हो। उन interpreter loaders के लिए defense-in-depth जो एक stable file operand से cleanly map नहीं होते।

Strict mode जिन examples को पकड़ता है:

  * `python -c`
  * `node -e`, `node --eval`, `node -p`
  * `ruby -e`
  * `perl -e`, `perl -E`
  * `php -r`
  * `lua -e`
  * `osascript -e`


Strict mode में इन commands को अभी भी explicit approval चाहिए, और `allow-always` उनके लिए automatically नई allowlist entries persist नहीं करता।

### `tools.exec.commandHighlighting`

Exec approval prompts में केवल presentation control करता है। Enabled होने पर, OpenClaw parser-derived command spans attach कर सकता है ताकि Web approval prompts command tokens highlight कर सकें। Command text highlighting enable करने के लिए इसे `true` पर set करें।

यह setting `security`, `ask`, allowlist matching, strict inline-eval behavior, approval forwarding, या command execution को **नहीं** बदलती। इसे globally `tools.exec.commandHighlighting` के तहत या per agent `agents.list[].tools.exec.commandHighlighting` के तहत set किया जा सकता है।

## YOLO mode (no-approval)

यदि आप चाहते हैं कि host exec approval prompts के बिना चले, तो आपको **दोनों** policy layers खोलनी होंगी - OpenClaw config में requested exec policy (`tools.exec.*`) **और** execution host approvals file में host-local approvals policy।

OpenClaw छोड़े गए `askFallback` को default रूप से `deny` करता है। जब no-UI approval prompt को allow पर fallback करना चाहिए, तो host `askFallback` को स्पष्ट रूप से `full` पर set करें।

Layer | YOLO setting  
---|---  
`tools.exec.security` | `gateway`/`node` पर `full`  
`tools.exec.ask` | `off`  
Host `askFallback` | `full`  
  
CLI-backed providers जो अपना noninteractive permission mode expose करते हैं इस policy का अनुसरण कर सकते हैं। Claude CLI `--permission-mode bypassPermissions` जोड़ता है जब OpenClaw की effective exec policy YOLO होती है। OpenClaw-managed Claude live sessions के लिए, OpenClaw की effective exec policy Claude के native permission mode पर authoritative है: YOLO live launches को `--permission-mode bypassPermissions` में normalize करता है, और restrictive effective exec policy live launches को `--permission-mode default` में normalize करती है, भले ही raw Claude backend args कोई दूसरा mode specify करें।

यदि आप अधिक conservative setup चाहते हैं, तो OpenClaw exec policy को फिर से `allowlist` / `on-miss` या `deny` तक tighten करें।

### Persistent gateway-host "never prompt" setup

* ### Requested config policy set करें

bashCopy code
[code]
    openclaw config set tools.exec.host gatewayopenclaw config set tools.exec.security fullopenclaw config set tools.exec.ask offopenclaw gateway restart
[/code]

* ### Host approvals file match करें

bashCopy code
[code]
    openclaw approvals set --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

### Local shortcut

bashCopy code
[code]
    openclaw exec-policy preset yolo
[/code]

वह local shortcut दोनों को update करता है:

  * Local `tools.exec.host/security/ask`।
  * Local approvals file defaults, जिसमें `askFallback: "full"` शामिल है।


यह जानबूझकर local-only है। Gateway-host या node-host approvals को remotely बदलने के लिए, `openclaw approvals set --gateway` या `openclaw approvals set --node <id|name|ip>` उपयोग करें।

### Node host

Node host के लिए, वही approvals file उस node पर apply करें:

bashCopy code
[code]
    openclaw approvals set --node <id|name|ip> --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

### Session-only shortcut

  * `/exec security=full ask=off` केवल वर्तमान सत्र को बदलता है।
  * `/elevated full` एक आपातकालीन शॉर्टकट है जो exec अनुमोदनों को केवल तब छोड़ता है जब अनुरोधित नीति और होस्ट अनुमोदन फ़ाइल दोनों `security: "full"` और `ask: "off"` पर हल हों। अधिक सख्त होस्ट फ़ाइल, जैसे `ask: "always"`, फिर भी संकेत दिखाती है।


यदि होस्ट अनुमोदन फ़ाइल कॉन्फ़िग से अधिक सख्त रहती है, तो अधिक सख्त होस्ट नीति ही प्रभावी रहती है।

## अनुमति-सूची (प्रति एजेंट)

अनुमति-सूचियाँ **प्रति एजेंट** होती हैं। यदि कई एजेंट मौजूद हैं, तो macOS ऐप में वह एजेंट बदलें जिसे आप संपादित कर रहे हैं। पैटर्न glob मिलान होते हैं।

पैटर्न हल किए गए बाइनरी पथ glob या केवल कमांड-नाम glob हो सकते हैं। केवल नाम उन कमांड से मिलते हैं जिन्हें `PATH` के माध्यम से चलाया गया हो, इसलिए `rg` `/opt/homebrew/bin/rg` से मिल सकता है जब कमांड `rg` हो, लेकिन **नहीं** `./rg` या `/tmp/rg` से। जब आप किसी एक विशिष्ट बाइनरी स्थान पर भरोसा करना चाहते हैं, तब पथ glob का उपयोग करें।

पुरानी `agents.default` प्रविष्टियाँ लोड पर `agents.main` में माइग्रेट की जाती हैं। `echo ok && pwd` जैसी shell chains को अभी भी हर शीर्ष-स्तरीय segment को अनुमति-सूची नियमों को पूरा करना होगा।

उदाहरण:

  * `rg`
  * `~/Projects/**/bin/peekaboo`
  * `~/.local/bin/*`
  * `/opt/homebrew/bin/rg`


### argPattern से arguments सीमित करना

जब किसी अनुमति-सूची प्रविष्टि को किसी बाइनरी और किसी विशिष्ट argument आकार से मिलना चाहिए, तब `argPattern` जोड़ें। OpenClaw नियमित अभिव्यक्ति का मूल्यांकन parsed command arguments के विरुद्ध करता है, executable token (`argv[0]`) को छोड़कर। हाथ से लिखी प्रविष्टियों के लिए, arguments को एक single space से जोड़ा जाता है, इसलिए जब आपको exact match चाहिए तब pattern को anchor करें।

jsonCopy code
[code]
    {  "version": 1,  "agents": {    "main": {      "allowlist": [        {          "pattern": "python3",          "argPattern": "^safe\\.py$"        }      ]    }  }}
[/code]

वह प्रविष्टि `python3 safe.py` को अनुमति देती है; `python3 other.py` अनुमति-सूची miss है। यदि उसी बाइनरी के लिए path-only प्रविष्टि भी मौजूद है, तो unmatched arguments अभी भी उस path-only प्रविष्टि पर वापस जा सकते हैं। जब लक्ष्य बाइनरी को घोषित arguments तक सीमित करना हो, तो path-only प्रविष्टि छोड़ दें।

approval flows द्वारा सहेजी गई प्रविष्टियाँ exact argv matching के लिए एक internal separator format का उपयोग कर सकती हैं। encoded value को हाथ से संपादित करने के बजाय उन प्रविष्टियों को दोबारा बनाने के लिए UI या approval flow को प्राथमिकता दें। यदि OpenClaw किसी command segment के लिए argv parse नहीं कर सकता, तो `argPattern` वाली प्रविष्टियाँ match नहीं करतीं।

हर अनुमति-सूची प्रविष्टि यह समर्थन करती है:

फ़ील्ड | अर्थ  
---|---  
`pattern` | हल किया गया बाइनरी पथ glob या केवल कमांड-नाम glob  
`argPattern` | वैकल्पिक argv regex; छोड़ी गई प्रविष्टियाँ path-only होती हैं  
`id` | UI पहचान के लिए उपयोग किया जाने वाला स्थिर UUID  
`source` | प्रविष्टि स्रोत, जैसे `allow-always`  
`commandText` | अनुमोदन flow ने प्रविष्टि बनाते समय capture किया गया command text  
`lastUsedAt` | आखिरी उपयोग का timestamp  
`lastUsedCommand` | आखिरी matched command  
`lastResolvedPath` | आखिरी हल किया गया बाइनरी पथ  
  
## skill CLI को auto-allow करना

जब **skill CLI को auto-allow करें** सक्षम होता है, तो ज्ञात skills द्वारा संदर्भित executables को nodes (macOS node या headless node host) पर अनुमति-सूचीबद्ध माना जाता है। यह skill bin list लाने के लिए Gateway RPC पर `skills.bins` का उपयोग करता है। यदि आप सख्त manual allowlists चाहते हैं, तो इसे अक्षम करें।

## सुरक्षित bins और approval forwarding

safe bins (stdin-only fast-path), interpreter binding विवरण, और approval prompts को Slack/Discord/Telegram पर forward करने (या उन्हें native approval clients के रूप में चलाने) के तरीके के लिए देखें [Exec अनुमोदन - उन्नत](</hi/tools/exec-approvals-advanced>)।

## Control UI संपादन

defaults, प्रति-एजेंट overrides, और allowlists संपादित करने के लिए **Control UI → Nodes → Exec अनुमोदन** card का उपयोग करें। एक scope (Defaults या कोई एजेंट) चुनें, policy बदलें, allowlist patterns जोड़ें/हटाएँ, फिर **Save** करें। UI हर pattern के लिए last-used metadata दिखाता है ताकि आप सूची को व्यवस्थित रख सकें।

target selector **Gateway** (local approvals) या किसी **Node** को चुनता है। Nodes को `system.execApprovals.get/set` (macOS app या headless node host) advertise करना होगा। यदि कोई node अभी तक exec approvals advertise नहीं करता, तो उसकी local approvals file को सीधे संपादित करें।

CLI: `openclaw approvals` gateway या node editing का समर्थन करता है - देखें [Approvals CLI](</hi/cli/approvals>)।

## अनुमोदन flow

जब prompt आवश्यक होता है, gateway operator clients को `exec.approval.requested` broadcast करता है। Control UI और macOS app इसे `exec.approval.resolve` के माध्यम से resolve करते हैं, फिर gateway approved request को node host पर forward करता है।

`host=node` के लिए, approval requests में canonical `systemRunPlan` payload शामिल होता है। gateway approved `system.run` requests forward करते समय उस plan को authoritative command/cwd/session context के रूप में उपयोग करता है।

यह async approval latency के लिए महत्वपूर्ण है:

  * node exec path शुरुआत में एक canonical plan तैयार करता है।
  * approval record उस plan और उसके binding metadata को store करता है।
  * approval के बाद, अंतिम forwarded `system.run` call बाद के caller edits पर भरोसा करने के बजाय stored plan को reuse करता है।
  * यदि approval request बनने के बाद caller `command`, `rawCommand`, `cwd`, `agentId`, या `sessionKey` बदलता है, तो gateway forwarded run को approval mismatch के रूप में reject करता है।


## System events

Exec lifecycle system messages के रूप में surfaced होता है:

  * `Exec running` (केवल यदि command running notice threshold से अधिक समय लेता है)।
  * `Exec finished`।


ये node द्वारा event report करने के बाद agent के session में post किए जाते हैं। Denied exec approvals host command के लिए terminal होते हैं: command run नहीं करता। originating session वाले main-agent async approvals के लिए, OpenClaw denial को उस session में internal followup के रूप में वापस post करता है ताकि agent async command पर waiting बंद कर सके और missing-result repair से बच सके। यदि कोई session नहीं है या session resume नहीं किया जा सकता, तो OpenClaw अभी भी operator या direct chat route को संक्षिप्त denial report कर सकता है। subagent sessions के लिए denials subagent में वापस post नहीं किए जाते। Gateway-host exec approvals command finish होने पर वही lifecycle events emit करते हैं (और threshold से अधिक लंबा चलने पर वैकल्पिक रूप से running event भी)। Approval-gated execs आसान correlation के लिए इन messages में approval id को `runId` के रूप में reuse करते हैं।

## Denied approval behavior

जब async exec approval deny होता है, OpenClaw host command को terminal और fail-closed मानता है। main-agent sessions के लिए, denial को एक internal session followup के रूप में deliver किया जाता है जो agent को बताता है कि async command run नहीं हुआ। यह stale command output expose किए बिना transcript continuity बनाए रखता है। यदि session delivery unavailable है, तो OpenClaw सुरक्षित route मौजूद होने पर संक्षिप्त operator या direct-chat denial पर fallback करता है।

## प्रभाव

  * **`full`** शक्तिशाली है; संभव हो तो allowlists को प्राथमिकता दें।
  * **`ask`** आपको loop में रखता है जबकि fast approvals की अनुमति देता है।
  * प्रति-एजेंट allowlists एक एजेंट के approvals को दूसरों में leak होने से रोकती हैं।
  * Approvals केवल **authorized senders** से आए host exec requests पर लागू होते हैं। Unauthorized senders `/exec` issue नहीं कर सकते।
  * `/exec security=full` authorized operators के लिए session-level convenience है और design के अनुसार approvals छोड़ता है। host exec को hard-block करने के लिए, approvals security को `deny` पर set करें या tool policy के माध्यम से `exec` tool को deny करें।


## संबंधित

[**Exec अनुमोदन - उन्नत** Safe bins, interpreter binding, और chat पर approval forwarding। ](</hi/tools/exec-approvals-advanced>) [**Exec tool** Shell command execution tool। ](</hi/tools/exec>) [**Elevated mode** आपातकालीन path जो approvals भी छोड़ता है। ](</hi/tools/elevated>) [**Sandboxing** Sandbox modes और workspace access। ](</hi/gateway/sandboxing>) [**Security** Security model और hardening। ](</hi/gateway/security>) [**Sandbox बनाम tool policy बनाम elevated** हर control का उपयोग कब करना है। ](</hi/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Skills** Skill-backed auto-allow behavior। ](</hi/tools/skills>)

Was this useful?YesNo

Open issue