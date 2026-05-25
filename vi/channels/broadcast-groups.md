---
title: Nhóm phát sóng
source_url: https://docs.openclaw.ai/vi/channels/broadcast-groups
scraped_at: 2026-05-25
---

## Tổng quan

Nhóm phát sóng cho phép nhiều tác tử xử lý và phản hồi cùng một tin nhắn đồng thời. Điều này cho phép bạn tạo các nhóm tác tử chuyên biệt cùng làm việc trong một nhóm WhatsApp hoặc DM duy nhất — tất cả đều dùng một số điện thoại.

Phạm vi hiện tại: **chỉ WhatsApp** (kênh web).

Nhóm phát sóng được đánh giá sau danh sách cho phép của kênh và quy tắc kích hoạt nhóm. Trong các nhóm WhatsApp, điều này nghĩa là phát sóng diễn ra khi OpenClaw thường sẽ phản hồi (ví dụ: khi được nhắc đến, tùy thuộc vào cài đặt nhóm của bạn).

## Trường hợp sử dụng

1\. Nhóm tác tử chuyên biệt

Triển khai nhiều tác tử với các trách nhiệm nguyên tử, tập trung:

CodeCopy code
[code]
    Group: "Development Team"Agents:  - CodeReviewer (reviews code snippets)  - DocumentationBot (generates docs)  - SecurityAuditor (checks for vulnerabilities)  - TestGenerator (suggests test cases)
[/code]

Mỗi tác tử xử lý cùng một tin nhắn và đưa ra góc nhìn chuyên biệt của mình.

2\. Hỗ trợ đa ngôn ngữ CodeCopy code
[code]
    Group: "International Support"Agents:  - Agent_EN (responds in English)  - Agent_DE (responds in German)  - Agent_ES (responds in Spanish)
[/code]

3\. Quy trình đảm bảo chất lượng CodeCopy code
[code]
    Group: "Customer Support"Agents:  - SupportAgent (provides answer)  - QAAgent (reviews quality, only responds if issues found)
[/code]

4\. Tự động hóa tác vụ CodeCopy code
[code]
    Group: "Project Management"Agents:  - TaskTracker (updates task database)  - TimeLogger (logs time spent)  - ReportGenerator (creates summaries)
[/code]

## Cấu hình

### Thiết lập cơ bản

Thêm một phần `broadcast` cấp cao nhất (bên cạnh `bindings`). Các khóa là ID peer của WhatsApp:

  * trò chuyện nhóm: JID nhóm (ví dụ `120363403215116621@g.us`)
  * DM: số điện thoại E.164 (ví dụ `+15551234567`)

jsonCopy code
[code]
    {  "broadcast": {    "120363403215116621@g.us": ["alfred", "baerbel", "assistant3"]  }}
[/code]

**Kết quả:** Khi OpenClaw sẽ phản hồi trong cuộc trò chuyện này, nó sẽ chạy cả ba tác tử.

### Chiến lược xử lý

Kiểm soát cách tác tử xử lý tin nhắn:

### parallel (mặc định)

Tất cả tác tử xử lý đồng thời:

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### sequential

Tác tử xử lý theo thứ tự (mỗi tác tử chờ tác tử trước hoàn tất):

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### Ví dụ hoàn chỉnh

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "code-reviewer",        "name": "Code Reviewer",        "workspace": "/path/to/code-reviewer",        "sandbox": { "mode": "all" }      },      {        "id": "security-auditor",        "name": "Security Auditor",        "workspace": "/path/to/security-auditor",        "sandbox": { "mode": "all" }      },      {        "id": "docs-generator",        "name": "Documentation Generator",        "workspace": "/path/to/docs-generator",        "sandbox": { "mode": "all" }      }    ]  },  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["code-reviewer", "security-auditor", "docs-generator"],    "120363424282127706@g.us": ["support-en", "support-de"],    "+15555550123": ["assistant", "logger"]  }}
[/code]

## Cách hoạt động

### Luồng tin nhắn

* ### Tin nhắn đến

Một tin nhắn nhóm WhatsApp hoặc DM đến.

* ### Kiểm tra phát sóng

Hệ thống kiểm tra xem ID peer có trong `broadcast` hay không.

* ### Nếu có trong danh sách phát sóng

  * Tất cả tác tử được liệt kê xử lý tin nhắn.
  * Mỗi tác tử có khóa phiên riêng và ngữ cảnh tách biệt.
  * Tác tử xử lý song song (mặc định) hoặc tuần tự.


* ### Nếu không có trong danh sách phát sóng

Áp dụng định tuyến bình thường (binding khớp đầu tiên).

### Tách biệt phiên

Mỗi tác tử trong một nhóm phát sóng duy trì hoàn toàn riêng biệt:

  * **Khóa phiên** (`agent:alfred:whatsapp:group:120363...` so với `agent:baerbel:whatsapp:group:120363...`)
  * **Lịch sử hội thoại** (tác tử không thấy tin nhắn của các tác tử khác)
  * **Workspace** (sandbox riêng nếu được cấu hình)
  * **Quyền truy cập công cụ** (danh sách cho phép/từ chối khác nhau)
  * **Bộ nhớ/ngữ cảnh** ([IDENTITY.md](<http://IDENTITY.md>), [SOUL.md](<http://SOUL.md>), v.v. riêng)
  * **Bộ đệm ngữ cảnh nhóm** (các tin nhắn nhóm gần đây dùng làm ngữ cảnh) được chia sẻ theo từng peer, vì vậy tất cả tác tử phát sóng thấy cùng một ngữ cảnh khi được kích hoạt


Điều này cho phép mỗi tác tử có:

  * Tính cách khác nhau
  * Quyền truy cập công cụ khác nhau (ví dụ: chỉ đọc so với đọc-ghi)
  * Mô hình khác nhau (ví dụ: opus so với sonnet)
  * Skills khác nhau đã cài đặt


### Ví dụ: phiên tách biệt

Trong nhóm `120363403215116621@g.us` với các tác tử `["alfred", "baerbel"]`:

### Ngữ cảnh của Alfred

CodeCopy code
[code]
    Session: agent:alfred:whatsapp:group:120363403215116621@g.usHistory: [user message, alfred's previous responses]Workspace: /Users/user/openclaw-alfred/Tools: read, write, exec
[/code]

### Ngữ cảnh của Bärbel

CodeCopy code
[code]
    Session: agent:baerbel:whatsapp:group:120363403215116621@g.usHistory: [user message, baerbel's previous responses]Workspace: /Users/user/openclaw-baerbel/Tools: read only
[/code]

## Thực hành tốt nhất

1\. Giữ tác tử tập trung

Thiết kế mỗi tác tử với một trách nhiệm duy nhất, rõ ràng:

jsonCopy code
[code]
    {  "broadcast": {    "DEV_GROUP": ["formatter", "linter", "tester"]  }}
[/code]

✅ **Tốt:** Mỗi tác tử có một nhiệm vụ. ❌ **Không tốt:** Một tác tử "dev-helper" chung chung.

2\. Dùng tên mô tả rõ

Làm rõ mỗi tác tử làm gì:

jsonCopy code
[code]
    {  "agents": {    "security-scanner": { "name": "Security Scanner" },    "code-formatter": { "name": "Code Formatter" },    "test-generator": { "name": "Test Generator" }  }}
[/code]

3\. Cấu hình quyền truy cập công cụ khác nhau

Chỉ cấp cho tác tử những công cụ chúng cần:

jsonCopy code
[code]
    {  "agents": {    "reviewer": {      "tools": { "allow": ["read", "exec"] }    },    "fixer": {      "tools": { "allow": ["read", "write", "edit", "exec"] }    }  }}
[/code]

`reviewer` chỉ đọc. `fixer` có thể đọc và ghi.

4\. Giám sát hiệu năng

Với nhiều tác tử, hãy cân nhắc:

  * Dùng `"strategy": "parallel"` (mặc định) để tăng tốc độ
  * Giới hạn nhóm phát sóng ở 5-10 tác tử
  * Dùng mô hình nhanh hơn cho các tác tử đơn giản hơn

5\. Xử lý lỗi một cách mềm dẻo

Tác tử thất bại độc lập. Lỗi của một tác tử không chặn các tác tử khác:

CodeCopy code
[code]
    Message → [Agent A ✓, Agent B ✗ error, Agent C ✓]Result: Agent A and C respond, Agent B logs error
[/code]

## Khả năng tương thích

### Nhà cung cấp

Nhóm phát sóng hiện hoạt động với:

  * ✅ WhatsApp (đã triển khai)
  * 🚧 Telegram (đã lên kế hoạch)
  * 🚧 Discord (đã lên kế hoạch)
  * 🚧 Slack (đã lên kế hoạch)


### Định tuyến

Nhóm phát sóng hoạt động cùng với định tuyến hiện có:

jsonCopy code
[code]
    {  "bindings": [    {      "match": { "channel": "whatsapp", "peer": { "kind": "group", "id": "GROUP_A" } },      "agentId": "alfred"    }  ],  "broadcast": {    "GROUP_B": ["agent1", "agent2"]  }}
[/code]

  * `GROUP_A`: Chỉ alfred phản hồi (định tuyến bình thường).
  * `GROUP_B`: agent1 VÀ agent2 phản hồi (phát sóng).


## Khắc phục sự cố

Tác tử không phản hồi

**Kiểm tra:**

  1. ID tác tử tồn tại trong `agents.list`.
  2. Định dạng ID peer chính xác (ví dụ `120363403215116621@g.us`).
  3. Tác tử không nằm trong danh sách từ chối.


**Gỡ lỗi:**

bashCopy code
[code]
    tail -f ~/.openclaw/logs/gateway.log | grep broadcast
[/code]

Chỉ một tác tử phản hồi

**Nguyên nhân:** ID peer có thể nằm trong `bindings` nhưng không nằm trong `broadcast`.

**Cách sửa:** Thêm vào cấu hình phát sóng hoặc xóa khỏi bindings.

Vấn đề hiệu năng

Nếu chậm với nhiều tác tử:

  * Giảm số lượng tác tử trên mỗi nhóm.
  * Dùng mô hình nhẹ hơn (sonnet thay vì opus).
  * Kiểm tra thời gian khởi động sandbox.


## Ví dụ

Ví dụ 1: Nhóm đánh giá mã jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": [      "code-formatter",      "security-scanner",      "test-coverage",      "docs-checker"    ]  },  "agents": {    "list": [      {        "id": "code-formatter",        "workspace": "~/agents/formatter",        "tools": { "allow": ["read", "write"] }      },      {        "id": "security-scanner",        "workspace": "~/agents/security",        "tools": { "allow": ["read", "exec"] }      },      {        "id": "test-coverage",        "workspace": "~/agents/testing",        "tools": { "allow": ["read", "exec"] }      },      { "id": "docs-checker", "workspace": "~/agents/docs", "tools": { "allow": ["read"] } }    ]  }}
[/code]

**Người dùng gửi:** Đoạn mã.

**Phản hồi:**

  * code-formatter: "Đã sửa thụt lề và thêm gợi ý kiểu"
  * security-scanner: "⚠️ Lỗ hổng SQL injection ở dòng 12"
  * test-coverage: "Độ bao phủ là 45%, thiếu kiểm thử cho các trường hợp lỗi"
  * docs-checker: "Thiếu docstring cho hàm `process_data`"

Ví dụ 2: Hỗ trợ đa ngôn ngữ jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "+15555550123": ["detect-language", "translator-en", "translator-de"]  },  "agents": {    "list": [      { "id": "detect-language", "workspace": "~/agents/lang-detect" },      { "id": "translator-en", "workspace": "~/agents/translate-en" },      { "id": "translator-de", "workspace": "~/agents/translate-de" }    ]  }}
[/code]

## Tham chiếu API

### Lược đồ cấu hình

typescriptCopy code
[code]
    interface OpenClawConfig {  broadcast?: {    strategy?: "parallel" | "sequential";    [peerId: string]: string[];  };}
[/code]

### Trường

Cách xử lý tác tử. `parallel` chạy tất cả tác tử đồng thời; `sequential` chạy chúng theo thứ tự trong mảng.

JID nhóm WhatsApp, số E.164 hoặc ID peer khác. Giá trị là mảng ID tác tử sẽ xử lý tin nhắn.

## Hạn chế

  1. **Số tác tử tối đa:** Không có giới hạn cứng, nhưng 10+ tác tử có thể chậm.
  2. **Ngữ cảnh chia sẻ:** Tác tử không thấy phản hồi của nhau (theo thiết kế).
  3. **Thứ tự tin nhắn:** Phản hồi song song có thể đến theo bất kỳ thứ tự nào.
  4. **Giới hạn tốc độ:** Tất cả tác tử đều tính vào giới hạn tốc độ của WhatsApp.


## Cải tiến trong tương lai

Các tính năng đã lên kế hoạch:

  * [ ] Chế độ ngữ cảnh chia sẻ (tác tử thấy phản hồi của nhau)
  * [ ] Điều phối tác tử (tác tử có thể gửi tín hiệu cho nhau)
  * [ ] Chọn tác tử động (chọn tác tử dựa trên nội dung tin nhắn)
  * [ ] Mức ưu tiên tác tử (một số tác tử phản hồi trước các tác tử khác)


## Liên quan

  * [Định tuyến kênh](</vi/channels/channel-routing>)
  * [Nhóm](</vi/channels/groups>)
  * [Công cụ môi trường cách ly đa tác nhân](</vi/tools/multi-agent-sandbox-tools>)
  * [Ghép nối](</vi/channels/pairing>)
  * [Quản lý phiên](</vi/concepts/session>)


Was this useful?YesNo