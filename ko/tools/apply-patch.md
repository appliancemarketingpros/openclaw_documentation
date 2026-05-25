---
title: apply_patch 도구
source_url: https://docs.openclaw.ai/ko/tools/apply-patch
scraped_at: 2026-05-25
---

구조화된 패치 형식을 사용하여 파일 변경 사항을 적용합니다. 단일 `edit` 호출이 취약할 수 있는 다중 파일 또는 다중 헝크 편집에 적합합니다.

이 도구는 하나 이상의 파일 작업을 감싸는 단일 `input` 문자열을 받습니다.

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## 매개변수

  * `input` (필수): `*** Begin Patch`와 `*** End Patch`를 포함한 전체 패치 내용입니다.


## 참고 사항

  * 패치 경로는 상대 경로(워크스페이스 디렉터리 기준)와 절대 경로를 지원합니다.
  * `tools.exec.applyPatch.workspaceOnly`의 기본값은 `true`(워크스페이스 내부로 제한)입니다. 의도적으로 `apply_patch`가 워크스페이스 디렉터리 밖에 쓰거나 삭제하도록 하려는 경우에만 `false`로 설정하세요.
  * 파일 이름을 변경하려면 `*** Update File:` 헝크 안에서 `*** Move to:`를 사용하세요.
  * `*** End of File`은 필요할 때 EOF 전용 삽입을 표시합니다.
  * OpenAI 및 OpenAI Codex 모델에서 기본적으로 사용할 수 있습니다. 비활성화하려면 `tools.exec.applyPatch.enabled: false`를 설정하세요.
  * 선택적으로 다음을 통해 모델별로 제한할 수 있습니다. `tools.exec.applyPatch.allowModels`.
  * 구성은 `tools.exec` 아래에만 있습니다.


## 예시

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## 관련 항목

[**Diff** 변경 사항 표시를 위한 읽기 전용 diff 뷰어입니다. ](</ko/tools/diffs>) [**Exec 도구** 에이전트에서 셸 명령을 실행합니다. ](</ko/tools/exec>) [**코드 실행** xAI를 사용하는 샌드박스 원격 Python 분석입니다. ](</ko/tools/code-execution>)

Was this useful?YesNo