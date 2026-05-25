---
title: macOS-VMs
source_url: https://docs.openclaw.ai/de/install/macos-vm
scraped_at: 2026-05-25
---

## Empfohlener Standard (die meisten Benutzer)

  * **Kleiner Linux-VPS** für ein dauerhaft laufendes Gateway und geringe Kosten. Siehe [VPS-Hosting](</de/vps>).
  * **Dedizierte Hardware** (Mac mini oder Linux-Rechner), wenn Sie volle Kontrolle und eine **Residential-IP** für Browser-Automatisierung wünschen. Viele Websites blockieren Rechenzentrums-IPs, daher funktioniert lokales Browsing oft besser.
  * **Hybrid:** Lassen Sie das Gateway auf einem günstigen VPS laufen und verbinden Sie Ihren Mac als **Node** , wenn Sie Browser-/UI-Automatisierung benötigen. Siehe [Nodes](</de/nodes>) und [Gateway remote](</de/gateway/remote>).


Verwenden Sie eine macOS-VM, wenn Sie ausdrücklich macOS-spezifische Funktionen wie iMessage benötigen oder eine strikte Isolation von Ihrem täglichen Mac wünschen.

## macOS-VM-Optionen

### Lokale VM auf Ihrem Apple-Silicon-Mac (Lume)

Führen Sie OpenClaw in einer sandboxierten macOS-VM auf Ihrem vorhandenen Apple-Silicon-Mac mit [Lume](<https://cua.ai/docs/lume>) aus.

Das bietet Ihnen:

  * Vollständige macOS-Umgebung in Isolation (Ihr Host bleibt sauber)
  * iMessage-Unterstützung über `imsg` (der standardmäßige lokale Pfad ist unter Linux/Windows nicht möglich)
  * Sofortiges Zurücksetzen durch Klonen von VMs
  * Keine zusätzliche Hardware oder Cloud-Kosten


### Gehostete Mac-Provider (Cloud)

Wenn Sie macOS in der Cloud nutzen möchten, funktionieren gehostete Mac-Provider ebenfalls:

  * [MacStadium](<https://www.macstadium.com/>) (gehostete Macs)
  * Andere gehostete Mac-Anbieter funktionieren ebenfalls; folgen Sie deren VM- und SSH-Dokumentation


Sobald Sie SSH-Zugriff auf eine macOS-VM haben, fahren Sie unten mit Schritt 6 fort.

* * *

## Schneller Weg (Lume, erfahrene Benutzer)

  1. Lume installieren
  2. `lume create openclaw --os macos --ipsw latest`
  3. Einrichtungsassistenten abschließen, Remote Login (SSH) aktivieren
  4. `lume run openclaw --no-display`
  5. Per SSH anmelden, OpenClaw installieren, Kanäle konfigurieren
  6. Fertig


* * *

## Was Sie benötigen (Lume)

  * Apple-Silicon-Mac (M1/M2/M3/M4)
  * macOS Sequoia oder neuer auf dem Host
  * ~60 GB freier Speicherplatz pro VM
  * ~20 Minuten


* * *

## 1) Lume installieren

bashCopy code
[code]
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
[/code]

Wenn `~/.local/bin` nicht in Ihrem PATH ist:

bashCopy code
[code]
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.zshrc && source ~/.zshrc
[/code]

Überprüfen:

bashCopy code
[code]
    lume --version
[/code]

Dokumentation: [Lume Installation](<https://cua.ai/docs/lume/guide/getting-started/installation>)

* * *

## 2) Die macOS-VM erstellen

bashCopy code
[code]
    lume create openclaw --os macos --ipsw latest
[/code]

Dies lädt macOS herunter und erstellt die VM. Ein VNC-Fenster wird automatisch geöffnet.

* * *

## 3) Einrichtungsassistenten abschließen

Im VNC-Fenster:

  1. Sprache und Region auswählen
  2. Apple-ID überspringen (oder anmelden, wenn Sie iMessage später verwenden möchten)
  3. Benutzerkonto erstellen (Benutzername und Passwort merken)
  4. Alle optionalen Funktionen überspringen


Aktivieren Sie nach Abschluss der Einrichtung SSH:

  1. Systemeinstellungen → Allgemein → Teilen öffnen
  2. „Remote Login“ aktivieren


* * *

## 4) IP-Adresse der VM abrufen

bashCopy code
[code]
    lume get openclaw
[/code]

Suchen Sie nach der IP-Adresse (normalerweise `192.168.64.x`).

* * *

## 5) Per SSH mit der VM verbinden

bashCopy code
[code]
    ssh youruser@192.168.64.X
[/code]

Ersetzen Sie `youruser` durch das von Ihnen erstellte Konto und die IP durch die IP Ihrer VM.

* * *

## 6) OpenClaw installieren

Innerhalb der VM:

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Folgen Sie den Onboarding-Eingabeaufforderungen, um Ihren Modell-Provider einzurichten (Anthropic, OpenAI usw.).

* * *

## 7) Kanäle konfigurieren

Bearbeiten Sie die Konfigurationsdatei:

bashCopy code
[code]
    nano ~/.openclaw/openclaw.json
[/code]

Fügen Sie Ihre Kanäle hinzu:

json5Copy code
[code]
    {  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551234567"],    },    telegram: {      botToken: "YOUR_BOT_TOKEN",    },  },}
[/code]

Melden Sie sich dann bei WhatsApp an (QR scannen):

bashCopy code
[code]
    openclaw channels login
[/code]

* * *

## 8) Die VM headless ausführen

Stoppen Sie die VM und starten Sie sie ohne Anzeige neu:

bashCopy code
[code]
    lume stop openclawlume run openclaw --no-display
[/code]

Die VM läuft im Hintergrund. Der Daemon von OpenClaw hält das Gateway am Laufen.

Status prüfen:

bashCopy code
[code]
    ssh youruser@192.168.64.X "openclaw status"
[/code]

* * *

## Bonus: iMessage-Integration

Dies ist die Hauptfunktion beim Betrieb unter macOS. Verwenden Sie [iMessage](</de/channels/imessage>) mit `imsg`, um Nachrichten zu OpenClaw hinzuzufügen.

Innerhalb der VM:

  1. Bei Nachrichten anmelden.
  2. `imsg` installieren.
  3. Vollzugriff auf die Festplatte und Automatisierungsberechtigung für den Prozess gewähren, der OpenClaw/`imsg` ausführt.
  4. RPC-Unterstützung mit `imsg rpc --help` überprüfen.


Zu Ihrer OpenClaw-Konfiguration hinzufügen:

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "imsg",      dbPath: "~/Library/Messages/chat.db",    },  },}
[/code]

Starten Sie das Gateway neu. Jetzt kann Ihr Agent iMessages senden und empfangen.

Vollständige Einrichtungsdetails: [iMessage-Kanal](</de/channels/imessage>)

* * *

## Golden Image speichern

Erstellen Sie vor weiterer Anpassung einen Snapshot Ihres sauberen Zustands:

bashCopy code
[code]
    lume stop openclawlume clone openclaw openclaw-golden
[/code]

Jederzeit zurücksetzen:

bashCopy code
[code]
    lume stop openclaw && lume delete openclawlume clone openclaw-golden openclawlume run openclaw --no-display
[/code]

* * *

## 24/7-Betrieb

Halten Sie die VM am Laufen, indem Sie:

  * Ihren Mac am Stromnetz angeschlossen lassen
  * den Ruhezustand in Systemeinstellungen → Energiesparen deaktivieren
  * bei Bedarf `caffeinate` verwenden


Für echten Dauerbetrieb sollten Sie einen dedizierten Mac mini oder einen kleinen VPS in Betracht ziehen. Siehe [VPS-Hosting](</de/vps>).

* * *

## Fehlerbehebung

Problem | Lösung  
---|---  
SSH-Verbindung zur VM nicht möglich | Prüfen Sie, ob „Remote Login“ in den Systemeinstellungen der VM aktiviert ist  
VM-IP wird nicht angezeigt | Warten Sie, bis die VM vollständig gestartet ist, und führen Sie `lume get openclaw` erneut aus  
Lume-Befehl nicht gefunden | Fügen Sie `~/.local/bin` zu Ihrem PATH hinzu  
WhatsApp-QR wird nicht gescannt | Stellen Sie sicher, dass Sie in der VM angemeldet sind (nicht auf dem Host), wenn Sie `openclaw channels login` ausführen  
  
* * *

## Zugehörige Dokumentation

  * [VPS-Hosting](</de/vps>)
  * [Nodes](</de/nodes>)
  * [Gateway remote](</de/gateway/remote>)
  * [iMessage-Kanal](</de/channels/imessage>)
  * [Lume Quickstart](<https://cua.ai/docs/lume/guide/getting-started/quickstart>)
  * [Lume CLI-Referenz](<https://cua.ai/docs/lume/reference/cli-reference>)
  * [Unbeaufsichtigte VM-Einrichtung](<https://cua.ai/docs/lume/guide/fundamentals/unattended-setup>) (fortgeschritten)
  * [Docker-Sandboxing](</de/install/docker>) (alternativer Isolationsansatz)


Was this useful?YesNo