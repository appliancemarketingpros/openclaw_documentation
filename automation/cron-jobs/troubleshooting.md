---
title: Automation troubleshooting
source_url: https://docs.openclaw.ai/automation/cron-jobs/troubleshooting
scraped_at: 2026-09-14
---

CapabilitiesAutomation

A command ladder and the common failure shapes for scheduled jobs. Part of the [Automations](</automation/cron-jobs>) guide.

## Troubleshooting

### Command ladder

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw automations statusopenclaw automations listopenclaw automations runs <jobId> --limit 20openclaw system heartbeat lastopenclaw logs --followopenclaw doctor
[/code]

Automations not firing

  * Check the `cron.enabled` config setting and `OPENCLAW_SKIP_CRON` in the Gateway's launch environment. Either can disable automatic runs; clear both disable settings and restart the Gateway to enable scheduling.
  * Confirm the Gateway is running continuously.
  * For `cron` schedules, verify timezone (`--tz`) vs the host timezone.
  * `reason: not-due` in run output means the manual run was checked with `openclaw automations run <jobId> --due` and the job was not due yet.
  * If the job's execution agent cannot be resolved, automatic and manual attempts record a failed task and a skipped run-history entry with the reason. Select an agent with `openclaw automations edit <jobId> --agent <id>`.
  * If a capped job's stored named creator account is unavailable, the run fails before model/tool execution. Job details, run history, and warning logs name the account. Re-add it to the channel configuration, or recreate the automation from the intended account; changing the delivery `--account` does not change creator authority. Legacy jobs without account metadata keep their existing execution policy.

Job fired but no delivery

  * Delivery mode `none` means no runner fallback send is expected. The agent can still send directly with the `message` tool when a chat route is available.
  * Delivery target missing/invalid (`channel`/`to`) means outbound was skipped.
  * For Matrix, copied or legacy jobs with lowercased `delivery.to` room IDs can fail because Matrix room IDs are case-sensitive. Edit the job to the exact `!room:server` or `room:!room:server` value from Matrix.
  * Channel auth errors (`unauthorized`, `Forbidden`) mean delivery was blocked by credentials.
  * When the dispatcher records intentional suppression, job state, run history, and finished events include `deliverySuppressionReason` (`empty`, `silent`, `heartbeat`, or `channel_transform`). This is separate from `lastDeliveryError` / `deliveryError`; required delivery failures also log an error when they happen.
  * If the isolated run returns only the silent token (`NO_REPLY` / `no_reply`), OpenClaw suppresses direct outbound delivery and the fallback queued-summary path, so nothing is posted back to chat.
  * If the agent should message the user itself, check that the job has a usable route (`channel: "last"` with a previous chat, or an explicit channel/target).

Automations or heartbeat appear to prevent /new-style rollover

  * Daily and idle reset freshness is not based on `updatedAt`; see [Session management](</concepts/session#session-lifecycle>).
  * Automation wakeups, heartbeat runs, exec notifications, and gateway bookkeeping may update the session row for routing/status, but they do not extend `sessionStartedAt` or `lastInteractionAt`.
  * For legacy rows created before those fields existed, OpenClaw can recover `sessionStartedAt` from the transcript JSONL session header when the file is still available. Legacy idle rows without `lastInteractionAt` use that recovered start time as their idle baseline.

Timezone gotchas

  * Cron expressions without `--tz` use the gateway host timezone.
  * `at` schedules without timezone are treated as UTC.
  * Heartbeat `activeHours` uses configured timezone resolution.


Was this useful?YesNo

Open issue