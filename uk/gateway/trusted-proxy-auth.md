---
title: Автентифікація через довірений проксі
source_url: https://docs.openclaw.ai/uk/gateway/trusted-proxy-auth
scraped_at: 2026-05-25
---

## Коли використовувати

Використовуйте режим автентифікації `trusted-proxy`, коли:

  * Ви запускаєте OpenClaw за **проксі з урахуванням ідентичності** (Pomerium, Caddy + OAuth, nginx + oauth2-proxy, Traefik + forward auth).
  * Ваш проксі обробляє всю автентифікацію й передає ідентичність користувача через заголовки.
  * Ви працюєте в Kubernetes або контейнерному середовищі, де проксі є єдиним шляхом до Gateway.
  * Ви стикаєтеся з помилками WebSocket `1008 unauthorized`, бо браузери не можуть передавати токени в корисному навантаженні WS.


## Коли НЕ використовувати

  * Якщо ваш проксі не автентифікує користувачів (лише завершує TLS або працює як балансувальник навантаження).
  * Якщо існує будь-який шлях до Gateway в обхід проксі (дірки у firewall, доступ через внутрішню мережу).
  * Якщо ви не впевнені, чи ваш проксі коректно видаляє або перезаписує переслані заголовки.
  * Якщо вам потрібен лише персональний доступ для одного користувача (розгляньте Tailscale Serve + loopback для простішого налаштування).


## Як це працює

* ### Проксі автентифікує користувача

Ваш зворотний проксі автентифікує користувачів (OAuth, OIDC, SAML тощо).

* ### Проксі додає заголовок ідентичності

Проксі додає заголовок з ідентичністю автентифікованого користувача (наприклад, `x-forwarded-user: nick@example.com`).

* ### Gateway перевіряє довірене джерело

OpenClaw перевіряє, що запит надійшов від **довіреної IP-адреси проксі** (налаштованої в `gateway.trustedProxies`).

* ### Gateway витягує ідентичність

OpenClaw витягує ідентичність користувача з налаштованого заголовка.

* ### Авторизація

Якщо всі перевірки успішні, запит авторизується.

## Поведінка сполучення Control UI

Коли активний `gateway.auth.mode = "trusted-proxy"` і запит проходить перевірки trusted-proxy, WebSocket-сеанси Control UI можуть підключатися без ідентичності сполученого пристрою.

Наслідки:

  * Сполучення більше не є основним бар’єром для доступу до Control UI у цьому режимі.
  * Політика автентифікації вашого зворотного проксі та `allowUsers` стають фактичним контролем доступу.
  * Тримайте вхідний доступ до gateway обмеженим лише довіреними IP-адресами проксі (`gateway.trustedProxies` \+ firewall).


## Конфігурація

json5Copy code
[code]
    {  gateway: {    // Trusted-proxy auth expects requests from a non-loopback trusted proxy source by default    bind: "lan",     // CRITICAL: Only add your proxy's IP(s) here    trustedProxies: ["10.0.0.1", "172.17.0.1"],     auth: {      mode: "trusted-proxy",      trustedProxy: {        // Header containing authenticated user identity (required)        userHeader: "x-forwarded-user",         // Optional: headers that MUST be present (proxy verification)        requiredHeaders: ["x-forwarded-proto", "x-forwarded-host"],         // Optional: restrict to specific users (empty = allow all)        allowUsers: ["nick@example.com", "admin@company.org"],         // Optional: allow a same-host loopback proxy after explicit opt-in        allowLoopback: false,      },    },  },}
[/code]

### Довідник конфігурації

Масив IP-адрес проксі, яким слід довіряти. Запити з інших IP-адрес відхиляються.

Має бути `"trusted-proxy"`.

Назва заголовка, що містить ідентичність автентифікованого користувача.

Додаткові заголовки, які мають бути присутніми, щоб запит вважався довіреним.

Список дозволених ідентичностей користувачів. Порожнє значення означає дозволити всіх автентифікованих користувачів.

Явне ввімкнення підтримки зворотних проксі на тому самому хості через loopback. За замовчуванням `false`.

## Завершення TLS і HSTS

Використовуйте одну точку завершення TLS і застосовуйте HSTS там.

### Завершення TLS на проксі (рекомендовано)

Коли ваш зворотний проксі обробляє HTTPS для `https://control.example.com`, установіть `Strict-Transport-Security` на проксі для цього домену.

  * Добре підходить для розгортань, доступних з інтернету.
  * Тримає сертифікат і політику посилення HTTP-безпеки в одному місці.
  * OpenClaw може залишатися на loopback HTTP за проксі.


Приклад значення заголовка:

textCopy code
[code]
    Strict-Transport-Security: max-age=31536000; includeSubDomains
[/code]

### Завершення TLS на Gateway

Якщо OpenClaw сам напряму обслуговує HTTPS (без проксі, що завершує TLS), установіть:

json5Copy code
[code]
    {  gateway: {    tls: { enabled: true },    http: {      securityHeaders: {        strictTransportSecurity: "max-age=31536000; includeSubDomains",      },    },  },}
[/code]

`strictTransportSecurity` приймає рядкове значення заголовка або `false` для явного вимкнення.

### Рекомендації з розгортання

  * Спочатку почніть з короткого максимального віку (наприклад, `max-age=300`), доки перевіряєте трафік.
  * Збільшуйте до довготривалих значень (наприклад, `max-age=31536000`) лише після високої впевненості.
  * Додавайте `includeSubDomains` лише якщо кожен піддомен готовий до HTTPS.
  * Використовуйте preload лише якщо ви навмисно виконуєте вимоги preload для всього набору доменів.
  * Локальна розробка лише через loopback не отримує користі від HSTS.


## Приклади налаштування проксі

Pomerium

Pomerium передає ідентичність у `x-pomerium-claim-email` (або інших заголовках тверджень) і JWT у `x-pomerium-jwt-assertion`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Pomerium's IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-pomerium-claim-email",        requiredHeaders: ["x-pomerium-jwt-assertion"],      },    },  },}
[/code]

Фрагмент конфігурації Pomerium:

yamlCopy code
[code]
    routes:  - from: https://openclaw.example.com    to: http://openclaw-gateway:18789    policy:      - allow:          or:            - email:                is: nick@example.com    pass_identity_headers: true
[/code]

Caddy з OAuth

Caddy з Plugin `caddy-security` може автентифікувати користувачів і передавати заголовки ідентичності.

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

oauth2-proxy автентифікує користувачів і передає ідентичність у `x-auth-request-email`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // nginx/oauth2-proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-auth-request-email",      },    },  },}
[/code]

Фрагмент конфігурації nginx:

nginxCopy code
[code]
    location / {    auth_request /oauth2/auth;    auth_request_set $user $upstream_http_x_auth_request_email;     proxy_pass http://openclaw:18789;    proxy_set_header X-Auth-Request-Email $user;    proxy_http_version 1.1;    proxy_set_header Upgrade $http_upgrade;    proxy_set_header Connection "upgrade";}
[/code]

Traefik з forward auth json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["172.17.0.1"], // Traefik container IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

## Змішана конфігурація токенів

OpenClaw відхиляє неоднозначні конфігурації, у яких одночасно активні `gateway.auth.token` (або `OPENCLAW_GATEWAY_TOKEN`) і режим `trusted-proxy`. Змішані конфігурації токенів можуть призвести до того, що loopback-запити непомітно автентифікуватимуться неправильним шляхом автентифікації.

Якщо під час запуску ви бачите помилку `mixed_trusted_proxy_token`:

  * Видаліть спільний токен під час використання режиму trusted-proxy, або
  * Перемкніть `gateway.auth.mode` на `"token"`, якщо ви плануєте автентифікацію на основі токенів.


Заголовки ідентичності trusted-proxy через loopback усе ще безпечно відмовляють: виклики з того самого хоста не автентифікуються непомітно як користувачі проксі. Внутрішні виклики OpenClaw, що обходять проксі, можуть натомість автентифікуватися за допомогою `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD`. Token fallback навмисно не підтримується в режимі trusted-proxy.

## Заголовок операторських областей дії

Автентифікація trusted-proxy є HTTP-режимом, що несе ідентичність, тому виклики можуть необов’язково оголошувати операторські області дії за допомогою `x-openclaw-scopes`.

Приклади:

  * `x-openclaw-scopes: operator.read`
  * `x-openclaw-scopes: operator.read,operator.write`
  * `x-openclaw-scopes: operator.admin,operator.write`


Поведінка:

  * Коли заголовок присутній, OpenClaw враховує оголошений набір областей дії.
  * Коли заголовок присутній, але порожній, запит оголошує, що **не має** операторських областей дії.
  * Коли заголовок відсутній, звичайні HTTP API, що несуть ідентичність, повертаються до стандартного набору операторських областей дії за замовчуванням.
  * Plugin HTTP-маршрути з gateway-auth за замовчуванням вужчі: коли `x-openclaw-scopes` відсутній, їхня runtime-область дії повертається до `operator.write`.
  * HTTP-запити з браузерного джерела все ще мають пройти `gateway.controlUi.allowedOrigins` (або навмисний режим fallback за заголовком Host), навіть після успішної автентифікації trusted-proxy.


Практичне правило: надсилайте `x-openclaw-scopes` явно, коли хочете, щоб запит trusted-proxy був вужчим за значення за замовчуванням, або коли gateway-auth Plugin-маршруту потрібне щось сильніше за область дії write.

## Контрольний список безпеки

Перед увімкненням автентифікації trusted-proxy перевірте:

  * [ ] **Проксі — єдиний шлях** : Порт Gateway захищено брандмауером від усього, крім вашого проксі.
  * [ ] **trustedProxies мінімальний** : Лише фактичні IP-адреси ваших проксі, а не цілі підмережі.
  * [ ] **Джерело loopback-проксі вибране навмисно** : Автентифікація trusted-proxy закривається з відмовою для запитів із loopback-джерела, якщо `gateway.auth.trustedProxy.allowLoopback` не ввімкнено явно для проксі на тому самому хості.
  * [ ] **Проксі видаляє заголовки** : Ваш проксі перезаписує (а не додає) заголовки `x-forwarded-*` від клієнтів.
  * [ ] **Завершення TLS** : Ваш проксі обробляє TLS; користувачі підключаються через HTTPS.
  * [ ] **allowedOrigins задано явно** : Control UI не з loopback використовує явні `gateway.controlUi.allowedOrigins`.
  * [ ] **allowUsers задано** (рекомендовано): Обмежте доступ відомими користувачами, а не дозволяйте будь-кому автентифікованому.
  * [ ] **Без змішаної конфігурації токенів** : Не задавайте одночасно `gateway.auth.token` і `gateway.auth.mode: "trusted-proxy"`.
  * [ ] **Локальний резервний пароль приватний** : Якщо ви налаштовуєте `gateway.auth.password` для внутрішніх прямих викликачів, тримайте порт Gateway за брандмауером, щоб віддалені клієнти не через проксі не могли підключитися до нього напряму.


## Аудит безпеки

`openclaw security audit` позначатиме автентифікацію trusted-proxy як знахідку з **критичною** серйозністю. Це навмисно — це нагадування, що ви делегуєте безпеку налаштуванню свого проксі.

Аудит перевіряє:

  * Базове попередження/критичне нагадування `gateway.trusted_proxy_auth`
  * Відсутню конфігурацію `trustedProxies`
  * Відсутню конфігурацію `userHeader`
  * Порожній `allowUsers` (дозволяє будь-якого автентифікованого користувача)
  * Увімкнений `allowLoopback` для джерел проксі на тому самому хості
  * Політику походження браузера з wildcard або її відсутність на відкритих поверхнях Control UI


## Усунення несправностей

trusted_proxy_untrusted_source

Запит не надійшов з IP-адреси в `gateway.trustedProxies`. Перевірте:

  * Чи правильна IP-адреса проксі? (IP-адреси контейнерів Docker можуть змінюватися.)
  * Чи є балансувальник навантаження перед вашим проксі?
  * Використайте `docker inspect` або `kubectl get pods -o wide`, щоб знайти фактичні IP-адреси.

trusted_proxy_loopback_source

OpenClaw відхилив запит trusted-proxy з loopback-джерела.

Перевірте:

  * Чи проксі підключається з `127.0.0.1` / `::1`?
  * Чи ви намагаєтеся використовувати автентифікацію trusted-proxy зі зворотним проксі loopback на тому самому хості?


Виправлення:

  * Віддавайте перевагу автентифікації за токеном/паролем для внутрішніх клієнтів на тому самому хості, які не проходять через проксі, або
  * Спрямовуйте трафік через адресу довіреного проксі, що не є loopback, і тримайте цю IP-адресу в `gateway.trustedProxies`, або
  * Для навмисного зворотного проксі на тому самому хості задайте `gateway.auth.trustedProxy.allowLoopback = true`, залиште адресу loopback у `gateway.trustedProxies` і переконайтеся, що проксі видаляє або перезаписує заголовки ідентичності.

trusted_proxy_user_missing

Заголовок користувача був порожній або відсутній. Перевірте:

  * Чи налаштовано ваш проксі передавати заголовки ідентичності?
  * Чи правильна назва заголовка? (регістр не враховується, але написання має значення)
  * Чи користувач справді автентифікований на проксі?

trusted_proxy_missing_header_*

Обов’язкового заголовка не було. Перевірте:

  * Конфігурацію вашого проксі для цих конкретних заголовків.
  * Чи не видаляються заголовки десь у ланцюжку.

trusted_proxy_user_not_allowed

Користувач автентифікований, але його немає в `allowUsers`. Додайте його або видаліть список дозволених.

trusted_proxy_origin_not_allowed

Автентифікація trusted-proxy успішна, але заголовок браузера `Origin` не пройшов перевірки походження Control UI.

Перевірте:

  * `gateway.controlUi.allowedOrigins` містить точне походження браузера.
  * Ви не покладаєтеся на wildcard-походження, якщо тільки навмисно не хочете дозволити все.
  * Якщо ви навмисно використовуєте резервний режим Host-заголовка, `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` задано свідомо.

WebSocket still failing

Переконайтеся, що ваш проксі:

  * Підтримує оновлення WebSocket (`Upgrade: websocket`, `Connection: upgrade`).
  * Передає заголовки ідентичності в запитах оновлення WebSocket (не лише HTTP).
  * Не має окремого шляху автентифікації для підключень WebSocket.


## Міграція з автентифікації за токеном

Якщо ви переходите з автентифікації за токеном на trusted-proxy:

* ### Configure the proxy

Налаштуйте свій проксі для автентифікації користувачів і передавання заголовків.

* ### Test the proxy independently

Протестуйте налаштування проксі окремо (`curl` із заголовками).

* ### Update OpenClaw config

Оновіть конфігурацію OpenClaw для автентифікації trusted-proxy.

* ### Restart the Gateway

Перезапустіть Gateway.

* ### Test WebSocket

Протестуйте підключення WebSocket з Control UI.

* ### Audit

Запустіть `openclaw security audit` і перегляньте знахідки.

## Пов’язане

  * [Конфігурація](</uk/gateway/configuration>) — довідник конфігурації
  * [Віддалений доступ](</uk/gateway/remote>) — інші шаблони віддаленого доступу
  * [Безпека](</uk/gateway/security>) — повний посібник із безпеки
  * [Tailscale](</uk/gateway/tailscale>) — простіша альтернатива для доступу лише через tailnet


Was this useful?YesNo