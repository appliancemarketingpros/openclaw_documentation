---
title: Browser Login
source_url: https://docs.openclaw.ai/tools/browser-login
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Browser

Browser Login

# 

​

Browser login + X/Twitter posting

## 

​

Manual login (recommended)

When a site requires login, **sign in manually** in the **host** browser profile (the openclaw browser). Do **not** give the model your credentials. Automated logins often trigger anti‑bot defenses and can lock the account. Back to the main browser docs: [Browser](</tools/browser>).

## 

​

Which Chrome profile is used?

OpenClaw controls a **dedicated Chrome profile** (named `openclaw`, orange‑tinted UI). This is separate from your daily browser profile. For agent browser tool calls:

  * Default choice: the agent should use its isolated `openclaw` browser.
  * Use `profile="user"` only when existing logged-in sessions matter and the user is at the computer to click/approve any attach prompt.
  * If you have multiple user-browser profiles, specify the profile explicitly instead of guessing.

Two easy ways to access it:

  1. **Ask the agent to open the browser** and then log in yourself.
  2. **Open it via CLI** :


Copy
[code]
    openclaw browser start
    openclaw browser open https://x.com
    
[/code]

If you have multiple profiles, pass `--browser-profile <name>` (the default is `openclaw`).

## 

​

X/Twitter: recommended flow

  * **Read/search/threads:** use the **host** browser (manual login).
  * **Post updates:** use the **host** browser (manual login).


## 

​

Sandboxing + host browser access

Sandboxed browser sessions are **more likely** to trigger bot detection. For X/Twitter (and other strict sites), prefer the **host** browser. If the agent is sandboxed, the browser tool defaults to the sandbox. To allow host control:

Copy
[code]
    {
      agents: {
        defaults: {
          sandbox: {
            mode: "non-main",
            browser: {
              allowHostControl: true,
            },
          },
        },
      },
    }
    
[/code]

Then target the host browser:

Copy
[code]
    openclaw browser open https://x.com --browser-profile openclaw --target host
    
[/code]

Or disable sandboxing for the agent that posts updates.

[Browser (OpenClaw-managed)](</tools/browser>)[Browser Troubleshooting](</tools/browser-linux-troubleshooting>)

⌘I