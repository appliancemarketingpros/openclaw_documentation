---
title: DNS
source_url: https://docs.openclaw.ai/vi/cli/dns
scraped_at: 2026-05-25
---

# `openclaw dns`

Các trình hỗ trợ DNS cho khám phá diện rộng (Tailscale + CoreDNS). Hiện tập trung vào macOS + Homebrew CoreDNS.

Liên quan:

  * Khám phá Gateway: [Khám phá](</vi/gateway/discovery>)
  * Cấu hình khám phá diện rộng: [Cấu hình](</vi/gateway/configuration>)


## Thiết lập

bashCopy code
[code]
    openclaw dns setupopenclaw dns setup --domain openclaw.internalopenclaw dns setup --apply
[/code]

## `dns setup`

Lập kế hoạch hoặc áp dụng thiết lập CoreDNS cho khám phá DNS-SD unicast.

Tùy chọn:

  * `--domain <domain>`: domain khám phá diện rộng (ví dụ `openclaw.internal`)
  * `--apply`: cài đặt hoặc cập nhật cấu hình CoreDNS và khởi động lại dịch vụ (yêu cầu sudo; chỉ macOS)


Nội dung hiển thị:

  * domain khám phá đã phân giải
  * đường dẫn tệp vùng
  * các IP tailnet hiện tại
  * cấu hình khám phá `openclaw.json` được khuyến nghị
  * các giá trị nameserver/domain Split DNS của Tailscale cần đặt


Ghi chú:

  * Không có `--apply`, lệnh chỉ là trình hỗ trợ lập kế hoạch và in thiết lập được khuyến nghị.
  * Nếu bỏ qua `--domain`, OpenClaw dùng `discovery.wideArea.domain` từ cấu hình.
  * `--apply` hiện chỉ hỗ trợ macOS và yêu cầu Homebrew CoreDNS.
  * `--apply` khởi tạo tệp vùng nếu cần, bảo đảm stanza import của CoreDNS tồn tại, và khởi động lại dịch vụ brew `coredns`.


## Liên quan

  * [Tham chiếu CLI](</vi/cli>)
  * [Khám phá](</vi/gateway/discovery>)


Was this useful?YesNo