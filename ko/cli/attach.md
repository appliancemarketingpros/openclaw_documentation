---
title: CLI 연결
source_url: https://docs.openclaw.ai/ko/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach`는 하나의 Gateway 세션에 바인딩된 엄격한 임시 MCP 구성으로 Claude Code를 실행합니다.

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

옵션:

  * `--session <key>`는 권한 부여를 Gateway 세션에 바인딩합니다. 기본값은 메인 세션입니다.
  * `--ttl <ms>`는 밀리초 단위의 양수 권한 부여 TTL을 요청합니다. Gateway는 자체 상한을 적용합니다.
  * `--bin <path>`는 Claude Code 바이너리를 선택합니다. 기본값은 `claude`입니다.
  * `--print-config`는 임시 `.mcp.json`을 쓰고, 실행 명령과 env를 출력하며, TTL이 만료될 때까지 권한 부여를 활성 상태로 둡니다.


전달자 토큰은 argv가 아니라 환경 변수를 통해 전달됩니다. OpenClaw는 주변 Claude MCP 서버가 연결된 세션에 참여하지 않도록 `--strict-mcp-config --mcp-config <path>`로 Claude Code를 실행합니다. 일반 실행은 Claude Code 프로세스가 종료될 때 권한 부여를 취소합니다.

참고 항목: [Gateway CLI](</ko/cli/gateway>), [MCP CLI](</ko/cli/mcp>), [ACP CLI](</ko/cli/acp>).

Was this useful?YesNo

Open issue