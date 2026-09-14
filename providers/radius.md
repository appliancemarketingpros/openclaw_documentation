---
title: Radius
source_url: https://docs.openclaw.ai/providers/radius
scraped_at: 2026-09-14
---

ModelsProviders

[Radius](<https://radius.earendil.com>) is Earendil's model gateway for Pi-compatible clients. The `radius` plugin connects OpenClaw's agent loop to Radius, including streamed responses, reasoning, images on supported models, and tool calls. Radius owns upstream routing, model policies, rewrites, and billing.

## Sign in

Create a Radius account on the [Radius website](<https://radius.earendil.com>), then sign in from OpenClaw:

bashCopy code
[code]
    openclaw models auth login --provider radius --method oauth --set-default
[/code]

OpenClaw displays a pairing code and opens the Radius verification page. Enter the code, choose your organization, and authorize access. This device flow also works on a remote Gateway: open the displayed URL in your local browser. OpenClaw stores the OAuth credentials in its auth profiles and refreshes them automatically. Signing in to Pi separately does not sign OpenClaw in.

You can also select Radius during onboarding:

bashCopy code
[code]
    openclaw onboard --auth-choice radius
[/code]

### Organization API key

Create an API key from your organization's **API keys** page in Radius, then use the interactive prompt:

bashCopy code
[code]
    openclaw models auth login --provider radius --method api-key --set-default
[/code]

For unattended setup, supply `RADIUS_API_KEY` through your environment or secret manager and run:

bashCopy code
[code]
    openclaw onboard --auth-choice radius-api-key
[/code]

Both authentication methods use the selected organization's credits, budgets, and model access. An expired or revoked API key needs replacement; OAuth refresh does not extend an API key's lifetime.

## Choose a model

bashCopy code
[code]
    openclaw models list --provider radius --refreshopenclaw models set radius/balanced
[/code]

OpenClaw discovers the catalog from Radius using your credential. This includes organization models, reasoning capabilities, context limits, and pricing tiers. Sign-in recommends `radius/balanced` when available, otherwise the first model in your organization's catalog. Use a model ID shown by `models list`; available models and virtual routes can change.

Radius uses its native Pi message protocol at `https://radius.pi.dev/v1`. The plugin selects that transport automatically. Do not configure Radius as an OpenAI-compatible `/chat/completions` endpoint.

## Scope and troubleshooting

This plugin provides model access. Radius's optional Pi extension packages, including their `/radius` commands, web search, artifacts, and Google Workspace tools, are separate integrations and are not installed by this plugin. Organization-side routing and rewrite policies still apply to model requests.

If sign-in expires, start it again and enter the new pairing code. If model discovery rejects authentication, sign in again or replace the organization API key. If no models are available, check the organization's model access and budgets in Radius. A broken or truncated response is reported as an error rather than a successful empty reply.

See [Radius documentation](<https://radius.earendil.com/docs>), [Radius models](<https://radius.earendil.com/docs/models>), and [model authentication](</concepts/oauth>).

Was this useful?YesNo

Open issue