---
title: एजेंट कार्यक्षेत्र
source_url: https://docs.openclaw.ai/hi/concepts/agent-workspace
scraped_at: 2026-06-29
---

AgentsFundamentals

कार्यक्षेत्र एजेंट का घर है। यह फ़ाइल टूल्स और कार्यक्षेत्र संदर्भ के लिए उपयोग की जाने वाली एकमात्र कार्यशील डायरेक्टरी है। इसे निजी रखें और इसे मेमोरी की तरह मानें।

यह `~/.openclaw/` से अलग है, जहाँ config, credentials, और sessions संग्रहीत होते हैं।

## डिफ़ॉल्ट स्थान

  * डिफ़ॉल्ट: `~/.openclaw/workspace`
  * यदि `OPENCLAW_PROFILE` सेट है और `"default"` नहीं है, तो डिफ़ॉल्ट `~/.openclaw/workspace-<profile>` बन जाता है।
  * `~/.openclaw/openclaw.json` में override करें:

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure`, या `openclaw setup` कार्यक्षेत्र बनाएँगे और यदि bootstrap फ़ाइलें अनुपस्थित हैं तो उन्हें seed करेंगे।

यदि आप पहले से ही कार्यक्षेत्र फ़ाइलें स्वयं manage करते हैं, तो आप bootstrap फ़ाइल निर्माण अक्षम कर सकते हैं:

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## अतिरिक्त कार्यक्षेत्र फ़ोल्डर

पुराने installs ने `~/openclaw` बनाया हो सकता है। कई कार्यक्षेत्र डायरेक्टरी रखना भ्रमित करने वाला auth या state drift पैदा कर सकता है, क्योंकि एक समय में केवल एक कार्यक्षेत्र active होता है।

## कार्यक्षेत्र फ़ाइल मानचित्र

ये वे मानक फ़ाइलें हैं जिनकी OpenClaw कार्यक्षेत्र के अंदर अपेक्षा करता है:

AGENTS.md - संचालन निर्देश

एजेंट के लिए संचालन निर्देश और उसे मेमोरी का उपयोग कैसे करना चाहिए। हर session की शुरुआत में loaded होता है। नियमों, प्राथमिकताओं, और "कैसे व्यवहार करें" विवरणों के लिए अच्छी जगह।

SOUL.md - persona और tone

Persona, tone, और boundaries। हर session में loaded होता है। Guide: [SOUL.md personality guide](</hi/concepts/soul>).

USER.md - user कौन है

User कौन है और उन्हें कैसे address करना है। हर session में loaded होता है।

IDENTITY.md - name, vibe, emoji

एजेंट का name, vibe, और emoji। bootstrap ritual के दौरान बनाया/अपडेट किया जाता है।

TOOLS.md - स्थानीय tool conventions

आपके स्थानीय tools और conventions के बारे में notes। यह tool availability नियंत्रित नहीं करता; यह केवल guidance है।

HEARTBEAT.md - Heartbeat checklist

Heartbeat runs के लिए वैकल्पिक छोटी checklist। token burn से बचने के लिए इसे छोटा रखें।

BOOT.md - startup checklist

वैकल्पिक startup checklist जो gateway restart पर automatic चलती है (जब [internal hooks](</hi/automation/hooks>) सक्षम हों)। इसे छोटा रखें; outbound sends के लिए message tool का उपयोग करें।

BOOTSTRAP.md - first-run ritual

एक बार चलने वाला first-run ritual। केवल बिल्कुल नए कार्यक्षेत्र के लिए बनाया जाता है। ritual पूरा होने के बाद इसे delete कर दें।

memory/YYYY-MM-DD.md - दैनिक मेमोरी log

दैनिक मेमोरी log (प्रति दिन एक फ़ाइल)। session start पर today + yesterday पढ़ने की सिफ़ारिश की जाती है।

MEMORY.md - curated long-term memory (वैकल्पिक)

Curated long-term memory: durable facts, preferences, decisions, और short summaries। विस्तृत logs `memory/YYYY-MM-DD.md` में रखें ताकि memory tools उन्हें हर prompt में inject किए बिना on demand retrieve कर सकें। `MEMORY.md` को केवल main, private session में load करें (shared/group contexts में नहीं)। workflow और automatic memory flush के लिए [Memory](</hi/concepts/memory>) देखें।

skills/ - कार्यक्षेत्र Skills (वैकल्पिक)

कार्यक्षेत्र-विशिष्ट Skills। उस कार्यक्षेत्र के लिए सबसे उच्च-precedence skill location। names collide होने पर project agent skills, personal agent skills, managed skills, bundled skills, और `skills.load.extraDirs` को override करता है।

canvas/ - Canvas UI files (वैकल्पिक)

node displays के लिए Canvas UI files (उदाहरण के लिए `canvas/index.html`)।

## कार्यक्षेत्र में क्या नहीं है

ये `~/.openclaw/` के अंतर्गत रहते हैं और कार्यक्षेत्र repo में commit नहीं किए जाने चाहिए:

  * `~/.openclaw/openclaw.json` (config)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (model auth profiles: OAuth + API keys)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (per-agent Codex runtime account, config, skills, plugins, और native thread state)
  * `~/.openclaw/credentials/` (channel/provider state plus legacy OAuth import data)
  * `~/.openclaw/agents/<agentId>/sessions/` (session transcripts + metadata)
  * `~/.openclaw/skills/` (managed skills)


यदि आपको sessions या config migrate करने हैं, तो उन्हें अलग से copy करें और version control से बाहर रखें।

## Git backup (सिफ़ारिश की गई, निजी)

कार्यक्षेत्र को निजी मेमोरी की तरह मानें। इसे **private** git repo में रखें ताकि इसका backup हो और यह recoverable रहे।

इन steps को उस machine पर run करें जहाँ Gateway चलता है (वही जगह है जहाँ कार्यक्षेत्र रहता है)।

* ### Repo initialize करें

यदि git installed है, तो बिल्कुल नए कार्यक्षेत्र automatic initialize होते हैं। यदि यह कार्यक्षेत्र पहले से repo नहीं है, तो run करें:

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### Private remote जोड़ें

### GitHub web UI

  1. GitHub पर एक नया **private** repository बनाएँ।
  2. README से initialize न करें (merge conflicts से बचता है)।
  3. HTTPS remote URL copy करें।
  4. remote add करें और push करें:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### GitLab web UI

  1. GitLab पर एक नया **private** repository बनाएँ।
  2. README से initialize न करें (merge conflicts से बचता है)।
  3. HTTPS remote URL copy करें।
  4. remote add करें और push करें:

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### लगातार updates

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## Secrets commit न करें

Suggested `.gitignore` starter:

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## कार्यक्षेत्र को नई machine पर ले जाना

* ### Repo clone करें

Repo को desired path पर clone करें (डिफ़ॉल्ट `~/.openclaw/workspace`)।

* ### Config update करें

`~/.openclaw/openclaw.json` में `agents.defaults.workspace` को उस path पर set करें।

* ### Missing files seed करें

किसी भी missing files को seed करने के लिए `openclaw setup --workspace <path>` run करें।

* ### Sessions copy करें (वैकल्पिक)

यदि आपको sessions चाहिए, तो old machine से `~/.openclaw/agents/<agentId>/sessions/` अलग से copy करें।

## Advanced notes

  * Multi-agent routing प्रति एजेंट अलग-अलग कार्यक्षेत्रों का उपयोग कर सकती है। routing configuration के लिए [Channel routing](</hi/channels/channel-routing>) देखें।
  * यदि `agents.defaults.sandbox` सक्षम है, तो non-main sessions `agents.defaults.sandbox.workspaceRoot` के अंतर्गत per-session sandbox workspaces का उपयोग कर सकते हैं।


## Related

  * [Heartbeat](</hi/gateway/heartbeat>) \- HEARTBEAT.md कार्यक्षेत्र फ़ाइल
  * [Sandboxing](</hi/gateway/sandboxing>) \- sandboxed environments में कार्यक्षेत्र access
  * [Session](</hi/concepts/session>) \- session storage paths
  * [Standing orders](</hi/automation/standing-orders>) \- कार्यक्षेत्र फ़ाइलों में persistent instructions


Was this useful?YesNo

Open issue