---
title: Tạo nhạc
source_url: https://docs.openclaw.ai/vi/tools/music-generation
scraped_at: 2026-05-25
---

Công cụ `music_generate` cho phép agent tạo nhạc hoặc âm thanh thông qua năng lực tạo nhạc dùng chung với các nhà cung cấp đã cấu hình — hiện nay là Google, MiniMax và ComfyUI được cấu hình bằng workflow.

Đối với các lần chạy agent có phiên hỗ trợ, OpenClaw khởi động việc tạo nhạc dưới dạng tác vụ nền, theo dõi tác vụ đó trong sổ cái tác vụ, rồi đánh thức agent lần nữa khi bản nhạc đã sẵn sàng để agent có thể báo cho người dùng và đính kèm âm thanh hoàn chỉnh. Trong các cuộc trò chuyện nhóm/kênh dùng cơ chế phân phối hiển thị chỉ qua công cụ tin nhắn, agent chuyển tiếp kết quả qua công cụ tin nhắn. Nếu agent hoàn tất chỉ ghi một phản hồi cuối riêng tư, OpenClaw sẽ dự phòng bằng cách gửi trực tiếp qua kênh kèm phương tiện đã tạo. Lần đánh thức khi hoàn tất cảnh báo rõ cho agent rằng các phản hồi cuối thông thường là riêng tư trong những tuyến đó.

## Bắt đầu nhanh

### Được hỗ trợ bởi nhà cung cấp dùng chung

* ### Cấu hình xác thực

Đặt khóa API cho ít nhất một nhà cung cấp — ví dụ `GEMINI_API_KEY` hoặc `MINIMAX_API_KEY`.

* ### Chọn model mặc định (tùy chọn)

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

* ### Yêu cầu agent

_"Tạo một bản synthpop sôi động về chuyến lái xe ban đêm qua một thành phố neon."_

Agent tự động gọi `music_generate`. Không cần đưa công cụ vào danh sách cho phép.

Đối với các ngữ cảnh đồng bộ trực tiếp không có lần chạy agent được phiên hỗ trợ, công cụ tích hợp sẵn vẫn dự phòng sang tạo nội tuyến và trả về đường dẫn phương tiện cuối trong kết quả công cụ.

### Workflow ComfyUI

* ### Cấu hình workflow

Cấu hình `plugins.entries.comfy.config.music` với JSON workflow và các nút prompt/đầu ra.

* ### Xác thực đám mây (tùy chọn)

Với Comfy Cloud, đặt `COMFY_API_KEY` hoặc `COMFY_CLOUD_API_KEY`.

* ### Gọi công cụ

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Ví dụ prompt:

textCopy code
[code]
    Generate a cinematic piano track with soft strings and no vocals.
[/code]

textCopy code
[code]
    Generate an energetic chiptune loop about launching a rocket at sunrise.
[/code]

## Nhà cung cấp được hỗ trợ

Nhà cung cấp | Model mặc định | Đầu vào tham chiếu | Điều khiển được hỗ trợ | Xác thực  
---|---|---|---|---  
ComfyUI | `workflow` | Tối đa 1 ảnh | Nhạc hoặc âm thanh do workflow định nghĩa | `COMFY_API_KEY`, `COMFY_CLOUD_API_KEY`  
Google | `lyria-3-clip-preview` | Tối đa 10 ảnh | `lyrics`, `instrumental`, `format` | `GEMINI_API_KEY`, `GOOGLE_API_KEY`  
MiniMax | `music-2.6` | Không có | `lyrics`, `instrumental`, `durationSeconds`, `format=mp3` | `MINIMAX_API_KEY` hoặc MiniMax OAuth  
  
### Ma trận năng lực

Hợp đồng chế độ tường minh được `music_generate`, các kiểm thử hợp đồng và lượt quét live dùng chung sử dụng:

Nhà cung cấp | `generate` | `edit` | Giới hạn chỉnh sửa | Làn live dùng chung  
---|---|---|---|---  
ComfyUI | ✓ | ✓ | 1 ảnh | Không nằm trong lượt quét dùng chung; được bao phủ bởi `extensions/comfy/comfy.live.test.ts`  
Google | ✓ | ✓ | 10 ảnh | `generate`, `edit`  
MiniMax | ✓ | — | Không có | `generate`  
  
Dùng `action: "list"` để kiểm tra các nhà cung cấp và model dùng chung khả dụng lúc chạy:

textCopy code
[code]
    /tool music_generate action=list
[/code]

Dùng `action: "status"` để kiểm tra tác vụ nhạc đang hoạt động được phiên hỗ trợ:

textCopy code
[code]
    /tool music_generate action=status
[/code]

Ví dụ tạo trực tiếp:

textCopy code
[code]
    /tool music_generate prompt="Dreamy lo-fi hip hop with vinyl texture and gentle rain" instrumental=true
[/code]

## Tham số công cụ

Prompt tạo nhạc. Bắt buộc với `action: "generate"`.

`"status"` trả về tác vụ phiên hiện tại; `"list"` kiểm tra nhà cung cấp.

Ghi đè nhà cung cấp/model (ví dụ `google/lyria-3-pro-preview`, `comfy/workflow`).

Lời bài hát tùy chọn khi nhà cung cấp hỗ trợ đầu vào lời bài hát tường minh.

Yêu cầu đầu ra chỉ nhạc không lời khi nhà cung cấp hỗ trợ.

Đường dẫn hoặc URL của một ảnh tham chiếu.

Nhiều ảnh tham chiếu (tối đa 10 trên các nhà cung cấp hỗ trợ).

Thời lượng mục tiêu tính bằng giây khi nhà cung cấp hỗ trợ gợi ý thời lượng.

Gợi ý định dạng đầu ra khi nhà cung cấp hỗ trợ.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Thời gian chờ yêu cầu nhà cung cấp tùy chọn tính bằng mili giây. Khi bỏ qua, OpenClaw dùng `agents.defaults.musicGenerationModel.timeoutMs` nếu đã cấu hình. Các giá trị dưới 10000ms được nâng lên 10000ms và được báo cáo trong kết quả công cụ. OPENCLAW_DOCS_MARKER:paramClose:

## Hành vi bất đồng bộ

Tạo nhạc có phiên hỗ trợ chạy dưới dạng tác vụ nền:

  * **Tác vụ nền:** `music_generate` tạo một tác vụ nền, trả về phản hồi đã bắt đầu/tác vụ ngay lập tức, và đăng bản nhạc hoàn chỉnh sau đó trong một tin nhắn agent tiếp theo.
  * **Ngăn trùng lặp:** khi một tác vụ đang `queued` hoặc `running`, các lệnh gọi `music_generate` sau trong cùng phiên trả về trạng thái tác vụ thay vì bắt đầu một lượt tạo khác. Dùng `action: "status"` để kiểm tra rõ ràng.
  * **Tra cứu trạng thái:** `openclaw tasks list` hoặc `openclaw tasks show <taskId>` kiểm tra trạng thái đã xếp hàng, đang chạy và trạng thái cuối.
  * **Đánh thức khi hoàn tất:** OpenClaw chèn một sự kiện hoàn tất nội bộ trở lại cùng phiên để model có thể tự viết phần theo dõi hiển thị cho người dùng.
  * **Gợi ý prompt:** các lượt người dùng/thủ công sau trong cùng phiên nhận một gợi ý runtime nhỏ khi tác vụ nhạc đang chạy, để model không gọi `music_generate` lại một cách mù quáng.
  * **Dự phòng không phiên:** các ngữ cảnh trực tiếp/cục bộ không có phiên agent thật sẽ chạy nội tuyến và trả về kết quả âm thanh cuối trong cùng lượt.


### Vòng đời tác vụ

Trạng thái | Ý nghĩa  
---|---  
`queued` | Tác vụ đã tạo, đang chờ nhà cung cấp chấp nhận.  
`running` | Nhà cung cấp đang xử lý (thường 30 giây đến 3 phút tùy nhà cung cấp và thời lượng).  
`succeeded` | Bản nhạc đã sẵn sàng; agent được đánh thức và đăng vào cuộc trò chuyện.  
`failed` | Lỗi nhà cung cấp hoặc hết thời gian chờ; agent được đánh thức kèm chi tiết lỗi.  
  
Kiểm tra trạng thái từ CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

## Cấu hình

### Chọn model

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",        fallbacks: ["minimax/music-2.6"],      },    },  },}
[/code]

### Thứ tự chọn nhà cung cấp

OpenClaw thử các nhà cung cấp theo thứ tự này:

  1. Tham số `model` từ lệnh gọi công cụ (nếu agent chỉ định).
  2. `musicGenerationModel.primary` từ cấu hình.
  3. `musicGenerationModel.fallbacks` theo thứ tự.
  4. Tự động phát hiện chỉ bằng mặc định của nhà cung cấp có xác thực: 
     * nhà cung cấp mặc định hiện tại trước;
     * các nhà cung cấp tạo nhạc đã đăng ký còn lại theo thứ tự provider-id.


Nếu một nhà cung cấp thất bại, ứng viên tiếp theo sẽ được thử tự động. Nếu tất cả đều thất bại, lỗi sẽ bao gồm chi tiết từ từng lần thử.

Đặt `agents.defaults.mediaGenerationAutoProviderFallback: false` để chỉ dùng các mục `model`, `primary` và `fallbacks` tường minh.

## Ghi chú nhà cung cấp

ComfyUI

Hoạt động theo workflow và phụ thuộc vào đồ thị đã cấu hình cùng ánh xạ nút cho các trường prompt/đầu ra. Plugin `comfy` tích hợp sẵn kết nối vào công cụ `music_generate` dùng chung thông qua registry nhà cung cấp tạo nhạc.

Google (Lyria 3)

Dùng tạo theo lô Lyria 3. Luồng tích hợp sẵn hiện tại hỗ trợ prompt, văn bản lời bài hát tùy chọn và ảnh tham chiếu tùy chọn.

MiniMax

Dùng endpoint theo lô `music_generation`. Hỗ trợ prompt, lời bài hát tùy chọn, chế độ nhạc không lời, điều hướng thời lượng và đầu ra mp3 thông qua xác thực khóa API `minimax` hoặc OAuth `minimax-portal`.

## Chọn đường dẫn phù hợp

  * **Được hỗ trợ bởi nhà cung cấp dùng chung** khi bạn muốn chọn model, chuyển dự phòng nhà cung cấp và luồng tác vụ/trạng thái bất đồng bộ tích hợp sẵn.
  * **Đường dẫn Plugin (ComfyUI)** khi bạn cần đồ thị workflow tùy chỉnh hoặc một nhà cung cấp không thuộc năng lực nhạc tích hợp dùng chung.


Nếu bạn đang gỡ lỗi hành vi dành riêng cho ComfyUI, xem [ComfyUI](</vi/providers/comfy>). Nếu bạn đang gỡ lỗi hành vi nhà cung cấp dùng chung, hãy bắt đầu với [Google (Gemini)](</vi/providers/google>) hoặc [MiniMax](</vi/providers/minimax>).

## Chế độ năng lực của nhà cung cấp

Hợp đồng tạo nhạc dùng chung hỗ trợ khai báo chế độ tường minh:

  * `generate` cho việc tạo chỉ bằng prompt.
  * `edit` khi yêu cầu bao gồm một hoặc nhiều ảnh tham chiếu.


Các triển khai nhà cung cấp mới nên ưu tiên các khối chế độ tường minh:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxTracks: 1,    supportsLyrics: true,    supportsFormat: true,  },  edit: {    enabled: true,    maxTracks: 1,    maxInputImages: 1,    supportsFormat: true,  },}
[/code]

Các trường phẳng cũ như `maxInputImages`, `supportsLyrics` và `supportsFormat` **không** đủ để quảng bá hỗ trợ chỉnh sửa. Nhà cung cấp nên khai báo `generate` và `edit` tường minh để kiểm thử live, kiểm thử hợp đồng và công cụ `music_generate` dùng chung có thể xác thực hỗ trợ chế độ một cách xác định.

## Kiểm thử live

Phạm vi live chọn tham gia cho các nhà cung cấp tích hợp dùng chung:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/music-generation-providers.live.test.ts
[/code]

Wrapper repo:

bashCopy code
[code]
    pnpm test:live:media music
[/code]

Tệp live này tải các biến môi trường nhà cung cấp bị thiếu từ `~/.profile`, mặc định ưu tiên khóa API live/env trước các hồ sơ xác thực đã lưu trữ, và chạy cả phạm vi `generate` lẫn `edit` đã khai báo khi nhà cung cấp bật chế độ chỉnh sửa. Phạm vi hiện tại:

  * `google`: `generate` cộng với `edit`
  * `minimax`: chỉ `generate`
  * `comfy`: phạm vi live Comfy riêng, không phải sweep nhà cung cấp dùng chung


Bật tùy chọn phạm vi live cho đường dẫn nhạc ComfyUI đi kèm:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Tệp live Comfy cũng bao phủ các quy trình ảnh và video comfy khi các phần đó được cấu hình.

## Liên quan

  * [Tác vụ nền](</vi/automation/tasks>) — theo dõi tác vụ cho các lần chạy `music_generate` tách rời
  * [ComfyUI](</vi/providers/comfy>)
  * [Tham chiếu cấu hình](</vi/gateway/config-agents#agent-defaults>) — cấu hình `musicGenerationModel`
  * [Google (Gemini)](</vi/providers/google>)
  * [MiniMax](</vi/providers/minimax>)
  * [Mô hình](</vi/concepts/models>) — cấu hình mô hình và chuyển đổi dự phòng
  * [Tổng quan về công cụ](</vi/tools>)


Was this useful?YesNo