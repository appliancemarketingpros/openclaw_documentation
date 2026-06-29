---
title: कैनवास
source_url: https://docs.openclaw.ai/hi/platforms/mac/canvas
scraped_at: 2026-06-29
---

PlatformsmacOS companion app

macOS ऐप `WKWebView` का उपयोग करके एजेंट-नियंत्रित **कैनवास पैनल** एम्बेड करता है। यह HTML/CSS/JS, A2UI, और छोटी इंटरैक्टिव UI सतहों के लिए एक हल्का दृश्य कार्यक्षेत्र है।

## कैनवास कहाँ रहता है

कैनवास स्थिति Application Support के अंतर्गत संग्रहीत होती है:

  * `~/Library/Application Support/OpenClaw/canvas/<session>/...`


कैनवास पैनल इन फ़ाइलों को एक **कस्टम URL स्कीम** के माध्यम से सर्व करता है:

  * `openclaw-canvas://<session>/<path>`


उदाहरण:

  * `openclaw-canvas://main/` → `<canvasRoot>/main/index.html`
  * `openclaw-canvas://main/assets/app.css` → `<canvasRoot>/main/assets/app.css`
  * `openclaw-canvas://main/widgets/todo/` → `<canvasRoot>/main/widgets/todo/index.html`


यदि रूट पर कोई `index.html` मौजूद नहीं है, तो ऐप एक **अंतर्निहित स्कैफ़ोल्ड पेज** दिखाता है।

## पैनल व्यवहार

  * मेनू बार (या माउस कर्सर) के पास एंकर किया गया बॉर्डरलेस, आकार बदलने योग्य पैनल।
  * प्रति सत्र आकार/स्थिति याद रखता है।
  * स्थानीय कैनवास फ़ाइलों में बदलाव होने पर अपने-आप रीलोड होता है।
  * एक समय में केवल एक कैनवास पैनल दिखाई देता है (आवश्यकतानुसार सत्र बदला जाता है)।


कैनवास को सेटिंग्स → **कैनवास की अनुमति दें** से बंद किया जा सकता है। बंद होने पर, कैनवास नोड कमांड `CANVAS_DISABLED` लौटाते हैं।

## एजेंट API सतह

कैनवास **Gateway WebSocket** के माध्यम से उपलब्ध है, इसलिए एजेंट ये कर सकता है:

  * पैनल दिखाना/छिपाना
  * किसी पथ या URL पर नेविगेट करना
  * JavaScript का मूल्यांकन करना
  * स्नैपशॉट इमेज कैप्चर करना


CLI उदाहरण:

bashCopy code
[code]
    openclaw nodes canvas present --node <id>openclaw nodes canvas navigate --node <id> --url "/"openclaw nodes canvas eval --node <id> --js "document.title"openclaw nodes canvas snapshot --node <id>
[/code]

नोट्स:

  * `canvas.navigate` **स्थानीय कैनवास पथ** , `http(s)` URL, और `file://` URL स्वीकार करता है।
  * यदि आप `"/"` पास करते हैं, तो कैनवास स्थानीय स्कैफ़ोल्ड या `index.html` दिखाता है।


## कैनवास में A2UI

A2UI को Gateway कैनवास होस्ट द्वारा होस्ट किया जाता है और कैनवास पैनल के भीतर रेंडर किया जाता है। जब Gateway कैनवास होस्ट का विज्ञापन करता है, तो macOS ऐप पहली बार खोलने पर अपने-आप A2UI होस्ट पेज पर नेविगेट करता है।

डिफ़ॉल्ट A2UI होस्ट URL:

CodeCopy code
[code]
    http://<gateway-host>:18789/__openclaw__/a2ui/
[/code]

### A2UI कमांड (v0.8)

कैनवास वर्तमान में **A2UI v0.8** सर्वर→क्लाइंट संदेश स्वीकार करता है:

  * `beginRendering`
  * `surfaceUpdate`
  * `dataModelUpdate`
  * `deleteSurface`


`createSurface` (v0.9) समर्थित नहीं है।

CLI उदाहरण:

bashCopy code
[code]
    cat > /tmp/a2ui-v0.8.jsonl <<'EOFA2'{"surfaceUpdate":{"surfaceId":"main","components":[{"id":"root","component":{"Column":{"children":{"explicitList":["title","content"]}}}},{"id":"title","component":{"Text":{"text":{"literalString":"Canvas (A2UI v0.8)"},"usageHint":"h1"}}},{"id":"content","component":{"Text":{"text":{"literalString":"If you can read this, A2UI push works."},"usageHint":"body"}}}]}}{"beginRendering":{"surfaceId":"main","root":"root"}}EOFA2 openclaw nodes canvas a2ui push --jsonl /tmp/a2ui-v0.8.jsonl --node <id>
[/code]

त्वरित स्मोक:

bashCopy code
[code]
    openclaw nodes canvas a2ui push --node <id> --text "Hello from A2UI"
[/code]

## कैनवास से एजेंट रन ट्रिगर करना

कैनवास डीप लिंक के माध्यम से नए एजेंट रन ट्रिगर कर सकता है:

  * `openclaw://agent?...`


उदाहरण (JS में):

jsCopy code
[code]
    window.location.href = "openclaw://agent?message=Review%20this%20design";
[/code]

समर्थित क्वेरी पैरामीटर:

  * `message`: पहले से भरा हुआ एजेंट प्रॉम्प्ट।
  * `sessionKey`: स्थिर सत्र पहचानकर्ता।
  * `thinking`: वैकल्पिक थिंकिंग प्रोफ़ाइल।
  * `deliver`, `to`, या `channel`: डिलीवरी लक्ष्य।
  * `timeoutSeconds`: वैकल्पिक रन टाइमआउट।
  * `key`: विश्वसनीय स्थानीय कॉलर के लिए ऐप-जनरेटेड सुरक्षा टोकन।


वैध कुंजी प्रदान न होने पर ऐप पुष्टि के लिए पूछता है। बिना कुंजी वाले लिंक स्वीकृति से पहले संदेश और URL दिखाते हैं, और डिलीवरी रूटिंग फ़ील्ड अनदेखा करते हैं; कुंजी वाले लिंक सामान्य Gateway रन पथ का उपयोग करते हैं।

## सुरक्षा नोट्स

  * कैनवास स्कीम डायरेक्टरी ट्रैवर्सल को ब्लॉक करती है; फ़ाइलें सत्र रूट के अंतर्गत होनी चाहिए।
  * स्थानीय कैनवास सामग्री कस्टम स्कीम का उपयोग करती है (किसी loopback सर्वर की आवश्यकता नहीं)।
  * बाहरी `http(s)` URL केवल स्पष्ट रूप से नेविगेट किए जाने पर अनुमत हैं।


## संबंधित

  * [macOS ऐप](</hi/platforms/macos>)
  * [WebChat](</hi/web/webchat>)


Was this useful?YesNo

Open issue