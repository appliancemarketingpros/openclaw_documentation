---
title: Tryby uprawnień
source_url: https://docs.openclaw.ai/pl/tools/permission-modes
scraped_at: 2026-06-29
---

CapabilitiesTools

Tryby uprawnień decydują, ile uprawnień ma agent, zanim będzie mógł uruchamiać polecenia hosta, zapisywać pliki lub poprosić backend harness o dodatkowy dostęp. Zacznij od `tools.exec.mode: "auto"`, gdy chcesz, aby OpenClaw najpierw używał list dozwolonych, a potem natywnej automatycznej recenzji Codex albo ścieżki zatwierdzenia przez człowieka dla nietrafień.

## Zalecana wartość domyślna

Użyj `auto` dla agentów kodujących, które potrzebują użytecznego dostępu do hosta bez zamieniania każdego nietrafienia w monit dla człowieka:

bashCopy code
[code]
    openclaw config set tools.exec.mode autoopenclaw approvals getopenclaw gateway restart
[/code]

Następnie zweryfikuj obowiązującą politykę:

bashCopy code
[code]
    openclaw exec-policy show
[/code]

W trybie `auto` OpenClaw uruchamia bezpośrednio deterministyczne dopasowania do listy dozwolonych. Nietrafienia wymagające zatwierdzenia najpierw przechodzą przez natywnego automatycznego recenzenta OpenClaw, a potem w razie potrzeby wracają do skonfigurowanej ścieżki zatwierdzenia przez człowieka.

## Tryby OpenClaw host exec

`tools.exec.mode` to znormalizowana powierzchnia polityki dla host `exec`.

Tryb | Zachowanie | Użyj, gdy  
---|---|---  
`deny` | Blokuje host exec. | Żadne polecenia hosta nie są dozwolone.  
`allowlist` | Uruchamia tylko polecenia z listy dozwolonych. | Masz znany, bezpieczny zestaw poleceń.  
`ask` | Uruchamia dopasowania do listy dozwolonych i pyta przy nietrafieniach. | Człowiek powinien recenzować nowe kształty poleceń.  
`auto` | Uruchamia dopasowania do listy dozwolonych, potem używa automatycznej recenzji. | Sesje kodowania potrzebują praktycznego, kontrolowanego dostępu.  
`full` | Uruchamia host exec bez monitów. | Ten zaufany host/sesja powinien pomijać bramki zatwierdzeń.  
  
Pełną politykę host exec, lokalny plik zatwierdzeń, schemat listy dozwolonych, bezpieczne binaria i zachowanie przekazywania opisuje sekcja [Zatwierdzenia exec](</pl/tools/exec-approvals>).

## Mapowanie Codex Guardian

Dla natywnych sesji serwera aplikacji Codex `tools.exec.mode: "auto"` mapuje się na zatwierdzenia recenzowane przez Codex Guardian, gdy pozwalają na to lokalne wymagania Codex. OpenClaw zwykle wysyła:

Pole Codex | Typowa wartość  
---|---  
`approvalPolicy` | `on-request`  
`approvalsReviewer` | `auto_review`  
`sandbox` | `workspace-write`  
  
W trybie `auto` OpenClaw nie zachowuje starszych niebezpiecznych nadpisań Codex, takich jak `approvalPolicy: "never"` czy `sandbox: "danger-full-access"`. Używaj `tools.exec.mode: "full"` tylko wtedy, gdy celowo chcesz postawy bez zatwierdzeń.

Konfigurację serwera aplikacji, kolejność uwierzytelniania i szczegóły natywnego środowiska wykonawczego Codex opisuje sekcja [harness Codex](</pl/plugins/codex-harness>).

## Uprawnienia harness ACPX

Sesje ACPX są nieinteraktywne, więc nie mogą kliknąć monitu uprawnień w TTY. ACPX używa oddzielnych ustawień na poziomie harness pod `plugins.entries.acpx.config`:

Ustawienie | Typowa wartość | Znaczenie  
---|---|---  
`permissionMode` | `approve-reads` | Automatycznie zatwierdza tylko odczyty.  
`permissionMode` | `approve-all` | Automatycznie zatwierdza zapisy i polecenia powłoki.  
`permissionMode` | `deny-all` | Odrzuca wszystkie monity uprawnień.  
`nonInteractivePermissions` | `fail` | Przerywa, gdy wymagany byłby monit.  
`nonInteractivePermissions` | `deny` | Odrzuca monit i kontynuuje, gdy to możliwe.  
  
Ustaw uprawnienia ACPX oddzielnie od zatwierdzeń OpenClaw exec:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions failopenclaw gateway restart
[/code]

Użyj `approve-all` jako odpowiednika awaryjnego obejścia ACPX dla sesji harness bez monitów. Szczegóły konfiguracji i tryby awarii opisuje sekcja [Konfiguracja agentów ACP](</pl/tools/acp-agents-setup#permission-configuration>).

## Wybór trybu

Cel | Konfiguracja  
---|---  
Całkowicie zablokować polecenia hosta | `tools.exec.mode: "deny"`  
Pozwalać uruchamiać tylko znane bezpieczne polecenia | `tools.exec.mode: "allowlist"`  
Pytać człowieka o każdy nowy kształt polecenia | `tools.exec.mode: "ask"`  
Użyć automatycznej recenzji Codex/OpenClaw przed ludźmi | `tools.exec.mode: "auto"`  
Całkowicie pominąć zatwierdzenia host exec | `tools.exec.mode: "full"` plus pasujący plik zatwierdzeń hosta  
Pozwolić nieinteraktywnym sesjom ACPX pisać/wykonywać | `plugins.entries.acpx.config.permissionMode: "approve-all"`  
  
Jeśli polecenie nadal wyświetla monit albo kończy się niepowodzeniem po zmianie trybu, sprawdź obie warstwy:

bashCopy code
[code]
    openclaw approvals getopenclaw exec-policy show
[/code]

Host exec używa bardziej rygorystycznego wyniku konfiguracji OpenClaw i lokalnego pliku zatwierdzeń hosta. Uprawnienia ACPX harness nie rozluźniają zatwierdzeń host exec, a zatwierdzenia host exec nie rozluźniają monitów ACPX harness.

## Powiązane

  * [Zatwierdzenia exec](</pl/tools/exec-approvals>)
  * [Zatwierdzenia exec - zaawansowane](</pl/tools/exec-approvals-advanced>)
  * [harness Codex](</pl/plugins/codex-harness>)
  * [Konfiguracja agentów ACP](</pl/tools/acp-agents-setup#permission-configuration>)


Was this useful?YesNo

Open issue