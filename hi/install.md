---
title: इंस्टॉल करें
source_url: https://docs.openclaw.ai/hi/install
scraped_at: 2026-06-29
---

InstallInstall overview

## सिस्टम आवश्यकताएँ

  * **Node 24** (अनुशंसित) या Node 22.19+ - इंस्टॉलर स्क्रिप्ट इसे अपने आप संभालती है
  * **macOS, Linux, या Windows** \- Windows उपयोगकर्ता नेटिव Windows Hub ऐप, PowerShell CLI इंस्टॉलर, या WSL2 Gateway से शुरू कर सकते हैं। देखें [Windows](</hi/platforms/windows>)।
  * `pnpm` की ज़रूरत केवल तब होती है जब आप स्रोत से बिल्ड करते हैं


## अनुशंसित: इंस्टॉलर स्क्रिप्ट

इंस्टॉल करने का सबसे तेज़ तरीका। यह आपका OS पहचानता है, ज़रूरत होने पर Node इंस्टॉल करता है, OpenClaw इंस्टॉल करता है, और ऑनबोर्डिंग शुरू करता है।

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

ऑनबोर्डिंग चलाए बिना इंस्टॉल करने के लिए:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

सभी फ़्लैग और CI/ऑटोमेशन विकल्पों के लिए, देखें [इंस्टॉलर आंतरिक विवरण](</hi/install/installer>)।

## वैकल्पिक इंस्टॉल विधियाँ

### लोकल प्रीफ़िक्स इंस्टॉलर (`install-cli.sh`)

इसे तब उपयोग करें जब आप चाहते हों कि OpenClaw और Node किसी लोकल प्रीफ़िक्स, जैसे `~/.openclaw`, के तहत रहें, बिना सिस्टम-वाइड Node इंस्टॉल पर निर्भर हुए:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

यह डिफ़ॉल्ट रूप से npm इंस्टॉल का समर्थन करता है, साथ ही उसी प्रीफ़िक्स फ़्लो के तहत git-checkout इंस्टॉल का भी। पूरा संदर्भ: [इंस्टॉलर आंतरिक विवरण](</hi/install/installer#install-clish>)।

पहले से इंस्टॉल है? पैकेज और git इंस्टॉल के बीच स्विच करें `openclaw update --channel dev` और `openclaw update --channel stable` के साथ। देखें [अपडेट करना](</hi/install/updating#switch-between-npm-and-git-installs>)।

### npm, pnpm, या bun

यदि आप पहले से Node स्वयं मैनेज करते हैं:

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### स्रोत से

योगदानकर्ताओं या उन सभी के लिए जो लोकल checkout से चलाना चाहते हैं:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

या link छोड़ें और repo के अंदर से `pnpm openclaw ...` उपयोग करें। पूर्ण विकास workflows के लिए देखें [सेटअप](</hi/start/setup>)।

### GitHub main checkout से इंस्टॉल करें

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git --version main
[/code]

### कंटेनर और पैकेज मैनेजर

[**Docker** कंटेनराइज़्ड या headless deployments। ](</hi/install/docker>) [**Podman** Docker का rootless कंटेनर विकल्प। ](</hi/install/podman>) [**Nix** Nix flake के ज़रिए घोषणात्मक इंस्टॉल। ](</hi/install/nix>) [**Ansible** स्वचालित fleet provisioning। ](</hi/install/ansible>) [**Bun** Bun runtime के ज़रिए केवल-CLI उपयोग। ](</hi/install/bun>)

## इंस्टॉल सत्यापित करें

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

यदि आप इंस्टॉल के बाद managed startup चाहते हैं:

  * macOS: `openclaw onboard --install-daemon` या `openclaw gateway install` के ज़रिए LaunchAgent
  * Linux/WSL2: उन्हीं commands के ज़रिए systemd user service
  * नेटिव Windows: पहले Scheduled Task, और यदि task बनाना अस्वीकार हो जाए तो प्रति-उपयोगकर्ता Startup-folder login item fallback


## होस्टिंग और deployment

OpenClaw को cloud server या VPS पर deploy करें:

[**VPS** कोई भी Linux VPS। ](</hi/vps>) [**Docker VM** साझा Docker चरण। ](</hi/install/docker-vm-runtime>) [**Kubernetes** K8s deployment। ](</hi/install/kubernetes>) [**Fly.io** Fly.io पर deploy करें। ](</hi/install/fly>) [**Hetzner** Hetzner deployment। ](</hi/install/hetzner>) [**GCP** Google Cloud deployment। ](</hi/install/gcp>) [**Azure** Azure deployment। ](</hi/install/azure>) [**Railway** Railway deployment। ](</hi/install/railway>) [**Render** Render deployment। ](</hi/install/render>) [**Northflank** Northflank deployment। ](</hi/install/northflank>)

## अपडेट, migrate, या uninstall करें

[**Updating** OpenClaw को अद्यतित रखें। ](</hi/install/updating>) [**Migrating** नई मशीन पर जाएँ। ](</hi/install/migrating>) [**Uninstall** OpenClaw को पूरी तरह हटाएँ। ](</hi/install/uninstall>)

## समस्या निवारण: `openclaw` नहीं मिला

यदि इंस्टॉल सफल रहा लेकिन आपके terminal में `openclaw` नहीं मिला:

bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

यदि `$(npm prefix -g)/bin` आपके `$PATH` में नहीं है, तो इसे अपनी shell startup file (`~/.zshrc` या `~/.bashrc`) में जोड़ें:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

फिर नया terminal खोलें। अधिक विवरण के लिए देखें [Node सेटअप](</hi/install/node>)।

Was this useful?YesNo

Open issue