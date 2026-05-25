---
title: OpenAI
source_url: https://docs.openclaw.ai/vi/providers/openai
scraped_at: 2026-05-25
---

OpenAI cung cấp API cho nhà phát triển cho các mô hình GPT, và Codex cũng có sẵn dưới dạng tác tử lập trình theo gói ChatGPT thông qua các client Codex của OpenAI. OpenClaw giữ các bề mặt này tách biệt để cấu hình luôn dễ dự đoán.

OpenClaw dùng `openai/*` làm tuyến mô hình OpenAI chuẩn. Các lượt tác tử nhúng trên mô hình OpenAI chạy qua runtime app-server Codex gốc theo mặc định; xác thực bằng khóa API OpenAI trực tiếp vẫn có sẵn cho các bề mặt OpenAI không phải tác tử như hình ảnh, embeddings, giọng nói và realtime.

  * **Mô hình tác tử** \- các mô hình `openai/*` thông qua runtime Codex; đăng nhập bằng xác thực Codex để dùng gói đăng ký ChatGPT/Codex, hoặc cấu hình một bản dự phòng khóa API OpenAI tương thích với Codex khi bạn chủ ý muốn xác thực bằng khóa API.
  * **API OpenAI không phải tác tử** \- truy cập OpenAI Platform trực tiếp với tính phí theo mức sử dụng thông qua `OPENAI_API_KEY` hoặc onboarding khóa API OpenAI.
  * **Cấu hình cũ** \- các tham chiếu mô hình `openai-codex/*` được sửa bởi `openclaw doctor --fix` thành `openai/*` cộng với runtime Codex.


OpenAI hỗ trợ rõ ràng việc dùng OAuth theo gói đăng ký trong các công cụ và workflow bên ngoài như OpenClaw.

Nhà cung cấp, mô hình, runtime và kênh là các lớp riêng biệt. Nếu các nhãn đó đang bị trộn lẫn với nhau, hãy đọc [Runtime tác tử](</vi/concepts/agent-runtimes>) trước khi thay đổi cấu hình.

## Lựa chọn nhanh

Mục tiêu | Dùng | Ghi chú  
---|---|---  
Gói đăng ký ChatGPT/Codex với runtime Codex gốc | `openai/gpt-5.5` | Thiết lập tác tử OpenAI mặc định. Đăng nhập bằng xác thực Codex.  
Tính phí khóa API trực tiếp cho mô hình tác tử | `openai/gpt-5.5` cộng với hồ sơ khóa API tương thích Codex | Dùng `auth.order.openai` để đặt bản dự phòng sau xác thực gói đăng ký.  
Tính phí khóa API trực tiếp qua PI rõ ràng | `openai/gpt-5.5` cộng với runtime nhà cung cấp/mô hình `pi` | Chọn một hồ sơ khóa API `openai` thông thường.  
Bí danh API ChatGPT Instant mới nhất | `openai/chat-latest` | Chỉ dùng khóa API trực tiếp. Bí danh di động cho thử nghiệm, không phải mặc định.  
Xác thực gói đăng ký ChatGPT/Codex qua PI rõ ràng | `openai/gpt-5.5` cộng với runtime nhà cung cấp/mô hình `pi` | Chọn một hồ sơ xác thực `openai-codex` cho tuyến tương thích.  
Tạo hoặc chỉnh sửa hình ảnh | `openai/gpt-image-2` | Hoạt động với `OPENAI_API_KEY` hoặc OAuth OpenAI Codex.  
Hình ảnh nền trong suốt | `openai/gpt-image-1.5` | Dùng `outputFormat=png` hoặc `webp` và `openai.background=transparent`.  
  
## Bản đồ tên gọi

Các tên tương tự nhau nhưng không thể thay thế cho nhau:

Tên bạn thấy | Lớp | Ý nghĩa  
---|---|---  
`openai` | Tiền tố nhà cung cấp | Tuyến mô hình OpenAI chuẩn; các lượt tác tử dùng runtime Codex.  
`openai-codex` | Tiền tố xác thực/hồ sơ cũ | Namespace hồ sơ OAuth/gói đăng ký OpenAI Codex cũ hơn. Các hồ sơ hiện có và `auth.order.openai-codex` vẫn hoạt động.  
Plugin `codex` | Plugin | Plugin OpenClaw đi kèm cung cấp runtime app-server Codex gốc và điều khiển chat `/codex`.  
provider/model `agentRuntime.id: codex` | Runtime tác tử | Buộc dùng harness app-server Codex gốc cho các lượt nhúng khớp.  
`/codex ...` | Bộ lệnh chat | Ràng buộc/điều khiển các luồng app-server Codex từ một cuộc hội thoại.  
`runtime: "acp", agentId: "codex"` | Tuyến phiên ACP | Đường dự phòng rõ ràng chạy Codex thông qua ACP/acpx.  
  
Điều này có nghĩa là một cấu hình có thể chủ ý chứa các tham chiếu mô hình `openai/*` trong khi các hồ sơ xác thực vẫn trỏ đến thông tin xác thực tương thích với Codex. Ưu tiên `auth.order.openai` cho cấu hình mới; các hồ sơ `openai-codex:*` hiện có và `auth.order.openai-codex` vẫn được hỗ trợ. `openclaw doctor --fix` ghi lại các tham chiếu mô hình cũ `openai-codex/*` sang tuyến mô hình OpenAI chuẩn.

## Phạm vi tính năng OpenClaw

Năng lực OpenAI | Bề mặt OpenClaw | Trạng thái  
---|---|---  
Chat / Responses | Nhà cung cấp mô hình `openai/<model>` | Có  
Mô hình gói đăng ký Codex | `openai/<model>` với OAuth `openai-codex` | Có  
Tham chiếu mô hình Codex cũ | `openai-codex/<model>` | Được doctor sửa thành `openai/<model>`  
Harness app-server Codex | `openai/<model>` với runtime bị bỏ qua hoặc provider/model `agentRuntime.id: codex` | Có  
Tìm kiếm web phía server | Công cụ OpenAI Responses gốc | Có, khi tìm kiếm web được bật và không ghim nhà cung cấp  
Hình ảnh | `image_generate` | Có  
Video | `video_generate` | Có  
Chuyển văn bản thành giọng nói | `messages.tts.provider: "openai"` / `tts` | Có  
Chuyển giọng nói thành văn bản theo lô | `tools.media.audio` / hiểu media | Có  
Chuyển giọng nói thành văn bản streaming | Voice Call `streaming.provider: "openai"` | Có  
Giọng nói realtime | Voice Call `realtime.provider: "openai"` / Control UI Talk | Có  
Embeddings | Nhà cung cấp embedding bộ nhớ | Có  
  
## Embeddings bộ nhớ

OpenClaw có thể dùng OpenAI, hoặc một endpoint embedding tương thích OpenAI, cho việc lập chỉ mục `memory_search` và embeddings truy vấn:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        model: "text-embedding-3-small",      },    },  },}
[/code]

Với các endpoint tương thích OpenAI yêu cầu nhãn embedding bất đối xứng, đặt `queryInputType` và `documentInputType` bên dưới `memorySearch`. OpenClaw chuyển tiếp chúng dưới dạng các trường yêu cầu `input_type` dành riêng cho nhà cung cấp: embeddings truy vấn dùng `queryInputType`; các đoạn bộ nhớ đã lập chỉ mục và lập chỉ mục theo lô dùng `documentInputType`. Xem [Tham chiếu cấu hình bộ nhớ](</vi/reference/memory-config#provider-specific-config>) để biết ví dụ đầy đủ.

## Bắt đầu

Chọn phương thức xác thực bạn ưu tiên và làm theo các bước thiết lập.

### Khóa API (OpenAI Platform)

**Phù hợp nhất cho:** truy cập API trực tiếp và tính phí theo mức sử dụng.

* ### Lấy khóa API của bạn

Tạo hoặc sao chép một khóa API từ [bảng điều khiển OpenAI Platform](<https://platform.openai.com/api-keys>).

* ### Chạy onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice openai-api-key
[/code]

Hoặc truyền khóa trực tiếp:

bashCopy code
[code]
    openclaw onboard --openai-api-key "$OPENAI_API_KEY"
[/code]

* ### Xác minh mô hình có sẵn

bashCopy code
[code]
    openclaw models list --provider openai
[/code]

### Tóm tắt tuyến

Tham chiếu mô hình | Cấu hình runtime | Tuyến | Xác thực  
---|---|---|---  
`openai/gpt-5.5` | bị bỏ qua / provider/model `agentRuntime.id: "codex"` | Harness app-server Codex | Hồ sơ OpenAI tương thích Codex  
`openai/gpt-5.4-mini` | bị bỏ qua / provider/model `agentRuntime.id: "codex"` | Harness app-server Codex | Hồ sơ OpenAI tương thích Codex  
`openai/gpt-5.5` | provider/model `agentRuntime.id: "pi"` | Runtime nhúng PI | Hồ sơ `openai` hoặc hồ sơ `openai-codex` đã chọn  
  
### Ví dụ cấu hình

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "openai/gpt-5.5" } } },}
[/code]

Để thử mô hình Instant hiện tại của ChatGPT từ OpenAI API, đặt mô hình thành `openai/chat-latest`:

json5Copy code
[code]
    {  env: { OPENAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "openai/chat-latest" } } },}
[/code]

`chat-latest` là một bí danh di động. OpenAI mô tả nó là mô hình Instant mới nhất được dùng trong ChatGPT và khuyến nghị `gpt-5.5` cho việc dùng API sản xuất, vì vậy hãy giữ `openai/gpt-5.5` làm mặc định ổn định trừ khi bạn chủ ý muốn hành vi của bí danh đó. Bí danh hiện chỉ chấp nhận độ dài văn bản `medium`, nên OpenClaw chuẩn hóa các override độ dài văn bản OpenAI không tương thích cho mô hình này.

### Đăng ký Codex

**Phù hợp nhất cho:** sử dụng gói đăng ký ChatGPT/Codex của bạn với cách thực thi app-server Codex gốc thay vì một API key riêng. Đám mây Codex yêu cầu đăng nhập ChatGPT.

* ### Chạy Codex OAuth

bashCopy code
[code]
    openclaw onboard --auth-choice openai-codex
[/code]

Hoặc chạy OAuth trực tiếp:

bashCopy code
[code]
    openclaw models auth login --provider openai-codex
[/code]

Với các thiết lập headless hoặc không thuận lợi cho callback, hãy thêm `--device-code` để đăng nhập bằng luồng mã thiết bị ChatGPT thay vì callback trình duyệt localhost:

bashCopy code
[code]
    openclaw models auth login --provider openai-codex --device-code
[/code]

* ### Dùng tuyến model OpenAI chuẩn

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary openai/gpt-5.5
[/code]

Đường dẫn mặc định không yêu cầu cấu hình runtime. Các lượt tác nhân OpenAI tự động chọn runtime app-server Codex gốc, và OpenClaw cài đặt hoặc sửa chữa plugin Codex đi kèm khi tuyến này được chọn.

* ### Xác minh Codex auth khả dụng

bashCopy code
[code]
    openclaw models list --provider openai-codex
[/code]

Sau khi gateway đang chạy, hãy gửi `/codex status` hoặc `/codex models` trong chat để xác minh runtime app-server gốc.

### Tóm tắt tuyến

Tham chiếu model | Cấu hình runtime | Tuyến | Xác thực  
---|---|---|---  
`openai/gpt-5.5` | bỏ qua / provider/model `agentRuntime.id: "codex"` | Bộ harness app-server Codex gốc | Đăng nhập Codex hoặc hồ sơ xác thực `openai` theo thứ tự  
`openai/gpt-5.5` | provider/model `agentRuntime.id: "pi"` | Runtime nhúng PI với transport Codex-auth nội bộ | Hồ sơ `openai-codex` đã chọn  
`openai-codex/gpt-5.5` | được doctor sửa chữa | Tuyến cũ được viết lại thành `openai/gpt-5.5` | Hồ sơ `openai-codex` hiện có  
  
### Ví dụ cấu hình

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },}
[/code]

Với API-key dự phòng, hãy giữ model ở `openai/gpt-5.5` và đặt thứ tự auth dưới `openai`. OpenClaw sẽ thử gói đăng ký trước, sau đó API key, đồng thời vẫn ở trên harness Codex:

json5Copy code
[code]
    {  plugins: { entries: { codex: { enabled: true } } },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },    },  },  auth: {    order: {      openai: [        "openai-codex:user@example.com",        "openai:api-key-backup",      ],    },  },}
[/code]

### Kiểm tra và khôi phục định tuyến Codex OAuth

Dùng các lệnh này để xem model, runtime và tuyến auth nào mà tác nhân mặc định của bạn đang sử dụng:

bashCopy code
[code]
    openclaw models statusopenclaw models auth list --provider openai-codexopenclaw config get agents.defaults.model --jsonopenclaw config get models.providers.openai.agentRuntime --json
[/code]

Với một tác nhân cụ thể, hãy thêm `--agent <id>`:

bashCopy code
[code]
    openclaw models status --agent <id>openclaw models auth list --agent <id> --provider openai-codex
[/code]

Nếu cấu hình cũ hơn vẫn có `openai-codex/gpt-*` hoặc một ghim phiên OpenAI PI lỗi thời mà không có cấu hình runtime rõ ràng, hãy sửa chữa nó:

bashCopy code
[code]
    openclaw doctor --fixopenclaw config validate
[/code]

Nếu `models auth list --provider openai-codex` không hiển thị hồ sơ khả dụng nào, hãy đăng nhập lại:

bashCopy code
[code]
    openclaw models auth login --provider openai-codexopenclaw models status --probe --probe-provider openai-codex
[/code]

`openai/*` là tuyến model cho các lượt tác nhân OpenAI thông qua Codex. Id nhà cung cấp auth/hồ sơ `openai-codex` vẫn được chấp nhận cho các hồ sơ hiện có và danh sách CLI.

### Chỉ báo trạng thái

Chat `/status` hiển thị runtime model nào đang hoạt động cho phiên hiện tại. Harness app-server Codex đi kèm xuất hiện dưới dạng `Runtime: OpenAI Codex` cho các lượt model tác nhân OpenAI. Các ghim phiên PI lỗi thời được sửa chữa thành Codex trừ khi cấu hình ghim PI rõ ràng.

### Cảnh báo doctor

Nếu các tuyến `openai-codex/*` hoặc ghim OpenAI PI lỗi thời vẫn còn trong cấu hình hoặc trạng thái phiên, `openclaw doctor --fix` sẽ viết lại chúng thành `openai/*` với runtime Codex trừ khi PI được cấu hình rõ ràng.

### Giới hạn cửa sổ ngữ cảnh

OpenClaw xử lý metadata model và giới hạn ngữ cảnh runtime như các giá trị riêng biệt.

Với `openai/gpt-5.5` thông qua catalog Codex OAuth:

  * `contextWindow` gốc: `1000000`
  * Giới hạn `contextTokens` runtime mặc định: `272000`


Giới hạn mặc định nhỏ hơn có đặc tính độ trễ và chất lượng tốt hơn trong thực tế. Ghi đè nó bằng `contextTokens`:

json5Copy code
[code]
    {  models: {    providers: {      "openai-codex": {        models: [{ id: "gpt-5.5", contextTokens: 160000 }],      },    },  },}
[/code]

### Khôi phục catalog

OpenClaw dùng metadata catalog Codex upstream cho `gpt-5.5` khi nó có mặt. Nếu quá trình khám phá Codex trực tiếp bỏ qua hàng `gpt-5.5` trong khi tài khoản đã được xác thực, OpenClaw tổng hợp hàng model OAuth đó để cron, tác nhân phụ và các lượt chạy default-model đã cấu hình không thất bại với `Unknown model`.

## Xác thực app-server Codex gốc

Harness app-server Codex gốc dùng các tham chiếu model `openai/*` kèm cấu hình runtime bị bỏ qua hoặc provider/model `agentRuntime.id: "codex"`, nhưng auth của nó vẫn dựa trên tài khoản. OpenClaw chọn auth theo thứ tự này:

  1. Các hồ sơ auth OpenAI theo thứ tự cho tác nhân, ưu tiên dưới `auth.order.openai`. Các hồ sơ `openai-codex:*` hiện có và `auth.order.openai-codex` vẫn hợp lệ cho bản cài đặt cũ hơn.
  2. Tài khoản hiện có của app-server, chẳng hạn như đăng nhập ChatGPT bằng Codex CLI cục bộ.
  3. Chỉ với các lần khởi chạy app-server stdio cục bộ, `CODEX_API_KEY`, sau đó `OPENAI_API_KEY`, khi app-server báo cáo không có tài khoản và vẫn yêu cầu OpenAI auth.


Điều đó có nghĩa là đăng nhập đăng ký ChatGPT/Codex cục bộ không bị thay thế chỉ vì tiến trình gateway cũng có `OPENAI_API_KEY` cho các model OpenAI trực tiếp hoặc embeddings. Dự phòng API-key qua env chỉ là đường dẫn stdio cục bộ không có tài khoản; nó không được gửi đến các kết nối app-server WebSocket. Khi một hồ sơ Codex kiểu đăng ký được chọn, OpenClaw cũng giữ `CODEX_API_KEY` và `OPENAI_API_KEY` khỏi tiến trình con app-server stdio được tạo và gửi thông tin đăng nhập đã chọn thông qua RPC đăng nhập app-server. Khi hồ sơ đăng ký đó bị chặn bởi một giới hạn sử dụng Codex, OpenClaw có thể xoay sang hồ sơ API-key `openai:*` theo thứ tự tiếp theo mà không thay đổi model đã chọn hoặc rời khỏi harness Codex. Sau khi thời gian đặt lại đăng ký trôi qua, hồ sơ đăng ký lại đủ điều kiện.

## Tạo hình ảnh

Plugin `openai` đi kèm đăng ký tạo hình ảnh thông qua công cụ `image_generate`. Nó hỗ trợ cả tạo hình ảnh bằng OpenAI API-key và tạo hình ảnh bằng Codex OAuth thông qua cùng tham chiếu model `openai/gpt-image-2`.

Khả năng | OpenAI API key | Codex OAuth  
---|---|---  
Tham chiếu model | `openai/gpt-image-2` | `openai/gpt-image-2`  
Xác thực | `OPENAI_API_KEY` | Đăng nhập OpenAI Codex OAuth  
Transport | OpenAI Images API | Backend Codex Responses  
Số hình ảnh tối đa mỗi yêu cầu | 4 | 4  
Chế độ chỉnh sửa | Đã bật (tối đa 5 hình ảnh tham chiếu) | Đã bật (tối đa 5 hình ảnh tham chiếu)  
Ghi đè kích thước | Được hỗ trợ, bao gồm kích thước 2K/4K | Được hỗ trợ, bao gồm kích thước 2K/4K  
Tỷ lệ khung hình / độ phân giải | Không chuyển tiếp đến OpenAI Images API | Được ánh xạ tới kích thước được hỗ trợ khi an toàn  
json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: { primary: "openai/gpt-image-2" },    },  },}
[/code]

`gpt-image-2` là mặc định cho cả tạo hình ảnh từ văn bản OpenAI và chỉnh sửa hình ảnh. `gpt-image-1.5`, `gpt-image-1` và `gpt-image-1-mini` vẫn có thể dùng như các ghi đè model rõ ràng. Dùng `openai/gpt-image-1.5` cho đầu ra PNG/WebP nền trong suốt; API `gpt-image-2` hiện tại từ chối `background: "transparent"`.

Với yêu cầu nền trong suốt, tác nhân nên gọi `image_generate` với `model: "openai/gpt-image-1.5"`, `outputFormat: "png"` hoặc `"webp"`, và `background: "transparent"`; tùy chọn nhà cung cấp `openai.background` cũ hơn vẫn được chấp nhận. OpenClaw cũng bảo vệ các tuyến OpenAI công khai và OpenAI Codex OAuth bằng cách viết lại các yêu cầu trong suốt mặc định `openai/gpt-image-2` thành `gpt-image-1.5`; Azure và các endpoint tương thích OpenAI tùy chỉnh giữ nguyên tên deployment/model đã cấu hình của chúng.

Thiết lập tương tự được cung cấp cho các lượt chạy CLI headless:

bashCopy code
[code]
    openclaw infer image generate \  --model openai/gpt-image-1.5 \  --output-format png \  --background transparent \  --prompt "A simple red circle sticker on a transparent background" \  --json
[/code]

Dùng cùng các cờ `--output-format` và `--background` với `openclaw infer image edit` khi bắt đầu từ một tệp đầu vào. `--openai-background` vẫn khả dụng dưới dạng alias riêng cho OpenAI.

Với các bản cài đặt Codex OAuth, hãy giữ cùng tham chiếu `openai/gpt-image-2`. Khi một hồ sơ OAuth `openai-codex` được cấu hình, OpenClaw phân giải OAuth access token đã lưu đó và gửi yêu cầu hình ảnh qua backend Codex Responses. Nó không thử `OPENAI_API_KEY` trước hoặc âm thầm chuyển về một API key cho yêu cầu đó. Hãy cấu hình `models.providers.openai` rõ ràng bằng API key, URL cơ sở tùy chỉnh hoặc endpoint Azure khi bạn muốn tuyến OpenAI Images API trực tiếp thay thế. Nếu endpoint hình ảnh tùy chỉnh đó nằm trên LAN/địa chỉ riêng đáng tin cậy, cũng đặt `browser.ssrfPolicy.dangerouslyAllowPrivateNetwork: true`; OpenClaw giữ các endpoint hình ảnh tương thích OpenAI riêng tư/nội bộ bị chặn trừ khi lựa chọn tham gia này có mặt.

Tạo:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="A polished launch poster for OpenClaw on macOS" size=3840x2160 count=1
[/code]

Tạo PNG trong suốt:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

Chỉnh sửa:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2 prompt="Preserve the object shape, change the material to translucent glass" image=/path/to/reference.png size=1024x1536
[/code]

## Tạo video

Plugin `openai` được đóng gói kèm đăng ký tạo video thông qua công cụ `video_generate`.

Khả năng | Giá trị  
---|---  
Mô hình mặc định | `openai/sora-2`  
Chế độ | Văn bản-thành-video, hình ảnh-thành-video, chỉnh sửa một video  
Đầu vào tham chiếu | 1 hình ảnh hoặc 1 video  
Ghi đè kích thước | Được hỗ trợ  
Ghi đè khác | `aspectRatio`, `resolution`, `audio`, `watermark` bị bỏ qua kèm cảnh báo công cụ  
json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "openai/sora-2" },    },  },}
[/code]

## Đóng góp lời nhắc GPT-5

OpenClaw thêm một đóng góp lời nhắc GPT-5 dùng chung cho các lượt chạy thuộc họ GPT-5 trên nhiều nhà cung cấp. Nó áp dụng theo mã định danh mô hình, nên `openai/gpt-5.5`, các tham chiếu cũ trước khi sửa chữa như `openai-codex/gpt-5.5`, `openrouter/openai/gpt-5.5`, `opencode/gpt-5.5`, và các tham chiếu GPT-5 tương thích khác đều nhận cùng một lớp phủ. Các mô hình GPT-4.x cũ hơn thì không.

Bộ khai thác Codex gốc được đóng gói kèm sử dụng cùng hành vi GPT-5 và lớp phủ Heartbeat thông qua chỉ dẫn dành cho nhà phát triển của máy chủ ứng dụng Codex, nên các phiên `openai/gpt-5.x` được định tuyến qua Codex vẫn giữ cùng hướng dẫn theo đến cùng và Heartbeat chủ động, dù Codex sở hữu phần còn lại của lời nhắc bộ khai thác.

Đóng góp GPT-5 thêm một hợp đồng hành vi có gắn thẻ cho việc duy trì persona, an toàn thực thi, kỷ luật công cụ, hình dạng đầu ra, kiểm tra hoàn tất và xác minh. Hành vi trả lời theo kênh và tin nhắn im lặng vẫn nằm trong lời nhắc hệ thống OpenClaw dùng chung và chính sách gửi đi. Hướng dẫn GPT-5 luôn được bật cho các mô hình khớp. Lớp kiểu tương tác thân thiện là riêng biệt và có thể cấu hình.

Giá trị | Hiệu ứng  
---|---  
`"friendly"` (mặc định) | Bật lớp kiểu tương tác thân thiện  
`"on"` | Bí danh cho `"friendly"`  
`"off"` | Chỉ tắt lớp kiểu thân thiện  
  
### Config

json5Copy code
[code]
    {  agents: {    defaults: {      promptOverlays: {        gpt5: { personality: "friendly" },      },    },  },}
[/code]

### CLI

bashCopy code
[code]
    openclaw config set agents.defaults.promptOverlays.gpt5.personality off
[/code]

## Giọng nói và lời nói

Speech synthesis (TTS)

Plugin `openai` được đóng gói kèm đăng ký tổng hợp lời nói cho bề mặt `messages.tts`.

Thiết lập | Đường dẫn cấu hình | Mặc định  
---|---|---  
Mô hình | `messages.tts.providers.openai.model` | `gpt-4o-mini-tts`  
Giọng | `messages.tts.providers.openai.voice` | `coral`  
Tốc độ | `messages.tts.providers.openai.speed` | (chưa đặt)  
Chỉ dẫn | `messages.tts.providers.openai.instructions` | (chưa đặt, chỉ `gpt-4o-mini-tts`)  
Định dạng | `messages.tts.providers.openai.responseFormat` | `opus` cho ghi chú thoại, `mp3` cho tệp  
Khóa API | `messages.tts.providers.openai.apiKey` | Dự phòng về `OPENAI_API_KEY`  
URL cơ sở | `messages.tts.providers.openai.baseUrl` | `https://api.openai.com/v1`  
Phần thân bổ sung | `messages.tts.providers.openai.extraBody` / `extra_body` | (chưa đặt)  
  
Các mô hình có sẵn: `gpt-4o-mini-tts`, `tts-1`, `tts-1-hd`. Các giọng có sẵn: `alloy`, `ash`, `ballad`, `cedar`, `coral`, `echo`, `fable`, `juniper`, `marin`, `onyx`, `nova`, `sage`, `shimmer`, `verse`.

`extraBody` được hợp nhất vào JSON yêu cầu `/audio/speech` sau các trường do OpenClaw tạo, vì vậy hãy dùng nó cho các điểm cuối tương thích OpenAI cần khóa bổ sung như `lang`. Các khóa prototype bị bỏ qua.

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        openai: { model: "gpt-4o-mini-tts", voice: "coral" },      },    },  },}
[/code]

Speech-to-text

Plugin `openai` được đóng gói kèm đăng ký chuyển lời nói thành văn bản theo lô thông qua bề mặt phiên âm hiểu nội dung đa phương tiện của OpenClaw.

  * Mô hình mặc định: `gpt-4o-transcribe`
  * Điểm cuối: OpenAI REST `/v1/audio/transcriptions`
  * Đường dẫn đầu vào: tải lên tệp âm thanh multipart
  * Được OpenClaw hỗ trợ ở mọi nơi phiên âm âm thanh đầu vào sử dụng `tools.media.audio`, bao gồm các đoạn kênh thoại Discord và tệp đính kèm âm thanh của kênh


Để ép dùng OpenAI cho phiên âm âm thanh đầu vào:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "openai",            model: "gpt-4o-transcribe",          },        ],      },    },  },}
[/code]

Gợi ý ngôn ngữ và lời nhắc được chuyển tiếp đến OpenAI khi được cung cấp bởi cấu hình đa phương tiện âm thanh dùng chung hoặc yêu cầu phiên âm theo từng lệnh gọi.

Phiên âm thời gian thực

Plugin `openai` đi kèm đăng ký tính năng phiên âm thời gian thực cho Plugin Voice Call.

Cài đặt | Đường dẫn cấu hình | Mặc định  
---|---|---  
Mô hình | `plugins.entries.voice-call.config.streaming.providers.openai.model` | `gpt-4o-transcribe`  
Ngôn ngữ | `...openai.language` | (chưa đặt)  
Lời nhắc | `...openai.prompt` | (chưa đặt)  
Thời lượng im lặng | `...openai.silenceDurationMs` | `800`  
Ngưỡng VAD | `...openai.vadThreshold` | `0.5`  
Xác thực | `...openai.apiKey`, `OPENAI_API_KEY`, hoặc OAuth `openai-codex` | Khóa API kết nối trực tiếp; OAuth phát hành bí mật máy khách phiên âm Realtime  
Giọng nói thời gian thực

Plugin `openai` đi kèm đăng ký giọng nói thời gian thực cho Plugin Voice Call.

Cài đặt | Đường dẫn cấu hình | Mặc định  
---|---|---  
Mô hình | `plugins.entries.voice-call.config.realtime.providers.openai.model` | `gpt-realtime-2`  
Giọng nói | `...openai.voice` | `alloy`  
Nhiệt độ (cầu nối triển khai Azure) | `...openai.temperature` | `0.8`  
Ngưỡng VAD | `...openai.vadThreshold` | `0.5`  
Thời lượng im lặng | `...openai.silenceDurationMs` | `500`  
Phần đệm tiền tố | `...openai.prefixPaddingMs` | `300`  
Mức nỗ lực suy luận | `...openai.reasoningEffort` | (chưa đặt)  
Xác thực | `...openai.apiKey`, `OPENAI_API_KEY`, hoặc OAuth `openai-codex` | Browser Talk và các cầu nối backend không phải Azure có thể dùng OAuth Codex  
  
Các giọng Realtime tích hợp sẵn có cho `gpt-realtime-2`: `alloy`, `ash`, `ballad`, `coral`, `echo`, `sage`, `shimmer`, `verse`, `marin`, `cedar`. OpenAI khuyến nghị `marin` và `cedar` để có chất lượng Realtime tốt nhất. Đây là một tập riêng biệt với các giọng Chuyển văn bản thành giọng nói ở trên; đừng giả định một giọng TTS như `fable`, `nova`, hoặc `onyx` là hợp lệ cho các phiên Realtime.

## Endpoint Azure OpenAI

Nhà cung cấp `openai` đi kèm có thể nhắm tới một tài nguyên Azure OpenAI để tạo hình ảnh bằng cách ghi đè URL cơ sở. Trên đường dẫn tạo hình ảnh, OpenClaw phát hiện tên máy chủ Azure trên `models.providers.openai.baseUrl` và tự động chuyển sang dạng yêu cầu của Azure.

Dùng Azure OpenAI khi:

  * Bạn đã có gói đăng ký, hạn mức, hoặc thỏa thuận doanh nghiệp Azure OpenAI
  * Bạn cần vùng lưu trú dữ liệu theo khu vực hoặc các kiểm soát tuân thủ do Azure cung cấp
  * Bạn muốn giữ lưu lượng bên trong một tenancy Azure hiện có


### Cấu hình

Để tạo hình ảnh Azure thông qua nhà cung cấp `openai` đi kèm, trỏ `models.providers.openai.baseUrl` tới tài nguyên Azure của bạn và đặt `apiKey` thành khóa Azure OpenAI (không phải khóa OpenAI Platform):

json5Copy code
[code]
    {  models: {    providers: {      openai: {        baseUrl: "https://<your-resource>.openai.azure.com",        apiKey: "<azure-openai-api-key>",      },    },  },}
[/code]

OpenClaw nhận dạng các hậu tố máy chủ Azure này cho tuyến tạo hình ảnh Azure:

  * `*.openai.azure.com`
  * `*.services.ai.azure.com`
  * `*.cognitiveservices.azure.com`


Đối với các yêu cầu tạo hình ảnh trên một máy chủ Azure được nhận dạng, OpenClaw:

  * Gửi header `api-key` thay vì `Authorization: Bearer`
  * Dùng các đường dẫn theo phạm vi triển khai (`/openai/deployments/{deployment}/...`)
  * Thêm `?api-version=...` vào mỗi yêu cầu
  * Dùng thời gian chờ yêu cầu mặc định 600 giây cho các lệnh gọi tạo hình ảnh Azure. Các giá trị `timeoutMs` theo từng lệnh gọi vẫn ghi đè mặc định này.


Các URL cơ sở khác (OpenAI công khai, proxy tương thích OpenAI) giữ dạng yêu cầu hình ảnh OpenAI tiêu chuẩn.

### Phiên bản API

Đặt `AZURE_OPENAI_API_VERSION` để ghim một phiên bản Azure preview hoặc GA cụ thể cho đường dẫn tạo hình ảnh của Azure:

bashCopy code
[code]
    export AZURE_OPENAI_API_VERSION="2024-12-01-preview"
[/code]

Mặc định là `2024-12-01-preview` khi biến này chưa được đặt.

### Tên model là tên triển khai

Azure OpenAI liên kết model với các triển khai. Đối với các yêu cầu tạo hình ảnh Azure được định tuyến qua nhà cung cấp `openai` đi kèm, trường `model` trong OpenClaw phải là **tên triển khai Azure** mà bạn đã cấu hình trong cổng Azure, không phải id model OpenAI công khai.

Nếu bạn tạo một triển khai tên là `gpt-image-2-prod` phục vụ `gpt-image-2`:

CodeCopy code
[code]
    /tool image_generate model=openai/gpt-image-2-prod prompt="A clean poster" size=1024x1024 count=1
[/code]

Quy tắc dùng tên triển khai tương tự cũng áp dụng cho các lệnh gọi tạo hình ảnh được định tuyến qua nhà cung cấp `openai` đi kèm.

### Tình trạng khả dụng theo khu vực

Tạo hình ảnh Azure hiện chỉ khả dụng ở một số khu vực (ví dụ `eastus2`, `swedencentral`, `polandcentral`, `westus3`, `uaenorth`). Hãy kiểm tra danh sách khu vực hiện tại của Microsoft trước khi tạo triển khai, và xác nhận model cụ thể được cung cấp trong khu vực của bạn.

### Khác biệt về tham số

Azure OpenAI và OpenAI công khai không phải lúc nào cũng chấp nhận cùng các tham số hình ảnh. Azure có thể từ chối các tùy chọn mà OpenAI công khai cho phép (ví dụ một số giá trị `background` nhất định trên `gpt-image-2`) hoặc chỉ cung cấp chúng trên các phiên bản model cụ thể. Những khác biệt này đến từ Azure và model nền tảng, không phải OpenClaw. Nếu một yêu cầu Azure thất bại với lỗi xác thực, hãy kiểm tra tập tham số được hỗ trợ bởi triển khai và phiên bản API cụ thể của bạn trong cổng Azure.

## Cấu hình nâng cao

Transport (WebSocket so với SSE)

OpenClaw ưu tiên WebSocket và dự phòng SSE (`"auto"`) cho `openai/*`.

Ở chế độ `"auto"`, OpenClaw:

  * Thử lại một lỗi WebSocket sớm một lần trước khi chuyển sang SSE
  * Sau một lỗi, đánh dấu WebSocket là suy giảm trong khoảng 60 giây và dùng SSE trong thời gian chờ nguội
  * Gắn các tiêu đề định danh phiên và lượt ổn định cho các lần thử lại và kết nối lại
  * Chuẩn hóa bộ đếm sử dụng (`input_tokens` / `prompt_tokens`) trên các biến thể transport

Giá trị | Hành vi  
---|---  
`"auto"` (mặc định) | WebSocket trước, dự phòng SSE  
`"sse"` | Chỉ buộc dùng SSE  
`"websocket"` | Chỉ buộc dùng WebSocket  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { transport: "auto" },        },      },    },  },}
[/code]

Tài liệu OpenAI liên quan:

  * [Realtime API với WebSocket](<https://platform.openai.com/docs/guides/realtime-websocket>)
  * [Phản hồi Streaming API (SSE)](<https://platform.openai.com/docs/guides/streaming-responses>)

Chế độ nhanh

OpenClaw cung cấp một nút bật/tắt chế độ nhanh dùng chung cho `openai/*`:

  * **Chat/UI:** `/fast status|on|off`
  * **Cấu hình:** `agents.defaults.models["<provider>/<model>"].params.fastMode`


Khi được bật, OpenClaw ánh xạ chế độ nhanh sang xử lý ưu tiên của OpenAI (`service_tier = "priority"`). Các giá trị `service_tier` hiện có được giữ nguyên, và chế độ nhanh không viết lại `reasoning` hoặc `text.verbosity`.

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

Xử lý ưu tiên (service_tier)

API của OpenAI cung cấp xử lý ưu tiên qua `service_tier`. Đặt giá trị này cho từng mô hình trong OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": { params: { serviceTier: "priority" } },      },    },  },}
[/code]

Giá trị được hỗ trợ: `auto`, `default`, `flex`, `priority`.

Compaction phía máy chủ (Responses API)

Với các mô hình OpenAI Responses trực tiếp (`openai/*` trên `api.openai.com`), trình bao bọc luồng Pi-harness của OpenAI plugin tự động bật Compaction phía máy chủ:

  * Bắt buộc `store: true` (trừ khi tương thích mô hình đặt `supportsStore: false`)
  * Chèn `context_management: [{ type: "compaction", compact_threshold: ... }]`
  * `compact_threshold` mặc định: 70% của `contextWindow` (hoặc `80000` khi không có)


Điều này áp dụng cho đường dẫn Pi harness tích hợp sẵn và các hook của nhà cung cấp OpenAI được dùng bởi các lần chạy nhúng. Harness máy chủ ứng dụng Codex gốc tự quản lý ngữ cảnh của nó thông qua Codex và được cấu hình bằng tuyến tác nhân mặc định của OpenAI hoặc chính sách runtime của nhà cung cấp/mô hình.

### Bật rõ ràng

Hữu ích cho các endpoint tương thích như Azure OpenAI Responses:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "azure-openai-responses/gpt-5.5": {          params: { responsesServerCompaction: true },        },      },    },  },}
[/code]

### Ngưỡng tùy chỉnh

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: {            responsesServerCompaction: true,            responsesCompactThreshold: 120000,          },        },      },    },  },}
[/code]

### Tắt

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openai/gpt-5.5": {          params: { responsesServerCompaction: false },        },      },    },  },}
[/code]

Chế độ GPT strict-agentic

Với các lần chạy họ GPT-5 trên `openai/*`, OpenClaw có thể dùng một hợp đồng thực thi nhúng nghiêm ngặt hơn:

json5Copy code
[code]
    {  agents: {    defaults: {      embeddedPi: { executionContract: "strict-agentic" },    },  },}
[/code]

Với `strict-agentic`, OpenClaw:

  * Không còn xem một lượt chỉ lập kế hoạch là tiến triển thành công khi có sẵn hành động công cụ
  * Thử lại lượt đó với điều hướng hành động ngay
  * Tự động bật `update_plan` cho công việc đáng kể
  * Hiển thị trạng thái bị chặn rõ ràng nếu mô hình tiếp tục lập kế hoạch mà không hành động

Tuyến gốc so với tuyến tương thích OpenAI

OpenClaw xử lý các endpoint OpenAI trực tiếp, Codex và Azure OpenAI khác với các proxy `/v1` tương thích OpenAI chung:

**Tuyến gốc** (`openai/*`, Azure OpenAI):

  * Chỉ giữ `reasoning: { effort: "none" }` cho các mô hình hỗ trợ mức nỗ lực `none` của OpenAI
  * Bỏ qua suy luận đã tắt đối với các mô hình hoặc proxy từ chối `reasoning.effort: "none"`
  * Mặc định dùng chế độ nghiêm ngặt cho lược đồ công cụ
  * Chỉ đính kèm các header ghi công ẩn trên các máy chủ gốc đã xác minh
  * Giữ định hình yêu cầu chỉ dành cho OpenAI (`service_tier`, `store`, tương thích suy luận, gợi ý cache prompt)


**Tuyến proxy/tương thích:**

  * Dùng hành vi tương thích thoáng hơn
  * Loại bỏ `store` của Completions khỏi payload `openai-completions` không gốc
  * Chấp nhận JSON truyền qua nâng cao `params.extra_body`/`params.extraBody` cho các proxy Completions tương thích OpenAI
  * Chấp nhận `params.chat_template_kwargs` cho các proxy Completions tương thích OpenAI như vLLM
  * Không bắt buộc lược đồ công cụ nghiêm ngặt hoặc header chỉ dành cho tuyến gốc


Azure OpenAI dùng truyền tải gốc và hành vi tương thích nhưng không nhận các header ghi công ẩn.

## Liên quan

[**Lựa chọn mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Tạo hình ảnh** Tham số công cụ hình ảnh dùng chung và lựa chọn nhà cung cấp. ](</vi/tools/image-generation>) [**Tạo video** Tham số công cụ video dùng chung và lựa chọn nhà cung cấp. ](</vi/tools/video-generation>) [**OAuth và xác thực** Chi tiết xác thực và quy tắc tái sử dụng thông tin đăng nhập. ](</vi/gateway/authentication>)

Was this useful?YesNo