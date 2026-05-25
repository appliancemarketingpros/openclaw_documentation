---
title: 초기화
source_url: https://docs.openclaw.ai/ko/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

로컬 설정/상태를 초기화합니다(CLI는 설치된 상태로 유지됨).

옵션:

  * `--scope <scope>`: `config`, `config+creds+sessions`, 또는 `full`
  * `--yes`: 확인 프롬프트 건너뛰기
  * `--non-interactive`: 프롬프트 비활성화, `--scope`와 `--yes` 필요
  * `--dry-run`: 파일을 제거하지 않고 수행 작업만 출력


예시:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

참고:

  * 로컬 상태를 제거하기 전에 복원 가능한 스냅샷을 원한다면 먼저 `openclaw backup create`를 실행하세요.
  * `--scope`를 생략하면 `openclaw reset`은 무엇을 제거할지 선택하는 대화형 프롬프트를 사용합니다.
  * `--non-interactive`는 `--scope`와 `--yes`가 모두 설정된 경우에만 유효합니다.


## 관련 항목

  * [CLI reference](</ko/cli>)


Was this useful?YesNo