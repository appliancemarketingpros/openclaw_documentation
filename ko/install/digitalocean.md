---
title: DigitalOcean
source_url: https://docs.openclaw.ai/ko/install/digitalocean
scraped_at: 2026-05-25
---

OpenClaw Gateway를 DigitalOcean Droplet에서 지속 실행합니다(1 GB Basic 플랜 기준 약 $6/월).

DigitalOcean은 가장 간단한 유료 VPS 경로입니다. 더 저렴하거나 무료인 옵션을 선호한다면:

  * [Hetzner](</ko/install/hetzner>) — 월 €3.79, 비용 대비 더 많은 코어/RAM.
  * [Oracle Cloud](</ko/install/oracle>) — Always Free ARM(최대 4 OCPU, 24 GB RAM)이지만, 가입이 까다로울 수 있고 ARM 전용입니다.


## 필수 조건

  * DigitalOcean 계정([가입](<https://cloud.digitalocean.com/registrations/new>))
  * SSH 키 쌍(또는 비밀번호 인증 사용 의향)
  * 약 20분


## 설정

* ### Create a Droplet

  1. [DigitalOcean](<https://cloud.digitalocean.com/>)에 로그인합니다.
  2. **Create > Droplets**를 클릭합니다.
  3. 다음을 선택합니다: 
     * **Region:** 가장 가까운 지역
     * **Image:** Ubuntu 24.04 LTS
     * **Size:** Basic, Regular, 1 vCPU / 1 GB RAM / 25 GB SSD
     * **Authentication:** SSH 키(권장) 또는 비밀번호
  4. **Create Droplet** 을 클릭하고 IP 주소를 기록합니다.


* ### Connect and install

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

시스템 부트스트랩에만 루트 셸을 사용하세요. OpenClaw 명령은 비루트 `openclaw` 사용자로 실행하여 상태가 `/home/openclaw/.openclaw/` 아래에 저장되고 Gateway가 해당 사용자의 systemd 서비스로 설치되도록 합니다.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

마법사가 모델 인증, 채널 설정, Gateway 토큰 생성, 데몬 설치(systemd)를 안내합니다.

* ### Add swap (recommended for 1 GB Droplets)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### Verify the gateway

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Access the Control UI

Gateway는 기본적으로 loopback에 바인딩됩니다. 다음 옵션 중 하나를 선택하세요.

**옵션 A: SSH 터널(가장 간단함)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

그런 다음 `http://localhost:18789`를 엽니다.

**옵션 B: Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

그런 다음 tailnet의 아무 기기에서나 `https://<magicdns>/`를 엽니다.

Tailscale Serve는 tailnet ID 헤더를 통해 제어 UI와 WebSocket 트래픽을 인증하며, 이는 Gateway 호스트 자체를 신뢰한다고 가정합니다. HTTP API 엔드포인트는 이와 관계없이 Gateway의 일반 인증 모드(토큰/비밀번호)를 따릅니다. Serve에서 명시적인 공유 비밀 자격 증명을 요구하려면 `gateway.auth.allowTailscale: false`를 설정하고 `gateway.auth.mode: "token"` 또는 `"password"`를 사용하세요.

**옵션 C: Tailnet 바인딩(Serve 없음)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

그런 다음 `http://<tailscale-ip>:18789`를 엽니다(토큰 필요).

## 지속성과 백업

OpenClaw 상태는 다음 위치에 저장됩니다:

  * `~/.openclaw/` — `openclaw.json`, 에이전트별 `auth-profiles.json`, 채널/프로바이더 상태, 세션 데이터.
  * `~/.openclaw/workspace/` — 에이전트 워크스페이스([SOUL.md](<http://SOUL.md>), 메모리, 아티팩트).


이 데이터는 Droplet 재부팅 후에도 유지됩니다. 이식 가능한 스냅샷을 만들려면:

bashCopy code
[code]
    openclaw backup create
[/code]

DigitalOcean 스냅샷은 전체 Droplet을 백업합니다. `openclaw backup create`는 호스트 간에 이식 가능합니다.

## 1 GB RAM 팁

$6 Droplet에는 RAM이 1 GB뿐입니다. 원활하게 유지하려면:

  * 위의 스왑 단계가 `/etc/fstab`에 들어 있어 재부팅 후에도 유지되는지 확인하세요.
  * 로컬 모델보다 API 기반 모델(Claude, GPT)을 선호하세요. 로컬 LLM 추론은 1 GB에 맞지 않습니다.
  * 큰 프롬프트에서 OOM이 발생하면 `agents.defaults.model.primary`를 더 작은 모델로 설정하세요.
  * `free -h`와 `htop`으로 모니터링하세요.


## 문제 해결

**Gateway가 시작되지 않음** \-- `openclaw doctor --non-interactive`를 실행하고 `journalctl --user -u openclaw-gateway.service -n 50`으로 로그를 확인하세요.

**포트가 이미 사용 중임** \-- `lsof -i :18789`를 실행하여 프로세스를 찾은 다음 중지하세요.

**메모리 부족** \-- `free -h`로 스왑이 활성화되어 있는지 확인하세요. 여전히 OOM이 발생하면 로컬 모델 대신 API 기반 모델(Claude, GPT)을 사용하거나 2 GB Droplet으로 업그레이드하세요.

## 다음 단계

  * [채널](</ko/channels>) \-- Telegram, WhatsApp, Discord 등을 연결
  * [Gateway 구성](</ko/gateway/configuration>) \-- 모든 구성 옵션
  * [업데이트](</ko/install/updating>) \-- OpenClaw를 최신 상태로 유지


## 관련 항목

  * [설치 개요](</ko/install>)
  * [Fly.io](</ko/install/fly>)
  * [Hetzner](</ko/install/hetzner>)
  * [VPS 호스팅](</ko/vps>)


Was this useful?YesNo