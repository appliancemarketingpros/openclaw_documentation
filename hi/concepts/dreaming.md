---
title: Dreaming
source_url: https://docs.openclaw.ai/hi/concepts/dreaming
scraped_at: 2026-06-29
---

AgentsSessions and memory

Dreaming, `memory-core` में पृष्ठभूमि memory consolidation प्रणाली है। यह OpenClaw को मजबूत अल्पकालिक संकेतों को टिकाऊ memory में ले जाने में मदद करता है, जबकि प्रक्रिया को समझाने योग्य और समीक्षा योग्य बनाए रखता है।

## Dreaming क्या लिखता है

Dreaming दो प्रकार के आउटपुट रखता है:

  * `memory/.dreams/` में **मशीन स्थिति** (recall store, phase signals, ingestion checkpoints, locks)।
  * `DREAMS.md` (या मौजूदा `dreams.md`) में **मानव-पठनीय आउटपुट** और `memory/dreaming/<phase>/YYYY-MM-DD.md` के अंतर्गत वैकल्पिक phase report फ़ाइलें।


दीर्घकालिक promotion अब भी केवल `MEMORY.md` में लिखता है।

## Phase model

Dreaming तीन सहयोगी phases का उपयोग करता है:

Phase | उद्देश्य | टिकाऊ write  
---|---|---  
Light | हाल की अल्पकालिक सामग्री को क्रमबद्ध और stage करना | नहीं  
Deep | टिकाऊ candidates को score और promote करना | हाँ (`MEMORY.md`)  
REM | themes और दोहराए जाने वाले ideas पर विचार करना | नहीं  
  
ये phases आंतरिक implementation details हैं, अलग user-configured "modes" नहीं।

Light phase

Light phase हाल के दैनिक memory signals और recall traces को ingest करता है, उन्हें dedupe करता है, और candidate lines को stage करता है।

  * उपलब्ध होने पर short-term recall state, हाल की दैनिक memory files, और redacted session transcripts से पढ़ता है।
  * जब storage में inline output शामिल हो, तो managed `## Light Sleep` block लिखता है।
  * बाद की deep ranking के लिए reinforcement signals रिकॉर्ड करता है।
  * कभी भी `MEMORY.md` में नहीं लिखता।

Deep phase

Deep phase तय करता है कि क्या long-term memory बनेगा।

  * weighted scoring और threshold gates का उपयोग करके candidates को rank करता है।
  * pass करने के लिए `minScore`, `minRecallCount`, और `minUniqueQueries` की आवश्यकता होती है।
  * लिखने से पहले live daily files से snippets को rehydrate करता है, इसलिए stale/deleted snippets छोड़ दिए जाते हैं।
  * promoted entries को `MEMORY.md` में append करता है।
  * `DREAMS.md` में `## Deep Sleep` summary लिखता है और वैकल्पिक रूप से `memory/dreaming/deep/YYYY-MM-DD.md` लिखता है।

REM phase

REM phase patterns और reflective signals निकालता है।

  * हाल के short-term traces से theme और reflection summaries बनाता है।
  * जब storage में inline output शामिल हो, तो managed `## REM Sleep` block लिखता है।
  * deep ranking द्वारा उपयोग किए जाने वाले REM reinforcement signals रिकॉर्ड करता है।
  * कभी भी `MEMORY.md` में नहीं लिखता।


## Session transcript ingestion

Dreaming redacted session transcripts को dreaming corpus में ingest कर सकता है। जब transcripts उपलब्ध होते हैं, तो उन्हें दैनिक memory signals और recall traces के साथ light phase में भेजा जाता है। Personal और sensitive content ingestion से पहले redact किया जाता है।

## स्वप्न डायरी

Dreaming `DREAMS.md` में एक narrative **स्वप्न डायरी** भी रखता है। प्रत्येक phase में पर्याप्त सामग्री होने के बाद, `memory-core` best-effort background subagent turn चलाता है और एक छोटी diary entry append करता है। जब तक `dreaming.model` configured न हो, यह default runtime model का उपयोग करता है। यदि configured model उपलब्ध नहीं है, तो स्वप्न डायरी session default model के साथ एक बार retry करती है।

Review और recovery work के लिए एक grounded historical backfill lane भी है:

Backfill commands

  * `memory rem-harness --path ... --grounded` historical `YYYY-MM-DD.md` notes से grounded diary output preview करता है।
  * `memory rem-backfill --path ...` reversible grounded diary entries को `DREAMS.md` में लिखता है।
  * `memory rem-backfill --path ... --stage-short-term` grounded durable candidates को उसी short-term evidence store में stage करता है जिसका normal deep phase पहले से उपयोग करता है।
  * `memory rem-backfill --rollback` और `--rollback-short-term` ordinary diary entries या live short-term recall को छुए बिना उन staged backfill artifacts को हटाते हैं।


Control UI वही diary backfill/reset flow expose करता है, ताकि आप grounded candidates promotion के योग्य हैं या नहीं यह तय करने से पहले Dreams scene में results inspect कर सकें। Scene एक अलग grounded lane भी दिखाता है, ताकि आप देख सकें कि कौन-सी staged short-term entries historical replay से आईं, कौन-से promoted items grounded-led थे, और ordinary live short-term state को छुए बिना केवल grounded-only staged entries clear कर सकें।

## Deep ranking signals

Deep ranking छह weighted base signals और phase reinforcement का उपयोग करता है:

Signal | Weight | विवरण  
---|---|---  
Frequency | 0.24 | entry ने कितने short-term signals जमा किए  
Relevance | 0.30 | entry के लिए average retrieval quality  
Query diversity | 0.15 | अलग-अलग query/day contexts जिन्होंने इसे surfaced किया  
Recency | 0.15 | time-decayed freshness score  
Consolidation | 0.10 | multi-day recurrence strength  
Conceptual richness | 0.06 | snippet/path से concept-tag density  
  
Light और REM phase hits `memory/.dreams/phase-signals.json` से छोटा recency-decayed boost जोड़ते हैं।

Shadow-trial results को किसी भी durable write से पहले review signal के रूप में उस base score के ऊपर layer किया जा सकता है। Helpful trial candidate को छोटा bounded boost देता है, neutral trial उसे deferred रखता है, और harmful trial उस scoring pass के लिए उसे rejected चिह्नित करता है। यह signal अभी भी report-only है: यह candidate ordering या review metadata बदल सकता है, लेकिन यह `MEMORY.md` में नहीं लिखता या candidate को अपने आप promote नहीं करता।

## QA shadow trial report coverage

QA Lab में यह explore करने के लिए report-only scenario शामिल है कि future dreaming shadow trial promotion से पहले candidate memory की review कैसे कर सकता है। Scenario एक agent से baseline answer की तुलना उस answer से करने को कहता है जो candidate memory का उपयोग कर सकता है, फिर verdict, reason, और risk flags के साथ local report लिखता है।

यह coverage जानबूझकर QA तक scoped है। यह verify करता है कि report artifact `MEMORY.md` से अलग रहता है और agent यह दावा नहीं करता कि candidate promote हुआ था। यह production shadow-trial behavior नहीं जोड़ता या deep-phase promotion engine नहीं बदलता।

`memory-core` shadow-trial runner उन code paths के लिए वही report-only contract रखता है जिन्हें stable artifact चाहिए। यह candidate, trial prompt, baseline outcome, candidate outcome, verdict, reason, risk flags, और evidence references स्वीकार करता है, फिर `promotion action: report-only` के साथ report लिखता है। Helpful verdicts `promote` recommendation से map होते हैं, neutral verdicts `defer` से map होते हैं, और harmful verdicts `reject` से map होते हैं; इनमें से कोई भी recommendation `MEMORY.md` में नहीं लिखती या deep-phase promotion लागू नहीं करती।

## Scheduling

Enabled होने पर, `memory-core` full dreaming sweep के लिए एक Cron job auto-manage करता है। प्रत्येक sweep phases को क्रम में चलाता है: light → REM → deep।

Sweep में primary runtime workspace और कोई भी configured agent workspaces शामिल होते हैं, path के आधार पर dedupe किए हुए, ताकि subagent workspace fan-out main agent के `DREAMS.md` और memory state को exclude न करे।

Default cadence behavior:

Setting | Default  
---|---  
`dreaming.frequency` | `0 3 * * *`  
`dreaming.model` | default model  
  
## Quick start

### Enable dreaming

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true          }        }      }    }  }}
[/code]

### Custom sweep cadence

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true,            "timezone": "America/Los_Angeles",            "frequency": "0 */6 * * *"          }        }      }    }  }}
[/code]

## Slash command

CodeCopy code
[code]
    /dreaming status/dreaming on/dreaming off/dreaming help
[/code]

## CLI workflow

### Promotion preview / apply

bashCopy code
[code]
    openclaw memory promoteopenclaw memory promote --applyopenclaw memory promote --limit 5openclaw memory status --deep
[/code]

Manual `memory promote` default रूप से deep-phase thresholds का उपयोग करता है, जब तक कि CLI flags से override न किया जाए।

### Explain promotion

समझाएँ कि कोई specific candidate promote क्यों होगा या क्यों नहीं होगा:

bashCopy code
[code]
    openclaw memory promote-explain "router vlan"openclaw memory promote-explain "router vlan" --json
[/code]

### REM harness preview

कुछ भी लिखे बिना REM reflections, candidate truths, और deep promotion output preview करें:

bashCopy code
[code]
    openclaw memory rem-harnessopenclaw memory rem-harness --json
[/code]

## Key defaults

सभी settings `plugins.entries.memory-core.config.dreaming` के अंतर्गत रहते हैं।

dreaming sweep को enable या disable करें।

full dreaming sweep के लिए Cron cadence।

वैकल्पिक स्वप्न डायरी subagent model override। subagent `allowedModels` allowlist set करते समय canonical `provider/model` value का उपयोग करें।

`MEMORY.md` में promote किए गए प्रत्येक short-term recall snippet से रखा गया maximum estimated token count। Ranking provenance visible रहता है।

## Dreams UI

Enabled होने पर, Gateway **Dreams** tab दिखाता है:

  * वर्तमान dreaming enabled state
  * phase-level status और managed-sweep presence
  * short-term, grounded, signal, और promoted-today counts
  * अगला scheduled run timing
  * staged historical replay entries के लिए अलग grounded Scene lane
  * `doctor.memory.dreamDiary` द्वारा backed expandable स्वप्न डायरी reader


## Dreaming कभी नहीं चलता: status blocked दिखाता है

यदि `openclaw memory status` `Dreaming status: blocked` report करता है, तो managed cron मौजूद है लेकिन default agent Heartbeat fire नहीं हो रहा। जाँचें कि default agent के लिए Heartbeat enabled है और उसका target `none` नहीं है, फिर अगले Heartbeat interval के बाद `openclaw memory status --deep` फिर से चलाएँ।

## Related

  * [Memory](</hi/concepts/memory>)
  * [Memory CLI](</hi/cli/memory>)
  * [Memory configuration reference](</hi/reference/memory-config>)
  * [Memory search](</hi/concepts/memory-search>)


Was this useful?YesNo

Open issue