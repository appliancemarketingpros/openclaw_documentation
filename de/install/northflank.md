---
title: Northflank
source_url: https://docs.openclaw.ai/de/install/northflank
scraped_at: 2026-05-25
---

# Northflank

Stellen Sie OpenClaw auf Northflank mit einer One-Click-Vorlage bereit und greifen Sie über die webbasierte Control UI darauf zu. Dies ist der einfachste Weg „ohne Terminal auf dem Server“: Northflank führt das Gateway für Sie aus.

## Erste Schritte

  1. Klicken Sie auf [Deploy OpenClaw](<https://northflank.com/stacks/deploy-openclaw>), um die Vorlage zu öffnen.
  2. Erstellen Sie ein [Konto bei Northflank](<https://app.northflank.com/signup>), falls Sie noch keines haben.
  3. Klicken Sie auf **Deploy OpenClaw now**.
  4. Setzen Sie die erforderliche Umgebungsvariable: `OPENCLAW_GATEWAY_TOKEN` (verwenden Sie einen starken Zufallswert).
  5. Klicken Sie auf **Deploy stack** , um die OpenClaw-Vorlage zu bauen und auszuführen.
  6. Warten Sie, bis die Bereitstellung abgeschlossen ist, und klicken Sie dann auf **View resources**.
  7. Öffnen Sie den OpenClaw-Service.
  8. Öffnen Sie die öffentliche OpenClaw-URL unter `/openclaw` und verbinden Sie sich mit dem konfigurierten gemeinsamen Secret. Diese Vorlage verwendet standardmäßig `OPENCLAW_GATEWAY_TOKEN`; wenn Sie es durch Passwortauthentifizierung ersetzen, verwenden Sie stattdessen dieses Passwort.


## Was Sie erhalten

  * Gehostetes OpenClaw Gateway + Control UI
  * Persistenter Speicher über Northflank Volume (`/data`), sodass `openclaw.json`, `auth-profiles.json` pro Agent, Channel-/Provider-Status, Sitzungen und Workspace Neustarts der Bereitstellung überstehen


## Einen Channel verbinden

Verwenden Sie die Control UI unter `/openclaw` oder führen Sie `openclaw onboard` per SSH aus, um Anweisungen zur Channel-Einrichtung zu erhalten:

  * [Telegram](</de/channels/telegram>) (am schnellsten — nur ein Bot-Token)
  * [Discord](</de/channels/discord>)
  * [All channels](</de/channels>)


## Nächste Schritte

  * Messaging-Channels einrichten: [Channels](</de/channels>)
  * Das Gateway konfigurieren: [Gateway configuration](</de/gateway/configuration>)
  * OpenClaw aktuell halten: [Updating](</de/install/updating>)


Was this useful?YesNo