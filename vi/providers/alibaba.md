---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/vi/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw cung cấp sẵn một Plugin `alibaba` đăng ký nhà cung cấp tạo video cho các mô hình Wan trên Alibaba Model Studio (tên quốc tế của DashScope). Plugin này được bật theo mặc định; bạn chỉ cần đặt API key.

Thuộc tính | Giá trị  
---|---  
ID nhà cung cấp | `alibaba`  
Plugin | đi kèm, `enabledByDefault: true`  
Biến môi trường xác thực | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (khớp đầu tiên được dùng)  
Cờ thiết lập ban đầu | `--auth-choice alibaba-model-studio-api-key`  
Cờ CLI trực tiếp | `--alibaba-model-studio-api-key <key>`  
Mô hình mặc định | `alibaba/wan2.6-t2v`  
URL cơ sở mặc định | `https://dashscope-intl.aliyuncs.com`  
  
## Bắt đầu

* ### Set an API key

Dùng quy trình thiết lập ban đầu để lưu khóa cho nhà cung cấp `alibaba`:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

Hoặc truyền khóa trực tiếp trong lúc cài đặt/thiết lập ban đầu:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

Hoặc xuất bất kỳ biến môi trường nào được chấp nhận trước khi khởi động Gateway:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Set a default video model

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Verify the provider is configured

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

Danh sách này phải bao gồm cả năm mô hình Wan đi kèm. Nếu `MODELSTUDIO_API_KEY` chưa được phân giải, `openclaw models status --json` sẽ báo thông tin xác thực còn thiếu trong `auth.unusableProfiles`.

## Các mô hình Wan tích hợp sẵn

Tham chiếu mô hình | Chế độ  
---|---  
`alibaba/wan2.6-t2v` | Văn bản thành video (mặc định)  
`alibaba/wan2.6-i2v` | Hình ảnh thành video  
`alibaba/wan2.6-r2v` | Tham chiếu thành video  
`alibaba/wan2.6-r2v-flash` | Tham chiếu thành video (nhanh)  
`alibaba/wan2.7-r2v` | Tham chiếu thành video  
  
## Khả năng và giới hạn

Nhà cung cấp đi kèm phản ánh các giới hạn của API video Wan của DashScope. Cả ba chế độ dùng chung giới hạn số video mỗi yêu cầu và giới hạn thời lượng; chỉ hình dạng đầu vào là khác nhau.

Chế độ | Số video đầu ra tối đa | Số ảnh đầu vào tối đa | Số video đầu vào tối đa | Thời lượng tối đa | Điều khiển được hỗ trợ  
---|---|---|---|---|---  
Văn bản thành video | 1 | không áp dụng | không áp dụng | 10 giây | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Hình ảnh thành video | 1 | 1 | không áp dụng | 10 giây | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Tham chiếu thành video | 1 | không áp dụng | 4 | 10 giây | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
Khi một yêu cầu bỏ qua `durationSeconds`, nhà cung cấp gửi giá trị mặc định được DashScope chấp nhận là **5 giây**. Đặt rõ `durationSeconds` trên [công cụ tạo video](</vi/tools/video-generation>) để kéo dài tối đa đến 10 giây.

## Cấu hình nâng cao

Override the DashScope base URL

Nhà cung cấp mặc định dùng điểm cuối DashScope quốc tế. Để nhắm đến điểm cuối khu vực Trung Quốc, hãy đặt:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

Nhà cung cấp loại bỏ dấu gạch chéo ở cuối trước khi tạo URL tác vụ AIGC.

Auth env priority

OpenClaw phân giải API key Alibaba từ các biến môi trường theo thứ tự này, lấy giá trị khác rỗng đầu tiên:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


Các mục `auth.profiles` đã cấu hình (đặt qua `openclaw models auth login`) ghi đè phân giải biến môi trường. Xem [hồ sơ xác thực trong FAQ về mô hình](</vi/help/faq-models#what-is-an-auth-profile>) để biết cơ chế xoay vòng hồ sơ, thời gian chờ và ghi đè.

Relationship to the Qwen plugin

Cả hai Plugin đi kèm đều giao tiếp với DashScope và chấp nhận các API key chồng lắp. Dùng:

  * ID `alibaba/wan*.*` để điều khiển nhà cung cấp video Wan chuyên dụng được ghi lại trên trang này.
  * ID `qwen/*` cho trò chuyện, embedding và hiểu phương tiện của Qwen (xem [Qwen](</vi/providers/qwen>)).


Đặt `MODELSTUDIO_API_KEY` một lần sẽ xác thực cả hai Plugin vì danh sách biến môi trường xác thực cố ý chồng lắp; bạn không cần thiết lập từng Plugin riêng.

## Liên quan

[**Video generation** Tham số công cụ video dùng chung và lựa chọn nhà cung cấp. ](</vi/tools/video-generation>) [**Qwen** Thiết lập trò chuyện, embedding và hiểu phương tiện của Qwen trên cùng xác thực DashScope. ](</vi/providers/qwen>) [**Configuration reference** Mặc định của tác nhân và cấu hình mô hình. ](</vi/gateway/config-agents#agent-defaults>) [**Models FAQ** Hồ sơ xác thực, chuyển đổi mô hình và xử lý lỗi "không có hồ sơ". ](</vi/help/faq-models>)

Was this useful?YesNo