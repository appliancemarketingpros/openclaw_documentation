---
title: Webhook
source_url: https://docs.openclaw.ai/hi/cli/webhooks
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw webhooks`

Webhook सहायक और इंटीग्रेशन। आज यह सतह उन Gmail Pub/Sub प्रवाहों तक सीमित है जो bundled `gog` watcher के साथ इंटीग्रेट होते हैं।

## उपकमांड

bashCopy code
[code]
    openclaw webhooks gmail setup --account <email> [...]openclaw webhooks gmail run   [--account <email>] [...]
[/code]

उपकमांड | विवरण  
---|---  
`gmail setup` | Gmail watch, Pub/Sub topic/subscription, और OpenClaw webhook डिलीवरी लक्ष्य कॉन्फ़िगर करें।  
`gmail run` | `gog watch serve` और watch auto-renew loop चलाएँ।  
  
## `webhooks gmail setup`

Gmail watch, Pub/Sub, और OpenClaw webhook डिलीवरी कॉन्फ़िगर करें।

bashCopy code
[code]
    openclaw webhooks gmail setup --account you@example.comopenclaw webhooks gmail setup --account you@example.com --project my-gcp-project --jsonopenclaw webhooks gmail setup --account you@example.com --hook-url https://gateway.example.com/hooks/gmail
[/code]

### आवश्यक

फ़्लैग | विवरण  
---|---  
`--account <email>` | निगरानी के लिए Gmail खाता।  
  
### Pub/Sub विकल्प

फ़्लैग | डिफ़ॉल्ट | विवरण  
---|---|---  
`--project <id>` | (none) | GCP project id (OAuth client owner)।  
`--topic <name>` | `gog-gmail-watch` | Pub/Sub topic नाम।  
`--subscription <name>` | `gog-gmail-watch-push` | Pub/Sub subscription नाम।  
`--label <label>` | `INBOX` | निगरानी के लिए Gmail label।  
`--push-endpoint <url>` | (none) | स्पष्ट Pub/Sub push endpoint। Tailscale को ओवरराइड करता है।  
  
### OpenClaw डिलीवरी विकल्प

फ़्लैग | डिफ़ॉल्ट | विवरण  
---|---|---  
`--hook-url <url>` | (none) | OpenClaw webhook URL।  
`--hook-token <token>` | (none) | OpenClaw webhook token।  
`--push-token <token>` | (none) | `gog watch serve` को भेजा गया push token।  
  
### `gog watch serve` विकल्प

फ़्लैग | डिफ़ॉल्ट | विवरण  
---|---|---  
`--bind <host>` | `127.0.0.1` | `gog watch serve` bind host।  
`--port <port>` | `8788` | `gog watch serve` port।  
`--path <path>` | `/gmail-pubsub` | `gog watch serve` path।  
`--include-body` | `true` | ईमेल body snippets शामिल करें। अक्षम करने के लिए `--no-include-body` पास करें।  
`--max-bytes <n>` | `20000` | प्रति body snippet अधिकतम bytes।  
`--renew-minutes <n>` | `720` (12h) | हर N मिनट में Gmail watch नवीनीकृत करें।  
  
### Tailscale एक्सपोज़र

फ़्लैग | डिफ़ॉल्ट | विवरण  
---|---|---  
`--tailscale <mode>` | `funnel` | push endpoint को Tailscale के ज़रिए expose करें: `funnel`, `serve`, या `off`।  
`--tailscale-path <path>` | (none) | Tailscale serve/funnel के लिए path।  
`--tailscale-target <t>` | (none) | Tailscale serve/funnel target (port, `host:port`, या URL)।  
  
### आउटपुट

फ़्लैग | विवरण  
---|---  
`--json` | text के बजाय मशीन-पठनीय सारांश प्रिंट करें।  
  
## `webhooks gmail run`

`gog watch serve` और watch auto-renew loop को foreground में चलाएँ।

bashCopy code
[code]
    openclaw webhooks gmail run --account you@example.com
[/code]

`run`, `setup` जैसे ही `gog watch serve`, OpenClaw delivery, Pub/Sub, और Tailscale flags स्वीकार करता है, सिवाय इसके:

  * `--account`, `run` पर **वैकल्पिक** है (यह configured account पर fallback करता है)।
  * `run`, `--project`, `--push-endpoint`, या `--json` स्वीकार **नहीं** करता।
  * `run` flags में built-in defaults नहीं होते; अनुपस्थित values, `setup` द्वारा लिखी गई values पर fallback करती हैं।


श्रेणी | फ़्लैग  
---|---  
Pub/Sub | `--account`, `--topic`, `--subscription`, `--label`  
OpenClaw delivery | `--hook-url`, `--hook-token`, `--push-token`  
`gog watch serve` | `--bind`, `--port`, `--path`, `--include-body`, `--max-bytes`, `--renew-minutes`  
Tailscale | `--tailscale`, `--tailscale-path`, `--tailscale-target`  
  
## एंड-टू-एंड प्रवाह

इन CLI commands के साथ जोड़ी बनने वाले GCP project, OAuth, और gateway-side setup के लिए [Gmail Pub/Sub integration](</hi/automation/cron-jobs#gmail-pubsub-integration>) देखें।

## संबंधित

  * [CLI reference](</hi/cli>)
  * [Webhook automation](</hi/automation/cron-jobs>)
  * [Gmail Pub/Sub](</hi/automation/cron-jobs#gmail-pubsub-integration>)


Was this useful?YesNo

Open issue