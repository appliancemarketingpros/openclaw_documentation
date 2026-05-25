---
title: Agenten-Bootstrapping
source_url: https://docs.openclaw.ai/de/start/bootstrapping
scraped_at: 2026-05-25
---

Bootstrapping ist das **Erstlauf** -Ritual, das einen Agent-Arbeitsbereich vorbereitet und Identitätsdetails sammelt. Es erfolgt nach dem Onboarding, wenn der Agent zum ersten Mal startet.

## Was Bootstrapping bewirkt

Beim ersten Agent-Lauf richtet OpenClaw den Arbeitsbereich ein (Standard: `~/.openclaw/workspace`):

  * Legt `AGENTS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, `USER.md` an.
  * Führt ein kurzes Frage-und-Antwort-Ritual aus (jeweils eine Frage).
  * Schreibt Identität und Einstellungen in `IDENTITY.md`, `USER.md`, `SOUL.md`.
  * Entfernt `BOOTSTRAP.md` nach Abschluss, damit es nur einmal ausgeführt wird.


Für eingebettete/lokale Modellausführungen hält OpenClaw `BOOTSTRAP.md` aus dem privilegierten Systemkontext heraus. Beim primären interaktiven Erstlauf übergibt es den Dateiinhalt dennoch im Benutzer-Prompt, damit Modelle, die das Tool `read` nicht zuverlässig aufrufen, das Ritual abschließen können. Wenn der aktuelle Lauf nicht sicher auf den Arbeitsbereich zugreifen kann, erhält der Agent stattdessen einen eingeschränkten Bootstrap-Hinweis anstelle einer allgemeinen Begrüßung.

## Bootstrapping überspringen

Um dies für einen vorbefüllten Arbeitsbereich zu überspringen, führen Sie `openclaw onboard --skip-bootstrap` aus.

## Wo es ausgeführt wird

Bootstrapping wird immer auf dem **Gateway-Host** ausgeführt. Wenn die macOS-App eine Verbindung zu einem entfernten Gateway herstellt, befinden sich der Arbeitsbereich und die Bootstrapping-Dateien auf diesem entfernten Rechner.

## Zugehörige Dokumentation

  * macOS-App-Onboarding: [Onboarding](</de/start/onboarding>)
  * Arbeitsbereichslayout: [Agent-Arbeitsbereich](</de/concepts/agent-workspace>)


Was this useful?YesNo