---
title: Skills
source_url: https://docs.openclaw.ai/it/cli/skills
scraped_at: 2026-05-25
---

# `openclaw skills`

Ispeziona gli Skills locali e installa/aggiorna Skills da ClawHub.

Correlati:

  * Sistema Skills: [Skills](</it/tools/skills>)
  * Configurazione Skills: [Configurazione Skills](</it/tools/skills-config>)
  * Installazioni ClawHub: [ClawHub](</it/clawhub/cli>)


## Comandi

bashCopy code
[code]
    openclaw skills search "calendar"openclaw skills search --limit 20 --jsonopenclaw skills install <slug>openclaw skills install <slug> --version <version>openclaw skills install <slug> --forceopenclaw skills install <slug> --agent <id>openclaw skills update <slug>openclaw skills update --allopenclaw skills update --all --agent <id>openclaw skills listopenclaw skills list --eligibleopenclaw skills list --jsonopenclaw skills list --verboseopenclaw skills list --agent <id>openclaw skills info <name>openclaw skills info <name> --jsonopenclaw skills info <name> --agent <id>openclaw skills checkopenclaw skills check --agent <id>openclaw skills check --json
[/code]

`search`/`install`/`update` usano direttamente ClawHub e installano nella directory `skills/` del workspace attivo. `list`/`info`/`check` ispezionano ancora gli Skills locali visibili al workspace e alla configurazione correnti. I comandi basati sul workspace risolvono il workspace di destinazione da `--agent <id>`, poi dalla directory di lavoro corrente quando si trova all'interno di un workspace agente configurato, quindi dall'agente predefinito.

Questo comando CLI `install` scarica cartelle di Skills da ClawHub. Le installazioni delle dipendenze degli Skills basate su Gateway, attivate dall'onboarding o dalle impostazioni Skills, usano invece il percorso di richiesta separato `skills.install`.

Note:

  * `search [query...]` accetta una query facoltativa; omettila per sfogliare il feed di ricerca predefinito di ClawHub.
  * `search --limit <n>` limita il numero di risultati restituiti.
  * `install --force` sovrascrive una cartella Skill del workspace esistente per lo stesso slug.
  * `--agent <id>` punta a un singolo workspace agente configurato e sostituisce l'inferenza basata sulla directory di lavoro corrente.
  * `update --all` aggiorna solo le installazioni ClawHub tracciate nel workspace attivo.
  * `check --agent <id>` controlla il workspace dell'agente selezionato e segnala quali Skills pronti sono effettivamente visibili al prompt o alla superficie di comando di quell'agente.
  * `list` è l'azione predefinita quando non viene fornito alcun sottocomando.
  * `list`, `info` e `check` scrivono il loro output renderizzato su stdout. Con `--json`, questo significa che il payload leggibile dalla macchina resta su stdout per pipe e script.


## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Skills](</it/tools/skills>)


Was this useful?YesNo