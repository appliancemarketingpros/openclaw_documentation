---
title: 자동 완성
source_url: https://docs.openclaw.ai/ko/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

셸 자동 완성 스크립트를 생성하고, 선택적으로 셸 프로필에 설치합니다.

## 사용법

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## 옵션

  * `-s, --shell <shell>`: 셸 대상 (`zsh`, `bash`, `powershell`, `fish`; 기본값: `zsh`)
  * `-i, --install`: 셸 프로필에 source 줄을 추가해 자동 완성 설치
  * `--write-state`: stdout에 출력하지 않고 자동 완성 스크립트를 `$OPENCLAW_STATE_DIR/completions`에 씀
  * `-y, --yes`: 설치 확인 프롬프트 건너뛰기


## 참고

  * `--install`은 셸 프로필에 작은 "OpenClaw Completion" 블록을 쓰고 이를 캐시된 스크립트에 연결합니다.
  * `--install`이나 `--write-state` 없이 실행하면 명령은 스크립트를 stdout에 출력합니다.
  * 자동 완성 생성은 중첩된 하위 명령까지 포함되도록 명령 트리를 즉시 로드합니다.


## 관련

  * [CLI 참조](</ko/cli>)


Was this useful?YesNo