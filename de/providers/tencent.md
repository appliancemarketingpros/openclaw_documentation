---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/de/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud wird in OpenClaw als gebündeltes Provider-Plugin ausgeliefert. Es bietet Zugriff auf Tencent Hy3 preview über den TokenHub-Endpunkt (`tencent-tokenhub`) mit einer OpenAI-kompatiblen API.

Eigenschaft | Wert  
---|---  
Provider-ID | `tencent-tokenhub`  
Plugin | gebündelt, `enabledByDefault: true`  
Auth-Env-Var | `TOKENHUB_API_KEY`  
Onboarding-Flag | `--auth-choice tokenhub-api-key`  
Direkter CLI-Flag | `--tokenhub-api-key <key>`  
API | OpenAI-kompatibel (`openai-completions`)  
Standard-Basis-URL | `https://tokenhub.tencentmaas.com/v1`  
Globale Basis-URL | `https://tokenhub-intl.tencentmaas.com/v1` (Override)  
Standardmodell | `tencent-tokenhub/hy3-preview`  
  
## Schnellstart

* ### TokenHub-API-Schlüssel erstellen

Erstellen Sie einen API-Schlüssel in Tencent Cloud TokenHub. Wenn Sie für den Schlüssel einen eingeschränkten Zugriffsbereich wählen, nehmen Sie **Hy3 preview** in die zulässigen Modelle auf.

* ### Onboarding ausführen

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Direktes FlagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Nur EnvCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Modell überprüfen

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Nicht interaktive Einrichtung

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Integrierter Katalog

Modellreferenz | Name | Eingabe | Kontext | Maximale Ausgabe | Hinweise  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | Text | 256.000 | 64.000 | Standard; reasoning-fähig  
  
Hy3 preview ist das große MoE-Sprachmodell von Tencent Hunyuan für Reasoning, Befolgen von Anweisungen mit langem Kontext, Code und Agent-Workflows. Die OpenAI-kompatiblen Beispiele von Tencent verwenden `hy3-preview` als Modell-ID und unterstützen standardmäßiges Chat-Completions-Tool-Calling sowie `reasoning_effort`.

## Gestaffelte Preise

Der gebündelte Katalog enthält gestaffelte Kostenmetadaten, die mit der Länge des Eingabefensters skalieren, sodass Kostenschätzungen ohne manuelle Overrides befüllt werden.

Bereich der Eingabe-Token | Eingaberate | Ausgaberate | Cache-Lesezugriff  
---|---|---|---  
0 - 16.000 | 0,176 | 0,587 | 0,059  
16.000 - 32.000 | 0,235 | 0,939 | 0,088  
32.000+ | 0,293 | 1,173 | 0,117  
  
Die Raten gelten pro Million Token in USD, wie von Tencent angegeben. Überschreiben Sie die Preise unter `models.providers.tencent-tokenhub` nur, wenn Sie eine andere Oberfläche benötigen.

## Erweiterte Konfiguration

Endpunkt-Override

OpenClaw verwendet standardmäßig den Tencent-Cloud-Endpunkt `https://tokenhub.tencentmaas.com/v1`. Tencent dokumentiert außerdem einen internationalen TokenHub-Endpunkt:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

Überschreiben Sie den Endpunkt nur, wenn Ihr TokenHub-Konto oder Ihre Region dies erfordert.

Umgebungsverfügbarkeit für den Daemon

Wenn der Gateway als verwalteter Dienst ausgeführt wird (launchd, systemd, Docker), muss `TOKENHUB_API_KEY` für diesen Prozess sichtbar sein. Legen Sie ihn in `~/.openclaw/.env` oder über `env.shellEnv` fest, damit launchd-, systemd- oder Docker-Exec-Umgebungen ihn lesen können.

## Verwandte Themen

[**Modell-Provider** Provider, Modellreferenzen und Failover-Verhalten auswählen. ](</de/concepts/model-providers>) [**Konfigurationsreferenz** Vollständiges Konfigurationsschema einschließlich Provider-Einstellungen. ](</de/gateway/configuration>) [**Tencent TokenHub** Produktseite von Tencent Cloud TokenHub. ](<https://cloud.tencent.com/product/tokenhub>) [**Hy3-preview-Modellkarte** Details und Benchmarks zu Tencent Hunyuan Hy3 preview. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo