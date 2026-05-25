---
title: Hiểu nội dung đa phương tiện
source_url: https://docs.openclaw.ai/vi/nodes/media-understanding
scraped_at: 2026-05-25
---

OpenClaw có thể **tóm tắt phương tiện đầu vào** (hình ảnh/âm thanh/video) trước khi quy trình trả lời chạy. Nó tự động phát hiện khi có công cụ cục bộ hoặc khóa nhà cung cấp khả dụng, và có thể được tắt hoặc tùy chỉnh. Nếu tính năng hiểu bị tắt, các mô hình vẫn nhận các tệp/URL gốc như thường lệ.

Hành vi phương tiện theo từng nhà cung cấp được đăng ký bởi các Plugin của nhà cung cấp, trong khi lõi OpenClaw sở hữu cấu hình `tools.media` dùng chung, thứ tự dự phòng và tích hợp quy trình trả lời.

## Mục tiêu

  * Tùy chọn: tiền xử lý phương tiện đầu vào thành văn bản ngắn để định tuyến nhanh hơn + phân tích lệnh tốt hơn.
  * Luôn giữ nguyên việc gửi phương tiện gốc đến mô hình.
  * Hỗ trợ **API nhà cung cấp** và **dự phòng CLI**.
  * Cho phép nhiều mô hình với dự phòng theo thứ tự (lỗi/kích thước/hết thời gian).


## Hành vi cấp cao

* ### Thu thập tệp đính kèm

Thu thập tệp đính kèm đầu vào (`MediaPaths`, `MediaUrls`, `MediaTypes`).

* ### Chọn theo từng năng lực

Với mỗi năng lực được bật (hình ảnh/âm thanh/video), chọn tệp đính kèm theo chính sách (mặc định: **đầu tiên**).

* ### Chọn mô hình

Chọn mục mô hình đủ điều kiện đầu tiên (kích thước + năng lực + xác thực).

* ### Dự phòng khi thất bại

Nếu một mô hình thất bại hoặc phương tiện quá lớn, **dự phòng sang mục tiếp theo**.

* ### Áp dụng khối thành công

Khi thành công:

  * `Body` trở thành khối `[Image]`, `[Audio]`, hoặc `[Video]`.
  * Âm thanh đặt `{{Transcript}}`; phân tích lệnh dùng văn bản chú thích khi có, nếu không thì dùng bản chép lời.
  * Chú thích được giữ dưới dạng `User text:` bên trong khối.


Nếu việc hiểu thất bại hoặc bị tắt, **luồng trả lời vẫn tiếp tục** với nội dung gốc + tệp đính kèm.

## Tổng quan cấu hình

`tools.media` hỗ trợ **mô hình dùng chung** cùng các ghi đè theo từng năng lực:

Khóa cấp cao nhất

  * `tools.media.models`: danh sách mô hình dùng chung (dùng `capabilities` để kiểm soát).
  * `tools.media.image` / `tools.media.audio` / `tools.media.video`: 
    * giá trị mặc định (`prompt`, `maxChars`, `maxBytes`, `timeoutSeconds`, `language`)
    * ghi đè nhà cung cấp (`baseUrl`, `headers`, `providerOptions`)
    * tùy chọn âm thanh Deepgram qua `tools.media.audio.providerOptions.deepgram`
    * điều khiển lặp lại bản chép lời âm thanh (`echoTranscript`, mặc định `false`; `echoFormat`)
    * **danh sách`models` theo từng năng lực** tùy chọn (được ưu tiên trước mô hình dùng chung)
    * chính sách `attachments` (`mode`, `maxAttachments`, `prefer`)
    * `scope` (kiểm soát tùy chọn theo channel/chatType/session key)
  * `tools.media.concurrency`: số lần chạy năng lực đồng thời tối đa (mặc định **2**).


json5Copy code
[code]
    {  tools: {    media: {      models: [        /* shared list */      ],      image: {        /* optional overrides */      },      audio: {        /* optional overrides */        echoTranscript: true,        echoFormat: '📝 "{transcript}"',      },      video: {        /* optional overrides */      },    },  },}
[/code]

### Mục mô hình

Mỗi mục `models[]` có thể là **nhà cung cấp** hoặc **CLI** :

### Mục nhà cung cấp

json5Copy code
[code]
    {  type: "provider", // default if omitted  provider: "openai",  model: "gpt-5.5",  prompt: "Describe the image in <= 500 chars.",  maxChars: 500,  maxBytes: 10485760,  timeoutSeconds: 60,  capabilities: ["image"], // optional, used for multi-modal entries  profile: "vision-profile",  preferredProfile: "vision-fallback",}
[/code]

### Mục CLI

json5Copy code
[code]
    {  type: "cli",  command: "gemini",  args: [    "-m",    "gemini-3-flash",    "--allowed-tools",    "read_file",    "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",  ],  maxChars: 500,  maxBytes: 52428800,  timeoutSeconds: 120,  capabilities: ["video", "image"],}
[/code]

Mẫu CLI cũng có thể dùng:

  * `{{MediaDir}}` (thư mục chứa tệp phương tiện)
  * `{{OutputDir}}` (thư mục nháp được tạo cho lần chạy này)
  * `{{OutputBase}}` (đường dẫn cơ sở của tệp nháp, không có phần mở rộng)


## Mặc định và giới hạn

Mặc định khuyến nghị:

  * `maxChars`: **500** cho hình ảnh/video (ngắn, thân thiện với lệnh)
  * `maxChars`: **không đặt** cho âm thanh (bản chép lời đầy đủ trừ khi bạn đặt giới hạn)
  * `maxBytes`: 
    * hình ảnh: **10MB**
    * âm thanh: **20MB**
    * video: **50MB**


Quy tắc

  * Nếu phương tiện vượt quá `maxBytes`, mô hình đó bị bỏ qua và **mô hình tiếp theo được thử**.
  * Tệp âm thanh nhỏ hơn **1024 byte** được xem là trống/hỏng và bị bỏ qua trước khi chép lời bằng nhà cung cấp/CLI; ngữ cảnh trả lời đầu vào nhận một bản chép lời giữ chỗ xác định để tác nhân biết ghi chú quá nhỏ.
  * Nếu mô hình trả về nhiều hơn `maxChars`, đầu ra sẽ được cắt bớt.
  * `prompt` mặc định là câu đơn giản "Describe the {media}." cộng với hướng dẫn `maxChars` (chỉ hình ảnh/video).
  * Nếu mô hình hình ảnh chính đang hoạt động đã hỗ trợ thị giác nguyên bản, OpenClaw bỏ qua khối tóm tắt `[Image]` và truyền hình ảnh gốc vào mô hình thay vào đó.
  * Nếu mô hình chính Gateway/WebChat chỉ hỗ trợ văn bản, tệp đính kèm hình ảnh được giữ dưới dạng tham chiếu `media://inbound/*` đã offload để các công cụ hình ảnh/PDF hoặc mô hình hình ảnh đã cấu hình vẫn có thể kiểm tra chúng thay vì mất tệp đính kèm.
  * Các yêu cầu `openclaw infer image describe --model <provider/model>` tường minh thì khác: chúng chạy trực tiếp nhà cung cấp/mô hình có năng lực hình ảnh đó, bao gồm các tham chiếu Ollama như `ollama/qwen2.5vl:7b`.
  * Nếu `<capability>.enabled: true` nhưng không có mô hình nào được cấu hình, OpenClaw thử **mô hình trả lời đang hoạt động** khi nhà cung cấp của nó hỗ trợ năng lực đó.


### Tự động phát hiện khả năng hiểu phương tiện (mặc định)

Nếu `tools.media.<capability>.enabled` **không** được đặt thành `false` và bạn chưa cấu hình mô hình, OpenClaw tự động phát hiện theo thứ tự này và **dừng ở tùy chọn hoạt động đầu tiên** :

* ### Mô hình trả lời đang hoạt động

Mô hình trả lời đang hoạt động khi nhà cung cấp của nó hỗ trợ năng lực.

* ### agents.defaults.imageModel

Tham chiếu chính/dự phòng `agents.defaults.imageModel` (chỉ hình ảnh). Ưu tiên tham chiếu `provider/model`. Tham chiếu trần được xác định nhà cung cấp từ các mục mô hình nhà cung cấp có năng lực hình ảnh đã cấu hình chỉ khi kết quả khớp là duy nhất.

* ### CLI cục bộ (chỉ âm thanh)

CLI cục bộ (nếu đã cài đặt):

  * `sherpa-onnx-offline` (yêu cầu `SHERPA_ONNX_MODEL_DIR` có encoder/decoder/joiner/tokens)
  * `whisper-cli` (`whisper-cpp`; dùng `WHISPER_CPP_MODEL` hoặc mô hình tiny được đóng gói)
  * `whisper` (CLI Python; tự động tải mô hình)


* ### Gemini CLI

`gemini` dùng `read_many_files`.

* ### Xác thực nhà cung cấp

  * Các mục `models.providers.*` đã cấu hình hỗ trợ năng lực được thử trước thứ tự dự phòng đóng gói sẵn.
  * Các nhà cung cấp cấu hình chỉ dành cho hình ảnh có mô hình hỗ trợ hình ảnh sẽ tự động đăng ký cho khả năng hiểu phương tiện ngay cả khi chúng không phải là Plugin nhà cung cấp đóng gói sẵn.
  * Khả năng hiểu hình ảnh Ollama có sẵn khi được chọn tường minh, ví dụ qua `agents.defaults.imageModel` hoặc `openclaw infer image describe --model ollama/<vision-model>`.


Thứ tự dự phòng đóng gói sẵn:

  * Âm thanh: OpenAI → Groq → xAI → Deepgram → OpenRouter → Google → SenseAudio → ElevenLabs → Mistral
  * Hình ảnh: OpenAI → Anthropic → Google → MiniMax → MiniMax Portal → [Z.AI](<http://Z.AI>)
  * Video: Google → Qwen → Moonshot


Để tắt tự động phát hiện, đặt:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: false,      },    },  },}
[/code]

### Hỗ trợ môi trường proxy (mô hình nhà cung cấp)

Khi khả năng hiểu phương tiện **âm thanh** và **video** dựa trên nhà cung cấp được bật, OpenClaw tôn trọng các biến môi trường proxy đầu ra tiêu chuẩn cho lệnh gọi HTTP đến nhà cung cấp:

  * `HTTPS_PROXY`
  * `HTTP_PROXY`
  * `ALL_PROXY`
  * `https_proxy`
  * `http_proxy`
  * `all_proxy`


Nếu không có biến môi trường proxy nào được đặt, khả năng hiểu phương tiện dùng kết nối trực tiếp ra ngoài. Nếu giá trị proxy không đúng định dạng, OpenClaw ghi cảnh báo và quay về tải trực tiếp.

## Năng lực (tùy chọn)

Nếu bạn đặt `capabilities`, mục đó chỉ chạy cho các loại phương tiện đó. Với danh sách dùng chung, OpenClaw có thể suy ra mặc định:

  * `openai`, `anthropic`, `minimax`: **hình ảnh**
  * `minimax-portal`: **hình ảnh**
  * `moonshot`: **hình ảnh + video**
  * `openrouter`: **hình ảnh + âm thanh**
  * `google` (Gemini API): **hình ảnh + âm thanh + video**
  * `qwen`: **hình ảnh + video**
  * `mistral`: **âm thanh**
  * `zai`: **hình ảnh**
  * `groq`: **âm thanh**
  * `xai`: **âm thanh**
  * `deepgram`: **âm thanh**
  * Bất kỳ danh mục `models.providers.<id>.models[]` nào có mô hình hỗ trợ hình ảnh: **hình ảnh**


Với mục CLI, **hãy đặt`capabilities` tường minh** để tránh các kết quả khớp bất ngờ. Nếu bạn bỏ qua `capabilities`, mục đó đủ điều kiện cho danh sách nơi nó xuất hiện.

## Ma trận hỗ trợ nhà cung cấp (tích hợp OpenClaw)

Năng lực | Tích hợp nhà cung cấp | Ghi chú  
---|---|---  
Hình ảnh | OpenAI, OpenAI Codex OAuth, Codex app-server, OpenRouter, Anthropic, Google, MiniMax, Moonshot, Qwen, [Z.AI](<http://Z.AI>), nhà cung cấp cấu hình | Plugin nhà cung cấp đăng ký hỗ trợ hình ảnh; `openai-codex/*` dùng hệ thống nhà cung cấp OAuth; `codex/*` dùng một lượt Codex app-server có giới hạn; MiniMax và MiniMax OAuth đều dùng `MiniMax-VL-01`; nhà cung cấp cấu hình có năng lực hình ảnh tự động đăng ký.  
Âm thanh | OpenAI, Groq, xAI, Deepgram, OpenRouter, Google, SenseAudio, ElevenLabs, Mistral | Chép lời bởi nhà cung cấp (Whisper/Groq/xAI/Deepgram/OpenRouter STT/Gemini/SenseAudio/Scribe/Voxtral).  
Video | Google, Qwen, Moonshot | Khả năng hiểu video của nhà cung cấp qua Plugin nhà cung cấp; khả năng hiểu video của Qwen dùng các endpoint Standard DashScope.  
  
## Hướng dẫn chọn mô hình

  * Ưu tiên mô hình thế hệ mới nhất mạnh nhất có sẵn cho từng năng lực phương tiện khi chất lượng và an toàn là quan trọng.
  * Với các tác nhân có bật công cụ đang xử lý đầu vào không đáng tin cậy, tránh các mô hình phương tiện cũ/yếu hơn.
  * Giữ ít nhất một dự phòng cho mỗi năng lực để đảm bảo khả dụng (mô hình chất lượng + mô hình nhanh hơn/rẻ hơn).
  * Dự phòng CLI (`whisper-cli`, `whisper`, `gemini`) hữu ích khi API nhà cung cấp không khả dụng.
  * Ghi chú `parakeet-mlx`: với `--output-dir`, OpenClaw đọc `<output-dir>/<media-basename>.txt` khi định dạng đầu ra là `txt` (hoặc không được chỉ định); các định dạng không phải `txt` quay về stdout.


## Chính sách tệp đính kèm

`attachments` theo từng năng lực kiểm soát tệp đính kèm nào được xử lý:

Xử lý tệp đính kèm đầu tiên được chọn hay tất cả các tệp đính kèm.

Giới hạn số lượng được xử lý.

Tùy chọn ưu tiên khi chọn trong các tệp đính kèm ứng viên.

Khi `mode: "all"`, đầu ra được gắn nhãn `[Image 1/2]`, `[Audio 2/2]`, v.v.

Hành vi trích xuất tệp đính kèm

  * Văn bản tệp được trích xuất được bọc dưới dạng **nội dung bên ngoài không đáng tin cậy** trước khi được thêm vào prompt phương tiện.
  * Khối được chèn sử dụng các dấu ranh giới rõ ràng như `<<&lt;EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` / `<<&lt;END_EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` và bao gồm một dòng siêu dữ liệu `Source: External`.
  * Đường dẫn trích xuất tệp đính kèm này cố ý bỏ qua biểu ngữ dài `SECURITY NOTICE:` để tránh làm prompt phương tiện phình to; các dấu ranh giới và siêu dữ liệu vẫn được giữ lại.
  * Nếu một tệp không có văn bản có thể trích xuất, OpenClaw chèn `[No extractable text]`.
  * Nếu một PDF chuyển sang dùng hình ảnh trang được render trong đường dẫn này, prompt phương tiện giữ chỗ dành sẵn `[PDF content rendered to images; images not forwarded to model]` vì bước trích xuất tệp đính kèm này chuyển tiếp các khối văn bản, không phải hình ảnh PDF đã render.


## Ví dụ cấu hình

### Mô hình dùng chung + ghi đè

json5Copy code
[code]
    {  tools: {    media: {      models: [        { provider: "openai", model: "gpt-5.5", capabilities: ["image"] },        {          provider: "google",          model: "gemini-3-flash-preview",          capabilities: ["image", "audio", "video"],        },        {          type: "cli",          command: "gemini",          args: [            "-m",            "gemini-3-flash",            "--allowed-tools",            "read_file",            "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",          ],          capabilities: ["image", "video"],        },      ],      audio: {        attachments: { mode: "all", maxAttachments: 2 },      },      video: {        maxChars: 500,      },    },  },}
[/code]

### Chỉ âm thanh + video

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [          { provider: "openai", model: "gpt-4o-mini-transcribe" },          {            type: "cli",            command: "whisper",            args: ["--model", "base", "{{MediaPath}}"],          },        ],      },      video: {        enabled: true,        maxChars: 500,        models: [          { provider: "google", model: "gemini-3-flash-preview" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Chỉ hình ảnh

json5Copy code
[code]
    {  tools: {    media: {      image: {        enabled: true,        maxBytes: 10485760,        maxChars: 500,        models: [          { provider: "openai", model: "gpt-5.5" },          { provider: "anthropic", model: "claude-opus-4-6" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Một mục đa phương thức

json5Copy code
[code]
    {  tools: {    media: {      image: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      audio: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      video: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },    },  },}
[/code]

## Đầu ra trạng thái

Khi hiểu phương tiện chạy, `/status` bao gồm một dòng tóm tắt ngắn:

CodeCopy code
[code]
    📎 Media: image ok (openai/gpt-5.4) · audio skipped (maxBytes)
[/code]

Dòng này hiển thị kết quả theo từng capability và nhà cung cấp/mô hình đã chọn khi áp dụng.

## Ghi chú

  * Việc hiểu là **cố gắng tối đa**. Lỗi không chặn phản hồi.
  * Tệp đính kèm vẫn được chuyển cho mô hình ngay cả khi tính năng hiểu bị tắt.
  * Dùng `scope` để giới hạn nơi tính năng hiểu chạy (ví dụ: chỉ DM).


## Liên quan

  * [Cấu hình](</vi/gateway/configuration>)
  * [Hỗ trợ hình ảnh & phương tiện](</vi/nodes/images>)


Was this useful?YesNo