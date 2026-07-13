---
title: LongCat
source_url: https://docs.openclaw.ai/de/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>) stellt eine gehostete API für LongCat-2.0 bereit, ein Reasoning-Modell für Coding- und agentische Workloads. OpenClaw stellt das offizielle `longcat`-Plugin für den OpenAI-kompatiblen Endpunkt von LongCat bereit.

Eigenschaft | Wert  
---|---  
Provider | `longcat`  
Auth | `LONGCAT_API_KEY`  
API | OpenAI-kompatible Chat Completions  
Basis-URL | `https://api.longcat.chat/openai`  
Modell | `longcat/LongCat-2.0`  
Kontext | 1,048,576 Token  
Max. Ausgabe | 131,072 Token  
Eingabe | Text  
  
## Plugin installieren

Installieren Sie das offizielle Paket und starten Sie anschließend den Gateway neu:

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## Erste Schritte

* ### API-Schlüssel erstellen

Melden Sie sich bei der [LongCat API Platform](<https://longcat.chat/platform/>) an und erstellen Sie auf der Seite [API Keys](<https://longcat.chat/platform/api_keys>) einen Schlüssel.

* ### Onboarding ausführen

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### Modell überprüfen

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

Das Onboarding fügt den gehosteten Katalog hinzu und wählt `longcat/LongCat-2.0` aus, wenn noch kein primäres Modell konfiguriert ist.

### Nicht interaktive Einrichtung

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## Reasoning-Verhalten

LongCat bietet eine binäre Steuerung des Denkprozesses. OpenClaw ordnet aktivierte Denkstufen `thinking: { type: "enabled" }` und `/think off` `thinking: { type: "disabled" }` zu. LongCat dokumentiert derzeit `reasoning_effort` nicht, daher sendet OpenClaw diesen Wert nicht.

LongCat gibt Reasoning in `reasoning_content` zurück. OpenClaw behält dieses Feld bei der Wiedergabe von Assistant-Tool-Call-Turns bei, damit agentische Sitzungen mit mehreren Turns die vom Provider erwartete Nachrichtenstruktur beibehalten.

## Preise

Der integrierte Katalog verwendet die nutzungsabhängigen Listenpreise von LongCat in USD pro Million Token: $0.75 für nicht zwischengespeicherte Eingaben, $0.015 für zwischengespeicherte Eingaben und $2.95 für Ausgaben. LongCat kann vorübergehende Rabatte anbieten; maßgeblich sind die [Preisseite](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) und Ihre Abrechnungsunterlagen.

## Selbst gehostetes LongCat-2.0

Der `longcat`-Provider ist auf die gehostete API von LongCat ausgerichtet. Um die offenen Gewichte auf [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>) zu verwenden, stellen Sie das Modell über eine OpenAI-kompatible Runtime bereit und verwenden Sie stattdessen den bestehenden [vLLM](</de/providers/vllm>)\- oder [SGLang](</de/providers/sglang>)-Provider von OpenClaw.

Behalten Sie die exakte Modellkennung der Runtime im Katalog des selbst gehosteten Providers bei; leiten Sie eine lokale Bereitstellung nicht über `longcat/LongCat-2.0`.

## Fehlerbehebung

Der Schlüssel funktioniert in einer Shell, aber nicht im Gateway

Von einem Daemon verwaltete Gateway-Prozesse übernehmen nicht jede Variable der interaktiven Shell. Hinterlegen Sie `LONGCAT_API_KEY` in `~/.openclaw/.env`, konfigurieren Sie ihn über das Onboarding oder verwenden Sie eine genehmigte Secret-Referenz.

Anfragen schlagen mit 402 oder 429 fehl

`402` bedeutet, dass das Konto nicht über ein ausreichendes Token-Kontingent verfügt. `429` bedeutet, dass der API- Schlüssel ein Ratenlimit erreicht hat. Prüfen Sie die [LongCat-Nutzung](<https://longcat.chat/platform/usage>) und versuchen Sie ratenbegrenzte Anfragen nach Ablauf des Backoff-Zeitfensters des Providers erneut.

Das Modell wird nicht angezeigt

Führen Sie `openclaw plugins list` aus und bestätigen Sie, dass das `longcat`-Plugin aktiviert ist. Führen Sie anschließend `openclaw models list --provider longcat` aus.

## Verwandte Themen

[**Modell-Provider** Provider-Konfiguration, Modellreferenzen und Failover-Verhalten. ](</de/concepts/model-providers>) [**LongCat-API-Dokumentation** Gehostete API-Endpunkte, Authentifizierung, Beschränkungen und Beispiele. ](<https://longcat.chat/platform/docs/>) [**LongCat-2.0-Modellkarte** Architektur, Bereitstellungshinweise und Modelldetails. ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**Secrets** Speichern Sie Provider-Anmeldedaten, ohne Klartext in die Konfiguration einzubetten. ](</de/gateway/secrets>)

Was this useful?YesNo

Open issue