---
title: Uninstall
source_url: https://docs.openclaw.ai/ko/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

gateway 서비스 + 로컬 데이터를 제거합니다(CLI는 유지됨).

옵션:

  * `--service`: gateway 서비스를 제거합니다
  * `--state`: 상태 및 config를 제거합니다
  * `--workspace`: 워크스페이스 디렉터리를 제거합니다
  * `--app`: macOS 앱을 제거합니다
  * `--all`: 서비스, 상태, 워크스페이스, 앱을 모두 제거합니다
  * `--yes`: 확인 프롬프트를 건너뜁니다
  * `--non-interactive`: 프롬프트를 비활성화합니다. `--yes`가 필요합니다
  * `--dry-run`: 파일을 제거하지 않고 수행할 작업만 출력합니다


예시:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

참고:

  * 상태 또는 워크스페이스를 제거하기 전에 복원 가능한 스냅샷이 필요하면 먼저 `openclaw backup create`를 실행하세요.
  * `--all`은 서비스, 상태, 워크스페이스, 앱을 함께 제거하는 축약형입니다.
  * `--non-interactive`에는 `--yes`가 필요합니다.


## 관련

  * [CLI reference](</ko/cli>)
  * [Uninstall](</ko/install/uninstall>)


Was this useful?YesNo