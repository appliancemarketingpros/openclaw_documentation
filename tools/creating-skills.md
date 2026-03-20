---
title: Creating Skills
source_url: https://docs.openclaw.ai/tools/creating-skills
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Skills

Creating Skills

# 

​

Creating Skills

Skills teach the agent how and when to use tools. Each skill is a directory containing a `SKILL.md` file with YAML frontmatter and markdown instructions. For how skills are loaded and prioritized, see [Skills](</tools/skills>).

## 

​

Create your first skill

1

Create the skill directory

Skills live in your workspace. Create a new folder:

Copy
[code]
    mkdir -p ~/.openclaw/workspace/skills/hello-world
    
[/code]

2

Write SKILL.md

Create `SKILL.md` inside that directory. The frontmatter defines metadata, and the markdown body contains instructions for the agent.

Copy
[code]
    ---
    name: hello_world
    description: A simple skill that says hello.
    ---
    
    # Hello World Skill
    
    When the user asks for a greeting, use the `echo` tool to say
    "Hello from your custom skill!".
    
[/code]

3

Add tools (optional)

You can define custom tool schemas in the frontmatter or instruct the agent to use existing system tools (like `exec` or `browser`). Skills can also ship inside plugins alongside the tools they document.

4

Load the skill

Start a new session so OpenClaw picks up the skill:

Copy
[code]
    # From chat
    /new
    
    # Or restart the gateway
    openclaw gateway restart
    
[/code]

Verify the skill loaded:

Copy
[code]
    openclaw skills list
    
[/code]

5

Test it

Send a message that should trigger the skill:

Copy
[code]
    openclaw agent --message "give me a greeting"
    
[/code]

Or just chat with the agent and ask for a greeting.

## 

​

Skill metadata reference

The YAML frontmatter supports these fields:

Field| Required| Description  
---|---|---  
`name`| Yes| Unique identifier (snake_case)  
`description`| Yes| One-line description shown to the agent  
`metadata.openclaw.os`| No| OS filter (`["darwin"]`, `["linux"]`, etc.)  
`metadata.openclaw.requires.bins`| No| Required binaries on PATH  
`metadata.openclaw.requires.config`| No| Required config keys  
  
## 

​

Best practices

  * **Be concise** — instruct the model on _what_ to do, not how to be an AI
  * **Safety first** — if your skill uses `exec`, ensure prompts don’t allow arbitrary command injection from untrusted input
  * **Test locally** — use `openclaw agent --message "..."` to test before sharing
  * **Use ClawHub** — browse and contribute skills at [ClawHub](<https://clawhub.com>)


## 

​

Where skills live

Location| Precedence| Scope  
---|---|---  
`\<workspace\>/skills/`| Highest| Per-agent  
`~/.openclaw/skills/`| Medium| Shared (all agents)  
Bundled (shipped with OpenClaw)| Lowest| Global  
`skills.load.extraDirs`| Lowest| Custom shared folders  
  
## 

​

Related

  * [Skills reference](</tools/skills>) — loading, precedence, and gating rules
  * [Skills config](</tools/skills-config>) — `skills.*` config schema
  * [ClawHub](</tools/clawhub>) — public skill registry
  * [Building Plugins](</plugins/building-plugins>) — plugins can ship skills


[Skills](</tools/skills>)[Skills Config](</tools/skills-config>)

⌘I