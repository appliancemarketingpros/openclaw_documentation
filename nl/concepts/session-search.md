---
title: Sessies zoeken
source_url: https://docs.openclaw.ai/nl/concepts/session-search
scraped_at: 2026-07-20
---

AgentsSessions and memory

# Sessies doorzoeken

`sessions_search` doorzoekt de tekst van de gebruiker en de assistent in je eigen eerdere sessies. Elk resultaat bevat een `sessionKey`, tijdstempel, rol en een kort overeenkomend fragment. Geef de geretourneerde `sessionKey` door aan `sessions_history` wanneer je de omringende conversatie nodig hebt.

## Zichtbaarheid en uitvoer

De zoekfunctie gebruikt dezelfde regels voor sessiezichtbaarheid als `sessions_history`. Resultaten buiten de zichtbare sessieboom van de aanroeper worden verwijderd voordat de resultaatlimieten worden toegepast. Agents in een sandbox blijven beperkt tot sessies die ze zelf hebben gestart wanneer zichtbaarheid van gestarte sessies is ingeschakeld.

Fragmenten worden geredigeerd voordat ze aan het model worden geretourneerd. Resultaten worden ook begrensd op aantal, fragmentlengte en totale responsgrootte.

## Levenscyclus van de index

OpenClaw slaat een volledige-tekstindex op naast de transcriptierijen in de SQLite-database van elke agent. Nieuwe berichten van gebruikers en assistenten worden geïndexeerd in dezelfde transactie waarin ze worden opgeslagen, zodat de index nooit achterloopt op actieve conversaties; toolresultaten, redeneerblokken en afbeeldingen worden uitgesloten. Alleen de actieve tak van het transcript kan worden doorzocht.

Transcripties van vóór de index (bijvoorbeeld sessies die zijn geïmporteerd door `openclaw doctor`) en sessies waarvan de actieve tak is teruggedraaid, worden opnieuw geïndexeerd door een afstemming op de achtergrond die bij de volgende zoekopdracht begint. Een respons met `indexing: true` kan daarom onvolledig zijn; probeer het opnieuw nadat het indexeren is voltooid. Als een sessie wordt verwijderd, worden de bijbehorende indexvermeldingen in dezelfde transactie verwijderd.

De zoekfunctie gebruikt momenteel SQLite's Unicode-woordtokenizer met verwijdering van diakritische tekens. Trigramtokenisatie voor het vinden van CJK-deeltekenreeksen is een toekomstige verbetering.

## Sessies doorzoeken versus geheugen doorzoeken

Gebruik `sessions_search` voor exacte woorden of woordgroepen uit onbewerkte sessietranscripties. Gebruik [`memory_search`](</nl/concepts/memory-search>) voor duurzame geheugenbestanden en semantisch ophalen. Het experimentele sessiegeheugencorpus is de semantische aanvulling op deze exacte zoekfunctie voor transcripties.

Was this useful?YesNo

Open issue