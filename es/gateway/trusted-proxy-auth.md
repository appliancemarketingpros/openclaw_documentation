---
title: Autenticación mediante proxy de confianza
source_url: https://docs.openclaw.ai/es/gateway/trusted-proxy-auth
scraped_at: 2026-05-25
---

## Cuándo usarlo

Usa el modo de autenticación `trusted-proxy` cuando:

  * Ejecutas OpenClaw detrás de un **proxy consciente de identidad** (Pomerium, Caddy + OAuth, nginx + oauth2-proxy, Traefik + forward auth).
  * Tu proxy gestiona toda la autenticación y pasa la identidad del usuario mediante encabezados.
  * Estás en un entorno de Kubernetes o contenedores donde el proxy es la única ruta al Gateway.
  * Te encuentras con errores de WebSocket `1008 unauthorized` porque los navegadores no pueden pasar tokens en cargas WS.


## Cuándo NO usarlo

  * Si tu proxy no autentica usuarios (solo es un terminador TLS o balanceador de carga).
  * Si existe alguna ruta al Gateway que omite el proxy (huecos en el firewall, acceso desde la red interna).
  * Si no tienes claro si tu proxy elimina o sobrescribe correctamente los encabezados reenviados.
  * Si solo necesitas acceso personal para un único usuario (considera Tailscale Serve + loopback para una configuración más sencilla).


## Cómo funciona

* ### El proxy autentica al usuario

Tu proxy inverso autentica a los usuarios (OAuth, OIDC, SAML, etc.).

* ### El proxy agrega un encabezado de identidad

El proxy agrega un encabezado con la identidad del usuario autenticado (por ejemplo, `x-forwarded-user: nick@example.com`).

* ### El Gateway verifica la fuente de confianza

OpenClaw comprueba que la solicitud provenga de una **IP de proxy de confianza** (configurada en `gateway.trustedProxies`).

* ### El Gateway extrae la identidad

OpenClaw extrae la identidad del usuario desde el encabezado configurado.

* ### Autorizar

Si todo es correcto, la solicitud se autoriza.

## Comportamiento de emparejamiento de Control UI

Cuando `gateway.auth.mode = "trusted-proxy"` está activo y la solicitud supera las comprobaciones de proxy de confianza, las sesiones WebSocket de Control UI pueden conectarse sin identidad de emparejamiento de dispositivo.

Implicaciones:

  * El emparejamiento deja de ser la puerta principal para el acceso a Control UI en este modo.
  * La política de autenticación de tu proxy inverso y `allowUsers` se convierten en el control de acceso efectivo.
  * Mantén la entrada del Gateway bloqueada solo a IPs de proxy de confianza (`gateway.trustedProxies` \+ firewall).


## Configuración

json5Copy code
[code]
    {  gateway: {    // Trusted-proxy auth expects requests from a non-loopback trusted proxy source by default    bind: "lan",     // CRITICAL: Only add your proxy's IP(s) here    trustedProxies: ["10.0.0.1", "172.17.0.1"],     auth: {      mode: "trusted-proxy",      trustedProxy: {        // Header containing authenticated user identity (required)        userHeader: "x-forwarded-user",         // Optional: headers that MUST be present (proxy verification)        requiredHeaders: ["x-forwarded-proto", "x-forwarded-host"],         // Optional: restrict to specific users (empty = allow all)        allowUsers: ["nick@example.com", "admin@company.org"],         // Optional: allow a same-host loopback proxy after explicit opt-in        allowLoopback: false,      },    },  },}
[/code]

### Referencia de configuración

Arreglo de direcciones IP de proxy en las que confiar. Las solicitudes desde otras IPs se rechazan.

Debe ser `"trusted-proxy"`.

Nombre del encabezado que contiene la identidad del usuario autenticado.

Encabezados adicionales que deben estar presentes para que la solicitud sea de confianza.

Lista de permitidos de identidades de usuario. Vacío significa permitir todos los usuarios autenticados.

Soporte opcional para proxies inversos loopback en el mismo host. El valor predeterminado es `false`.

## Terminación TLS y HSTS

Usa un único punto de terminación TLS y aplica HSTS allí.

### Terminación TLS en el proxy (recomendado)

Cuando tu proxy inverso gestiona HTTPS para `https://control.example.com`, establece `Strict-Transport-Security` en el proxy para ese dominio.

  * Buena opción para implementaciones expuestas a internet.
  * Mantiene el certificado y la política de endurecimiento HTTP en un solo lugar.
  * OpenClaw puede permanecer en HTTP loopback detrás del proxy.


Valor de encabezado de ejemplo:

textCopy code
[code]
    Strict-Transport-Security: max-age=31536000; includeSubDomains
[/code]

### Terminación TLS en el Gateway

Si OpenClaw sirve HTTPS directamente por sí mismo (sin proxy que termine TLS), establece:

json5Copy code
[code]
    {  gateway: {    tls: { enabled: true },    http: {      securityHeaders: {        strictTransportSecurity: "max-age=31536000; includeSubDomains",      },    },  },}
[/code]

`strictTransportSecurity` acepta un valor de encabezado de cadena o `false` para deshabilitarlo explícitamente.

### Guía de despliegue

  * Empieza primero con una duración máxima corta (por ejemplo, `max-age=300`) mientras validas el tráfico.
  * Aumenta a valores de larga duración (por ejemplo, `max-age=31536000`) solo cuando la confianza sea alta.
  * Agrega `includeSubDomains` solo si todos los subdominios están listos para HTTPS.
  * Usa preload solo si cumples intencionalmente los requisitos de preload para todo tu conjunto de dominios.
  * El desarrollo local solo con loopback no se beneficia de HSTS.


## Ejemplos de configuración de proxy

Pomerium

Pomerium pasa la identidad en `x-pomerium-claim-email` (u otros encabezados de claims) y un JWT en `x-pomerium-jwt-assertion`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Pomerium's IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-pomerium-claim-email",        requiredHeaders: ["x-pomerium-jwt-assertion"],      },    },  },}
[/code]

Fragmento de configuración de Pomerium:

yamlCopy code
[code]
    routes:  - from: https://openclaw.example.com    to: http://openclaw-gateway:18789    policy:      - allow:          or:            - email:                is: nick@example.com    pass_identity_headers: true
[/code]

Caddy con OAuth

Caddy con el Plugin `caddy-security` puede autenticar usuarios y pasar encabezados de identidad.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Caddy/sidecar proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

Fragmento de Caddyfile:

CodeCopy code
[code]
    openclaw.example.com {    authenticate with oauth2_provider    authorize with policy1     reverse_proxy openclaw:18789 {        header_up X-Forwarded-User {http.auth.user.email}    }}
[/code]

nginx + oauth2-proxy

oauth2-proxy autentica usuarios y pasa la identidad en `x-auth-request-email`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // nginx/oauth2-proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-auth-request-email",      },    },  },}
[/code]

Fragmento de configuración de nginx:

nginxCopy code
[code]
    location / {    auth_request /oauth2/auth;    auth_request_set $user $upstream_http_x_auth_request_email;     proxy_pass http://openclaw:18789;    proxy_set_header X-Auth-Request-Email $user;    proxy_http_version 1.1;    proxy_set_header Upgrade $http_upgrade;    proxy_set_header Connection "upgrade";}
[/code]

Traefik con forward auth json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["172.17.0.1"], // Traefik container IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

## Configuración mixta de tokens

OpenClaw rechaza configuraciones ambiguas en las que tanto un `gateway.auth.token` (o `OPENCLAW_GATEWAY_TOKEN`) como el modo `trusted-proxy` están activos al mismo tiempo. Las configuraciones mixtas de tokens pueden hacer que las solicitudes loopback se autentiquen silenciosamente por la ruta de autenticación equivocada.

Si ves un error `mixed_trusted_proxy_token` al iniciar:

  * Elimina el token compartido al usar el modo de proxy de confianza, o
  * Cambia `gateway.auth.mode` a `"token"` si quieres autenticación basada en tokens.


Los encabezados de identidad de proxy de confianza en loopback siguen fallando de forma cerrada: los llamadores en el mismo host no se autentican silenciosamente como usuarios del proxy. Los llamadores internos de OpenClaw que omiten el proxy pueden autenticarse con `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD` en su lugar. La alternativa de token sigue sin admitirse intencionalmente en modo de proxy de confianza.

## Encabezado de ámbitos de operador

La autenticación de proxy de confianza es un modo HTTP **portador de identidad** , por lo que los llamadores pueden declarar opcionalmente ámbitos de operador con `x-openclaw-scopes`.

Ejemplos:

  * `x-openclaw-scopes: operator.read`
  * `x-openclaw-scopes: operator.read,operator.write`
  * `x-openclaw-scopes: operator.admin,operator.write`


Comportamiento:

  * Cuando el encabezado está presente, OpenClaw respeta el conjunto de ámbitos declarado.
  * Cuando el encabezado está presente pero vacío, la solicitud declara **ningún** ámbito de operador.
  * Cuando el encabezado está ausente, las API HTTP normales portadoras de identidad recurren al conjunto estándar de ámbitos de operador predeterminados.
  * Las **rutas HTTP de Plugin** con autenticación de Gateway son más estrechas de forma predeterminada: cuando `x-openclaw-scopes` está ausente, su ámbito de tiempo de ejecución recurre a `operator.write`.
  * Las solicitudes HTTP con origen de navegador aún deben pasar `gateway.controlUi.allowedOrigins` (o el modo deliberado de alternativa con encabezado Host) incluso después de que la autenticación de proxy de confianza tenga éxito.


Regla práctica: envía `x-openclaw-scopes` explícitamente cuando quieras que una solicitud de proxy de confianza sea más estrecha que los valores predeterminados, o cuando una ruta de Plugin con autenticación de Gateway necesite algo más fuerte que el ámbito de escritura.

## Lista de comprobación de seguridad

Antes de habilitar la autenticación trusted-proxy, verifica:

  * [ ] **El proxy es la única ruta** : El puerto del Gateway está protegido por firewall frente a todo excepto tu proxy.
  * [ ] **trustedProxies es mínimo** : Solo las IP reales de tu proxy, no subredes completas.
  * [ ] **La fuente de proxy loopback es deliberada** : La autenticación trusted-proxy falla de forma cerrada para solicitudes con fuente loopback a menos que `gateway.auth.trustedProxy.allowLoopback` esté habilitado explícitamente para un proxy en el mismo host.
  * [ ] **El proxy elimina encabezados** : Tu proxy sobrescribe (no agrega) los encabezados `x-forwarded-*` de los clientes.
  * [ ] **Terminación TLS** : Tu proxy maneja TLS; los usuarios se conectan mediante HTTPS.
  * [ ] **allowedOrigins es explícito** : La Control UI que no usa loopback utiliza `gateway.controlUi.allowedOrigins` explícito.
  * [ ] **allowUsers está configurado** (recomendado): Restringe a usuarios conocidos en lugar de permitir a cualquier persona autenticada.
  * [ ] **Sin configuración mixta de tokens** : No configures tanto `gateway.auth.token` como `gateway.auth.mode: "trusted-proxy"`.
  * [ ] **La alternativa de contraseña local es privada** : Si configuras `gateway.auth.password` para llamadores directos internos, mantén el puerto del Gateway protegido por firewall para que los clientes remotos que no pasan por el proxy no puedan acceder directamente.


## Auditoría de seguridad

`openclaw security audit` marcará la autenticación trusted-proxy con un hallazgo de gravedad **crítica**. Esto es intencional: es un recordatorio de que estás delegando la seguridad a la configuración de tu proxy.

La auditoría comprueba:

  * Advertencia/recordatorio crítico base `gateway.trusted_proxy_auth`
  * Falta la configuración de `trustedProxies`
  * Falta la configuración de `userHeader`
  * `allowUsers` vacío (permite cualquier usuario autenticado)
  * `allowLoopback` habilitado para fuentes de proxy en el mismo host
  * Política de origen del navegador comodín o ausente en superficies expuestas de la Control UI


## Solución de problemas

trusted_proxy_untrusted_source

La solicitud no provino de una IP en `gateway.trustedProxies`. Comprueba:

  * ¿La IP del proxy es correcta? (Las IP de contenedores Docker pueden cambiar).
  * ¿Hay un balanceador de carga delante de tu proxy?
  * Usa `docker inspect` o `kubectl get pods -o wide` para encontrar las IP reales.

trusted_proxy_loopback_source

OpenClaw rechazó una solicitud trusted-proxy con fuente loopback.

Comprueba:

  * ¿El proxy se conecta desde `127.0.0.1` / `::1`?
  * ¿Intentas usar autenticación trusted-proxy con un proxy inverso loopback en el mismo host?


Corrección:

  * Prefiere autenticación por token/contraseña para clientes internos del mismo host que no pasan por el proxy, o
  * Enruta a través de una dirección de proxy de confianza que no sea loopback y mantén esa IP en `gateway.trustedProxies`, o
  * Para un proxy inverso deliberado en el mismo host, establece `gateway.auth.trustedProxy.allowLoopback = true`, mantén la dirección loopback en `gateway.trustedProxies` y asegúrate de que el proxy elimine o sobrescriba los encabezados de identidad.

trusted_proxy_user_missing

El encabezado de usuario estaba vacío o faltaba. Comprueba:

  * ¿Tu proxy está configurado para pasar encabezados de identidad?
  * ¿El nombre del encabezado es correcto? (no distingue entre mayúsculas y minúsculas, pero la ortografía importa)
  * ¿El usuario está realmente autenticado en el proxy?

trusted_proxy_missing_header_*

Faltaba un encabezado obligatorio. Comprueba:

  * La configuración de tu proxy para esos encabezados específicos.
  * Si los encabezados se están eliminando en algún punto de la cadena.

trusted_proxy_user_not_allowed

El usuario está autenticado pero no está en `allowUsers`. Agrégalo o elimina la lista de permitidos.

trusted_proxy_origin_not_allowed

La autenticación trusted-proxy tuvo éxito, pero el encabezado `Origin` del navegador no superó las comprobaciones de origen de la Control UI.

Comprueba:

  * `gateway.controlUi.allowedOrigins` incluye el origen exacto del navegador.
  * No dependes de orígenes comodín a menos que quieras intencionalmente un comportamiento que permita todo.
  * Si usas intencionalmente el modo de alternativa con encabezado Host, `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` está establecido deliberadamente.

WebSocket still failing

Asegúrate de que tu proxy:

  * Admita actualizaciones de WebSocket (`Upgrade: websocket`, `Connection: upgrade`).
  * Pase los encabezados de identidad en las solicitudes de actualización de WebSocket (no solo HTTP).
  * No tenga una ruta de autenticación separada para conexiones WebSocket.


## Migración desde autenticación por token

Si estás migrando desde autenticación por token a trusted-proxy:

* ### Configure the proxy

Configura tu proxy para autenticar usuarios y pasar encabezados.

* ### Test the proxy independently

Prueba la configuración del proxy de forma independiente (curl con encabezados).

* ### Update OpenClaw config

Actualiza la configuración de OpenClaw con autenticación trusted-proxy.

* ### Restart the Gateway

Reinicia el Gateway.

* ### Test WebSocket

Prueba las conexiones WebSocket desde la Control UI.

* ### Audit

Ejecuta `openclaw security audit` y revisa los hallazgos.

## Relacionado

  * [Configuración](</es/gateway/configuration>) — referencia de configuración
  * [Acceso remoto](</es/gateway/remote>) — otros patrones de acceso remoto
  * [Seguridad](</es/gateway/security>) — guía completa de seguridad
  * [Tailscale](</es/gateway/tailscale>) — alternativa más simple para acceso solo por tailnet


Was this useful?YesNo