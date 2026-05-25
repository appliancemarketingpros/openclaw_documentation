---
title: Tokenjuice
source_url: https://docs.openclaw.ai/ko/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice`는 명령이 이미 실행된 후 시끄러운 `exec` 및 `bash` 도구 결과를 압축하는 선택적 번들 plugin입니다.

이 plugin은 명령 자체가 아니라 반환되는 `tool_result`를 변경합니다. Tokenjuice는 shell 입력을 다시 쓰거나, 명령을 재실행하거나, 종료 코드를 바꾸지 않습니다.

현재 이 기능은 PI 임베디드 실행과 Codex app-server harness의 OpenClaw 동적 도구에 적용됩니다. Tokenjuice는 OpenClaw의 tool-result 미들웨어에 hook을 걸고, 출력이 활성 harness 세션으로 돌아가기 전에 이를 trim합니다.

## plugin 활성화

빠른 경로:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

동등한 명령:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw는 이미 이 plugin을 포함하고 있습니다. 별도의 `plugins install` 또는 `tokenjuice install openclaw` 단계는 없습니다.

config를 직접 편집하고 싶다면:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## tokenjuice가 변경하는 것

  * 세션으로 다시 전달되기 전에 시끄러운 `exec` 및 `bash` 결과를 압축합니다.
  * 원래 명령 실행은 그대로 유지합니다.
  * 정확한 파일 내용 읽기와 tokenjuice가 원본 그대로 남겨야 하는 다른 명령은 보존합니다.
  * opt-in 방식으로 유지됩니다. 모든 곳에서 verbatim 출력을 원한다면 plugin을 비활성화하세요.


## 동작 확인

  1. plugin을 활성화합니다.
  2. `exec`를 호출할 수 있는 세션을 시작합니다.
  3. `git status` 같은 시끄러운 명령을 실행합니다.
  4. 반환된 도구 결과가 원시 shell 출력보다 더 짧고 구조화되어 있는지 확인합니다.


## plugin 비활성화

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

또는:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## 관련

  * [Exec tool](</ko/tools/exec>)
  * [Thinking levels](</ko/tools/thinking>)
  * [Context engine](</ko/concepts/context-engine>)


Was this useful?YesNo