---
title: Konfigurieren
source_url: https://docs.openclaw.ai/de/cli/configure
scraped_at: 2026-05-25
---

# `openclaw configure`

Interaktive Eingabeaufforderung für gezielte Änderungen an einer bestehenden Einrichtung: Zugangsdaten, Geräte, Agent-Standardwerte, Gateway, Kanäle, Plugins, Skills und Zustandsprüfungen.

Verwenden Sie `openclaw onboard` für den vollständigen geführten ersten Durchlauf, `openclaw setup` nur für die Basiskonfiguration/den Arbeitsbereich und `openclaw channels add`, wenn Sie nur die Einrichtung eines Kanalkontos benötigen.

Wenn configure über eine Provider-Authentifizierungsoption gestartet wird, bevorzugen die Auswahl für Standardmodell und Positivliste automatisch diesen Provider. Bei gekoppelten Providern wie Volcengine und BytePlus gilt dieselbe Präferenz auch für deren Coding-Plan-Varianten (`volcengine-plan/*`, `byteplus-plan/*`). Wenn der Filter für den bevorzugten Provider eine leere Liste ergeben würde, fällt configure stattdessen auf den ungefilterten Katalog zurück, anstatt eine leere Auswahl anzuzeigen.

Für die Websuche können Sie mit `openclaw configure --section web` einen Provider auswählen und dessen Zugangsdaten konfigurieren. Einige Provider zeigen außerdem Provider-spezifische Folgeeingaben an:

  * **Grok** kann eine optionale `x_search`-Einrichtung mit demselben `XAI_API_KEY` anbieten und Sie ein `x_search`-Modell auswählen lassen.
  * **Kimi** kann nach der Moonshot-API-Region (`api.moonshot.ai` vs `api.moonshot.cn`) und dem standardmäßigen Kimi-Websuchmodell fragen.


Verwandt:

  * Referenz zur Gateway-Konfiguration: [Konfiguration](</de/gateway/configuration>)
  * Konfigurations-CLI: [Konfiguration](</de/cli/config>)


## Optionen

  * `--section <section>`: wiederholbarer Abschnittsfilter


Verfügbare Abschnitte:

  * `workspace`
  * `model`
  * `web`
  * `gateway`
  * `daemon`
  * `channels`
  * `plugins`
  * `skills`
  * `health`


Hinweise:

  * Die Auswahl, wo das Gateway ausgeführt wird, aktualisiert immer `gateway.mode`. Sie können „Fortfahren“ auswählen, ohne weitere Abschnitte zu verwenden, wenn das alles ist, was Sie benötigen.
  * Nach lokalen Konfigurationsschreibvorgängen installiert configure ausgewählte herunterladbare Plugins, wenn der gewählte Einrichtungspfad sie erfordert. Die Remote-Gateway-Konfiguration installiert keine lokalen Plugin-Pakete.
  * Kanalorientierte Dienste (Slack/Discord/Matrix/Microsoft Teams) fragen während der Einrichtung nach Positivlisten für Kanäle/Räume. Sie können Namen oder IDs eingeben; der Assistent löst Namen nach Möglichkeit in IDs auf.
  * Wenn Sie den Daemon-Installationsschritt ausführen, die Token-Authentifizierung ein Token erfordert und `gateway.auth.token` von SecretRef verwaltet wird, validiert configure die SecretRef, speichert aber keine aufgelösten Klartext-Tokenwerte in den Umgebungsmetadaten des Supervisor-Dienstes.
  * Wenn die Token-Authentifizierung ein Token erfordert und die konfigurierte Token-SecretRef nicht aufgelöst ist, blockiert configure die Daemon-Installation mit umsetzbaren Hinweisen zur Behebung.
  * Wenn sowohl `gateway.auth.token` als auch `gateway.auth.password` konfiguriert sind und `gateway.auth.mode` nicht gesetzt ist, blockiert configure die Daemon-Installation, bis der Modus explizit gesetzt wird.


## Beispiele

bashCopy code
[code]
    openclaw configureopenclaw configure --section webopenclaw configure --section model --section channelsopenclaw configure --section gateway --section daemon
[/code]

## Verwandt

  * [CLI-Referenz](</de/cli>)
  * [Konfiguration](</de/gateway/configuration>)


Was this useful?YesNo