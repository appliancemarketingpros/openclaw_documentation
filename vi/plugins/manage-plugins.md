---
title: Quản lý Plugin
source_url: https://docs.openclaw.ai/vi/plugins/manage-plugins
scraped_at: 2026-05-25
---

Hầu hết quy trình làm việc với Plugin chỉ gồm vài lệnh: tìm kiếm, cài đặt, khởi động lại Gateway, xác minh và gỡ cài đặt khi bạn không còn cần Plugin nữa.

## Liệt kê Plugin

bashCopy code
[code]
    openclaw plugins listopenclaw plugins list --enabledopenclaw plugins list --verboseopenclaw plugins list --json
[/code]

Dùng `--json` cho script. Cờ này bao gồm chẩn đoán registry và `dependencyStatus` tĩnh của từng Plugin khi gói Plugin khai báo `dependencies` hoặc `optionalDependencies`.

bashCopy code
[code]
    openclaw plugins list --json \  | jq '.plugins[] | {id, enabled, format, source, dependencyStatus}'
[/code]

`plugins list` là bước kiểm tra kho lạnh. Nó hiển thị những gì OpenClaw có thể phát hiện từ cấu hình, manifest và registry Plugin; nó không chứng minh rằng một tiến trình Gateway đang chạy đã nhập runtime của Plugin.

## Cài đặt Plugin

bashCopy code
[code]
    # Search ClawHub for plugin packages.openclaw plugins search "calendar" # Bare package specs try ClawHub first, then npm fallback.openclaw plugins install <package> # Force one source.openclaw plugins install clawhub:<package>openclaw plugins install npm:<package> # Install a specific version or dist-tag.openclaw plugins install clawhub:<package>@1.2.3openclaw plugins install clawhub:<package>@betaopenclaw plugins install npm:@scope/openclaw-plugin@1.2.3openclaw plugins install npm:@openclaw/codex # Install from git or a local development checkout.openclaw plugins install git:github.com/acme/openclaw-plugin@v1.0.0openclaw plugins install ./my-pluginopenclaw plugins install --link ./my-plugin
[/code]

Sau khi cài đặt mã Plugin, hãy khởi động lại Gateway phục vụ các kênh của bạn:

bashCopy code
[code]
    openclaw gateway restartopenclaw plugins inspect <plugin-id> --runtime --json
[/code]

Dùng `inspect --runtime` khi bạn cần bằng chứng rằng Plugin đã đăng ký các bề mặt runtime như công cụ, hook, dịch vụ, phương thức Gateway hoặc lệnh CLI do Plugin sở hữu.

## Cập nhật Plugin

bashCopy code
[code]
    openclaw plugins update <plugin-id>openclaw plugins update <npm-package-or-spec>openclaw plugins update --all
[/code]

Nếu một Plugin được cài đặt từ npm dist-tag như `@beta`, các lần gọi `update <plugin-id>` sau đó sẽ dùng lại tag đã ghi đó. Truyền một npm spec rõ ràng sẽ chuyển bản cài đặt được theo dõi sang spec đó cho các bản cập nhật trong tương lai.

bashCopy code
[code]
    openclaw plugins update @scope/openclaw-plugin@betaopenclaw plugins update @scope/openclaw-plugin
[/code]

Lệnh thứ hai đưa một Plugin trở lại dòng phát hành mặc định của registry khi trước đó nó được ghim vào một phiên bản hoặc tag chính xác.

Khi `openclaw update` chạy trên kênh beta, các bản ghi Plugin npm và ClawHub thuộc dòng mặc định sẽ thử bản phát hành Plugin `@beta` tương ứng trước. Nếu bản phát hành beta đó không tồn tại, OpenClaw sẽ quay về spec mặc định/mới nhất đã ghi. Với Plugin npm, OpenClaw cũng quay về khi gói beta tồn tại nhưng không vượt qua xác thực cài đặt. Các phiên bản chính xác và tag rõ ràng như `@rc` hoặc `@beta` được giữ nguyên.

## Gỡ cài đặt Plugin

bashCopy code
[code]
    openclaw plugins uninstall <plugin-id> --dry-runopenclaw plugins uninstall <plugin-id>openclaw plugins uninstall <plugin-id> --keep-filesopenclaw gateway restart
[/code]

Gỡ cài đặt sẽ xóa mục cấu hình của Plugin, bản ghi chỉ mục Plugin, các mục danh sách cho phép/từ chối và đường dẫn tải được liên kết khi áp dụng. Thư mục cài đặt được quản lý sẽ bị xóa trừ khi bạn truyền `--keep-files`.

Ở chế độ Nix (`OPENCLAW_NIX_MODE=1`), các lệnh cài đặt, cập nhật, gỡ cài đặt, bật và tắt Plugin bị vô hiệu hóa. Thay vào đó, hãy quản lý các lựa chọn đó trong nguồn Nix cho bản cài đặt; với nix-openclaw, hãy dùng [Khởi động nhanh](<https://github.com/openclaw/nix-openclaw#quick-start>) ưu tiên agent.

## Phát hành Plugin

Bạn có thể phát hành Plugin bên ngoài lên [ClawHub](<https://clawhub.ai>), [npmjs.com](<http://npmjs.com>) hoặc cả hai.

### Phát hành lên ClawHub

ClawHub là bề mặt khám phá công khai chính cho Plugin OpenClaw. Nó cung cấp cho người dùng metadata có thể tìm kiếm, lịch sử phiên bản và kết quả quét registry trước khi cài đặt.

bashCopy code
[code]
    npm i -g clawhubclawhub loginclawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginclawhub package publish your-org/your-plugin@v1.0.0
[/code]

Người dùng cài đặt từ ClawHub bằng:

bashCopy code
[code]
    openclaw plugins install clawhub:<package>openclaw plugins install <package>
[/code]

Dạng rút gọn vẫn kiểm tra ClawHub trước.

### Phát hành lên [npmjs.com](<http://npmjs.com>)

Plugin npm native phải bao gồm manifest Plugin và metadata entrypoint OpenClaw trong `package.json`.

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

bashCopy code
[code]
    npm publish --access public
[/code]

Người dùng chỉ cài đặt npm bằng:

bashCopy code
[code]
    openclaw plugins install npm:@acme/openclaw-pluginopenclaw plugins install npm:@acme/openclaw-plugin@betaopenclaw plugins install npm:@acme/openclaw-plugin@1.0.0
[/code]

Nếu cùng gói đó cũng có trên ClawHub, `npm:` sẽ bỏ qua tra cứu ClawHub và ép phân giải qua npm.

## Lựa chọn nguồn

  * **ClawHub** : dùng khi bạn muốn khả năng khám phá native cho OpenClaw, bản tóm tắt quét, phiên bản và gợi ý cài đặt.
  * **[npmjs.com](<http://npmjs.com>)** : dùng khi bạn đã phát hành các gói JavaScript hoặc cần quy trình dist-tag/registry riêng của npm.
  * **Git** : dùng khi bạn muốn cài đặt trực tiếp từ một nhánh, tag hoặc commit.
  * **Đường dẫn cục bộ** : dùng khi bạn đang phát triển hoặc kiểm thử một Plugin trên cùng máy.


## Liên quan

  * [Plugin](</vi/tools/plugin>) \- tổng quan và khắc phục sự cố
  * [`openclaw plugins`](</vi/cli/plugins>) \- tài liệu tham khảo CLI đầy đủ
  * [ClawHub](</vi/clawhub/cli>) \- thao tác phát hành và registry
  * [Xây dựng Plugin](</vi/plugins/building-plugins>) \- tạo một gói Plugin
  * [Manifest Plugin](</vi/plugins/manifest>) \- manifest và metadata gói


Was this useful?YesNo