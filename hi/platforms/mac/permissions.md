---
title: macOS अनुमतियाँ
source_url: https://docs.openclaw.ai/hi/platforms/mac/permissions
scraped_at: 2026-06-29
---

PlatformsmacOS companion app

macOS अनुमति अनुदान नाजुक होते हैं। TCC किसी अनुमति अनुदान को ऐप के कोड हस्ताक्षर, बंडल पहचानकर्ता, और ऑन-डिस्क पथ से जोड़ता है। यदि इनमें से कुछ भी बदलता है, macOS ऐप को नया मानता है और प्रॉम्प्ट हटा या छिपा सकता है।

## स्थिर अनुमतियों की आवश्यकताएं

  * वही पथ: ऐप को किसी निश्चित स्थान से चलाएं (OpenClaw के लिए, `dist/OpenClaw.app`)।
  * वही बंडल पहचानकर्ता: बंडल ID बदलने से नई अनुमति पहचान बनती है।
  * हस्ताक्षरित ऐप: अहस्ताक्षरित या ad-hoc हस्ताक्षरित बिल्ड अनुमतियां स्थायी नहीं रखते।
  * सुसंगत हस्ताक्षर: वास्तविक Apple Development या Developer ID प्रमाणपत्र का उपयोग करें ताकि रीबिल्ड के बीच हस्ताक्षर स्थिर रहे।


Ad-hoc हस्ताक्षर हर बिल्ड में नई पहचान बनाते हैं। macOS पिछले अनुदान भूल जाएगा, और प्रॉम्प्ट पूरी तरह गायब हो सकते हैं जब तक पुराने प्रविष्टियां साफ़ नहीं की जातीं।

## Node और CLI रनटाइम के लिए Accessibility अनुदान

किसी सामान्य `node` बाइनरी के बजाय OpenClaw.app, Peekaboo.app, या अपने बंडल पहचानकर्ता वाले किसी अन्य हस्ताक्षरित हेल्पर को Accessibility देना बेहतर है।

macOS TCC जिस प्रक्रिया को देखता है उसकी कोड पहचान को Accessibility देता है। यदि कोई Homebrew, nvm, pnpm, या npm वर्कफ़्लो किसी साझा `node` executable को Accessibility दिला देता है, तो उसी executable के माध्यम से लॉन्च किया गया कोई भी JavaScript पैकेज GUI ऑटोमेशन विशेषाधिकार विरासत में पा सकता है।

System Settings में `node` प्रविष्टि को उस Node रनटाइम के लिए व्यापक अनुमति मानें, न कि किसी एक npm पैकेज के लिए अनुमति। `node` को Accessibility देने से बचें जब तक आप उस सटीक Node इंस्टॉल के माध्यम से लॉन्च किए गए हर script और package पर भरोसा न करते हों।

यदि आपने गलती से `node` को Accessibility दे दी है, तो उस प्रविष्टि को System Settings -> Privacy & Security -> Accessibility से हटाएं। फिर उस हस्ताक्षरित ऐप या हेल्पर को अनुमति दें जिसे UI ऑटोमेशन का स्वामी होना चाहिए।

## प्रॉम्प्ट गायब होने पर रिकवरी चेकलिस्ट

  1. ऐप बंद करें।
  2. System Settings -> Privacy & Security में ऐप प्रविष्टि हटाएं।
  3. ऐप को उसी पथ से दोबारा लॉन्च करें और अनुमतियां फिर से दें।
  4. यदि प्रॉम्प्ट फिर भी दिखाई नहीं देता, तो `tccutil` से TCC प्रविष्टियां रीसेट करें और फिर से कोशिश करें।
  5. कुछ अनुमतियां केवल पूर्ण macOS रीस्टार्ट के बाद फिर से दिखाई देती हैं।


रीसेट के उदाहरण (आवश्यकतानुसार बंडल ID बदलें):

bashCopy code
[code]
    sudo tccutil reset Accessibility ai.openclaw.macsudo tccutil reset ScreenCapture ai.openclaw.macsudo tccutil reset AppleEvents
[/code]

## फ़ाइलों और फ़ोल्डरों की अनुमतियां (Desktop/Documents/Downloads)

macOS टर्मिनल/बैकग्राउंड प्रक्रियाओं के लिए Desktop, Documents, और Downloads को भी गेट कर सकता है। यदि फ़ाइल पढ़ना या डायरेक्टरी लिस्टिंग अटक जाती है, तो उसी प्रक्रिया संदर्भ को access दें जो फ़ाइल operations करता है (उदाहरण के लिए Terminal/iTerm, LaunchAgent-launched app, या SSH process)।

वर्कअराउंड: यदि आप प्रति-फ़ोल्डर अनुदान से बचना चाहते हैं, तो फ़ाइलों को OpenClaw workspace (`~/.openclaw/workspace`) में ले जाएं।

यदि आप अनुमतियों का परीक्षण कर रहे हैं, तो हमेशा वास्तविक प्रमाणपत्र से हस्ताक्षर करें। Ad-hoc बिल्ड केवल उन त्वरित स्थानीय रन के लिए स्वीकार्य हैं जहां अनुमतियां मायने नहीं रखतीं।

## संबंधित

  * [macOS ऐप](</hi/platforms/macos>)
  * [macOS हस्ताक्षर](</hi/platforms/mac/signing>)


Was this useful?YesNo

Open issue