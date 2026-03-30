---
title: Code Execution
source_url: https://docs.openclaw.ai/tools/code-execution
scraped_at: 2026-03-30
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Tools

Code Execution

# 

​

Code Execution

`code_execution` runs sandboxed remote Python analysis on xAI’s Responses API. This is different from local [`exec`](</tools/exec>):

  * `exec` runs shell commands on your machine or node
  * `code_execution` runs Python in xAI’s remote sandbox

Use `code_execution` for:

  * calculations
  * tabulation
  * quick statistics
  * chart-style analysis
  * analyzing data returned by `x_search` or `web_search`

Do **not** use it when you need local files, your shell, your repo, or paired devices. Use [`exec`](</tools/exec>) for that.

## 

​

Setup

You need an xAI API key. Any of these work:

  * `XAI_API_KEY`
  * `plugins.entries.xai.config.webSearch.apiKey`

Example:
[code] 
    {
      plugins: {
        entries: {
          xai: {
            config: {
              webSearch: {
                apiKey: "xai-...",
              },
              codeExecution: {
                enabled: true,
                model: "grok-4-1-fast",
                maxTurns: 2,
                timeoutSeconds: 30,
              },
            },
          },
        },
      },
    }
    
[/code]

## 

​

How To Use It

Ask naturally and make the analysis intent explicit:
[code] 
    Use code_execution to calculate the 7-day moving average for these numbers: ...
    
[/code]
[code] 
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
    
[/code]
[code] 
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
    
[/code]

The tool takes a single `task` parameter internally, so the agent should send the full analysis request and any inline data in one prompt.

## 

​

Limits

  * This is remote xAI execution, not local process execution.
  * It should be treated as ephemeral analysis, not a persistent notebook.
  * Do not assume access to local files or your workspace.
  * For fresh X data, use [`x_search`](</tools/web#x_search>) first.


## 

​

See Also

  * [Web tools](</tools/web>)
  * [Exec](</tools/exec>)
  * [xAI](</providers/xai>)


[BTW Side Questions](</tools/btw>)[Diffs](</tools/diffs>)

⌘I