---
title: 설정
source_url: https://docs.openclaw.ai/ko/cli/config
scraped_at: 2026-05-25
---

`openclaw.json`의 비대화형 편집을 위한 구성 도우미입니다. 경로별로 값을 get/set/patch/unset/file/schema/validate하고 활성 구성 파일을 출력합니다. 하위 명령 없이 실행하면 구성 마법사가 열립니다(`openclaw configure`와 동일).

## 루트 옵션

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc2VjdGlvbiA8c2VjdGlvbg " type="string"> 하위 명령 없이 `openclaw config`를 실행할 때 반복해서 지정할 수 있는 안내식 설정 섹션 필터입니다.

지원되는 안내 섹션: `workspace`, `model`, `web`, `gateway`, `daemon`, `channels`, `plugins`, `skills`, `health`.

## 예시

bashCopy code
[code]
    openclaw config fileopenclaw config --section modelopenclaw config --section gateway --section daemonopenclaw config schemaopenclaw config get browser.executablePathopenclaw config set browser.executablePath "/usr/bin/google-chrome"openclaw config set browser.profiles.work.executablePath "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"openclaw config set agents.defaults.heartbeat.every "2h"openclaw config set agents.list[0].tools.exec.node "node-id-or-name"openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKENopenclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode jsonopenclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config unset plugins.entries.brave.config.webSearch.apiKeyopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-runopenclaw config validateopenclaw config validate --json
[/code]

### `config schema`

`openclaw.json`용으로 생성된 JSON 스키마를 JSON으로 stdout에 출력합니다.

포함 내용

  * 현재 루트 구성 스키마와 편집기 도구용 루트 `$schema` 문자열 필드.
  * Control UI에서 사용하는 필드 `title` 및 `description` 문서 메타데이터.
  * 일치하는 필드 문서가 있으면 중첩 객체, 와일드카드(`*`), 배열 항목(`[]`) 노드가 동일한 `title` / `description` 메타데이터를 상속합니다.
  * 일치하는 필드 문서가 있으면 `anyOf` / `oneOf` / `allOf` 분기도 동일한 문서 메타데이터를 상속합니다.
  * 런타임 매니페스트를 로드할 수 있을 때 최선의 실시간 Plugin + 채널 스키마 메타데이터.
  * 현재 구성이 유효하지 않은 경우에도 깔끔한 대체 스키마.

관련 런타임 RPC

`config.schema.lookup`은 얕은 스키마 노드(`title`, `description`, `type`, `enum`, `const`, 공통 범위), 일치하는 UI 힌트 메타데이터, 즉시 하위 요약과 함께 정규화된 구성 경로 하나를 반환합니다. Control UI 또는 사용자 지정 클라이언트에서 경로 범위 드릴다운에 사용하세요.

bashCopy code
[code]
    openclaw config schema
[/code]

다른 도구로 검사하거나 검증하려면 파일로 파이프하세요.

bashCopy code
[code]
    openclaw config schema > openclaw.schema.json
[/code]

### 경로

경로는 점 표기법 또는 대괄호 표기법을 사용합니다.

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config get agents.list[0].id
[/code]

특정 agent를 대상으로 지정하려면 agent 목록 인덱스를 사용하세요.

bashCopy code
[code]
    openclaw config get agents.listopenclaw config set agents.list[1].tools.exec.node "node-id-or-name"
[/code]

## 값

값은 가능하면 JSON5로 파싱되고, 그렇지 않으면 문자열로 처리됩니다. JSON5 파싱을 요구하려면 `--strict-json`을 사용하세요. `--json`은 레거시 별칭으로 계속 지원됩니다.

bashCopy code
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"openclaw config set gateway.port 19001 --strict-jsonopenclaw config set channels.whatsapp.groups '["*"]' --strict-json
[/code]

`config get <path> --json`은 터미널 형식의 텍스트 대신 원시 값을 JSON으로 출력합니다.

해당 맵에 항목을 추가할 때는 `--merge`를 사용하세요.

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set models.providers.ollama.models '[{"id":"llama3.2","name":"Llama 3.2"}]' --strict-json --merge
[/code]

제공한 값이 완전한 대상 값이 되도록 의도한 경우에만 `--replace`를 사용하세요.

## `config set` 모드

`openclaw config set`은 네 가지 할당 방식을 지원합니다.

### 값 모드

bashCopy code
[code]
    openclaw config set <path> <value>
[/code]

### SecretRef 빌더 모드

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN
[/code]

### Provider 빌더 모드

Provider 빌더 모드는 `secrets.providers.<alias>` 경로만 대상으로 합니다.

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-timeout-ms 5000
[/code]

### 배치 모드

bashCopy code
[code]
    openclaw config set --batch-json '[  {    "path": "secrets.providers.default",    "provider": { "source": "env" }  },  {    "path": "channels.discord.token",    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }  }]'
[/code]

bashCopy code
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
[/code]

배치 파싱은 항상 배치 페이로드(`--batch-json`/`--batch-file`)를 신뢰 기준으로 사용합니다. `--strict-json` / `--json`은 배치 파싱 동작을 변경하지 않습니다.

## `config patch`

경로 기반 `config set` 명령을 여러 번 실행하는 대신 구성 형태의 패치를 붙여 넣거나 파이프하려면 `config patch`를 사용하세요. 입력은 JSON5 객체입니다. 객체는 재귀적으로 병합되고, 배열과 스칼라 값은 대상 값을 교체하며, `null`은 대상 경로를 삭제합니다.

bashCopy code
[code]
    openclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config patch --file ./openclaw.patch.json5
[/code]

원격 설정 스크립트에 유용하도록 stdin으로 패치를 파이프할 수도 있습니다.

bashCopy code
[code]
    ssh openclaw-host 'openclaw config patch --stdin --dry-run' < ./openclaw.patch.json5ssh openclaw-host 'openclaw config patch --stdin' < ./openclaw.patch.json5
[/code]

예시 패치:

json5Copy code
[code]
    {  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

객체나 배열 하나가 재귀적으로 패치되는 대신 제공한 값과 정확히 같아져야 할 때는 `--replace-path <path>`를 사용하세요.

bashCopy code
[code]
    openclaw config patch --file ./discord.patch.json5 --replace-path 'channels.discord.guilds["123"].channels'
[/code]

`--dry-run`은 쓰기 없이 스키마 및 SecretRef 해석 가능성 검사를 실행합니다. exec 기반 SecretRefs는 dry-run 중 기본적으로 건너뜁니다. dry-run에서 provider 명령을 실행하도록 의도한 경우 `--allow-exec`를 추가하세요.

JSON 경로/값 모드는 SecretRefs와 providers 모두에 대해 계속 지원됩니다.

bashCopy code
[code]
    openclaw config set channels.discord.token \  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \  --strict-json openclaw config set secrets.providers.vaultfile \  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \  --strict-json
[/code]

## Provider 빌더 플래그

Provider 빌더 대상은 경로로 `secrets.providers.<alias>`를 사용해야 합니다.

공통 플래그

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>` (`file`, `exec`)

Env provider (--provider-source env)

  * `--provider-allowlist &lt;ENV_VAR&gt;` (반복 가능)

File provider (--provider-source file)

  * `--provider-path <path>` (필수)
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`
  * `--provider-allow-insecure-path`

Exec provider (--provider-source exec)

  * `--provider-command <path>` (필수)
  * `--provider-arg <arg>` (반복 가능)
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env &lt;KEY=VALUE&gt;` (반복 가능)
  * `--provider-pass-env &lt;ENV_VAR&gt;` (반복 가능)
  * `--provider-trusted-dir <path>` (반복 가능)
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`


강화된 exec provider 예시:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-json-only \  --provider-pass-env VAULT_TOKEN \  --provider-trusted-dir /usr/local/bin \  --provider-timeout-ms 5000
[/code]

## Dry run

`openclaw.json`에 쓰지 않고 변경 사항을 검증하려면 `--dry-run`을 사용하세요.

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run \  --json openclaw config set channels.discord.token \  --ref-provider vault \  --ref-source exec \  --ref-id discord/token \  --dry-run \  --allow-exec
[/code]

Dry-run 동작

  * 빌더 모드: 변경된 refs/providers에 대해 SecretRef 해석 가능성 검사를 실행합니다.
  * JSON 모드(`--strict-json`, `--json` 또는 배치 모드): 스키마 검증과 SecretRef 해석 가능성 검사를 실행합니다.
  * 알려진 미지원 SecretRef 대상 표면에 대해서도 정책 검증이 실행됩니다.
  * 정책 검사는 변경 후 전체 구성을 평가하므로, 부모 객체 쓰기(예: `hooks`를 객체로 설정)가 미지원 표면 검증을 우회할 수 없습니다.
  * Exec SecretRef 검사는 명령 부작용을 피하기 위해 dry-run 중 기본적으로 건너뜁니다.
  * exec SecretRef 검사에 참여하려면 `--dry-run`과 함께 `--allow-exec`를 사용하세요. 이 경우 provider 명령이 실행될 수 있습니다.
  * `--allow-exec`는 dry-run 전용이며 `--dry-run` 없이 사용하면 오류가 발생합니다.

\--dry-run --json 필드

`--dry-run --json`은 기계가 읽을 수 있는 보고서를 출력합니다:

  * `ok`: 드라이런 통과 여부
  * `operations`: 평가된 할당 수
  * `checks`: 스키마/해결 가능성 검사가 실행되었는지 여부
  * `checks.resolvabilityComplete`: 해결 가능성 검사가 완료될 때까지 실행되었는지 여부(exec 참조를 건너뛴 경우 false)
  * `refsChecked`: 드라이런 중 실제로 해결된 참조 수
  * `skippedExecRefs`: `--allow-exec`가 설정되지 않아 건너뛴 exec 참조 수
  * `errors`: `ok=false`일 때의 구조화된 스키마/해결 가능성 실패


### JSON 출력 형태

json5Copy code
[code]
    {  ok: boolean,  operations: number,  configPath: string,  inputModes: ["value" | "json" | "builder", ...],  checks: {    schema: boolean,    resolvability: boolean,    resolvabilityComplete: boolean,  },  refsChecked: number,  skippedExecRefs: number,  errors?: [    {      kind: "schema" | "resolvability",      message: string,      ref?: string, // present for resolvability errors    },  ],}
[/code]

### 성공 예시

jsonCopy code
[code]
    {  "ok": true,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0}
[/code]

### 실패 예시

jsonCopy code
[code]
    {  "ok": false,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0,  "errors": [    {      "kind": "resolvability",      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",      "ref": "env:default:MISSING_TEST_SECRET"    }  ]}
[/code]

드라이런이 실패하는 경우

  * `config schema validation failed`: 변경 후 구성 형태가 유효하지 않습니다. 경로/값 또는 provider/ref 객체 형태를 수정하세요.
  * `Config policy validation failed: unsupported SecretRef usage`: 해당 자격 증명을 평문/문자열 입력으로 되돌리고 SecretRef는 지원되는 표면에서만 유지하세요.
  * `SecretRef assignment(s) could not be resolved`: 참조된 provider/ref를 현재 해결할 수 없습니다. env var 누락, 잘못된 파일 포인터, exec provider 실패 또는 provider/source 불일치가 원인일 수 있습니다.
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: 드라이런이 exec 참조를 건너뛰었습니다. exec 해결 가능성 검증이 필요하면 `--allow-exec`로 다시 실행하세요.
  * 배치 모드에서는 실패한 항목을 수정하고 쓰기 전에 `--dry-run`을 다시 실행하세요.


## 쓰기 안전성

`openclaw config set` 및 기타 OpenClaw 소유 구성 작성기는 디스크에 커밋하기 전에 변경 후 전체 구성을 검증합니다. 새 페이로드가 스키마 검증에 실패하거나 파괴적인 덮어쓰기처럼 보이면 활성 구성은 그대로 두고 거부된 페이로드를 `openclaw.json.rejected.*`로 그 옆에 저장합니다.

작은 편집에는 CLI 쓰기를 권장합니다.

bashCopy code
[code]
    openclaw config set gateway.reload.mode hybrid --dry-runopenclaw config set gateway.reload.mode hybridopenclaw config validate
[/code]

쓰기가 거부되면 저장된 페이로드를 확인하고 전체 구성 형태를 수정하세요.

bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".rejected.* 2>/dev/null | headopenclaw config validate
[/code]

직접 편집기로 쓰는 것도 허용되지만, 실행 중인 Gateway는 검증이 완료될 때까지 이를 신뢰할 수 없는 것으로 취급합니다. 유효하지 않은 직접 편집은 시작에 실패하거나 핫 리로드에서 건너뜁니다. Gateway는 `openclaw.json`을 다시 쓰지 않습니다. 접두사가 붙었거나 덮어써진 구성을 복구하거나 마지막으로 정상인 복사본을 복원하려면 `openclaw doctor --fix`를 실행하세요. [Gateway 문제 해결](</ko/gateway/troubleshooting#gateway-rejected-invalid-config>)을 참고하세요.

전체 파일 복구는 doctor 복구용으로만 예약되어 있습니다. Plugin 스키마 변경 또는 `minHostVersion` 불일치는 모델, provider, 인증 프로필, 채널, Gateway 노출, 도구, 메모리, 브라우저 또는 cron 구성 같은 관련 없는 사용자 설정을 롤백하는 대신 명확히 드러납니다.

## 하위 명령

  * `config file`: 활성 구성 파일 경로를 출력합니다(`OPENCLAW_CONFIG_PATH` 또는 기본 위치에서 해결됨). 경로는 심볼릭 링크가 아니라 일반 파일을 가리켜야 합니다.


편집 후 Gateway를 다시 시작하세요.

## 검증

Gateway를 시작하지 않고 현재 구성을 활성 스키마에 대해 검증합니다.

bashCopy code
[code]
    openclaw config validateopenclaw config validate --json
[/code]

`openclaw config validate`가 통과한 후에는 로컬 TUI를 사용해 같은 터미널에서 각 변경 사항을 검증하는 동안 내장 에이전트가 활성 구성을 문서와 비교하도록 할 수 있습니다.

bashCopy code
[code]
    openclaw chat
[/code]

그런 다음 TUI 안에서:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

일반적인 복구 루프:

* ### 문서와 비교

에이전트에게 현재 구성을 관련 문서 페이지와 비교하고 가장 작은 수정 사항을 제안하도록 요청하세요.

* ### 대상 지정 편집 적용

`openclaw config set` 또는 `openclaw configure`로 대상 지정 편집을 적용하세요.

* ### 다시 검증

각 변경 후 `openclaw config validate`를 다시 실행하세요.

* ### 런타임 문제에는 doctor 사용

검증은 통과하지만 런타임이 여전히 정상적이지 않다면 마이그레이션 및 복구 도움말을 위해 `openclaw doctor` 또는 `openclaw doctor --fix`를 실행하세요.

## 관련

  * [CLI 참조](</ko/cli>)
  * [구성](</ko/gateway/configuration>)


Was this useful?YesNo