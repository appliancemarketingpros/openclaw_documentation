---
title: Semantica delle credenziali di autenticazione
source_url: https://docs.openclaw.ai/it/auth-credential-semantics
scraped_at: 2026-05-25
---

Questo documento definisce le semantiche canoniche di idoneità e risoluzione delle credenziali usate in:

  * `resolveAuthProfileOrder`
  * `resolveApiKeyForProfile`
  * `models status --probe`
  * `doctor-auth`


L'obiettivo è mantenere allineato il comportamento in fase di selezione e in fase di runtime.

## Codici motivo stabili del probe

  * `ok`
  * `excluded_by_auth_order`
  * `missing_credential`
  * `invalid_expires`
  * `expired`
  * `unresolved_ref`
  * `no_model`


## Credenziali token

Le credenziali token (`type: "token"`) supportano `token` inline e/o `tokenRef`.

### Regole di idoneità

  1. Un profilo token non è idoneo quando sia `token` sia `tokenRef` sono assenti.
  2. `expires` è facoltativo.
  3. Se `expires` è presente, deve essere un numero finito maggiore di `0`.
  4. Se `expires` non è valido (`NaN`, `0`, negativo, non finito o di tipo errato), il profilo non è idoneo con `invalid_expires`.
  5. Se `expires` è nel passato, il profilo non è idoneo con `expired`.
  6. `tokenRef` non aggira la convalida di `expires`.


### Regole di risoluzione

  1. Le semantiche del resolver corrispondono alle semantiche di idoneità per `expires`.
  2. Per i profili idonei, il materiale del token può essere risolto dal valore inline o da `tokenRef`.
  3. I riferimenti non risolvibili producono `unresolved_ref` nell'output di `models status --probe`.


## Portabilità della copia dell'agente

L'ereditarietà dell'autenticazione dell'agente è a lettura trasparente. Quando un agente non ha un profilo locale, può risolvere i profili dall'archivio dell'agente predefinito/principale a runtime senza copiare materiale segreto nel proprio `auth-profiles.json`.

I flussi di copia espliciti, come `openclaw agents add`, usano questa policy di portabilità:

  * I profili `api_key` sono portabili salvo `copyToAgents: false`.
  * I profili `token` sono portabili salvo `copyToAgents: false`.
  * I profili `oauth` non sono portabili per impostazione predefinita perché i token di refresh possono essere monouso o sensibili alla rotazione.
  * I flussi OAuth di proprietà del provider possono aderire con `copyToAgents: true` solo quando è noto che copiare il materiale di refresh tra agenti è sicuro.


I profili non portabili restano disponibili tramite ereditarietà a lettura trasparente salvo che l'agente di destinazione effettui l'accesso separatamente e crei il proprio profilo locale.

## Route di autenticazione solo configurazione

Le voci `auth.profiles` con `mode: "aws-sdk"` sono metadati di routing, non credenziali archiviate. Sono valide quando il provider di destinazione usa `models.providers.<id>.auth: "aws-sdk"` o la route AWS SDK predefinita integrata di Amazon Bedrock. Questi ID profilo possono apparire in `auth.order` e negli override di sessione anche quando non esiste alcuna voce corrispondente in `auth-profiles.json`.

Non scrivere `type: "aws-sdk"` in `auth-profiles.json`. Se un'installazione legacy contiene tale marcatore, `openclaw doctor --fix` lo sposta in `auth.profiles` e rimuove il marcatore dall'archivio delle credenziali.

## Filtro esplicito dell'ordine di autenticazione

  * Quando `auth.order.<provider>` o l'override dell'ordine dell'archivio di autenticazione è impostato per un provider, `models status --probe` esegue il probe solo sugli ID profilo che rimangono nell'ordine di autenticazione risolto per quel provider.
  * Un profilo archiviato per quel provider che viene omesso dall'ordine esplicito non viene provato silenziosamente in seguito. L'output del probe lo segnala con `reasonCode: excluded_by_auth_order` e il dettaglio `Excluded by auth.order for this provider.`


## Risoluzione del target del probe

  * I target del probe possono provenire da profili di autenticazione, credenziali d'ambiente o `models.json`.
  * Se un provider ha credenziali ma OpenClaw non riesce a risolvere un modello candidato sondabile per esso, `models status --probe` segnala `status: no_model` con `reasonCode: no_model`.


## Rilevamento delle credenziali CLI esterne

  * Le credenziali solo runtime di proprietà di CLI esterne vengono rilevate solo quando il provider, il runtime o il profilo di autenticazione rientra nell'ambito dell'operazione corrente, oppure quando esiste già un profilo locale archiviato per quella sorgente esterna.
  * I chiamanti dell'archivio di autenticazione devono scegliere una modalità esplicita di rilevamento della CLI esterna: `none` solo per autenticazione persistita/Plugin, `existing` per aggiornare profili CLI esterni già archiviati, oppure `scoped` per un insieme concreto di provider/profili.
  * I percorsi di sola lettura/stato passano `allowKeychainPrompt: false`; usano solo credenziali CLI esterne basate su file e non leggono né riutilizzano risultati del Portachiavi macOS.


## Guardia della policy OAuth SecretRef

  * L'input SecretRef è riservato alle credenziali statiche.
  * Se una credenziale del profilo è `type: "oauth"`, gli oggetti SecretRef non sono supportati per il materiale delle credenziali di quel profilo.
  * Se `auth.profiles.<id>.mode` è `"oauth"`, l'input `keyRef`/`tokenRef` basato su SecretRef per quel profilo viene rifiutato.
  * Le violazioni sono errori bloccanti nei percorsi di risoluzione dell'autenticazione all'avvio/ricaricamento.


## Messaggistica compatibile con le versioni legacy

Per compatibilità con gli script, gli errori del probe mantengono invariata questa prima riga:

`Auth profile credentials are missing or expired.`

Dettagli orientati agli utenti e codici motivo stabili possono essere aggiunti nelle righe successive.

## Correlati

  * [Gestione dei segreti](</it/gateway/secrets>)
  * [Archiviazione autenticazione](</it/concepts/oauth>)


Was this useful?YesNo