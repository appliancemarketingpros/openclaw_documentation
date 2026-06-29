---
title: Nhà cung cấp llama.cpp
source_url: https://docs.openclaw.ai/vi/plugins/llama-cpp
scraped_at: 2026-06-29
---

CapabilitiesBundled plugin guides

`llama-cpp` là plugin nhà cung cấp bên ngoài chính thức cho embedding GGUF cục bộ. Nó sở hữu phụ thuộc runtime `node-llama-cpp` được dùng bởi `memorySearch.provider: "local"`.

Cài đặt trước khi dùng embedding bộ nhớ cục bộ:

bashCopy code
[code]
    openclaw plugins install @openclaw/llama-cpp-provider
[/code]

Gói npm `openclaw` chính không bao gồm `node-llama-cpp`. Việc giữ phụ thuộc native trong plugin này giúp các bản cập nhật npm OpenClaw thông thường không xóa runtime đã cài thủ công bên trong thư mục gói OpenClaw.

## Cấu hình

Đặt nhà cung cấp tìm kiếm bộ nhớ thành `local`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        local: {          modelPath: "hf:ggml-org/embeddinggemma-300m-qat-q8_0-GGUF/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

Mô hình mặc định là `embeddinggemma-300m-qat-Q8_0.gguf`. Bạn cũng có thể trỏ `local.modelPath` tới một tệp `.gguf` cục bộ.

## Runtime native

Dùng Node 24 để có đường dẫn cài đặt native mượt nhất. Các checkout mã nguồn dùng pnpm có thể cần phê duyệt và xây dựng lại phụ thuộc native:

bashCopy code
[code]
    pnpm approve-buildspnpm rebuild node-llama-cpp
[/code]

Để dùng embedding cục bộ ít ma sát hơn, hãy dùng nhà cung cấp dịch vụ cục bộ như Ollama hoặc LM Studio thay thế.

Was this useful?YesNo

Open issue