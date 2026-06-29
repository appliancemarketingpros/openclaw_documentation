---
title: अपडेट किया जा रहा है
source_url: https://docs.openclaw.ai/hi/install/updating
scraped_at: 2026-06-29
---

InstallMaintenance

OpenClaw को अप टू डेट रखें।

## अनुशंसित: `openclaw update`

अपडेट करने का सबसे तेज़ तरीका। यह आपके इंस्टॉल प्रकार (npm या git) का पता लगाता है, नवीनतम संस्करण लाता है, `openclaw doctor` चलाता है, और gateway को फिर से शुरू करता है।

bashCopy code
[code]
    openclaw update
[/code]

चैनल बदलने या किसी विशिष्ट संस्करण को लक्षित करने के लिए:

bashCopy code
[code]
    openclaw update --channel betaopenclaw update --channel devopenclaw update --dry-run   # लागू किए बिना पूर्वावलोकन करें
[/code]

`openclaw update` `--verbose` स्वीकार नहीं करता। अपडेट निदान के लिए, नियोजित कार्रवाइयों का पूर्वावलोकन करने हेतु `--dry-run`, संरचित परिणामों के लिए `--json`, या चैनल और उपलब्धता स्थिति की जांच करने हेतु `openclaw update status --json` का उपयोग करें। इंस्टॉलर का अपना `--verbose` फ़्लैग है, लेकिन वह फ़्लैग `openclaw update` का हिस्सा नहीं है।

`--channel beta` beta को प्राथमिकता देता है, लेकिन जब beta टैग अनुपस्थित हो या नवीनतम stable रिलीज़ से पुराना हो, तो runtime stable/latest पर वापस आ जाता है। यदि आप एक बार के पैकेज अपडेट के लिए raw npm beta dist-tag चाहते हैं, तो `--tag beta` का उपयोग करें।

स्थायी रूप से बदलते GitHub `main` checkout के लिए `--channel dev` का उपयोग करें। पैकेज अपडेट के लिए, `--tag main` एक रन के लिए `github:openclaw/openclaw#main` पर मैप होता है, और GitHub/git source specs को staged npm install से पहले अस्थायी tarball में पैक किया जाता है।

प्रबंधित plugins के लिए, beta-channel fallback एक चेतावनी है: core अपडेट फिर भी सफल हो सकता है जबकि कोई plugin अपनी दर्ज की गई default/latest रिलीज़ का उपयोग करता है क्योंकि कोई plugin beta उपलब्ध नहीं है।

चैनल semantics के लिए [Development channels](</hi/install/development-channels>) देखें।

## npm और git इंस्टॉल के बीच स्विच करें

जब आप इंस्टॉल प्रकार बदलना चाहते हैं, तो channels का उपयोग करें। updater आपके state, config, credentials, और workspace को `~/.openclaw` में रखता है; यह केवल यह बदलता है कि CLI और gateway कौन सा OpenClaw code install उपयोग करते हैं।

bashCopy code
[code]
    # npm package install -> editable git checkoutopenclaw update --channel dev # git checkout -> npm package installopenclaw update --channel stable
[/code]

सटीक install-mode switch का पूर्वावलोकन करने के लिए पहले `--dry-run` के साथ चलाएं:

bashCopy code
[code]
    openclaw update --channel dev --dry-runopenclaw update --channel stable --dry-run
[/code]

`dev` channel git checkout सुनिश्चित करता है, उसे build करता है, और उस checkout से global CLI इंस्टॉल करता है। `stable` और `beta` channels package installs का उपयोग करते हैं। यदि gateway पहले से इंस्टॉल है, तो `openclaw update` service metadata को refresh करता है और उसे restart करता है, जब तक कि आप `--no-restart` पास न करें।

managed Gateway service के साथ package installs के लिए, `openclaw update` उस service द्वारा उपयोग किए गए package root को लक्षित करता है। यदि shell `openclaw` command किसी अलग install से आती है, तो updater दोनों roots और managed service Node path प्रिंट करता है। package update उस package manager का उपयोग करता है जो service root का owner है और package बदलने से पहले managed service Node को target release engine के विरुद्ध जांचता है।

## विकल्प: installer फिर से चलाएं

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

onboarding छोड़ने के लिए `--no-onboard` जोड़ें। installer के माध्यम से किसी विशिष्ट install type को force करने के लिए, `--install-method git --no-onboard` या `--install-method npm --no-onboard` पास करें।

यदि `openclaw update` npm package install चरण के बाद विफल हो जाता है, तो installer फिर से चलाएं। installer पुराने updater को call नहीं करता; यह global package install सीधे चलाता है और आंशिक रूप से updated npm install को recover कर सकता है।

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm
[/code]

recovery को किसी विशिष्ट version या dist-tag पर pin करने के लिए, `--version` जोड़ें:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm --version <version-or-dist-tag>
[/code]

## विकल्प: manual npm, pnpm, या bun

bashCopy code
[code]
    npm i -g openclaw@latest
[/code]

supervised installs के लिए `openclaw update` को प्राथमिकता दें क्योंकि यह running Gateway service के साथ package swap को coordinate कर सकता है। यदि आप supervised install पर manually update करते हैं, तो package manager शुरू होने से पहले managed Gateway को stop करें। Package managers files को in place replace करते हैं, और running Gateway अन्यथा package tree के अस्थायी रूप से half-swapped होने पर core या plugin files load करने का प्रयास कर सकता है। package manager समाप्त होने के बाद Gateway को restart करें ताकि service नया install उठा ले।

root-owned Linux system-global install के लिए, यदि `openclaw update` `EACCES` के साथ विफल होता है और आप system npm से recover करते हैं, तो manual package replacement के दौरान Gateway को stopped रखें। उसी `openclaw` profile flags या environment का उपयोग करें जो आप आमतौर पर उस Gateway के लिए उपयोग करते हैं। अपने host पर root-owned global prefix का owner system npm `/usr/bin/npm` की जगह उपयोग करें:

bashCopy code
[code]
    openclaw gateway stopsudo /usr/bin/npm i -g openclaw@latestopenclaw gateway install --forceopenclaw gateway restart
[/code]

फिर service verify करें:

bashCopy code
[code]
    openclaw --versioncurl -fsS http://127.0.0.1:18789/readyzopenclaw plugins list --jsonopenclaw gateway status --deep --jsonopenclaw doctor --lint --json
[/code]

जब `openclaw update` global npm install manage करता है, तो यह पहले target को temporary npm prefix में install करता है, packaged `dist` inventory verify करता है, फिर clean package tree को real global prefix में swap करता है। इससे npm पुराने package की stale files पर नया package overlay करने से बचता है। यदि install command विफल होती है, तो OpenClaw `--omit=optional` के साथ एक बार retry करता है। यह retry उन hosts में मदद करता है जहां native optional dependencies compile नहीं हो पातीं, जबकि fallback भी विफल होने पर original failure visible रखता है।

OpenClaw-managed npm update और plugin-update commands child npm process के लिए npm `min-release-age` quarantine भी clear करते हैं। npm उस policy को derived `before` cutoff के रूप में report कर सकता है; दोनों सामान्य supply-chain quarantine policies के लिए उपयोगी हैं, लेकिन explicit OpenClaw update का अर्थ है "चयनित OpenClaw release अभी install करें।"

bashCopy code
[code]
    pnpm add -g openclaw@latest
[/code]

bashCopy code
[code]
    bun add -g openclaw@latest
[/code]

### Advanced npm install topics

Read-only package tree

OpenClaw packaged global installs को runtime पर read-only मानता है, भले ही global package directory current user द्वारा writable हो। Plugin package installs user config directory के अंतर्गत OpenClaw-owned npm/git roots में रहते हैं, और Gateway startup OpenClaw package tree को mutate नहीं करता।

कुछ Linux npm setups global packages को root-owned directories जैसे `/usr/lib/node_modules/openclaw` के अंतर्गत install करते हैं। OpenClaw उस layout का समर्थन करता है क्योंकि plugin install/update commands उस global package directory के बाहर write करते हैं।

Hardened systemd units

OpenClaw को उसके config/state roots तक write access दें ताकि explicit plugin installs, plugin updates, और doctor cleanup अपने changes persist कर सकें:

iniCopy code
[code]
    ReadWritePaths=/var/lib/openclaw /home/openclaw/.openclaw /tmp
[/code]

Disk-space preflight

package updates और explicit plugin installs से पहले, OpenClaw target volume के लिए best-effort disk-space check आज़माता है। Low space checked path के साथ warning देता है, लेकिन update को block नहीं करता क्योंकि filesystem quotas, snapshots, और network volumes check के बाद बदल सकते हैं। actual package-manager install और post-install verification authoritative रहते हैं।

## Auto-updater

auto-updater default रूप से off है। इसे `~/.openclaw/openclaw.json` में enable करें:

json5Copy code
[code]
    {  update: {    channel: "stable",    auto: {      enabled: true,      stableDelayHours: 6,      stableJitterHours: 12,      betaCheckIntervalHours: 1,    },  },}
[/code]

Channel | Behavior  
---|---  
`stable` | `stableDelayHours` प्रतीक्षा करता है, फिर `stableJitterHours` में deterministic jitter के साथ apply करता है (spread rollout)।  
`beta` | हर `betaCheckIntervalHours` पर check करता है (default: hourly) और तुरंत apply करता है।  
`dev` | कोई automatic apply नहीं। `openclaw update` manually उपयोग करें।  
  
gateway startup पर update hint भी log करता है (`update.checkOnStart: false` से disable करें)। downgrade या incident recovery के लिए, Gateway environment में `OPENCLAW_NO_AUTO_UPDATE=1` set करें ताकि `update.auto.enabled` configured होने पर भी automatic applies block हों। Startup update hints तब भी चल सकते हैं जब तक `update.checkOnStart` भी disabled न हो।

live Gateway control-plane handler के माध्यम से अनुरोधित Package-manager updates running Gateway process के अंदर package tree को replace नहीं करते। managed service installs पर, Gateway detached handoff शुरू करता है, exit करता है, और normal `openclaw update --yes --json` CLI path को service stop करने, package replace करने, service metadata refresh करने, restart करने, Gateway version और reachability verify करने, और संभव होने पर installed-but-unloaded macOS LaunchAgent recover करने देता है। यदि Gateway वह handoff safely नहीं कर सकता, तो `update.run` package manager in-process चलाने के बजाय safe shell command report करता है।

## अपडेट करने के बाद

### doctor चलाएं

bashCopy code
[code]
    openclaw doctor
[/code]

config migrate करता है, DM policies audit करता है, और gateway health check करता है। विवरण: [Doctor](</hi/gateway/doctor>)

### gateway restart करें

bashCopy code
[code]
    openclaw gateway restart
[/code]

### Verify करें

bashCopy code
[code]
    openclaw health
[/code]

## Rollback

### version pin करें (npm)

bashCopy code
[code]
    npm i -g openclaw@<version>openclaw doctoropenclaw gateway restart
[/code]

### commit pin करें (source)

bashCopy code
[code]
    git fetch origingit checkout "$(git rev-list -n 1 --before=\"2026-01-01\" origin/main)"pnpm install && pnpm buildopenclaw gateway restart
[/code]

latest पर लौटने के लिए: `git checkout main && git pull`।

## यदि आप अटके हुए हैं

  * `openclaw doctor` फिर से चलाएं और output ध्यान से पढ़ें।
  * source checkouts पर `openclaw update --channel dev` के लिए, updater आवश्यकता होने पर `pnpm` को auto-bootstrap करता है। यदि आपको pnpm/corepack bootstrap error दिखे, तो `pnpm` manually install करें (या `corepack` फिर से enable करें) और update rerun करें।
  * जांचें: [Troubleshooting](</hi/gateway/troubleshooting>)
  * Discord में पूछें: <https://discord.gg/clawd>


## संबंधित

  * [Install overview](</hi/install>): सभी installation methods।
  * [Doctor](</hi/gateway/doctor>): updates के बाद health checks।
  * [Migrating](</hi/install/migrating>): major version migration guides।


Was this useful?YesNo

Open issue