---
title: Media and attachments
source_url: https://docs.openclaw.ai/help/faq/media-and-attachments
scraped_at: 2026-09-14
---

HelpFAQ

## Media and attachments

My skill generated an image/PDF, but nothing was sent

Outbound attachments from the agent must use structured media fields such as `media`, `mediaUrl`, `path`, or `filePath`. See [OpenClaw assistant setup](</start/openclaw>) and [Agent send](</tools/agent-send>).

bashCopy code
[code]
    openclaw message send --target +15555550123 --message "Here you go" --media /path/to/file.png
[/code]

Also check: the target channel supports outbound media and is not blocked by allowlists; the file is within the provider's size limits (images resize to a max side of 2048px); `tools.fs.workspaceOnly=true` limits local-path sends to workspace, temp/media-store, and sandbox-validated files; `tools.fs.workspaceOnly=false` (default) lets structured local media sends use host-local files the agent can already read, for media plus safe document types (images, audio, video, PDF, Office docs, and validated text documents such as Markdown/MD, TXT, JSON, YAML/YML). This is not a secret scanner - an agent-readable `secret.txt` or `config.json` can be attached when the extension and content validation match. Keep sensitive files outside agent-readable paths, or keep `tools.fs.workspaceOnly=true` for stricter local-path sends.

See [Images](</nodes/images>).

Was this useful?YesNo

Open issue