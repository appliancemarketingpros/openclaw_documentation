---
title: Konwencje symboli zastępczych sekretów
source_url: https://docs.openclaw.ai/pl/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Konwencje symboli zastępczych sekretów

Używaj symboli zastępczych, które są czytelne dla człowieka, ale nie przypominają prawdziwych sekretów.

## Zalecany styl

  * Preferuj opisowe wartości, takie jak `example-openai-key-not-real` lub `example-discord-bot-token`.
  * W fragmentach powłoki preferuj `${OPENAI_API_KEY}` zamiast wbudowanych ciągów przypominających tokeny.
  * Dbaj, aby przykłady były oczywiście fikcyjne i ograniczone do celu (dostawca, kanał, typ uwierzytelniania).


## Unikaj tych wzorców w dokumentacji

  * Dosłownego tekstu nagłówka lub stopki prywatnego klucza PEM.
  * Prefiksów przypominających aktywne dane uwierzytelniające, na przykład `sk-...`, `xoxb-...`, `AKIA...`.
  * Realistycznie wyglądających tokenów bearer skopiowanych z logów środowiska uruchomieniowego.


## Przykład

bashCopy code
[code]
    # Dobrzeexport OPENAI_API_KEY="example-openai-key-not-real" # Lepiej (gdy dokument dotyczy podłączania zmiennych środowiskowych)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue