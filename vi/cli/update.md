---
title: Cập nhật
source_url: https://docs.openclaw.ai/vi/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

Cập nhật OpenClaw an toàn và chuyển đổi giữa các kênh stable/beta/dev.

Nếu bạn cài đặt qua **npm/pnpm/bun** (cài đặt global, không có metadata git), các bản cập nhật sẽ diễn ra qua luồng trình quản lý gói trong [Cập nhật](</vi/install/updating>).

## Cách sử dụng

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## Tùy chọn

  * `--no-restart`: bỏ qua việc khởi động lại dịch vụ Gateway sau khi cập nhật thành công. Các bản cập nhật bằng trình quản lý gói có khởi động lại Gateway sẽ xác minh dịch vụ đã khởi động lại báo cáo đúng phiên bản đã cập nhật mong đợi trước khi lệnh thành công.
  * `--channel <stable|beta|dev>`: đặt kênh cập nhật (git + npm; được lưu trong cấu hình).
  * `--tag <dist-tag|version|spec>`: ghi đè đích gói chỉ cho lần cập nhật này. Với các bản cài đặt bằng gói, `main` ánh xạ tới `github:openclaw/openclaw#main`.
  * `--dry-run`: xem trước các hành động cập nhật dự kiến (luồng channel/tag/target/restart) mà không ghi cấu hình, cài đặt, đồng bộ plugin hoặc khởi động lại.
  * `--json`: in JSON `UpdateRunResult` máy có thể đọc, bao gồm `postUpdate.plugins.warnings` khi các plugin được quản lý bị hỏng hoặc không thể tải cần sửa chữa sau khi cập nhật lõi thành công, chi tiết fallback plugin kênh beta khi một plugin không có bản phát hành beta, và `postUpdate.plugins.integrityDrifts` khi phát hiện drift artifact plugin npm trong quá trình đồng bộ plugin sau cập nhật.
  * `--timeout <seconds>`: thời gian chờ cho mỗi bước (mặc định là 1800s).
  * `--yes`: bỏ qua lời nhắc xác nhận (ví dụ xác nhận hạ cấp).


`openclaw update` không có cờ `--verbose`. Dùng `--dry-run` để xem trước các hành động channel/tag/install/restart dự kiến, `--json` để nhận kết quả máy có thể đọc, và `openclaw update status --json` khi bạn chỉ cần kênh và chi tiết khả dụng. Nếu bạn đang gỡ lỗi nhật ký Gateway quanh một bản cập nhật, độ chi tiết console và mức nhật ký tệp là riêng biệt: Gateway `--verbose` ảnh hưởng đến đầu ra terminal/WebSocket, còn nhật ký tệp yêu cầu `logging.level: "debug"` hoặc `"trace"` trong cấu hình. Xem [Ghi nhật ký Gateway](</vi/gateway/logging>).

## `update status`

Hiển thị kênh cập nhật đang hoạt động + git tag/branch/SHA (với checkout từ nguồn), cùng với khả năng cập nhật.

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

Tùy chọn:

  * `--json`: in JSON trạng thái máy có thể đọc.
  * `--timeout <seconds>`: thời gian chờ cho các kiểm tra (mặc định là 3s).


## `update wizard`

Luồng tương tác để chọn kênh cập nhật và xác nhận có khởi động lại Gateway sau khi cập nhật hay không (mặc định là khởi động lại). Nếu bạn chọn `dev` mà không có checkout git, nó sẽ đề nghị tạo một checkout.

Tùy chọn:

  * `--timeout <seconds>`: thời gian chờ cho từng bước cập nhật (mặc định `1800`)


## Chức năng

Khi bạn chuyển kênh rõ ràng (`--channel ...`), OpenClaw cũng giữ cho phương thức cài đặt được căn chỉnh:

  * `dev` → bảo đảm có checkout git (mặc định: `~/openclaw`, ghi đè bằng `OPENCLAW_GIT_DIR`), cập nhật nó và cài đặt CLI global từ checkout đó.
  * `stable` → cài đặt từ npm bằng `latest`.
  * `beta` → ưu tiên npm dist-tag `beta`, nhưng fallback về `latest` khi beta thiếu hoặc cũ hơn bản phát hành stable hiện tại.


Trình tự động cập nhật lõi Gateway (khi được bật qua cấu hình) khởi chạy đường dẫn cập nhật CLI bên ngoài trình xử lý yêu cầu Gateway đang chạy. Các bản cập nhật trình quản lý gói `update.run` ở control-plane buộc khởi động lại cập nhật không trì hoãn, không cooldown sau khi hoán đổi gói, vì tiến trình Gateway cũ có thể vẫn có các chunk trong bộ nhớ trỏ tới các tệp đã bị gói mới xóa.

Với các bản cài đặt bằng trình quản lý gói, `openclaw update` phân giải phiên bản gói đích trước khi gọi trình quản lý gói. Các bản cài đặt global npm dùng cài đặt theo giai đoạn: OpenClaw cài đặt gói mới vào một prefix npm tạm thời, xác minh inventory `dist` đã đóng gói tại đó, rồi hoán đổi cây gói sạch đó vào prefix global thật. Nếu xác minh thất bại, doctor sau cập nhật, đồng bộ plugin và việc khởi động lại sẽ không chạy từ cây đáng nghi. Ngay cả khi phiên bản đã cài đặt đã khớp với đích, lệnh vẫn làm mới bản cài đặt gói global, sau đó chạy đồng bộ plugin, làm mới hoàn tất lệnh lõi và công việc khởi động lại. Điều này giữ các sidecar đã đóng gói và bản ghi plugin do kênh sở hữu căn chỉnh với bản dựng OpenClaw đã cài đặt, đồng thời để các lần dựng lại hoàn tất lệnh plugin đầy đủ cho các lần chạy `openclaw completion --write-state` rõ ràng.

Khi một dịch vụ Gateway được quản lý cục bộ đã được cài đặt và khởi động lại được bật, các bản cập nhật bằng trình quản lý gói sẽ dừng dịch vụ đang chạy trước khi thay thế cây gói, sau đó làm mới metadata dịch vụ từ bản cài đặt đã cập nhật, khởi động lại dịch vụ và xác minh Gateway đã khởi động lại báo cáo đúng phiên bản mong đợi trước khi báo cáo thành công. Trên macOS, kiểm tra sau cập nhật cũng xác minh LaunchAgent đã được tải/đang chạy cho hồ sơ đang hoạt động và cổng loopback đã cấu hình khỏe mạnh. Nếu plist đã được cài đặt nhưng launchd không giám sát nó, OpenClaw tự động bootstrap lại LaunchAgent, rồi chạy lại các kiểm tra sức khỏe/phiên bản/kênh sẵn sàng. Một bootstrap mới tải job RunAtLoad trực tiếp, nên phục hồi cập nhật không ngay lập tức `kickstart -k` Gateway vừa được sinh ra. Nếu Gateway vẫn không trở nên khỏe mạnh, lệnh thoát khác 0 và in đường dẫn nhật ký khởi động lại cùng hướng dẫn rõ ràng để khởi động lại, cài đặt lại và rollback gói. Với `--no-restart`, việc thay thế gói vẫn chạy nhưng dịch vụ được quản lý không bị dừng hoặc khởi động lại, nên Gateway đang chạy có thể tiếp tục dùng mã cũ cho đến khi bạn khởi động lại thủ công.

## Luồng checkout git

### Chọn kênh

  * `stable`: checkout tag non-beta mới nhất, rồi build và doctor.
  * `beta`: ưu tiên tag `-beta` mới nhất, nhưng fallback về tag stable mới nhất khi beta thiếu hoặc cũ hơn.
  * `dev`: checkout `main`, rồi fetch và rebase.


### Các bước cập nhật

* ### Xác minh worktree sạch

Yêu cầu không có thay đổi chưa commit.

* ### Chuyển kênh

Chuyển sang kênh đã chọn (tag hoặc branch).

* ### Fetch upstream

Chỉ dành cho dev.

* ### Build preflight (chỉ dev)

Chạy build TypeScript trong một worktree tạm. Nếu tip thất bại, lùi lại tối đa 10 commit để tìm commit mới nhất có thể build. Đặt `OPENCLAW_UPDATE_PREFLIGHT_LINT=1` để cũng chạy lint trong preflight này; lint chạy ở chế độ serial giới hạn vì máy cập nhật của người dùng thường nhỏ hơn CI runner.

* ### Rebase

Rebase lên commit đã chọn (chỉ dev).

* ### Cài đặt dependency

Dùng trình quản lý gói của repo. Với checkout pnpm, trình cập nhật bootstrap `pnpm` khi cần (trước tiên qua `corepack`, rồi fallback tạm thời bằng `npm install pnpm@11`) thay vì chạy `npm run build` bên trong workspace pnpm.

* ### Build Control UI

Build gateway và Control UI.

* ### Chạy doctor

`openclaw doctor` chạy như kiểm tra cập nhật an toàn cuối cùng.

* ### Đồng bộ plugin

Đồng bộ plugin với kênh đang hoạt động. Dev dùng plugin được đóng gói kèm; stable và beta dùng npm. Cập nhật các bản cài đặt plugin được theo dõi.

Trên kênh cập nhật beta, các bản cài đặt plugin npm và ClawHub được theo dõi đi theo dòng default/latest sẽ thử bản phát hành plugin `@beta` trước. Nếu plugin không có bản phát hành beta, OpenClaw fallback về spec default/latest đã ghi nhận và báo cáo điều đó như một cảnh báo. Với plugin npm, OpenClaw cũng fallback khi gói beta tồn tại nhưng không vượt qua xác thực cài đặt. Các cảnh báo fallback plugin này không làm cập nhật lõi thất bại. Phiên bản chính xác và tag rõ ràng không bị ghi lại.

## Viết tắt `--update`

`openclaw --update` được viết lại thành `openclaw update` (hữu ích cho shell và script launcher).

## Liên quan

  * `openclaw doctor` (đề nghị chạy update trước trên checkout git)
  * [Kênh phát triển](</vi/install/development-channels>)
  * [Cập nhật](</vi/install/updating>)
  * [Tham chiếu CLI](</vi/cli>)


Was this useful?YesNo