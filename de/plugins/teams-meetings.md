---
title: Microsoft Teams-Besprechungs-Plugin
source_url: https://docs.openclaw.ai/de/plugins/teams-meetings
scraped_at: 2026-10-12
---

CapabilitiesPlugin guides

Das `teams-meetings`-Plugin tritt Microsoft Teams-Links als Gast im OpenClaw-Chrome-Profil bei. Es akzeptiert geschäftliche Links unter `teams.microsoft.com/l/meetup-join/...` und Links für Privatkunden unter `teams.live.com/meet/...`. Es erstellt keine Besprechungen, wählt sich nicht ein, ruft Microsoft Graph nicht auf und zeichnet weder Audio noch Video auf.

## Einrichtung

Die Sprachausgabe verwendet dieselben lokalen Audiovoraussetzungen wie das [Google Meet-Plugin](</de/plugins/google-meet>): macOS, das virtuelle Audiogerät `BlackHole 2ch` und SoX.

bashCopy code
[code]
    brew install blackhole-2ch soxsudo rebootsystem_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

Das Plugin ist enthalten und standardmäßig aktiviert. Fügen Sie nur dann einen Eintrag hinzu, wenn Sie es anpassen möchten, und prüfen Sie anschließend die Einrichtung:

json5Copy code
[code]
    {  plugins: {    entries: {      "teams-meetings": {        config: {          defaultMode: "agent",          chrome: { guestName: "OpenClaw Agent" },        },      },    },  },}
[/code]

Führen Sie `openclaw plugins disable teams-meetings` aus, wenn das Plugin nicht aktiv sein soll.

bashCopy code
[code]
    openclaw teamsmeetings setupopenclaw teamsmeetings join 'https://teams.microsoft.com/l/meetup-join/...'
[/code]

Verwenden Sie `chromeNode.node`, um Chrome, BlackHole und SoX auf einer gekoppelten macOS-Node auszuführen. Die Node muss `teamsmeetings.chrome` und `browser.proxy` zulassen.

## Modi

Modus | Verhalten  
---|---  
`agent` | Die Echtzeittranskription konsultiert den konfigurierten OpenClaw-Agenten; TTS antwortet.  
`bidi` | Ein Echtzeit-Sprachmodell hört zu und antwortet direkt.  
`transcribe` | Beitritt nur zur Beobachtung mit Momentaufnahmen des Live-Untertiteltranskripts.  
  
Teams-Liveuntertitel werden nach der Zulassung in jedem Modus aktiviert, damit OpenClaw Notizen mit Sprecherzuordnung dauerhaft speichern kann. Die Aktion `transcript` gibt weiterhin nur für `transcribe`-Sitzungen den begrenzten Live-Puffer zurück. Beim Verlassen speichert OpenClaw das dauerhafte Transkript und die daraus abgeleitete Zusammenfassung in der gemeinsamen Zustandsdatenbank; listen oder exportieren Sie diese mit [`openclaw transcripts`](</de/cli/transcripts>).

Automatische Notizen sind standardmäßig aktiviert. Setzen Sie `transcripts.enabled: false`, um dauerhafte Notizen global zu deaktivieren; der explizite Modus `transcribe` stellt weiterhin nur seinen begrenzten Live-Ausschnitt bereit.

## Einschränkungen beim Gastbeitritt

Der Browseradapter schließt den App-Zwischenbildschirm, trägt den Gastnamen ein, schaltet die Kamera aus, konfiguriert das Mikrofon für den ausgewählten Modus und klickt auf die Schaltfläche zum Beitritt. Im Anrufstatus wird das Steuerelement zum Auflegen verwendet; bei Lobby-, Mandantenanmeldungs- und Geräteberechtigungsstatus werden eindeutige Gründe für erforderliche manuelle Aktionen zurückgegeben. Weiterleitungen des Startprogramms für Besprechungen für Privatkunden und die von Chrome angezeigten `BlackHole 2ch (Virtual)`-Beschriftungen werden unterstützt.

Die Teams-Mandantenrichtlinie kann eine Anmeldung, E-Mail-Verifizierung oder Zulassung durch den Organisator erfordern. Führen Sie diesen Schritt im OpenClaw-Chrome-Profil aus und prüfen Sie anschließend erneut den Status oder die Sprachausgabe. Das Plugin umgeht die Mandantenrichtlinie nicht.

Der Teams-Webclient für Privatkunden wurde für den App-Zwischenbildschirm, die Eingabe des Gastnamens, Mikrofon-/Kamera-Umschalter vor dem Beitritt, den Beitritt, die Zulassung aus der Lobby, Medienberechtigungen, die Erkennung laufender Anrufe, Liveuntertitel, die Ein-/Ausgabeweiterleitung über BlackHole, das Verlassen und die Erkennung nach dem Anruf live validiert. Geschäftliche Mandanten können abweichende Richtlinien für Anmeldung, E-Mail-Verifizierung, Zulassung und Bestätigung beim Verlassen durchsetzen; führen Sie alle gemeldeten manuellen Aktionen im OpenClaw-Chrome-Profil aus.

## Tool- und Gateway-Oberfläche

Das Agenten-Tool `teams_meetings` unterstützt `join`, `leave`, `status`, `transcript` und `speak`. Gateway-Methoden verwenden das Präfix `teamsmeetings.*`. Der Node-Befehl lautet `teamsmeetings.chrome`.

## Verwandte Themen

  * [Übersicht über Besprechungs-Plugins](</de/plugins/meeting-plugins>)
  * [Microsoft Teams-Kanal](</de/channels/msteams>)


Was this useful?YesNo

Open issue