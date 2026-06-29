---
title: Node समस्या निवारण
source_url: https://docs.openclaw.ai/hi/nodes/troubleshooting
scraped_at: 2026-06-29
---

Gateway & OpsNodes and media

किसी node के status में दिखने पर लेकिन node tools के असफल होने पर इस पृष्ठ का उपयोग करें।

## कमांड क्रम

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctoropenclaw channels status --probe
[/code]

फिर node-विशिष्ट जांच चलाएँ:

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>
[/code]

स्वस्थ संकेत:

  * Node जुड़ा हुआ है और role `node` के लिए paired है।
  * `nodes describe` में वह capability शामिल है जिसे आप कॉल कर रहे हैं।
  * Exec approvals अपेक्षित mode/allowlist दिखाते हैं।


## foreground आवश्यकताएँ

`canvas.*`, `camera.*`, और `screen.*` iOS/Android nodes पर केवल foreground में उपलब्ध हैं।

त्वरित जांच और सुधार:

bashCopy code
[code]
    openclaw nodes describe --node <idOrNameOrIp>openclaw nodes canvas snapshot --node <idOrNameOrIp>openclaw logs --follow
[/code]

यदि आपको `NODE_BACKGROUND_UNAVAILABLE` दिखता है, तो node app को foreground में लाएँ और फिर से प्रयास करें।

## अनुमतियों की मैट्रिक्स

Capability | iOS | Android | macOS node app | सामान्य failure code  
---|---|---|---|---  
`camera.snap`, `camera.clip` | Camera (clip audio के लिए mic सहित) | Camera (clip audio के लिए mic सहित) | Camera (clip audio के लिए mic सहित) | `*_PERMISSION_REQUIRED`  
`screen.record` | Screen Recording (mic वैकल्पिक) | Screen capture prompt (mic वैकल्पिक) | Screen Recording | `*_PERMISSION_REQUIRED`  
`location.get` | While Using या Always (mode पर निर्भर) | mode के आधार पर Foreground/Background location | Location permission | `LOCATION_PERMISSION_REQUIRED`  
`system.run` | n/a (node host path) | n/a (node host path) | Exec approvals आवश्यक | `SYSTEM_RUN_DENIED`  
  
## Pairing बनाम approvals

ये अलग-अलग gates हैं:

  1. **Device pairing** : क्या यह node gateway से connect हो सकता है?
  2. **Gateway node command policy** : क्या RPC command ID को `gateway.nodes.allowCommands` / `denyCommands` और platform defaults द्वारा अनुमति है?
  3. **Exec approvals** : क्या यह node किसी विशिष्ट shell command को locally चला सकता है?


त्वरित जांच:

bashCopy code
[code]
    openclaw devices listopenclaw nodes statusopenclaw approvals get --node <idOrNameOrIp>openclaw approvals allowlist add --node <idOrNameOrIp> "/usr/bin/uname"
[/code]

यदि pairing अनुपस्थित है, तो पहले node device को approve करें। यदि `nodes describe` में कोई command अनुपस्थित है, तो gateway node command policy और यह जांचें कि node ने connect होते समय वास्तव में वह command घोषित किया था या नहीं। यदि pairing ठीक है लेकिन `system.run` विफल होता है, तो उस node पर exec approvals/allowlist ठीक करें।

Node pairing एक identity/trust gate है, per-command approval surface नहीं। `system.run` के लिए, per-node policy उस node की exec approvals file (`openclaw approvals get --node ...`) में रहती है, gateway pairing record में नहीं।

approval-backed `host=node` runs के लिए, gateway execution को तैयार canonical `systemRunPlan` से भी bind करता है। यदि कोई बाद का caller approved run forward होने से पहले command/cwd या session metadata बदलता है, तो gateway edited payload पर भरोसा करने के बजाय run को approval mismatch के रूप में reject करता है।

## सामान्य node error codes

  * `NODE_BACKGROUND_UNAVAILABLE` → app backgrounded है; इसे foreground में लाएँ।
  * `CAMERA_DISABLED` → node settings में camera toggle disabled है।
  * `*_PERMISSION_REQUIRED` → OS permission अनुपस्थित/denied है।
  * `LOCATION_DISABLED` → location mode off है।
  * `LOCATION_PERMISSION_REQUIRED` → requested location mode granted नहीं है।
  * `LOCATION_BACKGROUND_UNAVAILABLE` → app backgrounded है लेकिन केवल While Using permission मौजूद है।
  * `SYSTEM_RUN_DENIED: approval required` → exec request को explicit approval चाहिए।
  * `SYSTEM_RUN_DENIED: allowlist miss` → command allowlist mode द्वारा blocked है। Windows node hosts पर, `cmd.exe /c ...` जैसे shell-wrapper forms को allowlist mode में allowlist misses माना जाता है, जब तक ask flow के माध्यम से approved न हों।


## तेज़ recovery loop

bashCopy code
[code]
    openclaw nodes statusopenclaw nodes describe --node <idOrNameOrIp>openclaw approvals get --node <idOrNameOrIp>openclaw logs --follow
[/code]

यदि अभी भी अटके हैं:

  * Device pairing को फिर से approve करें।
  * Node app को फिर से खोलें (foreground).
  * OS permissions फिर से grant करें।
  * Exec approval policy को recreate/adjust करें।


## संबंधित

  * [Nodes overview](</hi/nodes>)
  * [Camera nodes](</hi/nodes/camera>)
  * [Location command](</hi/nodes/location-command>)
  * [Exec approvals](</hi/tools/exec-approvals>)
  * [Gateway pairing](</hi/gateway/pairing>)
  * [Gateway troubleshooting](</hi/gateway/troubleshooting>)
  * [Channel troubleshooting](</hi/channels/troubleshooting>)


Was this useful?YesNo

Open issue