---
title: Kartu skor kematangan
source_url: https://docs.openclaw.ai/id/maturity/scorecard
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Kartu skor kematangan

kesiapan rilis - dibuat dari taksonomi + bukti QA

Tampilan praktis tentang apa yang siap, apa yang terbukti, dan apa yang masih perlu dikerjakan.

50 permukaan - 281 area kapabilitas - cakupan deterministik ditambah kualitas dan kelengkapan yang ditinjau manusia.

Telusuri permukaan / Periksa bukti QA / [Baca taksonomi](</id/maturity/taxonomy>)

## Tujuan halaman ini

Gunakan halaman ini untuk menjawab satu pertanyaan: permukaan OpenClaw mana yang merupakan pilihan kredibel untuk rilis, dan bukti apa yang mendukung penilaian tersebut? Cakupan berasal dari bukti QA deterministik; kualitas dan kelengkapan dipelihara sebagai skor kematangan yang telah ditinjau.

## Sekilas

67% Skor kematangan

Alfa Kualitas + kelengkapan Cakupan Eksperimental - 4% Kualitas Alfa - 63% Kelengkapan Beta - 70%

Cakupan sengaja dipandu oleh bukti: sebuah area tidak menjadi "siap" hanya karena implementasinya ada. Ini bukan masukan untuk skor kematangan, tetapi OpenClaw bertujuan mempertahankan cakupan end-to-end di atas 90% untuk fitur matang tingkat Stabil atau lebih baik seiring waktu.

## Rentang skor

Eksperimental0-50%

Alfa50-70%

Beta70-80%

Stabil80-95%

Clawesome95-100%

## Penjelajah permukaan

Permukaan diurutkan berdasarkan tingkat kematangan, kelengkapan, dan kualitas. Dukungan LTS ditampilkan bersama setiap baris agar opsi yang siap rilis mudah dibandingkan.

### Semua permukaan

[CLIM4Stabil7 area](</id/maturity/taxonomy#cli>)

CakupanEksperimental4%

KualitasStabil83%

KelengkapanStabil90%

Parsial - 6

[Runtime GatewayM4Stabil13 area](</id/maturity/taxonomy#gateway-runtime>)

CakupanEksperimental6%

KualitasStabil81%

KelengkapanStabil89%

Parsial - 12

[Host Gateway LinuxM4Stabil5 area](</id/maturity/taxonomy#linux-gateway-host>)

CakupanEksperimental0%

KualitasBeta75%

KelengkapanStabil89%

Parsial - 4

[Host Gateway macOSM4Stabil7 area](</id/maturity/taxonomy#macos-gateway-host>)

CakupanEksperimental0%

KualitasBeta74%

KelengkapanStabil88%

Tidak ada

[DiscordM4Stabil6 area](</id/maturity/taxonomy#discord>)

CakupanEksperimental0%

KualitasBeta73%

KelengkapanStabil87%

Parsial - 4

[Runtime AgenM3Beta9 area](</id/maturity/taxonomy#agent-runtime>)

CakupanEksperimental33%

KualitasBeta78%

KelengkapanBeta79%

Parsial - 6

[Mesin sesi, memori, dan konteksM3Beta9 area](</id/maturity/taxonomy#session-memory-and-context-engine>)

CakupanEksperimental30%

KualitasBeta77%

KelengkapanBeta79%

Sebagian - 6

[Kerangka kerja saluranM3Beta8 area](</id/maturity/taxonomy#channel-framework>)

CakupanEksperimental13%

KualitasBeta76%

KelengkapanBeta79%

Sebagian - 5

[Alat otomatisasi browser, exec, dan sandboxM3Beta3 area](</id/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

CakupanEksperimental21%

KualitasBeta75%

KelengkapanBeta79%

Sebagian - 2

[ObservabilitasM3Beta5 area](</id/maturity/taxonomy#observability>)

CakupanEksperimental18%

KualitasBeta75%

KelengkapanBeta79%

Sebagian - 3

[Jalur penyedia OpenAI dan CodexM3Beta5 area](</id/maturity/taxonomy#openai-and-codex-provider-path>)

CakupanEksperimental26%

KualitasBeta74%

KelengkapanBeta79%

Sebagian - 3

[Aplikasi Web GatewayM3Beta6 area](</id/maturity/taxonomy#gateway-web-app>)

CakupanEksperimental4%

KualitasBeta74%

KelengkapanBeta79%

Tidak ada

[Alat pencarian webM3Beta4 area](</id/maturity/taxonomy#web-search-tools>)

CakupanEksperimental9%

KualitasBeta74%

KelengkapanBeta79%

Tidak ada

[PluginM3Beta9 area](</id/maturity/taxonomy#plugins>)

CakupanEksperimental12%

KualitasBeta72%

KelengkapanBeta79%

Sebagian - 7

[Keamanan, autentikasi, penyandingan, dan rahasiaM3Beta6 area](</id/maturity/taxonomy#security-auth-pairing-and-secrets>)

CakupanEksperimental16%

KualitasBeta72%

KelengkapanBeta79%

Sebagian - 5

[Automasi: Cron, hook, tugas, pollingM3Beta6 area](</id/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

CakupanEksperimental2%

KualitasBeta72%

KelengkapanBeta79%

Tidak ada

[Hosting Docker dan PodmanM3Beta4 area](</id/maturity/taxonomy#docker-and-podman-hosting>)

CakupanEksperimental7%

KualitasBeta71%

KelengkapanBeta79%

Tidak ada

[Windows melalui WSL2M3Beta6 area](</id/maturity/taxonomy#windows-via-wsl2>)

CakupanEksperimental6%

KualitasAlfa69%

KelengkapanBeta79%

Sebagian - 5

[Raspberry Pi dan perangkat Linux kecilM3Beta4 area](</id/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

CakupanEksperimental0%

KualitasAlfa67%

KelengkapanBeta79%

Tidak ada

[Jalur penyedia AnthropicM3Beta5 area](</id/maturity/taxonomy#anthropic-provider-path>)

CakupanEksperimental0%

KualitasBeta71%

KelengkapanBeta78%

Tidak ada

[TelegramM3Beta5 area](</id/maturity/taxonomy#telegram>)

CakupanEksperimental0%

KualitasAlfa68%

KelengkapanBeta78%

Penuh - 5

[SlackM3Beta5 area](</id/maturity/taxonomy#slack>)

CakupanEksperimental0%

KualitasAlfa66%

KelengkapanBeta78%

Penuh - 5

[Jalur penyedia GoogleM3Beta5 area](</id/maturity/taxonomy#google-provider-path>)

CakupanEksperimental0%

KualitasAlfa66%

KelengkapanBeta78%

Tidak ada

[iMessage dan BlueBubblesM3Beta5 area](</id/maturity/taxonomy#imessage-and-bluebubbles>)

CakupanEksperimental0%

KualitasAlfa66%

KelengkapanBeta78%

Tidak ada

[Aplikasi pendamping macOSM3Beta8 area](</id/maturity/taxonomy#macos-companion-app>)

CakupanEksperimental0%

KualitasAlfa66%

KelengkapanBeta78%

Tidak ada

[Jalur penyedia OpenRouterM3Beta4 area](</id/maturity/taxonomy#openrouter-provider-path>)

CakupanEksperimental0%

KualitasAlpha66%

KelengkapanBeta78%

Tidak ada

[WhatsAppM3Beta5 area](</id/maturity/taxonomy#whatsapp>)

CakupanEksperimental0%

KualitasAlpha66%

KelengkapanBeta78%

Tidak ada

[Pemahaman media dan pembuatan mediaM2Alpha6 area](</id/maturity/taxonomy#media-understanding-and-media-generation>)

CakupanEksperimental2%

KualitasAlpha64%

KelengkapanAlpha68%

Tidak ada

[Alat pembuatan gambar, video, dan musikM2Alpha5 area](</id/maturity/taxonomy#image-video-and-music-generation-tools>)

CakupanEksperimental0%

KualitasAlpha61%

KelengkapanAlpha68%

Tidak ada

[Penyedia model lokal: Ollama, vLLM, SGLang, LM StudioM2Alpha5 area](</id/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

CakupanEksperimental0%

KualitasAlpha61%

KelengkapanAlpha68%

Tidak ada

[Penyedia terhosting berekor panjangM2Alpha3 area](</id/maturity/taxonomy#long-tail-hosted-providers>)

CakupanEksperimental0%

KualitasAlpha61%

KelengkapanAlpha68%

Tidak ada

[Suara dan percakapan waktu nyataM2Alfa6 area](</id/maturity/taxonomy#voice-and-realtime-talk>)

CakupanEksperimental0%

KualitasAlfa61%

KelengkapanAlfa68%

Tidak ada

[MatrixM2Alfa6 area](</id/maturity/taxonomy#matrix>)

CakupanEksperimental0%

KualitasAlfa60%

KelengkapanAlfa67%

Tidak ada

[Aplikasi AndroidM2Alfa7 area](</id/maturity/taxonomy#android-app>)

CakupanEksperimental0%

KualitasAlfa59%

KelengkapanAlfa66%

Tidak ada

[Google ChatM2Alfa5 area](</id/maturity/taxonomy#google-chat>)

CakupanEksperimental0%

KualitasAlfa59%

KelengkapanAlfa66%

Tidak ada

[Microsoft TeamsM2Alfa5 area](</id/maturity/taxonomy#microsoft-teams>)

CakupanEksperimental0%

KualitasAlfa59%

KelengkapanAlfa66%

Tidak ada

[SignalM2Alfa5 area](</id/maturity/taxonomy#signal>)

CakupanEksperimental0%

KualitasAlfa59%

KelengkapanAlfa66%

Tidak ada

[TUIM2Alfa5 area](</id/maturity/taxonomy#tui>)

CakupanEksperimental0%

KualitasAlpha59%

KelengkapanAlpha66%

Tidak ada

[Windows NativeM2Alpha4 area](</id/maturity/taxonomy#native-windows>)

CakupanEksperimental0%

KualitasAlpha58%

KelengkapanAlpha66%

Sebagian - 1

[ClawHubM2Alpha4 area](</id/maturity/taxonomy#clawhub>)

CakupanEksperimental0%

KualitasAlpha58%

KelengkapanAlpha62%

Tidak ada

[Hosting KubernetesM2Alpha4 area](</id/maturity/taxonomy#kubernetes-hosting>)

CakupanEksperimental0%

KualitasAlpha55%

KelengkapanAlpha61%

Tidak ada

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, kanal regionalM2Alpha4 area](</id/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

CakupanEksperimental0%

KualitasAlpha55%

KelengkapanAlpha58%

Tidak ada

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alpha4 area](</id/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

CakupanEksperimental0%

KualitasAlpha53%

KelengkapanAlpha54%

Tidak ada

[OpenClaw App SDKM2Alpha6 area](</id/maturity/taxonomy#openclaw-app-sdk>)

CakupanEksperimental3%

KualitasAlfa54%

KelengkapanAlfa53%

Tidak ada

[aplikasi iOSM1Eksperimental8 area](</id/maturity/taxonomy#ios-app>)

CakupanEksperimental0%

KualitasEksperimental41%

KelengkapanEksperimental44%

Tidak ada

[jalur instalasi NixM1Eksperimental5 area](</id/maturity/taxonomy#nix-install-path>)

CakupanEksperimental0%

KualitasEksperimental41%

KelengkapanEksperimental44%

Tidak ada

[saluran Panggilan SuaraM1Eksperimental5 area](</id/maturity/taxonomy#voice-call-channel>)

CakupanEksperimental0%

KualitasEksperimental41%

KelengkapanEksperimental44%

Tidak ada

[permukaan pendamping watchOSM1Eksperimental5 area](</id/maturity/taxonomy#watchos-companion-surfaces>)

CakupanEksperimental0%

KualitasEksperimental41%

KelengkapanEksperimental44%

Tidak ada

[aplikasi pendamping LinuxM0Direncanakan5 area](</id/maturity/taxonomy#linux-companion-app>)

CakupanEksperimental0%

KualitasEksperimental19%

KelengkapanEksperimental21%

Tidak ada

[aplikasi pendamping Windows nativeM0Direncanakan5 area](</id/maturity/taxonomy#native-windows-companion-app>)

CakupanEksperimental0%

KualitasEksperimental19%

KelengkapanEksperimental21%

Tidak ada

### Inti

[CLIM4Stabil7 area](</id/maturity/taxonomy#cli>)

CakupanEksperimental4%

KualitasStabil83%

KelengkapanStabil90%

Sebagian - 6

[Runtime GatewayM4Stabil13 area](</id/maturity/taxonomy#gateway-runtime>)

CakupanEksperimental6%

KualitasStabil81%

KelengkapanStabil89%

Sebagian - 12

[Runtime AgenM3Beta9 area](</id/maturity/taxonomy#agent-runtime>)

CakupanEksperimental33%

KualitasBeta78%

KelengkapanBeta79%

Sebagian - 6

[Mesin sesi, memori, dan konteksM3Beta9 area](</id/maturity/taxonomy#session-memory-and-context-engine>)

CakupanEksperimental30%

KualitasBeta77%

KelengkapanBeta79%

Sebagian - 6

[Kerangka kerja saluranM3Beta8 area](</id/maturity/taxonomy#channel-framework>)

CakupanEksperimental13%

KualitasBeta76%

KelengkapanBeta79%

Sebagian - 5

[ObservabilitasM3Beta5 area](</id/maturity/taxonomy#observability>)

CakupanEksperimental18%

KualitasBeta75%

KelengkapanBeta79%

Parsial - 3

[Aplikasi Web GatewayM3Beta6 area](</id/maturity/taxonomy#gateway-web-app>)

CakupanEksperimental4%

KualitasBeta74%

KelengkapanBeta79%

Tidak ada

[PluginM3Beta9 area](</id/maturity/taxonomy#plugins>)

CakupanEksperimental12%

KualitasBeta72%

KelengkapanBeta79%

Parsial - 7

[Keamanan, autentikasi, pemasangan, dan rahasiaM3Beta6 area](</id/maturity/taxonomy#security-auth-pairing-and-secrets>)

CakupanEksperimental16%

KualitasBeta72%

KelengkapanBeta79%

Parsial - 5

[Automasi: Cron, hook, tugas, pollingM3Beta6 area](</id/maturity/taxonomy#automation-cron-hooks-tasks-polling>)

CakupanEksperimental2%

KualitasBeta72%

KelengkapanBeta79%

Tidak ada

[Pemahaman media dan pembuatan mediaM2Alpha6 area](</id/maturity/taxonomy#media-understanding-and-media-generation>)

CakupanEksperimental2%

KualitasAlpha64%

KelengkapanAlpha68%

Tidak ada

[Suara dan percakapan waktu nyataM2Alpha6 area](</id/maturity/taxonomy#voice-and-realtime-talk>)

CakupanEksperimental0%

KualitasAlpha61%

KelengkapanAlpha68%

Tidak ada

[TUIM2Alfa5 area](</id/maturity/taxonomy#tui>)

CakupanEksperimental0%

KualitasAlfa59%

KelengkapanAlfa66%

Tidak ada

[ClawHubM2Alfa4 area](</id/maturity/taxonomy#clawhub>)

CakupanEksperimental0%

KualitasAlfa58%

KelengkapanAlfa62%

Tidak ada

[SDK Aplikasi OpenClawM2Alfa6 area](</id/maturity/taxonomy#openclaw-app-sdk>)

CakupanEksperimental3%

KualitasAlfa54%

KelengkapanAlfa53%

Tidak ada

### Platform

[host Gateway LinuxM4Stabil5 area](</id/maturity/taxonomy#linux-gateway-host>)

CakupanEksperimental0%

KualitasBeta75%

KelengkapanStabil89%

Parsial - 4

[host Gateway macOSM4Stabil7 area](</id/maturity/taxonomy#macos-gateway-host>)

CakupanEksperimental0%

KualitasBeta74%

KelengkapanStabil88%

Tidak ada

[hosting Docker dan PodmanM3Beta4 area](</id/maturity/taxonomy#docker-and-podman-hosting>)

CakupanEksperimental7%

KualitasBeta71%

KelengkapanBeta79%

Tidak ada

[Windows melalui WSL2M3Beta6 area](</id/maturity/taxonomy#windows-via-wsl2>)

CakupanEksperimental6%

KualitasAlfa69%

KelengkapanBeta79%

Parsial - 5

[Raspberry Pi dan perangkat Linux kecilM3Beta4 area](</id/maturity/taxonomy#raspberry-pi-and-small-linux-devices>)

CakupanEksperimental0%

KualitasAlfa67%

KelengkapanBeta79%

Tidak ada

[aplikasi pendamping macOSM3Beta8 area](</id/maturity/taxonomy#macos-companion-app>)

CakupanEksperimental0%

KualitasAlfa66%

KelengkapanBeta78%

Tidak ada

[aplikasi AndroidM2Alfa7 area](</id/maturity/taxonomy#android-app>)

CakupanEksperimental0%

KualitasAlfa59%

KelengkapanAlfa66%

Tidak ada

[Windows natifM2Alfa4 area](</id/maturity/taxonomy#native-windows>)

CakupanEksperimental0%

KualitasAlfa58%

KelengkapanAlfa66%

Parsial - 1

[hosting KubernetesM2Alfa4 area](</id/maturity/taxonomy#kubernetes-hosting>)

CakupanEksperimental0%

KualitasAlfa55%

KelengkapanAlfa61%

Tidak ada

[aplikasi iOSM1Eksperimental8 area](</id/maturity/taxonomy#ios-app>)

CakupanEksperimental0%

KualitasEksperimental41%

KelengkapanEksperimental44%

Tidak ada

[Jalur instalasi NixM1Eksperimental5 area](</id/maturity/taxonomy#nix-install-path>)

CakupanEksperimental0%

KualitasEksperimental41%

KelengkapanEksperimental44%

Tidak ada

[Surface pendamping watchOSM1Eksperimental5 area](</id/maturity/taxonomy#watchos-companion-surfaces>)

CakupanEksperimental0%

KualitasEksperimental41%

KelengkapanEksperimental44%

Tidak ada

[Aplikasi pendamping LinuxM0Direncanakan5 area](</id/maturity/taxonomy#linux-companion-app>)

CakupanEksperimental0%

KualitasEksperimental19%

KelengkapanEksperimental21%

Tidak ada

[Aplikasi pendamping Windows nativeM0Direncanakan5 area](</id/maturity/taxonomy#native-windows-companion-app>)

CakupanEksperimental0%

KualitasEksperimental19%

KelengkapanEksperimental21%

Tidak ada

### Kanal

[DiscordM4Stabil6 area](</id/maturity/taxonomy#discord>)

CakupanEksperimental0%

KualitasBeta73%

KelengkapanStabil87%

Parsial - 4

[TelegramM3Beta5 area](</id/maturity/taxonomy#telegram>)

CakupanEksperimental0%

KualitasAlfa68%

KelengkapanBeta78%

Penuh - 5

[SlackM3Beta5 area](</id/maturity/taxonomy#slack>)

CakupanEksperimental0%

KualitasAlfa66%

KelengkapanBeta78%

Penuh - 5

[iMessage dan BlueBubblesM3Beta5 area](</id/maturity/taxonomy#imessage-and-bluebubbles>)

CakupanEksperimental0%

KualitasAlfa66%

KelengkapanBeta78%

Tidak ada

[WhatsAppM3Beta5 area](</id/maturity/taxonomy#whatsapp>)

CakupanEksperimental0%

KualitasAlfa66%

KelengkapanBeta78%

Tidak ada

[MatrixM2Alfa6 area](</id/maturity/taxonomy#matrix>)

CakupanEksperimental0%

KualitasAlfa60%

KelengkapanAlfa67%

Tidak ada

[Google ChatM2Alfa5 area](</id/maturity/taxonomy#google-chat>)

CakupanEksperimental0%

KualitasAlfa59%

KelengkapanAlfa66%

Tidak ada

[Microsoft TeamsM2Alfa5 area](</id/maturity/taxonomy#microsoft-teams>)

CakupanEksperimental0%

KualitasAlfa59%

KelengkapanAlfa66%

Tidak ada

[SignalM2Alfa5 area](</id/maturity/taxonomy#signal>)

CakupanEksperimental0%

KualitasAlfa59%

KelengkapanAlfa66%

Tidak ada

[Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, saluran regionalM2Alfa4 area](</id/maturity/taxonomy#feishu-qq-bot-wechat-yuanbao-zalo-zalo-personal-regional-channels>)

CakupanEksperimental0%

KualitasAlfa55%

KelengkapanAlfa58%

Tidak ada

[Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology ChatM2Alfa4 area](</id/maturity/taxonomy#mattermost-line-irc-nextcloud-talk-nostr-twitch-tlon-synology-chat>)

CakupanEksperimental0%

KualitasAlfa53%

KelengkapanAlfa54%

Tidak ada

[Saluran Panggilan SuaraM1Eksperimental5 area](</id/maturity/taxonomy#voice-call-channel>)

CakupanEksperimental0%

KualitasEksperimental41%

KelengkapanEksperimental44%

Tidak ada

### Penyedia dan alat

[Otomasi browser, exec, dan alat sandboxM3Beta3 area](</id/maturity/taxonomy#browser-automation-exec-and-sandbox-tools>)

CakupanEksperimental21%

KualitasBeta75%

KelengkapanBeta79%

Sebagian - 2

[Jalur penyedia OpenAI dan CodexM3Beta5 area](</id/maturity/taxonomy#openai-and-codex-provider-path>)

CakupanEksperimental26%

KualitasBeta74%

KelengkapanBeta79%

Parsial - 3

[Alat pencarian webM3Beta4 area](</id/maturity/taxonomy#web-search-tools>)

CakupanEksperimental9%

KualitasBeta74%

KelengkapanBeta79%

Tidak ada

[Jalur penyedia AnthropicM3Beta5 area](</id/maturity/taxonomy#anthropic-provider-path>)

CakupanEksperimental0%

KualitasBeta71%

KelengkapanBeta78%

Tidak ada

[Jalur penyedia GoogleM3Beta5 area](</id/maturity/taxonomy#google-provider-path>)

CakupanEksperimental0%

KualitasAlfa66%

KelengkapanBeta78%

Tidak ada

[Jalur penyedia OpenRouterM3Beta4 area](</id/maturity/taxonomy#openrouter-provider-path>)

CakupanEksperimental0%

KualitasAlfa66%

KelengkapanBeta78%

Tidak ada

[Alat pembuatan gambar, video, dan musikM2Alfa5 area](</id/maturity/taxonomy#image-video-and-music-generation-tools>)

CakupanEksperimental0%

KualitasAlfa61%

KelengkapanAlfa68%

Tidak ada

[Penyedia model lokal: Ollama, vLLM, SGLang, LM StudioM2Alfa5 area](</id/maturity/taxonomy#local-model-providers-ollama-vllm-sglang-lm-studio>)

CakupanEksperimental0%

KualitasAlfa61%

KelengkapanAlfa68%

Tidak ada

[Penyedia hosted long-tailM2Alfa3 area](</id/maturity/taxonomy#long-tail-hosted-providers>)

CakupanEksperimental0%

KualitasAlfa61%

KelengkapanAlfa68%

Tidak ada

## Ringkasan bukti QA

Pemeriksaan di bawah ini menunjukkan area kartu skor mana yang dijalankan oleh bukti profil QA.

Validasi taksonomi penuh 2026-06-23T07:24:36.128Z 96 pemeriksaan - 94 lulus, 2 diblokir 0 dari 281 (0%) area - 20 dari 1675 (1.2%) fitur - 77 dari 1665 (4.6%) ID cakupan

### Kesiapan berdasarkan area

Buka sebuah permukaan untuk memeriksa status bukti setiap kategori. Daftar tetap diciutkan agar halaman tetap berguna secara sekilas.

Runtime Agen - 9 area

8 ditinjau sebagian / 1 perlu ditinjau

Eksekusi Giliran Agen Ditinjau sebagian - Validasi taksonomi penuh

0 dari 3 (0%) / 7 dari 24 (29.2%) 17 celah kemampuan

Runtime Eksternal dan Subagen Ditinjau sebagian - Validasi taksonomi penuh

0 dari 4 (0%) / 3 dari 10 (30%) 7 celah kemampuan

Eksekusi Penyedia Terhosting Ditinjau sebagian - Validasi taksonomi penuh

1 dari 5 (20%) / 1 dari 5 (20%) 4 celah kemampuan

Penyedia Lokal dan Dihosting Sendiri Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 celah kemampuan

Pemilihan Model dan Runtime Ditinjau sebagian - Validasi taksonomi penuh

0 dari 4 (0%) / 2 dari 8 (25%) 6 celah kemampuan

Autentikasi Penyedia Ditinjau sebagian - Validasi taksonomi penuh

0 dari 10 (0%) / 4 dari 17 (23.5%) 13 celah kemampuan

Streaming dan Kemajuan Ditinjau sebagian - Validasi taksonomi penuh

0 dari 2 (0%) / 5 dari 9 (55.6%) 4 celah kemampuan

Panggilan Alat dan Penanganan Respons Ditinjau sebagian - Validasi taksonomi penuh

0 dari 3 (0%) / 15 dari 23 (65.2%) 8 celah kemampuan

Kontrol Eksekusi Alat Ditinjau sebagian - Validasi taksonomi penuh

0 dari 6 (0%) / 6 dari 12 (50%) 6 celah kemampuan

Aplikasi Android - 7 area

7 perlu ditinjau

Penyiapan Koneksi Perlu ditinjau - Validasi taksonomi penuh

0 dari 1 (0%) / 0 dari 1 (0%) 1 celah kemampuan

Runtime Perangkat Perlu ditinjau - Validasi taksonomi penuh

0 dari 2 (0%) / 0 dari 2 (0%) 2 celah kemampuan

Distribusi Perlu ditinjau - Validasi taksonomi penuh

0 dari 3 (0%) / 0 dari 3 (0%) 3 celah kemampuan

Pengambilan Media Perlu ditinjau - Validasi taksonomi penuh

0 dari 1 (0%) / 0 dari 1 (0%) 1 celah kemampuan

Obrolan Seluler Perlu ditinjau - Validasi taksonomi penuh

0 dari 1 (0%) / 0 dari 1 (0%) 1 celah kemampuan

Pengaturan Perlu ditinjau - Validasi taksonomi penuh

0 dari 1 (0%) / 0 dari 1 (0%) 1 celah kemampuan

Suara Perlu ditinjau - Validasi taksonomi penuh

0 dari 1 (0%) / 0 dari 1 (0%) 1 celah kemampuan

Jalur penyedia Anthropic - 5 area

5 perlu ditinjau

Input Media Perlu ditinjau - Validasi taksonomi penuh

0 dari 4 (0%) / 0 dari 4 (0%) 4 celah kemampuan

Pemilihan Model dan Runtime Perlu ditinjau - Validasi taksonomi penuh

0 dari 10 (0%) / 0 dari 12 (0%) 12 celah kemampuan

Cache Prompt dan Konteks Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 celah kemampuan

Autentikasi dan Pemulihan Penyedia Perlu ditinjau - Validasi taksonomi penuh

0 dari 9 (0%) / 0 dari 9 (0%) 9 celah kemampuan

Transport Permintaan dan Semantik Giliran Perlu ditinjau - Validasi taksonomi penuh

0 dari 10 (0%) / 0 dari 10 (0%) 10 celah kemampuan

Automasi: Cron, hook, tugas, polling - 6 area

5 perlu ditinjau / 1 ditinjau sebagian

Hook Automasi Perlu ditinjau - Validasi taksonomi penuh

0 dari 11 (0%) / 0 dari 11 (0%) 11 kesenjangan kapabilitas

Tugas dan Alur Latar Belakang Perlu ditinjau - Validasi taksonomi penuh

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kapabilitas

Cron Job Perlu ditinjau - Validasi taksonomi penuh

0 dari 15 (0%) / 0 dari 15 (0%) 15 kesenjangan kapabilitas

Ingress Peristiwa Perlu ditinjau - Validasi taksonomi penuh

0 dari 15 (0%) / 0 dari 15 (0%) 15 kesenjangan kapabilitas

Heartbeat Ditinjau sebagian - Validasi taksonomi penuh

0 dari 5 (0%) / 1 dari 7 (14.3%) 6 kesenjangan kapabilitas

Kontrol Polling Perlu ditinjau - Validasi taksonomi penuh

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kapabilitas

Automasi browser, exec, dan alat sandbox - 3 area

2 ditinjau sebagian / 1 perlu ditinjau

Automasi Browser Ditinjau sebagian - Validasi taksonomi penuh

1 dari 8 (12.5%) / 1 dari 8 (12.5%) 7 kesenjangan kapabilitas

Kebijakan Sandbox dan Alat Perlu ditinjau - Validasi taksonomi penuh

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Pemanggilan dan Eksekusi Alat Ditinjau sebagian - Validasi taksonomi penuh

2 dari 6 (33.3%) / 4 dari 8 (50%) 4 kesenjangan kapabilitas

Aplikasi Web Gateway - 6 area

3 perlu ditinjau / 3 ditinjau sebagian

Akses dan Kepercayaan Browser Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Percakapan Realtime Browser Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

UI Browser Ditinjau sebagian - Validasi taksonomi penuh

0 dari 10 (0%) / 1 dari 12 (8.3%) 11 kesenjangan kapabilitas

Konfigurasi Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Konsol Operator Ditinjau sebagian - Validasi taksonomi penuh

0 dari 10 (0%) / 1 dari 12 (8.3%) 11 kesenjangan kapabilitas

Percakapan WebChat Ditinjau sebagian - Validasi taksonomi penuh

0 dari 15 (0%) / 2 dari 20 (10%) 18 kesenjangan kapabilitas

Kerangka kerja channel - 8 area

4 perlu ditinjau / 4 ditinjau sebagian

Perintah Tindakan dan Persetujuan Channel Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Penyiapan Channel Ditinjau sebagian - Validasi taksonomi penuh

0 dari 5 (0%) / 1 dari 7 (14.3%) 6 kesenjangan kapabilitas

Perutean dan Pengiriman Percakapan Ditinjau sebagian - Validasi taksonomi penuh

0 dari 10 (0%) / 5 dari 27 (18.5%) 22 kesenjangan kapabilitas

Perilaku Thread Grup dan Ruang Ambien Ditinjau sebagian - Validasi taksonomi penuh

0 dari 5 (0%) / 4 dari 11 (36.4%) 7 kesenjangan kapabilitas

Akses Masuk dan Gerbang Identitas Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Lampiran Media dan Data Channel Kaya Perlu ditinjau - Validasi taksonomi penuh

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kapabilitas

Pengiriman Keluar dan Alur Balasan Ditinjau sebagian - Validasi taksonomi penuh

0 dari 4 (0%) / 8 dari 21 (38.1%) 13 kesenjangan kapabilitas

Kesehatan Status dan Kontrol Operator Perlu ditinjau - Validasi taksonomi penuh

0 dari 4 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

ClawHub - 4 area

4 perlu ditinjau

Penemuan Katalog Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Kompatibilitas dan Kepercayaan Perlu ditinjau - Validasi taksonomi penuh

0 dari 12 (0%) / 0 dari 12 (0%) 12 kesenjangan kapabilitas

Siklus Hidup dan Kesehatan Plugin Perlu ditinjau - Validasi taksonomi penuh

0 dari 26 (0%) / 0 dari 26 (0%) 26 kesenjangan kapabilitas

Penerbitan Perlu ditinjau - Validasi taksonomi penuh

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kapabilitas

CLI - 7 area

5 perlu ditinjau / 2 ditinjau sebagian

Observabilitas CLI Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Penyiapan CLI Ditinjau sebagian - Validasi taksonomi penuh

1 dari 6 (16.7%) / 1 dari 6 (16.7%) 5 kesenjangan kapabilitas

Doctor Perlu ditinjau - Validasi taksonomi penuh

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kapabilitas

Manajemen Layanan Gateway Ditinjau sebagian - Validasi taksonomi penuh

0 dari 5 (0%) / 1 dari 7 (14.3%) 6 kesenjangan kapabilitas

Onboarding dan Penyiapan Autentikasi Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Penyiapan Plugin dan Kanal Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Pembaruan dan Peningkatan Versi Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Discord - 6 area

6 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi penuh

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Penyiapan dan Operasi Kanal Perlu ditinjau - Validasi taksonomi penuh

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kapabilitas

Perutean dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi penuh

0 dari 12 (0%) / 0 dari 12 (0%) 12 kesenjangan kapabilitas

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi penuh

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Kontrol dan Persetujuan Native Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Suara dan Panggilan Realtime Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Hosting Docker dan Podman - 4 area

3 perlu ditinjau / 1 ditinjau sebagian

Sandbox dan Tooling Agen Perlu ditinjau - Validasi taksonomi penuh

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kapabilitas

Operasi Kontainer Perlu ditinjau - Validasi taksonomi penuh

0 dari 11 (0%) / 0 dari 11 (0%) 11 kesenjangan kapabilitas

Penyiapan Kontainer Perlu ditinjau - Validasi taksonomi penuh

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Rilis dan Validasi Image Ditinjau sebagian - Validasi taksonomi penuh

1 dari 5 (20%) / 2 dari 7 (28.6%) 5 kesenjangan kapabilitas

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, kanal regional - 4 area

4 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Penyiapan dan Operasi Kanal Perlu ditinjau - Validasi taksonomi lengkap

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Perutean dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Runtime Gateway - 13 area

9 perlu ditinjau / 4 ditinjau sebagian

Persetujuan dan Eksekusi Jarak Jauh Perlu ditinjau - Validasi taksonomi lengkap

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Autentikasi dan Penyandingan Perangkat Perlu ditinjau - Validasi taksonomi lengkap

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kapabilitas

Siklus Hidup Gateway Ditinjau sebagian - Validasi taksonomi lengkap

0 dari 7 (0%) / 4 dari 12 (33.3%) 8 kesenjangan kapabilitas

API dan Peristiwa RPC Gateway Ditinjau sebagian - Validasi taksonomi lengkap

0 dari 20 (0%) / 2 dari 22 (9.1%) 20 kesenjangan kapabilitas

Kesehatan, Diagnostik, dan Perbaikan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kapabilitas

Permukaan Web yang Dihosting Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kapabilitas

API HTTP Ditinjau sebagian - Validasi taksonomi lengkap

1 dari 4 (25%) / 1 dari 4 (25%) 3 kesenjangan kapabilitas

Akses dan Penemuan Jaringan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Node dan Kapabilitas Jarak Jauh Perlu ditinjau - Validasi taksonomi lengkap

0 dari 8 (0%) / 0 dari 8 (0%) 8 kesenjangan kapabilitas

Kompatibilitas Protokol Perlu ditinjau - Validasi taksonomi lengkap

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kapabilitas

Peran dan Izin Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Kontrol Keamanan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Koneksi WebSocket Ditinjau sebagian - Validasi taksonomi lengkap

1 dari 8 (12.5%) / 1 dari 8 (12.5%) 7 kesenjangan kapabilitas

Google Chat - 5 area

5 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 11 (0%) / 0 dari 11 (0%) 11 kesenjangan kapabilitas

Penyiapan dan Operasi Kanal Perlu ditinjau - Validasi taksonomi lengkap

0 dari 16 (0%) / 0 dari 16 (0%) 16 kesenjangan kapabilitas

Perutean dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Kontrol dan Persetujuan Native Perlu ditinjau - Validasi taksonomi lengkap

0 dari 16 (0%) / 0 dari 16 (0%) 16 kesenjangan kapabilitas

Jalur penyedia Google - 5 area

5 perlu ditinjau

Runtime Gemini Langsung Perlu ditinjau - Validasi taksonomi lengkap

0 dari 9 (0%) / 0 dari 9 (0%) 9 kesenjangan kemampuan

Media, Pencarian, dan Realtime Perlu ditinjau - Validasi taksonomi lengkap

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kemampuan

Perutean Model dan Endpoint Perlu ditinjau - Validasi taksonomi lengkap

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kemampuan

Penyimpanan Cache Prompt Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kemampuan

Penyiapan Penyedia dan Kredensial Perlu ditinjau - Validasi taksonomi lengkap

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kemampuan

Alat pembuatan gambar, video, dan musik - 5 area

5 perlu ditinjau

Pembuatan Gambar Perlu ditinjau - Validasi taksonomi lengkap

0 dari 9 (0%) / 0 dari 9 (0%) 9 kesenjangan kemampuan

Perutean dan Penemuan Media Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kemampuan

Pembuatan Musik Perlu ditinjau - Validasi taksonomi lengkap

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kemampuan

Siklus Hidup Tugas dan Pengiriman Perlu ditinjau - Validasi taksonomi lengkap

0 dari 12 (0%) / 0 dari 12 (0%) 12 kesenjangan kemampuan

Pembuatan Video Perlu ditinjau - Validasi taksonomi lengkap

0 dari 11 (0%) / 0 dari 11 (0%) 11 kesenjangan kemampuan

iMessage dan BlueBubbles - 5 area

5 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kemampuan

Penyiapan dan Operasi Channel Perlu ditinjau - Validasi taksonomi lengkap

0 dari 11 (0%) / 0 dari 11 (0%) 11 kesenjangan kemampuan

Perutean dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kemampuan

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi lengkap

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kemampuan

Kontrol Native dan Persetujuan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kemampuan

Aplikasi iOS - 8 area

8 perlu ditinjau

Kanvas dan Layar Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kemampuan

Chat dan Sesi Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kemampuan

Perintah Perangkat Perlu ditinjau - Validasi taksonomi lengkap

0 dari 2 (0%) / 0 dari 2 (0%) 2 kesenjangan kemampuan

Distribusi Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kemampuan

Penyiapan dan Diagnostik Gateway Perlu ditinjau - Validasi taksonomi lengkap

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kemampuan

Media dan Berbagi Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kemampuan

Notifikasi dan Latar Belakang Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kemampuan

Suara Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kemampuan

Hosting Kubernetes - 4 area

4 perlu ditinjau

Akses dan Eksposur Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Siklus Hidup Klaster Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Konfigurasi dan Rahasia Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Penyiapan Deployment Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Aplikasi pendamping Linux - 5 area

5 perlu ditinjau

Distribusi Aplikasi Perlu ditinjau - Validasi taksonomi lengkap

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kapabilitas

Chat dan Sesi Perlu ditinjau - Validasi taksonomi lengkap

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kapabilitas

Kapabilitas Desktop Perlu ditinjau - Validasi taksonomi lengkap

0 dari 9 (0%) / 0 dari 9 (0%) 9 kesenjangan kapabilitas

Konektivitas Gateway Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kapabilitas

Status dan Diagnostik Perlu ditinjau - Validasi taksonomi lengkap

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kapabilitas

Host Gateway Linux - 5 area

5 perlu ditinjau

Target Deployment Perlu ditinjau - Validasi taksonomi lengkap

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kapabilitas

Diagnostik dan Perbaikan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kapabilitas

Runtime Gateway dan Kontrol Layanan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Penyiapan dan Pembaruan Host Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kapabilitas

Akses Jarak Jauh dan Keamanan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Penyedia model lokal: Ollama, vLLM, SGLang, LM Studio - 5 area

5 perlu ditinjau

Memori Lokal dan Embedding Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Plugin Penyedia Native Perlu ditinjau - Validasi taksonomi lengkap

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kapabilitas

Keamanan Jaringan dan Kontrol Prompt Perlu ditinjau - Validasi taksonomi lengkap

0 dari 2 (0%) / 0 dari 2 (0%) 2 kesenjangan kapabilitas

Kompatibilitas Runtime yang Kompatibel dengan OpenAI Perlu ditinjau - Validasi taksonomi lengkap

0 dari 8 (0%) / 0 dari 8 (0%) 8 kesenjangan kapabilitas

Penyiapan, Siklus Hidup, dan Diagnostik Penyedia Perlu ditinjau - Validasi taksonomi lengkap

0 dari 12 (0%) / 0 dari 12 (0%) 12 kesenjangan kapabilitas

Penyedia hosted long-tail - 3 area

3 perlu ditinjau

Penyedia LLM Hosted Perlu ditinjau - Validasi taksonomi lengkap

0 dari 12 (0%) / 0 dari 12 (0%) 12 kesenjangan kapabilitas

Penyedia Media Hosted Perlu ditinjau - Validasi taksonomi lengkap

0 dari 8 (0%) / 0 dari 8 (0%) 8 kesenjangan kapabilitas

Operasi Penyedia Perlu ditinjau - Validasi taksonomi lengkap

0 dari 12 (0%) / 0 dari 12 (0%) 12 kesenjangan kapabilitas

aplikasi pendamping macOS - 8 area

8 perlu ditinjau

Kanvas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kemampuan

Penyiapan Lokal Perlu ditinjau - Validasi taksonomi lengkap

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kemampuan

Kemampuan Bawaan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kemampuan

Koneksi Jarak Jauh Perlu ditinjau - Validasi taksonomi lengkap

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kemampuan

WebChat Jarak Jauh Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kemampuan

Status dan Pengaturan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kemampuan

Suara dan Bicara Perlu ditinjau - Validasi taksonomi lengkap

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kemampuan

WebChat Perlu ditinjau - Validasi taksonomi lengkap

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kemampuan

host Gateway macOS - 7 area

7 perlu ditinjau

Penyiapan CLI Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kemampuan

Diagnostik dan Observabilitas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kemampuan

Siklus Hidup Layanan Gateway Perlu ditinjau - Validasi taksonomi lengkap

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kemampuan

Integrasi Gateway Lokal Perlu ditinjau - Validasi taksonomi lengkap

0 dari 9 (0%) / 0 dari 9 (0%) 9 kesenjangan kemampuan

Izin dan Kemampuan Bawaan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kemampuan

Profil dan Isolasi Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kemampuan

Mode Gateway Jarak Jauh Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kemampuan

Matrix - 6 area

6 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kemampuan

Penyiapan dan Operasi Saluran Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kemampuan

Perutean dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kemampuan

Enkripsi dan Verifikasi Perlu ditinjau - Validasi taksonomi lengkap

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kemampuan

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kemampuan

Kontrol Bawaan dan Persetujuan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kemampuan

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - 4 area

4 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Penyiapan dan Operasi Channel Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Perutean dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Pemahaman media dan pembuatan media - 6 area

4 perlu ditinjau / 2 ditinjau sebagian

Penanganan Media Channel Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Konfigurasi Media Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Pembuatan Media Ditinjau sebagian - Validasi taksonomi lengkap

1 dari 17 (5.9%) / 1 dari 19 (5.3%) 18 kesenjangan kapabilitas

Penerimaan dan Akses Media Perlu ditinjau - Validasi taksonomi lengkap

0 dari 8 (0%) / 0 dari 8 (0%) 8 kesenjangan kapabilitas

Pemahaman Media Ditinjau sebagian - Validasi taksonomi lengkap

0 dari 12 (0%) / 1 dari 14 (7.1%) 13 kesenjangan kapabilitas

Pengiriman Teks-ke-Ucapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 2 (0%) / 0 dari 2 (0%) 2 kesenjangan kapabilitas

Microsoft Teams - 5 area

5 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 9 (0%) / 0 dari 9 (0%) 9 kesenjangan kapabilitas

Penyiapan dan Operasi Channel Perlu ditinjau - Validasi taksonomi lengkap

0 dari 9 (0%) / 0 dari 9 (0%) 9 kesenjangan kapabilitas

Perutean dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Kontrol Native dan Persetujuan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Windows Native - 4 area

4 perlu ditinjau

CLI Perlu ditinjau - Validasi taksonomi lengkap

0 dari 9 (0%) / 0 dari 9 (0%) 9 kesenjangan kapabilitas

Manajemen Gateway Perlu ditinjau - Validasi taksonomi lengkap

0 dari 11 (0%) / 0 dari 11 (0%) 11 kesenjangan kapabilitas

Jaringan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kapabilitas

Pembaruan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kapabilitas

Aplikasi pendamping Windows native - 5 area

5 perlu ditinjau

Sesi Obrolan Perlu ditinjau - Validasi taksonomi penuh

0 dari 2 (0%) / 0 dari 2 (0%) 2 kesenjangan kemampuan

Alat Desktop dan Izin Perlu ditinjau - Validasi taksonomi penuh

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kemampuan

Koneksi Gateway Perlu ditinjau - Validasi taksonomi penuh

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kemampuan

Instalasi dan Pembaruan Perlu ditinjau - Validasi taksonomi penuh

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kemampuan

Status dan Perbaikan Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kemampuan

Jalur instalasi Nix - 5 area

5 perlu ditinjau

Aktivasi dan UX Aplikasi Perlu ditinjau - Validasi taksonomi penuh

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kemampuan

Konfigurasi dan Status Perlu ditinjau - Validasi taksonomi penuh

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kemampuan

Serah Terima Instalasi Perlu ditinjau - Validasi taksonomi penuh

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kemampuan

Siklus Hidup Plugin Perlu ditinjau - Validasi taksonomi penuh

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kemampuan

Runtime Layanan dan Pelindung Perlu ditinjau - Validasi taksonomi penuh

0 dari 8 (0%) / 0 dari 8 (0%) 8 kesenjangan kemampuan

Jalur penyedia OpenAI dan Codex - 5 area

2 perlu ditinjau / 3 ditinjau sebagian

Input Gambar dan Multimodal Perlu ditinjau - Validasi taksonomi penuh

0 dari 2 (0%) / 0 dari 2 (0%) 2 kesenjangan kemampuan

Model dan Autentikasi Ditinjau sebagian - Validasi taksonomi penuh

1 dari 6 (16.7%) / 4 dari 9 (44.4%) 5 kesenjangan kemampuan

Harness Codex Native Ditinjau sebagian - Validasi taksonomi penuh

0 dari 2 (0%) / 4 dari 9 (44.4%) 5 kesenjangan kemampuan

Kompatibilitas Respons dan Alat Ditinjau sebagian - Validasi taksonomi penuh

1 dari 4 (25%) / 2 dari 5 (40%) 3 kesenjangan kemampuan

Suara dan Audio Realtime Perlu ditinjau - Validasi taksonomi penuh

0 dari 2 (0%) / 0 dari 2 (0%) 2 kesenjangan kemampuan

SDK Aplikasi OpenClaw - 6 area

5 perlu ditinjau / 1 ditinjau sebagian

Percakapan Agen Perlu ditinjau - Validasi taksonomi penuh

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kemampuan

API Klien Perlu ditinjau - Validasi taksonomi penuh

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kemampuan

Kompatibilitas Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kemampuan

Peristiwa dan Persetujuan Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kemampuan

Akses Gateway Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kemampuan

Pembantu Sumber Daya Ditinjau sebagian - Validasi taksonomi penuh

0 dari 5 (0%) / 1 dari 6 (16.7%) 5 kesenjangan kemampuan

Jalur provider OpenRouter - 4 area

4 perlu ditinjau

Runtime Chat dan Normalisasi Perlu ditinjau - Validasi taksonomi penuh

0 dari 15 (0%) / 0 dari 15 (0%) 15 kesenjangan kapabilitas

Pembuatan Media dan Ucapan Perlu ditinjau - Validasi taksonomi penuh

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kapabilitas

Pemulihan dan Diagnostik Provider Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Penyiapan dan Auth Provider Perlu ditinjau - Validasi taksonomi penuh

0 dari 14 (0%) / 0 dari 14 (0%) 14 kesenjangan kapabilitas

Plugins - 9 area

6 perlu ditinjau / 3 ditinjau sebagian

Penulisan dan Pengemasan plugins Perlu ditinjau - Validasi taksonomi penuh

0 dari 8 (0%) / 0 dari 8 (0%) 8 kesenjangan kapabilitas

Plugins bawaan Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Plugin Canvas Perlu ditinjau - Validasi taksonomi penuh

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Plugins channel Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Menginstal dan menjalankan plugins Ditinjau sebagian - Validasi taksonomi penuh

0 dari 6 (0%) / 7 dari 20 (35%) 13 kesenjangan kapabilitas

Persetujuan Plugin Perlu ditinjau - Validasi taksonomi penuh

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Plugins provider dan alat Ditinjau sebagian - Validasi taksonomi penuh

1 dari 6 (16.7%) / 9 dari 21 (42.9%) 12 kesenjangan kapabilitas

Mempublikasikan plugins Perlu ditinjau - Validasi taksonomi penuh

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Menguji plugins Ditinjau sebagian - Validasi taksonomi penuh

0 dari 6 (0%) / 3 dari 11 (27.3%) 8 kesenjangan kapabilitas

Raspberry Pi dan perangkat Linux kecil - 4 area

4 perlu ditinjau

Runtime Gateway Perlu ditinjau - Validasi taksonomi penuh

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kapabilitas

Performa dan Diagnostik Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Akses Jarak Jauh dan Auth Perlu ditinjau - Validasi taksonomi penuh

0 dari 9 (0%) / 0 dari 9 (0%) 9 kesenjangan kapabilitas

Penyiapan dan Kompatibilitas Perlu ditinjau - Validasi taksonomi penuh

0 dari 12 (0%) / 0 dari 12 (0%) 12 kesenjangan kapabilitas

Keamanan, auth, pemasangan, dan rahasia - 6 area

2 ditinjau sebagian / 4 perlu ditinjau

Kebijakan Persetujuan dan Perlindungan Alat Ditinjau sebagian - Validasi taksonomi penuh

0 dari 2 (0%) / 3 dari 6 (50%) 3 kesenjangan kapabilitas

Kontrol Akses Channel Perlu ditinjau - Validasi taksonomi penuh

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kapabilitas

Higiene Kredensial dan Rahasia Ditinjau sebagian - Validasi taksonomi penuh

0 dari 5 (0%) / 5 dari 11 (45.5%) 6 kesenjangan kapabilitas

Pemasangan Perangkat dan Node Perlu ditinjau - Validasi taksonomi penuh

0 dari 11 (0%) / 0 dari 11 (0%) 11 kesenjangan kapabilitas

Auth Gateway dan Akses Jarak Jauh Perlu ditinjau - Validasi taksonomi penuh

0 dari 9 (0%) / 0 dari 9 (0%) 9 kesenjangan kapabilitas

Kepercayaan Plugin Perlu ditinjau - Validasi taksonomi penuh

0 dari 2 (0%) / 0 dari 2 (0%) 2 kesenjangan kapabilitas

Sesi, memori, dan mesin konteks - 9 area

2 perlu ditinjau / 7 ditinjau sebagian

Manajemen Sesi dan Transkrip CLI Perlu ditinjau - Validasi taksonomi lengkap

0 dari 2 (0%) / 0 dari 2 (0%) 2 kesenjangan kapabilitas

Mesin Konteks Ditinjau sebagian - Validasi taksonomi lengkap

0 dari 2 (0%) / 4 dari 7 (57.1%) 3 kesenjangan kapabilitas

Prompt Inti dan Konteks Ditinjau sebagian - Validasi taksonomi lengkap

0 dari 2 (0%) / 3 dari 8 (37.5%) 5 kesenjangan kapabilitas

Riwayat Lintas Klien dan Kesetaraan Sesi Ditinjau sebagian - Validasi taksonomi lengkap

0 dari 2 (0%) / 2 dari 5 (40%) 3 kesenjangan kapabilitas

Diagnostik, Pemeliharaan, dan Pemulihan Ditinjau sebagian - Validasi taksonomi lengkap

0 dari 3 (0%) / 4 dari 10 (40%) 6 kesenjangan kapabilitas

Memori Ditinjau sebagian - Validasi taksonomi lengkap

0 dari 5 (0%) / 6 dari 13 (46.2%) 7 kesenjangan kapabilitas

Perutean Sesi Ditinjau sebagian - Validasi taksonomi lengkap

0 dari 2 (0%) / 1 dari 4 (25%) 3 kesenjangan kapabilitas

Manajemen Token Ditinjau sebagian - Validasi taksonomi lengkap

0 dari 3 (0%) / 2 dari 10 (20%) 8 kesenjangan kapabilitas

Persistensi Transkrip Perlu ditinjau - Validasi taksonomi lengkap

0 dari 2 (0%) / 0 dari 2 (0%) 2 kesenjangan kapabilitas

Signal - 5 area

5 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Penyiapan dan Operasi Kanal Perlu ditinjau - Validasi taksonomi lengkap

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kapabilitas

Perutean dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi lengkap

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kapabilitas

Kontrol dan Persetujuan Native Perlu ditinjau - Validasi taksonomi lengkap

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kapabilitas

Slack - 5 area

5 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Penyiapan dan Operasi Kanal Perlu ditinjau - Validasi taksonomi lengkap

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kapabilitas

Perutean dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Kontrol dan Persetujuan Native Perlu ditinjau - Validasi taksonomi lengkap

0 dari 8 (0%) / 0 dari 8 (0%) 8 kesenjangan kapabilitas

Telegram - 5 area

5 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kapabilitas

Penyiapan dan Operasi Kanal Perlu ditinjau - Validasi taksonomi lengkap

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kapabilitas

Perutean dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 kesenjangan kapabilitas

Kontrol dan Persetujuan Native Perlu ditinjau - Validasi taksonomi lengkap

0 dari 9 (0%) / 0 dari 9 (0%) 9 kesenjangan kapabilitas

Observabilitas - 5 area

3 ditinjau sebagian / 2 perlu ditinjau

Pengumpulan Diagnostik Ditinjau sebagian - Validasi taksonomi lengkap

1 dari 8 (12.5%) / 3 dari 10 (30%) 7 celah kapabilitas

Kesehatan dan Perbaikan Ditinjau sebagian - Validasi taksonomi lengkap

1 dari 12 (8.3%) / 5 dari 18 (27.8%) 13 celah kapabilitas

Pencatatan log Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 celah kapabilitas

Diagnostik Sesi Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 celah kapabilitas

Ekspor Telemetri Ditinjau sebagian - Validasi taksonomi lengkap

1 dari 13 (7.7%) / 7 dari 21 (33.3%) 14 celah kapabilitas

TUI - 5 area

5 perlu ditinjau

Input dan Perintah Perlu ditinjau - Validasi taksonomi lengkap

0 dari 8 (0%) / 0 dari 8 (0%) 8 celah kapabilitas

Eksekusi Shell Lokal Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 celah kapabilitas

Keamanan Rendering dan Output Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 celah kapabilitas

Mode Runtime Perlu ditinjau - Validasi taksonomi lengkap

0 dari 14 (0%) / 0 dari 14 (0%) 14 celah kapabilitas

Manajemen Sesi Perlu ditinjau - Validasi taksonomi lengkap

0 dari 3 (0%) / 0 dari 3 (0%) 3 celah kapabilitas

Suara dan percakapan waktu nyata - 6 area

6 perlu ditinjau

Percakapan Aplikasi Native Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 celah kapabilitas

Sesi Percakapan Waktu Nyata Perlu ditinjau - Validasi taksonomi lengkap

0 dari 11 (0%) / 0 dari 11 (0%) 11 celah kapabilitas

Ucapan dan Transkripsi Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 celah kapabilitas

Observabilitas Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 5 (0%) / 0 dari 5 (0%) 5 celah kapabilitas

Penyedia Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 7 (0%) / 0 dari 7 (0%) 7 celah kapabilitas

Bangun Suara dan Routing Perlu ditinjau - Validasi taksonomi lengkap

0 dari 4 (0%) / 0 dari 4 (0%) 4 celah kapabilitas

Saluran Panggilan Suara - 5 area

5 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 celah kapabilitas

Penyiapan dan Operasi Saluran Perlu ditinjau - Validasi taksonomi lengkap

0 dari 2 (0%) / 0 dari 2 (0%) 2 celah kapabilitas

Routing dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi lengkap

0 dari 1 (0%) / 0 dari 1 (0%) 1 celah kapabilitas

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi lengkap

0 dari 2 (0%) / 0 dari 2 (0%) 2 celah kapabilitas

Suara dan Panggilan Waktu Nyata Perlu ditinjau - Validasi taksonomi lengkap

0 dari 2 (0%) / 0 dari 2 (0%) 2 celah kapabilitas

permukaan pendamping watchOS - 5 area

5 perlu ditinjau

Pengiriman dan Pemulihan Perlu ditinjau - Validasi taksonomi penuh

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kapabilitas

Distribusi dan Dukungan Perlu ditinjau - Validasi taksonomi penuh

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

Persetujuan Eksekusi Perlu ditinjau - Validasi taksonomi penuh

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kapabilitas

Notifikasi dan Balasan Perlu ditinjau - Validasi taksonomi penuh

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kapabilitas

UI Aplikasi Watch Perlu ditinjau - Validasi taksonomi penuh

0 dari 3 (0%) / 0 dari 3 (0%) 3 kesenjangan kapabilitas

Alat pencarian web - 4 area

2 perlu ditinjau / 2 ditinjau sebagian

Keamanan Jaringan Perlu ditinjau - Validasi taksonomi penuh

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kapabilitas

Penyedia Pencarian Ditinjau sebagian - Validasi taksonomi penuh

2 dari 19 (10.5%) / 2 dari 19 (10.5%) 17 kesenjangan kapabilitas

Penyiapan dan Diagnostik Perlu ditinjau - Validasi taksonomi penuh

0 dari 9 (0%) / 0 dari 9 (0%) 9 kesenjangan kapabilitas

Ketersediaan Alat dan Pengambilan Ditinjau sebagian - Validasi taksonomi penuh

2 dari 11 (18.2%) / 3 dari 12 (25%) 9 kesenjangan kapabilitas

WhatsApp - 5 area

5 perlu ditinjau

Akses dan Identitas Perlu ditinjau - Validasi taksonomi penuh

0 dari 7 (0%) / 0 dari 7 (0%) 7 kesenjangan kapabilitas

Penyiapan dan Operasi Kanal Perlu ditinjau - Validasi taksonomi penuh

0 dari 5 (0%) / 0 dari 5 (0%) 5 kesenjangan kapabilitas

Perutean dan Pengiriman Percakapan Perlu ditinjau - Validasi taksonomi penuh

0 dari 4 (0%) / 0 dari 4 (0%) 4 kesenjangan kapabilitas

Media dan Konten Kaya Perlu ditinjau - Validasi taksonomi penuh

0 dari 2 (0%) / 0 dari 2 (0%) 2 kesenjangan kapabilitas

Kontrol Native dan Persetujuan Perlu ditinjau - Validasi taksonomi penuh

0 dari 2 (0%) / 0 dari 2 (0%) 2 kesenjangan kapabilitas

Windows melalui WSL2 - 6 area

5 perlu ditinjau / 1 ditinjau sebagian

Browser dan UI Kontrol Perlu ditinjau - Validasi taksonomi penuh

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

CLI Perlu ditinjau - Validasi taksonomi penuh

0 dari 8 (0%) / 0 dari 8 (0%) 8 kesenjangan kapabilitas

Diagnostik dan Perbaikan Ditinjau sebagian - Validasi taksonomi penuh

1 dari 6 (16.7%) / 3 dari 8 (37.5%) 5 kesenjangan kapabilitas

Akses dan Eksposur Gateway Perlu ditinjau - Validasi taksonomi penuh

0 dari 11 (0%) / 0 dari 11 (0%) 11 kesenjangan kapabilitas

Siklus Hidup Layanan Gateway Perlu ditinjau - Validasi taksonomi penuh

0 dari 10 (0%) / 0 dari 10 (0%) 10 kesenjangan kapabilitas

Penyiapan WSL Perlu ditinjau - Validasi taksonomi penuh

0 dari 6 (0%) / 0 dari 6 (0%) 6 kesenjangan kapabilitas

> Terakhir diperbarui: 2026-06-22

Was this useful?YesNo

Open issue