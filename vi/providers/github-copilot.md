---
title: GitHub Copilot
source_url: https://docs.openclaw.ai/vi/providers/github-copilot
scraped_at: 2026-05-25
---

GitHub Copilot là trợ lý lập trình AI của GitHub. Nó cung cấp quyền truy cập vào các mô hình Copilot cho tài khoản và gói GitHub của bạn. OpenClaw có thể dùng Copilot làm nhà cung cấp mô hình theo hai cách khác nhau.

## Hai cách dùng Copilot trong OpenClaw

### Built-in provider (github-copilot)

Dùng luồng đăng nhập thiết bị gốc để lấy token GitHub, rồi trao đổi token đó lấy token API Copilot khi OpenClaw chạy. Đây là đường dẫn **mặc định** và đơn giản nhất vì không yêu cầu VS Code.

* ### Run the login command

bashCopy code
[code]
    openclaw models auth login-github-copilot
[/code]

Bạn sẽ được nhắc truy cập một URL và nhập mã dùng một lần. Giữ terminal mở cho đến khi hoàn tất.

* ### Set a default model

bashCopy code
[code]
    openclaw models set github-copilot/claude-opus-4.7
[/code]

Hoặc trong cấu hình:

json5Copy code
[code]
    {  agents: {    defaults: { model: { primary: "github-copilot/claude-opus-4.7" } },  },}
[/code]

### Copilot Proxy plugin (copilot-proxy)

Dùng tiện ích VS Code **Copilot Proxy** làm cầu nối cục bộ. OpenClaw giao tiếp với endpoint `/v1` của proxy và dùng danh sách mô hình bạn cấu hình ở đó.

## Cờ tùy chọn

Cờ | Mô tả  
---|---  
`--yes` | Bỏ qua lời nhắc xác nhận  
`--set-default` | Đồng thời áp dụng mô hình mặc định được nhà cung cấp khuyến nghị  
bashCopy code
[code]
    # Skip confirmationopenclaw models auth login-github-copilot --yes # Login and set the default model in one stepopenclaw models auth login --provider github-copilot --method device --set-default
[/code]

## Thiết lập ban đầu không tương tác

Nếu bạn đã có token truy cập GitHub OAuth cho Copilot, hãy nhập token đó trong quá trình thiết lập không có giao diện với `openclaw onboard --non-interactive`:

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --auth-choice github-copilot \  --github-copilot-token "$COPILOT_GITHUB_TOKEN" \  --skip-channels --skip-health
[/code]

Bạn cũng có thể bỏ qua `--auth-choice`; truyền `--github-copilot-token` sẽ suy ra lựa chọn xác thực nhà cung cấp GitHub Copilot. Nếu cờ này bị bỏ qua, quá trình thiết lập ban đầu sẽ dự phòng lần lượt về `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, rồi `GITHUB_TOKEN`. Dùng `--secret-input-mode ref` với `COPILOT_GITHUB_TOKEN` được đặt để lưu `tokenRef` được hỗ trợ bằng biến môi trường thay vì văn bản thuần trong `auth-profiles.json`.

Interactive TTY required

Luồng đăng nhập thiết bị yêu cầu TTY tương tác. Hãy chạy trực tiếp trong terminal, không chạy trong script không tương tác hoặc pipeline CI.

Model availability depends on your plan

Tính khả dụng của mô hình Copilot phụ thuộc vào gói GitHub của bạn. Nếu một mô hình bị từ chối, hãy thử ID khác (ví dụ `github-copilot/gpt-4.1`).

Live catalog refresh from the Copilot API

Sau khi đường dẫn xác thực đăng nhập thiết bị (hoặc biến môi trường) đã phân giải được token GitHub, OpenClaw làm mới danh mục mô hình theo yêu cầu từ `${baseUrl}/models` (cùng endpoint mà VS Code Copilot dùng), để runtime theo dõi quyền dùng theo từng tài khoản và cửa sổ ngữ cảnh chính xác mà không cần thay đổi manifest. Các mô hình Copilot mới phát hành sẽ hiển thị mà không cần nâng cấp OpenClaw, và cửa sổ ngữ cảnh phản ánh giới hạn thực theo từng mô hình (ví dụ 400k cho dòng gpt-5.x, 1M cho các biến thể nội bộ `claude-opus-*-1m`).

Danh mục tĩnh đi kèm vẫn là phương án dự phòng hiển thị khi discovery bị tắt, người dùng không có hồ sơ xác thực GitHub, quá trình trao đổi token thất bại, hoặc lệnh gọi HTTPS tới `/models` gặp lỗi. Để chọn không tham gia và chỉ dựa hoàn toàn vào danh mục manifest tĩnh (các kịch bản ngoại tuyến / tách biệt mạng):

json5Copy code
[code]
    {  plugins: {    entries: {      "github-copilot": {        config: { discovery: { enabled: false } },      },    },  },}
[/code]

Transport selection

ID mô hình Claude tự động dùng transport Anthropic Messages. Các mô hình GPT, o-series và Gemini giữ transport OpenAI Responses. OpenClaw chọn transport đúng dựa trên tham chiếu mô hình.

Request compatibility

OpenClaw gửi các header yêu cầu kiểu IDE Copilot trên các transport Copilot, bao gồm các lượt Compaction tích hợp, kết quả công cụ và theo dõi hình ảnh. Nó không bật tiếp nối Responses cấp nhà cung cấp cho Copilot trừ khi hành vi đó đã được xác minh với API của Copilot.

Environment variable resolution order

OpenClaw phân giải xác thực Copilot từ các biến môi trường theo thứ tự ưu tiên sau:

Mức ưu tiên | Biến | Ghi chú  
---|---|---  
1 | `COPILOT_GITHUB_TOKEN` | Ưu tiên cao nhất, dành riêng cho Copilot  
2 | `GH_TOKEN` | Token GitHub CLI (dự phòng)  
3 | `GITHUB_TOKEN` | Token GitHub tiêu chuẩn (thấp nhất)  
  
Khi nhiều biến được đặt, OpenClaw dùng biến có mức ưu tiên cao nhất. Luồng đăng nhập thiết bị (`openclaw models auth login-github-copilot`) lưu token của nó trong kho hồ sơ xác thực và được ưu tiên hơn tất cả biến môi trường.

Token storage

Lệnh đăng nhập lưu token GitHub trong kho hồ sơ xác thực và trao đổi token đó lấy token API Copilot khi OpenClaw chạy. Bạn không cần quản lý token theo cách thủ công.

## Embedding cho tìm kiếm bộ nhớ

GitHub Copilot cũng có thể đóng vai trò nhà cung cấp embedding cho [tìm kiếm bộ nhớ](</vi/concepts/memory-search>). Nếu bạn có đăng ký Copilot và đã đăng nhập, OpenClaw có thể dùng nó cho embedding mà không cần khóa API riêng.

### Tự động phát hiện

Khi `memorySearch.provider` là `"auto"` (mặc định), GitHub Copilot được thử ở mức ưu tiên 15 -- sau embedding cục bộ nhưng trước OpenAI và các nhà cung cấp trả phí khác. Nếu có token GitHub, OpenClaw khám phá các mô hình embedding có sẵn từ API Copilot và tự động chọn mô hình tốt nhất.

### Cấu hình rõ ràng

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "github-copilot",        // Optional: override the auto-discovered model        model: "text-embedding-3-small",      },    },  },}
[/code]

### Cách hoạt động

  1. OpenClaw phân giải token GitHub của bạn (từ biến môi trường hoặc hồ sơ xác thực).
  2. Trao đổi token đó lấy token API Copilot có thời hạn ngắn.
  3. Truy vấn endpoint `/models` của Copilot để khám phá các mô hình embedding có sẵn.
  4. Chọn mô hình tốt nhất (ưu tiên `text-embedding-3-small`).
  5. Gửi yêu cầu embedding tới endpoint `/embeddings` của Copilot.


Tính khả dụng của mô hình phụ thuộc vào gói GitHub của bạn. Nếu không có mô hình embedding nào khả dụng, OpenClaw bỏ qua Copilot và thử nhà cung cấp tiếp theo.

## Liên quan

[**Model selection** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**OAuth and auth** Chi tiết xác thực và quy tắc tái sử dụng thông tin đăng nhập. ](</vi/gateway/authentication>)

Was this useful?YesNo