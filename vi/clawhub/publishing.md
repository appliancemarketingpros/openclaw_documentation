---
title: Xuất bản
source_url: https://docs.openclaw.ai/vi/clawhub/publishing
scraped_at: 2026-05-25
---

# Xuất bản

Việc xuất bản trên ClawHub được giới hạn theo chủ sở hữu: mỗi lần xuất bản đều nhắm đến một nhà phát hành, và máy chủ quyết định liệu người dùng đã đăng nhập có được phép xuất bản ở đó hay không.

## Chủ sở hữu

Chủ sở hữu là một định danh nhà phát hành trên ClawHub, chẳng hạn như `@alice` hoặc `@openclaw`. Chủ sở hữu cá nhân được tạo cho người dùng. Chủ sở hữu tổ chức có thể có nhiều thành viên.

Khi xuất bản, bạn dùng chủ sở hữu cá nhân của mình hoặc chọn một chủ sở hữu tổ chức nơi bạn có quyền truy cập nhà phát hành.

## Skills

Skills được xuất bản từ một thư mục skill. Trang công khai là:

textCopy code
[code]
    https://clawhub.ai/<owner>/<slug>
[/code]

Ví dụ:

textCopy code
[code]
    https://clawhub.ai/alice/review-helper
[/code]

Yêu cầu xuất bản bao gồm chủ sở hữu đã chọn, slug, phiên bản, nhật ký thay đổi và các tệp. Máy chủ xác minh rằng tác nhân có thể xuất bản với tư cách chủ sở hữu đó trước khi tạo bản phát hành.

Để chuyển một skill hiện có sang chủ sở hữu khác trong khi xuất bản phiên bản mới, hãy chọn chủ sở hữu mới và xác nhận rõ ràng việc chuyển quyền sở hữu. Trong CLI/API, truyền chủ sở hữu đích cùng tùy chọn tham gia di chuyển:

shCopy code
[code]
    clawhub skill publish ./review-helper --owner openclaw --migrate-owner --version 1.2.0
[/code]

Di chuyển chủ sở hữu skill yêu cầu quyền truy cập quản trị viên hoặc chủ sở hữu trên cả chủ sở hữu hiện tại và chủ sở hữu đích. Việc này giữ nguyên skill, lịch sử phiên bản, số liệu thống kê, bình luận, fork, bí danh và dấu vết kiểm tra; URL chủ sở hữu cũ tiếp tục hoạt động thông qua đường dẫn bí danh/chuyển hướng.

## Plugins

Plugins dùng tên gói kiểu npm. Tên gói có phạm vi bao gồm chủ sở hữu ở phần đầu tiên của tên:

textCopy code
[code]
    @owner/package-name
[/code]

Phạm vi phải khớp với chủ sở hữu xuất bản đã chọn. Nếu gói của bạn có tên `@openclaw/dronzer`, nó chỉ có thể được xuất bản dưới dạng `@openclaw`. Nếu bạn xuất bản dưới dạng `@vintageayu`, hãy đổi tên gói thành `@vintageayu/dronzer`.

Điều này ngăn một gói xác nhận không gian tên tổ chức mà nhà phát hành không kiểm soát.

## Luồng phát hành

  1. Giao diện người dùng, CLI hoặc quy trình GitHub thu thập siêu dữ liệu và tệp của gói.
  2. Yêu cầu xuất bản được gửi đến ClawHub với chủ sở hữu đã chọn.
  3. Máy chủ xác thực quyền của chủ sở hữu, phạm vi gói, tên gói, phiên bản, giới hạn tệp và siêu dữ liệu nguồn.
  4. ClawHub lưu trữ bản phát hành và bắt đầu các kiểm tra bảo mật tự động.
  5. Các bản phát hành mới bị ẩn khỏi các bề mặt cài đặt/tải xuống thông thường cho đến khi quá trình đánh giá và xác minh hoàn tất.


Nếu xác thực không thành công, bản phát hành sẽ không được tạo.

## Câu hỏi thường gặp

### Phạm vi gói phải khớp với chủ sở hữu đã chọn

Nếu phạm vi gói và chủ sở hữu đã chọn không khớp, ClawHub sẽ từ chối việc xuất bản:

textCopy code
[code]
    Package scope "@openclaw" must match selected owner "@vintageayu".Publish as "@openclaw" or rename this package to "@vintageayu/dronzer".
[/code]

Để khắc phục, hãy chọn chủ sở hữu được nêu trong phạm vi gói, hoặc đổi tên gói để phạm vi khớp với chủ sở hữu mà bạn có thể dùng để xuất bản.

Nếu tên gói đã có phạm vi đúng nhưng gói thuộc về nhà phát hành sai, hãy chuyển quyền sở hữu thay vào đó:

shCopy code
[code]
    clawhub package transfer @opik/opik-openclaw --to opik
[/code]

Chỉ dùng chuyển gói hoặc skill khi bạn có quyền truy cập quản trị viên vào cả chủ sở hữu hiện tại và nhà phát hành đích. Chuyển gói không cho phép bạn xuất bản vào một phạm vi mà bạn không thể quản lý.

Điều này bảo vệ không gian tên tổ chức. Một gói có tên `@openclaw/dronzer` xác nhận không gian tên `@openclaw`, vì vậy chỉ các nhà phát hành có quyền truy cập vào chủ sở hữu `@openclaw` mới có thể xuất bản gói đó.

Was this useful?YesNo