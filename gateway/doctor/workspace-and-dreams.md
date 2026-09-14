---
title: Workspace tips and Dreams UI actions
source_url: https://docs.openclaw.ai/gateway/doctor/workspace-and-dreams
scraped_at: 2026-09-14
---

Gateway & OpsGateway

Checks 18-20 close a doctor run. The Control UI Dreams actions are documented here too because they use doctor-style RPC methods but are not part of the `openclaw doctor` CLI run.

## Checks 18-20

18\. Config write + wizard metadata

Doctor persists any config changes and stamps wizard metadata to record the doctor run.

19\. Workspace tips (backup + memory system)

Doctor suggests a workspace memory system when missing and prints a backup tip if the workspace is not already under git.

See [/concepts/agent-workspace](</concepts/agent-workspace>) for a full guide to workspace structure and git backup (recommended private GitHub or GitLab).

20\. Repointed workspace aliases

If you move a workspace folder and update its symlink, OpenClaw refuses to use the new target until you confirm the move. Incoming messages receive a repair notice instead of remaining stuck in retries.

Run `openclaw doctor --fix` and confirm only if the destination contains the same workspace. Doctor coordinates an owned managed Gateway; stop a foreground or externally managed Gateway through its owner first. For unattended recovery, `openclaw doctor --fix --force --non-interactive` supplies that confirmation; ordinary non-interactive `--fix` does not. Plain `openclaw doctor` reports the problem without transferring records. Keep the workspace paths and configuration unchanged until Doctor finishes.

The repair preserves setup completion, file-verification history, and migration records without changing workspace files. It removes stale path associations so later cleanup of the old location cannot delete the moved workspace's records. Start any Gateway you stopped manually, then send a message to check recovery.

Doctor leaves records untouched if the original folder still exists, the destination is missing or already owns records, another configured workspace still uses the old location, or inspection facts change. Pending or conflicting migration history must be resolved before the move can proceed. Follow the reported recovery instructions; do not delete workspace records to force a merge.

If you intended to switch to a different workspace, restore the original link or configure the intended destination directly. Do not confirm a transfer of the old workspace's history.

## Dreams UI backfill and reset

The Control UI Dreams scene includes **Backfill** , **Reset** , and **Clear Grounded** actions for the grounded dreaming workflow. These use gateway doctor-style RPC methods but are **not** part of `openclaw doctor` CLI repair/migration.

Action | What it does  
---|---  
Backfill | Scans historical `memory/YYYY-MM-DD.md` files in the active workspace, runs the grounded REM diary pass, and writes reversible backfill entries into `DREAMS.md`.  
Reset | Removes only the marked backfill diary entries from `DREAMS.md`.  
Clear Grounded | Removes only staged grounded-only short-term entries from historical replay that have not accumulated live recall or daily support yet.  
  
None of these edit `MEMORY.md`, run full doctor migrations, or stage grounded candidates into the live short-term promotion store on their own. To feed grounded historical replay into the normal deep promotion lane, use the CLI flow instead:

bashCopy code
[code]
    openclaw memory rem-backfill --path ./memory --stage-short-term
[/code]

That stages grounded durable candidates into the short-term dreaming store while `DREAMS.md` stays the review surface.

Was this useful?YesNo

Open issue