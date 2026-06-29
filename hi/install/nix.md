---
title: Nix
source_url: https://docs.openclaw.ai/hi/install/nix
scraped_at: 2026-06-29
---

InstallContainers

OpenClaw को घोषणात्मक रूप से **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** के साथ इंस्टॉल करें - प्रथम-पक्ष, batteries-included Home Manager मॉड्यूल।

## आपको क्या मिलता है

  * Gateway + macOS ऐप + टूल्स (whisper, spotify, cameras) -- सभी पिन किए गए
  * Launchd सेवा जो रीबूट के बाद भी बनी रहती है
  * घोषणात्मक कॉन्फ़िग के साथ Plugin सिस्टम
  * तत्काल रोलबैक: `home-manager switch --rollback`


## त्वरित शुरुआत

* ### Determinate Nix इंस्टॉल करें

यदि Nix पहले से इंस्टॉल नहीं है, तो [Determinate Nix installer](<https://github.com/DeterminateSystems/nix-installer>) निर्देशों का पालन करें।

* ### एक स्थानीय flake बनाएँ

nix-openclaw रेपो से agent-first टेम्पलेट का उपयोग करें:

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### सीक्रेट कॉन्फ़िगर करें

अपना मैसेजिंग बॉट टोकन और मॉडल प्रदाता API कुंजी सेट करें। `~/.secrets/` पर प्लेन फ़ाइलें ठीक काम करती हैं।

* ### टेम्पलेट प्लेसहोल्डर भरें और स्विच करें

bashCopy code
[code]
    home-manager switch
[/code]

* ### सत्यापित करें

पुष्टि करें कि launchd सेवा चल रही है और आपका बॉट संदेशों का जवाब देता है।

पूर्ण मॉड्यूल विकल्पों और उदाहरणों के लिए [nix-openclaw README](<https://github.com/openclaw/nix-openclaw>) देखें।

## Nix-mode रनटाइम व्यवहार

जब `OPENCLAW_NIX_MODE=1` सेट होता है (nix-openclaw के साथ स्वचालित), OpenClaw Nix-प्रबंधित इंस्टॉल के लिए निर्धारक मोड में प्रवेश करता है। अन्य Nix पैकेज भी वही मोड सेट कर सकते हैं; nix-openclaw प्रथम-पक्ष संदर्भ है।

आप इसे मैन्युअल रूप से भी सेट कर सकते हैं:

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

macOS पर, GUI ऐप shell environment variables को स्वचालित रूप से इनहेरिट नहीं करता। इसके बजाय defaults के माध्यम से Nix मोड सक्षम करें:

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### Nix मोड में क्या बदलता है

  * ऑटो-इंस्टॉल और सेल्फ़-म्यूटेशन फ़्लो अक्षम होते हैं
  * `openclaw.json` को अपरिवर्तनीय माना जाता है। स्टार्टअप-व्युत्पन्न defaults केवल रनटाइम में रहते हैं, और setup, onboarding, mutating `openclaw update`, plugin install/update/uninstall/enable, `doctor --fix`, `doctor --generate-gateway-token`, और `openclaw config set` जैसे कॉन्फ़िग लेखक फ़ाइल को संपादित करने से इनकार करते हैं।
  * Agents को इसके बजाय Nix स्रोत संपादित करना चाहिए। nix-openclaw के लिए, agent-first [Quick Start](<https://github.com/openclaw/nix-openclaw#quick-start>) का उपयोग करें और `programs.openclaw.config` या `instances.<name>.config` के अंतर्गत कॉन्फ़िग सेट करें।
  * अनुपलब्ध dependencies Nix-विशिष्ट सुधार संदेश दिखाती हैं
  * UI read-only Nix मोड बैनर दिखाता है


### कॉन्फ़िग और state पथ

OpenClaw `OPENCLAW_CONFIG_PATH` से JSON5 कॉन्फ़िग पढ़ता है और mutable data को `OPENCLAW_STATE_DIR` में संग्रहीत करता है। Nix के अंतर्गत चलाते समय, इन्हें स्पष्ट रूप से Nix-प्रबंधित स्थानों पर सेट करें ताकि runtime state और config immutable store से बाहर रहें।

Variable | Default  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### Service PATH discovery

launchd/systemd Gateway सेवा Nix-profile binaries को स्वतः खोजती है ताकि `nix`-इंस्टॉल किए गए executables को shell out करने वाले plugins और tools बिना मैन्युअल PATH सेटअप के काम करें:

  * जब `NIX_PROFILES` सेट होता है, तो हर entry को service PATH में दाएँ-से-बाएँ precedence में जोड़ा जाता है (Nix shell precedence से मेल खाता है - सबसे दायाँ जीतता है)।
  * जब `NIX_PROFILES` unset होता है, तो `~/.nix-profile/bin` fallback के रूप में जोड़ा जाता है।


यह macOS launchd और Linux systemd service environments दोनों पर लागू होता है।

## संबंधित

[**nix-openclaw** Source-of-truth Home Manager मॉड्यूल और पूर्ण setup guide। ](<https://github.com/openclaw/nix-openclaw>) [**Setup wizard** Non-Nix CLI setup walkthrough। ](</hi/start/wizard>) [**Docker** Non-Nix alternative के रूप में containerized setup। ](</hi/install/docker>) [**Updating** package के साथ Home Manager-managed installs को update करना। ](</hi/install/updating>)

Was this useful?YesNo

Open issue