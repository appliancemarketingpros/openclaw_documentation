---
title: Доверенная аутентификация прокси
source_url: https://docs.openclaw.ai/ru/gateway/trusted-proxy-auth
scraped_at: 2026-06-29
---

Gateway & OpsGateway

## Когда использовать

Используйте режим аутентификации `trusted-proxy`, когда:

  * Вы запускаете OpenClaw за **identity-aware прокси** (Pomerium, Caddy + OAuth, nginx + oauth2-proxy, Traefik + forward auth).
  * Ваш прокси обрабатывает всю аутентификацию и передает идентификацию пользователя через заголовки.
  * Вы работаете в Kubernetes или контейнерной среде, где прокси является единственным путем к Gateway.
  * Вы сталкиваетесь с ошибками WebSocket `1008 unauthorized`, потому что браузеры не могут передавать токены в полезной нагрузке WS.


## Когда НЕ использовать

  * Если ваш прокси не аутентифицирует пользователей (только TLS-терминатор или балансировщик нагрузки).
  * Если есть любой путь к Gateway в обход прокси (дыры в файрволе, доступ из внутренней сети).
  * Если вы не уверены, что ваш прокси корректно удаляет/перезаписывает переданные заголовки.
  * Если вам нужен только личный однопользовательский доступ (рассмотрите Tailscale Serve + loopback для более простой настройки).


## Как это работает

* ### Прокси аутентифицирует пользователя

Ваш обратный прокси аутентифицирует пользователей (OAuth, OIDC, SAML и т. д.).

* ### Прокси добавляет заголовок идентификации

Прокси добавляет заголовок с идентификацией аутентифицированного пользователя (например, `x-forwarded-user: nick@example.com`).

* ### Gateway проверяет доверенный источник

OpenClaw проверяет, что запрос пришел с **доверенного IP прокси** (настроенного в `gateway.trustedProxies`).

* ### Gateway извлекает идентификацию

OpenClaw извлекает идентификацию пользователя из настроенного заголовка.

* ### Авторизация

Если все проверки проходят успешно, запрос авторизуется.

## Поведение сопряжения Control UI

Когда `gateway.auth.mode = "trusted-proxy"` активен и запрос проходит проверки trusted-proxy, WebSocket-сеансы Control UI могут подключаться без идентификации сопряженного устройства.

Последствия для области действия:

  * WebSocket-сеансы Control UI без устройства подключаются, но по умолчанию не получают операторских областей действия. OpenClaw очищает запрошенный список областей действия до `[]`, чтобы сеанс, не привязанный к одобренному сопряженному устройству/токену, не мог самостоятельно объявлять разрешения.
  * Если методы завершаются ошибкой `missing scope` после успешного подключения WebSocket, используйте HTTPS, чтобы браузер мог сгенерировать идентификацию устройства и завершить сопряжение. См. [небезопасный HTTP Control UI](</ru/web/control-ui#insecure-http>).
  * Только для аварийного доступа: `gateway.controlUi.dangerouslyDisableDeviceAuth=true` сохраняет запрошенные области действия даже без идентификации устройства. Это серьезное снижение уровня безопасности; быстро отмените его. См. [небезопасный HTTP Control UI](</ru/web/control-ui#insecure-http>).


Ограничение областей действия обратным прокси:

  * Если ваш прокси отправляет `x-openclaw-scopes` в запросе обновления WebSocket Control UI, OpenClaw ограничивает области действия сеанса пересечением запрошенных областей действия и объявленных областей действия. Этот заголовок не выдает области действия; он только сужает то, чем может обладать сеанс.


Последствия:

  * Сопряжение больше не является основным шлюзом для доступа к Control UI в этом режиме.
  * Политика аутентификации вашего обратного прокси и `allowUsers` становятся фактическим контролем доступа.
  * Держите входящий доступ к gateway закрытым только для IP доверенных прокси (`gateway.trustedProxies` \+ файрвол).


Пользовательские WebSocket-клиенты не являются сеансами Control UI. `gateway.controlUi.dangerouslyDisableDeviceAuth` не выдает области действия произвольным клиентам с `client.mode: "backend"` или клиентам, похожим на CLI. Пользовательская автоматизация должна использовать идентификацию/сопряжение устройства, зарезервированный прямой локальный вспомогательный backend-путь `client.id: "gateway-client"` или [Plugin admin HTTP RPC](</ru/plugins/admin-http-rpc>), когда поверхность HTTP-запрос/ответ подходит лучше.

## Конфигурация

json5Copy code
[code]
    {  gateway: {    // Trusted-proxy auth expects requests from a non-loopback trusted proxy source by default    bind: "lan",     // CRITICAL: Only add your proxy's IP(s) here    trustedProxies: ["10.0.0.1", "172.17.0.1"],     auth: {      mode: "trusted-proxy",      trustedProxy: {        // Header containing authenticated user identity (required)        userHeader: "x-forwarded-user",         // Optional: headers that MUST be present (proxy verification)        requiredHeaders: ["x-forwarded-proto", "x-forwarded-host"],         // Optional: restrict to specific users (empty = allow all)        allowUsers: ["nick@example.com", "admin@company.org"],         // Optional: allow a same-host loopback proxy after explicit opt-in        allowLoopback: false,      },    },  },}
[/code]

### Справочник по конфигурации

Массив IP-адресов прокси, которым нужно доверять. Запросы с других IP отклоняются.

Должно быть `"trusted-proxy"`.

Имя заголовка, содержащего идентификацию аутентифицированного пользователя.

Дополнительные заголовки, которые должны присутствовать, чтобы запрос считался доверенным.

Список разрешенных идентификаторов пользователей. Пустой список означает разрешить всех аутентифицированных пользователей.

Явное включение поддержки обратных прокси loopback на том же хосте. По умолчанию `false`.

## Терминирование TLS и HSTS

Используйте одну точку терминирования TLS и применяйте HSTS там.

### Терминирование TLS на прокси (рекомендуется)

Когда ваш обратный прокси обрабатывает HTTPS для `https://control.example.com`, задайте `Strict-Transport-Security` на прокси для этого домена.

  * Хорошо подходит для развертываний, доступных из интернета.
  * Держит сертификат и политику усиления HTTP в одном месте.
  * OpenClaw может оставаться на loopback HTTP за прокси.


Пример значения заголовка:

textCopy code
[code]
    Strict-Transport-Security: max-age=31536000; includeSubDomains
[/code]

### Терминирование TLS на Gateway

Если сам OpenClaw напрямую обслуживает HTTPS (без прокси, терминирующего TLS), задайте:

json5Copy code
[code]
    {  gateway: {    tls: { enabled: true },    http: {      securityHeaders: {        strictTransportSecurity: "max-age=31536000; includeSubDomains",      },    },  },}
[/code]

`strictTransportSecurity` принимает строковое значение заголовка или `false` для явного отключения.

### Рекомендации по внедрению

  * Сначала начните с небольшого максимального срока действия (например, `max-age=300`) при проверке трафика.
  * Увеличивайте до долгосрочных значений (например, `max-age=31536000`) только после высокой уверенности.
  * Добавляйте `includeSubDomains` только если каждый поддомен готов к HTTPS.
  * Используйте preload только если вы намеренно выполняете требования preload для всего набора доменов.
  * Локальная разработка только через loopback не получает пользы от HSTS.


## Примеры настройки прокси

Pomerium

Pomerium передает идентификацию в `x-pomerium-claim-email` (или других заголовках claim) и JWT в `x-pomerium-jwt-assertion`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Pomerium's IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-pomerium-claim-email",        requiredHeaders: ["x-pomerium-jwt-assertion"],      },    },  },}
[/code]

Фрагмент конфигурации Pomerium:

yamlCopy code
[code]
    routes:  - from: https://openclaw.example.com    to: http://openclaw-gateway:18789    policy:      - allow:          or:            - email:                is: nick@example.com    pass_identity_headers: true
[/code]

Caddy с OAuth

Caddy с Plugin `caddy-security` может аутентифицировать пользователей и передавать заголовки идентификации.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Caddy/sidecar proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

Фрагмент Caddyfile:

CodeCopy code
[code]
    openclaw.example.com {    authenticate with oauth2_provider    authorize with policy1     reverse_proxy openclaw:18789 {        header_up X-Forwarded-User {http.auth.user.email}    }}
[/code]

nginx + oauth2-proxy

oauth2-proxy аутентифицирует пользователей и передает идентификацию в `x-auth-request-email`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // nginx/oauth2-proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-auth-request-email",      },    },  },}
[/code]

Фрагмент конфигурации nginx:

nginxCopy code
[code]
    location / {    auth_request /oauth2/auth;    auth_request_set $user $upstream_http_x_auth_request_email;     proxy_pass http://openclaw:18789;    proxy_set_header X-Auth-Request-Email $user;    proxy_http_version 1.1;    proxy_set_header Upgrade $http_upgrade;    proxy_set_header Connection "upgrade";}
[/code]

Traefik с forward auth json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["172.17.0.1"], // Traefik container IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

## Смешанная конфигурация токенов

OpenClaw отклоняет неоднозначные конфигурации, где одновременно активны `gateway.auth.token` (или `OPENCLAW_GATEWAY_TOKEN`) и режим `trusted-proxy`. Смешанные конфигурации токенов могут привести к тому, что loopback-запросы будут незаметно аутентифицироваться по неправильному пути аутентификации.

Если вы видите ошибку `mixed_trusted_proxy_token` при запуске:

  * Удалите общий токен при использовании режима trusted-proxy, или
  * Переключите `gateway.auth.mode` на `"token"`, если вы хотите использовать аутентификацию на основе токена.


Заголовки идентификации доверенного прокси для loopback по-прежнему отказывают закрыто: вызывающие стороны с того же хоста не проходят молчаливую аутентификацию как пользователи прокси. Внутренние вызывающие стороны OpenClaw, которые обходят прокси, могут вместо этого аутентифицироваться с помощью `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD`. Резервный переход на токен намеренно не поддерживается в режиме доверенного прокси.

## Заголовок областей оператора

Аутентификация через доверенный прокси — это HTTP-режим, **несущий идентификацию** , поэтому вызывающие стороны могут при необходимости объявлять области оператора с помощью `x-openclaw-scopes` в запросах HTTP API.

Примечание: области WebSocket определяются рукопожатием протокола Gateway и привязкой идентичности устройства. В запросах обновления WebSocket для Control UI `x-openclaw-scopes` является только ограничением согласованных областей сеанса, а не предоставлением доступа. Поведение областей WebSocket с доверенным прокси см. в разделе поведение сопряжения Control UI.

Примеры:

  * `x-openclaw-scopes: operator.read`
  * `x-openclaw-scopes: operator.read,operator.write`
  * `x-openclaw-scopes: operator.admin,operator.write`


Поведение:

  * Когда заголовок присутствует, OpenClaw учитывает объявленный набор областей.
  * Когда заголовок присутствует, но пуст, запрос объявляет **нулевые** области оператора.
  * Когда заголовок отсутствует, обычные HTTP API, несущие идентификацию, возвращаются к стандартному набору областей оператора по умолчанию.
  * **HTTP-маршруты Plugin** с аутентификацией Gateway по умолчанию уже: когда `x-openclaw-scopes` отсутствует, их область выполнения возвращается к `operator.write`.
  * HTTP-запросы из браузерного источника по-прежнему должны проходить `gateway.controlUi.allowedOrigins` (или намеренный резервный режим с заголовком Host) даже после успешной аутентификации через доверенный прокси.
  * Для сеансов WebSocket Control UI `x-openclaw-scopes` является ограничением областей, если присутствует в запросе обновления. Пустое значение не дает областей.


Практическое правило: отправляйте `x-openclaw-scopes` явно, когда нужно, чтобы запрос через доверенный прокси был уже значений по умолчанию, или когда маршруту Plugin с аутентификацией Gateway требуется что-то сильнее области записи.

## Контрольный список безопасности

Перед включением аутентификации через доверенный прокси проверьте:

  * [ ] **Прокси — единственный путь** : порт Gateway защищен файрволом от всего, кроме вашего прокси.
  * [ ] **trustedProxies минимален** : только фактические IP-адреса вашего прокси, а не целые подсети.
  * [ ] **Источник loopback-прокси задан намеренно** : аутентификация через доверенный прокси отказывает закрыто для запросов с loopback-источником, если `gateway.auth.trustedProxy.allowLoopback` явно не включен для прокси на том же хосте.
  * [ ] **Прокси удаляет заголовки** : ваш прокси перезаписывает (а не добавляет) заголовки `x-forwarded-*` от клиентов.
  * [ ] **Завершение TLS** : ваш прокси обрабатывает TLS; пользователи подключаются через HTTPS.
  * [ ] **allowedOrigins задан явно** : Control UI не через loopback использует явный `gateway.controlUi.allowedOrigins`.
  * [ ] **allowUsers задан** (рекомендуется): ограничьте доступ известными пользователями, а не разрешайте любого аутентифицированного.
  * [ ] **Нет смешанной конфигурации токенов** : не задавайте одновременно `gateway.auth.token` и `gateway.auth.mode: "trusted-proxy"`.
  * [ ] **Локальный резервный пароль приватен** : если вы настраиваете `gateway.auth.password` для внутренних прямых вызывающих сторон, держите порт Gateway за файрволом, чтобы удаленные клиенты вне прокси не могли обращаться к нему напрямую.


## Аудит безопасности

`openclaw security audit` пометит аутентификацию через доверенный прокси находкой с **критической** серьезностью. Это намеренно — это напоминание, что вы делегируете безопасность настройке своего прокси.

Аудит проверяет:

  * Базовое предупреждение/критическое напоминание `gateway.trusted_proxy_auth`
  * Отсутствующую конфигурацию `trustedProxies`
  * Отсутствующую конфигурацию `userHeader`
  * Пустой `allowUsers` (разрешает любого аутентифицированного пользователя)
  * Включенный `allowLoopback` для источников прокси на том же хосте
  * Шаблонную или отсутствующую политику браузерных источников на открытых поверхностях Control UI


## Устранение неполадок

trusted_proxy_untrusted_source

Запрос не пришел с IP-адреса из `gateway.trustedProxies`. Проверьте:

  * Правилен ли IP-адрес прокси? (IP-адреса контейнеров Docker могут меняться.)
  * Есть ли балансировщик нагрузки перед вашим прокси?
  * Используйте `docker inspect` или `kubectl get pods -o wide`, чтобы найти фактические IP-адреса.

trusted_proxy_loopback_source

OpenClaw отклонил запрос доверенного прокси с loopback-источником.

Проверьте:

  * Подключается ли прокси с `127.0.0.1` / `::1`?
  * Пытаетесь ли вы использовать аутентификацию через доверенный прокси с loopback reverse proxy на том же хосте?


Исправление:

  * Предпочитайте аутентификацию по токену/паролю для внутренних клиентов на том же хосте, которые не проходят через прокси, или
  * Маршрутизируйте через loopback-адрес доверенного прокси и держите этот IP в `gateway.trustedProxies`, или
  * Для намеренного reverse proxy на том же хосте задайте `gateway.auth.trustedProxy.allowLoopback = true`, оставьте loopback-адрес в `gateway.trustedProxies` и убедитесь, что прокси удаляет или перезаписывает заголовки идентификации.

trusted_proxy_user_missing

Заголовок пользователя был пустым или отсутствовал. Проверьте:

  * Настроен ли ваш прокси на передачу заголовков идентификации?
  * Правильно ли имя заголовка? (регистр не важен, но написание важно)
  * Действительно ли пользователь аутентифицирован на прокси?

trusted_proxy_missing_header_*

Обязательный заголовок отсутствовал. Проверьте:

  * Конфигурацию прокси для этих конкретных заголовков.
  * Не удаляются ли заголовки где-то в цепочке.

trusted_proxy_user_not_allowed

Пользователь аутентифицирован, но отсутствует в `allowUsers`. Либо добавьте его, либо удалите список разрешений.

trusted_proxy_origin_not_allowed

Аутентификация через доверенный прокси прошла успешно, но браузерный заголовок `Origin` не прошел проверки источника Control UI.

Проверьте:

  * `gateway.controlUi.allowedOrigins` включает точный браузерный источник.
  * Вы не полагаетесь на шаблонные источники, если только намеренно не хотите поведение «разрешить всем».
  * Если вы намеренно используете резервный режим с заголовком Host, `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` задан осознанно.

Connection succeeds but methods report missing scope

WebSocket подключается, но `chat.history`, `sessions.list` или `models.list` завершается ошибкой `missing scope: operator.read`.

Частые причины:

  * Сеанс Control UI без устройства: аутентификация через доверенный прокси может допустить подключение WebSocket без идентичности устройства, но OpenClaw по замыслу очищает области в сеансах без устройства.
  * Пользовательский backend-клиент: `gateway.controlUi.dangerouslyDisableDeviceAuth` относится к Control UI и не предоставляет области произвольным backend- или CLI-образным WebSocket-клиентам.
  * Слишком узкий `x-openclaw-scopes`: если ваш прокси внедряет этот заголовок в запрос обновления WebSocket для Control UI, области сеанса ограничиваются этим набором. Пустое значение заголовка не дает областей.


Исправление:

  * Для Control UI используйте HTTPS, чтобы браузер мог создать идентичность устройства и завершить сопряжение.
  * Для пользовательской автоматизации используйте идентичность устройства/сопряжение, зарезервированный прямой локальный вспомогательный backend-путь `gateway-client` или [admin HTTP RPC](</ru/plugins/admin-http-rpc>).
  * Используйте `gateway.controlUi.dangerouslyDisableDeviceAuth: true` только как временный аварийный путь для Control UI.

WebSocket still failing

Убедитесь, что ваш прокси:

  * Поддерживает обновления WebSocket (`Upgrade: websocket`, `Connection: upgrade`).
  * Передает заголовки идентификации в запросах обновления WebSocket (а не только HTTP).
  * Не имеет отдельного пути аутентификации для WebSocket-подключений.


## Миграция с аутентификации по токену

Если вы переходите с аутентификации по токену на доверенный прокси:

* ### Configure the proxy

Настройте прокси для аутентификации пользователей и передачи заголовков.

* ### Test the proxy independently

Протестируйте настройку прокси независимо (`curl` с заголовками).

* ### Update OpenClaw config

Обновите конфигурацию OpenClaw с аутентификацией через доверенный прокси.

* ### Restart the Gateway

Перезапустите Gateway.

* ### Test WebSocket

Протестируйте подключения WebSocket из Control UI.

* ### Audit

Запустите `openclaw security audit` и просмотрите находки.

## Связанные разделы

  * [Конфигурация](</ru/gateway/configuration>) — справочник конфигурации
  * [Удаленный доступ](</ru/gateway/remote>) — другие шаблоны удаленного доступа
  * [Безопасность](</ru/gateway/security>) — полное руководство по безопасности
  * [Tailscale](</ru/gateway/tailscale>) — более простая альтернатива для доступа только через tailnet


Was this useful?YesNo

Open issue