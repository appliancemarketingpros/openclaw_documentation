---
title: Docker VM 런타임
source_url: https://docs.openclaw.ai/ko/install/docker-vm-runtime
scraped_at: 2026-05-25
---

VM 기반 Docker 설치(예: GCP, Hetzner 및 유사한 VPS 제공업체)를 위한 공유 런타임 단계입니다.

## 필요한 바이너리를 이미지에 포함하기

실행 중인 컨테이너 안에 바이너리를 설치하는 것은 함정입니다. 런타임에 설치한 것은 재시작 시 모두 사라집니다.

Skills에 필요한 모든 외부 바이너리는 이미지 빌드 시점에 설치해야 합니다.

아래 예시는 일반적인 바이너리 세 가지를 보여줍니다.

  * Gmail 액세스를 위한 `gog`(`gogcli`에서 제공)
  * Google Places용 `goplaces`
  * WhatsApp용 `wacli`


이는 예시이며, 전체 목록이 아닙니다. 같은 패턴으로 필요한 만큼 바이너리를 설치할 수 있습니다.

나중에 추가 바이너리에 의존하는 새 Skills를 추가하는 경우 다음을 수행해야 합니다.

  1. Dockerfile 업데이트
  2. 이미지 다시 빌드
  3. 컨테이너 재시작


**Dockerfile 예시**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## 빌드 및 실행

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

`pnpm install --frozen-lockfile` 중 `Killed` 또는 `exit code 137`로 빌드가 실패하면 VM 메모리가 부족한 것입니다. 다시 시도하기 전에 더 큰 머신 클래스를 사용하세요.

바이너리를 확인합니다.

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

예상 출력:

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

Gateway 확인:

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

예상 출력:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## 무엇이 어디에 영구 저장되는가

OpenClaw는 Docker에서 실행되지만, Docker가 신뢰할 수 있는 원본은 아닙니다. 모든 장기 상태는 재시작, 재빌드, 재부팅 후에도 유지되어야 합니다.

구성 요소 | 위치 | 영구 저장 메커니즘 | 참고  
---|---|---|---  
Gateway 구성 | `/home/node/.openclaw/` | 호스트 볼륨 마운트 | `openclaw.json`, `.env` 포함  
모델 인증 프로필 | `/home/node/.openclaw/agents/` | 호스트 볼륨 마운트 | `agents/<agentId>/agent/auth-profiles.json` (OAuth, API 키)  
인증 프로필 키 | `/home/node/.config/openclaw/` | 호스트 볼륨 마운트 | OAuth 인증 프로필 토큰 자료를 위한 로컬 암호화 키  
Skill 구성 | `/home/node/.openclaw/skills/` | 호스트 볼륨 마운트 | Skill 수준 상태  
에이전트 작업공간 | `/home/node/.openclaw/workspace/` | 호스트 볼륨 마운트 | 코드 및 에이전트 아티팩트  
WhatsApp 세션 | `/home/node/.openclaw/` | 호스트 볼륨 마운트 | QR 로그인을 보존  
Gmail 키링 | `/home/node/.openclaw/` | 호스트 볼륨 + 비밀번호 | `GOG_KEYRING_PASSWORD` 필요  
Plugin 패키지 | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | 호스트 볼륨 마운트 | 다운로드 가능한 Plugin 패키지 루트  
외부 바이너리 | `/usr/local/bin/` | Docker 이미지 | 빌드 시점에 포함해야 함  
Node 런타임 | 컨테이너 파일 시스템 | Docker 이미지 | 이미지 빌드마다 다시 빌드됨  
OS 패키지 | 컨테이너 파일 시스템 | Docker 이미지 | 런타임에 설치하지 마세요  
Docker 컨테이너 | 임시 | 재시작 가능 | 삭제해도 안전함  
  
## 업데이트

VM에서 OpenClaw를 업데이트하려면:

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## 관련 문서

  * [Docker](</ko/install/docker>)
  * [Podman](</ko/install/podman>)
  * [ClawDock](</ko/install/clawdock>)


Was this useful?YesNo