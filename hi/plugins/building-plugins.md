---
title: Plugin बनाना
source_url: https://docs.openclaw.ai/hi/plugins/building-plugins
scraped_at: 2026-06-29
---

CapabilitiesBuilding plugins

Plugin कोर बदले बिना OpenClaw का विस्तार करते हैं। कोई Plugin मैसेजिंग चैनल, मॉडल प्रदाता, स्थानीय CLI बैकएंड, एजेंट टूल, हुक, मीडिया प्रदाता, या कोई अन्य Plugin-स्वामित्व वाली क्षमता जोड़ सकता है।

आपको OpenClaw repository में बाहरी Plugin जोड़ने की आवश्यकता नहीं है। पैकेज को [ClawHub](</hi/clawhub>) पर प्रकाशित करें और उपयोगकर्ता इसे इससे इंस्टॉल करते हैं:

bashCopy code
[code]
    openclaw plugins install clawhub:<package-name>
[/code]

लॉन्च कटओवर के दौरान bare package specs अब भी npm से इंस्टॉल होते हैं। जब आप ClawHub resolution चाहते हों, तो `clawhub:` prefix का उपयोग करें।

## आवश्यकताएँ

  * Node 22.19 या नया और `npm` या `pnpm` जैसा package manager उपयोग करें।
  * TypeScript ESM modules से परिचित रहें।
  * in-repo bundled Plugin कार्य के लिए, repository clone करें और `pnpm install` चलाएँ। Source-checkout Plugin development केवल pnpm है क्योंकि OpenClaw bundled Plugins को `extensions/*` workspace packages से लोड करता है।


## Plugin आकार चुनें

[**Channel Plugin** OpenClaw को किसी मैसेजिंग platform से कनेक्ट करें। ](</hi/plugins/sdk-channel-plugins>) [**Provider Plugin** कोई मॉडल, मीडिया, खोज, fetch, speech, या realtime प्रदाता जोड़ें। ](</hi/plugins/sdk-provider-plugins>) [**CLI backend Plugin** OpenClaw मॉडल fallback के माध्यम से स्थानीय AI CLI चलाएँ। ](</hi/plugins/cli-backend-plugins>) [**Tool Plugin** एजेंट टूल register करें। ](</hi/plugins/tool-plugins>)

## Quickstart

एक required एजेंट टूल register करके न्यूनतम Tool Plugin बनाएँ। यह सबसे छोटा उपयोगी Plugin आकार है और package, manifest, entry point, और local proof दिखाता है।

* ### Package metadata बनाएँ

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {"extensions": ["./index.ts"],"compat": {"pluginApi": ">=2026.3.24-beta.2","minGatewayVersion": "2026.3.24-beta.2"},"build": {"openclawVersion": "2026.3.24-beta.2","pluginSdkVersion": "2026.3.24-beta.2"}}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {"tools": ["my_tool"]},"activation": {"onStartup": true},"configSchema": {"type": "object","additionalProperties": false}}
[/code]

Published external Plugins को runtime entries को built JavaScript files की ओर इंगित करना चाहिए। पूरे entry point contract के लिए [SDK entry points](</hi/plugins/sdk-entrypoints>) देखें।

हर Plugin को manifest चाहिए, भले ही उसमें config न हो। Runtime tools `contracts.tools` में दिखने चाहिए ताकि OpenClaw हर Plugin runtime को eagerly load किए बिना ownership खोज सके। `activation.onStartup` जानबूझकर सेट करें। यह उदाहरण Gateway startup पर शुरू होता है।

Host-trusted Plugin surfaces भी manifest-gated हैं और installed Plugins के लिए explicit enablement की आवश्यकता होती है। अगर कोई installed Plugin `api.registerAgentToolResultMiddleware(...)` register करता है, तो `contracts.agentToolResultMiddleware` में प्रत्येक target runtime declare करें। अगर वह `api.registerTrustedToolPolicy(...)` register करता है, तो `contracts.trustedToolPolicies` में प्रत्येक policy id declare करें। ये declarations install-time inspection और runtime registration को aligned रखते हैं।

हर manifest field के लिए, [Plugin manifest](</hi/plugins/manifest>) देखें।

* ### Tool register करें

index.tsCopy code
[code]
    import { Type } from "typebox";import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Echo one input value",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return {          content: [{ type: "text", text: `Got: ${params.input}` }],        };      },    });  },});
[/code]

Non-channel Plugins के लिए `definePluginEntry` उपयोग करें। Channel Plugins `defineChannelPluginEntry` उपयोग करते हैं।

* ### Runtime test करें

Installed या external Plugin के लिए, loaded runtime inspect करें:

bashCopy code
[code]
    openclaw plugins inspect my-plugin --runtime --json
[/code]

अगर Plugin कोई CLI command register करता है, तो वह command भी चलाएँ। उदाहरण के लिए, demo command के पास `openclaw demo-plugin ping` जैसा execution proof होना चाहिए।

इस repository में bundled Plugin के लिए, OpenClaw `extensions/*` workspace से source-checkout Plugin packages खोजता है। सबसे निकट targeted test चलाएँ:

bashCopy code
[code]
    pnpm test -- extensions/my-plugin/pnpm check
[/code]

* ### Publish करें

प्रकाशित करने से पहले package validate करें:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-plugin
[/code]

Canonical ClawHub snippets `docs/snippets/plugin-publish/` में रहते हैं।

* ### Install करें

Published package को ClawHub के माध्यम से install करें:

bashCopy code
[code]
    openclaw plugins install clawhub:your-org/your-plugin
[/code]

## Tools register करना

Tools required या optional हो सकते हैं। Required tools हमेशा उपलब्ध रहते हैं जब Plugin enabled होता है। Optional tools को user opt-in की आवश्यकता होती है।

typescriptCopy code
[code]
    register(api) {  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

`api.registerTool(...)` के साथ register किए गए हर tool को Plugin manifest में भी declare किया जाना चाहिए:

jsonCopy code
[code]
    {  "contracts": {    "tools": ["workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

Users `tools.allow` के साथ opt in करते हैं:

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] }, // or ["my-plugin"] for all tools from one plugin}
[/code]

Optional tools नियंत्रित करते हैं कि tool model के सामने expose होता है या नहीं। जब कोई tool या hook model द्वारा चुने जाने के बाद और action चलने से पहले approval माँगना चाहिए, तो [Plugin permission requests](</hi/plugins/plugin-permission-requests>) उपयोग करें।

Side effects, असामान्य binaries, या default रूप से expose न की जाने वाली capabilities के लिए optional tools उपयोग करें। Tool names core tools से conflict नहीं करने चाहिए; conflicts skip किए जाते हैं और Plugin diagnostics में reported होते हैं। Malformed registrations, जिनमें `parameters` के बिना tool descriptors भी शामिल हैं, skip किए जाते हैं और उसी तरह reported होते हैं। Registered tools typed functions हैं जिन्हें model policy और allowlist checks pass होने के बाद call कर सकता है।

Tool factories को runtime-supplied context object मिलता है। जब किसी tool को current turn के active model के अनुसार log, display, या adapt करना हो, तो `ctx.activeModel` उपयोग करें। Object में `provider`, `modelId`, और `modelRef` शामिल हो सकते हैं। इसे informational runtime metadata मानें, local operator, installed Plugin code, या modified OpenClaw runtime के विरुद्ध security boundary नहीं। Sensitive local tools को अब भी explicit Plugin या operator opt-in की आवश्यकता होनी चाहिए और active-model metadata missing या unsuitable होने पर fail closed होना चाहिए।

Manifest ownership और discovery declare करता है; execution फिर भी live registered tool implementation को call करता है। `toolMetadata.<tool>.optional: true` को `api.registerTool(..., { optional: true })` के साथ aligned रखें ताकि OpenClaw tool के explicitly allowlisted होने तक उस Plugin runtime को load करने से बच सके।

## Import conventions

Focused SDK subpaths से import करें:

typescriptCopy code
[code]
      
[/code]

Deprecated root barrel से import न करें:

typescriptCopy code
[code]
     
[/code]

अपने Plugin package के भीतर, internal imports के लिए `api.ts` और `runtime-api.ts` जैसी local barrel files उपयोग करें। SDK path के माध्यम से अपने ही Plugin को import न करें। Provider-specific helpers को provider package में रहना चाहिए जब तक seam सच में generic न हो।

Custom Gateway RPC methods एक advanced entry point हैं। उन्हें Plugin-specific prefix पर रखें; `config.*`, `exec.approvals.*`, `operator.admin.*`, `wizard.*`, और `update.*` जैसे core admin namespaces reserved रहते हैं और `operator.admin` में resolve होते हैं। `openclaw/plugin-sdk/gateway-method-runtime` bridge उन Plugin HTTP routes के लिए reserved है जो `contracts.gatewayMethodDispatch: ["authenticated-request"]` declare करते हैं।

पूरे import map के लिए, [Plugin SDK overview](</hi/plugins/sdk-overview>) देखें।

## Pre-submission checklist

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **package.json** में सही `openclaw` metadata है OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **openclaw.plugin.json** manifest मौजूद और valid है OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Entry point `defineChannelPluginEntry` या `definePluginEntry` उपयोग करता है OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s सभी imports focused `plugin-sdk/<subpath>` paths उपयोग करते हैं OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo

Open issue