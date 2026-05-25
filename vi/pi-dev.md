---
title: Quy trình phát triển Pi
source_url: https://docs.openclaw.ai/vi/pi-dev
scraped_at: 2026-05-25
---

Quy trình hợp lý để làm việc trên tích hợp Pi trong OpenClaw.

## Kiểm tra kiểu và lint

  * Cổng kiểm cục bộ mặc định: `pnpm check`
  * Cổng kiểm build: `pnpm build` khi thay đổi có thể ảnh hưởng đến đầu ra build, đóng gói, hoặc ranh giới tải lười/module
  * Cổng kiểm đầy đủ trước khi hợp nhất cho các thay đổi trọng tâm Pi: `pnpm check && pnpm test`


## Chạy kiểm thử Pi

Chạy trực tiếp bộ kiểm thử tập trung vào Pi bằng Vitest:

bashCopy code
[code]
    pnpm test \  "src/agents/pi-*.test.ts" \  "src/agents/pi-embedded-*.test.ts" \  "src/agents/pi-tools*.test.ts" \  "src/agents/pi-settings.test.ts" \  "src/agents/pi-tool-definition-adapter*.test.ts" \  "src/agents/pi-hooks/**/*.test.ts"
[/code]

Để bao gồm bài chạy thử nhà cung cấp trực tiếp:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/pi-embedded-runner-extraparams.live.test.ts
[/code]

Phần này bao phủ các bộ kiểm thử đơn vị Pi chính:

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-tool-definition-adapter.test.ts`
  * `src/agents/pi-hooks/*.test.ts`


## Kiểm thử thủ công

Luồng được khuyến nghị:

  * Chạy Gateway ở chế độ phát triển: 
    * `pnpm gateway:dev`
  * Kích hoạt trực tiếp tác tử: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Dùng TUI để gỡ lỗi tương tác: 
    * `pnpm tui`


Đối với hành vi gọi công cụ, hãy nhắc một hành động `read` hoặc `exec` để bạn có thể thấy quá trình truyền phát công cụ và xử lý payload.

## Đặt lại từ trạng thái sạch

Trạng thái nằm trong thư mục trạng thái OpenClaw. Mặc định là `~/.openclaw`. Nếu `OPENCLAW_STATE_DIR` được đặt, hãy dùng thư mục đó thay thế.

Để đặt lại mọi thứ:

  * `openclaw.json` cho cấu hình
  * `agents/<agentId>/agent/auth-profiles.json` cho hồ sơ xác thực mô hình (khóa API + OAuth)
  * `credentials/` cho trạng thái nhà cung cấp/kênh vẫn nằm ngoài kho hồ sơ xác thực
  * `agents/<agentId>/sessions/` cho lịch sử phiên tác tử
  * `agents/<agentId>/sessions/sessions.json` cho chỉ mục phiên
  * `sessions/` nếu các đường dẫn cũ tồn tại
  * `workspace/` nếu bạn muốn một workspace trống


Nếu bạn chỉ muốn đặt lại phiên, hãy xóa `agents/<agentId>/sessions/` cho tác tử đó. Nếu bạn muốn giữ xác thực, hãy giữ nguyên `agents/<agentId>/agent/auth-profiles.json` và mọi trạng thái nhà cung cấp trong `credentials/`.

## Tham khảo

  * [Kiểm thử](</vi/help/testing>)
  * [Bắt đầu](</vi/start/getting-started>)


## Liên quan

  * [Kiến trúc tích hợp Pi](</vi/pi>)


Was this useful?YesNo