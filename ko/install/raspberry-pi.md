---
title: Raspberry Pi
source_url: https://docs.openclaw.ai/ko/install/raspberry-pi
scraped_at: 2026-05-25
---

OpenClaw Gateway를 Raspberry Pi에서 지속적으로 항상 실행합니다. Pi는 Gateway일 뿐이므로(모델은 API를 통해 클라우드에서 실행됨), 보급형 Pi도 이 워크로드를 충분히 잘 처리합니다. 일반적인 하드웨어 비용은 **일회성 $35–80** 이며, 월간 요금은 없습니다.

## 하드웨어 호환성

Pi 모델 | RAM | 작동 여부 | 참고  
---|---|---|---  
Pi 5 | 4/8 GB | 최상 | 가장 빠르며 권장됩니다.  
Pi 4 | 4 GB | 좋음 | 대부분의 사용자에게 적합합니다.  
Pi 4 | 2 GB | 가능 | 스왑을 추가하세요.  
Pi 4 | 1 GB | 빠듯함 | 스왑과 최소 구성으로 가능합니다.  
Pi 3B+ | 1 GB | 느림 | 작동하지만 둔합니다.  
Pi Zero 2 W | 512 MB | 아니요 | 권장하지 않습니다.  
  
**최소:** RAM 1 GB, 코어 1개, 여유 디스크 500 MB, 64비트 OS. **권장:** RAM 2 GB 이상, 16 GB 이상 SD 카드(또는 USB SSD), 이더넷.

## 사전 요구 사항

  * RAM 2 GB 이상인 Raspberry Pi 4 또는 5(4 GB 권장)
  * MicroSD 카드(16 GB 이상) 또는 USB SSD(성능 향상)
  * 공식 Pi 전원 공급 장치
  * 네트워크 연결(이더넷 또는 WiFi)
  * 64비트 Raspberry Pi OS(필수 -- 32비트는 사용하지 마세요)
  * 약 30분


## 설정

* ### OS 플래시

**Raspberry Pi OS Lite (64-bit)**를 사용하세요 -- 헤드리스 서버에는 데스크톱이 필요하지 않습니다.

  1. [Raspberry Pi Imager](<https://www.raspberrypi.com/software/>)를 다운로드합니다.
  2. OS를 선택합니다: **Raspberry Pi OS Lite (64-bit)**.
  3. 설정 대화상자에서 미리 구성합니다: 
     * 호스트 이름: `gateway-host`
     * SSH 활성화
     * 사용자 이름과 비밀번호 설정
     * WiFi 구성(이더넷을 사용하지 않는 경우)
  4. SD 카드 또는 USB 드라이브에 플래시하고, 삽입한 뒤 Pi를 부팅합니다.


* ### SSH로 연결

bashCopy code
[code]
    ssh user@gateway-host
[/code]

* ### 시스템 업데이트

bashCopy code
[code]
    sudo apt update && sudo apt upgrade -ysudo apt install -y git curl build-essential # Set timezone (important for cron and reminders)sudo timedatectl set-timezone America/Chicago
[/code]

* ### Node.js 24 설치

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt install -y nodejsnode --version
[/code]

* ### 스왑 추가(2 GB 이하에서 중요)

bashCopy code
[code]
    sudo fallocate -l 2G /swapfilesudo chmod 600 /swapfilesudo mkswap /swapfilesudo swapon /swapfileecho '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # Reduce swappiness for low-RAM devicesecho 'vm.swappiness=10' | sudo tee -a /etc/sysctl.confsudo sysctl -p
[/code]

* ### OpenClaw 설치

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

* ### 온보딩 실행

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

마법사를 따르세요. 헤드리스 장치에는 OAuth보다 API 키를 권장합니다. Telegram이 시작하기 가장 쉬운 채널입니다.

* ### 확인

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Control UI에 접근

컴퓨터에서 Pi로부터 대시보드 URL을 가져옵니다:

bashCopy code
[code]
    ssh user@gateway-host 'openclaw dashboard --no-open'
[/code]

그런 다음 다른 터미널에서 SSH 터널을 만듭니다:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@gateway-host
[/code]

출력된 URL을 로컬 브라우저에서 엽니다. 항상 켜진 원격 접근은 [Tailscale 통합](</ko/gateway/tailscale>)을 참고하세요.

## 성능 팁

**USB SSD 사용** \-- SD 카드는 느리고 마모됩니다. USB SSD는 성능을 크게 향상합니다. [Pi USB 부팅 가이드](<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot>)를 참고하세요.

**모듈 컴파일 캐시 활성화** \-- 저전력 Pi 호스트에서 반복적인 CLI 호출 속도를 높입니다:

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF' # pragma: allowlist secretexport NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

**메모리 사용량 줄이기** \-- 헤드리스 설정에서는 GPU 메모리를 확보하고 사용하지 않는 서비스를 비활성화하세요:

bashCopy code
[code]
    echo 'gpu_mem=16' | sudo tee -a /boot/config.txtsudo systemctl disable bluetooth
[/code]

**안정적인 재시작을 위한 systemd 드롭인** \-- 이 Pi가 주로 OpenClaw를 실행하는 경우 서비스 드롭인을 추가하세요:

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

그런 다음 `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service`를 실행합니다. 헤드리스 Pi에서는 사용자가 로그아웃해도 사용자 서비스가 유지되도록 lingering도 한 번 활성화하세요: `sudo loginctl enable-linger "$(whoami)"`.

## 권장 모델 설정

Pi는 Gateway만 실행하므로 클라우드 호스팅 API 모델을 사용하세요:

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-sonnet-4-6",        "fallbacks": ["openai/gpt-5.4-mini"]      }    }  }}
[/code]

Pi에서 로컬 LLM을 실행하지 마세요. 작은 모델도 유용하게 쓰기에는 너무 느립니다. 모델 작업은 Claude 또는 GPT에 맡기세요.

## ARM 바이너리 참고 사항

대부분의 OpenClaw 기능은 변경 없이 ARM64에서 작동합니다(Node.js, Telegram, WhatsApp/Baileys, Chromium). ARM 빌드가 가끔 없는 바이너리는 보통 Skills에서 제공하는 선택적 Go/Rust CLI 도구입니다. 소스에서 빌드하기 전에 누락된 바이너리의 릴리스 페이지에서 `linux-arm64` / `aarch64` 아티팩트를 확인하세요.

## 지속성과 백업

OpenClaw 상태는 다음 위치에 있습니다:

  * `~/.openclaw/` — `openclaw.json`, 에이전트별 `auth-profiles.json`, 채널/제공자 상태, 세션.
  * `~/.openclaw/workspace/` — 에이전트 작업 공간([SOUL.md](<http://SOUL.md>), 메모리, 아티팩트).


이들은 재부팅 후에도 유지됩니다. 휴대 가능한 스냅샷은 다음으로 생성합니다:

bashCopy code
[code]
    openclaw backup create
[/code]

이 항목들을 SSD에 보관하면 SD 카드보다 성능과 수명이 모두 향상됩니다.

## 문제 해결

**메모리 부족** \-- `free -h`로 스왑이 활성 상태인지 확인하세요. 사용하지 않는 서비스를 비활성화하세요(`sudo systemctl disable cups bluetooth avahi-daemon`). API 기반 모델만 사용하세요.

**느린 성능** \-- SD 카드 대신 USB SSD를 사용하세요. `vcgencmd get_throttled`로 CPU 스로틀링을 확인하세요(`0x0`이 반환되어야 함).

**서비스가 시작되지 않음** \-- `journalctl --user -u openclaw-gateway.service --no-pager -n 100`으로 로그를 확인하고 `openclaw doctor --non-interactive`를 실행하세요. 헤드리스 Pi인 경우 lingering이 활성화되어 있는지도 확인하세요: `sudo loginctl enable-linger "$(whoami)"`.

**ARM 바이너리 문제** \-- skill이 "exec format error"로 실패하면 해당 바이너리에 ARM64 빌드가 있는지 확인하세요. `uname -m`으로 아키텍처를 확인하세요(`aarch64`가 표시되어야 함).

**WiFi 끊김** \-- WiFi 전원 관리를 비활성화하세요: `sudo iwconfig wlan0 power off`.

## 다음 단계

  * [채널](</ko/channels>) \-- Telegram, WhatsApp, Discord 등을 연결
  * [Gateway 구성](</ko/gateway/configuration>) \-- 모든 구성 옵션
  * [업데이트](</ko/install/updating>) \-- OpenClaw를 최신 상태로 유지


## 관련 항목

  * [설치 개요](</ko/install>)
  * [Linux 서버](</ko/vps>)
  * [플랫폼](</ko/platforms>)


Was this useful?YesNo