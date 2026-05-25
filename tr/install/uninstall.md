---
title: Kaldırma
source_url: https://docs.openclaw.ai/tr/install/uninstall
scraped_at: 2026-05-25
---

İki yol vardır:

  * `openclaw` hâlâ kuruluysa **kolay yol**.
  * CLI gitmiş ama servis hâlâ çalışıyorsa **elle servis kaldırma**.


## Kolay yol (CLI hâlâ kurulu)

Önerilen: yerleşik kaldırıcıyı kullanın:

bashCopy code
[code]
    openclaw uninstall
[/code]

Etkileşimsiz (otomasyon / npx):

bashCopy code
[code]
    openclaw uninstall --all --yes --non-interactivenpx -y openclaw uninstall --all --yes --non-interactive
[/code]

Elle adımlar (aynı sonuç):

  1. Gateway servisini durdurun:

bashCopy code
[code]
    openclaw gateway stop
[/code]

  2. Gateway servisini kaldırın (launchd/systemd/schtasks):

bashCopy code
[code]
    openclaw gateway uninstall
[/code]

  3. Durumu + yapılandırmayı silin:

bashCopy code
[code]
    rm -rf "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}"
[/code]

`OPENCLAW_CONFIG_PATH` değerini durum dizini dışında özel bir konuma ayarladıysanız, o dosyayı da silin.

  4. Çalışma alanınızı silin (isteğe bağlı, agent dosyalarını kaldırır):

bashCopy code
[code]
    rm -rf ~/.openclaw/workspace
[/code]

  5. CLI kurulumunu kaldırın (kullandığınızı seçin):

bashCopy code
[code]
    npm rm -g openclawpnpm remove -g openclawbun remove -g openclaw
[/code]

  6. macOS uygulamasını kurduysanız:

bashCopy code
[code]
    rm -rf /Applications/OpenClaw.app
[/code]

Notlar:

  * Profil kullandıysanız (`--profile` / `OPENCLAW_PROFILE`), 3. adımı her durum dizini için tekrarlayın (varsayılanlar `~/.openclaw-<profile>` şeklindedir).
  * Uzak modda durum dizini **Gateway host** üzerinde bulunur; bu nedenle 1-4. adımları orada da çalıştırın.


## Elle servis kaldırma (CLI kurulu değil)

Gateway servisi çalışmaya devam ediyor ama `openclaw` yoksa bunu kullanın.

### macOS (launchd)

Varsayılan etiket `ai.openclaw.gateway` şeklindedir (veya `ai.openclaw.<profile>`; eski `com.openclaw.*` girişleri hâlâ bulunabilir):

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.gatewayrm -f ~/Library/LaunchAgents/ai.openclaw.gateway.plist
[/code]

Profil kullandıysanız etiket ve plist adını `ai.openclaw.<profile>` ile değiştirin. Mevcutsa eski `com.openclaw.*` plist dosyalarını kaldırın.

### Linux (systemd kullanıcı birimi)

Varsayılan birim adı `openclaw-gateway.service` şeklindedir (veya `openclaw-gateway-<profile>.service`):

bashCopy code
[code]
    systemctl --user disable --now openclaw-gateway.servicerm -f ~/.config/systemd/user/openclaw-gateway.servicesystemctl --user daemon-reload
[/code]

### Windows (Scheduled Task)

Varsayılan görev adı `OpenClaw Gateway` şeklindedir (veya `OpenClaw Gateway (<profile>)`). Görev betiği durum dizininiz altında bulunur.

powershellCopy code
[code]
    schtasks /Delete /F /TN "OpenClaw Gateway"Remove-Item -Force "$env:USERPROFILE\.openclaw\gateway.cmd"
[/code]

Profil kullandıysanız eşleşen görev adını ve `~\.openclaw-<profile>\gateway.cmd` dosyasını silin.

## Normal kurulum ile source checkout farkı

### Normal kurulum ([install.sh](<http://install.sh>) / npm / pnpm / bun)

`https://openclaw.ai/install.sh` veya `install.ps1` kullandıysanız, CLI `npm install -g openclaw@latest` ile kurulmuştur. Bunu `npm rm -g openclaw` ile kaldırın (veya bu şekilde kurduysanız `pnpm remove -g` / `bun remove -g`).

### Source checkout (git clone)

Bir repo checkout'undan çalıştırıyorsanız (`git clone` \+ `openclaw ...` / `bun run openclaw ...`):

  1. Repo'yu silmeden **önce** Gateway servisini kaldırın (yukarıdaki kolay yolu veya elle servis kaldırmayı kullanın).
  2. Repo dizinini silin.
  3. Yukarıda gösterildiği gibi durumu + çalışma alanını kaldırın.


## İlgili

  * [Install overview](</tr/install>)
  * [Migration guide](</tr/install/migrating>)


Was this useful?YesNo