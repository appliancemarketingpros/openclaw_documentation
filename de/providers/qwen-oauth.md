---
title: Qwen OAuth / Portal
source_url: https://docs.openclaw.ai/de/providers/qwen-oauth
scraped_at: 2026-06-29
---

ModelsProviders

`qwen-oauth` ist die Qwen Portal-Provider-ID. Sie zielt auf den Qwen Portal-Endpunkt und hält ältere Qwen OAuth-/Portal-Einrichtungen über eine eigene Provider-ID adressierbar.

Verwenden Sie diesen Provider, wenn Sie speziell ein aktuelles Qwen Portal-Token für `https://portal.qwen.ai/v1` haben oder wenn Sie eine ältere Qwen Portal-/ Qwen CLI-Einrichtung migrieren und diese Anmeldedaten vom kanonischen Qwen Cloud-Provider getrennt halten möchten. Für neue Qwen-Benutzer ist er nicht die empfohlene erste Wahl.

Für neue Qwen Cloud-Einrichtungen bevorzugen Sie [Qwen](</de/providers/qwen>) mit dem Standard- ModelStudio-Endpunkt, sofern Sie nicht speziell ein aktuelles Qwen Portal-Token haben.

## Einrichtung

Geben Sie Ihr Portal-Token beim Onboarding an:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-oauth
[/code]

Oder setzen Sie:

bashCopy code
[code]
    export QWEN_API_KEY="<your-qwen-portal-token>" # pragma: allowlist secret
[/code]

## Standardwerte

  * Provider: `qwen-oauth`
  * Aliase: `qwen-portal`, `qwen-cli`
  * Basis-URL: `https://portal.qwen.ai/v1`
  * Umgebungsvariable: `QWEN_API_KEY`
  * API-Stil: OpenAI-kompatibel
  * Standardmodell: `qwen-oauth/qwen3.5-plus`


## Unterschied zu Qwen

OpenClaw hat zwei Provider-IDs für Qwen:

Provider | Endpunktfamilie | Am besten geeignet für  
---|---|---  
`qwen` | Qwen Cloud-/Alibaba DashScope- und Coding Plan-Endpunkte | Neue API-Key-Einrichtungen, Standard-Pay-as-you-go, Coding Plan, multimodale DashScope-Funktionen  
`qwen-oauth` | Qwen Portal-Endpunkt unter `portal.qwen.ai/v1` | Bestehende Qwen Portal-Token und ältere Qwen OAuth-/CLI-Einrichtungen  
  
Beide Provider verwenden OpenAI-kompatible Anfrageformate, sind aber getrennte Authentifizierungs- Oberflächen. Ein für `qwen-oauth` gespeichertes Token sollte nicht als DashScope- oder ModelStudio-Schlüssel behandelt werden, und ein neuer DashScope-Schlüssel sollte stattdessen den kanonischen `qwen`\- Provider verwenden.

## Wann Qwen OAuth / Portal gewählt werden sollte

  * Sie haben bereits ein funktionierendes Qwen Portal-Token.
  * Sie bewahren einen älteren Qwen OAuth- oder Qwen CLI-Workflow, während Sie zum Provider-Modell von OpenClaw wechseln.
  * Sie müssen die Kompatibilität speziell mit dem Qwen Portal-Endpunkt testen.


Wählen Sie [Qwen](</de/providers/qwen>) für neue Einrichtungen, breitere Endpunktauswahl, Standard- ModelStudio, Coding Plan und den vollständigen Qwen-Plugin-Katalog.

## Modelle

Der Qwen-Plugin-Katalog initialisiert den Qwen Portal-Standard:

  * `qwen-oauth/qwen3.5-plus`


Die Verfügbarkeit hängt vom aktuellen Qwen Portal-Konto und Token ab. Wenn Ihr Konto stattdessen ModelStudio-/DashScope-API-Keys verwendet, konfigurieren Sie den kanonischen `qwen`-Provider:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-keyopenclaw models set qwen/qwen3-coder-plus
[/code]

## Migration

Ältere Qwen Portal-OAuth-Profile sind möglicherweise nicht aktualisierbar. Wenn ein Portal-Profil nicht mehr funktioniert, authentifizieren Sie sich erneut mit einem aktuellen Token oder wechseln Sie zum Standard- Qwen-Provider:

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

Standard Global ModelStudio verwendet:

textCopy code
[code]
    https://dashscope-intl.aliyuncs.com/compatible-mode/v1
[/code]

## Fehlerbehebung

  * Fehler beim Aktualisieren von Portal OAuth: Ältere Qwen Portal-OAuth-Profile sind möglicherweise nicht aktualisierbar. Führen Sie das Onboarding mit einem aktuellen Token erneut aus.
  * Fehler durch falschen Endpunkt: Bestätigen Sie, dass die Modellreferenz mit `qwen-oauth/` beginnt, wenn Sie ein Portal-Token verwenden. Verwenden Sie `qwen/`-Referenzen nur für den kanonischen Qwen-Provider.
  * Verwirrung um `QWEN_API_KEY`: Beide Qwen-Seiten erwähnen diese Umgebungsvariable, aber das Onboarding speichert Anmeldedaten unter der ausgewählten Provider-ID. Bevorzugen Sie Onboarding, wenn Sie sowohl `qwen` als auch `qwen-oauth` auf demselben Rechner verfügbar halten.


## Verwandte Themen

  * [Qwen](</de/providers/qwen>)
  * [Alibaba Model Studio](</de/providers/alibaba>)
  * [Modell-Provider](</de/concepts/model-providers>)
  * [Alle Provider](</de/providers>)


Was this useful?YesNo

Open issue