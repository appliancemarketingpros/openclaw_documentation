---
title: Przegląd pamięci
source_url: https://docs.openclaw.ai/pl/concepts/memory
scraped_at: 2026-05-25
---

OpenClaw zapamiętuje rzeczy, zapisując **zwykłe pliki Markdown** w przestrzeni roboczej agenta. Model „pamięta” tylko to, co zostanie zapisane na dysku — nie ma żadnego ukrytego stanu.

## Jak to działa

Agent ma trzy pliki związane z pamięcią:

  * **`MEMORY.md`** — pamięć długoterminowa. Trwałe fakty, preferencje i decyzje. Ładowany na początku każdej sesji DM.
  * **`memory/YYYY-MM-DD.md`** — notatki dzienne. Bieżący kontekst i obserwacje. Notatki z dzisiaj i wczoraj są ładowane automatycznie.
  * **`DREAMS.md`** (opcjonalnie) — Dziennik Dream Diary i podsumowania przeglądów Dreaming do weryfikacji przez człowieka, w tym ugruntowane historyczne wpisy uzupełniające.


Te pliki znajdują się w przestrzeni roboczej agenta (domyślnie `~/.openclaw/workspace`).

## Co trafia gdzie

`MEMORY.md` to kompaktowa, kuratorowana warstwa. Używaj jej dla trwałych faktów, preferencji, stałych decyzji i krótkich podsumowań, które powinny być dostępne na początku głównej sesji prywatnej. Nie ma ona służyć jako surowy transkrypt, dzienny dziennik ani wyczerpujące archiwum.

Pliki `memory/YYYY-MM-DD.md` są warstwą roboczą. Używaj ich do szczegółowych notatek dziennych, obserwacji, podsumowań sesji i surowego kontekstu, który może nadal przydać się później. Te pliki są indeksowane dla `memory_search` i `memory_get`, ale nie są wstrzykiwane do normalnego promptu startowego przy każdym przebiegu.

Z czasem agent powinien destylować użyteczny materiał z notatek dziennych do `MEMORY.md` i usuwać nieaktualne wpisy długoterminowe. Wygenerowane instrukcje przestrzeni roboczej i przepływ Heartbeat mogą robić to okresowo; nie musisz ręcznie edytować `MEMORY.md` dla każdego zapamiętanego szczegółu.

Jeśli `MEMORY.md` przekroczy budżet pliku startowego, OpenClaw zachowa plik na dysku w całości, ale skróci kopię wstrzykiwaną do kontekstu modelu. Traktuj to jako sygnał, aby przenieść szczegółowy materiał z powrotem do `memory/*.md`, zostawić w `MEMORY.md` tylko trwałe podsumowanie albo zwiększyć limity startowe, jeśli wyraźnie chcesz przeznaczyć więcej budżetu promptu. Użyj `/context list`, `/context detail` lub `openclaw doctor`, aby zobaczyć surowe i wstrzyknięte rozmiary oraz stan skrócenia.

## Wywnioskowane zobowiązania

Niektóre przyszłe działania następcze nie są trwałymi faktami. Jeśli wspomnisz o jutrzejszej rozmowie kwalifikacyjnej, użyteczną pamięcią może być „odezwij się po rozmowie”, a nie „zapisz to na zawsze w `MEMORY.md`”.

[Zobowiązania](</pl/concepts/commitments>) to opcjonalne, krótkotrwałe pamięci działań następczych dla takiego przypadku. OpenClaw wywnioskowuje je w ukrytym przebiegu w tle, ogranicza ich zakres do tego samego agenta i kanału oraz dostarcza terminowe sprawdzenia przez Heartbeat. Jawne przypomnienia nadal używają [zaplanowanych zadań](</pl/automation/cron-jobs>).

## Narzędzia pamięci

Agent ma dwa narzędzia do pracy z pamięcią:

  * **`memory_search`** — znajduje odpowiednie notatki za pomocą wyszukiwania semantycznego, nawet gdy sformułowanie różni się od oryginału.
  * **`memory_get`** — odczytuje konkretny plik pamięci lub zakres wierszy.


Oba narzędzia są dostarczane przez aktywny Plugin pamięci (domyślnie: `memory-core`).

## Towarzyszący Plugin Memory Wiki

Jeśli chcesz, aby trwała pamięć zachowywała się bardziej jak utrzymywana baza wiedzy niż tylko surowe notatki, użyj dołączonego Plugin `memory-wiki`.

`memory-wiki` kompiluje trwałą wiedzę do skarbca wiki z:

  * deterministyczną strukturą stron
  * ustrukturyzowanymi twierdzeniami i dowodami
  * śledzeniem sprzeczności i aktualności
  * wygenerowanymi pulpitami
  * skompilowanymi streszczeniami dla konsumentów agenta/środowiska uruchomieniowego
  * narzędziami natywnymi dla wiki, takimi jak `wiki_search`, `wiki_get`, `wiki_apply` i `wiki_lint`


Nie zastępuje aktywnego Plugin pamięci. Aktywny Plugin pamięci nadal odpowiada za przypominanie, promowanie i Dreaming. `memory-wiki` dodaje obok niego bogatą w pochodzenie warstwę wiedzy.

Zobacz [Memory Wiki](</pl/plugins/memory-wiki>).

## Wyszukiwanie w pamięci

Gdy skonfigurowany jest dostawca embeddingów, `memory_search` używa **wyszukiwania hybrydowego** — łączy podobieństwo wektorowe (znaczenie semantyczne) z dopasowaniem słów kluczowych (dokładne terminy, takie jak identyfikatory i symbole kodu). Działa to od razu, gdy masz klucz API dla dowolnego obsługiwanego dostawcy.

Szczegóły działania wyszukiwania, opcje dostrajania i konfigurację dostawcy znajdziesz w [Wyszukiwanie w pamięci](</pl/concepts/memory-search>).

## Backendy pamięci

[**Wbudowany (domyślny)** Oparty na SQLite. Działa od razu z wyszukiwaniem słów kluczowych, podobieństwem wektorowym i wyszukiwaniem hybrydowym. Bez dodatkowych zależności. ](</pl/concepts/memory-builtin>) [**QMD** Lokalny sidecar z ponownym rankingowaniem, rozszerzaniem zapytań i możliwością indeksowania katalogów poza przestrzenią roboczą. ](</pl/concepts/memory-qmd>) [**Honcho** Natywna dla AI pamięć między sesjami z modelowaniem użytkownika, wyszukiwaniem semantycznym i świadomością wielu agentów. Instalacja Plugin. ](</pl/concepts/memory-honcho>) [**LanceDB** Dołączona pamięć oparta na LanceDB z embeddingami zgodnymi z OpenAI, automatycznym przypominaniem, automatycznym przechwytywaniem i obsługą lokalnych embeddingów Ollama. ](</pl/plugins/memory-lancedb>)

## Warstwa wiki wiedzy

[**Memory Wiki** Kompiluje trwałą pamięć do bogatego w pochodzenie skarbca wiki z twierdzeniami, pulpitami, trybem mostu i przepływami pracy przyjaznymi dla Obsidian. ](</pl/plugins/memory-wiki>)

## Automatyczne opróżnianie pamięci

Zanim [kompaktowanie](</pl/concepts/compaction>) podsumuje rozmowę, OpenClaw uruchamia cichy przebieg, który przypomina agentowi o zapisaniu ważnego kontekstu do plików pamięci. Jest to domyślnie włączone — nie musisz niczego konfigurować.

Aby utrzymać ten przebieg porządkowy na modelu lokalnym, ustaw dokładne nadpisanie modelu opróżniania pamięci:

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "compaction": {        "memoryFlush": {          "model": "ollama/qwen3:8b"        }      }    }  }}
[/code]

Nadpisanie dotyczy tylko przebiegu opróżniania pamięci i nie dziedziczy łańcucha rezerwowego aktywnej sesji.

## Dreaming

Dreaming to opcjonalny przebieg konsolidacji pamięci w tle. Zbiera sygnały krótkoterminowe, ocenia kandydatów i promuje do pamięci długoterminowej (`MEMORY.md`) tylko zakwalifikowane elementy.

Zaprojektowano go tak, aby pamięć długoterminowa miała wysoki stosunek sygnału do szumu:

  * **Opcjonalne** : domyślnie wyłączone.
  * **Zaplanowane** : po włączeniu `memory-core` automatycznie zarządza jednym cyklicznym zadaniem cron dla pełnego przeglądu Dreaming.
  * **Progowe** : promocje muszą przejść bramki wyniku, częstotliwości przypominania i różnorodności zapytań.
  * **Możliwe do przeglądu** : podsumowania faz i wpisy dziennika są zapisywane w `DREAMS.md` do weryfikacji przez człowieka.


Opis zachowania faz, sygnałów punktacji i szczegółów Dream Diary znajdziesz w [Dreaming](</pl/concepts/dreaming>).

## Ugruntowane uzupełnianie i promocja na żywo

System Dreaming ma teraz dwie ściśle powiązane ścieżki przeglądu:

  * **Dreaming na żywo** działa na krótkoterminowym magazynie Dreaming w `memory/.dreams/` i jest tym, czego normalna głęboka faza używa przy podejmowaniu decyzji, co może przejść do `MEMORY.md`.
  * **Ugruntowane uzupełnianie** odczytuje historyczne notatki `memory/YYYY-MM-DD.md` jako samodzielne pliki dzienne i zapisuje ustrukturyzowane wyniki przeglądu w `DREAMS.md`.


Ugruntowane uzupełnianie jest przydatne, gdy chcesz odtworzyć starsze notatki i sprawdzić, co system uznaje za trwałe, bez ręcznej edycji `MEMORY.md`.

Gdy użyjesz:

bashCopy code
[code]
    openclaw memory rem-backfill --path ./memory --stage-short-term
[/code]

ugruntowani trwa­li kandydaci nie są promowani bezpośrednio. Są umieszczani w tym samym krótkoterminowym magazynie Dreaming, którego normalna głęboka faza już używa. Oznacza to, że:

  * `DREAMS.md` pozostaje powierzchnią przeglądu dla człowieka.
  * magazyn krótkoterminowy pozostaje powierzchnią rankingową dla maszyny.
  * `MEMORY.md` nadal jest zapisywany tylko przez głęboką promocję.


Jeśli uznasz, że odtworzenie nie było przydatne, możesz usunąć przygotowane artefakty bez dotykania zwykłych wpisów dziennika ani normalnego stanu przypominania:

bashCopy code
[code]
    openclaw memory rem-backfill --rollbackopenclaw memory rem-backfill --rollback-short-term
[/code]

## CLI

bashCopy code
[code]
    openclaw memory status          # Check index status and provideropenclaw memory search "query"  # Search from the command lineopenclaw memory index --force   # Rebuild the index
[/code]

## Dalsza lektura

  * [Wbudowany silnik pamięci](</pl/concepts/memory-builtin>): domyślny backend SQLite.
  * [Silnik pamięci QMD](</pl/concepts/memory-qmd>): zaawansowany lokalny sidecar.
  * [Pamięć Honcho](</pl/concepts/memory-honcho>): natywna dla AI pamięć między sesjami.
  * [Memory LanceDB](</pl/plugins/memory-lancedb>): Plugin oparty na LanceDB z embeddingami zgodnymi z OpenAI.
  * [Memory Wiki](</pl/plugins/memory-wiki>): skompilowany skarbiec wiedzy i narzędzia natywne dla wiki.
  * [Wyszukiwanie w pamięci](</pl/concepts/memory-search>): potok wyszukiwania, dostawcy i dostrajanie.
  * [Dreaming](</pl/concepts/dreaming>): promocja w tle z krótkoterminowego przypominania do pamięci długoterminowej.
  * [Dokumentacja konfiguracji pamięci](</pl/reference/memory-config>): wszystkie pokrętła konfiguracji.
  * [Compaction](</pl/concepts/compaction>): jak Compaction współdziała z pamięcią.


## Powiązane

  * [Active memory](</pl/concepts/active-memory>)
  * [Wyszukiwanie w pamięci](</pl/concepts/memory-search>)
  * [Wbudowany silnik pamięci](</pl/concepts/memory-builtin>)
  * [Pamięć Honcho](</pl/concepts/memory-honcho>)
  * [Memory LanceDB](</pl/plugins/memory-lancedb>)
  * [Zobowiązania](</pl/concepts/commitments>)


Was this useful?YesNo