---
title: व्यवस्थापक HTTP RPC Plugin
source_url: https://docs.openclaw.ai/hi/plugins/admin-http-rpc
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

Bundled `admin-http-rpc` Plugin भरोसेमंद host automation के लिए चुनी हुई Gateway control-plane methods को HTTP पर expose करता है, जो सामान्य Gateway WebSocket RPC client का उपयोग नहीं कर सकता।

यह Plugin OpenClaw के साथ शामिल है, लेकिन default रूप से बंद रहता है। Disabled होने पर route registered नहीं होता। Enabled होने पर, यह जोड़ता है:

  * `POST /api/v1/admin/rpc`
  * Gateway जैसा ही listener: `http://<gateway-host>:<port>/api/v1/admin/rpc`


इसे केवल private host tooling, tailnet automation, या trusted internal ingress के लिए enable करें। इस route को सीधे public internet पर expose न करें.

## इसे enable करने से पहले

Admin HTTP RPC एक पूरा operator control-plane surface है। Gateway HTTP auth पास करने वाला कोई भी caller इस page पर allowlisted methods invoke कर सकता है।

इसे तब उपयोग करें जब ये सभी सही हों:

  * caller Gateway operate करने के लिए trusted है।
  * caller WebSocket RPC client का उपयोग नहीं कर सकता।
  * route केवल loopback, tailnet, या private authenticated ingress पर reachable है।
  * आपने allowed methods review कर ली हैं और वे आपकी planned automation से मेल खाती हैं।


OpenClaw clients और interactive tools के लिए WebSocket RPC path उपयोग करें जो Gateway WebSocket connection खुला रख सकते हैं।

## Enable करें

Bundled Plugin enable करें:

### CLI

bashCopy code
[code]
    openclaw plugins enable admin-http-rpcopenclaw gateway restart
[/code]

### Config

json5Copy code
[code]
    {  plugins: {    entries: {      "admin-http-rpc": { enabled: true },    },  },}
[/code]

Route Plugin startup के दौरान registered होता है। Plugin config बदलने के बाद Gateway restart करें।

जब आपको HTTP surface की जरूरत न रहे, तो इसे disable करें:

bashCopy code
[code]
    openclaw plugins disable admin-http-rpcopenclaw gateway restart
[/code]

## Route verify करें

सबसे छोटी safe request के रूप में `health` उपयोग करें:

bashCopy code
[code]
    curl -sS http://<gateway-host>:<port>/api/v1/admin/rpc \  -H 'Authorization: Bearer <gateway-token>' \  -H 'Content-Type: application/json' \  -d '{"method":"health","params":{}}'
[/code]

Successful response में `ok: true` होता है:

jsonCopy code
[code]
    {  "id": "generated-request-id",  "ok": true,  "payload": {    "status": "ok"  }}
[/code]

जब Plugin disabled होता है, route `404` return करता है क्योंकि वह registered नहीं होता।

## Authentication

Plugin route Gateway HTTP auth उपयोग करता है।

सामान्य authentication paths:

  * shared-secret auth (`gateway.auth.mode="token"` या `"password"`): `Authorization: Bearer <token-or-password>`
  * trusted identity-bearing HTTP auth (`gateway.auth.mode="trusted-proxy"`): configured identity-aware proxy के through route करें और उसे required identity headers inject करने दें
  * private-ingress open auth (`gateway.auth.mode="none"`): कोई auth header required नहीं


## Security model

इस Plugin को एक full Gateway operator surface मानें।

  * Plugin enable करना जानबूझकर `/api/v1/admin/rpc` पर allowlisted admin RPC methods की access देता है।
  * Plugin reserved `contracts.gatewayMethodDispatch: ["authenticated-request"]` manifest contract declare करता है, ताकि इसका Gateway-authenticated HTTP route process में control-plane methods dispatch कर सके।
  * Shared-secret bearer auth gateway operator secret के possession को prove करता है।
  * `token` और `password` auth के लिए, narrower `x-openclaw-scopes` headers ignore किए जाते हैं और normal full operator defaults restore किए जाते हैं।
  * Trusted identity-bearing HTTP modes मौजूद होने पर `x-openclaw-scopes` का सम्मान करते हैं।
  * `gateway.auth.mode="none"` का मतलब है कि Plugin enabled होने पर यह route unauthenticated है। इसे केवल ऐसे private ingress के पीछे उपयोग करें जिस पर आप पूरी तरह trust करते हैं।
  * Plugin route auth पास होने के बाद requests WebSocket RPC जैसे ही Gateway method handlers और scope checks के through dispatch होती हैं।
  * इस route को loopback, tailnet, या private trusted ingress पर रखें। इसे सीधे public internet पर expose न करें।
  * Plugin manifest contracts sandbox नहीं हैं। वे reserved SDK helpers के accidental use को रोकते हैं; trusted plugins फिर भी Gateway process में चलते हैं।


जब callers trust boundaries cross करते हैं, अलग gateways उपयोग करें।

## Request

httpCopy code
[code]
    POST /api/v1/admin/rpcAuthorization: Bearer <gateway-token>Content-Type: application/json
[/code]

jsonCopy code
[code]
    {  "id": "optional-request-id",  "method": "health",  "params": {}}
[/code]

Fields:

  * `id` (string, optional): response में copy किया जाता है। Omitted होने पर UUID generated होता है।
  * `method` (string, required): allowed Gateway method name।
  * `params` (any, optional): method-specific params।


Default max request body size 1 MB है।

## Response

Success responses Gateway RPC shape उपयोग करते हैं:

jsonCopy code
[code]
    {  "id": "optional-request-id",  "ok": true,  "payload": {}}
[/code]

Gateway method errors यह उपयोग करते हैं:

jsonCopy code
[code]
    {  "id": "optional-request-id",  "ok": false,  "error": {    "code": "INVALID_REQUEST",    "message": "bad params"  }}
[/code]

HTTP status संभव होने पर Gateway error का अनुसरण करता है। उदाहरण के लिए, `INVALID_REQUEST` `400` return करता है, और `UNAVAILABLE` `503` return करता है।

## Allowed methods

  * discovery: `commands.list` इस Plugin द्वारा allowed HTTP RPC method names return करता है।
  * gateway: `health`, `status`, `logs.tail`, `usage.status`, `usage.cost`, `gateway.restart.request`
  * config: `config.get`, `config.schema`, `config.schema.lookup`, `config.set`, `config.patch`, `config.apply`
  * channels: `channels.status`, `channels.start`, `channels.stop`, `channels.logout`
  * web: `web.login.start`, `web.login.wait`
  * models: `models.list`, `models.authStatus`
  * agents: `agents.list`, `agents.create`, `agents.update`, `agents.delete`
  * approvals: `exec.approvals.get`, `exec.approvals.set`, `exec.approvals.node.get`, `exec.approvals.node.set`
  * cron: `cron.status`, `cron.list`, `cron.get`, `cron.runs`, `cron.add`, `cron.update`, `cron.remove`, `cron.run`
  * devices: `device.pair.list`, `device.pair.approve`, `device.pair.reject`, `device.pair.remove`
  * nodes: `node.list`, `node.describe`, `node.pair.list`, `node.pair.approve`, `node.pair.reject`, `node.pair.remove`, `node.rename`
  * tasks: `tasks.list`, `tasks.get`, `tasks.cancel`
  * diagnostics: `doctor.memory.status`, `update.status`


अन्य Gateway methods तब तक blocked हैं जब तक उन्हें जानबूझकर add नहीं किया जाता।

## WebSocket comparison

सामान्य Gateway WebSocket RPC path OpenClaw clients के लिए preferred control-plane API बना रहता है। Admin HTTP RPC केवल उस host tooling के लिए उपयोग करें जिसे request/response HTTP surface चाहिए।

Trusted device identity के बिना shared-token WebSocket clients connect के दौरान admin scopes self-declare नहीं कर सकते। Admin HTTP RPC जानबूझकर मौजूदा trusted HTTP operator model का अनुसरण करता है: जब Plugin enabled होता है, shared-secret bearer auth को इस admin surface के लिए full operator access माना जाता है।

## Troubleshooting

`404 Not Found`

: Plugin disabled है, Gateway इसे enable करने के बाद restart नहीं हुआ है, या request किसी अलग Gateway process पर जा रही है।

`401 Unauthorized`

: request Gateway HTTP auth satisfy नहीं कर पाई। bearer token या trusted-proxy identity headers check करें।

`400 INVALID_REQUEST`

: request body valid JSON नहीं है, `method` field missing है, या method Plugin allowlist में नहीं है।

`503 UNAVAILABLE`

: Gateway method handler unavailable है। Gateway logs check करें और Gateway startup पूरा होने के बाद retry करें।

## Related

  * [Operator scopes](</hi/gateway/operator-scopes>)
  * [Gateway security](</hi/gateway/security>)
  * [Remote access](</hi/gateway/remote>)
  * [Plugin manifest](</hi/plugins/manifest#contracts>)
  * [SDK subpaths](</hi/plugins/sdk-subpaths>)


Was this useful?YesNo

Open issue