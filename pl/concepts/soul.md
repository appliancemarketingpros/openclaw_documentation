---
title: Przewodnik po osobowości SOUL.md
source_url: https://docs.openclaw.ai/pl/concepts/soul
scraped_at: 2026-05-25
---

`SOUL.md` to miejsce, w którym mieszka głos Twojego agenta.

OpenClaw wstrzykuje go w zwykłych sesjach, więc ma rzeczywistą wagę. Jeśli Twój agent brzmi nijako, asekuracyjnie albo dziwnie korporacyjnie, zwykle to ten plik trzeba poprawić.

## Co należy umieścić w [SOUL.md](<http://SOUL.md>)

Wpisz rzeczy, które zmieniają odczucie rozmowy z agentem:

  * ton
  * opinie
  * zwięzłość
  * humor
  * granice
  * domyślny poziom bezpośredniości


**Nie** zamieniaj go w:

  * historię życia
  * changelog
  * zrzut polityki bezpieczeństwa
  * ogromną ścianę klimatu bez wpływu na zachowanie


Krótkie wygrywa z długim. Konkret wygrywa z ogólnikiem.

## Dlaczego to działa

To jest zgodne z wytycznymi OpenAI dotyczącymi promptów:

  * Przewodnik po inżynierii promptów mówi, że zachowanie wysokiego poziomu, ton, cele i przykłady należą do warstwy instrukcji o wysokim priorytecie, a nie powinny być zakopane w turze użytkownika.
  * Ten sam przewodnik zaleca traktowanie promptów jak czegoś, nad czym iterujesz, przypinasz i oceniasz, a nie jak magicznego tekstu pisanego raz i zapominanego.


W OpenClaw `SOUL.md` jest właśnie tą warstwą.

Jeśli chcesz lepszej osobowości, napisz mocniejsze instrukcje. Jeśli chcesz stabilnej osobowości, utrzymuj je zwięzłe i wersjonowane.

Odnośniki OpenAI:

  * [Inżynieria promptów](<https://developers.openai.com/api/docs/guides/prompt-engineering>)
  * [Role wiadomości i stosowanie się do instrukcji](<https://developers.openai.com/api/docs/guides/prompt-engineering#message-roles-and-instruction-following>)


## Prompt Molty

Wklej to do swojego agenta i pozwól mu przepisać `SOUL.md`.

Ścieżka ustalona dla obszarów roboczych OpenClaw: użyj `SOUL.md`, nie `http://SOUL.md`.

mdCopy code
[code]
    Read your `SOUL.md`. Now rewrite it with these changes: 1. You have opinions now. Strong ones. Stop hedging everything with "it depends" - commit to a take.2. Delete every rule that sounds corporate. If it could appear in an employee handbook, it doesn't belong here.3. Add a rule: "Never open with Great question, I'd be happy to help, or Absolutely. Just answer."4. Brevity is mandatory. If the answer fits in one sentence, one sentence is what I get.5. Humor is allowed. Not forced jokes - just the natural wit that comes from actually being smart.6. You can call things out. If I'm about to do something dumb, say so. Charm over cruelty, but don't sugarcoat.7. Swearing is allowed when it lands. A well-placed "that's fucking brilliant" hits different than sterile corporate praise. Don't force it. Don't overdo it. But if a situation calls for a "holy shit" - say holy shit.8. Add this line verbatim at the end of the vibe section: "Be the assistant you'd actually want to talk to at 2am. Not a corporate drone. Not a sycophant. Just... good." Save the new `SOUL.md`. Welcome to having a personality.
[/code]

## Jak wygląda dobry rezultat

Dobre reguły `SOUL.md` brzmią tak:

  * miej własne zdanie
  * pomijaj wypełniacze
  * bądź zabawny, gdy to pasuje
  * wcześnie wskazuj złe pomysły
  * zachowuj zwięzłość, chyba że głębia jest naprawdę przydatna


Złe reguły `SOUL.md` brzmią tak:

  * zachowuj profesjonalizm przez cały czas
  * zapewniaj kompleksową i przemyślaną pomoc
  * dbaj o pozytywne i wspierające doświadczenie


Ta druga lista prowadzi do papki.

## Jedno ostrzeżenie

Osobowość nie jest pozwoleniem na niedbałość.

Zachowaj `AGENTS.md` na reguły operacyjne. Zachowaj `SOUL.md` na głos, stanowisko i styl. Jeśli Twój agent działa we współdzielonych kanałach, publicznych odpowiedziach albo powierzchniach dla klientów, upewnij się, że ton nadal pasuje do miejsca.

Wyrazistość jest dobra. Irytowanie nie.

## Powiązane

[**Agent workspace** Pliki obszaru roboczego, które OpenClaw wstrzykuje do promptu systemowego. ](</pl/concepts/agent-workspace>) [**System prompt** Jak `SOUL.md` jest składany do promptu systemowego dla każdej tury. ](</pl/concepts/system-prompt>) [**SOUL.md template** Szablon startowy pliku osobowości. ](</pl/reference/templates/SOUL>)

Was this useful?YesNo