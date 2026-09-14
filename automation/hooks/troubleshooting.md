---
title: Hook troubleshooting
source_url: https://docs.openclaw.ai/automation/hooks/troubleshooting
scraped_at: 2026-09-14
---

CapabilitiesAutomation

Diagnosing a hook that is not discovered, not eligible, or not executing. Part of the [Hooks](</automation/hooks>) guide.

## Troubleshooting

### Hook not discovered

Check the report's `workspaceDir` and `managedHooksDir` with `openclaw hooks list --json`. Confirm you are inspecting the intended host, profile, and agent. Each hook needs `HOOK.md` and one supported handler file; a metadata file alone is insufficient. Collection locations inspect immediate children. An explicit extra path or linked root can itself be a hook or pack. For a pack, verify that `openclaw.hooks` lists the intended hook directories directly: nested packs and collections are not followed, and rejected entries do not cause unlisted children to be scanned.

Check duplicate names and containment warnings in Gateway logs. A workspace hook cannot override a bundled or managed hook. For extra directories and linked packs, verify the root layout described under [Hook discovery](</automation/hooks/configuration#hook-discovery>).

### Hook not eligible

bashCopy code
[code]
    openclaw hooks info my-hookopenclaw hooks list --verbose
[/code]

Check `blockedReason`, missing binaries on the Gateway's `PATH`, environment, config paths, and OS. A workspace hook is disabled until explicitly enabled. A hook with no declared events is not loadable. Reports can pass requirements without proving that its module imports successfully.

### Hook not executing

Check `hooks.internal.enabled`, the configured-name selection, and the hook's `hookKey` entry and [reload mode](</gateway/configuration#reload-modes>). A `ready` report does not override the master switch or name selection and does not mean another agent's workspace was loaded.

bashCopy code
[code]
    openclaw logs --follow
[/code]

Look for import/export errors, boundary failures, unknown-event warnings, or `Hook error [<type>:<action>]`. Trigger the exact event again and verify a hook-specific marker or artifact. Ordinary chat text does not trigger `command:new`; `/stop` does not send hook replies; a metadata subscription does not invent a custom trigger.

If the marker appears but the chat reply does not, check the producer and route under [Reply delivery](</automation/hooks/writing-hooks#reply-delivery>), not just enablement. For `session-memory`, allow background writing to finish and inspect the resolved agent workspace rather than assuming the default workspace.

Was this useful?YesNo

Open issue