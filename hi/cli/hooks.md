---
title: हुक्स
source_url: https://docs.openclaw.ai/hi/cli/hooks
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw hooks`

एजेंट hooks प्रबंधित करें (`/new`, `/reset`, और gateway startup जैसे कमांड के लिए event-driven automation).

बिना subcommand के `openclaw hooks` चलाना `openclaw hooks list` के बराबर है।

संबंधित:

  * Hooks: [Hooks](</hi/automation/hooks>)
  * Plugin hooks: [Plugin hooks](</hi/plugins/hooks>)


## सभी hooks सूचीबद्ध करें

bashCopy code
[code]
    openclaw hooks list
[/code]

workspace, managed, extra, और bundled directories से खोजे गए सभी hooks सूचीबद्ध करें। Gateway startup आंतरिक hook handlers को तब तक लोड नहीं करता जब तक कम से कम एक आंतरिक hook कॉन्फ़िगर न हो।

**विकल्प:**

  * `--eligible`: केवल eligible hooks दिखाएं (requirements पूरी)
  * `--json`: JSON के रूप में output दें
  * `-v, --verbose`: missing requirements सहित विस्तृत जानकारी दिखाएं


**उदाहरण output:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**उदाहरण (verbose):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

ineligible hooks के लिए missing requirements दिखाता है।

**उदाहरण (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

programmatic उपयोग के लिए structured JSON लौटाता है।

## Hook जानकारी प्राप्त करें

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

किसी विशिष्ट hook के बारे में विस्तृत जानकारी दिखाएं।

**Arguments:**

  * `<name>`: Hook name या hook key (उदा., `session-memory`)


**विकल्प:**

  * `--json`: JSON के रूप में output दें


**उदाहरण:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Output:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Hooks eligibility जांचें

bashCopy code
[code]
    openclaw hooks check
[/code]

hook eligibility status का सारांश दिखाएं (कितने ready हैं बनाम not ready).

**विकल्प:**

  * `--json`: JSON के रूप में output दें


**उदाहरण output:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Hook सक्षम करें

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

किसी विशिष्ट hook को अपने config में जोड़कर सक्षम करें (default रूप से `~/.openclaw/openclaw.json`).

**नोट:** Workspace hooks default रूप से disabled रहते हैं जब तक यहां या config में enabled न किए जाएं। plugins द्वारा managed hooks `openclaw hooks list` में `plugin:<id>` दिखाते हैं और यहां enabled/disabled नहीं किए जा सकते। इसके बजाय plugin को enable/disable करें।

**Arguments:**

  * `<name>`: Hook name (उदा., `session-memory`)


**उदाहरण:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Output:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**यह क्या करता है:**

  * जांचता है कि hook मौजूद है और eligible है
  * आपके config में `hooks.internal.entries.<name>.enabled = true` अपडेट करता है
  * config को disk पर सहेजता है


यदि hook `<workspace>/hooks/` से आया है, तो Gateway द्वारा उसे लोड करने से पहले यह opt-in step आवश्यक है।

**सक्षम करने के बाद:**

  * gateway restart करें ताकि hooks reload हों (macOS पर menu bar app restart, या dev में अपना gateway process restart करें).


## Hook अक्षम करें

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

अपने config को अपडेट करके किसी विशिष्ट hook को अक्षम करें।

**Arguments:**

  * `<name>`: Hook name (उदा., `command-logger`)


**उदाहरण:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Output:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**अक्षम करने के बाद:**

  * gateway restart करें ताकि hooks reload हों


## नोट्स

  * `openclaw hooks list --json`, `info --json`, और `check --json` structured JSON को सीधे stdout पर लिखते हैं।
  * Plugin-managed hooks यहां enabled या disabled नहीं किए जा सकते; इसके बजाय owning plugin को enable या disable करें।


## Hook packs install करें

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

unified plugins installer के माध्यम से hook packs install करें।

`openclaw hooks install` अब भी compatibility alias के रूप में काम करता है, लेकिन यह deprecation warning print करता है और `openclaw plugins install` को forward करता है।

Npm specs **केवल registry** हैं (package name + optional **exact version** या **dist-tag**). Git/URL/file specs और semver ranges अस्वीकार किए जाते हैं। Dependency installs सुरक्षा के लिए `--ignore-scripts` के साथ project-local चलते हैं, तब भी जब आपके shell में global npm install settings हों।

Bare specs और `@latest` stable track पर रहते हैं। यदि npm इनमें से किसी को prerelease पर resolve करता है, तो OpenClaw रुकता है और आपसे `@beta`/`@rc` जैसे prerelease tag या exact prerelease version के साथ स्पष्ट opt in करने को कहता है।

**यह क्या करता है:**

  * hook pack को `~/.openclaw/hooks/<id>` में copy करता है
  * installed hooks को `hooks.internal.entries.*` में enable करता है
  * install को `hooks.internal.installs` के अंतर्गत record करता है


**विकल्प:**

  * `-l, --link`: copy करने के बजाय local directory link करें (इसे `hooks.internal.load.extraDirs` में जोड़ता है)
  * `--pin`: npm installs को `hooks.internal.installs` में exact resolved `name@version` के रूप में record करें


**Supported archives:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**उदाहरण:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

Linked hook packs को operator-configured directory से managed hooks माना जाता है, workspace hooks नहीं।

## Hook packs update करें

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

unified plugins updater के माध्यम से tracked npm-based hook packs update करें।

`openclaw hooks update` अब भी compatibility alias के रूप में काम करता है, लेकिन यह deprecation warning print करता है और `openclaw plugins update` को forward करता है।

**विकल्प:**

  * `--all`: सभी tracked hook packs update करें
  * `--dry-run`: लिखे बिना दिखाएं कि क्या बदलेगा


जब stored integrity hash मौजूद हो और fetched artifact hash बदल जाए, OpenClaw warning print करता है और आगे बढ़ने से पहले confirmation मांगता है। CI/non-interactive runs में prompts bypass करने के लिए global `--yes` का उपयोग करें।

## Bundled hooks

### session-memory

जब आप `/new` या `/reset` issue करते हैं तो session context को memory में सहेजता है।

**सक्षम करें:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Output:** default रूप से `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md`. model-generated filename slugs के लिए `hooks.internal.entries.session-memory.llmSlug: true` सेट करें।

**देखें:** [session-memory documentation](</hi/automation/hooks#session-memory>)

### bootstrap-extra-files

`agent:bootstrap` के दौरान अतिरिक्त bootstrap files (उदाहरण के लिए monorepo-local `AGENTS.md` / `TOOLS.md`) inject करता है।

**सक्षम करें:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**देखें:** [bootstrap-extra-files documentation](</hi/automation/hooks#bootstrap-extra-files>)

### command-logger

सभी command events को centralized audit file में log करता है।

**सक्षम करें:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Output:** `~/.openclaw/logs/commands.log`

**Logs देखें:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**देखें:** [command-logger documentation](</hi/automation/hooks#command-logger>)

### boot-md

gateway शुरू होने पर `BOOT.md` चलाता है (channels शुरू होने के बाद).

**Events** : `gateway:startup`

**सक्षम करें** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**देखें:** [boot-md documentation](</hi/automation/hooks#boot-md>)

## संबंधित

  * [CLI reference](</hi/cli>)
  * [Automation hooks](</hi/automation/hooks>)


Was this useful?YesNo

Open issue