---
title: Đang cập nhật
source_url: https://docs.openclaw.ai/vi/install/updating
scraped_at: 2026-05-25
---

Luôn cập nhật OpenClaw.

## Khuyến nghị: `openclaw update`

Cách cập nhật nhanh nhất. Lệnh này phát hiện kiểu cài đặt của bạn (npm hoặc git), tải phiên bản mới nhất, chạy `openclaw doctor` và khởi động lại Gateway.

bashCopy code
[code]
    openclaw update
[/code]

Để chuyển kênh hoặc nhắm tới một phiên bản cụ thể:

bashCopy code
[code]
    openclaw update --channel betaopenclaw update --channel devopenclaw update --tag mainopenclaw update --dry-run   # preview without applying
[/code]

`openclaw update` không chấp nhận `--verbose`. Để chẩn đoán cập nhật, hãy dùng `--dry-run` để xem trước các hành động dự kiến, `--json` để nhận kết quả có cấu trúc, hoặc `openclaw update status --json` để kiểm tra trạng thái kênh và khả dụng. Trình cài đặt có cờ `--verbose` riêng, nhưng cờ đó không thuộc `openclaw update`.

`--channel beta` ưu tiên beta, nhưng runtime sẽ quay về stable/latest khi thẻ beta bị thiếu hoặc cũ hơn bản phát hành stable mới nhất. Dùng `--tag beta` nếu bạn muốn dist-tag beta thô của npm cho một lần cập nhật gói riêng lẻ.

Với Plugin được quản lý, việc quay về từ kênh beta là một cảnh báo: bản cập nhật lõi vẫn có thể thành công trong khi Plugin dùng bản phát hành default/latest đã ghi nhận vì không có bản beta của Plugin.

Xem [Kênh phát triển](</vi/install/development-channels>) để biết ngữ nghĩa của kênh.

## Chuyển đổi giữa cài đặt npm và git

Dùng kênh khi bạn muốn thay đổi kiểu cài đặt. Trình cập nhật giữ nguyên trạng thái, cấu hình, thông tin xác thực và workspace của bạn trong `~/.openclaw`; nó chỉ thay đổi bản cài đặt mã OpenClaw mà CLI và Gateway sử dụng.

bashCopy code
[code]
    # npm package install -> editable git checkoutopenclaw update --channel dev # git checkout -> npm package installopenclaw update --channel stable
[/code]

Chạy với `--dry-run` trước để xem trước chính xác việc chuyển chế độ cài đặt:

bashCopy code
[code]
    openclaw update --channel dev --dry-runopenclaw update --channel stable --dry-run
[/code]

Kênh `dev` bảo đảm có một git checkout, build nó và cài đặt CLI toàn cục từ checkout đó. Các kênh `stable` và `beta` dùng cài đặt gói. Nếu Gateway đã được cài đặt, `openclaw update` làm mới metadata của dịch vụ và khởi động lại dịch vụ trừ khi bạn truyền `--no-restart`.

## Phương án khác: chạy lại trình cài đặt

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

Thêm `--no-onboard` để bỏ qua onboarding. Để ép một kiểu cài đặt cụ thể thông qua trình cài đặt, truyền `--install-method git --no-onboard` hoặc `--install-method npm --no-onboard`.

Nếu `openclaw update` thất bại sau giai đoạn cài đặt gói npm, hãy chạy lại trình cài đặt. Trình cài đặt không gọi trình cập nhật cũ; nó chạy trực tiếp cài đặt gói toàn cục và có thể khôi phục một bản cài đặt npm đã cập nhật dở.

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm
[/code]

Để ghim quá trình khôi phục vào một phiên bản hoặc dist-tag cụ thể, thêm `--version`:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm --version <version-or-dist-tag>
[/code]

## Phương án khác: npm, pnpm hoặc bun thủ công

bashCopy code
[code]
    npm i -g openclaw@latest
[/code]

Ưu tiên `openclaw update` cho các bản cài đặt được giám sát vì nó có thể phối hợp việc hoán đổi gói với dịch vụ Gateway đang chạy. Nếu bạn cập nhật thủ công trong khi Gateway được quản lý đang chạy, hãy khởi động lại Gateway ngay sau khi trình quản lý gói hoàn tất để tiến trình cũ không tiếp tục phục vụ từ các tệp gói đã được thay thế.

Khi `openclaw update` quản lý một bản cài đặt npm toàn cục, nó cài đặt mục tiêu vào một tiền tố npm tạm thời trước, xác minh inventory `dist` đã đóng gói, rồi hoán đổi cây gói sạch vào tiền tố toàn cục thật. Cách này tránh việc npm phủ một gói mới lên các tệp cũ còn sót lại từ gói cũ. Nếu lệnh cài đặt thất bại, OpenClaw thử lại một lần với `--omit=optional`. Lần thử lại đó hữu ích với các máy chủ nơi các dependency tùy chọn native không thể biên dịch, đồng thời vẫn giữ lỗi ban đầu hiển thị nếu phương án dự phòng cũng thất bại.

bashCopy code
[code]
    pnpm add -g openclaw@latest
[/code]

bashCopy code
[code]
    bun add -g openclaw@latest
[/code]

### Chủ đề nâng cao về cài đặt npm

Cây gói chỉ đọc

OpenClaw xem các bản cài đặt toàn cục đã đóng gói là chỉ đọc ở runtime, ngay cả khi thư mục gói toàn cục có thể ghi bởi người dùng hiện tại. Các bản cài đặt gói Plugin nằm trong các root npm/git do OpenClaw sở hữu bên dưới thư mục cấu hình người dùng, và quá trình khởi động Gateway không sửa đổi cây gói OpenClaw.

Một số thiết lập npm trên Linux cài đặt gói toàn cục dưới các thư mục thuộc sở hữu root như `/usr/lib/node_modules/openclaw`. OpenClaw hỗ trợ bố cục đó vì các lệnh cài đặt/cập nhật Plugin ghi ra ngoài thư mục gói toàn cục đó.

Đơn vị systemd được gia cố

Cấp quyền ghi cho OpenClaw vào các root cấu hình/trạng thái của nó để các lượt cài đặt Plugin rõ ràng, cập nhật Plugin và dọn dẹp doctor có thể lưu thay đổi:

iniCopy code
[code]
    ReadWritePaths=/var/lib/openclaw /home/openclaw/.openclaw /tmp
[/code]

Kiểm tra sơ bộ dung lượng đĩa

Trước các bản cập nhật gói và lượt cài đặt Plugin rõ ràng, OpenClaw cố gắng kiểm tra dung lượng đĩa theo khả năng tốt nhất cho volume mục tiêu. Dung lượng thấp tạo ra cảnh báo kèm đường dẫn đã kiểm tra, nhưng không chặn bản cập nhật vì quota hệ thống tệp, snapshot và volume mạng có thể thay đổi sau khi kiểm tra. Lượt cài đặt thực tế của trình quản lý gói và xác minh sau cài đặt vẫn là căn cứ có thẩm quyền.

## Trình tự động cập nhật

Trình tự động cập nhật mặc định tắt. Bật nó trong `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  update: {    channel: "stable",    auto: {      enabled: true,      stableDelayHours: 6,      stableJitterHours: 12,      betaCheckIntervalHours: 1,    },  },}
[/code]

Kênh | Hành vi  
---|---  
`stable` | Chờ `stableDelayHours`, rồi áp dụng với jitter xác định trên `stableJitterHours` (triển khai phân tán).  
`beta` | Kiểm tra mỗi `betaCheckIntervalHours` (mặc định: hằng giờ) và áp dụng ngay.  
`dev` | Không tự động áp dụng. Dùng `openclaw update` thủ công.  
  
Gateway cũng ghi log một gợi ý cập nhật khi khởi động (tắt bằng `update.checkOnStart: false`). Để hạ cấp hoặc khôi phục sự cố, đặt `OPENCLAW_NO_AUTO_UPDATE=1` trong môi trường Gateway để chặn việc tự động áp dụng ngay cả khi `update.auto.enabled` đã được cấu hình. Gợi ý cập nhật khi khởi động vẫn có thể chạy trừ khi `update.checkOnStart` cũng bị tắt.

Các bản cập nhật trình quản lý gói được yêu cầu thông qua handler control-plane Gateway trực tiếp ép khởi động lại cập nhật không trì hoãn, không cooldown sau khi hoán đổi gói. Điều đó tránh để một tiến trình cũ trong bộ nhớ tồn tại đủ lâu để lazy-load các chunk từ cây gói đã bị thay thế. Shell `openclaw update` vẫn là đường dẫn ưu tiên cho các bản cài đặt được giám sát vì nó có thể dừng và khởi động lại dịch vụ quanh quá trình cập nhật.

## Sau khi cập nhật

### Chạy doctor

bashCopy code
[code]
    openclaw doctor
[/code]

Di chuyển cấu hình, kiểm tra chính sách DM và kiểm tra sức khỏe Gateway. Chi tiết: [Doctor](</vi/gateway/doctor>)

### Khởi động lại Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

### Xác minh

bashCopy code
[code]
    openclaw health
[/code]

## Rollback

### Ghim một phiên bản (npm)

bashCopy code
[code]
    npm i -g openclaw@<version>openclaw doctoropenclaw gateway restart
[/code]

### Ghim một commit (source)

bashCopy code
[code]
    git fetch origingit checkout "$(git rev-list -n 1 --before=\"2026-01-01\" origin/main)"pnpm install && pnpm buildopenclaw gateway restart
[/code]

Để quay lại bản mới nhất: `git checkout main && git pull`.

## Nếu bạn bị kẹt

  * Chạy lại `openclaw doctor` và đọc kỹ đầu ra.
  * Với `openclaw update --channel dev` trên source checkout, trình cập nhật tự động bootstrap `pnpm` khi cần. Nếu bạn thấy lỗi bootstrap pnpm/corepack, hãy cài đặt `pnpm` thủ công (hoặc bật lại `corepack`) và chạy lại bản cập nhật.
  * Kiểm tra: [Khắc phục sự cố](</vi/gateway/troubleshooting>)
  * Hỏi trong Discord: <https://discord.gg/clawd>


## Liên quan

  * [Tổng quan cài đặt](</vi/install>): tất cả phương thức cài đặt.
  * [Doctor](</vi/gateway/doctor>): kiểm tra sức khỏe sau khi cập nhật.
  * [Di chuyển](</vi/install/migrating>): hướng dẫn di chuyển phiên bản lớn.


Was this useful?YesNo