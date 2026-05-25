---
title: Trình duyệt
source_url: https://docs.openclaw.ai/vi/cli/browser
scraped_at: 2026-05-25
---

# `openclaw browser`

Quản lý giao diện điều khiển trình duyệt của OpenClaw và chạy các thao tác trình duyệt (vòng đời, hồ sơ, tab, bản chụp, ảnh chụp màn hình, điều hướng, nhập liệu, mô phỏng trạng thái và gỡ lỗi).

Liên quan:

  * Công cụ trình duyệt + API: [Công cụ trình duyệt](</vi/tools/browser>)


## Cờ phổ biến

  * `--url <gatewayWsUrl>`: URL WebSocket của Gateway (mặc định theo cấu hình).
  * `--token <token>`: token Gateway (nếu bắt buộc).
  * `--timeout <ms>`: thời gian chờ yêu cầu (ms).
  * `--expect-final`: chờ phản hồi Gateway cuối cùng.
  * `--browser-profile <name>`: chọn một hồ sơ trình duyệt (mặc định từ cấu hình).
  * `--json`: đầu ra máy đọc được (khi được hỗ trợ).


## Bắt đầu nhanh (cục bộ)

bashCopy code
[code]
    openclaw browser profilesopenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw open https://example.comopenclaw browser --browser-profile openclaw snapshot
[/code]

Agent có thể chạy cùng kiểm tra sẵn sàng bằng `browser({ action: "doctor" })`.

## Khắc phục sự cố nhanh

Nếu `start` thất bại với `not reachable after start`, hãy khắc phục trạng thái sẵn sàng CDP trước. Nếu `start` và `tabs` thành công nhưng `open` hoặc `navigate` thất bại, mặt phẳng điều khiển trình duyệt đang hoạt động bình thường và lỗi thường là do chính sách SSRF điều hướng.

Chuỗi tối thiểu:

bashCopy code
[code]
    openclaw browser --browser-profile openclaw doctoropenclaw browser --browser-profile openclaw startopenclaw browser --browser-profile openclaw tabsopenclaw browser --browser-profile openclaw open https://example.com
[/code]

Hướng dẫn chi tiết: [Khắc phục sự cố trình duyệt](</vi/tools/browser#cdp-startup-failure-vs-navigation-ssrf-block>)

## Vòng đời

bashCopy code
[code]
    openclaw browser statusopenclaw browser doctoropenclaw browser doctor --deepopenclaw browser startopenclaw browser start --headlessopenclaw browser stopopenclaw browser --browser-profile openclaw reset-profile
[/code]

Ghi chú:

  * `doctor --deep` thêm một phép thăm dò bản chụp trực tiếp. Điều này hữu ích khi trạng thái sẵn sàng CDP cơ bản đã xanh nhưng bạn muốn bằng chứng rằng tab hiện tại có thể được kiểm tra.
  * Với hồ sơ `attachOnly` và CDP từ xa, `openclaw browser stop` đóng phiên điều khiển đang hoạt động và xóa các ghi đè mô phỏng tạm thời ngay cả khi OpenClaw không tự khởi chạy tiến trình trình duyệt.
  * Với hồ sơ cục bộ do hệ thống quản lý, `openclaw browser stop` dừng tiến trình trình duyệt đã được sinh ra.
  * `openclaw browser start --headless` chỉ áp dụng cho yêu cầu khởi động đó và chỉ khi OpenClaw khởi chạy một trình duyệt cục bộ do hệ thống quản lý. Nó không ghi lại `browser.headless` hoặc cấu hình hồ sơ, và không có tác dụng với trình duyệt đã đang chạy.
  * Trên máy chủ Linux không có `DISPLAY` hoặc `WAYLAND_DISPLAY`, hồ sơ cục bộ do hệ thống quản lý tự động chạy headless trừ khi `OPENCLAW_BROWSER_HEADLESS=0`, `browser.headless=false`, hoặc `browser.profiles.<name>.headless=false` yêu cầu rõ ràng một trình duyệt hiển thị được.


## Nếu thiếu lệnh

Nếu `openclaw browser` là lệnh không xác định, hãy kiểm tra `plugins.allow` trong `~/.openclaw/openclaw.json`.

Khi có `plugins.allow`, hãy liệt kê rõ ràng Plugin trình duyệt đi kèm, trừ khi cấu hình đã có khối `browser` ở gốc:

json5Copy code
[code]
    {  plugins: {    allow: ["telegram", "browser"],  },}
[/code]

Một khối `browser` rõ ràng ở gốc, ví dụ `browser.enabled=true` hoặc `browser.profiles.<name>`, cũng kích hoạt Plugin trình duyệt đi kèm trong một danh sách cho phép Plugin hạn chế.

Liên quan: [Công cụ trình duyệt](</vi/tools/browser#missing-browser-command-or-tool>)

## Hồ sơ

Hồ sơ là các cấu hình định tuyến trình duyệt có tên. Trong thực tế:

  * `openclaw`: khởi chạy hoặc gắn vào một phiên Chrome chuyên dụng do OpenClaw quản lý (thư mục dữ liệu người dùng tách biệt).
  * `user`: điều khiển phiên Chrome hiện có đã đăng nhập của bạn thông qua Chrome DevTools MCP.
  * hồ sơ CDP tùy chỉnh: trỏ tới một điểm cuối CDP cục bộ hoặc từ xa.

bashCopy code
[code]
    openclaw browser profilesopenclaw browser create-profile --name work --color "#FF5A36"openclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name remote --cdp-url https://browser-host.example.comopenclaw browser delete-profile --name work
[/code]

Dùng một hồ sơ cụ thể:

bashCopy code
[code]
    openclaw browser --browser-profile work tabs
[/code]

## Tab

bashCopy code
[code]
    openclaw browser tabsopenclaw browser tab new --label docsopenclaw browser tab label t1 docsopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://docs.openclaw.ai --label docsopenclaw browser focus docsopenclaw browser close t1
[/code]

`tabs` trả về `suggestedTargetId` trước, rồi đến `tabId` ổn định như `t1`, nhãn tùy chọn, và `targetId` thô. Agent nên truyền `suggestedTargetId` trở lại vào `focus`, `close`, bản chụp và thao tác. Bạn có thể gán nhãn bằng `open --label`, `tab new --label`, hoặc `tab label`; nhãn, id tab, id đích thô và tiền tố id đích duy nhất đều được chấp nhận. Khi Chromium thay thế đích thô bên dưới trong lúc điều hướng hoặc gửi biểu mẫu, OpenClaw giữ `tabId`/nhãn ổn định gắn với tab thay thế khi có thể chứng minh khớp. Id đích thô vẫn không ổn định; ưu tiên `suggestedTargetId`.

## Bản chụp / ảnh chụp màn hình / thao tác

Bản chụp:

bashCopy code
[code]
    openclaw browser snapshotopenclaw browser snapshot --urls
[/code]

Ảnh chụp màn hình:

bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref e12openclaw browser screenshot --labels
[/code]

Ghi chú:

  * `--full-page` chỉ dành cho chụp trang; không thể kết hợp với `--ref` hoặc `--element`.
  * Hồ sơ `existing-session` / `user` hỗ trợ ảnh chụp màn hình trang và ảnh chụp màn hình `--ref` từ đầu ra bản chụp, nhưng không hỗ trợ ảnh chụp màn hình CSS `--element`.
  * `--labels` phủ các ref bản chụp hiện tại lên ảnh chụp màn hình.
  * `snapshot --urls` thêm các đích liên kết đã phát hiện vào bản chụp AI để agent có thể chọn đích điều hướng trực tiếp thay vì chỉ đoán từ văn bản liên kết.


Điều hướng/nhấp/gõ (tự động hóa UI dựa trên ref):

bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser click <ref>openclaw browser click-coords 120 340openclaw browser type <ref> "hello"openclaw browser press Enteropenclaw browser hover <ref>openclaw browser scrollintoview <ref>openclaw browser drag <startRef> <endRef>openclaw browser select <ref> OptionA OptionBopenclaw browser fill --fields '[{"ref":"1","value":"Ada"}]'openclaw browser wait --text "Done"openclaw browser evaluate --fn '(el) => el.textContent' --ref <ref>
[/code]

Phản hồi thao tác trả về `targetId` thô hiện tại sau khi trang bị thay thế do thao tác kích hoạt, khi OpenClaw có thể chứng minh tab thay thế. Script vẫn nên lưu và truyền `suggestedTargetId`/nhãn cho các quy trình làm việc dài hạn.

Trình trợ giúp tệp + hộp thoại:

bashCopy code
[code]
    openclaw browser upload /tmp/openclaw/uploads/file.pdf --ref <ref>openclaw browser waitfordownloadopenclaw browser download <ref> report.pdfopenclaw browser dialog --accept
[/code]

Hồ sơ Chrome do hệ thống quản lý lưu các bản tải xuống thông thường được kích hoạt bằng nhấp chuột vào thư mục tải xuống của OpenClaw (`/tmp/openclaw/downloads` theo mặc định, hoặc thư mục tạm gốc đã cấu hình). Dùng `waitfordownload` hoặc `download` khi agent cần chờ một tệp cụ thể và trả về đường dẫn của tệp đó; các trình chờ rõ ràng đó sở hữu bản tải xuống kế tiếp.

## Trạng thái và lưu trữ

Viewport + mô phỏng:

bashCopy code
[code]
    openclaw browser resize 1280 720openclaw browser set viewport 1280 720openclaw browser set offline onopenclaw browser set media darkopenclaw browser set timezone Europe/Londonopenclaw browser set locale en-GBopenclaw browser set geo 51.5074 -0.1278 --accuracy 25openclaw browser set device "iPhone 14"openclaw browser set headers '{"x-test":"1"}'openclaw browser set credentials myuser mypass
[/code]

Cookie + lưu trữ:

bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url https://example.comopenclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set token abc123openclaw browser storage session clear
[/code]

## Gỡ lỗi

bashCopy code
[code]
    openclaw browser console --level erroropenclaw browser pdfopenclaw browser responsebody "**/api"openclaw browser highlight <ref>openclaw browser errors --clearopenclaw browser requests --filter apiopenclaw browser trace startopenclaw browser trace stop --out trace.zip
[/code]

## Chrome hiện có qua MCP

Dùng hồ sơ `user` tích hợp sẵn, hoặc tạo hồ sơ `existing-session` của riêng bạn:

bashCopy code
[code]
    openclaw browser --browser-profile user tabsopenclaw browser create-profile --name chrome-live --driver existing-sessionopenclaw browser create-profile --name brave-live --driver existing-session --user-data-dir "~/Library/Application Support/BraveSoftware/Brave-Browser"openclaw browser --browser-profile chrome-live tabs
[/code]

Đường dẫn này chỉ dành cho máy chủ lưu trữ. Với Docker, máy chủ headless, Browserless hoặc các thiết lập từ xa khác, hãy dùng hồ sơ CDP thay thế.

Giới hạn hiện tại của existing-session:

  * thao tác dựa trên bản chụp dùng ref, không dùng bộ chọn CSS
  * `browser.actionTimeoutMs` đặt mặc định các yêu cầu `act` được hỗ trợ thành 60000 ms khi bên gọi bỏ qua `timeoutMs`; `timeoutMs` theo từng lệnh gọi vẫn được ưu tiên.
  * `click` chỉ là nhấp chuột trái
  * `type` không hỗ trợ `slowly=true`
  * `press` không hỗ trợ `delayMs`
  * `hover`, `scrollintoview`, `drag`, `select`, `fill`, và `evaluate` từ chối ghi đè thời gian chờ theo từng lệnh gọi
  * `select` chỉ hỗ trợ một giá trị
  * `wait --load networkidle` không được hỗ trợ
  * tải tệp lên yêu cầu `--ref` / `--input-ref`, không hỗ trợ CSS `--element`, và hiện chỉ hỗ trợ một tệp mỗi lần
  * hook hộp thoại không hỗ trợ `--timeout`
  * ảnh chụp màn hình hỗ trợ chụp trang và `--ref`, nhưng không hỗ trợ CSS `--element`
  * `responsebody`, chặn tải xuống, xuất PDF và thao tác hàng loạt vẫn yêu cầu trình duyệt do hệ thống quản lý hoặc hồ sơ CDP thô


## Điều khiển trình duyệt từ xa (proxy máy chủ Node)

Nếu Gateway chạy trên một máy khác với trình duyệt, hãy chạy một **máy chủ Node** trên máy có Chrome/Brave/Edge/Chromium. Gateway sẽ proxy các thao tác trình duyệt tới Node đó (không cần máy chủ điều khiển trình duyệt riêng).

Dùng `gateway.nodes.browser.mode` để điều khiển định tuyến tự động và `gateway.nodes.browser.node` để ghim một Node cụ thể nếu có nhiều Node được kết nối.

Bảo mật + thiết lập từ xa: [Công cụ trình duyệt](</vi/tools/browser>), [Truy cập từ xa](</vi/gateway/remote>), [Tailscale](</vi/gateway/tailscale>), [Bảo mật](</vi/gateway/security>)

## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Trình duyệt](</vi/tools/browser>)


Was this useful?YesNo