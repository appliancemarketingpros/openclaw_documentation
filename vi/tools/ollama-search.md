---
title: Tìm kiếm trên web của Ollama
source_url: https://docs.openclaw.ai/vi/tools/ollama-search
scraped_at: 2026-05-25
---

OpenClaw hỗ trợ **Tìm kiếm Web Ollama** dưới dạng nhà cung cấp `web_search` được tích hợp sẵn. Nó sử dụng API tìm kiếm web của Ollama và trả về kết quả có cấu trúc với tiêu đề, URL và đoạn trích.

Đối với Ollama cục bộ hoặc tự lưu trữ, thiết lập này mặc định không cần khóa API. Nó yêu cầu:

  * một máy chủ Ollama mà OpenClaw có thể truy cập
  * `ollama signin`


Đối với tìm kiếm được lưu trữ trực tiếp, đặt URL cơ sở của nhà cung cấp Ollama thành `https://ollama.com` và cung cấp `OLLAMA_API_KEY` thật.

## Thiết lập

* ### Khởi động Ollama

Đảm bảo Ollama đã được cài đặt và đang chạy.

* ### Đăng nhập

Chạy:

bashCopy code
[code]
    ollama signin
[/code]

* ### Chọn Tìm kiếm Web Ollama

Chạy:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Sau đó chọn **Tìm kiếm Web Ollama** làm nhà cung cấp.

Nếu bạn đã sử dụng Ollama cho các mô hình, Tìm kiếm Web Ollama sẽ dùng lại cùng máy chủ đã cấu hình.

## Cấu hình

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

Ghi đè máy chủ Ollama tùy chọn:

json5Copy code
[code]
    {  plugins: {    entries: {      ollama: {        config: {          webSearch: {            baseUrl: "http://ollama-host:11434",          },        },      },    },  },}
[/code]

Nếu bạn đã cấu hình Ollama làm nhà cung cấp mô hình, nhà cung cấp tìm kiếm web có thể dùng lại máy chủ đó:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",      },    },  },}
[/code]

Nhà cung cấp mô hình Ollama dùng `baseUrl` làm khóa chính tắc. Nhà cung cấp tìm kiếm web cũng hỗ trợ `baseURL` trên `models.providers.ollama` để tương thích với các ví dụ cấu hình theo kiểu OpenAI SDK.

Nếu không đặt URL cơ sở Ollama rõ ràng, OpenClaw sử dụng `http://127.0.0.1:11434`.

Nếu máy chủ Ollama của bạn yêu cầu xác thực bearer, OpenClaw dùng lại `models.providers.ollama.apiKey` (hoặc xác thực nhà cung cấp tương ứng dựa trên env) cho các yêu cầu tới máy chủ đã cấu hình đó.

Tìm kiếm Web Ollama được lưu trữ trực tiếp:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",      },    },  },  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

## Ghi chú

  * Không cần trường khóa API riêng cho tìm kiếm web đối với nhà cung cấp này.
  * Nếu máy chủ Ollama được bảo vệ bằng xác thực, OpenClaw dùng lại khóa API của nhà cung cấp Ollama thông thường khi có.
  * Nếu `baseUrl` là `https://ollama.com`, OpenClaw gọi trực tiếp `https://ollama.com/api/web_search` và gửi khóa API Ollama đã cấu hình dưới dạng xác thực bearer.
  * Nếu máy chủ đã cấu hình không cung cấp tìm kiếm web và `OLLAMA_API_KEY` được đặt, OpenClaw có thể chuyển dự phòng sang `https://ollama.com/api/web_search` mà không gửi khóa env đó tới máy chủ cục bộ.
  * OpenClaw cảnh báo trong quá trình thiết lập nếu Ollama không thể truy cập hoặc chưa đăng nhập, nhưng không chặn việc lựa chọn.
  * Tự động phát hiện khi chạy có thể chuyển dự phòng sang Tìm kiếm Web Ollama khi không có nhà cung cấp có thông tin xác thực nào có mức ưu tiên cao hơn được cấu hình.
  * Các máy chủ daemon Ollama cục bộ sử dụng điểm cuối proxy cục bộ `/api/experimental/web_search`, điểm cuối này ký và chuyển tiếp tới Ollama Cloud.
  * Máy chủ `https://ollama.com` sử dụng trực tiếp điểm cuối được lưu trữ công khai `/api/web_search` với xác thực khóa API bearer.


## Liên quan

  * [Tổng quan về Tìm kiếm Web](</vi/tools/web>) \-- tất cả nhà cung cấp và tự động phát hiện
  * [Ollama](</vi/providers/ollama>) \-- thiết lập mô hình Ollama và các chế độ cloud/cục bộ


Was this useful?YesNo