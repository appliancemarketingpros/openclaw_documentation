---
title: 설정
source_url: https://docs.openclaw.ai/ko/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

기본 구성과 에이전트 작업 영역을 초기화합니다. 온보딩 플래그가 있으면 마법사도 실행합니다.

## 옵션

플래그 | 설명  
---|---  
`--workspace <dir>` | 에이전트 작업 영역 디렉터리(기본값 `~/.openclaw/workspace`, `agents.defaults.workspace`로 저장됨).  
`--wizard` | 대화형 온보딩을 실행합니다.  
`--non-interactive` | 프롬프트 없이 온보딩을 실행합니다.  
`--mode <mode>` | 온보딩 모드: `local` 또는 `remote`.  
`--import-from <provider>` | 온보딩 중 실행할 마이그레이션 제공자입니다.  
`--import-source <path>` | `--import-from`의 소스 에이전트 홈입니다.  
`--import-secrets` | 온보딩 마이그레이션 중 지원되는 비밀 정보를 가져옵니다.  
`--remote-url <url>` | 원격 Gateway WebSocket URL입니다.  
`--remote-token <token>` | 원격 Gateway 토큰(선택 사항)입니다.  
  
### 마법사 자동 트리거

`openclaw setup`은 `--wizard` 없이도 다음 플래그 중 하나가 명시적으로 있으면 마법사를 실행합니다.

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## 예시

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## 참고

  * 일반 `openclaw setup`은 전체 온보딩 흐름을 실행하지 않고 구성과 작업 영역을 초기화합니다.
  * 일반 setup 이후 전체 안내 과정을 진행하려면 `openclaw onboard`를 실행하고, 대상 변경을 하려면 `openclaw configure`를 실행하거나, 채널 계정을 추가하려면 `openclaw channels add`를 실행하세요.
  * Hermes 상태가 감지되면 대화형 온보딩에서 마이그레이션을 자동으로 제안할 수 있습니다. 가져오기 온보딩에는 새 setup이 필요합니다. 온보딩 외부에서 드라이런 계획, 백업, 덮어쓰기 모드를 사용하려면 [마이그레이션](</ko/cli/migrate>)을 사용하세요.


## 관련

  * [CLI 참조](</ko/cli>)
  * [온보딩(CLI)](</ko/start/wizard>)
  * [시작하기](</ko/start/getting-started>)
  * [설치 개요](</ko/install>)


Was this useful?YesNo