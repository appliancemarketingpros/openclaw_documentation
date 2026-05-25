---
title: Blocco del Gateway
source_url: https://docs.openclaw.ai/it/gateway/gateway-lock
scraped_at: 2026-05-25
---

## Perché

  * Assicurare che venga eseguita una sola istanza del Gateway per porta di base sullo stesso host; i Gateway aggiuntivi devono usare profili isolati e porte univoche.
  * Sopravvivere a crash/SIGKILL senza lasciare file di blocco obsoleti.
  * Fallire rapidamente con un errore chiaro quando la porta di controllo è già occupata.


## Meccanismo

  * Il Gateway acquisisce prima un file di blocco per configurazione nella directory dei blocchi di stato e verifica la porta configurata alla ricerca di un listener esistente.
  * Se il proprietario del blocco registrato non esiste più, la porta è libera o il blocco è obsoleto, l’avvio recupera il blocco e continua.
  * Il Gateway associa quindi il listener HTTP/WebSocket (predefinito `ws://127.0.0.1:18789`) usando un listener TCP esclusivo.
  * Se il binding fallisce con `EADDRINUSE`, l’avvio genera `GatewayLockError("another gateway instance is already listening on ws://127.0.0.1:<port>")`.
  * All’arresto, il Gateway chiude il server HTTP/WebSocket e rimuove il file di blocco.


## Superficie di errore

  * Se un altro processo mantiene la porta, l’avvio genera `GatewayLockError("another gateway instance is already listening on ws://127.0.0.1:<port>")`.
  * Gli altri errori di binding emergono come `GatewayLockError("failed to bind gateway socket on ws://127.0.0.1:<port>: …")`.


## Note operative

  * Se la porta è occupata da _un altro_ processo, l’errore è lo stesso; libera la porta o scegline un’altra con `openclaw gateway --port <port>`.
  * Sotto un supervisore di servizio, un nuovo processo Gateway che vede un risponditore `/healthz` integro esistente lascia il controllo a quel processo. Su systemd, lo starter duplicato esce con codice 78, così il valore predefinito `RestartPreventExitStatus=78` impedisce a `Restart=always` di entrare in loop su un conflitto di blocco o `EADDRINUSE`. Se il processo esistente non diventa mai integro, i tentativi sono limitati e l’avvio fallisce con un errore di blocco chiaro invece di ciclare all’infinito.
  * L’app macOS mantiene ancora la propria guardia PID leggera prima di avviare il Gateway; il blocco runtime è imposto dal file di blocco più il binding HTTP/WebSocket.


## Correlati

  * [Gateway multipli](</it/gateway/multiple-gateways>) — esecuzione di più istanze con porte univoche
  * [Risoluzione dei problemi](</it/gateway/troubleshooting>) — diagnosi di `EADDRINUSE` e dei conflitti di porta


Was this useful?YesNo