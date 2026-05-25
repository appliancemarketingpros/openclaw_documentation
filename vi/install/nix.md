---
title: Nix
source_url: https://docs.openclaw.ai/vi/install/nix
scraped_at: 2026-05-25
---

Cài đặt OpenClaw theo cách khai báo với **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** \- mô-đun Home Manager chính chủ, đầy đủ sẵn pin.

## Bạn nhận được gì

  * Gateway + ứng dụng macOS + công cụ (whisper, spotify, cameras) -- tất cả đều được ghim phiên bản
  * Dịch vụ launchd tồn tại qua các lần khởi động lại
  * Hệ thống Plugin với cấu hình khai báo
  * Hoàn tác tức thì: `home-manager switch --rollback`


## Bắt đầu nhanh

* ### Install Determinate Nix

Nếu Nix chưa được cài đặt, hãy làm theo hướng dẫn của [trình cài đặt Determinate Nix](<https://github.com/DeterminateSystems/nix-installer>).

* ### Create a local flake

Sử dụng mẫu ưu tiên tác nhân từ repo nix-openclaw:

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### Configure secrets

Thiết lập token bot nhắn tin và khóa API của nhà cung cấp mô hình. Các tệp thuần tại `~/.secrets/` hoạt động tốt.

* ### Fill in template placeholders and switch

bashCopy code
[code]
    home-manager switch
[/code]

* ### Verify

Xác nhận dịch vụ launchd đang chạy và bot của bạn phản hồi tin nhắn.

Xem [README nix-openclaw](<https://github.com/openclaw/nix-openclaw>) để biết đầy đủ tùy chọn mô-đun và ví dụ.

## Hành vi runtime ở chế độ Nix

Khi `OPENCLAW_NIX_MODE=1` được đặt (tự động với nix-openclaw), OpenClaw chuyển sang chế độ xác định cho các bản cài đặt do Nix quản lý. Các gói Nix khác có thể đặt cùng chế độ; nix-openclaw là tham chiếu chính chủ.

Bạn cũng có thể đặt thủ công:

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

Trên macOS, ứng dụng GUI không tự động kế thừa biến môi trường shell. Thay vào đó, bật chế độ Nix qua defaults:

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### Điều gì thay đổi trong chế độ Nix

  * Các luồng tự động cài đặt và tự thay đổi bị tắt
  * `openclaw.json` được xem là bất biến. Các mặc định sinh ra lúc khởi động chỉ tồn tại trong runtime, và các trình ghi cấu hình như setup, onboarding, `openclaw update` có thay đổi, cài đặt/cập nhật/gỡ cài đặt/bật Plugin, `doctor --fix`, `doctor --generate-gateway-token`, và `openclaw config set` sẽ từ chối chỉnh sửa tệp.
  * Các tác nhân nên chỉnh sửa nguồn Nix thay vào đó. Với nix-openclaw, hãy dùng [Bắt đầu nhanh](<https://github.com/openclaw/nix-openclaw#quick-start>) ưu tiên tác nhân và đặt cấu hình dưới `programs.openclaw.config` hoặc `instances.<name>.config`.
  * Các phụ thuộc bị thiếu hiển thị thông báo khắc phục dành riêng cho Nix
  * UI hiển thị banner chế độ Nix chỉ đọc


### Đường dẫn cấu hình và trạng thái

OpenClaw đọc cấu hình JSON5 từ `OPENCLAW_CONFIG_PATH` và lưu dữ liệu có thể thay đổi trong `OPENCLAW_STATE_DIR`. Khi chạy dưới Nix, hãy đặt rõ các giá trị này tới vị trí do Nix quản lý để trạng thái runtime và cấu hình không nằm trong kho bất biến.

Biến | Mặc định  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### Phát hiện PATH của dịch vụ

Dịch vụ gateway launchd/systemd tự động phát hiện các tệp nhị phân trong Nix-profile để các Plugin và công cụ gọi shell tới các tệp thực thi được cài bằng `nix` hoạt động mà không cần thiết lập PATH thủ công:

  * Khi `NIX_PROFILES` được đặt, mọi mục nhập được thêm vào PATH của dịch vụ theo thứ tự ưu tiên từ phải sang trái (khớp với mức ưu tiên shell Nix - mục ngoài cùng bên phải thắng).
  * Khi `NIX_PROFILES` chưa được đặt, `~/.nix-profile/bin` được thêm làm dự phòng.


Điều này áp dụng cho cả môi trường dịch vụ launchd trên macOS và systemd trên Linux.

## Liên quan

[**nix-openclaw** Mô-đun Home Manager nguồn sự thật và hướng dẫn thiết lập đầy đủ. ](<https://github.com/openclaw/nix-openclaw>) [**Setup wizard** Hướng dẫn từng bước thiết lập CLI không dùng Nix. ](</vi/start/wizard>) [**Docker** Thiết lập dạng container như một lựa chọn thay thế không dùng Nix. ](</vi/install/docker>) [**Updating** Cập nhật các bản cài đặt do Home Manager quản lý cùng với gói. ](</vi/install/updating>)

Was this useful?YesNo