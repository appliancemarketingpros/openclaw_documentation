---
title: API điều khiển trình duyệt
source_url: https://docs.openclaw.ai/vi/tools/browser-control
scraped_at: 2026-05-25
---

Để thiết lập, cấu hình và khắc phục sự cố, hãy xem [Trình duyệt](</vi/tools/browser>). Trang này là tài liệu tham chiếu cho HTTP API điều khiển cục bộ, CLI `openclaw browser` và các mẫu viết script (snapshot, ref, chờ, luồng gỡ lỗi).

## API điều khiển (tùy chọn)

Chỉ dành cho tích hợp cục bộ, Gateway cung cấp một HTTP API local loopback nhỏ:

  * Trạng thái/khởi động/dừng: `GET /`, `POST /start`, `POST /stop`
  * Tab: `GET /tabs`, `POST /tabs/open`, `POST /tabs/focus`, `DELETE /tabs/:targetId`
  * Snapshot/ảnh chụp màn hình: `GET /snapshot`, `POST /screenshot`
  * Hành động: `POST /navigate`, `POST /act`
  * Hook: `POST /hooks/file-chooser`, `POST /hooks/dialog`
  * Tải xuống: `POST /download`, `POST /wait/download`
  * Quyền: `POST /permissions/grant`
  * Gỡ lỗi: `GET /console`, `POST /pdf`
  * Gỡ lỗi: `GET /errors`, `GET /requests`, `POST /trace/start`, `POST /trace/stop`, `POST /highlight`
  * Mạng: `POST /response/body`
  * Trạng thái: `GET /cookies`, `POST /cookies/set`, `POST /cookies/clear`
  * Trạng thái: `GET /storage/:kind`, `POST /storage/:kind/set`, `POST /storage/:kind/clear`
  * Cài đặt: `POST /set/offline`, `POST /set/headers`, `POST /set/credentials`, `POST /set/geolocation`, `POST /set/media`, `POST /set/timezone`, `POST /set/locale`, `POST /set/device`


Tất cả endpoint chấp nhận `?profile=<name>`. `POST /start?headless=true` yêu cầu một lần khởi chạy headless cho hồ sơ được quản lý cục bộ mà không thay đổi cấu hình trình duyệt đã lưu; các hồ sơ chỉ đính kèm, CDP từ xa và phiên hiện có sẽ từ chối ghi đè đó vì OpenClaw không khởi chạy các tiến trình trình duyệt đó.

Nếu xác thực Gateway bằng shared-secret được cấu hình, các route HTTP của trình duyệt cũng yêu cầu xác thực:

  * `Authorization: Bearer <gateway token>`
  * `x-openclaw-password: <gateway password>` hoặc xác thực HTTP Basic bằng mật khẩu đó


Ghi chú:

  * API trình duyệt local loopback độc lập này **không** sử dụng trusted-proxy hoặc header danh tính Tailscale Serve.
  * Nếu `gateway.auth.mode` là `none` hoặc `trusted-proxy`, các route trình duyệt local loopback này không kế thừa các chế độ mang danh tính đó; hãy giữ chúng chỉ ở local loopback.


### Hợp đồng lỗi `/act`

`POST /act` dùng phản hồi lỗi có cấu trúc cho lỗi xác thực cấp route và lỗi chính sách:

jsonCopy code
[code]
    { "error": "<message>", "code": "ACT_*" }
[/code]

Các giá trị `code` hiện tại:

  * `ACT_KIND_REQUIRED` (HTTP 400): thiếu hoặc không nhận diện được `kind`.
  * `ACT_INVALID_REQUEST` (HTTP 400): payload hành động không chuẩn hóa hoặc xác thực được.
  * `ACT_SELECTOR_UNSUPPORTED` (HTTP 400): `selector` được dùng với loại hành động không được hỗ trợ.
  * `ACT_EVALUATE_DISABLED` (HTTP 403): `evaluate` (hoặc `wait --fn`) bị tắt bởi cấu hình.
  * `ACT_TARGET_ID_MISMATCH` (HTTP 403): `targetId` cấp cao nhất hoặc theo lô xung đột với đích yêu cầu.
  * `ACT_EXISTING_SESSION_UNSUPPORTED` (HTTP 501): hành động không được hỗ trợ cho hồ sơ phiên hiện có.


Các lỗi runtime khác vẫn có thể trả về `{ "error": "<message>" }` mà không có trường `code`.

### Yêu cầu Playwright

Một số tính năng (điều hướng/hành động/snapshot AI/snapshot vai trò, ảnh chụp phần tử, PDF) yêu cầu Playwright. Nếu Playwright chưa được cài đặt, các endpoint đó trả về lỗi 501 rõ ràng.

Những gì vẫn hoạt động khi không có Playwright:

  * Snapshot ARIA
  * Snapshot trợ năng kiểu vai trò (`--interactive`, `--compact`, `--depth`, `--efficient`) khi có WebSocket CDP theo từng tab. Đây là phương án dự phòng cho kiểm tra và khám phá ref; Playwright vẫn là engine hành động chính.
  * Ảnh chụp trang cho trình duyệt `openclaw` được quản lý khi có WebSocket CDP theo từng tab
  * Ảnh chụp trang cho hồ sơ `existing-session` / Chrome MCP
  * Ảnh chụp theo ref của `existing-session` (`--ref`) từ đầu ra snapshot


Những gì vẫn cần Playwright:

  * `navigate`
  * `act`
  * Snapshot AI phụ thuộc vào định dạng snapshot AI gốc của Playwright
  * Ảnh chụp phần tử bằng CSS-selector (`--element`)
  * xuất PDF toàn bộ trình duyệt


Ảnh chụp phần tử cũng từ chối `--full-page`; route trả về `fullPage is not supported for element screenshots`.

Nếu bạn thấy `Playwright is not available in this gateway build`, Gateway đã đóng gói đang thiếu phụ thuộc runtime trình duyệt lõi. Hãy cài đặt lại hoặc cập nhật OpenClaw, rồi khởi động lại Gateway. Với Docker, cũng cài đặt các binary trình duyệt Chromium như hiển thị bên dưới.

#### Cài đặt Docker Playwright

Nếu Gateway của bạn chạy trong Docker, hãy tránh `npx playwright` (xung đột ghi đè npm). Với image tùy chỉnh, hãy tích hợp Chromium vào image:

bashCopy code
[code]
    OPENCLAW_INSTALL_BROWSER=1 ./scripts/docker/setup.sh
[/code]

Với image hiện có, thay vào đó hãy cài đặt qua CLI đi kèm:

bashCopy code
[code]
    docker compose run --rm openclaw-cli \  node /app/node_modules/playwright-core/cli.js install chromium
[/code]

Để duy trì các bản tải xuống của trình duyệt, đặt `PLAYWRIGHT_BROWSERS_PATH` (ví dụ: `/home/node/.cache/ms-playwright`) và bảo đảm `/home/node` được lưu bền qua `OPENCLAW_HOME_VOLUME` hoặc bind mount. OpenClaw tự động phát hiện Chromium đã lưu bền trên Linux. Xem [Docker](</vi/install/docker>).

## Cách hoạt động (nội bộ)

Một máy chủ điều khiển local loopback nhỏ nhận yêu cầu HTTP và kết nối với trình duyệt dựa trên Chromium qua CDP. Các hành động nâng cao (nhấp/gõ/snapshot/PDF) đi qua Playwright trên CDP; khi thiếu Playwright, chỉ các thao tác không dùng Playwright khả dụng. Agent thấy một giao diện ổn định trong khi trình duyệt cục bộ/từ xa và hồ sơ được hoán đổi tự do bên dưới.

## Tham chiếu nhanh CLI

Tất cả lệnh chấp nhận `--browser-profile <name>` để nhắm tới một hồ sơ cụ thể, và `--json` cho đầu ra máy đọc được.

Basics: status, tabs, open/focus/close bashCopy code
[code]
    openclaw browser statusopenclaw browser startopenclaw browser start --headless # one-shot local managed headless launchopenclaw browser stop            # also clears emulation on attach-only/remote CDPopenclaw browser tabsopenclaw browser tab             # shortcut for current tabopenclaw browser tab newopenclaw browser tab select 2openclaw browser tab close 2openclaw browser open https://example.comopenclaw browser focus abcd1234openclaw browser close abcd1234
[/code]

Inspection: screenshot, snapshot, console, errors, requests bashCopy code
[code]
    openclaw browser screenshotopenclaw browser screenshot --full-pageopenclaw browser screenshot --ref 12        # or --ref e12openclaw browser screenshot --labelsopenclaw browser snapshotopenclaw browser snapshot --format aria --limit 200openclaw browser snapshot --interactive --compact --depth 6openclaw browser snapshot --efficientopenclaw browser snapshot --labelsopenclaw browser snapshot --urlsopenclaw browser snapshot --selector "#main" --interactiveopenclaw browser snapshot --frame "iframe#main" --interactiveopenclaw browser console --level erroropenclaw browser errors --clearopenclaw browser requests --filter api --clearopenclaw browser pdfopenclaw browser responsebody "**/api" --max-chars 5000
[/code]

Actions: navigate, click, type, drag, wait, evaluate bashCopy code
[code]
    openclaw browser navigate https://example.comopenclaw browser resize 1280 720openclaw browser click 12 --double           # or e12 for role refsopenclaw browser click-coords 120 340        # viewport coordinatesopenclaw browser type 23 "hello" --submitopenclaw browser press Enteropenclaw browser hover 44openclaw browser scrollintoview e12openclaw browser drag 10 11openclaw browser select 9 OptionA OptionBopenclaw browser download e12 report.pdfopenclaw browser waitfordownload report.pdfopenclaw browser upload /tmp/openclaw/uploads/file.pdfopenclaw browser fill --fields '[{"ref":"1","type":"text","value":"Ada"}]'openclaw browser dialog --acceptopenclaw browser wait --text "Done"openclaw browser wait "#main" --url "**/dash" --load networkidle --fn "window.ready===true"openclaw browser evaluate --fn '(el) => el.textContent' --ref 7openclaw browser highlight e12openclaw browser trace startopenclaw browser trace stop
[/code]

State: cookies, storage, offline, headers, geo, device bashCopy code
[code]
    openclaw browser cookiesopenclaw browser cookies set session abc123 --url "https://example.com"openclaw browser cookies clearopenclaw browser storage local getopenclaw browser storage local set theme darkopenclaw browser storage session clearopenclaw browser set offline onopenclaw browser set headers --headers-json '{"X-Debug":"1"}'openclaw browser set credentials user pass            # --clear to removeopenclaw browser set geo 37.7749 -122.4194 --origin "https://example.com"openclaw browser set media darkopenclaw browser set timezone America/New_Yorkopenclaw browser set locale en-USopenclaw browser set device "iPhone 14"
[/code]

Ghi chú:

  * `upload` và `dialog` là các lệnh **arming** ; chạy chúng trước thao tác nhấp/nhấn kích hoạt bộ chọn/hộp thoại.
  * `click`/`type`/v.v. yêu cầu một `ref` từ `snapshot` (số `12`, ref vai trò `e12`, hoặc ref ARIA có thể hành động `ax12`). CSS selector cố ý không được hỗ trợ cho hành động. Dùng `click-coords` khi vị trí viewport hiển thị là mục tiêu đáng tin cậy duy nhất.
  * Đường dẫn tải xuống, trace và upload bị giới hạn trong các gốc tạm của OpenClaw: `/tmp/openclaw{,/downloads,/uploads}` (dự phòng: `${os.tmpdir()}/openclaw/...`).
  * `upload` cũng có thể đặt file input trực tiếp qua `--input-ref` hoặc `--element`.


ID tab ổn định và nhãn tồn tại qua việc thay thế raw-target của Chromium khi OpenClaw có thể chứng minh tab thay thế, chẳng hạn như cùng URL hoặc một tab cũ duy nhất trở thành một tab mới duy nhất sau khi gửi biểu mẫu. Raw target id vẫn biến động; ưu tiên `suggestedTargetId` từ `tabs` trong script.

Tóm tắt nhanh các cờ snapshot:

  * `--format ai` (mặc định với Playwright): snapshot AI với ref dạng số (`aria-ref="<n>"`).
  * `--format aria`: cây trợ năng với ref `axN`. Khi có Playwright, OpenClaw liên kết ref với backend DOM id vào trang live để các hành động tiếp theo có thể dùng chúng; nếu không, hãy xem đầu ra chỉ để kiểm tra.
  * `--efficient` (hoặc `--mode efficient`): preset snapshot vai trò nhỏ gọn. Đặt `browser.snapshotDefaults.mode: "efficient"` để biến chế độ này thành mặc định (xem [Cấu hình Gateway](</vi/gateway/configuration-reference#browser>)).
  * `--interactive`, `--compact`, `--depth`, `--selector` buộc dùng snapshot vai trò với ref `ref=e12`. `--frame "<iframe>"` giới hạn snapshot vai trò vào một iframe.
  * `--labels` thêm ảnh chụp màn hình chỉ viewport với nhãn ref phủ lên (in `MEDIA:<path>`).
  * `--urls` thêm các đích liên kết đã phát hiện vào snapshot AI.


## Snapshot và ref

OpenClaw hỗ trợ hai kiểu "snapshot":

  * **Snapshot AI (ref dạng số)** : `openclaw browser snapshot` (mặc định; `--format ai`)

    * Đầu ra: một snapshot văn bản bao gồm ref dạng số.
    * Hành động: `openclaw browser click 12`, `openclaw browser type 23 "hello"`.
    * Nội bộ, ref được phân giải qua `aria-ref` của Playwright.
  * **Snapshot vai trò (ref vai trò như`e12`)**: `openclaw browser snapshot --interactive` (hoặc `--compact`, `--depth`, `--selector`, `--frame`)

    * Đầu ra: một danh sách/cây dựa trên vai trò với `[ref=e12]` (và tùy chọn `[nth=1]`).
    * Hành động: `openclaw browser click e12`, `openclaw browser highlight e12`.
    * Nội bộ, ref được phân giải qua `getByRole(...)` (cộng với `nth()` cho các bản trùng).
    * Thêm `--labels` để bao gồm ảnh chụp viewport với nhãn `e12` phủ lên.
    * Thêm `--urls` khi văn bản liên kết mơ hồ và agent cần các đích điều hướng cụ thể.
  * **Ảnh chụp nhanh ARIA (các tham chiếu ARIA như`ax12`)**: `openclaw browser snapshot --format aria`

    * Đầu ra: cây trợ năng dưới dạng các nút có cấu trúc.
    * Hành động: `openclaw browser click ax12` hoạt động khi đường dẫn ảnh chụp nhanh có thể liên kết tham chiếu thông qua Playwright và các id DOM backend của Chrome.
  * Nếu Playwright không khả dụng, ảnh chụp nhanh ARIA vẫn có thể hữu ích cho việc kiểm tra, nhưng các tham chiếu có thể không thao tác được. Chụp lại bằng `--format ai` hoặc `--interactive` khi bạn cần tham chiếu hành động.

  * Bằng chứng Docker cho đường dẫn dự phòng raw-CDP: `pnpm test:docker:browser-cdp-snapshot` khởi động Chromium với CDP, chạy `browser doctor --deep`, và xác minh rằng ảnh chụp nhanh vai trò bao gồm URL liên kết, phần tử có thể nhấp được thăng cấp từ con trỏ, và siêu dữ liệu iframe.


Hành vi tham chiếu:

  * Tham chiếu **không ổn định qua các lần điều hướng** ; nếu có lỗi, hãy chạy lại `snapshot` và dùng tham chiếu mới.
  * `/act` trả về `targetId` thô hiện tại sau khi thay thế do hành động kích hoạt khi nó có thể chứng minh tab thay thế. Tiếp tục dùng id/nhãn tab ổn định cho các lệnh tiếp theo.
  * Nếu ảnh chụp nhanh vai trò được lấy bằng `--frame`, các tham chiếu vai trò được giới hạn trong iframe đó cho đến ảnh chụp nhanh vai trò tiếp theo.
  * Tham chiếu `axN` không xác định hoặc đã cũ sẽ thất bại nhanh thay vì rơi tiếp xuống bộ chọn `aria-ref` của Playwright. Hãy chạy ảnh chụp nhanh mới trên cùng tab khi điều đó xảy ra.


## Nâng cấp sức mạnh cho thao tác chờ

Bạn có thể chờ nhiều thứ hơn là chỉ thời gian/văn bản:

  * Chờ URL (Playwright hỗ trợ glob): 
    * `openclaw browser wait --url "**/dash"`
  * Chờ trạng thái tải: 
    * `openclaw browser wait --load networkidle`
  * Chờ một predicate JS: 
    * `openclaw browser wait --fn "window.ready===true"`
  * Chờ một bộ chọn trở nên hiển thị: 
    * `openclaw browser wait "#main"`


Có thể kết hợp các tùy chọn này:

bashCopy code
[code]
    openclaw browser wait "#main" \  --url "**/dash" \  --load networkidle \  --fn "window.ready===true" \  --timeout-ms 15000
[/code]

## Quy trình gỡ lỗi

Khi một hành động thất bại (ví dụ: "not visible", "strict mode violation", "covered"):

  1. `openclaw browser snapshot --interactive`
  2. Dùng `click <ref>` / `type <ref>` (ưu tiên tham chiếu vai trò trong chế độ tương tác)
  3. Nếu vẫn thất bại: `openclaw browser highlight <ref>` để xem Playwright đang nhắm tới gì
  4. Nếu trang hoạt động bất thường: 
     * `openclaw browser errors --clear`
     * `openclaw browser requests --filter api --clear`
  5. Để gỡ lỗi sâu: ghi lại một trace: 
     * `openclaw browser trace start`
     * tái hiện sự cố
     * `openclaw browser trace stop` (in ra `TRACE:<path>`)


## Đầu ra JSON

`--json` dùng cho script và công cụ có cấu trúc.

Ví dụ:

bashCopy code
[code]
    openclaw browser status --jsonopenclaw browser snapshot --interactive --jsonopenclaw browser requests --filter api --jsonopenclaw browser cookies --json
[/code]

Ảnh chụp nhanh vai trò trong JSON bao gồm `refs` cùng một khối `stats` nhỏ (lines/chars/refs/interactive) để công cụ có thể suy luận về kích thước và mật độ payload.

## Trạng thái và nút điều chỉnh môi trường

Những mục này hữu ích cho các quy trình "làm cho trang web hoạt động như X":

  * Cookie: `cookies`, `cookies set`, `cookies clear`
  * Lưu trữ: `storage local|session get|set|clear`
  * Ngoại tuyến: `set offline on|off`
  * Header: `set headers --headers-json '{"X-Debug":"1"}'` (`set headers --json '{"X-Debug":"1"}'` kiểu cũ vẫn được hỗ trợ)
  * Xác thực HTTP basic: `set credentials user pass` (hoặc `--clear`)
  * Vị trí địa lý: `set geo <lat> <lon> --origin "https://example.com"` (hoặc `--clear`)
  * Media: `set media dark|light|no-preference|none`
  * Múi giờ / locale: `set timezone ...`, `set locale ...`
  * Thiết bị / viewport: 
    * `set device "iPhone 14"` (preset thiết bị của Playwright)
    * `set viewport 1280 720`


## Bảo mật và quyền riêng tư

  * Hồ sơ trình duyệt openclaw có thể chứa các phiên đã đăng nhập; hãy xem nó là dữ liệu nhạy cảm.
  * `browser act kind=evaluate` / `openclaw browser evaluate` và `wait --fn` thực thi JavaScript tùy ý trong ngữ cảnh trang. Prompt injection có thể điều hướng việc này. Tắt bằng `browser.evaluateEnabled=false` nếu bạn không cần.
  * Để biết ghi chú về đăng nhập và chống bot (X/Twitter, v.v.), xem [Đăng nhập trình duyệt + đăng bài X/Twitter](</vi/tools/browser-login>).
  * Giữ máy chủ Gateway/Node riêng tư (loopback hoặc chỉ tailnet).
  * Endpoint CDP từ xa rất mạnh; hãy tạo tunnel và bảo vệ chúng.


Ví dụ strict-mode (mặc định chặn đích riêng tư/nội bộ):

json5Copy code
[code]
    {  browser: {    ssrfPolicy: {      dangerouslyAllowPrivateNetwork: false,      hostnameAllowlist: ["*.example.com", "example.com"],      allowedHostnames: ["localhost"], // optional exact allow    },  },}
[/code]

## Liên quan

  * [Trình duyệt](</vi/tools/browser>) \- tổng quan, cấu hình, hồ sơ, bảo mật
  * [Đăng nhập trình duyệt](</vi/tools/browser-login>) \- đăng nhập vào các trang
  * [Khắc phục sự cố Trình duyệt trên Linux](</vi/tools/browser-linux-troubleshooting>)
  * [Khắc phục sự cố Trình duyệt WSL2](</vi/tools/browser-wsl2-windows-remote-cdp-troubleshooting>)


Was this useful?YesNo