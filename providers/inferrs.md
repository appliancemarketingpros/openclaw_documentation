---
title: inferrs
source_url: https://docs.openclaw.ai/providers/inferrs
scraped_at: 2026-04-13
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Providers

inferrs

# 

​

inferrs

[inferrs](<https://github.com/ericcurtin/inferrs>) can serve local models behind an OpenAI-compatible `/v1` API. OpenClaw works with `inferrs` through the generic `openai-completions` path. `inferrs` is currently best treated as a custom self-hosted OpenAI-compatible backend, not a dedicated OpenClaw provider plugin.

## 

​

Getting started

1

Start inferrs with a model
[code]
    inferrs serve google/gemma-4-E2B-it \
      --host 127.0.0.1 \
      --port 8080 \
      --device metal
    
[/code]

2

Verify the server is reachable
[code]
    curl http://127.0.0.1:8080/health
    curl http://127.0.0.1:8080/v1/models
    
[/code]

3

Add an OpenClaw provider entry

Add an explicit provider entry and point your default model at it. See the full config example below.

## 

​

Full config example

This example uses Gemma 4 on a local `inferrs` server.
[code] 
    {
      agents: {
        defaults: {
          model: { primary: "inferrs/google/gemma-4-E2B-it" },
          models: {
            "inferrs/google/gemma-4-E2B-it": {
              alias: "Gemma 4 (inferrs)",
            },
          },
        },
      },
      models: {
        mode: "merge",
        providers: {
          inferrs: {
            baseUrl: "http://127.0.0.1:8080/v1",
            apiKey: "inferrs-local",
            api: "openai-completions",
            models: [
              {
                id: "google/gemma-4-E2B-it",
                name: "Gemma 4 E2B (inferrs)",
                reasoning: false,
                input: ["text"],
                cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
                contextWindow: 131072,
                maxTokens: 4096,
                compat: {
                  requiresStringContent: true,
                },
              },
            ],
          },
        },
      },
    }
    
[/code]

## 

​

Advanced

Why requiresStringContent matters

Some `inferrs` Chat Completions routes accept only string `messages[].content`, not structured content-part arrays.

If OpenClaw runs fail with an error like:
[code]
    messages[1].content: invalid type: sequence, expected a string
    
[/code]

set `compat.requiresStringContent: true` in your model entry.
[code]
    compat: {
      requiresStringContent: true
    }
    
[/code]

OpenClaw will flatten pure text content parts into plain strings before sending the request.

Gemma and tool-schema caveat

Some current `inferrs` \+ Gemma combinations accept small direct `/v1/chat/completions` requests but still fail on full OpenClaw agent-runtime turns.If that happens, try this first:
[code]
    compat: {
      requiresStringContent: true,
      supportsTools: false
    }
    
[/code]

That disables OpenClaw’s tool schema surface for the model and can reduce prompt pressure on stricter local backends.If tiny direct requests still work but normal OpenClaw agent turns continue to crash inside `inferrs`, the remaining issue is usually upstream model/server behavior rather than OpenClaw’s transport layer.

Manual smoke test

Once configured, test both layers:
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \
      -H 'content-type: application/json' \
      -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
    
[/code]
[code]
    openclaw infer model run \
      --model inferrs/google/gemma-4-E2B-it \
      --prompt "What is 2 + 2? Reply with one short sentence." \
      --json
    
[/code]

If the first command works but the second fails, check the troubleshooting section below.

Proxy-style behavior

`inferrs` is treated as a proxy-style OpenAI-compatible `/v1` backend, not a native OpenAI endpoint.

  * Native OpenAI-only request shaping does not apply here
  * No `service_tier`, no Responses `store`, no prompt-cache hints, and no OpenAI reasoning-compat payload shaping
  * Hidden OpenClaw attribution headers (`originator`, `version`, `User-Agent`) are not injected on custom `inferrs` base URLs


## 

​

Troubleshooting

curl /v1/models fails

`inferrs` is not running, not reachable, or not bound to the expected host/port. Make sure the server is started and listening on the address you configured.

messages[].content expected a string

Set `compat.requiresStringContent: true` in the model entry. See the `requiresStringContent` section above for details.

Direct /v1/chat/completions calls pass but openclaw infer model run fails

Try setting `compat.supportsTools: false` to disable the tool schema surface. See the Gemma tool-schema caveat above.

inferrs still crashes on larger agent turns

If OpenClaw no longer gets schema errors but `inferrs` still crashes on larger agent turns, treat it as an upstream `inferrs` or model limitation. Reduce prompt pressure or switch to a different local backend or model.

For general help, see [Troubleshooting](</help/troubleshooting>) and [FAQ](</help/faq>).

## 

​

See also

## Local models

Running OpenClaw against local model servers.

## Gateway troubleshooting

Debugging local OpenAI-compatible backends that pass probes but fail agent runs.

## Model providers

Overview of all providers, model refs, and failover behavior.

[Hugging Face (Inference)](</providers/huggingface>)[Kilocode](</providers/kilocode>)

⌘I