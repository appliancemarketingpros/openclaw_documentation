---
title: Skill Workshop
source_url: https://docs.openclaw.ai/tools/skill-workshop
scraped_at: 2026-06-01
---

Skill Workshop is OpenClaw's governed path for creating and updating workspace skills.

Agents and operators do not write active `SKILL.md` files directly through this path. They create a **proposal** first. A proposal is a pending draft containing the proposed skill content, target binding, scanner state, hashes, support-file metadata, and rollback metadata. It becomes a live skill only when applied.

Skill Workshop writes workspace skills only. It does not mutate bundled, plugin, ClawHub, extra-root, managed, personal-agent, or system skills.

## How it works

  * **Proposal first:** generated skill content is stored as `PROPOSAL.md`, not `SKILL.md`.
  * **Apply is the only live write:** create, update, and revise do not change active skills.
  * **Workspace scoped:** creates target the workspace `skills/` root. Updates are allowed only for writable workspace skills.
  * **No clobber:** create fails if the target skill already exists.
  * **Hash bound:** update proposals bind to the current target hash and become stale if the live skill changes before apply.
  * **Scanner gated:** apply reruns scanning before writing.
  * **Recoverable:** apply writes rollback metadata before changing live files.
  * **Consistent surfaces:** chat, CLI, and Gateway all call the same Skill Workshop service.


## Lifecycle

textCopy code
[code]
    create/update -> pendingrevise        -> pendingapply         -> appliedreject        -> rejectedquarantine    -> quarantinedtarget change -> stale
[/code]

Only `pending` proposals can be revised, applied, rejected, or quarantined.

## Chat

Ask the agent for the skill you want. The agent calls `skill_workshop` and returns a proposal id.

Create:

textCopy code
[code]
    Make a skill called morning-catchup that runs my Monday inbox routine.
[/code]

Update an existing workspace skill:

textCopy code
[code]
    Update trip-planning to also check seat maps before booking.
[/code]

Iterate on a pending proposal:

textCopy code
[code]
    Show me the morning-catchup proposal.Revise it to also flag anything marked urgent.Apply the morning-catchup proposal.
[/code]

By default, agent-initiated `apply`, `reject`, and `quarantine` show an approval prompt before they run. Set `skills.workshop.approvalPolicy` to `"auto"` to skip the prompt for trusted environments.

## CLI

Create a new skill proposal:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name morning-catchup \  --description "Daily inbox catch-up: triage, archive, surface, draft, plan" \  --proposal ./PROPOSAL.md
[/code]

Create an update proposal for an existing workspace skill:

bashCopy code
[code]
    openclaw skills workshop propose-update trip-planning --proposal ./PROPOSAL.md
[/code]

List and inspect:

bashCopy code
[code]
    openclaw skills workshop listopenclaw skills workshop inspect <proposal-id>
[/code]

Revise before approval:

bashCopy code
[code]
    openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.md
[/code]

Close out the proposal:

bashCopy code
[code]
    openclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Duplicate"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

## Proposal content

While pending, the proposal is stored as `PROPOSAL.md` with proposal-only frontmatter:

markdownCopy code
[code]
    ---name: "morning-catchup"description: "Daily inbox catch-up: triage, archive, surface, draft, plan"status: proposalversion: "v1"date: "2026-05-30T00:00:00.000Z"---
[/code]

On apply, Skill Workshop writes the active `SKILL.md` and removes proposal-only fields: `status`, proposal `version`, and proposal `date`.

## Support files

Use `--proposal-dir` when the proposed skill needs files beside `PROPOSAL.md`:

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name weekly-update \  --description "Friday wrap-up: stats, highlights, next week's top three" \  --proposal-dir ./weekly-update-proposal
[/code]

The directory must contain `PROPOSAL.md`. Support files must be under:

  * `assets/`
  * `examples/`
  * `references/`
  * `scripts/`
  * `templates/`


Skill Workshop scans, hashes, and stores support files with the proposal. They are written beside the live `SKILL.md` only on apply.

Rejected support-file paths include absolute paths, hidden path segments, path traversal, overlapping paths, executable files from proposal directories, non-UTF-8 text, null bytes, and files outside the standard support folders.

## Agent tool

The model uses `skill_workshop`:

textCopy code
[code]
    action: create | update | revise | list | inspect | apply | reject | quarantine
[/code]

Agents must use `skill_workshop` for generated skill work. They must not create or change proposal files through `write`, `edit`, `exec`, shell commands, or direct filesystem operations.

## Approval and autonomy

json5Copy code
[code]
    {  skills: {    workshop: {      autonomous: {        enabled: false,      },      approvalPolicy: "pending",      maxPending: 50,      maxSkillBytes: 40000,    },  },}
[/code]

  * `autonomous.enabled`: allows OpenClaw to create pending proposals from durable conversation signals after successful turns. Default: `false`.
  * `approvalPolicy: "pending"`: requires an approval prompt before agent-initiated `apply`, `reject`, or `quarantine`.
  * `approvalPolicy: "auto"`: skips that approval prompt. The agent must still call the action.
  * `maxPending`: caps pending and quarantined proposals per workspace.
  * `maxSkillBytes`: caps proposal body size. Default: `40000`.


Proposal descriptions are always capped at 160 bytes.

## Gateway methods

textCopy code
[code]
    skills.proposals.listskills.proposals.inspectskills.proposals.createskills.proposals.updateskills.proposals.reviseskills.proposals.applyskills.proposals.rejectskills.proposals.quarantine
[/code]

Read-only methods require `operator.read`. Mutating methods require `operator.admin`.

## Storage

textCopy code
[code]
    &lt;OPENCLAW_STATE_DIR&gt;/skill-workshop/  proposals.json  proposals/<proposal-id>/    proposal.json    PROPOSAL.md    rollback.json    assets/    examples/    references/    scripts/    templates/
[/code]

Default state directory: `~/.openclaw`.

  * `proposal.json`: canonical proposal record.
  * `proposals.json`: fast listing index, rebuildable from proposal folders.
  * `PROPOSAL.md`: pending skill proposal.
  * `rollback.json`: recovery metadata written before apply changes live files.


## Limits

  * Description: 160 bytes.
  * Proposal body: `skills.workshop.maxSkillBytes` (default 40,000).
  * Support files: 64 per proposal.
  * Support file size: 256 KB each, 2 MB total.
  * Pending and quarantined proposals: `skills.workshop.maxPending` per workspace (default 50).


## Troubleshooting

Problem | Resolution  
---|---  
`Skill proposal description is too large` | Shorten `description` to 160 bytes or less.  
`Skill proposal content is too large` | Shorten the proposal body or raise `skills.workshop.maxSkillBytes`.  
`Target skill changed after proposal creation` | Revise the proposal against the current target, or create a new proposal.  
`Proposal scan failed` | Inspect scanner findings, then revise or quarantine the proposal.  
`Support file paths must be under one of...` | Move support files under `assets/`, `examples/`, `references/`, `scripts/`, or `templates/`.  
Proposal does not show in list | Check the selected `--agent` workspace and `OPENCLAW_STATE_DIR`.  
  
## Related

  * [Skills](</tools/skills>) for load order, precedence, and visibility
  * [Creating skills](</tools/creating-skills>) for hand-written `SKILL.md` basics
  * [Skills config](</tools/skills-config>) for the full `skills.workshop` schema
  * [Skills CLI](</cli/skills>) for `openclaw skills` commands


Was this useful?YesNo