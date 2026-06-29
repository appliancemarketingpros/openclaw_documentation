---
title: Taksonomia dojrzałości
source_url: https://docs.openclaw.ai/pl/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Taksonomia dojrzałości

model stojący za kartą wyników

Powierzchnie > kategorie > możliwości > dowody.

50 powierzchni pogrupowanych w 4 rodziny, z każdą kategorią powiązaną z kanoniczną dokumentacją i identyfikatorami pokrycia QA.

Przeglądaj obszary produktu / Otwórz szczegółową taksonomię / [Zobacz wyniki](</pl/maturity/scorecard>)

## Jak czytać tę stronę

Powierzchnia to obszar produktu, taki jak środowisko uruchomieniowe Gateway, Discord lub aplikacja macOS. Każda powierzchnia zawiera kategorie, a każda kategoria zawiera kontrole na poziomie możliwości, które obejmują scenariusze QA. Użyj karty wyników do oceny na poziomie wydania; użyj tej strony, aby sprawdzić model, który za nią stoi.

## Poziomy dojrzałości

M0PlanowaneKierunek jest znany, ale nie istnieje obsługiwana ścieżka użytkownika.Awans: istnieją zgłoszenie projektowe, właściciel i docelowa powierzchnia.

M1EksperymentalneZaimplementowane z zastrzeżeniami, flagami, kompilacjami ze źródeł lub przepływami tylko dla maintainerów.Awans: maintainer może uruchomić scenariusz z bieżącej gałęzi main.

M2AlphaRzeczywiści użytkownicy mogą to wypróbować, ale należy spodziewać się zmian łamiących zgodność i niepełnego UX.Awans: udokumentowana konfiguracja, podstawowe testy, znane zastrzeżenia i co najmniej jeden dowód z rzeczywistego środowiska.

M3BetaIstnieje publiczna ścieżka, a główny przepływ pracy jest użyteczny z ograniczonymi zastrzeżeniami.Awans: dokumentacja instalacji/aktualizacji, testy regresji, runbook wsparcia i pomyślny dowód scenariusza w oczekiwanym środowisku.

M4StabilneZalecana ścieżka dla typowych użytkowników. Awarie są traktowane jako regresje.Awans: bramka wydania, ścieżka doctor/rozwiązywania problemów, obszerna dokumentacja i powtarzalne dowody z rzeczywistego użycia.

M5ClawesomeDopracowane, przyjemne, dobrze zinstrumentowane i konkurencyjne wobec najlepszego porównywalnego przepływu pracy.Awans: poziom Stabilne plus zaliczenie karty wyników użytkowników wśród reprezentatywnych użytkowników.

## Obszary produktu

### Rdzeń

CLI M4Stabilne7 obszarów - 90% ukończone Środowisko uruchomieniowe Gateway M4Stabilne13 obszarów - 89% ukończone Środowisko uruchomieniowe agenta M3Beta9 obszarów - 79% ukończone Sesja, pamięć i silnik kontekstu M3Beta9 obszarów - 79% ukończone Framework kanałów M3Beta8 obszarów - 79% ukończone Obserwowalność M3Beta5 obszarów - 79% ukończone Aplikacja webowa Gateway M3Beta6 obszarów - 79% ukończone Pluginy M3Beta9 obszarów - ukończono 79% Bezpieczeństwo, uwierzytelnianie, parowanie i sekrety M3Beta6 obszarów - ukończono 79% Automatyzacja: cron, hooki, zadania, odpytywanie M3Beta6 obszarów - ukończono 79% Rozumienie mediów i generowanie mediów M2Alfa6 obszarów - ukończono 68% Głos i rozmowa w czasie rzeczywistym M2Alfa6 obszarów - ukończono 68% TUI M2Alfa5 obszarów - ukończono 66% ClawHub M2Alfa4 obszary - ukończono 62% OpenClaw App SDK M2Alfa6 obszarów - ukończono 53%

### Platforma

Host Gateway dla Linuksa M4Stabilne5 obszarów - ukończono 89% Host Gateway dla macOS M4Stabilne7 obszarów - ukończono 88% Hosting Docker i Podman M3Beta4 obszary - ukończono 79% Windows przez WSL2 M3Beta6 obszarów - ukończono 79% Raspberry Pi i małe urządzenia z Linuksem M3Beta4 obszary - ukończono 79% Aplikacja towarzysząca dla macOS M3Beta8 obszarów - ukończono 78% Aplikacja na Androida M2Alfa7 obszarów - ukończono 66% Natywny Windows M2Alfa4 obszary - ukończono 66% Hosting Kubernetes M2Alfa4 obszary - ukończono 61% Aplikacja iOS M1Eksperymentalne8 obszarów - ukończono 44% Ścieżka instalacji Nix M1Eksperymentalne5 obszarów - ukończono 44% Powierzchnie towarzyszące watchOS M1Eksperymentalne5 obszarów - ukończono 44% Aplikacja towarzysząca Linux M0Planowane5 obszarów - ukończono 21% Natywna aplikacja towarzysząca Windows M0Planowane5 obszarów - ukończono 21%

### Kanał

Discord M4Stabilne6 obszarów - ukończono 87% Telegram M3Beta5 obszarów - ukończono 78% Slack M3Beta5 obszarów - ukończono 78% iMessage i BlueBubbles M3Beta5 obszarów - ukończono 78% WhatsApp M3Beta5 obszarów - ukończono 78% Matrix M2Alfa6 obszarów - ukończono 67% Google Chat M2Alfa5 obszarów - ukończono 66% Microsoft Teams M2Alfa5 obszarów - ukończono 66% Signal M2Alfa5 obszarów - ukończono 66% Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, kanały regionalne M2Alfa4 obszary - ukończono 58% Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alfa4 obszary - ukończono 54% Kanał połączeń głosowych M1Eksperymentalne5 obszarów - ukończono 44%

### Dostawca i narzędzie

Automatyzacja przeglądarki, exec i narzędzia sandbox M3Beta3 obszary - ukończono 79% Ścieżka dostawcy OpenAI i Codex M3Beta5 obszarów - ukończono 79% Narzędzia wyszukiwania w sieci M3Beta4 obszary - ukończono 79% Ścieżka dostawcy Anthropic M3Beta5 obszarów - ukończono 78% Ścieżka dostawcy Google M3Beta5 obszarów - ukończono 78% Ścieżka dostawcy OpenRouter M3Beta4 obszary - ukończono 78% Narzędzia do generowania obrazów, wideo i muzyki M2Alfa5 obszarów - ukończono 68% Lokalni dostawcy modeli: Ollama, vLLM, SGLang, LM Studio M2Alfa5 obszarów - ukończono 68% Rzadziej używani dostawcy hostowani M2Alfa3 obszary - ukończono 68%

## Szczegóły

### Rdzeń

CLI - M4 Stabilne - 7 obszarów

Standardowe ścieżki konfiguracji i naprawy są udokumentowane w dokumentacji instalacji, CLI i Gateway. Ścieżki specyficzne dla platformy Windows są śledzone w wierszach Windows przez WSL2 i Natywny Windows.

Pokrycie Eksperymentalne - 4%Jakość Stabilne - 83%Kompletność Stabilne - 90%Częściowe - 6

Konfiguracja CLI 6 możliwości / obsługiwane w LTS

Eksperymentalne17%

Stabilne89%

Stabilne90%

[Indeks](</pl/install>), [Instalator](</pl/install/installer>), [Node](</pl/install/node>), [Aktualizowanie](</pl/install/updating>)

Wdrażanie i konfiguracja uwierzytelniania 5 możliwości / obsługiwane w LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Wdrożenie](</pl/cli/onboard>), [Konfiguracja](</pl/cli/configure>), [Omówienie wdrożenia](</pl/start/onboarding-overview>)

Konfiguracja Plugin i kanałów 5 możliwości

Eksperymentalne0%

Beta75%

Stabilne89%

[Wdrożenie](</pl/cli/onboard>), [Pluginy](</pl/cli/plugins>), [Kanały](</pl/cli/channels>)

Zarządzanie usługą Gateway 5 możliwości / obsługiwane w LTS

Eksperymentalne14%

Stabilne87%

Stabilne90%

[Gateway](</pl/cli/gateway>), [Aktualizowanie](</pl/install/updating>), [Rozwiązywanie problemów](</pl/gateway/troubleshooting>)

Obserwowalność CLI 5 możliwości / obsługiwane w LTS

Eksperymentalne0%

Stabilne89%

Stabilne90%

[Stan](</pl/cli/status>), [Kondycja](</pl/cli/health>), [Dzienniki](</pl/cli/logs>), [Diagnostyka](</pl/gateway/diagnostics>)

Doctor 10 możliwości / obsługiwane w LTS

Eksperymentalne0%

Stabilne89%

Stabilne90%

[Doctor](</pl/cli/doctor>), [Doctor](</pl/gateway/doctor>), [Sekrety](</pl/gateway/secrets>), [Rozwiązywanie problemów](</pl/gateway/troubleshooting>)

Aktualizacje i uaktualnienia 5 możliwości / obsługiwane w LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Aktualizowanie](</pl/install/updating>), [Aktualizacja](</pl/cli/update>), [Rozwiązywanie problemów](</pl/gateway/troubleshooting>)

Środowisko uruchomieniowe Gateway - M4 Stabilne - 13 obszarów

Podstawowa architektura, uwierzytelnianie, parowanie, dokumentacja protokołu, dokumentacja daemona i runbooki CLI są szerokie i aktualne.

Pokrycie eksperymentalne - 6%Jakość stabilna - 81%Kompletność stabilna - 89%Częściowe - 12

Zatwierdzenia i zdalne wykonywanie 6 możliwości / obsługiwane w LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Protokół](</pl/gateway/protocol>), [Indeks](</pl/gateway/security>)

Interfejsy API HTTP 4 możliwości / obsługiwane w LTS

Eksperymentalne25%

Stabilne90%

Stabilne90%

[Indeks](</pl/gateway>), [Interfejs API HTTP OpenAI](</pl/gateway/openai-http-api>), [Interfejs API HTTP Openresponses](</pl/gateway/openresponses-http-api>), [Interfejs API HTTP wywoływania narzędzi](</pl/gateway/tools-invoke-http-api>), [Hooks](</pl/automation/hooks>), [Indeks](</pl/web>)

Hostowana powierzchnia webowa 4 możliwości / obsługiwane w LTS

Eksperymentalne0%

Stabilne89%

Stabilne90%

[Indeks](</pl/gateway>), [Architektura](</pl/concepts/architecture>), [Interfejs Control UI](</pl/web/control-ui>), [Webchat](</pl/web/webchat>), [Canvas](</pl/refactor/canvas>)

Interfejsy API RPC i zdarzenia Gateway 20 możliwości / obsługiwane w LTS

Eksperymentalne9%

Stabilne90%

Stabilne90%

[Protokół](</pl/gateway/protocol>), [Indeks](</pl/gateway>), [Architektura](</pl/concepts/architecture>)

Uwierzytelnianie urządzeń i parowanie 10 możliwości / obsługiwane w LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Protokół](</pl/gateway/protocol>), [Parowanie](</pl/gateway/pairing>), [Indeks](</pl/gateway/security>)

Dostęp sieciowy i wykrywanie 6 możliwości / obsługiwane w LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Indeks](</pl/gateway>), [Wykrywanie](</pl/gateway/discovery>), [Protokół](</pl/gateway/protocol>)

Węzły i zdalne możliwości 8 możliwości

Eksperymentalne0%

Beta75%

Stabilne89%

[Protokół](</pl/gateway/protocol>), [Architektura](</pl/concepts/architecture>), [Indeks](</pl/nodes>)

Kondycja, diagnostyka i naprawa 7 możliwości / obsługiwane w LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Indeks](</pl/gateway>), [Diagnostyka](</pl/gateway/diagnostics>), [Diagnostyka naprawcza](</pl/gateway/doctor>)

Zgodność protokołu 7 możliwości / obsługiwane w LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Protokół](</pl/gateway/protocol>), [Architektura](</pl/concepts/architecture>), [Typebox](</pl/concepts/typebox>), [Protokół Bridge](</pl/gateway/bridge-protocol>)

Role i uprawnienia 5 możliwości / obsługiwane w LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Protokół](</pl/gateway/protocol>), [Indeks](</pl/gateway/security>)

Cykl życia Gateway 7 możliwości / obsługiwane w LTS

Eksperymentalne33%

Stabilne90%

Stabilne90%

[Indeks](</pl/gateway>), [Architektura](</pl/concepts/architecture>)

Mechanizmy kontroli bezpieczeństwa 6 możliwości / obsługiwane w LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Indeks](</pl/gateway/security>), [Protokół](</pl/gateway/protocol>), [Wykrywanie](</pl/gateway/discovery>)

Połączenie WebSocket 8 możliwości / obsługiwane w LTS

Eksperymentalne13%

Stabilne90%

Stabilne90%

[Protokół](</pl/gateway/protocol>), [Architektura](</pl/concepts/architecture>)

Środowisko uruchomieniowe agenta - M3 Beta - 9 obszarów

Główna pętla, modele, routing dostawców i strumieniowanie narzędzi są pełnoprawnymi obszarami, ale zachowanie dostawców zmienia się co tydzień i wymaga dowodu scenariuszowego dla każdego wydania.

Pokrycie eksperymentalne - 33%Jakość Beta - 78%Kompletność Beta - 79%Częściowe - 6

Wykonywanie tur agenta 3 możliwości / obsługiwane w LTS

Eksperymentalne29%

Beta79%

Beta79%

[Pętla agenta](</pl/concepts/agent-loop>), [Agent](</pl/cli/agent>), [Środowiska uruchomieniowe agenta](</pl/concepts/agent-runtimes>)

Zewnętrzne środowiska uruchomieniowe i podagenci 4 możliwości

Eksperymentalne30%

Beta79%

Beta79%

[Środowiska uruchomieniowe agenta](</pl/concepts/agent-runtimes>), [Anthropic](</pl/providers/anthropic>), [Google](</pl/providers/google>), [Podagenci](</pl/tools/subagents>)

Wykonywanie u hostowanych dostawców 5 możliwości / obsługiwane w LTS

Eksperymentalne20%

Beta79%

Beta79%

[Openai](</pl/providers/openai>), [Anthropic](</pl/providers/anthropic>), [Google](</pl/providers/google>), [Modele](</pl/concepts/models>)

Lokalni i samodzielnie hostowani dostawcy 5 możliwości

Eksperymentalne0%

Alfa68%

Beta79%

[Ollama](</pl/providers/ollama>), [Modele](</pl/concepts/models>), [Agent](</pl/cli/agent>)

Wybór modelu i środowiska uruchomieniowego 4 możliwości / obsługiwane w LTS

Eksperymentalne25%

Beta79%

Beta79%

[Modele](</pl/concepts/models>), [Modele](</pl/cli/models>), [Openai](</pl/providers/openai>), [Środowiska uruchomieniowe agenta](</pl/concepts/agent-runtimes>)

Uwierzytelnianie dostawcy 10 możliwości / obsługiwane w LTS

Eksperymentalne24%

Beta79%

Beta79%

[Modele](</pl/concepts/models>), [Agent](</pl/cli/agent>), [Modele](</pl/cli/models>), [Openai](</pl/providers/openai>), [Anthropic](</pl/providers/anthropic>), [Google](</pl/providers/google>), [Podagenci](</pl/tools/subagents>)

Streaming i postęp 2 możliwości

Alfa56%

Beta79%

Beta79%

[Streaming](</pl/concepts/streaming>), [Pętla agenta](</pl/concepts/agent-loop>)

Wywołania narzędzi i obsługa odpowiedzi 3 możliwości / obsługiwane w LTS

Alfa65%

Beta79%

Beta79%

[Pętla agenta](</pl/concepts/agent-loop>), [Ollama](</pl/providers/ollama>)

Kontrole wykonywania narzędzi 6 możliwości / obsługiwane przez LTS

Alfa50%

Beta79%

Beta79%

[Piaskownica a zasady narzędzi a tryb podwyższony](</pl/gateway/sandbox-vs-tool-policy-vs-elevated>), [Pętla agenta](</pl/concepts/agent-loop>), [Podagenci](</pl/tools/subagents>)

Sesja, pamięć i silnik kontekstu - M3 Beta - 9 obszarów

Dobra dokumentacja i aktywna implementacja. Dojrzałość zależy od trwałości transkrypcji, jakości Compaction oraz parytetu między klientami.

Pokrycie Eksperymentalne - 30%Jakość Beta - 77%Kompletność Beta - 79%Częściowe - 6

Zarządzanie sesjami CLI i transkrypcjami 2 możliwości / z obsługą LTS

Eksperymentalne0%

Alfa68%

Beta79%

[Sesja](</pl/concepts/session>), [Compaction zarządzania sesjami](</pl/reference/session-management-compaction>), [Sesje](</pl/cli/sessions>)

Zarządzanie tokenami 3 możliwości / z obsługą LTS

Eksperymentalne20%

Beta79%

Beta79%

[Compaction](</pl/concepts/compaction>), [Kontekst](</pl/concepts/context>), [Compaction zarządzania sesjami](</pl/reference/session-management-compaction>)

Silnik kontekstu 2 możliwości / z obsługą LTS

Alfa57%

Beta79%

Beta79%

[Kontekst](</pl/concepts/context>), [Silnik kontekstu](</pl/concepts/context-engine>), [Środowisko testowe silnika kontekstu Codex](</pl/plan/codex-context-engine-harness>)

Historia i parytet sesji między klientami 2 możliwości

Eksperymentalne40%

Beta79%

Beta79%

[Czat webowy](</pl/web/webchat>), [Android](</pl/platforms/android>), [Routing kanałów](</pl/channels/channel-routing>)

Diagnostyka, konserwacja i odzyskiwanie 3 możliwości

Eksperymentalne40%

Beta79%

Beta79%

[Diagnostyka](</pl/gateway/diagnostics>), [Compaction zarządzania sesjami](</pl/reference/session-management-compaction>), [Flagi](</pl/diagnostics/flags>)

Podstawowe prompty i kontekst 2 możliwości / z obsługą LTS

Eksperymentalne38%

Beta79%

Beta79%

[Kontekst](</pl/concepts/context>), [Higiena transkrypcji](</pl/reference/transcript-hygiene>), [Discord](</pl/channels/discord>)

Pamięć 5 możliwości

Eksperymentalne46%

Beta79%

Beta79%

[Konfiguracja pamięci](</pl/reference/memory-config>), [Qmd pamięci](</pl/concepts/memory-qmd>), [Pamięć](</pl/concepts/memory>), [Discord](</pl/channels/discord>)

Routing sesji 2 możliwości / z obsługą LTS

Eksperymentalne25%

Beta79%

Beta79%

[Sesja](</pl/concepts/session>), [Routing kanałów](</pl/channels/channel-routing>), [Discord](</pl/channels/discord>)

Trwałość transkrypcji 2 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa68%

Beta79%

[Compaction zarządzania sesją](</pl/reference/session-management-compaction>), [Higiena transkrypcji](</pl/reference/transcript-hygiene>)

Framework kanałów - M3 Beta - 8 obszarów

Wiele kanałów współdzieli kontrakty dostarczania i routingu Gateway, ale zachowanie kanałów różni się zależnie od ograniczeń nadrzędnego API i zasad konta.

Pokrycie Eksperymentalne - 13%Jakość Beta - 76%Kompletność Beta - 79%Częściowe - 5

Akcje kanałów, polecenia i zatwierdzenia 5 możliwości

Eksperymentalne0%

Beta79%

Beta79%

[Grupy](</pl/channels/groups>), [Discord](</pl/channels/discord>), [Google Chat](</pl/channels/googlechat>), [Signal](</pl/channels/signal>), [Matrix](</pl/channels/matrix>)

Konfiguracja kanałów 5 możliwości / obsługiwane w LTS

Eksperymentalne14%

Beta79%

Beta79%

[Indeks](</pl/channels>), [Parowanie](</pl/channels/pairing>), [Rozwiązywanie problemów](</pl/channels/troubleshooting>), [Plugin kanałów SDK](</pl/plugins/sdk-channel-plugins>)

Wątki grupowe i zachowanie pomieszczeń w tle 5 możliwości

Eksperymentalne36%

Beta79%

Beta79%

[Grupy](</pl/channels/groups>), [Wiadomości grupowe](</pl/channels/group-messages>), [Zdarzenia pomieszczeń w tle](</pl/channels/ambient-room-events>), [Grupy nadawcze](</pl/channels/broadcast-groups>), [Discord](</pl/channels/discord>)

Dostęp przychodzący i bramki tożsamości 5 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa68%

Beta79%

[Grupy dostępu](</pl/channels/access-groups>), [Grupy](</pl/channels/groups>), [Discord](</pl/channels/discord>), [LINE](</pl/channels/line>)

Załączniki multimedialne i rozbudowane dane kanałów 4 możliwości

Eksperymentalne0%

Alfa68%

Beta79%

[LINE](</pl/channels/line>), [Signal](</pl/channels/signal>), [Google Chat](</pl/channels/googlechat>), [Matrix](</pl/channels/matrix>), [Discord](</pl/channels/discord>)

Dostarczanie wychodzące i potok odpowiedzi 4 możliwości / obsługiwane w LTS

Eksperymentalne38%

Beta79%

Beta79%

[Grupy](</pl/channels/groups>), [Zdarzenia pomieszczeń w tle](</pl/channels/ambient-room-events>), [Discord](</pl/channels/discord>), [Matrix](</pl/channels/matrix>), [Kanały konfiguracji](</pl/gateway/config-channels>)

Trasowanie i dostarczanie rozmów 10 możliwości / obsługiwane w LTS

Eksperymentalne19%

Beta79%

Beta79%

[Trasowanie kanałów](</pl/channels/channel-routing>), [Grupy](</pl/channels/groups>), [Discord](</pl/channels/discord>), [Matrix](</pl/channels/matrix>), [Rozwiązywanie problemów](</pl/channels/troubleshooting>), [Dokumentacja konfiguracji](</pl/gateway/configuration-reference>)

Stan, kondycja i kontrolki operatora 4 możliwości / obsługiwane w LTS

Eksperymentalne0%

Beta79%

Beta79%

[Kondycja](</pl/gateway/health>), [Dokumentacja konfiguracji](</pl/gateway/configuration-reference>), [Rozwiązywanie problemów](</pl/channels/troubleshooting>), [Discord](</pl/channels/discord>)

Observability - M3 Beta - 5 areas

Dokumentacja OTel, Prometheus, logowania i diagnostyki istnieje. Wymaga publicznego przeglądu dojrzałości „na co operatorzy powinni patrzeć w pierwszej kolejności”.

Pokrycie Eksperymentalne - 18%Jakość Beta - 75%Kompletność Beta - 79%Częściowe - 3

Stan i naprawa 12 możliwości / z obsługą LTS

Eksperymentalne28%

Beta79%

Beta79%

[Stan](</pl/gateway/health>), [Telegram](</pl/channels/telegram>), [Doctor](</pl/cli/doctor>), [Doctor](</pl/gateway/doctor>), [Podścieżki SDK](</pl/plugins/sdk-subpaths>), [Stan](</pl/cli/health>), [Protokół](</pl/gateway/protocol>)

Rejestrowanie 5 możliwości / z obsługą LTS

Eksperymentalne0%

Alpha68%

Beta79%

[Rejestrowanie](</pl/logging>), [Rejestrowanie](</pl/gateway/logging>), [Logi](</pl/cli/logs>)

Zbieranie diagnostyki 8 możliwości

Eksperymentalne30%

Beta79%

Beta79%

[Diagnostyka](</pl/gateway/diagnostics>), [Stan](</pl/gateway/health>), [Harness Codex](</pl/plugins/codex-harness>), [Protokół](</pl/gateway/protocol>)

Eksport telemetrii 13 możliwości

Eksperymentalne33%

Beta79%

Beta79%

[Hooki](</pl/plugins/hooks>), [Opentelemetry](</pl/gateway/opentelemetry>), [Rejestrowanie](</pl/logging>), [Podścieżki SDK](</pl/plugins/sdk-subpaths>), [Diagnostyka Otel](</pl/plugins/reference/diagnostics-otel>), [Prometheus](</pl/gateway/prometheus>), [Diagnostyka Prometheus](</pl/plugins/reference/diagnostics-prometheus>)

Diagnostyka sesji 4 możliwości / z obsługą LTS

Eksperymentalne0%

Alpha68%

Beta79%

[Opentelemetry](</pl/gateway/opentelemetry>), [Prometheus](</pl/gateway/prometheus>), [Diagnostyka](</pl/gateway/diagnostics>), [Protokół](</pl/gateway/protocol>)

Aplikacja webowa Gateway - M3 Beta - 6 obszarów

Web UI jest udokumentowany z przepływami parowania, czatu, PWA, Talk, push oraz zdalnego Gateway. Awansuj po kartach wyników międzyprzeglądarkowych i mobilnego PWA.

Pokrycie Eksperymentalne - 4%Jakość Beta - 74%Kompletność Beta - 79%Brak

Rozmowa w czasie rzeczywistym w przeglądarce 5 możliwości

Eksperymentalne0%

Alfa68%

Beta79%

[Interfejs sterowania](</pl/web/control-ui>), [Protokół](</pl/gateway/protocol>), [Rozmowa](</pl/nodes/talk>)

Dostęp i zaufanie w przeglądarce 5 możliwości

Eksperymentalne0%

Alfa68%

Beta79%

[Interfejs sterowania](</pl/web/control-ui>), [Panel](</pl/web/dashboard>), [Tailscale](</pl/gateway/tailscale>), [Dostęp zdalny](</pl/gateway/remote>)

Konfiguracja 5 możliwości

Eksperymentalne0%

Alfa68%

Beta79%

[Interfejs sterowania](</pl/web/control-ui>), [Konfiguracja](</pl/gateway/configuration>)

Interfejs przeglądarkowy 10 możliwości

Eksperymentalne8%

Beta79%

Beta79%

[Interfejs sterowania](</pl/web/control-ui>), [Indeks](</pl/web>), [Panel](</pl/web/dashboard>), [Protokół](</pl/gateway/protocol>)

Konwersacje WebChat 15 możliwości

Eksperymentalne10%

Beta79%

Beta79%

[Interfejs sterowania](</pl/web/control-ui>), [Czat webowy](</pl/web/webchat>), [Pierwsze kroki](</pl/start/getting-started>), [Routing kanałów](</pl/channels/channel-routing>), [Bezpieczne operacje na plikach](</pl/gateway/security/secure-file-operations>)

Konsola operatora 10 możliwości

Eksperymentalne8%

Beta79%

Beta79%

[Interfejs sterowania](</pl/web/control-ui>), [Stan](</pl/gateway/health>), [Protokół](</pl/gateway/protocol>), [Panel](</pl/web/dashboard>)

Pluginy - M3 Beta - 9 obszarów

Istnieje szeroka dokumentacja i mocne wewnętrzne dowody działania środowiska wykonawczego w obszarach manifestów, wykrywania, ładowania, architektury dostawców/narzędzi oraz granic zatwierdzania. Utrzymaj wiersz na poziomie beta, dopóki publiczne API SDK, podścieżki i dowody dystrybucji zewnętrznej nie będą mocniejsze.

Zakres Eksperymentalne - 12%Jakość Beta - 72%Kompletność Beta - 79%Częściowe - 7

Tworzenie i pakowanie Pluginów 8 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa68%

Beta79%

[Budowanie Pluginów](</pl/plugins/building-plugins>), [Przegląd SDK](</pl/plugins/sdk-overview>), [Punkty wejścia SDK](</pl/plugins/sdk-entrypoints>), [Podścieżki SDK](</pl/plugins/sdk-subpaths>), [Manifest](</pl/plugins/manifest>), [Referencje](</pl/plugins/reference>)

Dołączone Pluginy 5 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa68%

Beta79%

[Spis Pluginów](</pl/plugins/plugin-inventory>), [Pluginy](</pl/cli/plugins>), [Wewnętrzna architektura](</pl/plugins/architecture-internals>)

Plugin Canvas 6 możliwości

Eksperymentalne0%

Alfa68%

Beta79%

[Canvas](</pl/plugins/reference/canvas>), [Canvas](</pl/refactor/canvas>), [Dokumentacja konfiguracji](</pl/gateway/configuration-reference>)

Instalowanie i uruchamianie Pluginów 6 możliwości / obsługiwane w LTS

Eksperymentalne35%

Beta79%

Beta79%

[Architektura](</pl/plugins/architecture>), [Wewnętrzna architektura](</pl/plugins/architecture-internals>), [Pluginy](</pl/cli/plugins>)

Pluginy kanałów 5 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa68%

Beta79%

[Pluginy kanałów SDK](</pl/plugins/sdk-channel-plugins>), [Kanał przychodzący SDK](</pl/plugins/sdk-channel-inbound>), [Kanał wychodzący SDK](</pl/plugins/sdk-channel-outbound>)

Pluginy dostawców i narzędzi 6 możliwości / obsługiwane w LTS

Eksperymentalne43%

Beta79%

Beta79%

[Pluginy dostawców SDK](</pl/plugins/sdk-provider-plugins>), [Pluginy narzędzi](</pl/plugins/tool-plugins>), [Dodawanie możliwości](</pl/plugins/adding-capabilities>)

Zatwierdzenia Pluginów 6 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa68%

Beta79%

[Żądania uprawnień Pluginów](</pl/plugins/plugin-permission-requests>), [Zatwierdzenia Exec](</pl/tools/exec-approvals>), [Pluginy kanałów SDK](</pl/plugins/sdk-channel-plugins>)

Publikowanie Pluginów 6 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa68%

Beta79%

[Pluginy](</pl/cli/plugins>), [Zgodność](</pl/plugins/compatibility>), [Publikowanie](</pl/clawhub/publishing>)

Testowanie Pluginów 6 możliwości

Eksperymentalne27%

Beta79%

Beta79%

[Testowanie SDK](</pl/plugins/sdk-testing>), [Konfiguracja SDK](</pl/plugins/sdk-setup>), [Harness Codex](</pl/plugins/codex-harness>)

Bezpieczeństwo, uwierzytelnianie, parowanie i sekrety - M3 Beta - 6 obszarów

Istnieje dobra dokumentacja i powierzchnie wzmacniania zabezpieczeń. Promuj po tym, jak regularne scenariusze aktualizacji i zabezpieczeń wykażą brak regresji konfiguracji.

Pokrycie Experimental - 16%Jakość Beta - 72%Kompletność Beta - 79%Częściowe - 5

Zasady zatwierdzania i zabezpieczenia narzędzi 2 możliwości / obsługiwane w LTS

Alpha50%

Beta79%

Beta79%

[Zatwierdzenia Exec](</pl/tools/exec-approvals>), [Zatwierdzenia](</pl/cli/approvals>), [Żądania uprawnień Plugin](</pl/plugins/plugin-permission-requests>), [Kontrole audytu](</pl/gateway/security/audit-checks>)

Uwierzytelnianie Gateway i dostęp zdalny 9 możliwości / obsługiwane w LTS

Experimental0%

Alpha68%

Beta79%

[Indeks](</pl/gateway/security>), [Runbook ekspozycji](</pl/gateway/security/exposure-runbook>), [Uwierzytelnianie zaufanego proxy](</pl/gateway/trusted-proxy-auth>), [Tailscale](</pl/gateway/tailscale>), [Dostęp zdalny](</pl/gateway/remote>), [Dokumentacja konfiguracji](</pl/gateway/configuration-reference>), [Gateway](</pl/cli/gateway>), [Doctor](</pl/cli/doctor>), [Interfejs Control UI](</pl/web/control-ui>), [Sterowanie przeglądarką](</pl/tools/browser-control>), [Kontrole audytu](</pl/gateway/security/audit-checks>)

Kontrola dostępu kanału 3 możliwości / obsługiwane w LTS

Experimental0%

Alpha68%

Beta79%

[Parowanie](</pl/channels/pairing>), [Telegram](</pl/channels/telegram>), [Grupy dostępu](</pl/channels/access-groups>), [Kontrole audytu](</pl/gateway/security/audit-checks>)

Parowanie urządzeń i Node 11 możliwości / obsługiwane w LTS

Experimental0%

Alpha68%

Beta79%

[Protokół](</pl/gateway/protocol>), [Urządzenia](</pl/cli/devices>), [Parowanie](</pl/channels/pairing>), [Parowanie](</pl/gateway/pairing>), [Zakresy operatora](</pl/gateway/operator-scopes>), [Interfejs Control UI](</pl/web/control-ui>), [Webchat](</pl/web/webchat>), [Zatwierdzenia](</pl/cli/approvals>)

Zaufanie do Plugin 2 możliwości

Experimental0%

Alpha68%

Beta79%

[Manifest](</pl/plugins/manifest>), [Żądania uprawnień Plugin](</pl/plugins/plugin-permission-requests>), [Zarządzanie Plugin](</pl/plugins/manage-plugins>), [Kontrole audytu](</pl/gateway/security/audit-checks>)

Higiena poświadczeń i sekretów 5 możliwości / obsługiwane w LTS

Experimental46%

Beta79%

Beta79%

[Uwierzytelnianie](</pl/gateway/authentication>), [Modele](</pl/cli/models>), [Openai](</pl/providers/openai>), [Oauth](</pl/concepts/oauth>), [Sekrety](</pl/gateway/secrets>), [Sekrety](</pl/cli/secrets>), [Powierzchnia poświadczeń Secretref](</pl/reference/secretref-credential-surface>), [Kontrole audytu](</pl/gateway/security/audit-checks>)

Automatyzacja: Cron, hooki, zadania, odpytywanie - M3 Beta - 6 obszarów

Udokumentowane i używalne, ale dowód scenariuszowy powinien obejmować dostarczanie bez nadzoru, ponawianie prób i widoczność awarii.

Pokrycie Experimental - 2%Jakość Beta - 72%Kompletność Beta - 79%Brak

Zadania Cron 15 możliwości

Eksperymentalne0%

Beta79%

Beta79%

[Zadania Cron](</pl/automation/cron-jobs>), [Cron](</pl/cli/cron>), [Protokół](</pl/gateway/protocol>), [Zadania](</pl/automation/tasks>), [Discord](</pl/channels/discord>)

Przyjmowanie zdarzeń 15 możliwości

Eksperymentalne0%

Alpha68%

Beta79%

[Telegram](</pl/channels/telegram>), [Zalo](</pl/channels/zalo>), [Rozwiązywanie problemów](</pl/channels/troubleshooting>), [iMessage z Bluebubbles](</pl/channels/imessage-from-bluebubbles>), [Integracja Gmail Pubsub](</pl/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</pl/automation/cron-jobs>), [Webhooki](</pl/cli/webhooks>), [Webhooki](</pl/automation/cron-jobs#webhooks>), [Webhook](</pl/automation/cron-jobs>)

Hooki automatyzacji 11 możliwości

Eksperymentalne0%

Alpha68%

Beta79%

[Hooki](</pl/automation/hooks>), [Hooki](</pl/cli/hooks>), [Hooki](</pl/plugins/hooks>), [Żądania uprawnień Plugin](</pl/plugins/plugin-permission-requests>), [Ścieżki podrzędne SDK](</pl/plugins/sdk-subpaths>)

Zadania i przepływy w tle 10 możliwości

Eksperymentalne0%

Alpha68%

Beta79%

[Zadania](</pl/automation/tasks>), [Indeks](</pl/automation>), [Zadania](</pl/cli/tasks>), [TaskFlow](</pl/automation/taskflow>), [Środowisko uruchomieniowe SDK](</pl/plugins/sdk-runtime>)

Heartbeat 5 możliwości

Eksperymentalne14%

Beta79%

Beta79%

[Indeks](</pl/automation>), [Heartbeat](</pl/gateway/heartbeat>), [Zobowiązania](</pl/concepts/commitments>)

Sterowanie odpytywaniem 10 możliwości

Eksperymentalne0%

Alpha68%

Beta79%

[Odpytywanie](</pl/cli/message>), [Wiadomość](</pl/cli/message>), [Telegram](</pl/channels/telegram>), [Msteams](</pl/channels/msteams>), [Proces w tle](</pl/gateway/background-process>)

Rozumienie multimediów i generowanie multimediów - M2 Alpha - 6 obszarów

Istnieje szeroki zakres możliwości, ale różnice między dostawcami, limity plików i parytet węzłów/aplikacji sprawiają, że nie jest to jeszcze stabilne.

Pokrycie Eksperymentalne - 2%Jakość Alpha - 64%Kompletność Alpha - 68%Brak

Pobieranie i dostęp do multimediów 8 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Przegląd multimediów](</pl/tools/media-overview>), [Rozumienie multimediów](</pl/nodes/media-understanding>), [Bezpieczne operacje na plikach](</pl/gateway/security/secure-file-operations>), [PDF](</pl/tools/pdf>), [Generowanie obrazów](</pl/tools/image-generation>), [QR](</pl/cli/qr>), [LINE](</pl/channels/line>), [WhatsApp](</pl/channels/whatsapp>)

Obsługa multimediów w kanałach 5 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Obrazy](</pl/nodes/images>), [Przegląd multimediów](</pl/tools/media-overview>), [Discord](</pl/channels/discord>)

Konfiguracja multimediów 1 możliwość

Eksperymentalne0%

Alpha61%

Alpha68%

[Przegląd multimediów](</pl/tools/media-overview>), [Generowanie obrazów](</pl/tools/image-generation>), [Manifest](</pl/plugins/manifest>), [Środowisko testowe Codex](</pl/plugins/codex-harness>)

Dostarczanie zamiany tekstu na mowę 2 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[TTS](</pl/tools/tts>), [Przegląd multimediów](</pl/tools/media-overview>), [Discord](</pl/channels/discord>)

Rozumienie multimediów 12 możliwości

Eksperymentalne7%

Alpha69%

Alpha69%

[Dźwięk](</pl/nodes/audio>), [Rozumienie multimediów](</pl/nodes/media-understanding>), [Przegląd multimediów](</pl/tools/media-overview>), [WhatsApp](</pl/channels/whatsapp>), [Obrazy](</pl/nodes/images>), [Infer](</pl/cli/infer>), [PDF](</pl/tools/pdf>)

Generowanie multimediów 17 możliwości

Eksperymentalne5%

Alpha69%

Alpha69%

[Generowanie obrazów](</pl/tools/image-generation>), [Przegląd multimediów](</pl/tools/media-overview>), [Skills](</pl/tools/skills>), [Generowanie muzyki](</pl/tools/music-generation>), [Generowanie wideo](</pl/tools/video-generation>)

Głos i rozmowa w czasie rzeczywistym - M2 Alpha - 6 obszarów

W Control UI, aplikacjach i u dostawców istnieje wiele implementacji. Przed wersją beta potrzebne są karty oceny opóźnień, trybów awarii i konfiguracji.

Zakres Eksperymentalne - 0%Jakość Alpha - 61%Kompletność Alpha - 68%Brak

Dostawcy rozmów 7 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Openai](</pl/providers/openai>), [Google](</pl/providers/google>), [Pluginy dostawców SDK](</pl/plugins/sdk-provider-plugins>), [Rozmowa](</pl/nodes/talk>), [Interfejs sterowania](</pl/web/control-ui>)

Sesje rozmów w czasie rzeczywistym 11 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Rozmowa](</pl/nodes/talk>), [Interfejs sterowania](</pl/web/control-ui>)

Mowa i transkrypcja 5 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Rozmowa](</pl/nodes/talk>), [Openai](</pl/providers/openai>), [Google](</pl/providers/google>)

Rozmowa w aplikacji natywnej 4 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Rozmowa](</pl/nodes/talk>), [Voicewake](</pl/platforms/mac/voicewake>)

Wybudzanie głosowe i routing 4 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Voicewake](</pl/nodes/voicewake>), [Voicewake](</pl/platforms/mac/voicewake>), [Nakładka głosowa](</pl/platforms/mac/voice-overlay>)

Obserwowalność rozmów 5 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Interfejs sterowania](</pl/web/control-ui>), [Nakładka głosowa](</pl/platforms/mac/voice-overlay>), [Rozmowa](</pl/nodes/talk>)

TUI - M2 Alpha - 5 obszarów

Obecne w dokumentacji i źródle, ale mniej widoczne jako podstawowy przepływ pracy użytkownika. Wymaga jednoznacznej definicji scenariusza.

Pokrycie Eksperymentalne - 0%Jakość Alpha - 59%Kompletność Alpha - 66%Brak

Tryby działania 14 możliwości

Eksperymentalny0%

Alfa59%

Alfa66%

[TUI](</pl/cli/tui>), [TUI](</pl/web/tui>), [Indeks](</pl/cli>)

Dane wejściowe i polecenia 8 możliwości

Eksperymentalny0%

Alfa59%

Alfa66%

[TUI](</pl/web/tui>)

Zarządzanie sesjami 3 możliwości

Eksperymentalny0%

Alfa59%

Alfa66%

[TUI](</pl/web/tui>), [Sesje](</pl/cli/sessions>)

Lokalne wykonywanie powłoki 4 możliwości

Eksperymentalny0%

Alfa59%

Alfa66%

[TUI](</pl/web/tui>), [TUI](</pl/cli/tui>)

Renderowanie i bezpieczeństwo danych wyjściowych 4 możliwości

Eksperymentalny0%

Alfa59%

Alfa66%

[TUI](</pl/web/tui>), [QR](</pl/cli/qr>), [Logi](</pl/cli/logs>), [Uzupełnianie](</pl/cli/completion>)

ClawHub - M2 Alfa - 4 obszary

Publiczna dokumentacja i koncepcja ekosystemu istnieją. Potrzebne są karty ocen instalacji, zaufania, aktualizacji, wycofywania zmian i zgodności.

Pokrycie eksperymentalne - 0%Jakość Alfa - 58%Kompletność Alfa - 62%Brak

Publikowanie 7 możliwości

Eksperymentalne0%

Alfa54%

Alfa55%

[Publikowanie](</pl/clawhub/publishing>), [Tworzenie Skills](</pl/tools/creating-skills>), [Społeczność](</pl/plugins/community>)

Odkrywanie katalogu 5 możliwości

Eksperymentalne0%

Alfa61%

Alfa68%

[Plugin](</pl/tools/plugin>), [Pluginy](</pl/cli/plugins>), [Skills](</pl/cli/skills>), [Skills](</pl/tools/skills>), [Społeczność](</pl/plugins/community>)

Zgodność i zaufanie 12 możliwości

Eksperymentalne0%

Alfa55%

Alfa56%

[Plugin](</pl/tools/plugin>), [Pluginy](</pl/cli/plugins>), [Zgodność](</pl/plugins/compatibility>), [Inwentarz Pluginów](</pl/plugins/plugin-inventory>), [Publikowanie](</pl/clawhub/publishing>), [Skills](</pl/tools/skills>), [Konfiguracja Skills](</pl/tools/skills-config>)

Cykl życia i kondycja Pluginów 26 możliwości

Eksperymentalne0%

Alfa61%

Alfa68%

[Plugin](</pl/tools/plugin>), [Pluginy](</pl/cli/plugins>), [Skills](</pl/cli/skills>), [Skills](</pl/tools/skills>), [Protokół](</pl/gateway/protocol>), [Pakiety](</pl/plugins/bundles>), [Rozwiązywanie zależności](</pl/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alfa - 6 obszarów

OpenClaw App SDK to odrębny kontrakt aplikacji zewnętrznej, niezależny od środowiska uruchomieniowego Gateway i Plugin SDK. Obecna punktacja pokazuje rzeczywistą ścieżkę `@openclaw/sdk` z lukami dotyczącymi publicznego pakowania, automatycznego odkrywania, zatwierdzeń, helperów i zgodności.

Pokrycie Eksperymentalne - 3%Jakość Alfa - 54%Kompletność Alfa - 53%Brak

API klienta 4 możliwości

Eksperymentalny0%

Alpha51%

Alpha50%

[SDK OpenClaw](</pl/gateway/external-apps>), [Projekt API SDK OpenClaw](</pl/gateway/external-apps>)

Dostęp do Gateway 5 możliwości

Eksperymentalny0%

Alpha53%

Alpha54%

[SDK OpenClaw](</pl/gateway/external-apps>), [Projekt API SDK OpenClaw](</pl/gateway/external-apps>), [Protokół](</pl/gateway/protocol>), [Indeks](</pl/gateway/security>)

Konwersacje agentów 6 możliwości

Eksperymentalny0%

Alpha52%

Alpha52%

[SDK OpenClaw](</pl/gateway/external-apps>), [Projekt API SDK OpenClaw](</pl/gateway/external-apps>), [Protokół](</pl/gateway/protocol>)

Zdarzenia i zatwierdzenia 5 możliwości

Eksperymentalny0%

Alpha52%

Alpha52%

[SDK OpenClaw](</pl/gateway/external-apps>), [Projekt API SDK OpenClaw](</pl/gateway/external-apps>), [Protokół](</pl/gateway/protocol>)

Pomocniki zasobów 5 możliwości

Eksperymentalny17%

Alpha62%

Alpha53%

[SDK OpenClaw](</pl/gateway/external-apps>), [Projekt API SDK OpenClaw](</pl/gateway/external-apps>)

Zgodność 5 możliwości

Eksperymentalny0%

Alpha54%

Alpha55%

[Projekt API SDK OpenClaw](</pl/gateway/external-apps>), [Typebox](</pl/concepts/typebox>), [Protokół](</pl/gateway/protocol>)

### Platforma

Host Gateway Linux - M4 Stabilny - 5 obszarów

Zalecane jest środowisko uruchomieniowe Node, udokumentowano usługę użytkownika systemd, a wskazówki dotyczące VPS/kontenerów są obszerne.

Pokrycie Eksperymentalne - 0%Jakość Beta - 75%Kompletność Stabilna - 89%Częściowo - 4

Konfiguracja hosta i aktualizacje 4 funkcje / z obsługą LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Indeks](</pl/install>), [Aktualizowanie](</pl/install/updating>), [Linux](</pl/platforms/linux>), [Indeks](</pl/platforms>)

Środowisko uruchomieniowe Gateway i sterowanie usługą 6 funkcji / z obsługą LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Indeks](</pl/gateway>), [Gateway](</pl/cli/gateway>), [Linux](</pl/platforms/linux>), [Vps](</pl/vps>)

Dostęp zdalny i zabezpieczenia 6 funkcji / z obsługą LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Zdalny](</pl/gateway/remote>), [Tailscale](</pl/gateway/tailscale>), [Procedura ekspozycji](</pl/gateway/security/exposure-runbook>), [Uwierzytelnianie](</pl/gateway/authentication>), [Sekrety](</pl/gateway/secrets>)

Diagnostyka i naprawa 4 funkcje / z obsługą LTS

Eksperymentalne0%

Beta75%

Stabilne89%

[Status](</pl/cli/status>), [Dzienniki](</pl/cli/logs>), [Doctor](</pl/cli/doctor>), [Diagnostyka](</pl/gateway/diagnostics>), [Indeks](</pl/gateway>)

Cele wdrożenia 3 funkcje

Eksperymentalne0%

Beta75%

Stabilne89%

[Vps](</pl/vps>), [Docker](</pl/install/docker>), [Hetzner](</pl/install/hetzner>), [Digitalocean](</pl/install/digitalocean>), [Kubernetes](</pl/install/kubernetes>), [Podman](</pl/install/podman>)

Host Gateway dla macOS - M4 Stabilne - 7 obszarów

Ścieżka usługi LaunchAgent, lokalne/zdalne tryby Gateway, instalacja CLI i integracja z aplikacją są udokumentowane.

Pokrycie Eksperymentalne - 0%Jakość Beta - 74%Kompletność Stabilne - 88%Brak

Konfiguracja CLI 4 możliwości

Eksperymentalne0%

Beta74%

Stabilne88%

[Macos](</pl/platforms/macos>), [Dołączony Gateway](</pl/platforms/mac/bundled-gateway>), [Instalator](</pl/install/installer>), [Node](</pl/install/node>)

Integracja lokalnego Gateway 9 możliwości

Eksperymentalne0%

Beta74%

Stabilne88%

[Macos](</pl/platforms/macos>), [Dołączony Gateway](</pl/platforms/mac/bundled-gateway>), [Zdalny](</pl/platforms/mac/remote>), [Indeks](</pl/gateway>), [Gateway](</pl/cli/gateway>), [Bonjour](</pl/gateway/bonjour>)

Tryb zdalnego Gateway 5 możliwości

Eksperymentalne0%

Beta74%

Stabilne88%

[Zdalny](</pl/platforms/mac/remote>), [Zdalny](</pl/gateway/remote>), [Tailscale](</pl/gateway/tailscale>)

Cykl życia usługi Gateway 10 możliwości

Eksperymentalne0%

Beta74%

Stabilne88%

[Macos](</pl/platforms/macos>), [Dołączony Gateway](</pl/platforms/mac/bundled-gateway>), [Gateway](</pl/cli/gateway>), [Indeks](</pl/gateway>), [Aktualizacja](</pl/cli/update>), [Aktualizowanie](</pl/install/updating>), [Odinstalowanie](</pl/install/uninstall>), [Rozwiązywanie problemów](</pl/gateway/troubleshooting>)

Diagnostyka i obserwowalność 4 możliwości

Eksperymentalne0%

Beta74%

Stabilne88%

[Dołączony Gateway](</pl/platforms/mac/bundled-gateway>), [Macos](</pl/platforms/macos>), [Gateway](</pl/cli/gateway>), [Doctor](</pl/gateway/doctor>), [Rozwiązywanie problemów](</pl/gateway/troubleshooting>)

Uprawnienia i funkcje natywne 4 możliwości

Eksperymentalne0%

Beta74%

Stabilne88%

[Macos](</pl/platforms/macos>), [Zdalny](</pl/platforms/mac/remote>)

Profile i izolacja 5 możliwości

Eksperymentalne0%

Beta74%

Stabilne88%

[Wiele Gateway](</pl/gateway/multiple-gateways>), [Indeks](</pl/gateway>), [Gateway](</pl/cli/gateway>)

Hosting Docker i Podman - M3 Beta - 4 obszary

Dokumentacja instalacji istnieje i obejmuje typowe ścieżki wdrożenia. Awansuj po tym, jak cykliczne smoke testy wydania obejmą zachowanie aktualizacji i woluminów.

Pokrycie Eksperymentalne - 7%Jakość Beta - 71%Kompletność Beta - 79%Brak

Konfiguracja kontenerów 6 funkcji

Eksperymentalne0%

Alpha68%

Beta79%

[Docker](</pl/install/docker>), [Podman](</pl/install/podman>)

Operacje na kontenerach 11 funkcji

Eksperymentalne0%

Alpha68%

Beta79%

[Podman](</pl/install/podman>), [Środowisko uruchomieniowe Docker Vm](</pl/install/docker-vm-runtime>), [Docker](</pl/install/docker>), [Hetzner](</pl/install/hetzner>), [Hostinger](</pl/install/hostinger>)

Wydanie i walidacja obrazów 5 funkcji

Eksperymentalne29%

Beta79%

Beta79%

[Docker](</pl/install/docker>), [Środowisko uruchomieniowe Docker Vm](</pl/install/docker-vm-runtime>), [Pełna walidacja wydania](</pl/reference/full-release-validation>)

Piaskownica agenta i narzędzia 3 funkcje

Eksperymentalne0%

Alpha68%

Beta79%

[Docker](</pl/install/docker>), [Środowisko uruchomieniowe Docker Vm](</pl/install/docker-vm-runtime>)

Windows przez WSL2 - M3 Beta - 6 obszarów

Zalecana ścieżka dla Windows z wytycznymi dotyczącymi systemd/usługi użytkownika oraz dokumentacją łańcucha rozruchowego. Promować po powtarzalnych kartach wyników instalacji/aktualizacji.

Pokrycie Eksperymentalne - 6%Jakość Alpha - 69%Kompletność Beta - 79%Częściowe - 5

Konfiguracja WSL 6 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa67%

Beta79%

[Windows](</pl/platforms/windows>), [Pierwsze kroki](</pl/start/getting-started>)

CLI 8 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa67%

Beta79%

[Windows](</pl/platforms/windows>), [Pierwsze kroki](</pl/start/getting-started>), [Aktualizacja](</pl/install/updating>), [Onboard](</pl/cli/onboard>), [Doctor](</pl/cli/doctor>), [Status](</pl/cli/status>), [Logi](</pl/cli/logs>)

Cykl życia usługi Gateway 10 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa67%

Beta79%

[Windows](</pl/platforms/windows>), [Indeks](</pl/gateway>), [Doctor](</pl/gateway/doctor>)

Dostęp i ekspozycja Gateway 11 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa67%

Beta79%

[Uwierzytelnianie](</pl/gateway/authentication>), [Sekrety](</pl/gateway/secrets>), [Zdalny dostęp](</pl/gateway/remote>), [Runbook ekspozycji](</pl/gateway/security/exposure-runbook>), [Windows](</pl/platforms/windows>)

Diagnostyka i naprawa 6 możliwości / obsługiwane w LTS

Eksperymentalne38%

Beta79%

Beta79%

[Windows](</pl/platforms/windows>), [Status](</pl/cli/status>), [Logi](</pl/cli/logs>), [Doctor](</pl/cli/doctor>), [Doctor](</pl/gateway/doctor>)

Przeglądarka i interfejs Control UI 6 możliwości

Eksperymentalne0%

Alfa67%

Beta79%

[Rozwiązywanie problemów z Browser Wsl2 Windows Remote Cdp](</pl/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Przeglądarka](</pl/tools/browser>), [Control UI](</pl/web/control-ui>)

Raspberry Pi i małe urządzenia z Linuksem - M3 Beta - 4 obszary

Dokumentacja platformy istnieje, a ścieżka Gateway jest oparta na Linuksie. Aby przejść wyżej, potrzebne jest potwierdzenie smoke dla wydania na konkretnym sprzęcie.

Pokrycie Eksperymentalne - 0%Jakość Alfa - 67%Kompletność Beta - 79%Brak

Konfiguracja i zgodność 12 możliwości

Eksperymentalne0%

Alfa67%

Beta79%

[Raspberry Pi](</pl/install/raspberry-pi>), [Indeks](</pl/install>), [FAQ pierwszego uruchomienia](</pl/help/faq-first-run>), [FAQ](</pl/help/faq>), [Linux](</pl/platforms/linux>), [Instalator](</pl/install/installer>)

Dostęp zdalny i uwierzytelnianie 9 możliwości

Eksperymentalne0%

Alfa67%

Beta79%

[Raspberry Pi](</pl/install/raspberry-pi>), [Uwierzytelnianie](</pl/gateway/authentication>), [Tajne dane](</pl/gateway/secrets>), [Parowanie](</pl/gateway/pairing>), [Urządzenia](</pl/cli/devices>), [Zdalny](</pl/gateway/remote>), [Tailscale](</pl/gateway/tailscale>)

Środowisko uruchomieniowe Gateway 10 możliwości

Eksperymentalne0%

Alfa67%

Beta79%

[Indeks](</pl/gateway>), [Gateway](</pl/cli/gateway>), [Raspberry Pi](</pl/install/raspberry-pi>), [Linux](</pl/platforms/linux>), [VPS](</pl/vps>)

Wydajność i diagnostyka 5 możliwości

Eksperymentalne0%

Alfa67%

Beta79%

[Raspberry Pi](</pl/install/raspberry-pi>), [Linux](</pl/platforms/linux>), [Kondycja](</pl/gateway/health>), [Diagnostyka](</pl/gateway/diagnostics>)

Aplikacja towarzysząca macOS - M3 Beta - 8 obszarów

Rozbudowana aplikacja paska menu, uprawnienia, tryb Node, Canvas, wybudzanie głosem, WebChat i tryb zdalny już istnieją. Nadal rozwijają się wystarczająco szybko, by unikać statusu Stabilne.

Pokrycie Eksperymentalne - 0%Jakość Alfa - 66%Kompletność Beta - 78%Brak

Canvas 4 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Canvas](</pl/platforms/mac/canvas>), [Macos](</pl/platforms/macos>), [Webchat](</pl/web/webchat>)

Konfiguracja lokalna 7 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Bundled Gateway](</pl/platforms/mac/bundled-gateway>), [Macos](</pl/platforms/macos>), [Proces podrzędny](</pl/platforms/mac/child-process>), [Konfiguracja deweloperska](</pl/platforms/mac/dev-setup>)

Status i ustawienia 5 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Pasek menu](</pl/platforms/mac/menu-bar>), [Ikona](</pl/platforms/mac/icon>), [Macos](</pl/platforms/macos>), [Kondycja](</pl/platforms/mac/health>), [Rejestrowanie](</pl/platforms/mac/logging>), [Zdalne](</pl/platforms/mac/remote>)

Możliwości natywne 5 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Macos](</pl/platforms/macos>), [Xpc](</pl/platforms/mac/xpc>), [Uprawnienia](</pl/platforms/mac/permissions>), [Podpisywanie](</pl/platforms/mac/signing>), [Peekaboo](</pl/platforms/mac/peekaboo>)

Połączenia zdalne 3 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Zdalne](</pl/platforms/mac/remote>), [Macos](</pl/platforms/macos>), [Zdalne](</pl/gateway/remote>)

Głos i rozmowa 3 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Voicewake](</pl/platforms/mac/voicewake>), [Nakładka głosowa](</pl/platforms/mac/voice-overlay>), [Rozmowa](</pl/nodes/talk>), [Macos](</pl/platforms/macos>)

WebChat 3 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Webchat](</pl/platforms/mac/webchat>), [Macos](</pl/platforms/macos>), [Webchat](</pl/web/webchat>)

Zdalny WebChat 5 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Webchat](</pl/platforms/mac/webchat>), [Zdalne](</pl/gateway/remote>), [Zdalne](</pl/platforms/mac/remote>)

Aplikacja na Androida - M2 Alpha - 7 obszarów

Publiczna ścieżka Google Play istnieje, ale dokumentacja aplikacji nadal opisuje przebudowę jako skrajnie alfa i wskazuje prace nad utwardzeniem wydania.

Pokrycie Eksperymentalne - 0%Jakość Alfa - 59%Kompletność Alfa - 66%Brak

Przechwytywanie multimediów 1 funkcja

Eksperymentalne0%

Alpha59%

Alpha66%

[Android](</pl/platforms/android>), [Kamera](</pl/nodes/camera>)

Czat mobilny 1 funkcja

Eksperymentalne0%

Alpha59%

Alpha66%

[Android](</pl/platforms/android>)

Konfiguracja połączenia 1 funkcja

Eksperymentalne0%

Alpha59%

Alpha66%

[Android](</pl/platforms/android>), [Bonjour](</pl/gateway/bonjour>), [Parowanie](</pl/gateway/pairing>)

Dystrybucja 3 funkcje

Eksperymentalne0%

Alpha59%

Alpha66%

[Android](</pl/platforms/android>)

Ustawienia 1 funkcja

Eksperymentalne0%

Alpha59%

Alpha66%

[Android](</pl/platforms/android>)

Głos 1 funkcja

Eksperymentalne0%

Alpha59%

Alpha66%

[Android](</pl/platforms/android>), [Rozmowa](</pl/nodes/talk>)

Środowisko uruchomieniowe urządzenia 2 funkcje

Eksperymentalne0%

Alpha59%

Alpha66%

[Android](</pl/platforms/android>), [Rozwiązywanie problemów](</pl/nodes/troubleshooting>), [Protokół](</pl/gateway/protocol>)

Natywny Windows - M2 Alpha - 4 obszary

Podstawowe przepływy CLI/Gateway działają, ale dokumentacja nadal zaleca WSL2, aby uzyskać pełne środowisko, i wymienia zastrzeżenia dotyczące natywnego działania.

Pokrycie Eksperymentalne - 0%Jakość Alpha - 58%Kompletność Alpha - 66%Częściowe - 1

CLI 9 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alpha54%

Alpha64%

[Indeks](</pl/install>), [Instalator](</pl/install/installer>), [Windows](</pl/platforms/windows>), [Pierwsze kroki](</pl/start/getting-started>), [Onboard](</pl/cli/onboard>)

Zarządzanie Gateway 11 możliwości

Eksperymentalne0%

Alpha59%

Alpha66%

[Windows](</pl/platforms/windows>), [Indeks](</pl/gateway>), [Gateway](</pl/cli/gateway>), [Doctor](</pl/cli/doctor>)

Sieć 4 możliwości

Eksperymentalne0%

Alpha59%

Alpha66%

[Windows](</pl/platforms/windows>), [Indeks](</pl/gateway>), [Gateway](</pl/cli/gateway>)

Aktualizacje 4 możliwości

Eksperymentalne0%

Alpha59%

Alpha66%

[Aktualizowanie](</pl/install/updating>), [CI](</pl/ci>)

Hosting Kubernetes - M2 Alpha - 4 obszary

Hosting Kubernetes to odrębna ścieżka wdrażania klastra oparta na Kustomize. Bieżąca ocena pokazuje rzeczywistą minimalną ścieżkę wdrożenia z lukami dotyczącymi CI specyficznego dla Kubernetes, pakietowania ingress/TLS/NetworkPolicy, kopii zapasowych/przywracania oraz wzmacniania ekspozycji produkcyjnej.

Pokrycie eksperymentalne - 0%Jakość Alpha - 55%Kompletność Alpha - 61%Brak

Konfiguracja wdrożenia 5 możliwości

Eksperymentalne0%

Alpha55%

Alpha61%

[Kubernetes](</pl/install/kubernetes>), [Indeks](</pl/install>)

Konfiguracja i sekrety 5 możliwości

Eksperymentalne0%

Alpha55%

Alpha61%

[Kubernetes](</pl/install/kubernetes>), [Sekrety](</pl/gateway/secrets>), [Środowisko](</pl/help/environment>)

Dostęp i ekspozycja 5 możliwości

Eksperymentalne0%

Alpha55%

Alpha61%

[Kubernetes](</pl/install/kubernetes>), [Uwierzytelnianie](</pl/gateway/authentication>), [Zdalny dostęp](</pl/gateway/remote>), [Runbook ekspozycji](</pl/gateway/security/exposure-runbook>)

Cykl życia klastra 5 możliwości

Eksperymentalne0%

Alpha55%

Alpha61%

[Kubernetes](</pl/install/kubernetes>), [Indeks](</pl/gateway>)

Aplikacja iOS - M1 eksperymentalne - 8 obszarów

Wewnętrzna wersja zapoznawcza / super-alpha. Przepływy push oparte na TestFlight i przekaźniku istnieją, ale nie ma jeszcze publicznej dystrybucji.

Pokrycie eksperymentalne - 0%Jakość eksperymentalna - 41%Kompletność eksperymentalna - 44%Brak

Multimedia i udostępnianie 1 funkcja

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>), [Kamera](</pl/nodes/camera>)

Kanwa i ekran 1 funkcja

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>), [Kanwa](</pl/plugins/reference/canvas>)

Czat i sesje 1 funkcja

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>), [Czat internetowy](</pl/web/webchat>), [Protokół](</pl/gateway/protocol>)

Konfiguracja i diagnostyka Gateway 7 funkcji

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>), [Parowanie](</pl/channels/pairing>)

Dystrybucja 1 funkcja

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>)

Polecenia urządzenia 2 funkcje

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>), [Protokół](</pl/gateway/protocol>)

Powiadomienia i działanie w tle 1 funkcja

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>), [Konfiguracja](</pl/gateway/configuration>)

Głos 1 funkcja

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>), [Rozmowa](</pl/nodes/talk>)

Ścieżka instalacji Nix - M1 eksperymentalne - 5 obszarów

Opcjonalny proces instalacji. Wymaga jaśniejszej deklaracji wsparcia przed promowaniem do wersji alfa/beta.

Pokrycie eksperymentalne - 0%Jakość eksperymentalna - 41%Kompletność eksperymentalna - 44%Brak

Przekazanie instalacji 4 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Nix](</pl/install/nix>), [Indeks](</pl/install>), [Katalog dokumentacji](</pl/start/docs-directory>)

Cykl życia Plugin 4 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Zarządzanie Pluginami](</pl/plugins/manage-plugins>), [Plugin](</pl/tools/plugin>), [Nix](</pl/install/nix>)

Aktywacja i UX aplikacji 7 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Nix](</pl/install/nix>)

Konfiguracja i stan 7 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Nix](</pl/install/nix>), [Konfiguracja](</pl/cli/setup>), [Środowisko](</pl/help/environment>)

Środowisko uruchomieniowe usługi i zabezpieczenia 8 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Nix](</pl/install/nix>), [Konfiguracja](</pl/cli/setup>), [Doctor](</pl/cli/doctor>), [Aktualizacja](</pl/cli/update>)

powierzchnie towarzyszące watchOS - M1 Eksperymentalne - 5 obszarów

Źródło ma powierzchnie aplikacji/rozszerzenia Watch; publiczna dokumentacja nie przedstawia tego jeszcze jako funkcji dla użytkownika.

Pokrycie eksperymentalne - 0%Jakość eksperymentalna - 41%Kompletność eksperymentalna - 44%Brak

Dostarczanie i odzyskiwanie 7 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>)

Zatwierdzenia Exec 3 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Zatwierdzenia Exec](</pl/tools/exec-approvals>), [Ios](</pl/platforms/ios>)

Dystrybucja i wsparcie 6 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>)

Powiadomienia i odpowiedzi 7 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>)

Interfejs aplikacji na zegarek 3 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Ios](</pl/platforms/ios>)

Aplikacja towarzysząca dla Linux - M0 Planowane - 5 obszarów

Dokumentacja mówi, że natywne aplikacje towarzyszące dla Linux są planowane; Gateway jest obecnie obsługiwaną ścieżką dla Linux.

Pokrycie eksperymentalne - 0%Jakość eksperymentalna - 19%Kompletność eksperymentalna - 21%Brak

Dystrybucja aplikacji 3 możliwości

Eksperymentalne0%

Eksperymentalne19%

Eksperymentalne21%

[Linux](</pl/platforms/linux>), [Indeks](</pl/platforms>), [Indeks](</pl/install>)

Łączność Gateway 4 możliwości

Eksperymentalne0%

Eksperymentalne19%

Eksperymentalne21%

[Linux](</pl/platforms/linux>), [Indeks](</pl/gateway>), [Parowanie](</pl/gateway/pairing>), [Zdalne](</pl/gateway/remote>)

Czat i sesje 3 możliwości

Eksperymentalne0%

Eksperymentalne19%

Eksperymentalne21%

[Linux](</pl/platforms/linux>), [Protokół](</pl/gateway/protocol>), [Czat internetowy](</pl/web/webchat>)

Możliwości pulpitu 9 możliwości

Eksperymentalne0%

Eksperymentalne19%

Eksperymentalne21%

[Linux](</pl/platforms/linux>), [Zatwierdzenia wykonania](</pl/tools/exec-approvals>), [Sekrety](</pl/gateway/secrets>), [Indeks](</pl/nodes>), [Wykonanie](</pl/tools/exec>), [Rozmowa](</pl/nodes/talk>), [Kamera](</pl/nodes/camera>)

Status i diagnostyka 7 możliwości

Eksperymentalne0%

Eksperymentalne19%

Eksperymentalne21%

[Linux](</pl/platforms/linux>), [OpenClaw](</pl/start/openclaw>), [Doctor](</pl/gateway/doctor>)

Natywna aplikacja towarzysząca dla Windows - M0 Planowane - 5 obszarów

Tylko planowane.

Pokrycie eksperymentalne - 0%Jakość eksperymentalna - 19%Kompletność eksperymentalna - 21%Brak

Instalacja i aktualizacje 4 możliwości

Eksperymentalne0%

Eksperymentalne19%

Eksperymentalne21%

[Windows](</pl/platforms/windows>), [Indeks](</pl/install>)

Połączenie z Gateway 3 możliwości

Eksperymentalne0%

Eksperymentalne19%

Eksperymentalne21%

[Windows](</pl/platforms/windows>), [Indeks](</pl/gateway>), [Parowanie](</pl/gateway/pairing>), [Zdalne](</pl/gateway/remote>)

Sesje czatu 2 możliwości

Eksperymentalne0%

Eksperymentalne19%

Eksperymentalne21%

[Windows](</pl/platforms/windows>), [Protokół](</pl/gateway/protocol>)

Status i naprawa 5 możliwości

Eksperymentalne0%

Eksperymentalne19%

Eksperymentalne21%

[Windows](</pl/platforms/windows>), [Doctor](</pl/gateway/doctor>), [Indeks](</pl/gateway>)

Narzędzia pulpitu i uprawnienia 10 możliwości

Eksperymentalne0%

Eksperymentalne19%

Eksperymentalne21%

[Windows](</pl/platforms/windows>), [Indeks](</pl/nodes>), [Exec](</pl/tools/exec>), [Zatwierdzenia Exec](</pl/tools/exec-approvals>), [Indeks](</pl/gateway/security>)

### Kanał

Discord - M4 stabilne - 6 obszarów

Szczegółowa dokumentacja i szerokie pokrycie funkcji. Ścieżki głosu/delegowania powinny nadal być oceniane osobno jako beta/alfa.

Pokrycie eksperymentalne - 0%Jakość beta - 73%Kompletność stabilna - 87%Częściowe - 4

Konfiguracja i obsługa kanałów 10 możliwości / objęte wsparciem LTS

Eksperymentalne0%

Beta73%

Stabilne87%

[Discord](</pl/channels/discord>), [Discord](</pl/plugins/reference/discord>), [Fly](</pl/install/fly>), [Polecenia z ukośnikiem](</pl/tools/slash-commands>), [Kondycja](</pl/gateway/health>), [Kanały](</pl/cli/channels>), [Kanały konfiguracji](</pl/gateway/config-channels>)

Dostęp i tożsamość 6 możliwości / objęte wsparciem LTS

Eksperymentalne0%

Beta73%

Stabilne87%

[Discord](</pl/channels/discord>), [Parowanie](</pl/channels/pairing>), [Grupy dostępu](</pl/channels/access-groups>), [Grupy](</pl/channels/groups>)

Trasowanie i dostarczanie rozmów 12 możliwości / objęte wsparciem LTS

Eksperymentalne0%

Beta73%

Stabilne87%

[Discord](</pl/channels/discord>), [Trasowanie kanałów](</pl/channels/channel-routing>), [Grupy](</pl/channels/groups>), [Grupy dostępu](</pl/channels/access-groups>), [Agenty ACP](</pl/tools/acp-agents>), [Podagenty](</pl/tools/subagents>)

Media i treści rozszerzone 1 możliwość / objęte wsparciem LTS

Eksperymentalne0%

Beta73%

Stabilne87%

[Discord](</pl/channels/discord>)

Natywne elementy sterujące i zatwierdzenia 5 możliwości

Eksperymentalne0%

Beta73%

Stabilne87%

[Discord](</pl/channels/discord>), [Polecenia z ukośnikiem](</pl/tools/slash-commands>)

Głos i połączenia w czasie rzeczywistym 5 możliwości

Eksperymentalne0%

Beta73%

Stabilne87%

[Discord](</pl/channels/discord>), [Openai](</pl/providers/openai>), [Elevenlabs](</pl/providers/elevenlabs>), [Automatyzacja QA E2E](</pl/concepts/qa-e2e-automation>), [Kanały konfiguracji](</pl/gateway/config-channels>)

Telegram - M3 Beta - 5 obszarów

Kanał główny jest wystarczająco dojrzały do regularnego użycia, ale UX o wysokiej zmienności i skrajne przypadki dotyczące mediów wymagają powtarzalnego potwierdzania scenariuszami.

Pokrycie Eksperymentalne - 0%Jakość Alfa - 68%Kompletność Beta - 78%Pełne - 5

Konfiguracja i obsługa kanałów 10 funkcji / obsługiwane w LTS

Eksperymentalny0%

Alfa66%

Beta78%

[Telegram](</pl/channels/telegram>), [Konfiguracja kanałów](</pl/gateway/config-channels>), [Kanały](</pl/cli/channels>)

Dostęp i tożsamość 10 funkcji / obsługiwane w LTS

Eksperymentalny0%

Alfa66%

Beta78%

[Telegram](</pl/channels/telegram>), [Parowanie](</pl/channels/pairing>), [Grupy dostępu](</pl/channels/access-groups>), [Grupy](</pl/channels/groups>), [Wielu agentów](</pl/concepts/multi-agent>)

Trasowanie i dostarczanie rozmów 1 funkcja / obsługiwana w LTS

Eksperymentalny0%

Alfa66%

Beta78%

[Telegram](</pl/channels/telegram>), [Grupy](</pl/channels/groups>), [Wielu agentów](</pl/concepts/multi-agent>)

Media i treści rozszerzone 1 funkcja / obsługiwana w LTS

Eksperymentalny0%

Alfa66%

Beta78%

[Telegram](</pl/channels/telegram>), [Lokalizacja](</pl/channels/location>)

Natywne elementy sterujące i zatwierdzenia 9 funkcji / obsługiwane w LTS

Eksperymentalny0%

Beta77%

Beta79%

[Telegram](</pl/channels/telegram>), [Zatwierdzenia wykonania](</pl/tools/exec-approvals>), [Reakcje](</pl/tools/reactions>)

Slack - M3 Beta - 5 obszarów

Pełnoprawna dokumentacja kanału i powierzchnia trasowania. Wymaga kart wyników dla scenariuszy instalacji w obszarze roboczym i administracji.

Pokrycie eksperymentalne - 0%Jakość Alfa - 66%Kompletność Beta - 78%Pełne - 5

Konfiguracja i obsługa kanałów 10 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa66%

Beta78%

[Slack](</pl/channels/slack>), [Slack](</pl/plugins/reference/slack>), [Sekrety](</pl/gateway/secrets>), [Automatyzacja QA E2E](</pl/concepts/qa-e2e-automation>), [Rozwiązywanie problemów](</pl/channels/troubleshooting>)

Dostęp i tożsamość 1 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa66%

Beta78%

[Slack](</pl/channels/slack>), [Parowanie](</pl/channels/pairing>)

Routing i dostarczanie konwersacji 5 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa66%

Beta78%

[Slack](</pl/channels/slack>), [Ochrona przed pętlą botów](</pl/channels/bot-loop-protection>), [Parowanie](</pl/channels/pairing>)

Multimedia i treści rozszerzone 1 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa66%

Beta78%

[Slack](</pl/channels/slack>), [Automatyzacja QA E2E](</pl/concepts/qa-e2e-automation>)

Natywne kontrolki i zatwierdzenia 8 możliwości / obsługiwane w LTS

Eksperymentalne0%

Alfa66%

Beta78%

[Slack](</pl/channels/slack>), [Polecenia ukośnikowe](</pl/tools/slash-commands>), [Zatwierdzenia wykonania](</pl/tools/exec-approvals>)

iMessage i BlueBubbles - M3 Beta - 5 obszarów

Obsługiwany iMessage działa przez imsg na hoście macOS z zalogowaną aplikacją Messages; starsze konfiguracje BlueBubbles wymagają migracji. Zachowaj widoczność zastrzeżeń dotyczących uprawnień macOS, wrappera SSH, SIP/private API i migracji.

Pokrycie Eksperymentalne - 0%Jakość Alfa - 66%Kompletność Beta - 78%Brak

Konfiguracja i obsługa kanałów 11 funkcji

Eksperymentalne0%

Alfa66%

Beta78%

[Bluebubbles Imessage](</pl/announcements/bluebubbles-imessage>), [Imessage z Bluebubbles](</pl/channels/imessage-from-bluebubbles>), [Konfiguracja kanałów](</pl/gateway/config-channels>), [Imessage](</pl/channels/imessage>)

Dostęp i tożsamość 6 funkcji

Eksperymentalne0%

Alfa66%

Beta78%

[Imessage](</pl/channels/imessage>), [Imessage z Bluebubbles](</pl/channels/imessage-from-bluebubbles>), [Konfiguracja kanałów](</pl/gateway/config-channels>)

Routing i dostarczanie rozmów 4 funkcje

Eksperymentalne0%

Alfa66%

Beta78%

[Imessage](</pl/channels/imessage>)

Media i treści rozszerzone 7 funkcji

Eksperymentalne0%

Alfa66%

Beta78%

[Imessage](</pl/channels/imessage>), [Imessage z Bluebubbles](</pl/channels/imessage-from-bluebubbles>), [Konfiguracja kanałów](</pl/gateway/config-channels>)

Natywne elementy sterujące i zatwierdzenia 3 funkcje

Eksperymentalne0%

Alfa66%

Beta78%

[Imessage](</pl/channels/imessage>)

WhatsApp - M3 Beta - 5 obszarów

Ścieżka rdzeniowa jest ważna i udokumentowana; zmienność nadrzędnego Baileys/sesji utrzymuje ją poniżej poziomu Stabilne.

Pokrycie Eksperymentalne - 0%Jakość Alfa - 66%Kompletność Beta - 78%Brak

Konfiguracja kanału i operacje 5 możliwości

Eksperymentalny0%

Alfa66%

Beta78%

[WhatsApp](</pl/channels/whatsapp>), [Konfiguracja kanałów](</pl/gateway/config-channels>), [WhatsApp](</pl/plugins/reference/whatsapp>), [Automatyzacja QA E2E](</pl/concepts/qa-e2e-automation>), [Diagnostyka](</pl/gateway/doctor>)

Dostęp i tożsamość 7 możliwości

Eksperymentalny0%

Alfa66%

Beta78%

[WhatsApp](</pl/channels/whatsapp>), [Konfiguracja kanałów](</pl/gateway/config-channels>), [Automatyzacja QA E2E](</pl/concepts/qa-e2e-automation>), [Parowanie](</pl/channels/pairing>)

Routing i dostarczanie konwersacji 4 możliwości

Eksperymentalny0%

Alfa66%

Beta78%

[WhatsApp](</pl/channels/whatsapp>), [Wiadomości grupowe](</pl/channels/group-messages>)

Multimedia i treści rozszerzone 2 możliwości

Eksperymentalny0%

Alfa66%

Beta78%

[WhatsApp](</pl/channels/whatsapp>)

Natywne kontrolki i zatwierdzenia 2 możliwości

Eksperymentalny0%

Alfa66%

Beta78%

[WhatsApp](</pl/channels/whatsapp>)

Matrix - M2 Alfa - 6 obszarów

Obsługiwane przez dołączony plugin. Wymaga kart wyników dla mostka, uwierzytelniania i cyklu życia pokoju.

Pokrycie eksperymentalne - 0%Jakość alfa - 60%Kompletność alfa - 67%Brak

Konfiguracja i obsługa kanału 5 możliwości

Eksperymentalne0%

Alfa60%

Alfa67%

[Matrix](</pl/channels/matrix>), [Migracja Matrix](</pl/channels/matrix-migration>)

Dostęp i tożsamość 7 możliwości

Eksperymentalne0%

Alfa60%

Alfa67%

[Matrix](</pl/channels/matrix>), [Grupy](</pl/channels/groups>), [Ochrona przed pętlą botów](</pl/channels/bot-loop-protection>)

Trasowanie i dostarczanie rozmów 1 możliwość

Eksperymentalne0%

Alfa60%

Alfa67%

[Matrix](</pl/channels/matrix>)

Multimedia i treści rozszerzone 1 możliwość

Eksperymentalne0%

Alfa60%

Alfa67%

[Matrix](</pl/channels/matrix>)

Natywne elementy sterujące i zatwierdzenia 6 możliwości

Eksperymentalne0%

Alfa60%

Alfa67%

[Matrix](</pl/channels/matrix>)

Szyfrowanie i weryfikacja 3 możliwości

Eksperymentalne0%

Alfa60%

Alfa67%

[Matrix](</pl/channels/matrix>), [Migracja Matrix](</pl/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 areas

Udokumentowany kanał, ale konfiguracja przedsiębiorstwa/administratora zwiększa ryzyko dojrzałości.

Pokrycie eksperymentalne - 0%Jakość alfa - 59%Kompletność alfa - 66%Brak

Konfiguracja i operacje kanałów 16 możliwości

Eksperymentalne0%

Alpha59%

Alpha66%

[Google Chat](</pl/channels/googlechat>), [Google Chat](</pl/plugins/reference/googlechat>), [Konfiguracja kanałów](</pl/gateway/config-channels>), [Dokumentacja referencyjna CLI kreatora](</pl/start/wizard-cli-reference>), [Sekrety](</pl/gateway/secrets>), [Powierzchnia danych uwierzytelniających Secretref](</pl/reference/secretref-credential-surface>), [Kondycja](</pl/gateway/health>), [Spis Pluginów](</pl/plugins/plugin-inventory>), [Indeks](</pl/channels>)

Dostęp i tożsamość 11 możliwości

Eksperymentalne0%

Alpha59%

Alpha66%

[Google Chat](</pl/channels/googlechat>), [Parowanie](</pl/channels/pairing>), [Grupy dostępu](</pl/channels/access-groups>), [Konfiguracja kanałów](</pl/gateway/config-channels>), [Ochrona przed pętlą botów](</pl/channels/bot-loop-protection>), [Routing kanałów](</pl/channels/channel-routing>)

Routing i dostarczanie rozmów 1 możliwość

Eksperymentalne0%

Alpha59%

Alpha66%

[Google Chat](</pl/channels/googlechat>), [Ochrona przed pętlą botów](</pl/channels/bot-loop-protection>), [Grupy dostępu](</pl/channels/access-groups>), [Routing kanałów](</pl/channels/channel-routing>)

Media i treści rozszerzone 1 możliwość

Eksperymentalne0%

Alpha59%

Alpha66%

[Google Chat](</pl/channels/googlechat>), [Wiadomość](</pl/cli/message>), [Rozumienie mediów](</pl/nodes/media-understanding>), [Powierzchnia danych uwierzytelniających Secretref](</pl/reference/secretref-credential-surface>)

Kontrolki natywne i zatwierdzenia 16 możliwości

Eksperymentalne0%

Alpha59%

Alpha66%

[Google Chat](</pl/channels/googlechat>), [Wiadomość](</pl/cli/message>), [Rozumienie mediów](</pl/nodes/media-understanding>), [Powierzchnia danych uwierzytelniających Secretref](</pl/reference/secretref-credential-surface>), [Reakcje](</pl/tools/reactions>), [Polecenia slash](</pl/tools/slash-commands>), [Konfiguracja agentów](</pl/gateway/config-agents>), [Refaktoryzacja cyklu życia wiadomości](</pl/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 obszarów

Przepływy uwierzytelniania i administracji w przedsiębiorstwie wymagają jednoznacznego potwierdzenia scenariuszami.

Pokrycie Eksperymentalne - 0%Jakość Alpha - 59%Kompletność Alpha - 66%Brak

Konfiguracja i obsługa kanału 9 możliwości

Eksperymentalne0%

Alpha59%

Alpha66%

[Msteams](</pl/channels/msteams>), [Msteams](</pl/plugins/reference/msteams>), [Kanały konfiguracji](</pl/gateway/config-channels>), [Kondycja](</pl/gateway/health>)

Dostęp i tożsamość 9 możliwości

Eksperymentalne0%

Alpha59%

Alpha66%

[Msteams](</pl/channels/msteams>), [Parowanie](</pl/channels/pairing>), [Grupy dostępu](</pl/channels/access-groups>)

Trasowanie i dostarczanie rozmów 5 możliwości

Eksperymentalne0%

Alpha59%

Alpha66%

[Msteams](</pl/channels/msteams>), [Grupy](</pl/channels/groups>), [Trasowanie kanałów](</pl/channels/channel-routing>)

Multimedia i treści rozszerzone 5 możliwości

Eksperymentalne0%

Alpha59%

Alpha66%

[Msteams](</pl/channels/msteams>)

Natywne elementy sterujące i zatwierdzenia 5 możliwości

Eksperymentalne0%

Alpha59%

Alpha66%

[Msteams](</pl/channels/msteams>), [Zaawansowane zatwierdzenia Exec](</pl/tools/exec-approvals-advanced>)

Signal - M2 Alpha - 5 obszarów

Istnieje dokumentacja obsługiwanych kanałów; potrzebne są mocniejsze dowody instalacji i ponownego połączenia.

Pokrycie Eksperymentalne - 0%Jakość Alpha - 59%Kompletność Alpha - 66%Brak

Konfiguracja i obsługa kanału 7 możliwości

Eksperymentalny0%

Alfa59%

Alfa66%

[Signal](</pl/channels/signal>), [Signal](</pl/plugins/reference/signal>)

Dostęp i tożsamość 6 możliwości

Eksperymentalny0%

Alfa59%

Alfa66%

[Signal](</pl/channels/signal>)

Routing i dostarczanie konwersacji 1 możliwość

Eksperymentalny0%

Alfa59%

Alfa66%

[Signal](</pl/channels/signal>)

Multimedia i treści rozszerzone 7 możliwości

Eksperymentalny0%

Alfa59%

Alfa66%

[Signal](</pl/channels/signal>)

Natywne kontrolki i zatwierdzenia 3 możliwości

Eksperymentalny0%

Alfa59%

Alfa66%

[Signal](</pl/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, kanały regionalne - M2 Alfa - 4 obszary

Ważne pokrycie regionalne, ale poziom publicznego wsparcia powinien być kalibrowany według typu konta, zatwierdzenia upstream i dowodów od opiekunów.

Pokrycie Eksperymentalny - 0%Jakość Alfa - 55%Kompletność Alfa - 58%Brak

Konfiguracja i obsługa kanałów 6 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Indeks](</pl/channels>), [Parowanie](</pl/channels/pairing>), [Feishu](</pl/plugins/reference/feishu>), [Wewnętrzne mechanizmy architektury](</pl/plugins/architecture-internals>)

Dostęp i tożsamość 1 możliwości

Eksperymentalne0%

Alpha53%

Alpha54%

Brak powiązanej dokumentacji

Trasowanie i dostarczanie rozmów 1 możliwości

Eksperymentalne0%

Alpha53%

Alpha54%

Brak powiązanej dokumentacji

Media i treści rozszerzone 1 możliwości

Eksperymentalne0%

Alpha53%

Alpha54%

Brak powiązanej dokumentacji

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 obszary

Obsługiwane powierzchnie istnieją, ale dojrzałość prawdopodobnie różni się w zależności od upstreamu i pokrycia przez opiekunów. Oceń indywidualnie później.

Pokrycie Eksperymentalne - 0%Jakość Alpha - 53%Kompletność Alpha - 54%Brak

Konfiguracja i obsługa kanałów 1 funkcja

Eksperymentalne0%

Alfa53%

Alfa54%

Brak powiązanej dokumentacji

Dostęp i tożsamość 1 funkcja

Eksperymentalne0%

Alfa53%

Alfa54%

Brak powiązanej dokumentacji

Trasowanie i dostarczanie rozmów 1 funkcja

Eksperymentalne0%

Alfa53%

Alfa54%

Brak powiązanej dokumentacji

Multimedia i treści rozszerzone 1 funkcja

Eksperymentalne0%

Alfa53%

Alfa54%

Brak powiązanej dokumentacji

Kanał połączeń głosowych - M1 eksperymentalne - 5 obszarów

Opcjonalna/Plugin ścieżka ze złożonym zachowaniem w czasie rzeczywistym. Wymaga karty wyników scenariuszy przed publiczną wersją beta.

Pokrycie eksperymentalne - 0%Jakość eksperymentalna - 41%Kompletność eksperymentalna - 44%Brak

Konfiguracja i obsługa kanałów 2 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Voicecall](</pl/cli/voicecall>), [Połączenie głosowe](</pl/plugins/voice-call>), [Protokół](</pl/gateway/protocol>)

Dostęp i tożsamość 1 możliwość

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Połączenie głosowe](</pl/plugins/voice-call>), [Voicecall](</pl/cli/voicecall>)

Trasowanie i dostarczanie konwersacji 1 możliwość

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Połączenie głosowe](</pl/plugins/voice-call>)

Multimedia i treści rozszerzone 2 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Połączenie głosowe](</pl/plugins/voice-call>), [Inwentarz Pluginów](</pl/plugins/plugin-inventory>)

Głos i połączenia w czasie rzeczywistym 2 możliwości

Eksperymentalne0%

Eksperymentalne41%

Eksperymentalne44%

[Połączenie głosowe](</pl/plugins/voice-call>)

### Dostawca i narzędzie

Automatyzacja przeglądarki, exec i narzędzia piaskownicy - M3 Beta - 3 obszary

Narzędzia podstawowe są udokumentowane, ale bezpieczeństwo hosta i UX uprawnień powinny pozostawać aktywnie oceniane w scorecardzie.

Pokrycie Eksperymentalne - 21%Jakość Beta - 75%Kompletność Beta - 79%Częściowe - 2

Automatyzacja przeglądarki 8 możliwości

Eksperymentalne13%

Beta79%

Beta79%

[Sterowanie przeglądarką](</pl/tools/browser-control>), [Testowanie](</pl/help/testing>), [Przeglądarka](</pl/tools/browser>), [Indeks](</pl/gateway/security>), [Kontrole audytu](</pl/gateway/security/audit-checks>)

Wywoływanie i wykonywanie narzędzi 6 możliwości / obsługiwane przez LTS

Alpha50%

Beta79%

Beta79%

[Exec](</pl/tools/exec>), [Proces w tle](</pl/gateway/background-process>), [Narzędzia wywołują API HTTP](</pl/gateway/tools-invoke-http-api>), [Zakresy operatora](</pl/gateway/operator-scopes>), [Protokół](</pl/gateway/protocol>), [Zatwierdzenia Exec](</pl/tools/exec-approvals>), [Zaawansowane zatwierdzenia Exec](</pl/tools/exec-approvals-advanced>), [Podwyższone uprawnienia](</pl/tools/elevated>)

Piaskownica i zasady narzędzi 6 możliwości / obsługiwane przez LTS

Eksperymentalne0%

Alpha68%

Beta79%

[Piaskownica](</pl/gateway/sandboxing>), [Piaskownica kontra zasady narzędzi kontra podwyższone uprawnienia](</pl/gateway/sandbox-vs-tool-policy-vs-elevated>), [Narzędzia piaskownicy dla wielu agentów](</pl/tools/multi-agent-sandbox-tools>), [Dokumentacja referencyjna uprzęży Codex](</pl/plugins/codex-harness-reference>), [Narzędzia konfiguracji](</pl/gateway/config-tools>)

Ścieżka dostawcy OpenAI i Codex - M3 Beta - 5 obszarów

Szczegółowa dokumentacja, ścieżka OAuth/subskrypcji, głos w czasie rzeczywistym, obraz i zachowanie kompatybilności. Zmienność dostawcy nie pozwala uznać tego za Stable bez dowodu z karty wyników wydania.

Pokrycie Eksperymentalne - 26%Jakość Beta - 74%Kompletność Beta - 79%Częściowe - 3

Model i uwierzytelnianie 6 możliwości / obsługiwane w LTS

Eksperymentalne44%

Beta79%

Beta79%

[Openai](</pl/providers/openai>), [Codex Harness](</pl/plugins/codex-harness>), [Modele](</pl/concepts/models>), [Oauth](</pl/concepts/oauth>), [Dokumentacja referencyjna Codex Harness](</pl/plugins/codex-harness-reference>), [Monitorowanie uwierzytelniania](</pl/gateway/authentication>)

Zgodność odpowiedzi i narzędzi 4 możliwości / obsługiwane w LTS

Eksperymentalne40%

Beta79%

Beta79%

[Openai](</pl/providers/openai>), [Openresponses Http Api](</pl/gateway/openresponses-http-api>), [Openai Http Api](</pl/gateway/openai-http-api>), [Natywne Pluginy Codex](</pl/plugins/codex-native-plugins>)

Natywny Codex Harness 2 możliwości / obsługiwane w LTS

Eksperymentalne44%

Beta79%

Beta79%

[Codex Harness](</pl/plugins/codex-harness>), [Środowisko uruchomieniowe Codex Harness](</pl/plugins/codex-harness-runtime>), [Dokumentacja referencyjna Codex Harness](</pl/plugins/codex-harness-reference>), [Natywne Pluginy Codex](</pl/plugins/codex-native-plugins>)

Obrazy i dane wejściowe multimodalne 2 możliwości

Eksperymentalne0%

Alpha67%

Beta79%

[Openai](</pl/providers/openai>), [Generowanie obrazów](</pl/tools/image-generation>), [Obrazy](</pl/nodes/images>)

Głos i dźwięk w czasie rzeczywistym 2 możliwości

Eksperymentalne0%

Alpha67%

Beta79%

[Openai](</pl/providers/openai>), [Discord](</pl/channels/discord>), [Połączenie głosowe](</pl/plugins/voice-call>)

Narzędzia wyszukiwania w sieci - M3 Beta - 4 obszary

Istnieje wielu dostawców i dokumentacja. Wymaga dowodów dotyczących limitów, błędów i SSRF dla każdej rodziny dostawców.

Pokrycie: eksperymentalne - 9%Jakość: Beta - 74%Kompletność: Beta - 79%Brak

Dostawcy wyszukiwania 19 funkcji

Eksperymentalne11%

Beta79%

Beta79%

[Web](</pl/tools/web>), [Brave Search](</pl/tools/brave-search>), [Tavily](</pl/tools/tavily>), [Exa Search](</pl/tools/exa-search>), [Firecrawl](</pl/tools/firecrawl>), [Perplexity Search](</pl/tools/perplexity-search>), [Duckduckgo Search](</pl/tools/duckduckgo-search>), [Searxng Search](</pl/tools/searxng-search>), [Gemini Search](</pl/tools/gemini-search>), [Grok Search](</pl/tools/grok-search>), [Kimi Search](</pl/tools/kimi-search>), [Minimax Search](</pl/tools/minimax-search>), [Ollama Search](</pl/tools/ollama-search>), [Podścieżki SDK](</pl/plugins/sdk-subpaths>), [Przegląd SDK](</pl/plugins/sdk-overview>), [Manifest](</pl/plugins/manifest>)

Konfiguracja i diagnostyka 9 funkcji

Eksperymentalne0%

Alpha68%

Beta79%

[Web](</pl/tools/web>), [Pobieranie Web](</pl/tools/web-fetch>), [FAQ](</pl/help/faq>), [Koszty użycia API](</pl/reference/api-usage-costs>), [Brave Search](</pl/tools/brave-search>), [Perplexity Search](</pl/tools/perplexity-search>), [Tavily](</pl/tools/tavily>), [Firecrawl](</pl/tools/firecrawl>)

Bezpieczeństwo sieci 4 funkcje

Eksperymentalne0%

Alpha68%

Beta79%

[Web](</pl/tools/web>), [Pobieranie Web](</pl/tools/web-fetch>), [Firecrawl](</pl/tools/firecrawl>), [Searxng Search](</pl/tools/searxng-search>)

Dostępność narzędzi i pobieranie 11 funkcji

Eksperymentalne25%

Beta79%

Beta79%

[Narzędzia konfiguracji](</pl/gateway/config-tools>), [Pobieranie Web](</pl/tools/web-fetch>), [Web](</pl/tools/web>), [FAQ](</pl/help/faq>)

Ścieżka dostawcy Anthropic - M3 Beta - 5 obszarów

Pełnoprawny dostawca modeli. Wymaga cyklicznego potwierdzania scenariuszy uwierzytelniania, katalogu i wywołań narzędzi.

Pokrycie Eksperymentalne - 0%Jakość Beta - 71%Kompletność Beta - 78%Brak

Uwierzytelnianie i odzyskiwanie dostawcy 9 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Anthropic](</pl/providers/anthropic>), [Doctor](</pl/gateway/doctor>), [Przykłady konfiguracji](</pl/gateway/configuration-examples>), [Rozwiązywanie problemów](</pl/gateway/troubleshooting>), [Buforowanie promptów](</pl/reference/prompt-caching>)

Wybór modelu i środowiska wykonawczego 10 możliwości

Eksperymentalne0%

Beta78%

Beta79%

[Anthropic](</pl/providers/anthropic>), [Agenci konfiguracji](</pl/gateway/config-agents>), [Modele](</pl/concepts/models>), [Backendy CLI](</pl/gateway/cli-backends>)

Transport żądań i semantyka tur 10 możliwości

Eksperymentalne0%

Beta77%

Beta79%

[Anthropic](</pl/providers/anthropic>), [Buforowanie promptów](</pl/reference/prompt-caching>), [Rozwiązywanie problemów](</pl/gateway/troubleshooting>), [Backendy CLI](</pl/gateway/cli-backends>), [Dostawcy modeli](</pl/concepts/model-providers>)

Pamięć podręczna promptów i kontekst 5 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Anthropic](</pl/providers/anthropic>), [Buforowanie promptów](</pl/reference/prompt-caching>), [Rozwiązywanie problemów](</pl/gateway/troubleshooting>), [Heartbeat](</pl/gateway/heartbeat>)

Wejścia multimedialne 4 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Anthropic](</pl/providers/anthropic>), [Agenci konfiguracji](</pl/gateway/config-agents>)

Ścieżka dostawcy Google - M3 Beta - 5 obszarów

Pełnoprawny dostawca z powierzchniami modeli i czasu rzeczywistego. Wymaga osobnej oceny Live/Talk.

Pokrycie Eksperymentalne - 0%Jakość Alpha - 66%Kompletność Beta - 78%Brak

Konfiguracja dostawcy i poświadczenia 10 możliwości

Eksperymentalne0%

Alfa66%

Beta78%

[Google](</pl/providers/google>), [Dostawcy modeli](</pl/concepts/model-providers>)

Routing modeli i punkty końcowe 10 możliwości

Eksperymentalne0%

Alfa66%

Beta78%

[Google](</pl/providers/google>), [Dostawcy modeli](</pl/concepts/model-providers>), [Google](</pl/plugins/reference/google>), [Wyszukiwanie Gemini](</pl/tools/gemini-search>)

Bezpośrednie środowisko uruchomieniowe Gemini 9 możliwości

Eksperymentalne0%

Alfa66%

Beta78%

[Google](</pl/providers/google>), [Dostawcy modeli](</pl/concepts/model-providers>), [FAQ dotyczące modeli](</pl/help/faq-models>), [Testowanie na żywo](</pl/help/testing-live>)

Multimedia, wyszukiwanie i czas rzeczywisty 10 możliwości

Eksperymentalne0%

Alfa66%

Beta78%

[Google](</pl/plugins/reference/google>), [Google](</pl/providers/google>)

Buforowanie promptów 5 możliwości

Eksperymentalne0%

Alfa66%

Beta78%

[Buforowanie promptów](</pl/reference/prompt-caching>), [Google](</pl/providers/google>), [Dostawcy modeli](</pl/concepts/model-providers>), [Użycie tokenów](</pl/reference/token-use>)

Ścieżka dostawcy OpenRouter - M3 Beta - 4 obszary

Ujednolicona ścieżka dostawcy jest udokumentowana i wartościowa, ale zachowanie specyficzne dla modelu bywa różne.

Zakres: eksperymentalne - 0%Jakość: Alfa - 66%Kompletność: Beta - 78%Brak

Konfiguracja i uwierzytelnianie dostawcy 14 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Openrouter](</pl/providers/openrouter>), [Dostawcy modeli](</pl/concepts/model-providers>), [Konfiguracja](</pl/cli/configure>), [Uwierzytelnianie](</pl/gateway/authentication>), [Środowisko](</pl/help/environment>), [Modele](</pl/cli/models>), [Modele](</pl/concepts/models>)

Środowisko wykonawcze czatu i normalizacja 15 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Openrouter](</pl/providers/openrouter>), [Dostawcy modeli](</pl/concepts/model-providers>), [Buforowanie promptów](</pl/reference/prompt-caching>)

Odzyskiwanie dostawcy i diagnostyka 5 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Przełączanie awaryjne modeli](</pl/concepts/model-failover>), [Openrouter](</pl/providers/openrouter>), [Modele](</pl/cli/models>)

Generowanie multimediów i mowa 7 możliwości

Eksperymentalne0%

Alpha66%

Beta78%

[Openrouter](</pl/providers/openrouter>), [Generowanie obrazów](</pl/tools/image-generation>), [Generowanie muzyki](</pl/tools/music-generation>), [Omówienie multimediów](</pl/tools/media-overview>), [Generowanie wideo](</pl/tools/video-generation>), [Tts](</pl/tools/tts>)

Narzędzia generowania obrazów, wideo i muzyki - M2 Alpha - 5 obszarów

Możliwość istnieje u różnych dostawców, ale jakość, opóźnienia i zgodność parametrów różnią się zbyt mocno, aby uznać ją za beta bez dowodów dla każdego dostawcy.

Pokrycie Eksperymentalne - 0%Jakość Alpha - 61%Kompletność Alpha - 68%Brak

Routing i wykrywanie multimediów 4 możliwości

Eksperymentalne0%

Alfa61%

Alfa68%

[Agenci konfiguracji](</pl/gateway/config-agents>), [Generowanie obrazów](</pl/tools/image-generation>), [Generowanie wideo](</pl/tools/video-generation>), [Generowanie muzyki](</pl/tools/music-generation>)

Cykl życia i dostarczanie zadań 12 możliwości

Eksperymentalne0%

Alfa61%

Alfa68%

[Przegląd multimediów](</pl/tools/media-overview>), [Generowanie obrazów](</pl/tools/image-generation>), [Generowanie wideo](</pl/tools/video-generation>), [Generowanie muzyki](</pl/tools/music-generation>)

Generowanie obrazów 9 możliwości

Eksperymentalne0%

Alfa61%

Alfa68%

[Generowanie obrazów](</pl/tools/image-generation>), [Infer](</pl/cli/infer>), [Przegląd multimediów](</pl/tools/media-overview>)

Generowanie wideo 11 możliwości

Eksperymentalne0%

Alfa61%

Alfa68%

[Generowanie wideo](</pl/tools/video-generation>), [Runway](</pl/providers/runway>), [Pixverse](</pl/providers/pixverse>), [Fal](</pl/providers/fal>), [Openrouter](</pl/providers/openrouter>)

Generowanie muzyki 6 możliwości

Eksperymentalne0%

Alfa61%

Alfa68%

[Generowanie muzyki](</pl/tools/music-generation>)

Lokalni dostawcy modeli: Ollama, vLLM, SGLang, LM Studio - M2 Alfa - 5 obszarów

Przydatne i udokumentowane, ale zmienność środowisk jest duża.

Pokrycie Eksperymentalne - 0%Jakość Alfa - 61%Kompletność Alfa - 68%Brak

Konfiguracja dostawców, cykl życia i diagnostyka 12 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Modele lokalne](</pl/gateway/local-models>), [Lmstudio](</pl/providers/lmstudio>), [Ollama](</pl/providers/ollama>), [Vllm](</pl/providers/vllm>), [Lokalne usługi modeli](</pl/gateway/local-model-services>), [Konfiguracja agentów](</pl/gateway/config-agents>), [Rozwiązywanie problemów](</pl/gateway/troubleshooting>), [Doctor](</pl/gateway/doctor>)

Natywne Plugin dostawców 10 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Ollama](</pl/providers/ollama>), [Lmstudio](</pl/providers/lmstudio>)

Zgodność środowiska uruchomieniowego zgodnego z OpenAI 8 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Vllm](</pl/providers/vllm>), [Sglang](</pl/providers/sglang>), [Modele lokalne](</pl/gateway/local-models>), [Lmstudio](</pl/providers/lmstudio>)

Pamięć lokalna i osadzania 5 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Pamięć](</pl/concepts/memory>), [Doctor](</pl/gateway/doctor>)

Bezpieczeństwo sieci i kontrola promptów 2 możliwości

Eksperymentalne0%

Alpha61%

Alpha68%

[Indeks](</pl/gateway/security>), [Konfiguracja narzędzi](</pl/gateway/config-tools>), [Modele lokalne](</pl/gateway/local-models>)

Dostawcy hostowani z długiego ogona - M2 Alpha - 3 obszary

Istnieje wiele stron dokumentacji/referencyjnych; wynik powinien być generowany z metadanych dostawców oraz pokrycia testami smoke na żywo.

Pokrycie Eksperymentalne - 0%Jakość Alfa - 61%Kompletność Alfa - 68%Brak

Hostowani dostawcy LLM 12 funkcji

Eksperymentalne0%

Alfa61%

Alfa68%

[Indeks](</pl/providers>), [Dostawcy modeli](</pl/concepts/model-providers>), [Testowanie na żywo](</pl/help/testing-live>), [Onboard](</pl/cli/onboard>)

Hostowani dostawcy mediów 8 funkcji

Eksperymentalne0%

Alfa61%

Alfa68%

[Manifest](</pl/plugins/manifest>), [Testowanie na żywo](</pl/help/testing-live>), [Indeks](</pl/providers>)

Operacje dostawców 12 funkcji

Eksperymentalne0%

Alfa61%

Alfa68%

[Indeks](</pl/providers>), [Dostawcy modeli](</pl/concepts/model-providers>), [Manifest](</pl/plugins/manifest>), [Testowanie na żywo](</pl/help/testing-live>), [Modele](</pl/cli/models>)

Was this useful?YesNo

Open issue