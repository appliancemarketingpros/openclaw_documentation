---
title: Convenzioni per i segnaposto dei segreti
source_url: https://docs.openclaw.ai/it/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Convenzioni per i segnaposto dei segreti

Usa segnaposto leggibili da una persona ma che non assomiglino a segreti reali.

## Stile consigliato

  * Preferisci valori descrittivi come `example-openai-key-not-real` o `example-discord-bot-token`.
  * Per gli snippet shell, preferisci `${OPENAI_API_KEY}` rispetto a stringhe inline che sembrano token.
  * Mantieni gli esempi chiaramente fittizi e circoscritti allo scopo (provider, canale, tipo di autenticazione).


## Evita questi pattern nella documentazione

  * Testo letterale di intestazione o piè di pagina di una chiave privata PEM.
  * Prefissi che assomigliano a credenziali attive, per esempio `sk-...`, `xoxb-...`, `AKIA...`.
  * Bearer token dall'aspetto realistico copiati dai log di runtime.


## Esempio

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue