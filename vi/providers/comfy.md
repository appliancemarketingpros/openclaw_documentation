---
title: ComfyUI
source_url: https://docs.openclaw.ai/vi/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw đi kèm Plugin `comfy` được tích hợp sẵn cho các lần chạy ComfyUI theo quy trình làm việc. Plugin này hoàn toàn dựa trên quy trình làm việc, vì vậy OpenClaw không cố ánh xạ các điều khiển chung như `size`, `aspectRatio`, `resolution`, `durationSeconds`, hoặc kiểu TTS vào đồ thị của bạn.

Thuộc tính | Chi tiết  
---|---  
Nhà cung cấp | `comfy`  
Mô hình | `comfy/workflow`  
Bề mặt dùng chung | `image_generate`, `video_generate`, `music_generate`  
Xác thực | Không cần cho ComfyUI cục bộ; `COMFY_API_KEY` hoặc `COMFY_CLOUD_API_KEY` cho Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` và Comfy Cloud `/api/*`  
  
## Hỗ trợ những gì

  * Tạo hình ảnh từ JSON quy trình làm việc
  * Chỉnh sửa hình ảnh với 1 hình ảnh tham chiếu đã tải lên
  * Tạo video từ JSON quy trình làm việc
  * Tạo video với 1 hình ảnh tham chiếu đã tải lên
  * Tạo nhạc hoặc âm thanh thông qua công cụ dùng chung `music_generate`
  * Tải xuống đầu ra từ một node đã cấu hình hoặc tất cả các node đầu ra khớp


## Bắt đầu

Chọn giữa việc chạy ComfyUI trên máy của bạn hoặc sử dụng Comfy Cloud.

### Cục bộ

**Phù hợp nhất cho:** chạy phiên bản ComfyUI của riêng bạn trên máy hoặc LAN.

* ### Khởi động ComfyUI cục bộ

Đảm bảo phiên bản ComfyUI cục bộ của bạn đang chạy (mặc định là `http://127.0.0.1:8188`).

* ### Chuẩn bị JSON quy trình làm việc của bạn

Xuất hoặc tạo tệp JSON quy trình làm việc ComfyUI. Ghi lại ID node cho node nhập lời nhắc và node đầu ra mà bạn muốn OpenClaw đọc từ đó.

* ### Cấu hình nhà cung cấp

Đặt `mode: "local"` và trỏ đến tệp quy trình làm việc của bạn. Đây là ví dụ hình ảnh tối thiểu:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Đặt mô hình mặc định

Trỏ OpenClaw đến mô hình `comfy/workflow` cho năng lực bạn đã cấu hình:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Xác minh

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**Phù hợp nhất cho:** chạy quy trình làm việc trên Comfy Cloud mà không cần quản lý tài nguyên GPU cục bộ.

* ### Lấy khóa API

Đăng ký tại [comfy.org](<https://comfy.org>) và tạo khóa API từ bảng điều khiển tài khoản của bạn.

* ### Đặt khóa API

Cung cấp khóa của bạn thông qua một trong các phương thức sau:

bashCopy code
[code]
    # Environment variable (preferred)export COMFY_API_KEY="your-key" # Alternative environment variableexport COMFY_CLOUD_API_KEY="your-key" # Or inline in configopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Chuẩn bị JSON quy trình làm việc của bạn

Xuất hoặc tạo tệp JSON quy trình làm việc ComfyUI. Ghi lại ID node cho node nhập lời nhắc và node đầu ra.

* ### Cấu hình nhà cung cấp

Đặt `mode: "cloud"` và trỏ đến tệp quy trình làm việc của bạn:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Đặt mô hình mặc định

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Xác minh

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Cấu hình

Comfy hỗ trợ các thiết lập kết nối cấp cao nhất dùng chung cùng với các phần quy trình làm việc theo từng năng lực (`image`, `video`, `music`):

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Khóa dùng chung

Khóa | Kiểu | Mô tả  
---|---|---  
`mode` | `"local"` hoặc `"cloud"` | Chế độ kết nối.  
`baseUrl` | string | Mặc định là `http://127.0.0.1:8188` cho cục bộ hoặc `https://cloud.comfy.org` cho đám mây.  
`apiKey` | string | Khóa nội tuyến tùy chọn, thay thế cho biến môi trường `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | Cho phép `baseUrl` riêng tư/LAN trong chế độ đám mây.  
  
### Khóa theo từng năng lực

Các khóa này áp dụng bên trong các phần `image`, `video`, hoặc `music`:

Khóa | Bắt buộc | Mặc định | Mô tả  
---|---|---|---  
`workflow` hoặc `workflowPath` | Có | \-- | Đường dẫn đến tệp JSON quy trình làm việc ComfyUI.  
`promptNodeId` | Có | \-- | ID node nhận lời nhắc văn bản.  
`promptInputName` | Không | `"text"` | Tên đầu vào trên node lời nhắc.  
`outputNodeId` | Không | \-- | ID node để đọc đầu ra từ đó. Nếu bỏ qua, tất cả node đầu ra khớp sẽ được dùng.  
`pollIntervalMs` | Không | \-- | Khoảng thời gian thăm dò tính bằng mili giây để hoàn tất tác vụ.  
`timeoutMs` | Không | \-- | Thời gian chờ tính bằng mili giây cho lần chạy quy trình làm việc.  
  
Các phần `image` và `video` cũng hỗ trợ:

Khóa | Bắt buộc | Mặc định | Mô tả  
---|---|---|---  
`inputImageNodeId` | Có (khi truyền một hình ảnh tham chiếu) | \-- | ID node nhận hình ảnh tham chiếu đã tải lên.  
`inputImageInputName` | Không | `"image"` | Tên đầu vào trên node hình ảnh.  
  
## Chi tiết quy trình làm việc

Quy trình làm việc hình ảnh

Đặt mô hình hình ảnh mặc định thành `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Ví dụ chỉnh sửa hình ảnh tham chiếu:**

Để bật chỉnh sửa hình ảnh với một hình ảnh tham chiếu đã tải lên, hãy thêm `inputImageNodeId` vào cấu hình hình ảnh của bạn:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Quy trình làm việc video

Đặt mô hình video mặc định thành `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Các quy trình làm việc video của Comfy hỗ trợ chuyển văn bản thành video và hình ảnh thành video thông qua đồ thị đã cấu hình.

Quy trình làm việc nhạc

Plugin tích hợp sẵn đăng ký một nhà cung cấp tạo nhạc cho đầu ra âm thanh hoặc nhạc được định nghĩa bằng quy trình làm việc, được hiển thị thông qua công cụ dùng chung `music_generate`:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Sử dụng phần cấu hình `music` để trỏ đến JSON quy trình làm việc âm thanh và node đầu ra của bạn.

Khả năng tương thích ngược

Cấu hình hình ảnh cấp cao nhất hiện có (không có phần `image` lồng nhau) vẫn hoạt động:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw coi hình dạng kế thừa đó là cấu hình quy trình làm việc hình ảnh. Bạn không cần di chuyển ngay lập tức, nhưng các phần `image` / `video` / `music` lồng nhau được khuyến nghị cho thiết lập mới.

Kiểm thử trực tiếp

Phạm vi kiểm thử trực tiếp tùy chọn có sẵn cho Plugin tích hợp sẵn:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Kiểm thử trực tiếp bỏ qua từng trường hợp hình ảnh, video, hoặc nhạc riêng lẻ trừ khi phần quy trình làm việc Comfy tương ứng được cấu hình.

## Liên quan

[**Tạo hình ảnh** Cấu hình và cách sử dụng công cụ tạo hình ảnh. ](</vi/tools/image-generation>) [**Tạo video** Cấu hình và cách sử dụng công cụ tạo video. ](</vi/tools/video-generation>) [**Tạo nhạc** Thiết lập công cụ tạo nhạc và âm thanh. ](</vi/tools/music-generation>) [**Danh mục nhà cung cấp** Tổng quan về tất cả nhà cung cấp và tham chiếu mô hình. ](</vi/providers>) [**Tham chiếu cấu hình** Tham chiếu cấu hình đầy đủ, bao gồm mặc định của tác tử. ](</vi/gateway/config-agents#agent-defaults>)

Was this useful?YesNo