---
title: openclaw status
source_url: https://docs.openclaw.ai/pl/cli/status
scraped_at: 2026-05-25
---

Diagnostyka kanałów + sesji.

bashCopy code
[code]
    openclaw statusopenclaw status --allopenclaw status --deepopenclaw status --usage
[/code]

Uwagi:

  * `--deep` uruchamia sondy na żywo (WhatsApp Web + Telegram + Discord + Slack + Signal).
  * Zwykłe `openclaw status` pozostaje na szybkiej ścieżce tylko do odczytu i oznacza pamięć jako `not checked` zamiast niedostępnej, gdy pomija inspekcję pamięci. Ciężki audyt bezpieczeństwa, zgodność pluginów oraz sondy wektorów pamięci są pozostawione dla `openclaw status --all`, `openclaw status --deep`, `openclaw security audit` i `openclaw memory status --deep`.
  * `status --json --all` raportuje szczegóły pamięci z aktywnego środowiska uruchomieniowego pluginu pamięci wybranego przez `plugins.slots.memory`. Niestandardowe pluginy pamięci mogą pozostawić wbudowane `agents.defaults.memorySearch.enabled` wyłączone i nadal raportować własne pliki, fragmenty, wektory oraz stan FTS.
  * `--usage` wypisuje znormalizowane okna użycia dostawcy jako `X% left`.
  * Dane wyjściowe statusu sesji rozdzielają `Execution:` od `Runtime:`. `Execution` to ścieżka sandboxa (`direct`, `docker/*`), a `Runtime` informuje, czy sesja używa `OpenClaw Pi Default`, `OpenAI Codex`, backendu CLI, czy backendu ACP, takiego jak `codex (acp/acpx)`. Zobacz [Środowiska uruchomieniowe agentów](</pl/concepts/agent-runtimes>), aby poznać rozróżnienie między dostawcą, modelem i środowiskiem uruchomieniowym.
  * Surowe pola MiniMax `usage_percent` / `usagePercent` oznaczają pozostały limit, więc OpenClaw odwraca je przed wyświetleniem; pola oparte na liczbie mają pierwszeństwo, gdy są obecne. Odpowiedzi `model_remains` preferują wpis modelu czatu, w razie potrzeby wyprowadzają etykietę okna ze znaczników czasu i uwzględniają nazwę modelu w etykiecie planu.
  * Gdy bieżący snapshot sesji jest skąpy, `/status` może uzupełnić liczniki tokenów i pamięci podręcznej z najnowszego dziennika użycia transkrypcji. Istniejące niezerowe wartości na żywo nadal mają pierwszeństwo przed wartościami zastępczymi z transkrypcji.
  * `/status` zawiera zwięzły czas działania procesu Gateway i czas działania systemu hosta.
  * Zastępcze dane z transkrypcji mogą też odzyskać etykietę aktywnego modelu środowiska uruchomieniowego, gdy brakuje jej w wpisie sesji na żywo. Jeśli ten model z transkrypcji różni się od wybranego modelu, status rozwiązuje okno kontekstu względem odzyskanego modelu środowiska uruchomieniowego zamiast wybranego.
  * Do rozliczania rozmiaru promptu zastępcze dane z transkrypcji preferują większą sumę zorientowaną na prompt, gdy metadanych sesji brakuje albo są mniejsze, dzięki czemu sesje niestandardowych dostawców nie sprowadzają wyświetlania tokenów do `0`.
  * Dane wyjściowe obejmują magazyny sesji dla poszczególnych agentów, gdy skonfigurowano wielu agentów.
  * Przegląd obejmuje status instalacji i działania usługi hosta Gateway + node, gdy jest dostępny.
  * Przegląd obejmuje kanał aktualizacji + SHA git (dla checkoutów źródłowych).
  * Informacje o aktualizacji pojawiają się w Przeglądzie; jeśli aktualizacja jest dostępna, status wypisuje podpowiedź, aby uruchomić `openclaw update` (zobacz [Aktualizowanie](</pl/install/updating>)).
  * Błędy odświeżania cen modeli są pokazywane jako opcjonalne ostrzeżenia o cenach. Nie oznaczają one, że Gateway lub kanały są w złym stanie.
  * Powierzchnie statusu tylko do odczytu (`status`, `status --json`, `status --all`) rozwiązują obsługiwane SecretRefs dla docelowych ścieżek konfiguracji, gdy to możliwe.
  * Jeśli skonfigurowano obsługiwany SecretRef kanału, ale jest niedostępny w bieżącej ścieżce polecenia, status pozostaje tylko do odczytu i raportuje zdegradowane dane wyjściowe zamiast ulegać awarii. Dane wyjściowe dla człowieka pokazują ostrzeżenia, takie jak „skonfigurowany token jest niedostępny w tej ścieżce polecenia”, a dane wyjściowe JSON zawierają `secretDiagnostics`.
  * Gdy rozwiązywanie SecretRef lokalne dla polecenia powiedzie się, status preferuje rozwiązany snapshot i usuwa przejściowe znaczniki kanału „sekret niedostępny” z końcowych danych wyjściowych.
  * `status --all` zawiera wiersz przeglądu sekretów oraz sekcję diagnozy, która podsumowuje diagnostykę sekretów (przyciętą dla czytelności) bez zatrzymywania generowania raportu.


## Powiązane

  * [Dokumentacja CLI](</pl/cli>)
  * [Doctor](</pl/gateway/doctor>)


Was this useful?YesNo