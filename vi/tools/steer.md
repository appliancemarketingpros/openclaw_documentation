---
title: Điều hướng
source_url: https://docs.openclaw.ai/vi/tools/steer
scraped_at: 2026-05-25
---

`/steer` gửi hướng dẫn đến một lượt chạy đang hoạt động. Lệnh này dành cho những thời điểm "điều chỉnh lượt chạy này trong khi nó vẫn đang hoạt động", không phải để bắt đầu một lượt mới.

## Phiên hiện tại

Dùng `/steer` cấp cao nhất để nhắm đến lượt chạy đang hoạt động cho phiên hiện tại:

textCopy code
[code]
    /steer prefer the smaller patch and keep the tests focused/tell summarize before making the next tool call
[/code]

Hành vi:

  * Chỉ nhắm đến lượt chạy đang hoạt động của phiên hiện tại.
  * Hoạt động độc lập với chế độ `/queue` của phiên.
  * Không bắt đầu một lượt chạy mới khi phiên đang rảnh.
  * Trả lời bằng cảnh báo khi không có lượt chạy đang hoạt động để điều hướng.
  * Dùng đường dẫn điều hướng của runtime đang hoạt động, vì vậy mô hình sẽ thấy hướng dẫn tại ranh giới runtime được hỗ trợ tiếp theo.


## Steer so với queue

`/queue steer` thay đổi cách các tin nhắn đến thông thường hoạt động khi chúng đến trong lúc một lượt chạy đang hoạt động. `/steer <message>` là một lệnh tường minh cố gắng chèn tin nhắn của lệnh đó vào lượt chạy đang hoạt động tại ranh giới runtime được hỗ trợ tiếp theo, bất kể thiết lập `/queue` đã lưu.

Dùng:

  * `/steer <message>` khi bạn muốn hướng dẫn lượt chạy đang hoạt động ngay bây giờ.
  * `/queue steer` khi bạn muốn các tin nhắn thông thường trong tương lai mặc định điều hướng các lượt chạy đang hoạt động.
  * `/queue collect` hoặc `/queue followup` khi tin nhắn mới nên chờ một lượt sau thay vì điều hướng lượt chạy đang hoạt động.


Để biết các chế độ hàng đợi và hành vi dự phòng, xem [Hàng đợi lệnh](</vi/concepts/queue>) và [Hàng đợi điều hướng](</vi/concepts/queue-steering>).

## Sub-agent

Dùng `/subagents steer` khi mục tiêu là một lượt chạy con:

textCopy code
[code]
    /subagents steer 2 focus only on the API surface
[/code]

`/steer` cấp cao nhất không chọn sub-agent theo id hoặc chỉ mục danh sách. Nó luôn nhắm đến lượt chạy đang hoạt động của phiên hiện tại. Xem [Sub-agent](</vi/tools/subagents>) để biết id, nhãn và lệnh điều khiển của sub-agent.

## Phiên ACP

Dùng `/acp steer` khi mục tiêu là một phiên harness ACP:

textCopy code
[code]
    /acp steer --session agent:main:acp:codex tighten the repro
[/code]

Xem [Agent ACP](</vi/tools/acp-agents>) để biết cách chọn phiên ACP và hành vi runtime.

## Liên quan

  * [Lệnh slash](</vi/tools/slash-commands>)
  * [Hàng đợi lệnh](</vi/concepts/queue>)
  * [Hàng đợi điều hướng](</vi/concepts/queue-steering>)
  * [Sub-agent](</vi/tools/subagents>)


Was this useful?YesNo