---
title: अनइंस्टॉल کریں
source_url: https://docs.openclaw.ai/hi/install/uninstall
scraped_at: 2026-06-29
---

InstallMaintenance

दो रास्ते:

  * **आसान रास्ता** यदि `openclaw` अभी भी इंस्टॉल है।
  * **मैन्युअल सेवा हटाना** यदि CLI हट गई है लेकिन सेवा अभी भी चल रही है।


## आसान रास्ता (CLI अभी भी इंस्टॉल है)

अनुशंसित: बिल्ट-इन अनइंस्टॉलर का उपयोग करें:

bashCopy code
[code]
    openclaw uninstall
[/code]

CLI का उपयोग करते समय, स्थिति हटाने से कॉन्फ़िगर की गई कार्यस्थान निर्देशिकाएँ सुरक्षित रहती हैं, जब तक कि आप `--workspace` भी न चुनें।

पूर्वावलोकन करें कि क्या हटाया जाएगा (सुरक्षित):

bashCopy code
[code]
    openclaw uninstall --dry-run --all
[/code]

गैर-इंटरैक्टिव (स्वचालन / npx)। सावधानी से उपयोग करें और केवल स्कोप की पुष्टि करने के बाद:

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

मैन्युअल चरण (वही परिणाम):

  1. Gateway सेवा रोकें:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Gateway सेवा अनइंस्टॉल करें (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. स्थिति + कॉन्फ़िगरेशन हटाएँ:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

यदि आपने `OPENCLAW_CONFIG_PATH` को स्थिति निर्देशिका के बाहर किसी कस्टम स्थान पर सेट किया है, तो वह फ़ाइल भी हटाएँ। यदि आप स्थिति निर्देशिका के अंदर कोई कार्यस्थान रखना चाहते हैं, जैसे `~/.openclaw/workspace`, तो `rm -rf` चलाने से पहले उसे अलग स्थान पर ले जाएँ या स्थिति सामग्री को चुनिंदा रूप से हटाएँ।

  4. अपना कार्यस्थान हटाएँ (वैकल्पिक, एजेंट फ़ाइलें हटाता है):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. CLI इंस्टॉल हटाएँ (जिसका आपने उपयोग किया था उसे चुनें):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. यदि आपने macOS ऐप इंस्टॉल किया था:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

नोट्स:

  * यदि आपने प्रोफ़ाइल (`--profile` / `OPENCLAW_PROFILE`) का उपयोग किया है, तो प्रत्येक स्थिति निर्देशिका के लिए चरण 3 दोहराएँ (डिफ़ॉल्ट `~/.openclaw-<profile>` हैं)।
  * दूरस्थ मोड में, स्थिति निर्देशिका **Gateway होस्ट** पर होती है, इसलिए चरण 1-4 वहाँ भी चलाएँ।


## मैन्युअल सेवा हटाना (CLI इंस्टॉल नहीं है)

इसका उपयोग करें यदि Gateway सेवा चलती रहती है लेकिन `openclaw` अनुपलब्ध है।

### macOS (launchd)

डिफ़ॉल्ट लेबल `ai.openclaw.gateway` है (या `ai.openclaw.<profile>`; पुराना `com.openclaw.*` अभी भी मौजूद हो सकता है):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

यदि आपने प्रोफ़ाइल का उपयोग किया है, तो लेबल और plist नाम को `ai.openclaw.<profile>` से बदलें। यदि कोई पुरानी `com.openclaw.*` plist मौजूद हो, तो उसे हटा दें।

### Linux (systemd उपयोगकर्ता यूनिट)

डिफ़ॉल्ट यूनिट नाम `openclaw-gateway.service` है (या `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (Scheduled Task)

डिफ़ॉल्ट कार्य नाम `OpenClaw Gateway` है (या `OpenClaw Gateway (<profile>)`)। कार्य स्क्रिप्ट आपकी स्थिति निर्देशिका के अंतर्गत `gateway.cmd` के रूप में होती है; मौजूदा इंस्टॉल एक विंडोलेस `gateway.vbs` लॉन्चर भी बना सकते हैं जिसे Task Scheduler सीधे `gateway.cmd` खोलने के बजाय चलाता है।

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd" -ErrorAction SilentlyContinueRemove-Item -Force "$env:USERPROFILE\.openclaw\gateway.vbs" -ErrorAction SilentlyContinue
[/code]

यदि आपने प्रोफ़ाइल का उपयोग किया है, तो मेल खाते कार्य नाम और `~\.openclaw-<profile>` के अंतर्गत `gateway.cmd` / `gateway.vbs` फ़ाइलें हटाएँ।

## सामान्य इंस्टॉल बनाम स्रोत चेकआउट

### सामान्य इंस्टॉल (install.sh / npm / pnpm / bun)

यदि आपने `https://openclaw.ai/install.sh` या `install.ps1` का उपयोग किया था, तो CLI `npm install -g openclaw@latest` से इंस्टॉल की गई थी। इसे `npm rm -g openclaw` से हटाएँ (या यदि आपने उस तरह इंस्टॉल किया था तो `pnpm remove -g` / `bun remove -g`)।

### स्रोत चेकआउट (git clone)

यदि आप किसी रिपॉज़िटरी चेकआउट (`git clone` \+ `openclaw ...` / `bun run openclaw ...`) से चलाते हैं:

  1. रिपॉज़िटरी हटाने से **पहले** Gateway सेवा अनइंस्टॉल करें (ऊपर दिया आसान रास्ता या मैन्युअल सेवा हटाना उपयोग करें)।
  2. रिपॉज़िटरी निर्देशिका हटाएँ।
  3. ऊपर दिखाए अनुसार स्थिति + कार्यस्थान हटाएँ।


## संबंधित

  * [इंस्टॉल अवलोकन](</hi/install>)
  * [माइग्रेशन गाइड](</hi/install/migrating>)


Was this useful?YesNo

Open issue