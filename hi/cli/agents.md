---
title: एजेंट्स
source_url: https://docs.openclaw.ai/hi/cli/agents
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw agents`

अलग-थलग agents प्रबंधित करें (workspaces + auth + routing).

संबंधित:

  * [Multi-agent routing](</hi/concepts/multi-agent>)
  * [Agent workspace](</hi/concepts/agent-workspace>)
  * [Skills config](</hi/tools/skills-config>): skill दृश्यता कॉन्फ़िगरेशन।


## उदाहरण

bashCopy code
[code]
    openclaw agents listopenclaw agents list --bindingsopenclaw agents add work --workspace ~/.openclaw/workspace-workopenclaw agents add work --workspace ~/.openclaw/workspace-work --bind telegram:*openclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactiveopenclaw agents bindingsopenclaw agents bind --agent work --bind telegram:opsopenclaw agents unbind --agent work --bind telegram:opsopenclaw agents set-identity --workspace ~/.openclaw/workspace --from-identityopenclaw agents set-identity --agent main --avatar avatars/openclaw.pngopenclaw agents delete work
[/code]

## Routing bindings

इनबाउंड channel traffic को किसी खास agent से पिन करने के लिए routing bindings का उपयोग करें।

यदि आप प्रति agent अलग-अलग दिखने वाली skills भी चाहते हैं, तो `openclaw.json` में `agents.defaults.skills` और `agents.list[].skills` कॉन्फ़िगर करें। [Skills config](</hi/tools/skills-config>) और [Configuration reference](</hi/gateway/config-agents#agents-defaults-skills>) देखें।

bindings सूचीबद्ध करें:

bashCopy code
[code]
    openclaw agents bindingsopenclaw agents bindings --agent workopenclaw agents bindings --json
[/code]

bindings जोड़ें:

bashCopy code
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
[/code]

agent बनाते समय भी आप bindings जोड़ सकते हैं:

bashCopy code
[code]
    openclaw agents add work --workspace ~/.openclaw/workspace-work --bind telegram:* --bind discord:*
[/code]

यदि आप `accountId` (`--bind <channel>`) छोड़ देते हैं, तो OpenClaw इसे plugin setup hooks, forced account binding, या channel के कॉन्फ़िगर किए गए account count से हल करता है।

यदि आप `bind` या `unbind` के लिए `--agent` छोड़ देते हैं, तो OpenClaw मौजूदा default agent को target करता है।

### `--bind` format

Format | अर्थ  
---|---  
`--bind <channel>:*` | channel पर सभी accounts से मिलान करें।  
`--bind <channel>:<account>` | एक account से मिलान करें।  
`--bind <channel>` | केवल default account से मिलान करें, जब तक CLI सुरक्षित रूप से plugin-specific account scope हल न कर सके।  
  
### Binding scope behavior

  * `accountId` के बिना stored binding केवल channel default account से मिलान करती है।
  * `accountId: "*"` channel-wide fallback (सभी accounts) है और explicit account binding से कम specific है।
  * यदि उसी agent के पास पहले से `accountId` के बिना matching channel binding है, और आप बाद में explicit या resolved `accountId` के साथ bind करते हैं, तो OpenClaw duplicate जोड़ने के बजाय उसी existing binding को inplace upgrade करता है।


उदाहरण:

bashCopy code
[code]
    # match all accounts on the channelopenclaw agents bind --agent work --bind telegram:* # match a specific accountopenclaw agents bind --agent work --bind telegram:ops # initial channel-only bindingopenclaw agents bind --agent work --bind telegram # later upgrade to account-scoped bindingopenclaw agents bind --agent work --bind telegram:alerts
[/code]

upgrade के बाद, उस binding के लिए routing `telegram:alerts` तक scoped होती है। यदि आप default-account routing भी चाहते हैं, तो उसे स्पष्ट रूप से जोड़ें (उदाहरण के लिए `--bind telegram:default`)।

bindings हटाएँ:

bashCopy code
[code]
    openclaw agents unbind --agent work --bind telegram:opsopenclaw agents unbind --agent work --all
[/code]

`unbind` या तो `--all` स्वीकार करता है या एक या अधिक `--bind` values, दोनों नहीं।

## Command surface

### `agents`

बिना subcommand के `openclaw agents` चलाना `openclaw agents list` के बराबर है।

### `agents list`

Options:

  * `--json`
  * `--bindings`: केवल per-agent counts/summaries नहीं, बल्कि पूरी routing rules शामिल करें


### `agents add [name]`

Options:

  * `--workspace <dir>`
  * `--model <id>`
  * `--agent-dir <dir>`
  * `--bind <channel[:accountId]>` (दोहराने योग्य)
  * `--non-interactive`
  * `--json`


नोट्स:

  * कोई भी explicit add flags पास करने से command non-interactive path में चला जाता है।
  * Non-interactive mode के लिए agent name और `--workspace` दोनों आवश्यक हैं।
  * `main` reserved है और नए agent id के रूप में उपयोग नहीं किया जा सकता।
  * interactive mode में, auth seeding केवल portable static profiles (`api_key` और default रूप से static `token`) कॉपी करती है। OAuth refresh-token profiles real `main` agent store से read-through inheritance के जरिए ही उपलब्ध रहती हैं। यदि configured default agent `main` नहीं है, तो नए agent पर OAuth profiles के लिए अलग से sign in करें।


### `agents bindings`

Options:

  * `--agent <id>`
  * `--json`


### `agents bind`

Options:

  * `--agent <id>` (मौजूदा default agent पर default होता है)
  * `--bind <channel[:accountId]>` (दोहराने योग्य)
  * `--json`


### `agents unbind`

Options:

  * `--agent <id>` (मौजूदा default agent पर default होता है)
  * `--bind <channel[:accountId]>` (दोहराने योग्य)
  * `--all`
  * `--json`


### `agents delete <id>`

Options:

  * `--force`
  * `--json`


नोट्स:

  * `main` delete नहीं किया जा सकता।
  * `--force` के बिना, interactive confirmation आवश्यक है।
  * Workspace, agent state, और session transcript directories को Trash में move किया जाता है, hard-delete नहीं किया जाता।
  * जब Gateway reachable होता है, deletion Gateway के जरिए भेजा जाता है ताकि config और session-store cleanup runtime traffic वाले writer को ही साझा करें। यदि Gateway तक नहीं पहुँचा जा सकता, तो CLI offline local path पर fallback करता है।
  * यदि किसी अन्य agent का workspace वही path है, इस workspace के अंदर है, या इस workspace को contain करता है, तो workspace retain किया जाता है और `--json` `workspaceRetained`, `workspaceRetainedReason`, और `workspaceSharedWith` report करता है।


## Identity files

हर agent workspace में workspace root पर एक `IDENTITY.md` शामिल हो सकता है:

  * Example path: `~/.openclaw/workspace/IDENTITY.md`
  * `set-identity --from-identity` workspace root (या explicit `--identity-file`) से पढ़ता है


Avatar paths workspace root के relative resolve होते हैं।

## Set identity

`set-identity` fields को `agents.list[].identity` में लिखता है:

  * `name`
  * `theme`
  * `emoji`
  * `avatar` (workspace-relative path, http(s) URL, या data URI)


Options:

  * `--agent <id>`
  * `--workspace <dir>`
  * `--identity-file <path>`
  * `--from-identity`
  * `--name <name>`
  * `--theme <theme>`
  * `--emoji <emoji>`
  * `--avatar <value>`
  * `--json`


नोट्स:

  * target agent चुनने के लिए `--agent` या `--workspace` का उपयोग किया जा सकता है।
  * यदि आप `--workspace` पर निर्भर करते हैं और कई agents वह workspace साझा करते हैं, तो command fail होती है और आपसे `--agent` पास करने को कहती है।
  * Local workspace-relative avatar image files 2 MB तक सीमित हैं। HTTP(S) URLs और `data:` URIs को local file-size limit से check नहीं किया जाता।
  * जब कोई explicit identity fields प्रदान नहीं किए जाते, तो command `IDENTITY.md` से identity data पढ़ती है।


`IDENTITY.md` से load करें:

bashCopy code
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
[/code]

fields को explicit रूप से override करें:

bashCopy code
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
[/code]

Config sample:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "main",        identity: {          name: "OpenClaw",          theme: "space lobster",          emoji: "🦞",          avatar: "avatars/openclaw.png",        },      },    ],  },}
[/code]

## संबंधित

  * [CLI reference](</hi/cli>)
  * [Multi-agent routing](</hi/concepts/multi-agent>)
  * [Agent workspace](</hi/concepts/agent-workspace>)


Was this useful?YesNo

Open issue