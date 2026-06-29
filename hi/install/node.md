---
title: Node.js
source_url: https://docs.openclaw.ai/hi/install/node
scraped_at: 2026-06-29
---

InstallInstall overview

OpenClaw के लिए **Node 22.19 या नया** आवश्यक है। इंस्टॉल, CI, और रिलीज़ वर्कफ़्लो के लिए **Node 24 डिफ़ॉल्ट और अनुशंसित runtime** है। Node 22 सक्रिय LTS लाइन के माध्यम से समर्थित बना रहता है। [installer script](</hi/install#alternative-install-methods>) Node को अपने-आप पहचानकर इंस्टॉल कर देगी - यह पेज तब के लिए है जब आप Node खुद सेट अप करना चाहते हैं और सुनिश्चित करना चाहते हैं कि सब कुछ सही तरह से जुड़ा है (versions, PATH, global installs)।

## अपना version जांचें

bashCopy code
[code]
    node -v
[/code]

अगर यह `v24.x.x` या उससे ऊपर प्रिंट करता है, तो आप अनुशंसित डिफ़ॉल्ट पर हैं। अगर यह `v22.19.x` या उससे ऊपर प्रिंट करता है, तो आप समर्थित Node 22 LTS पथ पर हैं, लेकिन सुविधाजनक होने पर हम फिर भी Node 24 पर अपग्रेड करने की सलाह देते हैं। अगर Node इंस्टॉल नहीं है या version बहुत पुराना है, तो नीचे कोई इंस्टॉल विधि चुनें।

## Node इंस्टॉल करें

### macOS

**Homebrew** (अनुशंसित):

bashCopy code
[code]
    brew install node
[/code]

या [nodejs.org](<https://nodejs.org/>) से macOS installer डाउनलोड करें।

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

या version manager इस्तेमाल करें (नीचे देखें)।

### Windows

**winget** (अनुशंसित):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

या [nodejs.org](<https://nodejs.org/>) से Windows installer डाउनलोड करें।

version manager का उपयोग करना (nvm, fnm, mise, asdf)

version manager आपको Node versions के बीच आसानी से स्विच करने देते हैं। लोकप्रिय विकल्प:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- तेज, cross-platform
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- macOS/Linux पर व्यापक रूप से उपयोग किया जाता है
  * [**mise**](<https://mise.jdx.dev/>) \- polyglot (Node, Python, Ruby, आदि)


fnm के साथ उदाहरण:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## समस्या निवारण

### `openclaw: command not found`

इसका लगभग हमेशा मतलब होता है कि npm की global bin directory आपके PATH पर नहीं है।

* ### अपना global npm prefix खोजें

bashCopy code
[code]
    npm prefix -g
[/code]

* ### जांचें कि यह आपके PATH पर है या नहीं

bashCopy code
[code]
    echo "$PATH"
[/code]

output में `<npm-prefix>/bin` (macOS/Linux) या `<npm-prefix>` (Windows) देखें।

* ### इसे अपनी shell startup file में जोड़ें

### macOS / Linux

`~/.zshrc` या `~/.bashrc` में जोड़ें:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

फिर नया terminal खोलें (या zsh में `rehash` / bash में `hash -r` चलाएं)।

### Windows

Settings → System → Environment Variables के माध्यम से `npm prefix -g` का output अपने system PATH में जोड़ें।

### `npm install -g` पर permission errors (Linux)

अगर आपको `EACCES` errors दिखें, तो npm के global prefix को user-writable directory पर स्विच करें:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

इसे स्थायी बनाने के लिए `export PATH=...` line को अपने `~/.bashrc` या `~/.zshrc` में जोड़ें।

## संबंधित

  * [इंस्टॉल अवलोकन](</hi/install>) \- सभी installation methods
  * [अपडेट करना](</hi/install/updating>) \- OpenClaw को up to date रखना
  * [शुरुआत करना](</hi/start/getting-started>) \- install के बाद पहले steps


Was this useful?YesNo

Open issue