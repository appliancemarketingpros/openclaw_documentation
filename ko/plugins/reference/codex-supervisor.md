---
title: Codex Supervisor Plugin
source_url: https://docs.openclaw.ai/ko/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Codex Supervisor Plugin

OpenClaw에서 Codex app-server 세션을 감독합니다.

## 배포

  * 패키지: `@openclaw/codex-supervisor`
  * 설치 경로: OpenClaw에 포함됨


## 표면

계약: 도구

## 세션 목록

`codex_sessions_list`는 기본적으로 로드된 Codex 세션만 표시합니다. 저장된 기록을 포함하려면 `include_stored`를 설정하세요. Plugin은 Codex app-server의 state-DB 전용 목록 경로를 사용하며, 저장된 결과를 기본적으로 200개로 제한합니다. 이 제한을 낮추거나 높이려면 `max_stored_sessions`를 전달하세요. 최대 1000개까지 가능합니다.

Was this useful?YesNo

Open issue