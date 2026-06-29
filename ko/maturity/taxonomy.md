---
title: 성숙도 분류体系
source_url: https://docs.openclaw.ai/ko/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# 성숙도 분류 체계

스코어카드의 기반 모델

서피스 > 카테고리 > 기능 > 증거.

50개 서피스를 4개 계열로 묶었으며, 모든 카테고리는 표준 문서와 QA 적용 범위 ID에 연결됩니다.

제품 영역 보기 / 상세 분류 체계 열기 / [점수 보기](</ko/maturity/scorecard>)

## 이 페이지 읽는 방법

서피스는 Gateway 런타임, Discord, macOS 앱 같은 제품 영역입니다. 각 서피스에는 카테고리가 포함되고, 각 카테고리에는 QA 시나리오가 다루는 기능 수준 점검 항목이 포함됩니다. 릴리스 수준 판단에는 스코어카드를 사용하고, 그 아래의 모델을 살펴볼 때는 이 페이지를 사용하세요.

## 성숙도 수준

M0계획됨방향은 정해졌지만 지원되는 사용자 경로는 아직 없습니다.승격: 설계 이슈, 소유자, 대상 서피스가 존재합니다.

M1실험적주의 사항, 플래그, 소스 빌드 또는 유지관리자 전용 흐름 뒤에 구현되어 있습니다.승격: 유지관리자가 현재 main에서 시나리오를 실행할 수 있습니다.

M2알파실제 사용자가 시도할 수 있지만, 변경으로 인한 호환성 깨짐과 불완전한 UX가 예상됩니다.승격: 문서화된 설정, 기본 테스트, 알려진 주의 사항, 그리고 최소 하나의 실제 환경 증거가 있습니다.

M3베타공개 경로가 존재하며, 주요 워크플로는 제한된 주의 사항 안에서 사용할 수 있습니다.승격: 설치/업데이트 문서, 회귀 테스트, 지원 런북, 예상 환경 전반에서 성공한 시나리오 증거가 있습니다.

M4안정일반 사용자에게 권장되는 경로입니다. 실패는 회귀로 간주됩니다.승격: 릴리스 게이트, doctor/문제 해결 경로, 폭넓은 문서, 반복된 실제 사용 증거가 있습니다.

M5Clawesome다듬어져 있고, 사용하기 즐거우며, 계측이 잘 되어 있고, 가장 우수한 비교 대상 워크플로와 경쟁할 수 있습니다.승격: 안정 수준에 더해 대표 사용자 전반의 사용자 스코어카드를 통과합니다.

## 제품 영역

### 핵심

CLI M4안정7개 영역 - 90% 완료 Gateway 런타임 M4안정13개 영역 - 89% 완료 에이전트 런타임 M3베타9개 영역 - 79% 완료 세션, 메모리 및 컨텍스트 엔진 M3베타9개 영역 - 79% 완료 채널 프레임워크 M3베타8개 영역 - 79% 완료 관측 가능성 M3베타5개 영역 - 79% 완료 Gateway 웹 앱 M3베타6개 영역 - 79% 완료 Plugin M3베타9개 영역 - 79% 완료 보안, 인증, 페어링 및 비밀 정보 M3베타6개 영역 - 79% 완료 자동화: Cron, 훅, 작업, 폴링 M3베타6개 영역 - 79% 완료 미디어 이해 및 미디어 생성 M2알파6개 영역 - 68% 완료 음성 및 실시간 대화 M2알파6개 영역 - 68% 완료 TUI M2알파5개 영역 - 66% 완료 ClawHub M2알파4개 영역 - 62% 완료 OpenClaw App SDK M2알파6개 영역 - 53% 완료

### 플랫폼

Linux Gateway 호스트 M4안정5개 영역 - 89% 완료 macOS Gateway 호스트 M4안정7개 영역 - 88% 완료 Docker 및 Podman 호스팅 M3베타4개 영역 - 79% 완료 WSL2를 통한 Windows M3베타6개 영역 - 79% 완료 Raspberry Pi 및 소형 Linux 기기 M3베타4개 영역 - 79% 완료 macOS 보조 앱 M3베타8개 영역 - 78% 완료 Android 앱 M2알파7개 영역 - 66% 완료 네이티브 Windows M2알파4개 영역 - 66% 완료 Kubernetes 호스팅 M2알파4개 영역 - 61% 완료 iOS 앱 M1실험적8개 영역 - 44% 완료 Nix 설치 경로 M1실험적5개 영역 - 44% 완료 watchOS 컴패니언 표면 M1실험적5개 영역 - 44% 완료 Linux 컴패니언 앱 M0계획됨5개 영역 - 21% 완료 네이티브 Windows 컴패니언 앱 M0계획됨5개 영역 - 21% 완료

### 채널

Discord M4안정6개 영역 - 87% 완료 Telegram M3베타5개 영역 - 78% 완료 Slack M3베타5개 영역 - 78% 완료 iMessage 및 BlueBubbles M3베타5개 영역 - 78% 완료 WhatsApp M3베타5개 영역 - 78% 완료 Matrix M2알파6개 영역 - 67% 완료 Google Chat M2알파5개 영역 - 66% 완료 Microsoft Teams M2알파5개 영역 - 66% 완료 Signal M2알파5개 영역 - 66% 완료 Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, 지역 채널 M2알파4개 영역 - 58% 완료 Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2알파4개 영역 - 54% 완료 음성 통화 채널 M1실험적5개 영역 - 44% 완료

### 제공자 및 도구

브라우저 자동화, exec 및 샌드박스 도구 M3베타3개 영역 - 79% 완료 OpenAI 및 Codex 제공자 경로 M3베타5개 영역 - 79% 완료 웹 검색 도구 M3베타4개 영역 - 79% 완료 Anthropic 제공자 경로 M3베타5개 영역 - 78% 완료 Google 제공자 경로 M3베타5개 영역 - 78% 완료 OpenRouter 제공자 경로 M3베타4개 영역 - 78% 완료 이미지, 비디오 및 음악 생성 도구 M2알파5개 영역 - 68% 완료 로컬 모델 제공자: Ollama, vLLM, SGLang, LM Studio M2알파5개 영역 - 68% 완료 롱테일 호스팅 제공자 M2알파3개 영역 - 68% 완료

## 세부 정보

### 코어

CLI - M4 안정 - 7개 영역

일반 설정 및 복구 경로는 설치, CLI, Gateway 문서 전반에 문서화되어 있습니다. 플랫폼별 Windows 경로는 WSL2를 통한 Windows 및 네이티브 Windows 행에서 추적됩니다.

적용 범위 실험적 - 4%품질 안정 - 83%완성도 안정 - 90%부분 - 6

CLI 설정 6개 기능 / LTS 지원

실험적17%

안정89%

안정90%

[색인](</ko/install>), [설치 프로그램](</ko/install/installer>), [Node](</ko/install/node>), [업데이트](</ko/install/updating>)

온보딩 및 인증 설정 5개 기능 / LTS 지원

실험적0%

베타75%

안정89%

[온보딩](</ko/cli/onboard>), [구성](</ko/cli/configure>), [온보딩 개요](</ko/start/onboarding-overview>)

Plugin 및 채널 설정 5개 기능

실험적0%

베타75%

안정89%

[온보딩](</ko/cli/onboard>), [Plugin](</ko/cli/plugins>), [채널](</ko/cli/channels>)

Gateway 서비스 관리 5개 기능 / LTS 지원

실험적14%

안정87%

안정90%

[Gateway](</ko/cli/gateway>), [업데이트](</ko/install/updating>), [문제 해결](</ko/gateway/troubleshooting>)

CLI 관측 가능성 5개 기능 / LTS 지원

실험적0%

안정89%

안정90%

[상태](</ko/cli/status>), [상태 확인](</ko/cli/health>), [로그](</ko/cli/logs>), [진단](</ko/gateway/diagnostics>)

진단 10개 기능 / LTS 지원

실험적0%

안정89%

안정90%

[진단](</ko/cli/doctor>), [진단](</ko/gateway/doctor>), [비밀 정보](</ko/gateway/secrets>), [문제 해결](</ko/gateway/troubleshooting>)

업데이트 및 업그레이드 5개 기능 / LTS 지원

실험적0%

베타75%

안정89%

[업데이트](</ko/install/updating>), [업데이트](</ko/cli/update>), [문제 해결](</ko/gateway/troubleshooting>)

Gateway 런타임 - M4 안정 - 13개 영역

핵심 아키텍처, 인증, 페어링, 프로토콜 문서, 데몬 문서, CLI 런북은 범위가 넓고 최신 상태입니다.

범위 실험적 - 6%품질 안정 - 81%완성도 안정 - 89%부분 - 12

승인 및 원격 실행 6개 기능 / LTS 지원

실험적0%

베타75%

안정89%

[프로토콜](</ko/gateway/protocol>), [색인](</ko/gateway/security>)

HTTP API 4개 기능 / LTS 지원

실험적25%

안정90%

안정90%

[색인](</ko/gateway>), [OpenAI HTTP API](</ko/gateway/openai-http-api>), [OpenResponses HTTP API](</ko/gateway/openresponses-http-api>), [도구 호출 HTTP API](</ko/gateway/tools-invoke-http-api>), [후크](</ko/automation/hooks>), [색인](</ko/web>)

호스팅 웹 표면 4개 기능 / LTS 지원

실험적0%

안정89%

안정90%

[색인](</ko/gateway>), [아키텍처](</ko/concepts/architecture>), [제어 UI](</ko/web/control-ui>), [웹 채팅](</ko/web/webchat>), [캔버스](</ko/refactor/canvas>)

Gateway RPC API 및 이벤트 20개 기능 / LTS 지원

실험적9%

안정90%

안정90%

[프로토콜](</ko/gateway/protocol>), [색인](</ko/gateway>), [아키텍처](</ko/concepts/architecture>)

기기 인증 및 페어링 10개 기능 / LTS 지원

실험적0%

베타75%

안정89%

[프로토콜](</ko/gateway/protocol>), [페어링](</ko/gateway/pairing>), [색인](</ko/gateway/security>)

네트워크 접근 및 검색 6개 기능 / LTS 지원

실험적0%

베타75%

안정89%

[색인](</ko/gateway>), [검색](</ko/gateway/discovery>), [프로토콜](</ko/gateway/protocol>)

Node 및 원격 기능 8개 기능

실험적0%

베타75%

안정89%

[프로토콜](</ko/gateway/protocol>), [아키텍처](</ko/concepts/architecture>), [색인](</ko/nodes>)

상태, 진단 및 복구 7개 기능 / LTS 지원

실험적0%

베타75%

안정89%

[색인](</ko/gateway>), [진단](</ko/gateway/diagnostics>), [Doctor](</ko/gateway/doctor>)

프로토콜 호환성 기능 7개 / LTS 지원

실험적0%

베타75%

안정89%

[프로토콜](</ko/gateway/protocol>), [아키텍처](</ko/concepts/architecture>), [Typebox](</ko/concepts/typebox>), [브리지 프로토콜](</ko/gateway/bridge-protocol>)

역할 및 권한 기능 5개 / LTS 지원

실험적0%

베타75%

안정89%

[프로토콜](</ko/gateway/protocol>), [색인](</ko/gateway/security>)

Gateway 수명 주기 기능 7개 / LTS 지원

실험적33%

안정90%

안정90%

[색인](</ko/gateway>), [아키텍처](</ko/concepts/architecture>)

보안 제어 기능 6개 / LTS 지원

실험적0%

베타75%

안정89%

[색인](</ko/gateway/security>), [프로토콜](</ko/gateway/protocol>), [검색](</ko/gateway/discovery>)

WebSocket 연결 기능 8개 / LTS 지원

실험적13%

안정90%

안정90%

[프로토콜](</ko/gateway/protocol>), [아키텍처](</ko/concepts/architecture>)

에이전트 런타임 - M3 베타 - 9개 영역

메인 루프, 모델, 공급자 라우팅, 도구 스트리밍은 일급 기능이지만, 공급자 동작은 매주 바뀌며 릴리스마다 시나리오 검증이 필요합니다.

적용 범위 실험적 - 33%품질 베타 - 78%완성도 베타 - 79%부분적 - 6

에이전트 턴 실행 기능 3개 / LTS 지원

실험적29%

베타79%

베타79%

[에이전트 루프](</ko/concepts/agent-loop>), [에이전트](</ko/cli/agent>), [에이전트 런타임](</ko/concepts/agent-runtimes>)

외부 런타임 및 하위 에이전트 기능 4개

실험적30%

베타79%

베타79%

[에이전트 런타임](</ko/concepts/agent-runtimes>), [Anthropic](</ko/providers/anthropic>), [Google](</ko/providers/google>), [하위 에이전트](</ko/tools/subagents>)

호스팅 제공자 실행 기능 5개 / LTS 지원

실험적20%

베타79%

베타79%

[Openai](</ko/providers/openai>), [Anthropic](</ko/providers/anthropic>), [Google](</ko/providers/google>), [모델](</ko/concepts/models>)

로컬 및 자체 호스팅 제공자 기능 5개

실험적0%

알파68%

베타79%

[Ollama](</ko/providers/ollama>), [모델](</ko/concepts/models>), [에이전트](</ko/cli/agent>)

모델 및 런타임 선택 기능 4개 / LTS 지원

실험적25%

베타79%

베타79%

[모델](</ko/concepts/models>), [모델](</ko/cli/models>), [Openai](</ko/providers/openai>), [에이전트 런타임](</ko/concepts/agent-runtimes>)

제공자 인증 기능 10개 / LTS 지원

실험적24%

베타79%

베타79%

[모델](</ko/concepts/models>), [에이전트](</ko/cli/agent>), [모델](</ko/cli/models>), [Openai](</ko/providers/openai>), [Anthropic](</ko/providers/anthropic>), [Google](</ko/providers/google>), [하위 에이전트](</ko/tools/subagents>)

스트리밍 및 진행 상황 기능 2개

알파56%

베타79%

베타79%

[스트리밍](</ko/concepts/streaming>), [에이전트 루프](</ko/concepts/agent-loop>)

도구 호출 및 응답 처리 기능 3개 / LTS 지원

알파65%

베타79%

베타79%

[에이전트 루프](</ko/concepts/agent-loop>), [Ollama](</ko/providers/ollama>)

도구 실행 제어 6개 기능 / LTS 지원

알파50%

베타79%

베타79%

[샌드박스와 도구 정책과 Elevated 비교](</ko/gateway/sandbox-vs-tool-policy-vs-elevated>), [Agent 루프](</ko/concepts/agent-loop>), [하위 에이전트](</ko/tools/subagents>)

세션, 메모리 및 컨텍스트 엔진 - M3 베타 - 9개 영역

탄탄한 문서와 활발한 구현이 있습니다. 성숙도는 전사본 내구성, Compaction 품질, 클라이언트 간 동등성에 따라 달라집니다.

커버리지 실험적 - 30%품질 베타 - 77%완성도 베타 - 79%부분적 - 6

CLI 세션 및 트랜스크립트 관리 기능 2개 / LTS 지원

실험적0%

알파68%

베타79%

[세션](</ko/concepts/session>), [세션 관리 Compaction](</ko/reference/session-management-compaction>), [세션](</ko/cli/sessions>)

토큰 관리 기능 3개 / LTS 지원

실험적20%

베타79%

베타79%

[Compaction](</ko/concepts/compaction>), [컨텍스트](</ko/concepts/context>), [세션 관리 Compaction](</ko/reference/session-management-compaction>)

컨텍스트 엔진 기능 2개 / LTS 지원

알파57%

베타79%

베타79%

[컨텍스트](</ko/concepts/context>), [컨텍스트 엔진](</ko/concepts/context-engine>), [Codex 컨텍스트 엔진 하네스](</ko/plan/codex-context-engine-harness>)

클라이언트 간 기록 및 세션 동등성 기능 2개

실험적40%

베타79%

베타79%

[웹 채팅](</ko/web/webchat>), [Android](</ko/platforms/android>), [채널 라우팅](</ko/channels/channel-routing>)

진단, 유지관리 및 복구 기능 3개

실험적40%

베타79%

베타79%

[진단](</ko/gateway/diagnostics>), [세션 관리 Compaction](</ko/reference/session-management-compaction>), [플래그](</ko/diagnostics/flags>)

핵심 프롬프트 및 컨텍스트 기능 2개 / LTS 지원

실험적38%

베타79%

베타79%

[컨텍스트](</ko/concepts/context>), [트랜스크립트 위생](</ko/reference/transcript-hygiene>), [Discord](</ko/channels/discord>)

메모리 기능 5개

실험적46%

베타79%

베타79%

[메모리 구성](</ko/reference/memory-config>), [메모리 Qmd](</ko/concepts/memory-qmd>), [메모리](</ko/concepts/memory>), [Discord](</ko/channels/discord>)

세션 라우팅 기능 2개 / LTS 지원

실험적25%

베타79%

베타79%

[세션](</ko/concepts/session>), [채널 라우팅](</ko/channels/channel-routing>), [Discord](</ko/channels/discord>)

대화 기록 지속성 2개 기능 / LTS 지원됨

실험적0%

알파68%

베타79%

[세션 관리 Compaction](</ko/reference/session-management-compaction>), [대화 기록 위생](</ko/reference/transcript-hygiene>)

채널 프레임워크 - M3 베타 - 8개 영역

많은 채널은 Gateway 전달 및 라우팅 계약을 공유하지만, 채널 동작은 업스트림 API와 계정 정책 제약에 따라 달라집니다.

적용 범위 실험적 - 13%품질 베타 - 76%완성도 베타 - 79%부분 - 5

채널 작업 명령 및 승인 기능 5개

실험적0%

베타79%

베타79%

[그룹](</ko/channels/groups>), [Discord](</ko/channels/discord>), [Google Chat](</ko/channels/googlechat>), [Signal](</ko/channels/signal>), [Matrix](</ko/channels/matrix>)

채널 설정 기능 5개 / LTS 지원

실험적14%

베타79%

베타79%

[색인](</ko/channels>), [페어링](</ko/channels/pairing>), [문제 해결](</ko/channels/troubleshooting>), [SDK 채널 Plugin](</ko/plugins/sdk-channel-plugins>)

그룹 스레드 및 Ambient Room 동작 기능 5개

실험적36%

베타79%

베타79%

[그룹](</ko/channels/groups>), [그룹 메시지](</ko/channels/group-messages>), [Ambient Room 이벤트](</ko/channels/ambient-room-events>), [브로드캐스트 그룹](</ko/channels/broadcast-groups>), [Discord](</ko/channels/discord>)

인바운드 액세스 및 ID 게이트 기능 5개 / LTS 지원

실험적0%

알파68%

베타79%

[액세스 그룹](</ko/channels/access-groups>), [그룹](</ko/channels/groups>), [Discord](</ko/channels/discord>), [LINE](</ko/channels/line>)

미디어 첨부 파일 및 풍부한 채널 데이터 기능 4개

실험적0%

알파68%

베타79%

[LINE](</ko/channels/line>), [Signal](</ko/channels/signal>), [Google Chat](</ko/channels/googlechat>), [Matrix](</ko/channels/matrix>), [Discord](</ko/channels/discord>)

아웃바운드 전달 및 응답 파이프라인 기능 4개 / LTS 지원

실험적38%

베타79%

베타79%

[그룹](</ko/channels/groups>), [Ambient Room 이벤트](</ko/channels/ambient-room-events>), [Discord](</ko/channels/discord>), [Matrix](</ko/channels/matrix>), [구성 채널](</ko/gateway/config-channels>)

대화 라우팅 및 전달 기능 10개 / LTS 지원

실험적19%

베타79%

베타79%

[채널 라우팅](</ko/channels/channel-routing>), [그룹](</ko/channels/groups>), [Discord](</ko/channels/discord>), [Matrix](</ko/channels/matrix>), [문제 해결](</ko/channels/troubleshooting>), [구성 참조](</ko/gateway/configuration-reference>)

상태 건전성 및 운영자 제어 기능 4개 / LTS 지원

실험적0%

베타79%

베타79%

[상태](</ko/gateway/health>), [구성 참조](</ko/gateway/configuration-reference>), [문제 해결](</ko/channels/troubleshooting>), [Discord](</ko/channels/discord>)

관측성 - M3 베타 - 5개 영역

OTel, Prometheus, 로깅 및 진단 문서가 있습니다. 공개용 "운영자가 먼저 살펴봐야 할 항목" 성숙도 검토가 필요합니다.

적용 범위 Experimental - 18%품질 Beta - 75%완성도 Beta - 79%부분 지원 - 3

상태 및 복구 12개 기능 / LTS 지원

Experimental28%

Beta79%

Beta79%

[상태](</ko/gateway/health>), [Telegram](</ko/channels/telegram>), [Doctor](</ko/cli/doctor>), [Doctor](</ko/gateway/doctor>), [Sdk 하위 경로](</ko/plugins/sdk-subpaths>), [상태](</ko/cli/health>), [프로토콜](</ko/gateway/protocol>)

로깅 5개 기능 / LTS 지원

Experimental0%

Alpha68%

Beta79%

[로깅](</ko/logging>), [로깅](</ko/gateway/logging>), [로그](</ko/cli/logs>)

진단 수집 8개 기능

Experimental30%

Beta79%

Beta79%

[진단](</ko/gateway/diagnostics>), [상태](</ko/gateway/health>), [Codex Harness](</ko/plugins/codex-harness>), [프로토콜](</ko/gateway/protocol>)

텔레메트리 내보내기 13개 기능

Experimental33%

Beta79%

Beta79%

[Hooks](</ko/plugins/hooks>), [Opentelemetry](</ko/gateway/opentelemetry>), [로깅](</ko/logging>), [Sdk 하위 경로](</ko/plugins/sdk-subpaths>), [Diagnostics Otel](</ko/plugins/reference/diagnostics-otel>), [Prometheus](</ko/gateway/prometheus>), [Diagnostics Prometheus](</ko/plugins/reference/diagnostics-prometheus>)

세션 진단 4개 기능 / LTS 지원

Experimental0%

Alpha68%

Beta79%

[Opentelemetry](</ko/gateway/opentelemetry>), [Prometheus](</ko/gateway/prometheus>), [진단](</ko/gateway/diagnostics>), [프로토콜](</ko/gateway/protocol>)

Gateway 웹 앱 - M3 Beta - 6개 영역

웹 UI는 페어링, 채팅, PWA, Talk, 푸시, 원격 Gateway 흐름과 함께 문서화되어 있습니다. 교차 브라우저 및 모바일 PWA 스코어카드 이후 승격하세요.

적용 범위 Experimental - 4%품질 Beta - 74%완성도 Beta - 79%없음

브라우저 실시간 대화 기능 5개

실험적0%

알파68%

베타79%

[제어 UI](</ko/web/control-ui>), [프로토콜](</ko/gateway/protocol>), [대화](</ko/nodes/talk>)

브라우저 액세스 및 신뢰 기능 5개

실험적0%

알파68%

베타79%

[제어 UI](</ko/web/control-ui>), [대시보드](</ko/web/dashboard>), [Tailscale](</ko/gateway/tailscale>), [원격](</ko/gateway/remote>)

구성 기능 5개

실험적0%

알파68%

베타79%

[제어 UI](</ko/web/control-ui>), [구성](</ko/gateway/configuration>)

브라우저 UI 기능 10개

실험적8%

베타79%

베타79%

[제어 UI](</ko/web/control-ui>), [색인](</ko/web>), [대시보드](</ko/web/dashboard>), [프로토콜](</ko/gateway/protocol>)

웹채팅 대화 기능 15개

실험적10%

베타79%

베타79%

[제어 UI](</ko/web/control-ui>), [웹채팅](</ko/web/webchat>), [시작하기](</ko/start/getting-started>), [채널 라우팅](</ko/channels/channel-routing>), [안전한 파일 작업](</ko/gateway/security/secure-file-operations>)

운영자 콘솔 기능 10개

실험적8%

베타79%

베타79%

[제어 UI](</ko/web/control-ui>), [상태](</ko/gateway/health>), [프로토콜](</ko/gateway/protocol>), [대시보드](</ko/web/dashboard>)

Plugin - M3 베타 - 영역 9개

매니페스트, 검색, 로딩, 제공자/도구 아키텍처, 승인 경계 전반에 걸쳐 폭넓은 문서와 강력한 내부 런타임 증거가 있습니다. 공개 SDK API/하위 경로와 외부 배포 증거가 더 강해질 때까지 이 행은 베타로 유지하세요.

범위 실험적 - 12%품질 베타 - 72%완성도 베타 - 79%부분 - 7

Plugin 작성 및 패키징 8개 기능 / LTS 지원

실험적0%

알파68%

베타79%

[Plugin 빌드](</ko/plugins/building-plugins>), [SDK 개요](</ko/plugins/sdk-overview>), [SDK 진입점](</ko/plugins/sdk-entrypoints>), [SDK 하위 경로](</ko/plugins/sdk-subpaths>), [매니페스트](</ko/plugins/manifest>), [참조](</ko/plugins/reference>)

번들 Plugin 5개 기능 / LTS 지원

실험적0%

알파68%

베타79%

[Plugin 인벤토리](</ko/plugins/plugin-inventory>), [Plugin](</ko/cli/plugins>), [아키텍처 내부 구조](</ko/plugins/architecture-internals>)

Canvas Plugin 6개 기능

실험적0%

알파68%

베타79%

[Canvas](</ko/plugins/reference/canvas>), [Canvas](</ko/refactor/canvas>), [구성 참조](</ko/gateway/configuration-reference>)

Plugin 설치 및 실행 6개 기능 / LTS 지원

실험적35%

베타79%

베타79%

[아키텍처](</ko/plugins/architecture>), [아키텍처 내부 구조](</ko/plugins/architecture-internals>), [Plugin](</ko/cli/plugins>)

채널 Plugin 5개 기능 / LTS 지원

실험적0%

알파68%

베타79%

[SDK 채널 Plugin](</ko/plugins/sdk-channel-plugins>), [SDK 채널 인바운드](</ko/plugins/sdk-channel-inbound>), [SDK 채널 아웃바운드](</ko/plugins/sdk-channel-outbound>)

제공자 및 도구 Plugin 6개 기능 / LTS 지원

실험적43%

베타79%

베타79%

[SDK 제공자 Plugin](</ko/plugins/sdk-provider-plugins>), [도구 Plugin](</ko/plugins/tool-plugins>), [기능 추가](</ko/plugins/adding-capabilities>)

Plugin 승인 6개 기능 / LTS 지원

실험적0%

알파68%

베타79%

[Plugin 권한 요청](</ko/plugins/plugin-permission-requests>), [Exec 승인](</ko/tools/exec-approvals>), [SDK 채널 Plugin](</ko/plugins/sdk-channel-plugins>)

Plugin 게시 6개 기능 / LTS 지원

실험적0%

알파68%

베타79%

[Plugin](</ko/cli/plugins>), [호환성](</ko/plugins/compatibility>), [게시](</ko/clawhub/publishing>)

Plugin 테스트 6개 기능

실험적27%

베타79%

베타79%

[SDK 테스트](</ko/plugins/sdk-testing>), [SDK 설정](</ko/plugins/sdk-setup>), [Codex 하네스](</ko/plugins/codex-harness>)

보안, 인증, 페어링 및 비밀 - M3 베타 - 6개 영역

좋은 문서와 강화 표면이 마련되어 있습니다. 정기적인 업그레이드/보안 시나리오 실행에서 설정 회귀가 없음을 입증한 뒤 승격하세요.

범위 실험 단계 - 16%품질 베타 - 72%완성도 베타 - 79%부분 - 5

승인 정책 및 도구 보호 장치 2개 기능 / LTS 지원

알파50%

베타79%

베타79%

[Exec 승인](</ko/tools/exec-approvals>), [승인](</ko/cli/approvals>), [Plugin 권한 요청](</ko/plugins/plugin-permission-requests>), [감사 검사](</ko/gateway/security/audit-checks>)

Gateway 인증 및 원격 액세스 9개 기능 / LTS 지원

실험 단계0%

알파68%

베타79%

[색인](</ko/gateway/security>), [노출 런북](</ko/gateway/security/exposure-runbook>), [신뢰할 수 있는 프록시 인증](</ko/gateway/trusted-proxy-auth>), [Tailscale](</ko/gateway/tailscale>), [원격](</ko/gateway/remote>), [구성 참조](</ko/gateway/configuration-reference>), [Gateway](</ko/cli/gateway>), [Doctor](</ko/cli/doctor>), [컨트롤 UI](</ko/web/control-ui>), [브라우저 제어](</ko/tools/browser-control>), [감사 검사](</ko/gateway/security/audit-checks>)

채널 액세스 제어 3개 기능 / LTS 지원

실험 단계0%

알파68%

베타79%

[페어링](</ko/channels/pairing>), [Telegram](</ko/channels/telegram>), [액세스 그룹](</ko/channels/access-groups>), [감사 검사](</ko/gateway/security/audit-checks>)

디바이스 및 Node 페어링 11개 기능 / LTS 지원

실험 단계0%

알파68%

베타79%

[프로토콜](</ko/gateway/protocol>), [디바이스](</ko/cli/devices>), [페어링](</ko/channels/pairing>), [페어링](</ko/gateway/pairing>), [운영자 범위](</ko/gateway/operator-scopes>), [컨트롤 UI](</ko/web/control-ui>), [웹챗](</ko/web/webchat>), [승인](</ko/cli/approvals>)

Plugin 신뢰 2개 기능

실험 단계0%

알파68%

베타79%

[매니페스트](</ko/plugins/manifest>), [Plugin 권한 요청](</ko/plugins/plugin-permission-requests>), [Plugin 관리](</ko/plugins/manage-plugins>), [감사 검사](</ko/gateway/security/audit-checks>)

자격 증명 및 비밀 위생 5개 기능 / LTS 지원

실험 단계46%

베타79%

베타79%

[인증](</ko/gateway/authentication>), [모델](</ko/cli/models>), [Openai](</ko/providers/openai>), [OAuth](</ko/concepts/oauth>), [비밀](</ko/gateway/secrets>), [비밀](</ko/cli/secrets>), [Secretref 자격 증명 표면](</ko/reference/secretref-credential-surface>), [감사 검사](</ko/gateway/security/audit-checks>)

자동화: Cron, 훅, 작업, 폴링 - M3 베타 - 6개 영역

문서화되어 있고 사용할 수 있지만, 시나리오 증명은 무인 전달, 재시도, 실패 가시성을 다루어야 합니다.

범위 실험 단계 - 2%품질 베타 - 72%완성도 베타 - 79%없음

Cron 작업 15개 기능

실험적0%

베타79%

베타79%

[Cron 작업](</ko/automation/cron-jobs>), [Cron](</ko/cli/cron>), [프로토콜](</ko/gateway/protocol>), [작업](</ko/automation/tasks>), [Discord](</ko/channels/discord>)

이벤트 인그레스 15개 기능

실험적0%

알파68%

베타79%

[Telegram](</ko/channels/telegram>), [Zalo](</ko/channels/zalo>), [문제 해결](</ko/channels/troubleshooting>), [Bluebubbles에서 iMessage 사용](</ko/channels/imessage-from-bluebubbles>), [Gmail Pubsub 통합](</ko/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</ko/automation/cron-jobs>), [Webhooks](</ko/cli/webhooks>), [Webhooks](</ko/automation/cron-jobs#webhooks>), [Webhook](</ko/automation/cron-jobs>)

자동화 Hook 11개 기능

실험적0%

알파68%

베타79%

[Hook](</ko/automation/hooks>), [Hook](</ko/cli/hooks>), [Hook](</ko/plugins/hooks>), [Plugin 권한 요청](</ko/plugins/plugin-permission-requests>), [SDK 하위 경로](</ko/plugins/sdk-subpaths>)

백그라운드 작업 및 흐름 10개 기능

실험적0%

알파68%

베타79%

[작업](</ko/automation/tasks>), [색인](</ko/automation>), [작업](</ko/cli/tasks>), [TaskFlow](</ko/automation/taskflow>), [SDK 런타임](</ko/plugins/sdk-runtime>)

Heartbeat 5개 기능

실험적14%

베타79%

베타79%

[색인](</ko/automation>), [Heartbeat](</ko/gateway/heartbeat>), [커밋먼트](</ko/concepts/commitments>)

폴링 제어 10개 기능

실험적0%

알파68%

베타79%

[폴링](</ko/cli/message>), [메시지](</ko/cli/message>), [Telegram](</ko/channels/telegram>), [Microsoft Teams](</ko/channels/msteams>), [백그라운드 프로세스](</ko/gateway/background-process>)

미디어 이해 및 미디어 생성 - M2 알파 - 6개 영역

광범위한 기능 표면은 존재하지만, 제공자별 차이, 파일 제한, Node/앱 간 동등성 때문에 아직 안정적이지 않습니다.

적용 범위 실험적 - 2%품질 알파 - 64%완성도 알파 - 68%없음

미디어 수집 및 접근 8개 기능

실험적0%

알파61%

알파68%

[미디어 개요](</ko/tools/media-overview>), [미디어 이해](</ko/nodes/media-understanding>), [보안 파일 작업](</ko/gateway/security/secure-file-operations>), [PDF](</ko/tools/pdf>), [이미지 생성](</ko/tools/image-generation>), [QR](</ko/cli/qr>), [LINE](</ko/channels/line>), [WhatsApp](</ko/channels/whatsapp>)

채널 미디어 처리 5개 기능

실험적0%

알파61%

알파68%

[이미지](</ko/nodes/images>), [미디어 개요](</ko/tools/media-overview>), [Discord](</ko/channels/discord>)

미디어 구성 1개 기능

실험적0%

알파61%

알파68%

[미디어 개요](</ko/tools/media-overview>), [이미지 생성](</ko/tools/image-generation>), [매니페스트](</ko/plugins/manifest>), [Codex 하네스](</ko/plugins/codex-harness>)

텍스트 음성 변환 전달 2개 기능

실험적0%

알파61%

알파68%

[TTS](</ko/tools/tts>), [미디어 개요](</ko/tools/media-overview>), [Discord](</ko/channels/discord>)

미디어 이해 12개 기능

실험적7%

알파69%

알파69%

[오디오](</ko/nodes/audio>), [미디어 이해](</ko/nodes/media-understanding>), [미디어 개요](</ko/tools/media-overview>), [WhatsApp](</ko/channels/whatsapp>), [이미지](</ko/nodes/images>), [추론](</ko/cli/infer>), [PDF](</ko/tools/pdf>)

미디어 생성 17개 기능

실험적5%

알파69%

알파69%

[이미지 생성](</ko/tools/image-generation>), [미디어 개요](</ko/tools/media-overview>), [Skills](</ko/tools/skills>), [음악 생성](</ko/tools/music-generation>), [비디오 생성](</ko/tools/video-generation>)

Voice and realtime talk - M2 Alpha - 6 areas

Control UI, 앱, 공급자 전반에 여러 구현이 있습니다. 베타 전에 지연 시간, 실패 모드, 설정 스코어카드가 필요합니다.

적용 범위 실험적 - 0%품질 알파 - 61%완성도 알파 - 68%없음

Talk 제공자 기능 7개

실험적0%

알파61%

알파68%

[Openai](</ko/providers/openai>), [Google](</ko/providers/google>), [Sdk 제공자 Plugin](</ko/plugins/sdk-provider-plugins>), [Talk](</ko/nodes/talk>), [제어 UI](</ko/web/control-ui>)

실시간 Talk 세션 기능 11개

실험적0%

알파61%

알파68%

[Talk](</ko/nodes/talk>), [제어 UI](</ko/web/control-ui>)

음성 및 전사 기능 5개

실험적0%

알파61%

알파68%

[Talk](</ko/nodes/talk>), [Openai](</ko/providers/openai>), [Google](</ko/providers/google>)

네이티브 앱 Talk 기능 4개

실험적0%

알파61%

알파68%

[Talk](</ko/nodes/talk>), [Voicewake](</ko/platforms/mac/voicewake>)

음성 깨우기 및 라우팅 기능 4개

실험적0%

알파61%

알파68%

[Voicewake](</ko/nodes/voicewake>), [Voicewake](</ko/platforms/mac/voicewake>), [음성 오버레이](</ko/platforms/mac/voice-overlay>)

Talk 관측 가능성 기능 5개

실험적0%

알파61%

알파68%

[제어 UI](</ko/web/control-ui>), [음성 오버레이](</ko/platforms/mac/voice-overlay>), [Talk](</ko/nodes/talk>)

TUI - M2 알파 - 5개 영역

문서와 소스에는 있지만, 기본 사용자 워크플로로는 덜 눈에 띕니다. 명시적인 시나리오 정의가 필요합니다.

범위 실험적 - 0%품질 알파 - 59%완성도 알파 - 66%없음

런타임 모드 14개 기능

실험적0%

알파59%

알파66%

[TUI](</ko/cli/tui>), [TUI](</ko/web/tui>), [색인](</ko/cli>)

입력 및 명령 8개 기능

실험적0%

알파59%

알파66%

[TUI](</ko/web/tui>)

세션 관리 3개 기능

실험적0%

알파59%

알파66%

[TUI](</ko/web/tui>), [세션](</ko/cli/sessions>)

로컬 셸 실행 4개 기능

실험적0%

알파59%

알파66%

[TUI](</ko/web/tui>), [TUI](</ko/cli/tui>)

렌더링 및 출력 안전성 4개 기능

실험적0%

알파59%

알파66%

[TUI](</ko/web/tui>), [QR](</ko/cli/qr>), [로그](</ko/cli/logs>), [완성](</ko/cli/completion>)

ClawHub - M2 알파 - 4개 영역

공개 문서와 생태계 개념이 있습니다. 설치, 신뢰, 업데이트, 롤백, 호환성 스코어카드가 필요합니다.

적용 범위 실험적 - 0%품질 알파 - 58%완성도 알파 - 62%없음

게시 7개 기능

실험적0%

알파54%

알파55%

[게시](</ko/clawhub/publishing>), [Skills 만들기](</ko/tools/creating-skills>), [커뮤니티](</ko/plugins/community>)

카탈로그 검색 5개 기능

실험적0%

알파61%

알파68%

[Plugin](</ko/tools/plugin>), [Plugins](</ko/cli/plugins>), [Skills](</ko/cli/skills>), [Skills](</ko/tools/skills>), [커뮤니티](</ko/plugins/community>)

호환성 및 신뢰 12개 기능

실험적0%

알파55%

알파56%

[Plugin](</ko/tools/plugin>), [Plugins](</ko/cli/plugins>), [호환성](</ko/plugins/compatibility>), [Plugin 인벤토리](</ko/plugins/plugin-inventory>), [게시](</ko/clawhub/publishing>), [Skills](</ko/tools/skills>), [Skills 구성](</ko/tools/skills-config>)

Plugin 수명 주기 및 상태 26개 기능

실험적0%

알파61%

알파68%

[Plugin](</ko/tools/plugin>), [Plugins](</ko/cli/plugins>), [Skills](</ko/cli/skills>), [Skills](</ko/tools/skills>), [프로토콜](</ko/gateway/protocol>), [번들](</ko/plugins/bundles>), [의존성 해석](</ko/plugins/dependency-resolution>)

OpenClaw App SDK - M2 알파 - 6개 영역

OpenClaw App SDK는 Gateway 런타임 및 Plugin SDK와 분리된 별도의 외부 앱 계약입니다. 현재 점수는 공개 패키징, 자동 검색, 승인, 도우미, 호환성 측면에 공백이 있는 실제 `@openclaw/sdk` 경로를 보여줍니다.

적용 범위 실험적 - 3%품질 알파 - 54%완성도 알파 - 53%없음

클라이언트 API 4개 기능

실험적0%

알파51%

알파50%

[OpenClaw SDK](</ko/gateway/external-apps>), [OpenClaw SDK API 설계](</ko/gateway/external-apps>)

Gateway 액세스 5개 기능

실험적0%

알파53%

알파54%

[OpenClaw SDK](</ko/gateway/external-apps>), [OpenClaw SDK API 설계](</ko/gateway/external-apps>), [프로토콜](</ko/gateway/protocol>), [인덱스](</ko/gateway/security>)

Agent 대화 6개 기능

실험적0%

알파52%

알파52%

[OpenClaw SDK](</ko/gateway/external-apps>), [OpenClaw SDK API 설계](</ko/gateway/external-apps>), [프로토콜](</ko/gateway/protocol>)

이벤트 및 승인 5개 기능

실험적0%

알파52%

알파52%

[OpenClaw SDK](</ko/gateway/external-apps>), [OpenClaw SDK API 설계](</ko/gateway/external-apps>), [프로토콜](</ko/gateway/protocol>)

리소스 헬퍼 5개 기능

실험적17%

알파62%

알파53%

[OpenClaw SDK](</ko/gateway/external-apps>), [OpenClaw SDK API 설계](</ko/gateway/external-apps>)

호환성 5개 기능

실험적0%

알파54%

알파55%

[OpenClaw SDK API 설계](</ko/gateway/external-apps>), [Typebox](</ko/concepts/typebox>), [프로토콜](</ko/gateway/protocol>)

### 플랫폼

Linux Gateway 호스트 - M4 안정 - 5개 영역

Node 런타임을 권장하며, systemd 사용자 서비스가 문서화되어 있고 VPS/컨테이너 지침은 폭넓게 제공됩니다.

적용 범위 실험적 - 0%품질 베타 - 75%완성도 안정 - 89%부분 - 4

호스트 설정 및 업데이트 4개 기능 / LTS 지원

실험적0%

베타75%

안정89%

[색인](</ko/install>), [업데이트](</ko/install/updating>), [Linux](</ko/platforms/linux>), [색인](</ko/platforms>)

Gateway 런타임 및 서비스 제어 6개 기능 / LTS 지원

실험적0%

베타75%

안정89%

[색인](</ko/gateway>), [Gateway](</ko/cli/gateway>), [Linux](</ko/platforms/linux>), [VPS](</ko/vps>)

원격 액세스 및 보안 6개 기능 / LTS 지원

실험적0%

베타75%

안정89%

[원격](</ko/gateway/remote>), [Tailscale](</ko/gateway/tailscale>), [노출 런북](</ko/gateway/security/exposure-runbook>), [인증](</ko/gateway/authentication>), [비밀](</ko/gateway/secrets>)

진단 및 복구 4개 기능 / LTS 지원

실험적0%

베타75%

안정89%

[상태](</ko/cli/status>), [로그](</ko/cli/logs>), [Doctor](</ko/cli/doctor>), [진단](</ko/gateway/diagnostics>), [색인](</ko/gateway>)

배포 대상 3개 기능

실험적0%

베타75%

안정89%

[VPS](</ko/vps>), [Docker](</ko/install/docker>), [Hetzner](</ko/install/hetzner>), [Digitalocean](</ko/install/digitalocean>), [Kubernetes](</ko/install/kubernetes>), [Podman](</ko/install/podman>)

macOS Gateway 호스트 - M4 안정 - 7개 영역

LaunchAgent 서비스 경로, 로컬/원격 Gateway 모드, CLI 설치 및 앱 통합이 문서화되어 있습니다.

범위 실험적 - 0%품질 베타 - 74%완성도 안정 - 88%없음

CLI 설정 4개 기능

실험적0%

Beta74%

안정88%

[Macos](</ko/platforms/macos>), [번들 Gateway](</ko/platforms/mac/bundled-gateway>), [설치 관리자](</ko/install/installer>), [Node](</ko/install/node>)

로컬 Gateway 통합 9개 기능

실험적0%

Beta74%

안정88%

[Macos](</ko/platforms/macos>), [번들 Gateway](</ko/platforms/mac/bundled-gateway>), [원격](</ko/platforms/mac/remote>), [색인](</ko/gateway>), [Gateway](</ko/cli/gateway>), [Bonjour](</ko/gateway/bonjour>)

원격 Gateway 모드 5개 기능

실험적0%

Beta74%

안정88%

[원격](</ko/platforms/mac/remote>), [원격](</ko/gateway/remote>), [Tailscale](</ko/gateway/tailscale>)

Gateway 서비스 수명 주기 10개 기능

실험적0%

Beta74%

안정88%

[Macos](</ko/platforms/macos>), [번들 Gateway](</ko/platforms/mac/bundled-gateway>), [Gateway](</ko/cli/gateway>), [색인](</ko/gateway>), [업데이트](</ko/cli/update>), [업데이트하기](</ko/install/updating>), [제거](</ko/install/uninstall>), [문제 해결](</ko/gateway/troubleshooting>)

진단 및 관측 가능성 4개 기능

실험적0%

Beta74%

안정88%

[번들 Gateway](</ko/platforms/mac/bundled-gateway>), [Macos](</ko/platforms/macos>), [Gateway](</ko/cli/gateway>), [Doctor](</ko/gateway/doctor>), [문제 해결](</ko/gateway/troubleshooting>)

권한 및 네이티브 기능 4개 기능

실험적0%

Beta74%

안정88%

[Macos](</ko/platforms/macos>), [원격](</ko/platforms/mac/remote>)

프로필 및 격리 5개 기능

실험적0%

Beta74%

안정88%

[여러 Gateway](</ko/gateway/multiple-gateways>), [색인](</ko/gateway>), [Gateway](</ko/cli/gateway>)

Docker 및 Podman 호스팅 - M3 Beta - 4개 영역

설치 문서가 있으며 일반적인 배포 경로입니다. 반복 릴리스 스모크 테스트에서 업그레이드 및 볼륨 동작을 캡처한 후 승격하세요.

적용 범위 실험적 - 7%품질 Beta - 71%완성도 Beta - 79%없음

컨테이너 설정 6개 기능

실험적0%

알파68%

베타79%

[Docker](</ko/install/docker>), [Podman](</ko/install/podman>)

컨테이너 운영 11개 기능

실험적0%

알파68%

베타79%

[Podman](</ko/install/podman>), [Docker Vm Runtime](</ko/install/docker-vm-runtime>), [Docker](</ko/install/docker>), [Hetzner](</ko/install/hetzner>), [Hostinger](</ko/install/hostinger>)

이미지 릴리스 및 검증 5개 기능

실험적29%

베타79%

베타79%

[Docker](</ko/install/docker>), [Docker Vm Runtime](</ko/install/docker-vm-runtime>), [Full Release Validation](</ko/reference/full-release-validation>)

Agent 샌드박스 및 도구 3개 기능

실험적0%

알파68%

베타79%

[Docker](</ko/install/docker>), [Docker Vm Runtime](</ko/install/docker-vm-runtime>)

WSL2를 통한 Windows - M3 베타 - 6개 영역

systemd/사용자 서비스 지침과 부팅 체인 문서를 포함한 권장 Windows 경로입니다. 반복된 설치/업데이트 스코어카드 이후 승격하세요.

적용 범위 실험적 - 6%품질 알파 - 69%완성도 베타 - 79%부분적 - 5

WSL 설정 6개 기능 / LTS 지원

실험적0%

알파67%

베타79%

[Windows](</ko/platforms/windows>), [시작하기](</ko/start/getting-started>)

CLI 8개 기능 / LTS 지원

실험적0%

알파67%

베타79%

[Windows](</ko/platforms/windows>), [시작하기](</ko/start/getting-started>), [업데이트](</ko/install/updating>), [온보드](</ko/cli/onboard>), [Doctor](</ko/cli/doctor>), [상태](</ko/cli/status>), [로그](</ko/cli/logs>)

Gateway 서비스 수명 주기 10개 기능 / LTS 지원

실험적0%

알파67%

베타79%

[Windows](</ko/platforms/windows>), [색인](</ko/gateway>), [Doctor](</ko/gateway/doctor>)

Gateway 액세스 및 노출 11개 기능 / LTS 지원

실험적0%

알파67%

베타79%

[인증](</ko/gateway/authentication>), [비밀](</ko/gateway/secrets>), [원격](</ko/gateway/remote>), [노출 런북](</ko/gateway/security/exposure-runbook>), [Windows](</ko/platforms/windows>)

진단 및 복구 6개 기능 / LTS 지원

실험적38%

베타79%

베타79%

[Windows](</ko/platforms/windows>), [상태](</ko/cli/status>), [로그](</ko/cli/logs>), [Doctor](</ko/cli/doctor>), [Doctor](</ko/gateway/doctor>)

브라우저 및 Control UI 6개 기능

실험적0%

알파67%

베타79%

[브라우저 Wsl2 Windows 원격 Cdp 문제 해결](</ko/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [브라우저](</ko/tools/browser>), [Control UI](</ko/web/control-ui>)

Raspberry Pi 및 소형 Linux 장치 - M3 베타 - 4개 영역

플랫폼 문서가 있으며 Gateway 경로는 Linux 기반입니다. 더 높은 단계로 이동하려면 하드웨어별 릴리스 스모크 증명이 필요합니다.

적용 범위 실험적 - 0%품질 알파 - 67%완성도 베타 - 79%없음

설정 및 호환성 12개 기능

실험적0%

알파67%

베타79%

[Raspberry Pi](</ko/install/raspberry-pi>), [색인](</ko/install>), [첫 실행 FAQ](</ko/help/faq-first-run>), [FAQ](</ko/help/faq>), [Linux](</ko/platforms/linux>), [설치 프로그램](</ko/install/installer>)

원격 액세스 및 인증 9개 기능

실험적0%

알파67%

베타79%

[Raspberry Pi](</ko/install/raspberry-pi>), [인증](</ko/gateway/authentication>), [시크릿](</ko/gateway/secrets>), [페어링](</ko/gateway/pairing>), [기기](</ko/cli/devices>), [원격](</ko/gateway/remote>), [Tailscale](</ko/gateway/tailscale>)

Gateway 런타임 10개 기능

실험적0%

알파67%

베타79%

[색인](</ko/gateway>), [Gateway](</ko/cli/gateway>), [Raspberry Pi](</ko/install/raspberry-pi>), [Linux](</ko/platforms/linux>), [VPS](</ko/vps>)

성능 및 진단 5개 기능

실험적0%

알파67%

베타79%

[Raspberry Pi](</ko/install/raspberry-pi>), [Linux](</ko/platforms/linux>), [상태](</ko/gateway/health>), [진단](</ko/gateway/diagnostics>)

macOS 컴패니언 앱 - M3 베타 - 8개 영역

풍부한 메뉴 막대 앱, 권한, Node 모드, Canvas, 음성 깨우기, WebChat, 원격 모드가 있습니다. 아직 Stable로 지정하기에는 충분히 빠르게 변화하고 있습니다.

적용 범위 실험적 - 0%품질 알파 - 66%완성도 베타 - 78%없음

캔버스 기능 4개

실험적0%

알파66%

베타78%

[캔버스](</ko/platforms/mac/canvas>), [macOS](</ko/platforms/macos>), [웹챗](</ko/web/webchat>)

로컬 설정 기능 7개

실험적0%

알파66%

베타78%

[번들 Gateway](</ko/platforms/mac/bundled-gateway>), [macOS](</ko/platforms/macos>), [자식 프로세스](</ko/platforms/mac/child-process>), [개발 설정](</ko/platforms/mac/dev-setup>)

상태 및 설정 기능 5개

실험적0%

알파66%

베타78%

[메뉴 막대](</ko/platforms/mac/menu-bar>), [아이콘](</ko/platforms/mac/icon>), [macOS](</ko/platforms/macos>), [상태](</ko/platforms/mac/health>), [로깅](</ko/platforms/mac/logging>), [원격](</ko/platforms/mac/remote>)

네이티브 기능 기능 5개

실험적0%

알파66%

베타78%

[macOS](</ko/platforms/macos>), [XPC](</ko/platforms/mac/xpc>), [권한](</ko/platforms/mac/permissions>), [서명](</ko/platforms/mac/signing>), [Peekaboo](</ko/platforms/mac/peekaboo>)

원격 연결 기능 3개

실험적0%

알파66%

베타78%

[원격](</ko/platforms/mac/remote>), [macOS](</ko/platforms/macos>), [원격](</ko/gateway/remote>)

음성 및 대화 기능 3개

실험적0%

알파66%

베타78%

[음성 깨우기](</ko/platforms/mac/voicewake>), [음성 오버레이](</ko/platforms/mac/voice-overlay>), [대화](</ko/nodes/talk>), [macOS](</ko/platforms/macos>)

웹챗 기능 3개

실험적0%

알파66%

베타78%

[웹챗](</ko/platforms/mac/webchat>), [macOS](</ko/platforms/macos>), [웹챗](</ko/web/webchat>)

원격 웹챗 기능 5개

실험적0%

알파66%

베타78%

[웹챗](</ko/platforms/mac/webchat>), [원격](</ko/gateway/remote>), [원격](</ko/platforms/mac/remote>)

Android app - M2 Alpha - 7 areas

공개 Google Play 경로는 있지만, 앱 문서에서는 여전히 재빌드를 극히 초기 알파로 설명하고 릴리스 강화를 위한 작업을 명시합니다.

적용 범위 실험적 - 0%품질 알파 - 59%완성도 알파 - 66%없음

미디어 캡처 기능 1개

실험적0%

알파59%

알파66%

[Android](</ko/platforms/android>), [카메라](</ko/nodes/camera>)

모바일 채팅 기능 1개

실험적0%

알파59%

알파66%

[Android](</ko/platforms/android>)

연결 설정 기능 1개

실험적0%

알파59%

알파66%

[Android](</ko/platforms/android>), [Bonjour](</ko/gateway/bonjour>), [페어링](</ko/gateway/pairing>)

배포 기능 3개

실험적0%

알파59%

알파66%

[Android](</ko/platforms/android>)

설정 기능 1개

실험적0%

알파59%

알파66%

[Android](</ko/platforms/android>)

음성 기능 1개

실험적0%

알파59%

알파66%

[Android](</ko/platforms/android>), [Talk](</ko/nodes/talk>)

기기 런타임 기능 2개

실험적0%

알파59%

알파66%

[Android](</ko/platforms/android>), [문제 해결](</ko/nodes/troubleshooting>), [프로토콜](</ko/gateway/protocol>)

네이티브 Windows - M2 알파 - 영역 4개

핵심 CLI/Gateway 흐름은 작동하지만, 문서는 여전히 전체 경험을 위해 WSL2를 권장하고 네이티브 사용 시 주의 사항을 나열합니다.

범위 실험적 - 0%품질 알파 - 58%완성도 알파 - 66%부분적 - 1

CLI 기능 9개 / LTS 지원

실험적0%

알파54%

알파64%

[인덱스](</ko/install>), [설치 관리자](</ko/install/installer>), [Windows](</ko/platforms/windows>), [시작하기](</ko/start/getting-started>), [온보드](</ko/cli/onboard>)

Gateway 관리 기능 11개

실험적0%

알파59%

알파66%

[Windows](</ko/platforms/windows>), [인덱스](</ko/gateway>), [Gateway](</ko/cli/gateway>), [Doctor](</ko/cli/doctor>)

네트워킹 기능 4개

실험적0%

알파59%

알파66%

[Windows](</ko/platforms/windows>), [인덱스](</ko/gateway>), [Gateway](</ko/cli/gateway>)

업데이트 기능 4개

실험적0%

알파59%

알파66%

[업데이트](</ko/install/updating>), [Ci](</ko/ci>)

Kubernetes 호스팅 - M2 알파 - 영역 4개

Kubernetes 호스팅은 Kustomize 기반의 별도 클러스터 배포 경로입니다. 현재 점수는 실제 최소 배포 경로가 있음을 보여 주지만, Kubernetes 전용 CI, ingress/TLS/NetworkPolicy 패키징, 백업/복원, 프로덕션 노출 강화와 관련한 공백이 있습니다.

적용 범위 실험적 - 0%품질 알파 - 55%완성도 알파 - 61%없음

배포 설정 5개 기능

실험적0%

알파55%

알파61%

[Kubernetes](</ko/install/kubernetes>), [색인](</ko/install>)

구성 및 보안 비밀 5개 기능

실험적0%

알파55%

알파61%

[Kubernetes](</ko/install/kubernetes>), [보안 비밀](</ko/gateway/secrets>), [환경](</ko/help/environment>)

접근 및 노출 5개 기능

실험적0%

알파55%

알파61%

[Kubernetes](</ko/install/kubernetes>), [인증](</ko/gateway/authentication>), [원격](</ko/gateway/remote>), [노출 런북](</ko/gateway/security/exposure-runbook>)

클러스터 수명 주기 5개 기능

실험적0%

알파55%

알파61%

[Kubernetes](</ko/install/kubernetes>), [색인](</ko/gateway>)

iOS 앱 - M1 실험적 - 8개 영역

내부 프리뷰 / 슈퍼 알파. TestFlight와 릴레이 기반 푸시 플로가 있지만, 아직 공개 배포는 없습니다.

적용 범위 실험적 - 0%품질 실험적 - 41%완성도 실험적 - 44%없음

미디어 및 공유 기능 1개

실험적0%

실험적41%

실험적44%

[Ios](</ko/platforms/ios>), [카메라](</ko/nodes/camera>)

캔버스 및 화면 기능 1개

실험적0%

실험적41%

실험적44%

[Ios](</ko/platforms/ios>), [캔버스](</ko/plugins/reference/canvas>)

채팅 및 세션 기능 1개

실험적0%

실험적41%

실험적44%

[Ios](</ko/platforms/ios>), [웹 채팅](</ko/web/webchat>), [프로토콜](</ko/gateway/protocol>)

Gateway 설정 및 진단 기능 7개

실험적0%

실험적41%

실험적44%

[Ios](</ko/platforms/ios>), [페어링](</ko/channels/pairing>)

배포 기능 1개

실험적0%

실험적41%

실험적44%

[Ios](</ko/platforms/ios>)

기기 명령 기능 2개

실험적0%

실험적41%

실험적44%

[Ios](</ko/platforms/ios>), [프로토콜](</ko/gateway/protocol>)

알림 및 백그라운드 기능 1개

실험적0%

실험적41%

실험적44%

[Ios](</ko/platforms/ios>), [구성](</ko/gateway/configuration>)

음성 기능 1개

실험적0%

실험적41%

실험적44%

[Ios](</ko/platforms/ios>), [말하기](</ko/nodes/talk>)

Nix install path - M1 Experimental - 5 areas

선택적 설치 흐름입니다. 알파/베타 승격 전에 더 명확한 지원 약속이 필요합니다.

범위 실험적 - 0%품질 실험적 - 41%완성도 실험적 - 44%없음

설치 인계 기능 4개

실험적0%

실험적41%

실험적44%

[Nix](</ko/install/nix>), [색인](</ko/install>), [문서 디렉터리](</ko/start/docs-directory>)

Plugin 수명 주기 기능 4개

실험적0%

실험적41%

실험적44%

[Plugin 관리](</ko/plugins/manage-plugins>), [Plugin](</ko/tools/plugin>), [Nix](</ko/install/nix>)

활성화 및 앱 UX 기능 7개

실험적0%

실험적41%

실험적44%

[Nix](</ko/install/nix>)

구성 및 상태 기능 7개

실험적0%

실험적41%

실험적44%

[Nix](</ko/install/nix>), [설정](</ko/cli/setup>), [환경](</ko/help/environment>)

서비스 런타임 및 가드 기능 8개

실험적0%

실험적41%

실험적44%

[Nix](</ko/install/nix>), [설정](</ko/cli/setup>), [Doctor](</ko/cli/doctor>), [업데이트](</ko/cli/update>)

watchOS 컴패니언 표면 - M1 실험적 - 영역 5개

소스에는 Watch 앱/확장 표면이 있지만, 공개 문서에서는 아직 이를 사용자 기능으로 제시하지 않습니다.

범위 실험적 - 0%품질 실험적 - 41%완성도 실험적 - 44%없음

전달 및 복구 7개 기능

실험적0%

실험적41%

실험적44%

[iOS](</ko/platforms/ios>)

실행 승인 3개 기능

실험적0%

실험적41%

실험적44%

[실행 승인](</ko/tools/exec-approvals>), [iOS](</ko/platforms/ios>)

배포 및 지원 6개 기능

실험적0%

실험적41%

실험적44%

[iOS](</ko/platforms/ios>)

알림 및 답장 7개 기능

실험적0%

실험적41%

실험적44%

[iOS](</ko/platforms/ios>)

Watch 앱 UI 3개 기능

실험적0%

실험적41%

실험적44%

[iOS](</ko/platforms/ios>)

Linux companion 앱 - M0 계획됨 - 5개 영역

문서에 따르면 네이티브 Linux companion 앱은 계획되어 있으며, 현재 Linux에서 지원되는 경로는 Gateway입니다.

적용 범위 실험적 - 0%품질 실험적 - 19%완성도 실험적 - 21%없음

앱 배포 3개 기능

실험적0%

실험적19%

실험적21%

[Linux](</ko/platforms/linux>), [색인](</ko/platforms>), [색인](</ko/install>)

Gateway 연결 4개 기능

실험적0%

실험적19%

실험적21%

[Linux](</ko/platforms/linux>), [색인](</ko/gateway>), [페어링](</ko/gateway/pairing>), [원격](</ko/gateway/remote>)

채팅 및 세션 3개 기능

실험적0%

실험적19%

실험적21%

[Linux](</ko/platforms/linux>), [프로토콜](</ko/gateway/protocol>), [웹 채팅](</ko/web/webchat>)

데스크톱 기능 9개 기능

실험적0%

실험적19%

실험적21%

[Linux](</ko/platforms/linux>), [실행 승인](</ko/tools/exec-approvals>), [시크릿](</ko/gateway/secrets>), [색인](</ko/nodes>), [실행](</ko/tools/exec>), [대화](</ko/nodes/talk>), [카메라](</ko/nodes/camera>)

상태 및 진단 7개 기능

실험적0%

실험적19%

실험적21%

[Linux](</ko/platforms/linux>), [Openclaw](</ko/start/openclaw>), [Doctor](</ko/gateway/doctor>)

네이티브 Windows 동반 앱 - M0 계획됨 - 5개 영역

계획만 있음.

Coverage 실험적 - 0%품질 실험적 - 19%완성도 실험적 - 21%없음

설치 및 업데이트 기능 4개

실험적0%

실험적19%

실험적21%

[Windows](</ko/platforms/windows>), [색인](</ko/install>)

Gateway 연결 기능 3개

실험적0%

실험적19%

실험적21%

[Windows](</ko/platforms/windows>), [색인](</ko/gateway>), [페어링](</ko/gateway/pairing>), [원격](</ko/gateway/remote>)

채팅 세션 기능 2개

실험적0%

실험적19%

실험적21%

[Windows](</ko/platforms/windows>), [프로토콜](</ko/gateway/protocol>)

상태 및 복구 기능 5개

실험적0%

실험적19%

실험적21%

[Windows](</ko/platforms/windows>), [Doctor](</ko/gateway/doctor>), [색인](</ko/gateway>)

데스크톱 도구 및 권한 기능 10개

실험적0%

실험적19%

실험적21%

[Windows](</ko/platforms/windows>), [색인](</ko/nodes>), [Exec](</ko/tools/exec>), [Exec 승인](</ko/tools/exec-approvals>), [색인](</ko/gateway/security>)

### 채널

Discord - M4 안정 - 영역 6개

심층 문서와 폭넓은 기능 범위. 음성/위임 경로는 베타/알파로 별도 채점 상태를 유지해야 합니다.

범위 실험적 - 0%품질 베타 - 73%완성도 안정 - 87%부분 - 4

채널 설정 및 운영 10개 기능 / LTS 지원

실험적0%

베타73%

안정87%

[Discord](</ko/channels/discord>), [Discord](</ko/plugins/reference/discord>), [Fly](</ko/install/fly>), [슬래시 명령](</ko/tools/slash-commands>), [상태](</ko/gateway/health>), [채널](</ko/cli/channels>), [설정 채널](</ko/gateway/config-channels>)

액세스 및 ID 6개 기능 / LTS 지원

실험적0%

베타73%

안정87%

[Discord](</ko/channels/discord>), [페어링](</ko/channels/pairing>), [액세스 그룹](</ko/channels/access-groups>), [그룹](</ko/channels/groups>)

대화 라우팅 및 전달 12개 기능 / LTS 지원

실험적0%

베타73%

안정87%

[Discord](</ko/channels/discord>), [채널 라우팅](</ko/channels/channel-routing>), [그룹](</ko/channels/groups>), [액세스 그룹](</ko/channels/access-groups>), [ACP 에이전트](</ko/tools/acp-agents>), [하위 에이전트](</ko/tools/subagents>)

미디어 및 리치 콘텐츠 1개 기능 / LTS 지원

실험적0%

베타73%

안정87%

[Discord](</ko/channels/discord>)

네이티브 컨트롤 및 승인 5개 기능

실험적0%

베타73%

안정87%

[Discord](</ko/channels/discord>), [슬래시 명령](</ko/tools/slash-commands>)

실시간 음성 및 통화 5개 기능

실험적0%

베타73%

안정87%

[Discord](</ko/channels/discord>), [Openai](</ko/providers/openai>), [Elevenlabs](</ko/providers/elevenlabs>), [QA E2E 자동화](</ko/concepts/qa-e2e-automation>), [설정 채널](</ko/gateway/config-channels>)

Telegram - M3 베타 - 5개 영역

핵심 채널은 정기적으로 사용하기에 충분히 성숙했지만, 편차가 큰 UX와 미디어 엣지 케이스에는 반복적인 시나리오 검증이 필요합니다.

적용 범위 실험적 - 0%품질 알파 - 68%완성도 베타 - 78%전체 - 5

채널 설정 및 운영 기능 10개 / LTS 지원

실험적0%

알파66%

베타78%

[Telegram](</ko/channels/telegram>), [채널 구성](</ko/gateway/config-channels>), [채널](</ko/cli/channels>)

액세스 및 ID 기능 10개 / LTS 지원

실험적0%

알파66%

베타78%

[Telegram](</ko/channels/telegram>), [페어링](</ko/channels/pairing>), [액세스 그룹](</ko/channels/access-groups>), [그룹](</ko/channels/groups>), [멀티 에이전트](</ko/concepts/multi-agent>)

대화 라우팅 및 전달 기능 1개 / LTS 지원

실험적0%

알파66%

베타78%

[Telegram](</ko/channels/telegram>), [그룹](</ko/channels/groups>), [멀티 에이전트](</ko/concepts/multi-agent>)

미디어 및 리치 콘텐츠 기능 1개 / LTS 지원

실험적0%

알파66%

베타78%

[Telegram](</ko/channels/telegram>), [위치](</ko/channels/location>)

네이티브 제어 및 승인 기능 9개 / LTS 지원

실험적0%

베타77%

베타79%

[Telegram](</ko/channels/telegram>), [실행 승인](</ko/tools/exec-approvals>), [반응](</ko/tools/reactions>)

Slack - M3 베타 - 5개 영역

일급 채널 문서와 라우팅 표면입니다. 워크스페이스 설치/관리자 시나리오 스코어카드가 필요합니다.

커버리지 실험적 - 0%품질 알파 - 66%완성도 베타 - 78%완전 - 5

채널 설정 및 운영 기능 10개 / LTS 지원

실험적0%

알파66%

베타78%

[Slack](</ko/channels/slack>), [Slack](</ko/plugins/reference/slack>), [비밀](</ko/gateway/secrets>), [QA E2E 자동화](</ko/concepts/qa-e2e-automation>), [문제 해결](</ko/channels/troubleshooting>)

액세스 및 ID 기능 1개 / LTS 지원

실험적0%

알파66%

베타78%

[Slack](</ko/channels/slack>), [페어링](</ko/channels/pairing>)

대화 라우팅 및 전달 기능 5개 / LTS 지원

실험적0%

알파66%

베타78%

[Slack](</ko/channels/slack>), [봇 루프 보호](</ko/channels/bot-loop-protection>), [페어링](</ko/channels/pairing>)

미디어 및 리치 콘텐츠 기능 1개 / LTS 지원

실험적0%

알파66%

베타78%

[Slack](</ko/channels/slack>), [QA E2E 자동화](</ko/concepts/qa-e2e-automation>)

네이티브 컨트롤 및 승인 기능 8개 / LTS 지원

실험적0%

알파66%

베타78%

[Slack](</ko/channels/slack>), [슬래시 명령](</ko/tools/slash-commands>), [Exec 승인](</ko/tools/exec-approvals>)

iMessage 및 BlueBubbles - M3 베타 - 5개 영역

지원되는 iMessage는 로그인된 macOS Messages 호스트에서 imsg를 통해 실행됩니다. 기존 BlueBubbles 구성은 마이그레이션이 필요합니다. macOS 권한, SSH 래퍼, SIP/비공개 API, 마이그레이션 주의 사항을 계속 표시하세요.

범위 실험적 - 0%품질 알파 - 66%완성도 베타 - 78%없음

채널 설정 및 운영 11개 기능

실험적0%

알파66%

베타78%

[Bluebubbles iMessage](</ko/announcements/bluebubbles-imessage>), [Bluebubbles의 iMessage](</ko/channels/imessage-from-bluebubbles>), [채널 구성](</ko/gateway/config-channels>), [iMessage](</ko/channels/imessage>)

액세스 및 ID 6개 기능

실험적0%

알파66%

베타78%

[iMessage](</ko/channels/imessage>), [Bluebubbles의 iMessage](</ko/channels/imessage-from-bluebubbles>), [채널 구성](</ko/gateway/config-channels>)

대화 라우팅 및 전달 4개 기능

실험적0%

알파66%

베타78%

[iMessage](</ko/channels/imessage>)

미디어 및 리치 콘텐츠 7개 기능

실험적0%

알파66%

베타78%

[iMessage](</ko/channels/imessage>), [Bluebubbles의 iMessage](</ko/channels/imessage-from-bluebubbles>), [채널 구성](</ko/gateway/config-channels>)

네이티브 제어 및 승인 3개 기능

실험적0%

알파66%

베타78%

[iMessage](</ko/channels/imessage>)

WhatsApp - M3 베타 - 5개 영역

핵심 경로는 중요하며 문서화되어 있습니다. 업스트림 Baileys/세션 변동성 때문에 Stable보다 낮은 단계로 유지됩니다.

범위 실험적 - 0%품질 알파 - 66%완성도 베타 - 78%없음

채널 설정 및 운영 5개 기능

실험적0%

알파66%

베타78%

[WhatsApp](</ko/channels/whatsapp>), [채널 구성](</ko/gateway/config-channels>), [WhatsApp](</ko/plugins/reference/whatsapp>), [QA E2E 자동화](</ko/concepts/qa-e2e-automation>), [Doctor](</ko/gateway/doctor>)

액세스 및 ID 7개 기능

실험적0%

알파66%

베타78%

[WhatsApp](</ko/channels/whatsapp>), [채널 구성](</ko/gateway/config-channels>), [QA E2E 자동화](</ko/concepts/qa-e2e-automation>), [페어링](</ko/channels/pairing>)

대화 라우팅 및 전달 4개 기능

실험적0%

알파66%

베타78%

[WhatsApp](</ko/channels/whatsapp>), [그룹 메시지](</ko/channels/group-messages>)

미디어 및 리치 콘텐츠 2개 기능

실험적0%

알파66%

베타78%

[WhatsApp](</ko/channels/whatsapp>)

네이티브 컨트롤 및 승인 2개 기능

실험적0%

알파66%

베타78%

[WhatsApp](</ko/channels/whatsapp>)

Matrix - M2 알파 - 6개 영역

번들 Plugin을 통해 지원됩니다. 브리지, 인증, 룸 수명 주기 스코어카드가 필요합니다.

범위 실험적 - 0%품질 알파 - 60%완성도 알파 - 67%없음

채널 설정 및 운영 5개 기능

실험적0%

알파60%

알파67%

[Matrix](</ko/channels/matrix>), [Matrix 마이그레이션](</ko/channels/matrix-migration>)

접근 및 ID 7개 기능

실험적0%

알파60%

알파67%

[Matrix](</ko/channels/matrix>), [그룹](</ko/channels/groups>), [봇 루프 보호](</ko/channels/bot-loop-protection>)

대화 라우팅 및 전달 1개 기능

실험적0%

알파60%

알파67%

[Matrix](</ko/channels/matrix>)

미디어 및 리치 콘텐츠 1개 기능

실험적0%

알파60%

알파67%

[Matrix](</ko/channels/matrix>)

네이티브 제어 및 승인 6개 기능

실험적0%

알파60%

알파67%

[Matrix](</ko/channels/matrix>)

암호화 및 검증 3개 기능

실험적0%

알파60%

알파67%

[Matrix](</ko/channels/matrix>), [Matrix 마이그레이션](</ko/channels/matrix-migration>)

Google Chat - M2 알파 - 5개 영역

문서화된 채널이지만, 엔터프라이즈/관리자 설정으로 인해 성숙도 위험이 높아집니다.

적용 범위 실험적 - 0%품질 알파 - 59%완성도 알파 - 66%없음

채널 설정 및 운영 16개 기능

실험적0%

Alpha59%

Alpha66%

[Googlechat](</ko/channels/googlechat>), [Googlechat](</ko/plugins/reference/googlechat>), [채널 구성](</ko/gateway/config-channels>), [마법사 CLI 참조](</ko/start/wizard-cli-reference>), [비밀](</ko/gateway/secrets>), [Secretref 자격 증명 표면](</ko/reference/secretref-credential-surface>), [상태](</ko/gateway/health>), [Plugin 인벤토리](</ko/plugins/plugin-inventory>), [색인](</ko/channels>)

액세스 및 ID 11개 기능

실험적0%

Alpha59%

Alpha66%

[Googlechat](</ko/channels/googlechat>), [페어링](</ko/channels/pairing>), [액세스 그룹](</ko/channels/access-groups>), [채널 구성](</ko/gateway/config-channels>), [봇 루프 보호](</ko/channels/bot-loop-protection>), [채널 라우팅](</ko/channels/channel-routing>)

대화 라우팅 및 전달 1개 기능

실험적0%

Alpha59%

Alpha66%

[Googlechat](</ko/channels/googlechat>), [봇 루프 보호](</ko/channels/bot-loop-protection>), [액세스 그룹](</ko/channels/access-groups>), [채널 라우팅](</ko/channels/channel-routing>)

미디어 및 리치 콘텐츠 1개 기능

실험적0%

Alpha59%

Alpha66%

[Googlechat](</ko/channels/googlechat>), [메시지](</ko/cli/message>), [미디어 이해](</ko/nodes/media-understanding>), [Secretref 자격 증명 표면](</ko/reference/secretref-credential-surface>)

네이티브 컨트롤 및 승인 16개 기능

실험적0%

Alpha59%

Alpha66%

[Googlechat](</ko/channels/googlechat>), [메시지](</ko/cli/message>), [미디어 이해](</ko/nodes/media-understanding>), [Secretref 자격 증명 표면](</ko/reference/secretref-credential-surface>), [반응](</ko/tools/reactions>), [슬래시 명령](</ko/tools/slash-commands>), [에이전트 구성](</ko/gateway/config-agents>), [메시지 수명 주기 리팩터링](</ko/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5개 영역

엔터프라이즈 인증/관리자 흐름에는 명시적인 시나리오 증명이 필요합니다.

범위 실험적 - 0%품질 Alpha - 59%완성도 Alpha - 66%없음

채널 설정 및 운영 9개 기능

실험적0%

알파59%

알파66%

[Msteams](</ko/channels/msteams>), [Msteams](</ko/plugins/reference/msteams>), [채널 구성](</ko/gateway/config-channels>), [상태](</ko/gateway/health>)

액세스 및 ID 9개 기능

실험적0%

알파59%

알파66%

[Msteams](</ko/channels/msteams>), [페어링](</ko/channels/pairing>), [액세스 그룹](</ko/channels/access-groups>)

대화 라우팅 및 전달 5개 기능

실험적0%

알파59%

알파66%

[Msteams](</ko/channels/msteams>), [그룹](</ko/channels/groups>), [채널 라우팅](</ko/channels/channel-routing>)

미디어 및 리치 콘텐츠 5개 기능

실험적0%

알파59%

알파66%

[Msteams](</ko/channels/msteams>)

네이티브 제어 및 승인 5개 기능

실험적0%

알파59%

알파66%

[Msteams](</ko/channels/msteams>), [고급 Exec 승인](</ko/tools/exec-approvals-advanced>)

Signal - M2 알파 - 5개 영역

지원되는 채널 문서가 있지만, 설치 및 재연결 증거를 더 강화해야 합니다.

적용 범위 실험적 - 0%품질 알파 - 59%완성도 알파 - 66%없음

채널 설정 및 운영 7개 기능

실험 단계0%

알파59%

알파66%

[Signal](</ko/channels/signal>), [Signal](</ko/plugins/reference/signal>)

접근 및 ID 6개 기능

실험 단계0%

알파59%

알파66%

[Signal](</ko/channels/signal>)

대화 라우팅 및 전달 1개 기능

실험 단계0%

알파59%

알파66%

[Signal](</ko/channels/signal>)

미디어 및 리치 콘텐츠 7개 기능

실험 단계0%

알파59%

알파66%

[Signal](</ko/channels/signal>)

네이티브 제어 및 승인 3개 기능

실험 단계0%

알파59%

알파66%

[Signal](</ko/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, 지역 채널 - M2 알파 - 4개 영역

중요한 지역별 적용 범위이지만, 공개 지원 수준은 계정 유형, 업스트림 승인, 유지관리자 증거에 따라 조정해야 합니다.

적용 범위 실험 단계 - 0%품질 알파 - 55%완성도 알파 - 58%없음

채널 설정 및 운영 6개 기능

실험적0%

알파61%

알파68%

[색인](</ko/channels>), [Pairing](</ko/channels/pairing>), [Feishu](</ko/plugins/reference/feishu>), [아키텍처 내부 구조](</ko/plugins/architecture-internals>)

액세스 및 신원 1개 기능

실험적0%

알파53%

알파54%

연결된 문서 없음

대화 라우팅 및 전달 1개 기능

실험적0%

알파53%

알파54%

연결된 문서 없음

미디어 및 리치 콘텐츠 1개 기능

실험적0%

알파53%

알파54%

연결된 문서 없음

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 알파 - 4개 영역

지원되는 표면은 존재하지만, 성숙도는 업스트림 및 유지관리자 범위에 따라 달라질 수 있습니다. 나중에 개별적으로 점수를 매기세요.

범위 실험적 - 0%품질 알파 - 53%완성도 알파 - 54%없음

채널 설정 및 운영 기능 1개

실험적0%

알파53%

알파54%

연결된 문서 없음

액세스 및 ID 기능 1개

실험적0%

알파53%

알파54%

연결된 문서 없음

대화 라우팅 및 전달 기능 1개

실험적0%

알파53%

알파54%

연결된 문서 없음

미디어 및 리치 콘텐츠 기능 1개

실험적0%

알파53%

알파54%

연결된 문서 없음

음성 통화 채널 - M1 실험적 - 영역 5개

복잡한 실시간 동작을 포함하는 선택적/Plugin 경로입니다. 공개 베타 전에 시나리오 점수표가 필요합니다.

범위 실험적 - 0%품질 실험적 - 41%완성도 실험적 - 44%없음

채널 설정 및 운영 기능 2개

실험적0%

실험적41%

실험적44%

[음성 통화](</ko/cli/voicecall>), [음성 통화](</ko/plugins/voice-call>), [프로토콜](</ko/gateway/protocol>)

액세스 및 ID 기능 1개

실험적0%

실험적41%

실험적44%

[음성 통화](</ko/plugins/voice-call>), [음성 통화](</ko/cli/voicecall>)

대화 라우팅 및 전달 기능 1개

실험적0%

실험적41%

실험적44%

[음성 통화](</ko/plugins/voice-call>)

미디어 및 리치 콘텐츠 기능 2개

실험적0%

실험적41%

실험적44%

[음성 통화](</ko/plugins/voice-call>), [Plugin 인벤토리](</ko/plugins/plugin-inventory>)

실시간 음성 및 통화 기능 2개

실험적0%

실험적41%

실험적44%

[음성 통화](</ko/plugins/voice-call>)

### 제공자 및 도구

브라우저 자동화, exec 및 샌드박스 도구 - M3 베타 - 영역 3개

핵심 도구는 문서화되어 있지만, 호스트 보안과 권한 UX는 계속해서 활성 점수표 검토 대상이어야 합니다.

범위 실험적 - 21%품질 베타 - 75%완성도 베타 - 79%부분 - 2

브라우저 자동화 8개 기능

실험적13%

베타79%

베타79%

[브라우저 제어](</ko/tools/browser-control>), [테스트](</ko/help/testing>), [브라우저](</ko/tools/browser>), [색인](</ko/gateway/security>), [감사 검사](</ko/gateway/security/audit-checks>)

도구 호출 및 실행 6개 기능 / LTS 지원

알파50%

베타79%

베타79%

[Exec](</ko/tools/exec>), [백그라운드 프로세스](</ko/gateway/background-process>), [도구 호출 HTTP API](</ko/gateway/tools-invoke-http-api>), [운영자 범위](</ko/gateway/operator-scopes>), [프로토콜](</ko/gateway/protocol>), [Exec 승인](</ko/tools/exec-approvals>), [고급 Exec 승인](</ko/tools/exec-approvals-advanced>), [Elevated](</ko/tools/elevated>)

샌드박스 및 도구 정책 6개 기능 / LTS 지원

실험적0%

알파68%

베타79%

[샌드박싱](</ko/gateway/sandboxing>), [샌드박스 대 도구 정책 대 Elevated](</ko/gateway/sandbox-vs-tool-policy-vs-elevated>), [멀티 에이전트 샌드박스 도구](</ko/tools/multi-agent-sandbox-tools>), [Codex 하네스 참조](</ko/plugins/codex-harness-reference>), [구성 도구](</ko/gateway/config-tools>)

OpenAI 및 Codex 공급자 경로 - M3 베타 - 5개 영역

심층 문서, OAuth/구독 경로, 실시간 음성, 이미지, 호환성 동작입니다. 공급자 변동성 때문에 릴리스 스코어카드 증거 없이는 안정 단계로 전환되지 않습니다.

범위 실험적 - 26%품질 베타 - 74%완성도 베타 - 79%부분적 - 3

모델 및 인증 6개 기능 / LTS 지원

실험적44%

베타79%

베타79%

[Openai](</ko/providers/openai>), [Codex 하네스](</ko/plugins/codex-harness>), [모델](</ko/concepts/models>), [Oauth](</ko/concepts/oauth>), [Codex 하네스 참조](</ko/plugins/codex-harness-reference>), [인증 모니터링](</ko/gateway/authentication>)

응답 및 도구 호환성 4개 기능 / LTS 지원

실험적40%

베타79%

베타79%

[Openai](</ko/providers/openai>), [Openresponses HTTP API](</ko/gateway/openresponses-http-api>), [Openai HTTP API](</ko/gateway/openai-http-api>), [Codex 네이티브 Plugin](</ko/plugins/codex-native-plugins>)

네이티브 Codex 하네스 2개 기능 / LTS 지원

실험적44%

베타79%

베타79%

[Codex 하네스](</ko/plugins/codex-harness>), [Codex 하네스 런타임](</ko/plugins/codex-harness-runtime>), [Codex 하네스 참조](</ko/plugins/codex-harness-reference>), [Codex 네이티브 Plugin](</ko/plugins/codex-native-plugins>)

이미지 및 멀티모달 입력 2개 기능

실험적0%

알파67%

베타79%

[Openai](</ko/providers/openai>), [이미지 생성](</ko/tools/image-generation>), [이미지](</ko/nodes/images>)

음성 및 실시간 오디오 2개 기능

실험적0%

알파67%

베타79%

[Openai](</ko/providers/openai>), [Discord](</ko/channels/discord>), [음성 통화](</ko/plugins/voice-call>)

웹 검색 도구 - M3 베타 - 4개 영역

여러 제공자와 문서가 있습니다. 제공자 제품군별 할당량/오류/SSRF 증명이 필요합니다.

적용 범위 실험적 - 9%품질 베타 - 74%완성도 베타 - 79%없음

검색 제공자 19개 기능

실험적11%

Beta79%

Beta79%

[Web](</ko/tools/web>), [Brave Search](</ko/tools/brave-search>), [Tavily](</ko/tools/tavily>), [Exa Search](</ko/tools/exa-search>), [Firecrawl](</ko/tools/firecrawl>), [Perplexity Search](</ko/tools/perplexity-search>), [Duckduckgo Search](</ko/tools/duckduckgo-search>), [Searxng Search](</ko/tools/searxng-search>), [Gemini Search](</ko/tools/gemini-search>), [Grok Search](</ko/tools/grok-search>), [Kimi Search](</ko/tools/kimi-search>), [Minimax Search](</ko/tools/minimax-search>), [Ollama Search](</ko/tools/ollama-search>), [Sdk Subpaths](</ko/plugins/sdk-subpaths>), [Sdk Overview](</ko/plugins/sdk-overview>), [Manifest](</ko/plugins/manifest>)

설정 및 진단 9개 기능

실험적0%

Alpha68%

Beta79%

[Web](</ko/tools/web>), [Web Fetch](</ko/tools/web-fetch>), [Faq](</ko/help/faq>), [Api Usage Costs](</ko/reference/api-usage-costs>), [Brave Search](</ko/tools/brave-search>), [Perplexity Search](</ko/tools/perplexity-search>), [Tavily](</ko/tools/tavily>), [Firecrawl](</ko/tools/firecrawl>)

네트워크 안전 4개 기능

실험적0%

Alpha68%

Beta79%

[Web](</ko/tools/web>), [Web Fetch](</ko/tools/web-fetch>), [Firecrawl](</ko/tools/firecrawl>), [Searxng Search](</ko/tools/searxng-search>)

도구 가용성 및 가져오기 11개 기능

실험적25%

Beta79%

Beta79%

[Config Tools](</ko/gateway/config-tools>), [Web Fetch](</ko/tools/web-fetch>), [Web](</ko/tools/web>), [Faq](</ko/help/faq>)

Anthropic 제공자 경로 - M3 Beta - 5개 영역

일급 모델 제공자입니다. 반복적인 인증/카탈로그/도구 호출 시나리오 증명이 필요합니다.

적용 범위 실험적 - 0%품질 Beta - 71%완성도 Beta - 78%없음

제공자 인증 및 복구 9개 기능

실험적0%

알파66%

베타78%

[Anthropic](</ko/providers/anthropic>), [Doctor](</ko/gateway/doctor>), [구성 예시](</ko/gateway/configuration-examples>), [문제 해결](</ko/gateway/troubleshooting>), [프롬프트 캐싱](</ko/reference/prompt-caching>)

모델 및 런타임 선택 10개 기능

실험적0%

베타78%

베타79%

[Anthropic](</ko/providers/anthropic>), [에이전트 구성](</ko/gateway/config-agents>), [모델](</ko/concepts/models>), [CLI 백엔드](</ko/gateway/cli-backends>)

요청 전송 및 턴 의미 체계 10개 기능

실험적0%

베타77%

베타79%

[Anthropic](</ko/providers/anthropic>), [프롬프트 캐싱](</ko/reference/prompt-caching>), [문제 해결](</ko/gateway/troubleshooting>), [CLI 백엔드](</ko/gateway/cli-backends>), [모델 제공자](</ko/concepts/model-providers>)

프롬프트 캐시 및 컨텍스트 5개 기능

실험적0%

알파66%

베타78%

[Anthropic](</ko/providers/anthropic>), [프롬프트 캐싱](</ko/reference/prompt-caching>), [문제 해결](</ko/gateway/troubleshooting>), [Heartbeat](</ko/gateway/heartbeat>)

미디어 입력 4개 기능

실험적0%

알파66%

베타78%

[Anthropic](</ko/providers/anthropic>), [에이전트 구성](</ko/gateway/config-agents>)

Google 제공자 경로 - M3 베타 - 5개 영역

모델 및 실시간 표면을 갖춘 일급 제공자입니다. 별도의 Live/Talk 점수가 필요합니다.

범위 실험적 - 0%품질 알파 - 66%완성도 베타 - 78%없음

제공자 설정 및 자격 증명 기능 10개

실험적0%

알파66%

베타78%

[Google](</ko/providers/google>), [모델 제공자](</ko/concepts/model-providers>)

모델 라우팅 및 엔드포인트 기능 10개

실험적0%

알파66%

베타78%

[Google](</ko/providers/google>), [모델 제공자](</ko/concepts/model-providers>), [Google](</ko/plugins/reference/google>), [Gemini 검색](</ko/tools/gemini-search>)

직접 Gemini 런타임 기능 9개

실험적0%

알파66%

베타78%

[Google](</ko/providers/google>), [모델 제공자](</ko/concepts/model-providers>), [FAQ 모델](</ko/help/faq-models>), [라이브 테스트](</ko/help/testing-live>)

미디어, 검색 및 실시간 기능 10개

실험적0%

알파66%

베타78%

[Google](</ko/plugins/reference/google>), [Google](</ko/providers/google>)

프롬프트 캐싱 기능 5개

실험적0%

알파66%

베타78%

[프롬프트 캐싱](</ko/reference/prompt-caching>), [Google](</ko/providers/google>), [모델 제공자](</ko/concepts/model-providers>), [토큰 사용](</ko/reference/token-use>)

OpenRouter 제공자 경로 - M3 베타 - 4개 영역

통합 제공자 경로는 문서화되어 있고 유용하지만, 모델별 동작은 다릅니다.

적용 범위 실험적 - 0%품질 알파 - 66%완성도 베타 - 78%없음

제공자 설정 및 인증 14개 기능

실험적0%

알파66%

베타78%

[Openrouter](</ko/providers/openrouter>), [모델 제공자](</ko/concepts/model-providers>), [구성](</ko/cli/configure>), [인증](</ko/gateway/authentication>), [환경](</ko/help/environment>), [모델](</ko/cli/models>), [모델](</ko/concepts/models>)

채팅 런타임 및 정규화 15개 기능

실험적0%

알파66%

베타78%

[Openrouter](</ko/providers/openrouter>), [모델 제공자](</ko/concepts/model-providers>), [프롬프트 캐싱](</ko/reference/prompt-caching>)

제공자 복구 및 진단 5개 기능

실험적0%

알파66%

베타78%

[모델 장애 조치](</ko/concepts/model-failover>), [Openrouter](</ko/providers/openrouter>), [모델](</ko/cli/models>)

미디어 생성 및 음성 7개 기능

실험적0%

알파66%

베타78%

[Openrouter](</ko/providers/openrouter>), [이미지 생성](</ko/tools/image-generation>), [음악 생성](</ko/tools/music-generation>), [미디어 개요](</ko/tools/media-overview>), [동영상 생성](</ko/tools/video-generation>), [Tts](</ko/tools/tts>)

이미지, 동영상, 음악 생성 도구 - M2 알파 - 5개 영역

기능은 여러 제공자에서 사용할 수 있지만, 제공자별 증명 없이는 품질, 지연 시간, 매개변수 호환성이 베타로 보기에는 너무 크게 다릅니다.

적용 범위 실험적 - 0%품질 알파 - 61%완성도 알파 - 68%없음

미디어 라우팅 및 검색 4개 기능

실험적0%

알파61%

알파68%

[구성 에이전트](</ko/gateway/config-agents>), [이미지 생성](</ko/tools/image-generation>), [동영상 생성](</ko/tools/video-generation>), [음악 생성](</ko/tools/music-generation>)

작업 수명 주기 및 전달 12개 기능

실험적0%

알파61%

알파68%

[미디어 개요](</ko/tools/media-overview>), [이미지 생성](</ko/tools/image-generation>), [동영상 생성](</ko/tools/video-generation>), [음악 생성](</ko/tools/music-generation>)

이미지 생성 9개 기능

실험적0%

알파61%

알파68%

[이미지 생성](</ko/tools/image-generation>), [Infer](</ko/cli/infer>), [미디어 개요](</ko/tools/media-overview>)

동영상 생성 11개 기능

실험적0%

알파61%

알파68%

[동영상 생성](</ko/tools/video-generation>), [Runway](</ko/providers/runway>), [Pixverse](</ko/providers/pixverse>), [Fal](</ko/providers/fal>), [Openrouter](</ko/providers/openrouter>)

음악 생성 6개 기능

실험적0%

알파61%

알파68%

[음악 생성](</ko/tools/music-generation>)

로컬 모델 제공자: Ollama, vLLM, SGLang, LM Studio - M2 알파 - 5개 영역

유용하고 문서화되어 있지만, 환경별 차이가 큽니다.

적용 범위 실험적 - 0%품질 알파 - 61%완성도 알파 - 68%없음

Provider 설정, 수명 주기 및 진단 12개 기능

실험적0%

알파61%

알파68%

[로컬 모델](</ko/gateway/local-models>), [Lmstudio](</ko/providers/lmstudio>), [Ollama](</ko/providers/ollama>), [Vllm](</ko/providers/vllm>), [로컬 모델 서비스](</ko/gateway/local-model-services>), [Config 에이전트](</ko/gateway/config-agents>), [문제 해결](</ko/gateway/troubleshooting>), [Doctor](</ko/gateway/doctor>)

네이티브 Provider Plugin 10개 기능

실험적0%

알파61%

알파68%

[Ollama](</ko/providers/ollama>), [Lmstudio](</ko/providers/lmstudio>)

OpenAI 호환 런타임 호환성 8개 기능

실험적0%

알파61%

알파68%

[Vllm](</ko/providers/vllm>), [Sglang](</ko/providers/sglang>), [로컬 모델](</ko/gateway/local-models>), [Lmstudio](</ko/providers/lmstudio>)

로컬 메모리 및 임베딩 5개 기능

실험적0%

알파61%

알파68%

[메모리](</ko/concepts/memory>), [Doctor](</ko/gateway/doctor>)

네트워크 안전 및 프롬프트 제어 2개 기능

실험적0%

알파61%

알파68%

[색인](</ko/gateway/security>), [Config 도구](</ko/gateway/config-tools>), [로컬 모델](</ko/gateway/local-models>)

롱테일 호스팅 Provider - M2 알파 - 3개 영역

많은 문서/참조 페이지가 존재합니다. 점수는 Provider 메타데이터와 라이브 스모크 적용 범위를 함께 사용해 생성해야 합니다.

커버리지 실험적 - 0%품질 알파 - 61%완성도 알파 - 68%없음

호스팅 LLM 제공자 12개 기능

실험적0%

알파61%

알파68%

[색인](</ko/providers>), [모델 제공자](</ko/concepts/model-providers>), [라이브 테스트](</ko/help/testing-live>), [온보딩](</ko/cli/onboard>)

호스팅 미디어 제공자 8개 기능

실험적0%

알파61%

알파68%

[매니페스트](</ko/plugins/manifest>), [라이브 테스트](</ko/help/testing-live>), [색인](</ko/providers>)

제공자 운영 12개 기능

실험적0%

알파61%

알파68%

[색인](</ko/providers>), [모델 제공자](</ko/concepts/model-providers>), [매니페스트](</ko/plugins/manifest>), [라이브 테스트](</ko/help/testing-live>), [모델](</ko/cli/models>)

Was this useful?YesNo

Open issue