---
title: Ghi đè cài đặt Plugin
source_url: https://docs.openclaw.ai/vi/plugins/install-overrides
scraped_at: 2026-05-25
---

Ghi đè cài đặt Plugin cho phép maintainer kiểm thử việc cài đặt Plugin trong lúc thiết lập bằng một gói npm cụ thể hoặc tarball npm-pack cục bộ. Chúng chỉ dành cho kiểm định E2E và gói. Người dùng thông thường nên cài đặt Plugin bằng [`openclaw plugins install`](</vi/cli/plugins>).

## Môi trường

Ghi đè bị tắt trừ khi cả hai biến đều được đặt:

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

Ánh xạ ghi đè là JSON được khóa theo id Plugin. Giá trị hỗ trợ:

  * `npm:<registry-spec>` cho các gói registry và phiên bản hoặc thẻ chính xác
  * `npm-pack:<path.tgz>` cho tarball cục bộ được tạo bởi `npm pack`


Đường dẫn `npm-pack:` tương đối được phân giải từ thư mục làm việc hiện tại.

## Hành vi

Khi một luồng trong lúc thiết lập yêu cầu cài đặt một Plugin có id xuất hiện trong ánh xạ, OpenClaw sử dụng nguồn ghi đè thay vì nguồn npm từ catalog, đi kèm hoặc mặc định. Điều này áp dụng cho onboarding và các luồng khác dùng bộ cài đặt Plugin dùng chung trong lúc thiết lập.

Ghi đè vẫn thực thi id Plugin dự kiến. Một tarball được ánh xạ tới `codex` phải cài đặt một Plugin có id manifest là `codex`.

Ghi đè không kế thừa trạng thái nguồn tin cậy chính thức. Ngay cả khi mục catalog thường đại diện cho một gói do OpenClaw sở hữu, ghi đè vẫn được xem là đầu vào kiểm thử do operator cung cấp.

Các tệp `.env` của workspace không thể bật ghi đè cài đặt. Hãy đặt các biến này trong shell tin cậy, job CI hoặc lệnh kiểm thử từ xa khởi chạy OpenClaw.

## E2E gói

Sử dụng một thư mục trạng thái cô lập để các lượt cài đặt gói và bản ghi cài đặt không chạm tới trạng thái OpenClaw thông thường của bạn:

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

Xác minh gói đã cài đặt trong thư mục trạng thái:

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/node_modules" -maxdepth 3 -name package.json -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/package-lock.json"
[/code]

Đối với E2E provider trực tiếp, lấy khóa API thật từ shell tin cậy hoặc secret CI trước khi khởi chạy lệnh kiểm thử. Không in khóa; chỉ báo cáo nguồn và liệu khóa có hiện diện hay không.

Was this useful?YesNo