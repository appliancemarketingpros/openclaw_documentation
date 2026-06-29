---
title: Ansible
source_url: https://docs.openclaw.ai/hi/install/ansible
scraped_at: 2026-06-29
---

InstallContainers

सुरक्षा-प्रथम आर्किटेक्चर वाले स्वचालित इंस्टॉलर **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** के साथ OpenClaw को उत्पादन सर्वरों पर तैनात करें।

## पूर्वापेक्षाएँ

आवश्यकता | विवरण  
---|---  
**OS** | Debian 11+ या Ubuntu 20.04+  
**पहुँच** | Root या sudo विशेषाधिकार  
**नेटवर्क** | पैकेज इंस्टॉलेशन के लिए इंटरनेट कनेक्शन  
**Ansible** | 2.14+ (क्विक-स्टार्ट स्क्रिप्ट द्वारा अपने-आप इंस्टॉल)  
  
## आपको क्या मिलता है

  * **Firewall-प्रथम सुरक्षा** \-- UFW + Docker आइसोलेशन (केवल SSH + Tailscale पहुँच योग्य)
  * **Tailscale VPN** \-- सेवाओं को सार्वजनिक रूप से उजागर किए बिना सुरक्षित रिमोट पहुँच
  * **Docker** \-- आइसोलेटेड सैंडबॉक्स कंटेनर, केवल localhost बाइंडिंग
  * **गहन रक्षा** \-- 4-स्तरीय सुरक्षा आर्किटेक्चर
  * **Systemd एकीकरण** \-- हार्डनिंग के साथ बूट पर ऑटो-स्टार्ट
  * **एक-कमांड सेटअप** \-- मिनटों में पूरा परिनियोजन


## त्वरित शुरुआत

एक-कमांड इंस्टॉल:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## क्या इंस्टॉल होता है

Ansible playbook इंस्टॉल और कॉन्फ़िगर करता है:

  1. **Tailscale** \-- सुरक्षित रिमोट पहुँच के लिए mesh VPN
  2. **UFW firewall** \-- केवल SSH + Tailscale पोर्ट
  3. **Docker CE + Compose V2** \-- डिफ़ॉल्ट एजेंट सैंडबॉक्स बैकएंड के लिए
  4. **Node.js 24 + pnpm** \-- रनटाइम निर्भरताएँ (Node 22 LTS, वर्तमान में `22.19+`, समर्थित रहता है)
  5. **OpenClaw** \-- होस्ट-आधारित, कंटेनरीकृत नहीं
  6. **Systemd सेवा** \-- सुरक्षा हार्डनिंग के साथ ऑटो-स्टार्ट


## इंस्टॉल के बाद सेटअप

* ### openclaw उपयोगकर्ता पर स्विच करें

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### ऑनबोर्डिंग विज़ार्ड चलाएँ

पोस्ट-इंस्टॉल स्क्रिप्ट आपको OpenClaw सेटिंग्स कॉन्फ़िगर करने में मार्गदर्शन करती है।

* ### मैसेजिंग प्रदाताओं को कनेक्ट करें

WhatsApp, Telegram, Discord, या Signal में लॉग इन करें:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### इंस्टॉलेशन सत्यापित करें

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Tailscale से कनेक्ट करें

सुरक्षित रिमोट पहुँच के लिए अपने VPN mesh से जुड़ें।

### त्वरित कमांड

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## सुरक्षा आर्किटेक्चर

परिनियोजन 4-स्तरीय रक्षा मॉडल का उपयोग करता है:

  1. **Firewall (UFW)** \-- केवल SSH (22) + Tailscale (41641/udp) सार्वजनिक रूप से उजागर
  2. **VPN (Tailscale)** \-- Gateway केवल VPN mesh के माध्यम से पहुँच योग्य
  3. **Docker आइसोलेशन** \-- DOCKER-USER iptables चेन बाहरी पोर्ट एक्सपोज़र रोकती है
  4. **Systemd हार्डनिंग** \-- NoNewPrivileges, PrivateTmp, विशेषाधिकार-रहित उपयोगकर्ता


अपनी बाहरी अटैक सतह सत्यापित करने के लिए:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

केवल पोर्ट 22 (SSH) खुला होना चाहिए। अन्य सभी सेवाएँ (Gateway, Docker) लॉक डाउन रहती हैं।

Docker एजेंट सैंडबॉक्स (आइसोलेटेड टूल निष्पादन) के लिए इंस्टॉल होता है, Gateway स्वयं चलाने के लिए नहीं। सैंडबॉक्स कॉन्फ़िगरेशन के लिए [Multi-Agent Sandbox and Tools](</hi/tools/multi-agent-sandbox-tools>) देखें।

## मैनुअल इंस्टॉलेशन

यदि आप स्वचालन पर मैनुअल नियंत्रण पसंद करते हैं:

* ### पूर्वापेक्षाएँ इंस्टॉल करें

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### रिपॉज़िटरी क्लोन करें

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Ansible collections इंस्टॉल करें

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### playbook चलाएँ

bashCopy code
[code]
    ./run-playbook.sh
[/code]

वैकल्पिक रूप से, सीधे चलाएँ और फिर बाद में सेटअप स्क्रिप्ट मैनुअली निष्पादित करें:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## अपडेट करना

Ansible इंस्टॉलर OpenClaw को मैनुअल अपडेट के लिए सेट करता है। मानक अपडेट प्रवाह के लिए [Updating](</hi/install/updating>) देखें।

Ansible playbook फिर से चलाने के लिए (उदाहरण के लिए, कॉन्फ़िगरेशन बदलावों के लिए):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

यह idempotent है और कई बार चलाना सुरक्षित है।

## समस्या निवारण

Firewall मेरा कनेक्शन ब्लॉक करता है

  * सुनिश्चित करें कि पहले आप Tailscale VPN के माध्यम से पहुँच सकते हैं
  * SSH पहुँच (पोर्ट 22) हमेशा अनुमत है
  * Gateway डिज़ाइन के अनुसार केवल Tailscale के माध्यम से पहुँच योग्य है

सेवा शुरू नहीं होगी bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Docker सैंडबॉक्स समस्याएँ bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

प्रदाता लॉगिन विफल होता है

सुनिश्चित करें कि आप `openclaw` उपयोगकर्ता के रूप में चला रहे हैं:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## उन्नत कॉन्फ़िगरेशन

विस्तृत सुरक्षा आर्किटेक्चर और समस्या निवारण के लिए, openclaw-ansible रेपो देखें:

  * [सुरक्षा आर्किटेक्चर](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [तकनीकी विवरण](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [समस्या निवारण गाइड](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## संबंधित

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- पूर्ण परिनियोजन गाइड
  * [Docker](</hi/install/docker>) \-- कंटेनरीकृत Gateway सेटअप
  * [Sandboxing](</hi/gateway/sandboxing>) \-- एजेंट सैंडबॉक्स कॉन्फ़िगरेशन
  * [Multi-Agent Sandbox and Tools](</hi/tools/multi-agent-sandbox-tools>) \-- प्रति-एजेंट आइसोलेशन


Was this useful?YesNo

Open issue