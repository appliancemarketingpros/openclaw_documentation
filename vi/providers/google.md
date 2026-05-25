---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/vi/providers/google
scraped_at: 2026-05-25
---

Plugin Google cung cấp quyền truy cập vào các mô hình Gemini thông qua Google AI Studio, cùng với tạo hình ảnh, hiểu nội dung phương tiện (hình ảnh/âm thanh/video), chuyển văn bản thành giọng nói và tìm kiếm web qua Gemini Grounding.

  * Nhà cung cấp: `google`
  * Xác thực: `GEMINI_API_KEY` hoặc `GOOGLE_API_KEY`
  * API: Google Gemini API
  * Tùy chọn thời gian chạy: nhà cung cấp/mô hình `agentRuntime.id: "google-gemini-cli"` tái sử dụng OAuth của Gemini CLI trong khi vẫn giữ tham chiếu mô hình ở dạng chuẩn là `google/*`.


## Bắt đầu

Chọn phương thức xác thực bạn muốn và làm theo các bước thiết lập.

### Khóa API

**Phù hợp nhất cho:** quyền truy cập Gemini API tiêu chuẩn thông qua Google AI Studio.

* ### Chạy quy trình giới thiệu

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

Hoặc truyền khóa trực tiếp:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Đặt mô hình mặc định

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Xác minh mô hình có sẵn

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**Phù hợp nhất cho:** tái sử dụng thông tin đăng nhập Gemini CLI hiện có qua PKCE OAuth thay vì dùng một khóa API riêng.

* ### Cài đặt Gemini CLI

Lệnh cục bộ `gemini` phải có sẵn trên `PATH`.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw hỗ trợ cả bản cài đặt Homebrew và bản cài đặt npm toàn cục, bao gồm các bố cục Windows/npm phổ biến.

* ### Đăng nhập qua OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Xác minh mô hình có sẵn

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * Mô hình mặc định: `google/gemini-3.1-pro-preview`
  * Thời gian chạy: `google-gemini-cli`
  * Bí danh: `gemini-cli`


ID mô hình Gemini API của Gemini 3.1 Pro là `gemini-3.1-pro-preview`. OpenClaw chấp nhận dạng ngắn hơn `google/gemini-3.1-pro` như một bí danh tiện lợi và chuẩn hóa nó trước khi gọi nhà cung cấp.

**Biến môi trường:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(Hoặc các biến thể `GEMINI_CLI_*`.)

Tham chiếu mô hình `google-gemini-cli/*` là các bí danh tương thích cũ. Cấu hình mới nên dùng tham chiếu mô hình `google/*` cùng với thời gian chạy `google-gemini-cli` khi muốn thực thi Gemini CLI cục bộ.

## Khả năng

Khả năng | Được hỗ trợ  
---|---  
Hoàn thành hội thoại | Có  
Tạo hình ảnh | Có  
Tạo nhạc | Có  
Chuyển văn bản thành giọng nói | Có  
Giọng nói thời gian thực | Có (Google Live API)  
Hiểu hình ảnh | Có  
Chép lời âm thanh | Có  
Hiểu video | Có  
Tìm kiếm web (Grounding) | Có  
Suy nghĩ/lập luận | Có (Gemini 2.5+ / Gemini 3+)  
Mô hình Gemma 4 | Có  
  
## Tìm kiếm web

Nhà cung cấp tìm kiếm web `gemini` đi kèm sử dụng grounding Google Search của Gemini. Cấu hình một khóa tìm kiếm chuyên dụng trong `plugins.entries.google.config.webSearch`, hoặc để nó tái sử dụng `models.providers.google.apiKey` sau `GEMINI_API_KEY`:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

Thứ tự ưu tiên thông tin xác thực là `webSearch.apiKey` chuyên dụng, rồi `GEMINI_API_KEY`, rồi `models.providers.google.apiKey`. `webSearch.baseUrl` là tùy chọn và tồn tại cho proxy của người vận hành hoặc các điểm cuối Gemini API tương thích; khi bị bỏ qua, tìm kiếm web Gemini tái sử dụng `models.providers.google.baseUrl`. Xem [Tìm kiếm Gemini](</vi/tools/gemini-search>) để biết hành vi công cụ dành riêng cho nhà cung cấp.

## Tạo hình ảnh

Nhà cung cấp tạo hình ảnh `google` đi kèm mặc định dùng `google/gemini-3.1-flash-image-preview`.

  * Cũng hỗ trợ `google/gemini-3-pro-image-preview`
  * Tạo: tối đa 4 hình ảnh mỗi yêu cầu
  * Chế độ chỉnh sửa: bật, tối đa 5 hình ảnh đầu vào
  * Điều khiển hình học: `size`, `aspectRatio` và `resolution`


Để dùng Google làm nhà cung cấp hình ảnh mặc định:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## Tạo video

Plugin `google` đi kèm cũng đăng ký tạo video thông qua công cụ dùng chung `video_generate`.

  * Mô hình video mặc định: `google/veo-3.1-fast-generate-preview`
  * Chế độ: luồng văn bản-thành-video, hình ảnh-thành-video và tham chiếu một video
  * Hỗ trợ `aspectRatio` (`16:9`, `9:16`) và `resolution` (`720P`, `1080P`); đầu ra âm thanh hiện không được Veo hỗ trợ
  * Thời lượng được hỗ trợ: **4, 6 hoặc 8 giây** (các giá trị khác sẽ được làm khớp về giá trị được phép gần nhất)


Để dùng Google làm nhà cung cấp video mặc định:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## Tạo nhạc

Plugin `google` đi kèm cũng đăng ký tạo nhạc thông qua công cụ dùng chung `music_generate`.

  * Mô hình nhạc mặc định: `google/lyria-3-clip-preview`
  * Cũng hỗ trợ `google/lyria-3-pro-preview`
  * Điều khiển lời nhắc: `lyrics` và `instrumental`
  * Định dạng đầu ra: mặc định là `mp3`, cộng thêm `wav` trên `google/lyria-3-pro-preview`
  * Đầu vào tham chiếu: tối đa 10 hình ảnh
  * Các lần chạy dựa trên phiên sẽ tách ra qua luồng tác vụ/trạng thái dùng chung, bao gồm `action: "status"`


Để dùng Google làm nhà cung cấp nhạc mặc định:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## Chuyển văn bản thành giọng nói

Nhà cung cấp giọng nói `google` đi kèm sử dụng đường dẫn TTS của Gemini API với `gemini-3.1-flash-tts-preview`.

  * Giọng mặc định: `Kore`
  * Xác thực: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` hoặc `GOOGLE_API_KEY`
  * Đầu ra: WAV cho tệp đính kèm TTS thông thường, Opus cho mục tiêu ghi chú thoại, PCM cho Talk/điện thoại
  * Đầu ra ghi chú thoại: Google PCM được bọc dưới dạng WAV và chuyển mã sang Opus 48 kHz bằng `ffmpeg`


Đường dẫn TTS Gemini theo lô của Google trả về âm thanh đã tạo trong phản hồi `generateContent` hoàn tất. Để có các cuộc trò chuyện bằng giọng nói có độ trễ thấp nhất, hãy dùng nhà cung cấp giọng nói thời gian thực của Google dựa trên Gemini Live API thay vì TTS theo lô.

Để dùng Google làm nhà cung cấp TTS mặc định:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS sử dụng lời nhắc ngôn ngữ tự nhiên để điều khiển phong cách. Đặt `audioProfile` để thêm một lời nhắc phong cách có thể tái sử dụng trước văn bản được đọc. Đặt `speakerName` khi văn bản lời nhắc của bạn nhắc đến một người nói có tên.

Gemini API TTS cũng chấp nhận các thẻ âm thanh biểu cảm trong ngoặc vuông trong văn bản, chẳng hạn như `[whispers]` hoặc `[laughs]`. Để giữ các thẻ khỏi phản hồi trò chuyện hiển thị trong khi vẫn gửi chúng đến TTS, hãy đặt chúng bên trong một khối `[[tts:text]]...[[/tts:text]]`:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## Giọng nói thời gian thực

Plugin `google` đi kèm đăng ký một nhà cung cấp giọng nói thời gian thực dựa trên Gemini Live API cho các cầu nối âm thanh backend như Voice Call và Google Meet.

Cài đặt | Đường dẫn cấu hình | Mặc định  
---|---|---  
Mô hình | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
Giọng nói | `...google.voice` | `Kore`  
Nhiệt độ | `...google.temperature` | (chưa đặt)  
Độ nhạy bắt đầu VAD | `...google.startSensitivity` | (chưa đặt)  
Độ nhạy kết thúc VAD | `...google.endSensitivity` | (chưa đặt)  
Thời lượng im lặng | `...google.silenceDurationMs` | (chưa đặt)  
Xử lý hoạt động | `...google.activityHandling` | Mặc định của Google, `start-of-activity-interrupts`  
Phạm vi lượt | `...google.turnCoverage` | Mặc định của Google, `only-activity`  
Tắt VAD tự động | `...google.automaticActivityDetectionDisabled` | `false`  
Khôi phục phiên | `...google.sessionResumption` | `true`  
Nén ngữ cảnh | `...google.contextWindowCompression` | `true`  
Khóa API | `...google.apiKey` | Dự phòng về `models.providers.google.apiKey`, `GEMINI_API_KEY`, hoặc `GOOGLE_API_KEY`  
  
Ví dụ cấu hình thời gian thực cho Voice Call:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

Để xác minh trực tiếp dành cho maintainer, hãy chạy `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`. Bài smoke cũng bao phủ các đường dẫn backend/WebRTC của OpenAI; nhánh Google tạo cùng dạng token Live API có ràng buộc mà Control UI Talk dùng, mở endpoint WebSocket của trình duyệt, gửi payload thiết lập ban đầu và chờ `setupComplete`.

## Cấu hình nâng cao

Tái sử dụng cache Gemini trực tiếp

Với các lần chạy Gemini API trực tiếp (`api: "google-generative-ai"`), OpenClaw truyền handle `cachedContent` đã cấu hình tới các yêu cầu Gemini.

  * Cấu hình tham số theo từng mô hình hoặc toàn cục bằng `cachedContent` hoặc `cached_content` cũ
  * Nếu có cả hai, `cachedContent` được ưu tiên
  * Giá trị ví dụ: `cachedContents/prebuilt-context`
  * Mức sử dụng cache-hit của Gemini được chuẩn hóa thành `cacheRead` của OpenClaw từ `cachedContentTokenCount` thượng nguồn

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Ghi chú sử dụng JSON của Gemini CLI

Khi dùng nhà cung cấp OAuth `google-gemini-cli`, OpenClaw chuẩn hóa đầu ra JSON của CLI như sau:

  * Văn bản trả lời đến từ trường `response` trong JSON của CLI.
  * Mức sử dụng dự phòng về `stats` khi CLI để trống `usage`.
  * `stats.cached` được chuẩn hóa thành `cacheRead` của OpenClaw.
  * Nếu thiếu `stats.input`, OpenClaw suy ra token đầu vào từ `stats.input_tokens - stats.cached`.

Thiết lập môi trường và daemon

Nếu Gateway chạy dưới dạng daemon (launchd/systemd), hãy đảm bảo `GEMINI_API_KEY` có sẵn cho tiến trình đó (ví dụ, trong `~/.openclaw/.env` hoặc qua `env.shellEnv`).

## Liên quan

[**Chọn mô hình** Chọn nhà cung cấp, tham chiếu mô hình và hành vi chuyển đổi dự phòng. ](</vi/concepts/model-providers>) [**Tạo hình ảnh** Tham số công cụ hình ảnh dùng chung và lựa chọn nhà cung cấp. ](</vi/tools/image-generation>) [**Tạo video** Tham số công cụ video dùng chung và lựa chọn nhà cung cấp. ](</vi/tools/video-generation>) [**Tạo nhạc** Tham số công cụ âm nhạc dùng chung và lựa chọn nhà cung cấp. ](</vi/tools/music-generation>)

Was this useful?YesNo