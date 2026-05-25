---
title: 문서
source_url: https://docs.openclaw.ai/ko/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

터미널에서 라이브 OpenClaw 문서 인덱스를 검색합니다. 이 명령은 공개 Mintlify 호스팅 문서 MCP 검색 엔드포인트인 `https://docs.openclaw.ai/mcp.SearchOpenClaw`를 셸로 호출하고 결과를 터미널에 렌더링합니다.

## 사용법

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

인수:

인수 | 설명  
---|---  
`[query...]` | 자유 형식 검색 쿼리입니다. 여러 단어로 된 쿼리는 공백으로 결합되어 하나로 전송됩니다.  
  
## 예시

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

쿼리가 없으면 `openclaw docs`는 검색을 실행하는 대신 문서 진입점 URL과 예시 검색 명령을 출력합니다.

## 작동 방식

`openclaw docs`는 `mcporter` CLI를 호출해 문서 검색 MCP 도구를 실행한 다음, 도구 출력의 `Title: / Link: / Content:` 블록을 결과 목록으로 파싱합니다.

`mcporter`를 확인하기 위해 OpenClaw는 다음 순서로 검사합니다.

  1. `PATH`의 `mcporter`(있으면 직접 사용).
  2. `pnpm`이 설치되어 있으면 `pnpm dlx mcporter ...`.
  3. `npx`가 설치되어 있으면 `npx -y mcporter ...`.


사용 가능한 항목이 없으면 이 명령은 `pnpm` 설치(`npm install -g pnpm`)를 안내하는 힌트와 함께 실패합니다.

검색 호출은 고정된 30초 제한 시간을 사용합니다. 결과 스니펫은 항목당 약 220자로 잘립니다.

## 출력

서식 있는(TTY) 터미널에서는 결과가 제목 다음에 글머리 기호 목록으로 렌더링됩니다. 각 글머리 기호는 페이지 제목, 링크된 문서 URL, 그리고 다음 줄의 짧은 스니펫을 표시합니다. 빈 결과는 "결과가 없습니다."를 출력합니다.

서식 없는 출력(파이프, `--no-color`, 스크립트)에서는 동일한 데이터가 Markdown으로 렌더링됩니다.

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## 종료 코드

코드 | 의미  
---|---  
`0` | 검색에 성공했습니다(결과가 0개인 응답 포함).  
`1` | MCP 도구 호출이 실패했습니다. stderr가 인라인으로 출력됩니다.  
  
## 관련 항목

  * [CLI 참조](</ko/cli>)
  * [라이브 문서](<https://docs.openclaw.ai>)


Was this useful?YesNo