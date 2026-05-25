---
title: Bloqueio do Gateway
source_url: https://docs.openclaw.ai/pt-BR/gateway/gateway-lock
scraped_at: 2026-05-25
---

## Por quê

  * Garanta que apenas uma instância do Gateway seja executada por porta base no mesmo host; Gateways adicionais devem usar perfis isolados e portas exclusivas.
  * Sobreviva a falhas/SIGKILL sem deixar arquivos de bloqueio obsoletos.
  * Falhe rapidamente com um erro claro quando a porta de controle já estiver ocupada.


## Mecanismo

  * O Gateway primeiro adquire um arquivo de bloqueio por configuração no diretório de bloqueios de estado e verifica a porta configurada em busca de um ouvinte existente.
  * Se o proprietário do bloqueio registrado não existir mais, a porta estiver livre ou o bloqueio estiver obsoleto, a inicialização recupera o bloqueio e continua.
  * Em seguida, o Gateway vincula o ouvinte HTTP/WebSocket (padrão `ws://127.0.0.1:18789`) usando um ouvinte TCP exclusivo.
  * Se a vinculação falhar com `EADDRINUSE`, a inicialização lança `GatewayLockError("another gateway instance is already listening on ws://127.0.0.1:<port>")`.
  * No desligamento, o Gateway fecha o servidor HTTP/WebSocket e remove o arquivo de bloqueio.


## Superfície de erro

  * Se outro processo mantiver a porta, a inicialização lança `GatewayLockError("another gateway instance is already listening on ws://127.0.0.1:<port>")`.
  * Outras falhas de vinculação aparecem como `GatewayLockError("failed to bind gateway socket on ws://127.0.0.1:<port>: …")`.


## Observações operacionais

  * Se a porta estiver ocupada por _outro_ processo, o erro será o mesmo; libere a porta ou escolha outra com `openclaw gateway --port <port>`.
  * Sob um supervisor de serviço, um novo processo do Gateway que encontra um respondedor `/healthz` existente e íntegro deixa esse processo no controle. No systemd, o inicializador duplicado sai com código 78 para que o `RestartPreventExitStatus=78` padrão impeça que `Restart=always` entre em loop em um conflito de bloqueio ou `EADDRINUSE`. Se o processo existente nunca se tornar íntegro, as tentativas são limitadas e a inicialização falha com um erro de bloqueio claro em vez de entrar em loop para sempre.
  * O app para macOS ainda mantém sua própria proteção leve por PID antes de iniciar o Gateway; o bloqueio em tempo de execução é imposto pelo arquivo de bloqueio mais a vinculação HTTP/WebSocket.


## Relacionado

  * [Vários Gateways](</pt-BR/gateway/multiple-gateways>) — executando várias instâncias com portas exclusivas
  * [Solução de problemas](</pt-BR/gateway/troubleshooting>) — diagnosticando `EADDRINUSE` e conflitos de porta


Was this useful?YesNo