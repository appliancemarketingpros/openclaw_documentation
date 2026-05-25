---
title: Comprobaciones de auditoría de seguridad
source_url: https://docs.openclaw.ai/es/gateway/security/audit-checks
scraped_at: 2026-05-25
---

`openclaw security audit` emite hallazgos estructurados identificados por `checkId`. Esta página es el catálogo de referencia para esos ID. Para el modelo de amenazas de alto nivel y la guía de endurecimiento, consulta [Seguridad](</es/gateway/security>).

Valores de `checkId` de alta señal que probablemente verás en implementaciones reales (no exhaustivo):

`checkId` | Gravedad | Por qué importa | Clave/ruta principal de corrección | Corrección automática  
---|---|---|---|---  
`fs.state_dir.perms_world_writable` | crítica | Otros usuarios/procesos pueden modificar todo el estado de OpenClaw | permisos del sistema de archivos en `~/.openclaw` | sí  
`fs.state_dir.perms_group_writable` | advertencia | Los usuarios del grupo pueden modificar todo el estado de OpenClaw | permisos del sistema de archivos en `~/.openclaw` | sí  
`fs.state_dir.perms_readable` | advertencia | Otros pueden leer el directorio de estado | permisos del sistema de archivos en `~/.openclaw` | sí  
`fs.state_dir.symlink` | advertencia | El destino del directorio de estado se convierte en otro límite de confianza | diseño del sistema de archivos del directorio de estado | no  
`fs.config.perms_writable` | crítica | Otros pueden cambiar la política/configuración de autenticación/herramientas | permisos del sistema de archivos en `~/.openclaw/openclaw.json` | sí  
`fs.config.symlink` | advertencia | Los archivos de configuración con symlink no son compatibles para escrituras y añaden otro límite de confianza | reemplazarlo por un archivo de configuración normal o apuntar `OPENCLAW_CONFIG_PATH` al archivo real | no  
`fs.config.perms_group_readable` | advertencia | Los usuarios del grupo pueden leer tokens/configuraciones | permisos del sistema de archivos en el archivo de configuración | sí  
`fs.config.perms_world_readable` | crítica | La configuración puede exponer tokens/configuraciones | permisos del sistema de archivos en el archivo de configuración | sí  
`fs.config_include.perms_writable` | crítica | El archivo de inclusión de configuración puede ser modificado por otros | permisos del archivo de inclusión referenciado desde `openclaw.json` | sí  
`fs.config_include.perms_group_readable` | advertencia | Los usuarios del grupo pueden leer secretos/configuraciones incluidos | permisos del archivo de inclusión referenciado desde `openclaw.json` | sí  
`fs.config_include.perms_world_readable` | crítica | Los secretos/configuraciones incluidos son legibles por todos | permisos del archivo de inclusión referenciado desde `openclaw.json` | sí  
`fs.auth_profiles.perms_writable` | crítica | Otros pueden inyectar o reemplazar credenciales de modelo almacenadas | permisos de `agents/<agentId>/agent/auth-profiles.json` | sí  
`fs.auth_profiles.perms_readable` | advertencia | Otros pueden leer claves de API y tokens de OAuth | permisos de `agents/<agentId>/agent/auth-profiles.json` | sí  
`fs.credentials_dir.perms_writable` | crítica | Otros pueden modificar el emparejamiento del canal/estado de credenciales | permisos del sistema de archivos en `~/.openclaw/credentials` | sí  
`fs.credentials_dir.perms_readable` | advertencia | Otros pueden leer el estado de credenciales del canal | permisos del sistema de archivos en `~/.openclaw/credentials` | sí  
`fs.sessions_store.perms_readable` | advertencia | Otros pueden leer transcripciones/metadatos de sesión | permisos del almacén de sesiones | sí  
`fs.log_file.perms_readable` | advertencia | Otros pueden leer registros redactados pero aún sensibles | permisos del archivo de registro del Gateway | sí  
`fs.synced_dir` | advertencia | El estado/configuración en iCloud/Dropbox/Drive amplía la exposición de tokens/transcripciones | mover la configuración/estado fuera de carpetas sincronizadas | no  
`gateway.bind_no_auth` | crítica | Enlace remoto sin secreto compartido | `gateway.bind`, `gateway.auth.*` | no  
`gateway.loopback_no_auth` | crítica | El loopback con proxy inverso puede quedar sin autenticación | `gateway.auth.*`, configuración del proxy | no  
`gateway.trusted_proxies_missing` | advertencia | Hay encabezados de proxy inverso presentes pero no son de confianza | `gateway.trustedProxies` | no  
`gateway.http.no_auth` | advertencia/crítica | Las API HTTP del Gateway son accesibles con `auth.mode="none"` | `gateway.auth.mode`, `gateway.http.endpoints.*` | no  
`gateway.http.session_key_override_enabled` | información | Los llamadores de la API HTTP pueden anular `sessionKey` | `gateway.http.allowSessionKeyOverride` | no  
`gateway.tools_invoke_http.dangerous_allow` | advertencia/crítica | Vuelve a habilitar herramientas peligrosas mediante la API HTTP | `gateway.tools.allow` | no  
`gateway.nodes.allow_commands_dangerous` | advertencia/crítica | Habilita comandos de nodo de alto impacto (cámara/pantalla/contactos/calendario/SMS) | `gateway.nodes.allowCommands` | no  
`gateway.nodes.deny_commands_ineffective` | advertencia | Las entradas de denegación tipo patrón no coinciden con texto de shell ni grupos | `gateway.nodes.denyCommands` | no  
`gateway.tailscale_funnel` | crítica | Exposición pública a internet | `gateway.tailscale.mode` | no  
`gateway.tailscale_serve` | información | La exposición de tailnet está habilitada mediante Serve | `gateway.tailscale.mode` | no  
`gateway.control_ui.allowed_origins_required` | crítica | Control UI no loopback sin lista de permitidos explícita de orígenes del navegador | `gateway.controlUi.allowedOrigins` | no  
`gateway.control_ui.allowed_origins_wildcard` | advertencia/crítica | `allowedOrigins=["*"]` deshabilita la lista de permitidos de orígenes del navegador | `gateway.controlUi.allowedOrigins` | no  
`gateway.control_ui.host_header_origin_fallback` | advertencia/crítica | Habilita el fallback de origen del encabezado Host (rebaja del endurecimiento contra DNS rebinding) | `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback` | no  
`gateway.control_ui.insecure_auth` | advertencia | Alternancia de compatibilidad de autenticación insegura habilitada | `gateway.controlUi.allowInsecureAuth` | no  
`gateway.control_ui.device_auth_disabled` | crítica | Deshabilita la comprobación de identidad del dispositivo | `gateway.controlUi.dangerouslyDisableDeviceAuth` | no  
`gateway.real_ip_fallback_enabled` | advertencia/crítica | Confiar en el fallback de `X-Real-IP` puede permitir suplantación de IP de origen mediante una mala configuración del proxy | `gateway.allowRealIpFallback`, `gateway.trustedProxies` | no  
`gateway.token_too_short` | advertencia | Un token compartido corto es más fácil de atacar por fuerza bruta | `gateway.auth.token` | no  
`gateway.auth_no_rate_limit` | advertencia | La autenticación expuesta sin limitación de tasa aumenta el riesgo de fuerza bruta | `gateway.auth.rateLimit` | no  
`gateway.trusted_proxy_auth` | crítica | La identidad del proxy pasa a ser el límite de autenticación | `gateway.auth.mode="trusted-proxy"` | no  
`gateway.trusted_proxy_no_proxies` | crítica | La autenticación trusted-proxy sin IPs de proxy de confianza no es segura | `gateway.trustedProxies` | no  
`gateway.trusted_proxy_no_user_header` | crítica | La autenticación trusted-proxy no puede resolver la identidad del usuario de forma segura | `gateway.auth.trustedProxy.userHeader` | no  
`gateway.trusted_proxy_no_allowlist` | advertencia | La autenticación trusted-proxy acepta cualquier usuario ascendente autenticado | `gateway.auth.trustedProxy.allowUsers` | no  
`gateway.trusted_proxy_allow_loopback` | advertencia | La autenticación de proxy de confianza acepta orígenes de proxy loopback permitidos explícitamente | `gateway.auth.trustedProxy.allowLoopback` | no  
`gateway.probe_auth_secretref_unavailable` | advertencia | La sonda profunda no pudo resolver los SecretRefs de autenticación en esta ruta de comando | origen de autenticación de la sonda profunda / disponibilidad de SecretRef | no  
`gateway.probe_failed` | advertencia/crítico | Error en la sonda en vivo de Gateway | accesibilidad/autenticación de gateway | no  
`discovery.mdns_full_mode` | advertencia/crítico | El modo completo de mDNS anuncia metadatos `cliPath`/`sshPort` en la red local | `discovery.mdns.mode`, `gateway.bind` | no  
`config.insecure_or_dangerous_flags` | advertencia | Cualquier marca de depuración insegura/peligrosa habilitada | varias claves (consulta el detalle del hallazgo) | no  
`config.secrets.gateway_password_in_config` | advertencia | La contraseña de Gateway se almacena directamente en la configuración | `gateway.auth.password` | no  
`config.secrets.hooks_token_in_config` | advertencia | El token portador de hook se almacena directamente en la configuración | `hooks.token` | no  
`hooks.token_reuse_gateway_token` | crítico | El token de entrada de hook también desbloquea la autenticación de Gateway | `hooks.token`, `gateway.auth.token` | no  
`hooks.token_too_short` | advertencia | Fuerza bruta más fácil en la entrada de hook | `hooks.token` | no  
`hooks.default_session_key_unset` | advertencia | Las ejecuciones del agente de hook se distribuyen en sesiones por solicitud generadas | `hooks.defaultSessionKey` | no  
`hooks.allowed_agent_ids_unrestricted` | advertencia/crítico | Los llamadores de hook autenticados pueden enrutar a cualquier agente configurado | `hooks.allowedAgentIds` | no  
`hooks.request_session_key_enabled` | advertencia/crítico | El llamador externo puede elegir sessionKey | `hooks.allowRequestSessionKey` | no  
`hooks.request_session_key_prefixes_missing` | advertencia/crítico | Sin límite para las formas de clave de sesión externas | `hooks.allowedSessionKeyPrefixes` | no  
`hooks.path_root` | crítico | La ruta de hook es `/`, lo que facilita que la entrada colisione o se enrute incorrectamente | `hooks.path` | no  
`hooks.installs_unpinned_npm_specs` | advertencia | Los registros de instalación de hook no están fijados a especificaciones npm inmutables | metadatos de instalación de hook | no  
`hooks.installs_missing_integrity` | advertencia | Los registros de instalación de hook carecen de metadatos de integridad | metadatos de instalación de hook | no  
`hooks.installs_version_drift` | advertencia | Los registros de instalación de hook divergen de los paquetes instalados | metadatos de instalación de hook | no  
`logging.redact_off` | advertencia | Los valores sensibles se filtran a registros/estado | `logging.redactSensitive` | sí  
`browser.control_invalid_config` | advertencia | La configuración de control del navegador no es válida antes del tiempo de ejecución | `browser.*` | no  
`browser.control_no_auth` | crítico | Control del navegador expuesto sin autenticación por token/contraseña | `gateway.auth.*` | no  
`browser.remote_cdp_http` | advertencia | CDP remoto sobre HTTP sin cifrar carece de cifrado de transporte | perfil del navegador `cdpUrl` | no  
`browser.remote_cdp_private_host` | advertencia | CDP remoto apunta a un host privado/interno | perfil del navegador `cdpUrl`, `browser.ssrfPolicy.*` | no  
`sandbox.docker_config_mode_off` | advertencia | Configuración Docker del entorno aislado presente pero inactiva | `agents.*.sandbox.mode` | no  
`sandbox.bind_mount_non_absolute` | advertencia | Los montajes bind relativos pueden resolverse de forma impredecible | `agents.*.sandbox.docker.binds[]` | no  
`sandbox.dangerous_bind_mount` | crítico | El montaje bind del entorno aislado apunta a rutas bloqueadas del sistema, credenciales o socket de Docker | `agents.*.sandbox.docker.binds[]` | no  
`sandbox.dangerous_network_mode` | crítico | La red Docker del entorno aislado usa `host` o el modo de unión a espacio de nombres `container:*` | `agents.*.sandbox.docker.network` | no  
`sandbox.dangerous_seccomp_profile` | crítico | El perfil seccomp del entorno aislado debilita el aislamiento del contenedor | `agents.*.sandbox.docker.securityOpt` | no  
`sandbox.dangerous_apparmor_profile` | crítico | El perfil AppArmor del entorno aislado debilita el aislamiento del contenedor | `agents.*.sandbox.docker.securityOpt` | no  
`sandbox.browser_cdp_bridge_unrestricted` | advertencia | El puente del navegador del entorno aislado se expone sin restricción de rango de origen | `sandbox.browser.cdpSourceRange` | no  
`sandbox.browser_container.non_loopback_publish` | crítico | El contenedor de navegador existente publica CDP en interfaces que no son loopback | configuración de publicación del contenedor de navegador del entorno aislado | no  
`sandbox.browser_container.hash_label_missing` | advertencia | El contenedor de navegador existente es anterior a las etiquetas de hash de configuración actuales | `openclaw sandbox recreate --browser --all` | no  
`sandbox.browser_container.hash_epoch_stale` | advertencia | El contenedor de navegador existente es anterior a la época de configuración de navegador actual | `openclaw sandbox recreate --browser --all` | no  
`tools.exec.host_sandbox_no_sandbox_defaults` | advertencia | `exec host=sandbox` falla de forma cerrada cuando el entorno aislado está desactivado | `tools.exec.host`, `agents.defaults.sandbox.mode` | no  
`tools.exec.host_sandbox_no_sandbox_agents` | advertencia | `exec host=sandbox` por agente falla de forma cerrada cuando el entorno aislado está desactivado | `agents.list[].tools.exec.host`, `agents.list[].sandbox.mode` | no  
`tools.exec.security_full_configured` | advertencia/crítico | La ejecución en host se está ejecutando con `security="full"` | `tools.exec.security`, `agents.list[].tools.exec.security` | no  
`tools.exec.fs_tools_disabled_but_exec_enabled` | advertencia | La política de herramientas del sistema de archivos no hace que la ejecución de shell sea de solo lectura | `tools.deny`, `agents.list[].tools.deny`, `agents.*.sandbox.workspaceAccess` | no  
`tools.exec.auto_allow_skills_enabled` | advertencia | Las aprobaciones de ejecución confían implícitamente en los binarios de skill | `~/.openclaw/exec-approvals.json` | no  
`tools.exec.allowlist_interpreter_without_strict_inline_eval` | advertencia | Las listas de permitidos de intérpretes permiten evaluación en línea sin reaprobación forzada | `tools.exec.strictInlineEval`, `agents.list[].tools.exec.strictInlineEval`, lista de permitidos de aprobaciones de ejecución | no  
`tools.exec.safe_bins_interpreter_unprofiled` | advertencia | Los binarios de intérprete/tiempo de ejecución en `safeBins` sin perfiles explícitos amplían el riesgo de ejecución | `tools.exec.safeBins`, `tools.exec.safeBinProfiles`, `agents.list[].tools.exec.*` | no  
`tools.exec.safe_bins_broad_behavior` | advertencia | Las herramientas de comportamiento amplio en `safeBins` debilitan el modelo de confianza de bajo riesgo con filtro de stdin | `tools.exec.safeBins`, `agents.list[].tools.exec.safeBins` | no  
`tools.exec.safe_bin_trusted_dirs_risky` | advertencia | `safeBinTrustedDirs` incluye directorios mutables o riesgosos | `tools.exec.safeBinTrustedDirs`, `agents.list[].tools.exec.safeBinTrustedDirs` | no  
`skills.workspace.symlink_escape` | advertencia | `skills/**/SKILL.md` del espacio de trabajo se resuelve fuera de la raíz del espacio de trabajo (deriva de cadena de enlaces simbólicos) | estado del sistema de archivos de `skills/**` del espacio de trabajo | no  
`plugins.extensions_no_allowlist` | warn | Los Plugins están instalados sin una lista de permitidos de Plugin explícita | `plugins.allowlist` | no  
`plugins.installs_unpinned_npm_specs` | warn | Los registros del índice de Plugin no están fijados a especificaciones npm inmutables | metadatos de instalación de Plugin | no  
`plugins.installs_missing_integrity` | warn | Los registros del índice de Plugin carecen de metadatos de integridad | metadatos de instalación de Plugin | no  
`plugins.installs_version_drift` | warn | Los registros del índice de Plugin difieren de los paquetes instalados | metadatos de instalación de Plugin | no  
`plugins.code_safety` | warn/critical | El análisis de código de Plugin encontró patrones sospechosos o peligrosos | código de Plugin / origen de instalación | no  
`plugins.code_safety.entry_path` | warn | La ruta de entrada del Plugin apunta a ubicaciones ocultas o de `node_modules` | `entry` del manifiesto del Plugin | no  
`plugins.code_safety.entry_escape` | critical | La entrada del Plugin se escapa del directorio del Plugin | `entry` del manifiesto del Plugin | no  
`plugins.code_safety.scan_failed` | warn | El análisis de código de Plugin no pudo completarse | ruta del Plugin / entorno de análisis | no  
`skills.code_safety` | warn/critical | Los metadatos/código del instalador de Skills contienen patrones sospechosos o peligrosos | origen de instalación de Skills | no  
`skills.code_safety.scan_failed` | warn | El análisis de código de Skills no pudo completarse | entorno de análisis de Skills | no  
`security.exposure.open_channels_with_exec` | warn/critical | Las salas compartidas/públicas pueden acceder a agentes con ejecución habilitada | `channels.*.dmPolicy`, `channels.*.groupPolicy`, `tools.exec.*`, `agents.list[].tools.exec.*` | no  
`security.exposure.open_groups_with_elevated` | critical | Los grupos abiertos + herramientas elevadas crean rutas de inyección de prompts de alto impacto | `channels.*.groupPolicy`, `tools.elevated.*` | no  
`security.exposure.open_groups_with_runtime_or_fs` | critical/warn | Los grupos abiertos pueden acceder a herramientas de comandos/archivos sin protecciones de sandbox/área de trabajo | `channels.*.groupPolicy`, `tools.profile/deny`, `tools.fs.workspaceOnly`, `agents.*.sandbox.mode` | no  
`security.trust_model.multi_user_heuristic` | warn | La configuración parece multiusuario mientras que el modelo de confianza del Gateway es de asistente personal | separar límites de confianza, o endurecimiento para usuarios compartidos (`sandbox.mode`, denegación de herramientas/alcance de área de trabajo) | no  
`tools.profile_minimal_overridden` | warn | Las anulaciones de agentes omiten el perfil mínimo global | `agents.list[].tools.profile` | no  
`plugins.tools_reachable_permissive_policy` | warn | Las herramientas de extensión son accesibles en contextos permisivos | `tools.profile` \+ permitir/denegar herramientas | no  
`models.legacy` | warn | Las familias de modelos heredadas todavía están configuradas | selección de modelo | no  
`models.weak_tier` | warn | Los modelos configurados están por debajo de los niveles recomendados actuales | selección de modelo | no  
`models.small_params` | critical/info | Los modelos pequeños + superficies de herramientas inseguras aumentan el riesgo de inyección | elección de modelo + política de sandbox/herramientas | no  
`summary.attack_surface` | info | Resumen acumulado de la postura de autenticación, canal, herramienta y exposición | varias claves (ver detalle del hallazgo) | no  
  
## Relacionado

  * [Seguridad](</es/gateway/security>)
  * [Configuración](</es/gateway/configuration>)
  * [Autenticación de proxy de confianza](</es/gateway/trusted-proxy-auth>)


Was this useful?YesNo