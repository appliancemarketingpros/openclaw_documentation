---
title: CLI संलग्न करें
source_url: https://docs.openclaw.ai/hi/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` एक Gateway session से बंधे सख्त अस्थायी MCP config के साथ Claude Code लॉन्च करता है।

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

विकल्प:

  * `--session <key>` grant को Gateway session से बांधता है। डिफ़ॉल्ट मुख्य session है।
  * `--ttl <ms>` मिलीसेकंड में सकारात्मक grant TTL का अनुरोध करता है। Gateway अपनी सीमा लागू करता है।
  * `--bin <path>` Claude Code binary चुनता है। डिफ़ॉल्ट `claude` है।
  * `--print-config` अस्थायी `.mcp.json` लिखता है, launch command और env प्रिंट करता है, और TTL समाप्ति तक grant को live छोड़ता है।


bearer token argv नहीं, बल्कि environment variables के माध्यम से पास किया जाता है। OpenClaw Claude Code को `--strict-mcp-config --mcp-config <path>` के साथ लॉन्च करता है ताकि परिवेशी Claude MCP servers attached session में शामिल न हों। सामान्य launches Claude Code process के exit होने पर grant को revoke कर देते हैं।

यह भी देखें: [Gateway CLI](</hi/cli/gateway>), [MCP CLI](</hi/cli/mcp>), और [ACP CLI](</hi/cli/acp>).

Was this useful?YesNo

Open issue