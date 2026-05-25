---
title: Script
source_url: https://docs.openclaw.ai/it/help/scripts
scraped_at: 2026-05-25
---

La directory `scripts/` contiene script di supporto per workflow locali e attività operative. Usali quando un'attività è chiaramente legata a uno script; altrimenti preferisci la CLI.

## Convenzioni

  * Gli script sono **facoltativi** salvo quando citati nella documentazione o nelle checklist di rilascio.
  * Preferisci le superfici CLI quando esistono (esempio: il monitoraggio dell'autenticazione usa `openclaw models status --check`).
  * Considera gli script specifici dell'host; leggili prima di eseguirli su una nuova macchina.


## Script di monitoraggio dell'autenticazione

Il monitoraggio dell'autenticazione è trattato in [Autenticazione](</it/gateway/authentication>). Gli script in `scripts/` sono extra facoltativi per workflow su telefono systemd/Termux.

## Helper di lettura GitHub

Usa `scripts/gh-read` quando vuoi che `gh` usi un token di installazione di GitHub App per chiamate di lettura con ambito repository, lasciando il normale `gh` sul tuo login personale per le azioni di scrittura.

Env richieste:

  * `OPENCLAW_GH_READ_APP_ID`
  * `OPENCLAW_GH_READ_PRIVATE_KEY_FILE`


Env facoltative:

  * `OPENCLAW_GH_READ_INSTALLATION_ID` quando vuoi saltare la ricerca dell'installazione basata sul repository
  * `OPENCLAW_GH_READ_PERMISSIONS` come override separato da virgole per il sottoinsieme di permessi di lettura da richiedere


Ordine di risoluzione del repository:

  * `gh ... -R owner/repo`
  * `GH_REPO`
  * `git remote origin`


Esempi:

  * `scripts/gh-read pr view 123`
  * `scripts/gh-read run list -R openclaw/openclaw`
  * `scripts/gh-read api repos/openclaw/openclaw/pulls/123`


## Quando si aggiungono script

  * Mantieni gli script focalizzati e documentati.
  * Aggiungi una breve voce nella documentazione pertinente (o creane una se manca).


## Correlati

  * [Testing](</it/help/testing>)
  * [Testing live](</it/help/testing-live>)


Was this useful?YesNo