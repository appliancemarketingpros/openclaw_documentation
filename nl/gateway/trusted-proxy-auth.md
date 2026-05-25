---
title: Vertrouwde proxy-authenticatie
source_url: https://docs.openclaw.ai/nl/gateway/trusted-proxy-auth
scraped_at: 2026-05-25
---

## Wanneer gebruiken

Gebruik de auth-modus `trusted-proxy` wanneer:

  * Je OpenClaw achter een **identiteitsbewuste proxy** draait (Pomerium, Caddy + OAuth, nginx + oauth2-proxy, Traefik + forward auth).
  * Je proxy alle authenticatie afhandelt en de gebruikersidentiteit via headers doorgeeft.
  * Je in een Kubernetes- of containeromgeving werkt waar de proxy het enige pad naar de Gateway is.
  * Je WebSocket-fouten `1008 unauthorized` krijgt omdat browsers geen tokens in WS-payloads kunnen doorgeven.


## Wanneer NIET gebruiken

  * Als je proxy gebruikers niet authenticeert (alleen een TLS-terminator of load balancer).
  * Als er een pad naar de Gateway is dat de proxy omzeilt (gaten in de firewall, interne netwerktoegang).
  * Als je niet zeker weet of je proxy doorgestuurde headers correct verwijdert/overschrijft.
  * Als je alleen persoonlijke toegang voor één gebruiker nodig hebt (overweeg Tailscale Serve + loopback voor een eenvoudigere configuratie).


## Hoe het werkt

* ### Proxy authenticates the user

Je reverseproxy authenticeert gebruikers (OAuth, OIDC, SAML, enz.).

* ### Proxy adds an identity header

De proxy voegt een header toe met de geauthenticeerde gebruikersidentiteit (bijv. `x-forwarded-user: nick@example.com`).

* ### Gateway verifies trusted source

OpenClaw controleert of de aanvraag afkomstig is van een **vertrouwd proxy-IP** (geconfigureerd in `gateway.trustedProxies`).

* ### Gateway extracts identity

OpenClaw haalt de gebruikersidentiteit uit de geconfigureerde header.

* ### Authorize

Als alles klopt, wordt de aanvraag geautoriseerd.

## Koppelingsgedrag van Control UI

Wanneer `gateway.auth.mode = "trusted-proxy"` actief is en de aanvraag de trusted-proxy-controles doorstaat, kunnen Control UI-WebSocket-sessies verbinden zonder apparaatkoppelingsidentiteit.

Gevolgen:

  * Koppeling is in deze modus niet langer de primaire poort voor toegang tot Control UI.
  * Het authenticatiebeleid van je reverseproxy en `allowUsers` worden de effectieve toegangscontrole.
  * Houd Gateway-ingress beperkt tot alleen vertrouwde proxy-IP's (`gateway.trustedProxies` \+ firewall).


## Configuratie

json5Copy code
[code]
    {  gateway: {    // Trusted-proxy auth expects requests from a non-loopback trusted proxy source by default    bind: "lan",     // CRITICAL: Only add your proxy's IP(s) here    trustedProxies: ["10.0.0.1", "172.17.0.1"],     auth: {      mode: "trusted-proxy",      trustedProxy: {        // Header containing authenticated user identity (required)        userHeader: "x-forwarded-user",         // Optional: headers that MUST be present (proxy verification)        requiredHeaders: ["x-forwarded-proto", "x-forwarded-host"],         // Optional: restrict to specific users (empty = allow all)        allowUsers: ["nick@example.com", "admin@company.org"],         // Optional: allow a same-host loopback proxy after explicit opt-in        allowLoopback: false,      },    },  },}
[/code]

### Configuratiereferentie

Array met proxy-IP-adressen die vertrouwd mogen worden. Aanvragen vanaf andere IP's worden geweigerd.

Moet `"trusted-proxy"` zijn.

Headernaam die de geauthenticeerde gebruikersidentiteit bevat.

Extra headers die aanwezig moeten zijn voordat de aanvraag vertrouwd wordt.

Allowlist met gebruikersidentiteiten. Leeg betekent dat alle geauthenticeerde gebruikers zijn toegestaan.

Opt-in-ondersteuning voor same-host loopback-reverseproxy's. Standaard `false`.

## TLS-terminatie en HSTS

Gebruik één TLS-terminatiepunt en pas HSTS daar toe.

### Proxy TLS termination (recommended)

Wanneer je reverseproxy HTTPS afhandelt voor `https://control.example.com`, stel je `Strict-Transport-Security` op de proxy in voor dat domein.

  * Geschikt voor implementaties die aan internet zijn blootgesteld.
  * Houdt certificaat- en HTTP-hardeningbeleid op één plek.
  * OpenClaw kan achter de proxy op loopback-HTTP blijven.


Voorbeeldheaderwaarde:

textCopy code
[code]
    Strict-Transport-Security: max-age=31536000; includeSubDomains
[/code]

### Gateway TLS termination

Als OpenClaw zelf rechtstreeks HTTPS serveert (zonder TLS-terminerende proxy), stel dan in:

json5Copy code
[code]
    {  gateway: {    tls: { enabled: true },    http: {      securityHeaders: {        strictTransportSecurity: "max-age=31536000; includeSubDomains",      },    },  },}
[/code]

`strictTransportSecurity` accepteert een stringheaderwaarde, of `false` om dit expliciet uit te schakelen.

### Uitroladvies

  * Begin eerst met een korte maximale leeftijd (bijvoorbeeld `max-age=300`) terwijl je verkeer valideert.
  * Verhoog pas naar langlevende waarden (bijvoorbeeld `max-age=31536000`) wanneer het vertrouwen groot is.
  * Voeg `includeSubDomains` alleen toe als elk subdomein klaar is voor HTTPS.
  * Gebruik preload alleen als je bewust voldoet aan de preload-vereisten voor je volledige domeinset.
  * Lokale ontwikkeling met alleen loopback heeft geen baat bij HSTS.


## Voorbeelden van proxyconfiguratie

Pomerium

Pomerium geeft identiteit door in `x-pomerium-claim-email` (of andere claimheaders) en een JWT in `x-pomerium-jwt-assertion`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Pomerium's IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-pomerium-claim-email",        requiredHeaders: ["x-pomerium-jwt-assertion"],      },    },  },}
[/code]

Pomerium-configuratiefragment:

yamlCopy code
[code]
    routes:  - from: https://openclaw.example.com    to: http://openclaw-gateway:18789    policy:      - allow:          or:            - email:                is: nick@example.com    pass_identity_headers: true
[/code]

Caddy with OAuth

Caddy met de Plugin `caddy-security` kan gebruikers authenticeren en identiteitsheaders doorgeven.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // Caddy/sidecar proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

Caddyfile-fragment:

CodeCopy code
[code]
    openclaw.example.com {    authenticate with oauth2_provider    authorize with policy1     reverse_proxy openclaw:18789 {        header_up X-Forwarded-User {http.auth.user.email}    }}
[/code]

nginx + oauth2-proxy

oauth2-proxy authenticeert gebruikers en geeft de identiteit door in `x-auth-request-email`.

json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["10.0.0.1"], // nginx/oauth2-proxy IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-auth-request-email",      },    },  },}
[/code]

nginx-configuratiefragment:

nginxCopy code
[code]
    location / {    auth_request /oauth2/auth;    auth_request_set $user $upstream_http_x_auth_request_email;     proxy_pass http://openclaw:18789;    proxy_set_header X-Auth-Request-Email $user;    proxy_http_version 1.1;    proxy_set_header Upgrade $http_upgrade;    proxy_set_header Connection "upgrade";}
[/code]

Traefik with forward auth json5Copy code
[code]
    {  gateway: {    bind: "lan",    trustedProxies: ["172.17.0.1"], // Traefik container IP    auth: {      mode: "trusted-proxy",      trustedProxy: {        userHeader: "x-forwarded-user",      },    },  },}
[/code]

## Gemengde tokenconfiguratie

OpenClaw weigert dubbelzinnige configuraties waarbij zowel een `gateway.auth.token` (of `OPENCLAW_GATEWAY_TOKEN`) als de modus `trusted-proxy` tegelijk actief zijn. Gemengde tokenconfiguraties kunnen ervoor zorgen dat loopback-aanvragen stilzwijgend via het verkeerde authenticatiepad worden geauthenticeerd.

Als je bij het opstarten een fout `mixed_trusted_proxy_token` ziet:

  * Verwijder het gedeelde token wanneer je de trusted-proxy-modus gebruikt, of
  * Schakel `gateway.auth.mode` over naar `"token"` als je tokengebaseerde authenticatie bedoelt.


Loopback trusted-proxy-identiteitsheaders falen nog steeds gesloten: same-host-aanroepers worden niet stilzwijgend geauthenticeerd als proxygebruikers. Interne OpenClaw-aanroepers die de proxy omzeilen, kunnen zich in plaats daarvan authenticeren met `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD`. Tokenfallback blijft in trusted-proxy-modus opzettelijk niet ondersteund.

## Header voor operatorscopes

Trusted-proxy-auth is een **identiteitsdragende** HTTP-modus, dus aanroepers mogen optioneel operatorscopes declareren met `x-openclaw-scopes`.

Voorbeelden:

  * `x-openclaw-scopes: operator.read`
  * `x-openclaw-scopes: operator.read,operator.write`
  * `x-openclaw-scopes: operator.admin,operator.write`


Gedrag:

  * Wanneer de header aanwezig is, respecteert OpenClaw de gedeclareerde scopeset.
  * Wanneer de header aanwezig maar leeg is, declareert de aanvraag **geen** operatorscopes.
  * Wanneer de header ontbreekt, vallen normale identiteitsdragende HTTP-API's terug op de standaard operatorscopeset.
  * Gateway-auth **Plugin-HTTP-routes** zijn standaard smaller: wanneer `x-openclaw-scopes` ontbreekt, valt hun runtimescope terug op `operator.write`.
  * HTTP-aanvragen vanuit browsers moeten nog steeds slagen voor `gateway.controlUi.allowedOrigins` (of de bewuste Host-header-fallbackmodus), zelfs nadat trusted-proxy-auth is geslaagd.


Praktische regel: stuur `x-openclaw-scopes` expliciet wanneer je wilt dat een trusted-proxy-aanvraag smaller is dan de standaardwaarden, of wanneer een gateway-auth Plugin-route iets sterkers nodig heeft dan schrijfscope.

## Beveiligingschecklist

Voordat je trusted-proxy-auth inschakelt, controleer:

  * [ ] **Proxy is het enige pad** : De Gateway-poort is afgeschermd voor alles behalve je proxy.
  * [ ] **trustedProxies is minimaal** : Alleen je daadwerkelijke proxy-IP's, geen volledige subnetten.
  * [ ] **Loopback-proxybron is bewust gekozen** : trusted-proxy-auth faalt gesloten voor aanvragen met een loopback-bron, tenzij `gateway.auth.trustedProxy.allowLoopback` expliciet is ingeschakeld voor een proxy op dezelfde host.
  * [ ] **Proxy stript headers** : Je proxy overschrijft (voegt niet toe aan) `x-forwarded-*`-headers van clients.
  * [ ] **TLS-terminatie** : Je proxy handelt TLS af; gebruikers verbinden via HTTPS.
  * [ ] **allowedOrigins is expliciet** : Niet-loopback Control UI gebruikt expliciete `gateway.controlUi.allowedOrigins`.
  * [ ] **allowUsers is ingesteld** (aanbevolen): Beperk dit tot bekende gebruikers in plaats van iedereen toe te staan die is geauthenticeerd.
  * [ ] **Geen gemengde tokenconfiguratie** : Stel niet zowel `gateway.auth.token` als `gateway.auth.mode: "trusted-proxy"` in.
  * [ ] **Lokale wachtwoordfallback is privé** : Als je `gateway.auth.password` configureert voor interne directe callers, houd de Gateway-poort dan afgeschermd zodat externe niet-proxyclients deze niet rechtstreeks kunnen bereiken.


## Beveiligingsaudit

`openclaw security audit` markeert trusted-proxy-auth met een bevinding met **kritieke** ernst. Dit is opzettelijk — het herinnert je eraan dat je beveiliging delegeert aan je proxyconfiguratie.

De audit controleert op:

  * Basiswaarschuwing/kritieke herinnering `gateway.trusted_proxy_auth`
  * Ontbrekende `trustedProxies`-configuratie
  * Ontbrekende `userHeader`-configuratie
  * Lege `allowUsers` (staat elke geauthenticeerde gebruiker toe)
  * Ingeschakelde `allowLoopback` voor proxybronnen op dezelfde host
  * Wildcard- of ontbrekend browser-originbeleid op blootgestelde Control UI-oppervlakken


## Probleemoplossing

trusted_proxy_untrusted_source

De aanvraag kwam niet van een IP in `gateway.trustedProxies`. Controleer:

  * Klopt het proxy-IP? (Docker-container-IP's kunnen wijzigen.)
  * Staat er een load balancer voor je proxy?
  * Gebruik `docker inspect` of `kubectl get pods -o wide` om daadwerkelijke IP's te vinden.

trusted_proxy_loopback_source

OpenClaw heeft een trusted-proxy-aanvraag met loopback-bron geweigerd.

Controleer:

  * Verbindt de proxy vanaf `127.0.0.1` / `::1`?
  * Probeer je trusted-proxy-auth te gebruiken met een loopback-reverseproxy op dezelfde host?


Oplossing:

  * Geef de voorkeur aan token-/wachtwoordauth voor interne clients op dezelfde host die niet via de proxy gaan, of
  * Routeer via een niet-loopback trusted proxy-adres en houd dat IP in `gateway.trustedProxies`, of
  * Stel voor een bewuste reverseproxy op dezelfde host `gateway.auth.trustedProxy.allowLoopback = true` in, houd het loopback-adres in `gateway.trustedProxies` en zorg ervoor dat de proxy identiteitsheaders stript of overschrijft.

trusted_proxy_user_missing

De gebruikersheader was leeg of ontbrak. Controleer:

  * Is je proxy geconfigureerd om identiteitsheaders door te geven?
  * Klopt de headernaam? (hoofdletterongevoelig, maar spelling telt)
  * Is de gebruiker daadwerkelijk geauthenticeerd bij de proxy?

trusted_proxy_missing_header_*

Een vereiste header was niet aanwezig. Controleer:

  * Je proxyconfiguratie voor die specifieke headers.
  * Of headers ergens in de keten worden gestript.

trusted_proxy_user_not_allowed

De gebruiker is geauthenticeerd, maar staat niet in `allowUsers`. Voeg de gebruiker toe of verwijder de allowlist.

trusted_proxy_origin_not_allowed

trusted-proxy-auth is geslaagd, maar de browserheader `Origin` kwam niet door de origincontroles van de Control UI.

Controleer:

  * `gateway.controlUi.allowedOrigins` bevat de exacte browser-origin.
  * Je vertrouwt niet op wildcard-origins, tenzij je bewust allow-all-gedrag wilt.
  * Als je bewust de Host-headerfallbackmodus gebruikt, is `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback=true` bewust ingesteld.

WebSocket blijft falen

Zorg ervoor dat je proxy:

  * WebSocket-upgrades ondersteunt (`Upgrade: websocket`, `Connection: upgrade`).
  * De identiteitsheaders doorgeeft bij WebSocket-upgradeaanvragen (niet alleen HTTP).
  * Geen afzonderlijk authpad heeft voor WebSocket-verbindingen.


## Migratie vanaf token-auth

Als je overstapt van token-auth naar trusted-proxy:

* ### Configureer de proxy

Configureer je proxy om gebruikers te authenticeren en headers door te geven.

* ### Test de proxy onafhankelijk

Test de proxyconfiguratie onafhankelijk (curl met headers).

* ### Werk de OpenClaw-configuratie bij

Werk de OpenClaw-configuratie bij met trusted-proxy-auth.

* ### Herstart de Gateway

Herstart de Gateway.

* ### Test WebSocket

Test WebSocket-verbindingen vanuit de Control UI.

* ### Audit

Voer `openclaw security audit` uit en bekijk de bevindingen.

## Gerelateerd

  * [Configuratie](</nl/gateway/configuration>) — configuratiereferentie
  * [Externe toegang](</nl/gateway/remote>) — andere patronen voor externe toegang
  * [Beveiliging](</nl/gateway/security>) — volledige beveiligingsgids
  * [Tailscale](</nl/gateway/tailscale>) — eenvoudiger alternatief voor toegang alleen via tailnet


Was this useful?YesNo