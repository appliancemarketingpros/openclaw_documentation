---
title: निर्देशिका
source_url: https://docs.openclaw.ai/hi/cli/directory
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw directory`

इसका समर्थन करने वाले चैनलों के लिए डायरेक्टरी लुकअप (संपर्क/पीयर, समूह, और "me")।

## सामान्य फ़्लैग

  * `--channel <name>`: चैनल आईडी/उपनाम (जब कई चैनल कॉन्फ़िगर किए गए हों तो आवश्यक; केवल एक कॉन्फ़िगर होने पर स्वतः)
  * `--account <id>`: खाता आईडी (डिफ़ॉल्ट: चैनल डिफ़ॉल्ट)
  * `--json`: JSON आउटपुट करें


## नोट्स

  * `directory` का उद्देश्य ऐसी आईडी ढूँढने में आपकी मदद करना है जिन्हें आप दूसरे कमांड में पेस्ट कर सकते हैं (विशेष रूप से `openclaw message send --target ...`)।
  * कई चैनलों के लिए, परिणाम लाइव प्रदाता डायरेक्टरी के बजाय कॉन्फ़िग-समर्थित (allowlists / कॉन्फ़िगर किए गए समूह) होते हैं।
  * इंस्टॉल किए गए चैनल Plugin फिर भी डायरेक्टरी समर्थन छोड़ सकते हैं; ऐसे में कमांड Plugin को फिर से इंस्टॉल करने के बजाय असमर्थित डायरेक्टरी ऑपरेशन की रिपोर्ट करता है।
  * डिफ़ॉल्ट आउटपुट टैब से अलग किया गया `id` (और कभी-कभी `name`) होता है; स्क्रिप्टिंग के लिए `--json` का उपयोग करें।


## `message send` के साथ परिणामों का उपयोग

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## आईडी फ़ॉर्मैट (चैनल के अनुसार)

  * WhatsApp: `+15551234567` (DM), `1234567890-1234567890@g.us` (समूह), `120363123456789@newsletter` (चैनल/न्यूज़लेटर आउटबाउंड लक्ष्य)
  * Telegram: `@username` या संख्यात्मक चैट आईडी; समूह संख्यात्मक आईडी होते हैं
  * Slack: `user:U…` और `channel:C…`
  * Discord: `user:<id>` और `channel:<id>`
  * Matrix (Plugin): `user:@user:server`, `room:!roomId:server`, या `#alias:server`
  * Microsoft Teams (Plugin): `user:<id>` और `conversation:<id>`
  * Zalo (Plugin): उपयोगकर्ता आईडी (Bot API)
  * Zalo Personal / `zalouser` (Plugin): `zca` से थ्रेड आईडी (DM/समूह) (`me`, `friend list`, `group list`)


## स्वयं ("me")

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## पीयर (संपर्क/उपयोगकर्ता)

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## समूह

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## संबंधित

  * [CLI संदर्भ](</hi/cli>)


Was this useful?YesNo

Open issue