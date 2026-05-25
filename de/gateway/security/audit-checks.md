---
title: Sicherheitsaudit-Prüfungen
source_url: https://docs.openclaw.ai/de/gateway/security/audit-checks
scraped_at: 2026-05-25
---

`openclaw security audit` gibt strukturierte Befunde aus, die nach `checkId` gruppiert sind. Diese Seite ist der Referenzkatalog für diese IDs. Das übergeordnete Bedrohungsmodell und Hinweise zur Härtung finden Sie unter [Sicherheit](</de/gateway/security>).

Aussagekräftige `checkId`-Werte, die Sie in realen Bereitstellungen am ehesten sehen werden (nicht vollständig):

`checkId` | Schweregrad | Warum es wichtig ist | Primärer Behebungsschlüssel/-pfad | Automatische Behebung  
---|---|---|---|---  
`fs.state_dir.perms_world_writable` | kritisch | Andere Benutzer/Prozesse können den gesamten OpenClaw-Zustand ändern | Dateisystemberechtigungen für `~/.openclaw` | ja  
`fs.state_dir.perms_group_writable` | Warnung | Gruppenbenutzer können den gesamten OpenClaw-Zustand ändern | Dateisystemberechtigungen für `~/.openclaw` | ja  
`fs.state_dir.perms_readable` | Warnung | Das Zustandsverzeichnis ist für andere lesbar | Dateisystemberechtigungen für `~/.openclaw` | ja  
`fs.state_dir.symlink` | Warnung | Das Ziel des Zustandsverzeichnisses wird zu einer weiteren Vertrauensgrenze | Dateisystemlayout des Zustandsverzeichnisses | nein  
`fs.config.perms_writable` | kritisch | Andere können Authentifizierungs-/Tool-Richtlinien oder Konfiguration ändern | Dateisystemberechtigungen für `~/.openclaw/openclaw.json` | ja  
`fs.config.symlink` | Warnung | Per Symlink verknüpfte Konfigurationsdateien werden für Schreibvorgänge nicht unterstützt und fügen eine weitere Vertrauensgrenze hinzu | durch eine reguläre Konfigurationsdatei ersetzen oder `OPENCLAW_CONFIG_PATH` auf die echte Datei zeigen lassen | nein  
`fs.config.perms_group_readable` | Warnung | Gruppenbenutzer können Konfigurationstokens/-einstellungen lesen | Dateisystemberechtigungen für die Konfigurationsdatei | ja  
`fs.config.perms_world_readable` | kritisch | Die Konfiguration kann Tokens/Einstellungen offenlegen | Dateisystemberechtigungen für die Konfigurationsdatei | ja  
`fs.config_include.perms_writable` | kritisch | Die Konfigurations-Include-Datei kann von anderen geändert werden | Berechtigungen der Include-Datei, auf die aus `openclaw.json` verwiesen wird | ja  
`fs.config_include.perms_group_readable` | Warnung | Gruppenbenutzer können eingebundene Secrets/Einstellungen lesen | Berechtigungen der Include-Datei, auf die aus `openclaw.json` verwiesen wird | ja  
`fs.config_include.perms_world_readable` | kritisch | Eingebundene Secrets/Einstellungen sind weltweit lesbar | Berechtigungen der Include-Datei, auf die aus `openclaw.json` verwiesen wird | ja  
`fs.auth_profiles.perms_writable` | kritisch | Andere können gespeicherte Modell-Anmeldedaten einschleusen oder ersetzen | Berechtigungen für `agents/<agentId>/agent/auth-profiles.json` | ja  
`fs.auth_profiles.perms_readable` | Warnung | Andere können API-Schlüssel und OAuth-Tokens lesen | Berechtigungen für `agents/<agentId>/agent/auth-profiles.json` | ja  
`fs.credentials_dir.perms_writable` | kritisch | Andere können den Pairing-/Anmeldedatenzustand des Kanals ändern | Dateisystemberechtigungen für `~/.openclaw/credentials` | ja  
`fs.credentials_dir.perms_readable` | Warnung | Andere können den Anmeldedatenzustand des Kanals lesen | Dateisystemberechtigungen für `~/.openclaw/credentials` | ja  
`fs.sessions_store.perms_readable` | Warnung | Andere können Sitzungstranskripte/-metadaten lesen | Berechtigungen des Sitzungsspeichers | ja  
`fs.log_file.perms_readable` | Warnung | Andere können redigierte, aber weiterhin sensible Logs lesen | Berechtigungen der Gateway-Logdatei | ja  
`fs.synced_dir` | Warnung | Zustand/Konfiguration in iCloud/Dropbox/Drive erweitert die Offenlegung von Tokens/Transkripten | Konfiguration/Zustand aus synchronisierten Ordnern verschieben | nein  
`gateway.bind_no_auth` | kritisch | Remote-Bind ohne gemeinsames Secret | `gateway.bind`, `gateway.auth.*` | nein  
`gateway.loopback_no_auth` | kritisch | Per Reverse Proxy angebundenes local loopback kann unauthentifiziert werden | `gateway.auth.*`, Proxy-Einrichtung | nein  
`gateway.trusted_proxies_missing` | Warnung | Reverse-Proxy-Header sind vorhanden, aber nicht vertrauenswürdig | `gateway.trustedProxies` | nein  
`gateway.http.no_auth` | Warnung/kritisch | Gateway-HTTP-APIs sind mit `auth.mode="none"` erreichbar | `gateway.auth.mode`, `gateway.http.endpoints.*` | nein  
`gateway.http.session_key_override_enabled` | Info | HTTP-API-Aufrufer können `sessionKey` überschreiben | `gateway.http.allowSessionKeyOverride` | nein  
`gateway.tools_invoke_http.dangerous_allow` | Warnung/kritisch | Aktiviert gefährliche Tools über die HTTP-API wieder | `gateway.tools.allow` | nein  
`gateway.nodes.allow_commands_dangerous` | Warnung/kritisch | Aktiviert weitreichende Node-Befehle (Kamera/Bildschirm/Kontakte/Kalender/SMS) | `gateway.nodes.allowCommands` | nein  
`gateway.nodes.deny_commands_ineffective` | Warnung | Musterartige Deny-Einträge stimmen nicht mit Shell-Text oder Gruppen überein | `gateway.nodes.denyCommands` | nein  
`gateway.tailscale_funnel` | kritisch | Exposition im öffentlichen Internet | `gateway.tailscale.mode` | nein  
`gateway.tailscale_serve` | Info | Tailnet-Exposition ist über Serve aktiviert | `gateway.tailscale.mode` | nein  
`gateway.control_ui.allowed_origins_required` | kritisch | Nicht-loopback Control UI ohne explizite Browser-Origin-Allowlist | `gateway.controlUi.allowedOrigins` | nein  
`gateway.control_ui.allowed_origins_wildcard` | Warnung/kritisch | `allowedOrigins=["*"]` deaktiviert die Browser-Origin-Allowlist | `gateway.controlUi.allowedOrigins` | nein  
`gateway.control_ui.host_header_origin_fallback` | Warnung/kritisch | Aktiviert Host-Header-Origin-Fallback (Abschwächung der DNS-Rebinding-Härtung) | `gateway.controlUi.dangerouslyAllowHostHeaderOriginFallback` | nein  
`gateway.control_ui.insecure_auth` | Warnung | Kompatibilitäts-Umschalter für unsichere Authentifizierung aktiviert | `gateway.controlUi.allowInsecureAuth` | nein  
`gateway.control_ui.device_auth_disabled` | kritisch | Deaktiviert die Geräteidentitätsprüfung | `gateway.controlUi.dangerouslyDisableDeviceAuth` | nein  
`gateway.real_ip_fallback_enabled` | Warnung/kritisch | Vertrauen in den `X-Real-IP`-Fallback kann Source-IP-Spoofing durch Proxy-Fehlkonfiguration ermöglichen | `gateway.allowRealIpFallback`, `gateway.trustedProxies` | nein  
`gateway.token_too_short` | Warnung | Ein kurzes gemeinsames Token ist leichter per Brute Force zu knacken | `gateway.auth.token` | nein  
`gateway.auth_no_rate_limit` | Warnung | Offen zugängliche Authentifizierung ohne Rate Limiting erhöht das Brute-Force-Risiko | `gateway.auth.rateLimit` | nein  
`gateway.trusted_proxy_auth` | kritisch | Die Proxy-Identität wird nun zur Authentifizierungsgrenze | `gateway.auth.mode="trusted-proxy"` | nein  
`gateway.trusted_proxy_no_proxies` | kritisch | Trusted-Proxy-Authentifizierung ohne vertrauenswürdige Proxy-IPs ist unsicher | `gateway.trustedProxies` | nein  
`gateway.trusted_proxy_no_user_header` | kritisch | Trusted-Proxy-Authentifizierung kann Benutzeridentität nicht sicher auflösen | `gateway.auth.trustedProxy.userHeader` | nein  
`gateway.trusted_proxy_no_allowlist` | Warnung | Trusted-Proxy-Authentifizierung akzeptiert jeden authentifizierten Upstream-Benutzer | `gateway.auth.trustedProxy.allowUsers` | nein  
`gateway.trusted_proxy_allow_loopback` | warn | Trusted-Proxy-Auth akzeptiert ausdrücklich erlaubte Loopback-Proxy-Quellen | `gateway.auth.trustedProxy.allowLoopback` | nein  
`gateway.probe_auth_secretref_unavailable` | warn | Deep Probe konnte Auth-SecretRefs in diesem Befehlspfad nicht auflösen | Auth-Quelle der Deep Probe / SecretRef-Verfügbarkeit | nein  
`gateway.probe_failed` | warn/critical | Live-Gateway-Probe fehlgeschlagen | Gateway-Erreichbarkeit/Auth | nein  
`discovery.mdns_full_mode` | warn/critical | Der mDNS-Vollmodus veröffentlicht `cliPath`/`sshPort`-Metadaten im lokalen Netzwerk | `discovery.mdns.mode`, `gateway.bind` | nein  
`config.insecure_or_dangerous_flags` | warn | Unsichere/gefährliche Debug-Flags aktiviert | mehrere Schlüssel (siehe Funddetails) | nein  
`config.secrets.gateway_password_in_config` | warn | Gateway-Passwort wird direkt in der Konfiguration gespeichert | `gateway.auth.password` | nein  
`config.secrets.hooks_token_in_config` | warn | Hook-Bearer-Token wird direkt in der Konfiguration gespeichert | `hooks.token` | nein  
`hooks.token_reuse_gateway_token` | critical | Hook-Ingress-Token entsperrt auch Gateway-Auth | `hooks.token`, `gateway.auth.token` | nein  
`hooks.token_too_short` | warn | Leichtere Brute-Force-Angriffe auf Hook-Ingress | `hooks.token` | nein  
`hooks.default_session_key_unset` | warn | Hook-Agent-Ausführungen fächern in generierte Sitzungen pro Anfrage auf | `hooks.defaultSessionKey` | nein  
`hooks.allowed_agent_ids_unrestricted` | warn/critical | Authentifizierte Hook-Aufrufer können an jeden konfigurierten Agent weiterleiten | `hooks.allowedAgentIds` | nein  
`hooks.request_session_key_enabled` | warn/critical | Externer Aufrufer kann `sessionKey` auswählen | `hooks.allowRequestSessionKey` | nein  
`hooks.request_session_key_prefixes_missing` | warn/critical | Keine Begrenzung für Formen externer Sitzungsschlüssel | `hooks.allowedSessionKeyPrefixes` | nein  
`hooks.path_root` | critical | Hook-Pfad ist `/`, wodurch Ingress leichter kollidieren oder fehlgeleitet werden kann | `hooks.path` | nein  
`hooks.installs_unpinned_npm_specs` | warn | Hook-Installationsdatensätze sind nicht auf unveränderliche npm-Spezifikationen gepinnt | Hook-Installationsmetadaten | nein  
`hooks.installs_missing_integrity` | warn | Hook-Installationsdatensätze enthalten keine Integritätsmetadaten | Hook-Installationsmetadaten | nein  
`hooks.installs_version_drift` | warn | Hook-Installationsdatensätze weichen von installierten Paketen ab | Hook-Installationsmetadaten | nein  
`logging.redact_off` | warn | Sensible Werte gelangen in Logs/Status | `logging.redactSensitive` | ja  
`browser.control_invalid_config` | warn | Browser-Control-Konfiguration ist vor der Laufzeit ungültig | `browser.*` | nein  
`browser.control_no_auth` | critical | Browser-Control ohne Token-/Passwort-Auth offengelegt | `gateway.auth.*` | nein  
`browser.remote_cdp_http` | warn | Remote-CDP über einfaches HTTP hat keine Transportverschlüsselung | Browser-Profil `cdpUrl` | nein  
`browser.remote_cdp_private_host` | warn | Remote-CDP zielt auf einen privaten/internen Host | Browser-Profil `cdpUrl`, `browser.ssrfPolicy.*` | nein  
`sandbox.docker_config_mode_off` | warn | Sandbox-Docker-Konfiguration vorhanden, aber inaktiv | `agents.*.sandbox.mode` | nein  
`sandbox.bind_mount_non_absolute` | warn | Relative Bind-Mounts können unvorhersehbar aufgelöst werden | `agents.*.sandbox.docker.binds[]` | nein  
`sandbox.dangerous_bind_mount` | critical | Sandbox-Bind-Mount zielt auf blockierte System-, Anmeldeinformations- oder Docker-Socket-Pfade | `agents.*.sandbox.docker.binds[]` | nein  
`sandbox.dangerous_network_mode` | critical | Sandbox-Docker-Netzwerk verwendet `host`\- oder `container:*`-Namespace-Join-Modus | `agents.*.sandbox.docker.network` | nein  
`sandbox.dangerous_seccomp_profile` | critical | Sandbox-seccomp-Profil schwächt Container-Isolation | `agents.*.sandbox.docker.securityOpt` | nein  
`sandbox.dangerous_apparmor_profile` | critical | Sandbox-AppArmor-Profil schwächt Container-Isolation | `agents.*.sandbox.docker.securityOpt` | nein  
`sandbox.browser_cdp_bridge_unrestricted` | warn | Sandbox-Browser-Bridge ist ohne Einschränkung des Quellbereichs offengelegt | `sandbox.browser.cdpSourceRange` | nein  
`sandbox.browser_container.non_loopback_publish` | critical | Vorhandener Browser-Container veröffentlicht CDP auf Nicht-Loopback-Schnittstellen | Veröffentlichungs-Konfiguration des Browser-Sandbox-Containers | nein  
`sandbox.browser_container.hash_label_missing` | warn | Vorhandener Browser-Container stammt aus der Zeit vor aktuellen Config-Hash-Labels | `openclaw sandbox recreate --browser --all` | nein  
`sandbox.browser_container.hash_epoch_stale` | warn | Vorhandener Browser-Container stammt aus der Zeit vor der aktuellen Browser-Konfigurationsepoche | `openclaw sandbox recreate --browser --all` | nein  
`tools.exec.host_sandbox_no_sandbox_defaults` | warn | `exec host=sandbox` schlägt geschlossen fehl, wenn die Sandbox deaktiviert ist | `tools.exec.host`, `agents.defaults.sandbox.mode` | nein  
`tools.exec.host_sandbox_no_sandbox_agents` | warn | Agent-spezifisches `exec host=sandbox` schlägt geschlossen fehl, wenn die Sandbox deaktiviert ist | `agents.list[].tools.exec.host`, `agents.list[].sandbox.mode` | nein  
`tools.exec.security_full_configured` | warn/critical | Host-Exec läuft mit `security="full"` | `tools.exec.security`, `agents.list[].tools.exec.security` | nein  
`tools.exec.fs_tools_disabled_but_exec_enabled` | warn | Dateisystem-Tool-Richtlinie macht Shell-Ausführung nicht schreibgeschützt | `tools.deny`, `agents.list[].tools.deny`, `agents.*.sandbox.workspaceAccess` | nein  
`tools.exec.auto_allow_skills_enabled` | warn | Exec-Genehmigungen vertrauen Skill-Bins implizit | `~/.openclaw/exec-approvals.json` | nein  
`tools.exec.allowlist_interpreter_without_strict_inline_eval` | warn | Interpreter-Allowlists erlauben Inline-Eval ohne erzwungene erneute Genehmigung | `tools.exec.strictInlineEval`, `agents.list[].tools.exec.strictInlineEval`, Exec-Genehmigungs-Allowlist | nein  
`tools.exec.safe_bins_interpreter_unprofiled` | warn | Interpreter-/Runtime-Bins in `safeBins` ohne explizite Profile erweitern Exec-Risiko | `tools.exec.safeBins`, `tools.exec.safeBinProfiles`, `agents.list[].tools.exec.*` | nein  
`tools.exec.safe_bins_broad_behavior` | warn | Tools mit breitem Verhalten in `safeBins` schwächen das Low-Risk-stdin-Filter-Vertrauensmodell | `tools.exec.safeBins`, `agents.list[].tools.exec.safeBins` | nein  
`tools.exec.safe_bin_trusted_dirs_risky` | warn | `safeBinTrustedDirs` enthält veränderbare oder riskante Verzeichnisse | `tools.exec.safeBinTrustedDirs`, `agents.list[].tools.exec.safeBinTrustedDirs` | nein  
`skills.workspace.symlink_escape` | warn | Workspace-`skills/**/SKILL.md` wird außerhalb der Workspace-Root aufgelöst (Symlink-Ketten-Drift) | Workspace-`skills/**`-Dateisystemzustand | nein  
`plugins.extensions_no_allowlist` | warn | Plugins sind ohne explizite Plugin-Zulassungsliste installiert | `plugins.allowlist` | nein  
`plugins.installs_unpinned_npm_specs` | warn | Plugin-Indexeinträge sind nicht auf unveränderliche npm-Spezifikationen festgelegt | Plugin-Installationsmetadaten | nein  
`plugins.installs_missing_integrity` | warn | Plugin-Indexeinträgen fehlen Integritätsmetadaten | Plugin-Installationsmetadaten | nein  
`plugins.installs_version_drift` | warn | Plugin-Indexeinträge weichen von installierten Paketen ab | Plugin-Installationsmetadaten | nein  
`plugins.code_safety` | warn/critical | Plugin-Code-Scan hat verdächtige oder gefährliche Muster gefunden | Plugin-Code / Installationsquelle | nein  
`plugins.code_safety.entry_path` | warn | Plugin-Einstiegspfad verweist auf versteckte Orte oder `node_modules`-Speicherorte | Plugin-Manifest `entry` | nein  
`plugins.code_safety.entry_escape` | critical | Plugin-Einstieg verlässt das Plugin-Verzeichnis | Plugin-Manifest `entry` | nein  
`plugins.code_safety.scan_failed` | warn | Plugin-Code-Scan konnte nicht abgeschlossen werden | Plugin-Pfad / Scan-Umgebung | nein  
`skills.code_safety` | warn/critical | Skill-Installer-Metadaten/-Code enthält verdächtige oder gefährliche Muster | Skill-Installationsquelle | nein  
`skills.code_safety.scan_failed` | warn | Skill-Code-Scan konnte nicht abgeschlossen werden | Skill-Scan-Umgebung | nein  
`security.exposure.open_channels_with_exec` | warn/critical | Geteilte/öffentliche Räume können Agents mit aktivierter Ausführung erreichen | `channels.*.dmPolicy`, `channels.*.groupPolicy`, `tools.exec.*`, `agents.list[].tools.exec.*` | nein  
`security.exposure.open_groups_with_elevated` | critical | Offene Gruppen + erweiterte Tools erzeugen Prompt-Injection-Pfade mit hoher Wirkung | `channels.*.groupPolicy`, `tools.elevated.*` | nein  
`security.exposure.open_groups_with_runtime_or_fs` | critical/warn | Offene Gruppen können Befehls-/Dateitools ohne Sandbox-/Workspace-Schutz erreichen | `channels.*.groupPolicy`, `tools.profile/deny`, `tools.fs.workspaceOnly`, `agents.*.sandbox.mode` | nein  
`security.trust_model.multi_user_heuristic` | warn | Config wirkt wie Mehrbenutzerbetrieb, während das Gateway-Vertrauensmodell auf persönliche Assistenz ausgelegt ist | Vertrauensgrenzen trennen oder Absicherung für geteilte Benutzer (`sandbox.mode`, Tool-Deny-/Workspace-Scoping) | nein  
`tools.profile_minimal_overridden` | warn | Agent-Overrides umgehen das globale Minimalprofil | `agents.list[].tools.profile` | nein  
`plugins.tools_reachable_permissive_policy` | warn | Plugin-Tools sind in permissiven Kontexten erreichbar | `tools.profile` \+ Tool-Allow-/Deny-Regeln | nein  
`models.legacy` | warn | Legacy-Modellfamilien sind noch konfiguriert | Modellauswahl | nein  
`models.weak_tier` | warn | Konfigurierte Modelle liegen unter den derzeit empfohlenen Stufen | Modellauswahl | nein  
`models.small_params` | critical/info | Kleine Modelle + unsichere Tool-Oberflächen erhöhen das Injection-Risiko | Modellwahl + Sandbox-/Tool-Richtlinie | nein  
`summary.attack_surface` | info | Zusammenfassende Übersicht über Auth-, Kanal-, Tool- und Exposure-Status | mehrere Schlüssel (siehe Detail zum Befund) | nein  
  
## Verwandt

  * [Sicherheit](</de/gateway/security>)
  * [Konfiguration](</de/gateway/configuration>)
  * [Authentifizierung über vertrauenswürdigen Proxy](</de/gateway/trusted-proxy-auth>)


Was this useful?YesNo