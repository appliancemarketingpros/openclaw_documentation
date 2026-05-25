---
title: Tạo video
source_url: https://docs.openclaw.ai/vi/tools/video-generation
scraped_at: 2026-05-25
---

Các agent OpenClaw có thể tạo video từ prompt văn bản, ảnh tham chiếu hoặc video hiện có. Mười sáu backend nhà cung cấp được hỗ trợ, mỗi backend có các tùy chọn mô hình, chế độ đầu vào và bộ tính năng khác nhau. Agent tự động chọn nhà cung cấp phù hợp dựa trên cấu hình và các khóa API khả dụng của bạn.

OpenClaw xem tạo video là ba chế độ runtime:

  * `generate` \- yêu cầu văn bản-sang-video không có media tham chiếu.
  * `imageToVideo` \- yêu cầu bao gồm một hoặc nhiều ảnh tham chiếu.
  * `videoToVideo` \- yêu cầu bao gồm một hoặc nhiều video tham chiếu.


Nhà cung cấp có thể hỗ trợ bất kỳ tập con nào của các chế độ đó. Công cụ xác thực chế độ đang hoạt động trước khi gửi và báo cáo các chế độ được hỗ trợ trong `action=list`.

## Bắt đầu nhanh

* ### Cấu hình xác thực

Đặt khóa API cho bất kỳ nhà cung cấp nào được hỗ trợ:

bashCopy code
[code]
    export GEMINI_API_KEY="your-key"
[/code]

* ### Chọn mô hình mặc định (tùy chọn)

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "google/veo-3.1-fast-generate-preview"
[/code]

* ### Yêu cầu agent

> Tạo một video điện ảnh dài 5 giây về một chú tôm hùm thân thiện đang lướt sóng lúc hoàng hôn.

Agent tự động gọi `video_generate`. Không cần đưa công cụ vào danh sách cho phép.

## Cách tạo bất đồng bộ hoạt động

Tạo video là bất đồng bộ. Khi agent gọi `video_generate` trong một phiên:

  1. OpenClaw gửi yêu cầu đến nhà cung cấp và lập tức trả về id tác vụ.
  2. Nhà cung cấp xử lý job ở chế độ nền (thường từ 30 giây đến vài phút tùy nhà cung cấp và độ phân giải; các nhà cung cấp chậm dựa trên hàng đợi có thể chạy đến hết thời gian chờ đã cấu hình).
  3. Khi video sẵn sàng, OpenClaw đánh thức cùng phiên đó bằng một sự kiện hoàn tất nội bộ.
  4. Agent thông báo cho người dùng và đính kèm video đã hoàn tất. Trong các cuộc trò chuyện nhóm/kênh dùng cách gửi hiển thị chỉ qua công cụ nhắn tin, agent chuyển tiếp kết quả qua công cụ nhắn tin thay vì để OpenClaw đăng trực tiếp.


Trong khi job đang chạy, các lệnh gọi `video_generate` trùng lặp trong cùng phiên sẽ trả về trạng thái tác vụ hiện tại thay vì bắt đầu một lần tạo khác. Dùng `openclaw tasks list` hoặc `openclaw tasks show <taskId>` để kiểm tra tiến trình từ CLI.

Bên ngoài các lần chạy agent có phiên hỗ trợ (ví dụ: gọi công cụ trực tiếp), công cụ sẽ chuyển sang tạo inline và trả về đường dẫn media cuối cùng trong cùng lượt.

Các tệp video đã tạo được lưu trong vùng lưu trữ media do OpenClaw quản lý khi nhà cung cấp trả về byte. Giới hạn lưu video đã tạo mặc định tuân theo giới hạn media video, và `agents.defaults.mediaMaxMb` tăng giới hạn đó cho các kết xuất lớn hơn. Khi nhà cung cấp cũng trả về URL đầu ra được lưu trữ, OpenClaw có thể gửi URL đó thay vì làm tác vụ thất bại nếu lưu cục bộ từ chối một tệp quá lớn.

### Vòng đời tác vụ

Trạng thái | Ý nghĩa  
---|---  
`queued` | Tác vụ đã tạo, đang chờ nhà cung cấp chấp nhận.  
`running` | Nhà cung cấp đang xử lý (thường từ 30 giây đến vài phút tùy nhà cung cấp và độ phân giải).  
`succeeded` | Video đã sẵn sàng; agent thức dậy và đăng video vào cuộc trò chuyện.  
`failed` | Lỗi nhà cung cấp hoặc hết thời gian chờ; agent thức dậy với chi tiết lỗi.  
  
Kiểm tra trạng thái từ CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

Nếu một tác vụ video đã ở trạng thái `queued` hoặc `running` cho phiên hiện tại, `video_generate` sẽ trả về trạng thái tác vụ hiện có thay vì bắt đầu một tác vụ mới. Dùng `action: "status"` để kiểm tra rõ ràng mà không kích hoạt một lần tạo mới.

## Nhà cung cấp được hỗ trợ

Nhà cung cấp | Mô hình mặc định | Văn bản | Tham chiếu ảnh | Tham chiếu video | Xác thực  
---|---|---|---|---|---  
Alibaba | `wan2.6-t2v` | ✓ | Có (URL từ xa) | Có (URL từ xa) | `MODELSTUDIO_API_KEY`  
BytePlus (1.0) | `seedance-1-0-pro-250528` | ✓ | Tối đa 2 ảnh (chỉ mô hình I2V; khung đầu + cuối) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 1.5 | `seedance-1-5-pro-251215` | ✓ | Tối đa 2 ảnh (khung đầu + cuối qua vai trò) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 2.0 | `dreamina-seedance-2-0-260128` | ✓ | Tối đa 9 ảnh tham chiếu | Tối đa 3 video | `BYTEPLUS_API_KEY`  
ComfyUI | `workflow` | ✓ | 1 ảnh | - | `COMFY_API_KEY` hoặc `COMFY_CLOUD_API_KEY`  
DeepInfra | `Pixverse/Pixverse-T2V` | ✓ | - | - | `DEEPINFRA_API_KEY`  
fal | `fal-ai/minimax/video-01-live` | ✓ | 1 ảnh; tối đa 9 ảnh với Seedance reference-to-video | Tối đa 3 video với Seedance reference-to-video | `FAL_KEY`  
Google | `veo-3.1-fast-generate-preview` | ✓ | 1 ảnh | 1 video | `GEMINI_API_KEY`  
MiniMax | `MiniMax-Hailuo-2.3` | ✓ | 1 ảnh | - | `MINIMAX_API_KEY` hoặc MiniMax OAuth  
OpenAI | `sora-2` | ✓ | 1 ảnh | 1 video | `OPENAI_API_KEY`  
OpenRouter | `google/veo-3.1-fast` | ✓ | Tối đa 4 ảnh (khung đầu/cuối hoặc tham chiếu) | - | `OPENROUTER_API_KEY`  
Qwen | `wan2.6-t2v` | ✓ | Có (URL từ xa) | Có (URL từ xa) | `QWEN_API_KEY`  
Runway | `gen4.5` | ✓ | 1 ảnh | 1 video | `RUNWAYML_API_SECRET`  
Together | `Wan-AI/Wan2.2-T2V-A14B` | ✓ | 1 ảnh | - | `TOGETHER_API_KEY`  
Vydra | `veo3` | ✓ | 1 ảnh (`kling`) | - | `VYDRA_API_KEY`  
xAI | `grok-imagine-video` | ✓ | 1 ảnh khung đầu hoặc tối đa 7 `reference_image` | 1 video | `XAI_API_KEY`  
  
Một số nhà cung cấp chấp nhận thêm hoặc thay thế bằng các biến môi trường khóa API khác. Xem từng trang nhà cung cấp để biết chi tiết.

Chạy `video_generate action=list` để kiểm tra các nhà cung cấp, mô hình và chế độ runtime khả dụng tại runtime.

### Ma trận năng lực

Hợp đồng chế độ tường minh được `video_generate`, các kiểm thử hợp đồng và đợt quét live dùng chung sử dụng:

Nhà cung cấp | `generate` | `imageToVideo` | `videoToVideo` | Các lane live dùng chung hiện nay  
---|---|---|---|---  
Alibaba | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; bỏ qua `videoToVideo` vì nhà cung cấp này cần URL video `http(s)` từ xa  
BytePlus | ✓ | ✓ | - | `generate`, `imageToVideo`  
ComfyUI | ✓ | ✓ | - | Không có trong đợt quét dùng chung; phạm vi kiểm thử theo workflow nằm trong các kiểm thử Comfy  
DeepInfra | ✓ | - | - | `generate`; các schema video DeepInfra gốc là văn bản-sang-video trong hợp đồng được đóng gói  
fal | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` chỉ khi dùng Seedance reference-to-video  
Google | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; bỏ qua `videoToVideo` dùng chung vì đợt quét Gemini/Veo hiện tại dựa trên buffer không chấp nhận đầu vào đó  
MiniMax | ✓ | ✓ | - | `generate`, `imageToVideo`  
OpenAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; bỏ qua `videoToVideo` dùng chung vì đường dẫn tổ chức/đầu vào này hiện cần quyền truy cập inpaint/remix phía nhà cung cấp  
OpenRouter | ✓ | ✓ | - | `generate`, `imageToVideo`  
Qwen | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; bỏ qua `videoToVideo` vì nhà cung cấp này cần URL video `http(s)` từ xa  
Runway | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` chỉ chạy khi mô hình được chọn là `runway/gen4_aleph`  
Together | ✓ | ✓ | - | `generate`, `imageToVideo`  
Vydra | ✓ | ✓ | - | `generate`; bỏ qua `imageToVideo` dùng chung vì `veo3` được đóng gói chỉ hỗ trợ văn bản và `kling` được đóng gói yêu cầu URL ảnh từ xa  
xAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; bỏ qua `videoToVideo` vì nhà cung cấp này hiện cần URL MP4 từ xa  
  
## Tham số công cụ

### Bắt buộc

Mô tả văn bản của video cần tạo. Bắt buộc cho `action: "generate"`.

### Đầu vào nội dung

Gợi ý vai trò tùy chọn theo từng vị trí, song song với danh sách ảnh kết hợp. Giá trị chuẩn: `first_frame`, `last_frame`, `reference_image`.

Gợi ý vai trò tùy chọn theo từng vị trí, song song với danh sách video kết hợp. Giá trị chuẩn: `reference_video`.

Âm thanh tham chiếu đơn (đường dẫn hoặc URL). Dùng cho nhạc nền hoặc tham chiếu giọng nói khi nhà cung cấp hỗ trợ đầu vào âm thanh.

Gợi ý vai trò tùy chọn theo từng vị trí, song song với danh sách âm thanh kết hợp. Giá trị chuẩn: `reference_audio`.

### Điều khiển kiểu

Gợi ý tỷ lệ khung hình như `1:1`, `16:9`, `9:16`, `adaptive`, hoặc giá trị riêng của nhà cung cấp. OpenClaw chuẩn hóa hoặc bỏ qua các giá trị không được hỗ trợ theo từng nhà cung cấp.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc29sdXRpb24iIHR5cGU9InN0cmluZyI Gợi ý độ phân giải như `480P`, `720P`, `768P`, `1080P`, `4K`, hoặc giá trị riêng của nhà cung cấp. OpenClaw chuẩn hóa hoặc bỏ qua các giá trị không được hỗ trợ theo từng nhà cung cấp. OPENCLAW_DOCS_MARKER:paramClose:

Thời lượng mục tiêu tính bằng giây (làm tròn đến giá trị gần nhất được nhà cung cấp hỗ trợ).

Bật âm thanh được tạo trong đầu ra khi được hỗ trợ. Khác với `audioRef*` (đầu vào).

`adaptive` là một sentinel riêng của nhà cung cấp: nó được chuyển tiếp nguyên trạng đến các nhà cung cấp khai báo `adaptive` trong capabilities của họ (ví dụ: BytePlus Seedance dùng nó để tự động phát hiện tỷ lệ từ kích thước ảnh đầu vào). Các nhà cung cấp không khai báo nó sẽ hiển thị giá trị qua `details.ignoredOverrides` trong kết quả công cụ để việc bỏ qua có thể quan sát được.

### Nâng cao

`"status"` trả về tác vụ phiên hiện tại; `"list"` kiểm tra các nhà cung cấp.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Ghi đè nhà cung cấp/model (ví dụ: `runway/gen4.5`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Thời gian chờ tùy chọn cho thao tác của nhà cung cấp, tính bằng mili giây. Khi bỏ qua, OpenClaw dùng `agents.defaults.videoGenerationModel.timeoutMs` nếu đã cấu hình. OPENCLAW_DOCS_MARKER:paramClose:

Tùy chọn riêng của nhà cung cấp dưới dạng đối tượng JSON (ví dụ: `{"seed": 42, "draft": true}`). Các nhà cung cấp khai báo schema có kiểu sẽ xác thực khóa và kiểu; khóa không xác định hoặc không khớp sẽ bỏ qua ứng viên trong quá trình fallback. Nhà cung cấp không có schema đã khai báo sẽ nhận tùy chọn nguyên trạng. Chạy `video_generate action=list` để xem từng nhà cung cấp chấp nhận gì.

Đầu vào tham chiếu chọn chế độ runtime:

  * Không có phương tiện tham chiếu → `generate`
  * Có bất kỳ tham chiếu ảnh nào → `imageToVideo`
  * Có bất kỳ tham chiếu video nào → `videoToVideo`
  * Đầu vào âm thanh tham chiếu **không** thay đổi chế độ đã phân giải; chúng áp dụng bên trên bất kỳ chế độ nào do tham chiếu ảnh/video chọn, và chỉ hoạt động với các nhà cung cấp khai báo `maxInputAudios`.


Trộn tham chiếu ảnh và video không phải là một bề mặt capability dùng chung ổn định. Ưu tiên một loại tham chiếu cho mỗi yêu cầu.

#### Fallback và tùy chọn có kiểu

Một số kiểm tra capability được áp dụng ở lớp fallback thay vì ranh giới công cụ, nên một yêu cầu vượt quá giới hạn của nhà cung cấp chính vẫn có thể chạy trên một fallback có khả năng:

  * Ứng viên đang hoạt động không khai báo `maxInputAudios` (hoặc `0`) sẽ bị bỏ qua khi yêu cầu chứa tham chiếu âm thanh; ứng viên tiếp theo sẽ được thử.
  * `maxDurationSeconds` của ứng viên đang hoạt động thấp hơn `durationSeconds` được yêu cầu và không có danh sách `supportedDurationSeconds` đã khai báo → bị bỏ qua.
  * Yêu cầu chứa `providerOptions` và ứng viên đang hoạt động khai báo rõ ràng schema `providerOptions` có kiểu → bị bỏ qua nếu các khóa được cung cấp không có trong schema hoặc kiểu giá trị không khớp. Nhà cung cấp không có schema đã khai báo sẽ nhận tùy chọn nguyên trạng (truyền qua tương thích ngược). Một nhà cung cấp có thể từ chối mọi tùy chọn nhà cung cấp bằng cách khai báo schema rỗng (`capabilities.providerOptions: {}`), điều này gây ra cùng kiểu bỏ qua như khi kiểu không khớp.


Lý do bỏ qua đầu tiên trong một yêu cầu được ghi log ở mức `warn` để operator thấy khi nhà cung cấp chính của họ bị bỏ qua; các lần bỏ qua tiếp theo ghi log ở mức `debug` để giữ các chuỗi fallback dài không ồn ào. Nếu mọi ứng viên đều bị bỏ qua, lỗi tổng hợp sẽ bao gồm lý do bỏ qua của từng ứng viên.

## Hành động

Hành động | Chức năng  
---|---  
`generate` | Mặc định. Tạo video từ prompt đã cho và các đầu vào tham chiếu tùy chọn.  
`status` | Kiểm tra trạng thái của tác vụ video đang chạy cho phiên hiện tại mà không bắt đầu lần tạo khác.  
`list` | Hiển thị các nhà cung cấp, model và capability hiện có.  
  
## Chọn model

OpenClaw phân giải model theo thứ tự này:

  1. **Tham số công cụ`model`** \- nếu agent chỉ định một model trong lệnh gọi.
  2. **`videoGenerationModel.primary`** từ cấu hình.
  3. **`videoGenerationModel.fallbacks`** theo thứ tự.
  4. **Tự động phát hiện** \- các nhà cung cấp có xác thực hợp lệ, bắt đầu bằng nhà cung cấp mặc định hiện tại, rồi các nhà cung cấp còn lại theo thứ tự chữ cái.


Nếu một nhà cung cấp thất bại, ứng viên tiếp theo sẽ được thử tự động. Nếu mọi ứng viên đều thất bại, lỗi sẽ bao gồm chi tiết từ từng lần thử.

Đặt `agents.defaults.mediaGenerationAutoProviderFallback: false` để chỉ dùng các mục `model`, `primary` và `fallbacks` rõ ràng.

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",        fallbacks: ["runway/gen4.5", "qwen/wan2.6-t2v"],      },    },  },}
[/code]

## Ghi chú về nhà cung cấp

Alibaba

Dùng endpoint bất đồng bộ DashScope / Model Studio. Ảnh và video tham chiếu phải là URL `http(s)` từ xa.

BytePlus (1.0)

ID nhà cung cấp: `byteplus`.

Model: `seedance-1-0-pro-250528` (mặc định), `seedance-1-0-pro-t2v-250528`, `seedance-1-0-pro-fast-251015`, `seedance-1-0-lite-t2v-250428`, `seedance-1-0-lite-i2v-250428`.

Model T2V (`*-t2v-*`) không chấp nhận đầu vào ảnh; model I2V và model `*-pro-*` tổng quát hỗ trợ một ảnh tham chiếu duy nhất (khung hình đầu tiên). Truyền ảnh theo vị trí hoặc đặt `role: "first_frame"`. ID model T2V được tự động chuyển sang biến thể I2V tương ứng khi có ảnh được cung cấp.

Khóa `providerOptions` được hỗ trợ: `seed` (số), `draft` (boolean - ép 480p), `camera_fixed` (boolean).

BytePlus Seedance 1.5

Yêu cầu plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). ID nhà cung cấp: `byteplus-seedance15`. Model: `seedance-1-5-pro-251215`.

Dùng API `content[]` hợp nhất. Hỗ trợ tối đa 2 ảnh đầu vào (`first_frame` \+ `last_frame`). Tất cả đầu vào phải là URL `https://` từ xa. Đặt `role: "first_frame"` / `"last_frame"` trên mỗi ảnh, hoặc truyền ảnh theo vị trí.

`aspectRatio: "adaptive"` tự động phát hiện tỷ lệ từ ảnh đầu vào. `audio: true` ánh xạ sang `generate_audio`. `providerOptions.seed` (số) được chuyển tiếp.

BytePlus Seedance 2.0

Yêu cầu plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). ID nhà cung cấp: `byteplus-seedance2`. Model: `dreamina-seedance-2-0-260128`, `dreamina-seedance-2-0-fast-260128`.

Dùng API `content[]` hợp nhất. Hỗ trợ tối đa 9 ảnh tham chiếu, 3 video tham chiếu và 3 âm thanh tham chiếu. Tất cả đầu vào phải là URL `https://` từ xa. Đặt `role` trên từng asset - các giá trị được hỗ trợ: `"first_frame"`, `"last_frame"`, `"reference_image"`, `"reference_video"`, `"reference_audio"`.

`aspectRatio: "adaptive"` tự động phát hiện tỷ lệ từ ảnh đầu vào. `audio: true` ánh xạ sang `generate_audio`. `providerOptions.seed` (số) được chuyển tiếp.

ComfyUI

Thực thi cục bộ hoặc trên đám mây dựa trên workflow. Hỗ trợ text-to-video và image-to-video thông qua graph đã cấu hình.

fal

Sử dụng luồng có hàng đợi hỗ trợ cho các tác vụ chạy lâu. Theo mặc định, OpenClaw chờ tối đa 20 phút trước khi xem một tác vụ hàng đợi fal đang chạy là đã hết thời gian chờ. Hầu hết các mô hình video fal chấp nhận một tham chiếu hình ảnh duy nhất. Các mô hình Seedance 2.0 reference-to-video chấp nhận tối đa 9 hình ảnh, 3 video và 3 tham chiếu âm thanh, với tối đa 12 tệp tham chiếu tổng cộng.

Google (Gemini / Veo)

Hỗ trợ một tham chiếu hình ảnh hoặc một tham chiếu video. Các yêu cầu tạo âm thanh bị bỏ qua kèm cảnh báo trên đường dẫn Gemini API vì API đó từ chối tham số `generateAudio` cho quá trình tạo video Veo hiện tại.

MiniMax

Chỉ một tham chiếu hình ảnh duy nhất. MiniMax chấp nhận độ phân giải `768P` và `1080P`; các yêu cầu như `720P` được chuẩn hóa thành giá trị được hỗ trợ gần nhất trước khi gửi.

OpenAI

Chỉ chuyển tiếp ghi đè `size`. Các ghi đè kiểu khác (`aspectRatio`, `resolution`, `audio`, `watermark`) bị bỏ qua kèm cảnh báo.

OpenRouter

Sử dụng API `/videos` bất đồng bộ của OpenRouter. OpenClaw gửi tác vụ, thăm dò `polling_url`, rồi tải xuống `unsigned_urls` hoặc endpoint nội dung tác vụ đã được tài liệu hóa. Mặc định `google/veo-3.1-fast` đi kèm công bố thời lượng 4/6/8 giây, độ phân giải `720P`/`1080P`, và tỷ lệ khung hình `16:9`/`9:16`.

Qwen

Cùng backend DashScope như Alibaba. Đầu vào tham chiếu phải là URL `http(s)` từ xa; tệp cục bộ bị từ chối ngay từ đầu.

Runway

Hỗ trợ tệp cục bộ qua data URI. Video-to-video yêu cầu `runway/gen4_aleph`. Các lượt chạy chỉ văn bản cung cấp tỷ lệ khung hình `16:9` và `9:16`.

Together

Chỉ một tham chiếu hình ảnh duy nhất.

Vydra

Sử dụng trực tiếp `https://www.vydra.ai/api/v1` để tránh các chuyển hướng làm mất xác thực. `veo3` được đi kèm chỉ dưới dạng text-to-video; `kling` yêu cầu URL hình ảnh từ xa.

xAI

Hỗ trợ text-to-video, image-to-video với một hình ảnh khung đầu tiên, tối đa 7 đầu vào `reference_image` thông qua `reference_images` của xAI, và các luồng chỉnh sửa/mở rộng video từ xa.

## Chế độ năng lực của nhà cung cấp

Hợp đồng tạo video dùng chung hỗ trợ các năng lực theo từng chế độ thay vì chỉ các giới hạn tổng hợp phẳng. Các triển khai nhà cung cấp mới nên ưu tiên các khối chế độ rõ ràng:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxVideos: 1,    maxDurationSeconds: 10,    supportsResolution: true,  },  imageToVideo: {    enabled: true,    maxVideos: 1,    maxInputImages: 1,    maxInputImagesByModel: { "provider/reference-to-video": 9 },    maxDurationSeconds: 5,  },  videoToVideo: {    enabled: true,    maxVideos: 1,    maxInputVideos: 1,    maxDurationSeconds: 5,  },}
[/code]

Các trường tổng hợp phẳng như `maxInputImages` và `maxInputVideos` **không** đủ để công bố hỗ trợ chế độ chuyển đổi. Nhà cung cấp nên khai báo rõ `generate`, `imageToVideo` và `videoToVideo` để các kiểm thử live, kiểm thử hợp đồng và công cụ `video_generate` dùng chung có thể xác thực hỗ trợ chế độ một cách xác định.

Khi một mô hình trong một nhà cung cấp có hỗ trợ đầu vào tham chiếu rộng hơn phần còn lại, hãy dùng `maxInputImagesByModel`, `maxInputVideosByModel` hoặc `maxInputAudiosByModel` thay vì nâng giới hạn cho toàn bộ chế độ.

## Kiểm thử live

Phạm vi kiểm thử live tự chọn cho các nhà cung cấp đi kèm dùng chung:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/video-generation-providers.live.test.ts
[/code]

Wrapper của repo:

bashCopy code
[code]
    pnpm test:live:media video
[/code]

Tệp live này tải các biến môi trường nhà cung cấp còn thiếu từ `~/.profile`, mặc định ưu tiên khóa API live/env trước các hồ sơ xác thực đã lưu, và mặc định chạy một smoke test an toàn cho phát hành:

  * `generate` cho mọi nhà cung cấp không phải FAL trong lượt quét.
  * Prompt tôm hùm một giây.
  * Giới hạn thao tác theo từng nhà cung cấp từ `OPENCLAW_LIVE_VIDEO_GENERATION_TIMEOUT_MS` (mặc định là `180000`).


FAL là tự chọn vì độ trễ hàng đợi phía nhà cung cấp có thể chiếm phần lớn thời gian phát hành:

bashCopy code
[code]
    pnpm test:live:media video --video-providers fal
[/code]

Đặt `OPENCLAW_LIVE_VIDEO_GENERATION_FULL_MODES=1` để cũng chạy các chế độ chuyển đổi đã khai báo mà lượt quét dùng chung có thể thực hiện an toàn với phương tiện cục bộ:

  * `imageToVideo` khi `capabilities.imageToVideo.enabled`.
  * `videoToVideo` khi `capabilities.videoToVideo.enabled` và nhà cung cấp/mô hình chấp nhận đầu vào video cục bộ dựa trên buffer trong lượt quét dùng chung.


Hiện tại, làn live `videoToVideo` dùng chung chỉ bao phủ `runway` khi bạn chọn `runway/gen4_aleph`.

## Cấu hình

Đặt mô hình tạo video mặc định trong cấu hình OpenClaw của bạn:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "qwen/wan2.6-t2v",        fallbacks: ["qwen/wan2.6-r2v-flash"],      },    },  },}
[/code]

Hoặc qua CLI:

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "qwen/wan2.6-t2v"
[/code]

## Liên quan

  * [Alibaba Model Studio](</vi/providers/alibaba>)
  * [Tác vụ nền](</vi/automation/tasks>) \- theo dõi tác vụ cho tạo video bất đồng bộ
  * [BytePlus](</vi/concepts/model-providers#byteplus-international>)
  * [ComfyUI](</vi/providers/comfy>)
  * [Tham chiếu cấu hình](</vi/gateway/config-agents#agent-defaults>)
  * [fal](</vi/providers/fal>)
  * [Google (Gemini)](</vi/providers/google>)
  * [MiniMax](</vi/providers/minimax>)
  * [Mô hình](</vi/concepts/models>)
  * [OpenAI](</vi/providers/openai>)
  * [Qwen](</vi/providers/qwen>)
  * [Runway](</vi/providers/runway>)
  * [Together AI](</vi/providers/together>)
  * [Tổng quan về công cụ](</vi/tools>)
  * [Vydra](</vi/providers/vydra>)
  * [xAI](</vi/providers/xai>)


Was this useful?YesNo