---
title: Tool-loop detection
source_url: https://docs.openclaw.ai/tools/loop-detection
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Tools

Tool-loop detection

# 

​

Tool-loop detection

OpenClaw can keep agents from getting stuck in repeated tool-call patterns. The guard is **disabled by default**. Enable it only where needed, because it can block legitimate repeated calls with strict settings.

## 

​

Why this exists

  * Detect repetitive sequences that do not make progress.
  * Detect high-frequency no-result loops (same tool, same inputs, repeated errors).
  * Detect specific repeated-call patterns for known polling tools.


## 

​

Configuration block

Global defaults:

Copy
[code]
    {
      tools: {
        loopDetection: {
          enabled: false,
          historySize: 30,
          warningThreshold: 10,
          criticalThreshold: 20,
          globalCircuitBreakerThreshold: 30,
          detectors: {
            genericRepeat: true,
            knownPollNoProgress: true,
            pingPong: true,
          },
        },
      },
    }
    
[/code]

Per-agent override (optional):

Copy
[code]
    {
      agents: {
        list: [
          {
            id: "safe-runner",
            tools: {
              loopDetection: {
                enabled: true,
                warningThreshold: 8,
                criticalThreshold: 16,
              },
            },
          },
        ],
      },
    }
    
[/code]

### 

​

Field behavior

  * `enabled`: Master switch. `false` means no loop detection is performed.
  * `historySize`: number of recent tool calls kept for analysis.
  * `warningThreshold`: threshold before classifying a pattern as warning-only.
  * `criticalThreshold`: threshold for blocking repetitive loop patterns.
  * `globalCircuitBreakerThreshold`: global no-progress breaker threshold.
  * `detectors.genericRepeat`: detects repeated same-tool + same-params patterns.
  * `detectors.knownPollNoProgress`: detects known polling-like patterns with no state change.
  * `detectors.pingPong`: detects alternating ping-pong patterns.


## 

​

Recommended setup

  * Start with `enabled: true`, defaults unchanged.
  * Keep thresholds ordered as `warningThreshold < criticalThreshold < globalCircuitBreakerThreshold`.
  * If false positives occur:
    * raise `warningThreshold` and/or `criticalThreshold`
    * (optionally) raise `globalCircuitBreakerThreshold`
    * disable only the detector causing issues
    * reduce `historySize` for less strict historical context


## 

​

Logs and expected behavior

When a loop is detected, OpenClaw reports a loop event and blocks or dampens the next tool-cycle depending on severity. This protects users from runaway token spend and lockups while preserving normal tool access.

  * Prefer warning and temporary suppression first.
  * Escalate only when repeated evidence accumulates.


## 

​

Notes

  * `tools.loopDetection` is merged with agent-level overrides.
  * Per-agent config fully overrides or extends global values.
  * If no config exists, guardrails stay off.


[Lobster](</tools/lobster>)[PDF Tool](</tools/pdf>)

⌘I