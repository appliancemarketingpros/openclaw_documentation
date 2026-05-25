---
title: 디바이스 모델 데이터베이스
source_url: https://docs.openclaw.ai/ko/reference/device-models
scraped_at: 2026-05-25
---

macOS companion 앱은 Apple 모델 식별자(예: `iPad16,6`, `Mac16,6`)를 사람이 읽기 쉬운 이름으로 매핑하여 **Instances** UI에서 친숙한 Apple 디바이스 모델 이름을 표시합니다.

이 매핑은 다음 위치에 JSON으로 vendor 처리됩니다:

  * `apps/macos/Sources/OpenClaw/Resources/DeviceModels/`


## 데이터 소스

현재 우리는 MIT 라이선스 저장소에서 이 매핑을 vendor 처리합니다:

  * `kyle-seongwoo-jun/apple-device-identifiers`


빌드를 결정적으로 유지하기 위해 JSON 파일은 특정 업스트림 커밋에 고정되어 있습니다(`apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`에 기록됨).

## 데이터베이스 업데이트

  1. 고정할 업스트림 커밋을 선택합니다(iOS용 하나, macOS용 하나).
  2. `apps/macos/Sources/OpenClaw/Resources/DeviceModels/NOTICE.md`의 커밋 해시를 업데이트합니다.
  3. 해당 커밋에 고정된 JSON 파일을 다시 다운로드합니다:

bashCopy code
[code]
    IOS_COMMIT="<ios-device-identifiers.json용 commit sha>"MAC_COMMIT="<mac-device-identifiers.json용 commit sha>" curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${IOS_COMMIT}/ios-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/ios-device-identifiers.json curl -fsSL "https://raw.githubusercontent.com/kyle-seongwoo-jun/apple-device-identifiers/${MAC_COMMIT}/mac-device-identifiers.json" \  -o apps/macos/Sources/OpenClaw/Resources/DeviceModels/mac-device-identifiers.json
[/code]

  4. `apps/macos/Sources/OpenClaw/Resources/DeviceModels/LICENSE.apple-device-identifiers.txt`가 여전히 업스트림과 일치하는지 확인합니다(업스트림 라이선스가 변경되었으면 교체하세요).
  5. macOS 앱이 경고 없이 정상적으로 빌드되는지 검증합니다:

bashCopy code
[code]
    swift build --package-path apps/macos
[/code]

## 관련 항목

  * [Nodes](</ko/nodes>)
  * [Node troubleshooting](</ko/nodes/troubleshooting>)


Was this useful?YesNo