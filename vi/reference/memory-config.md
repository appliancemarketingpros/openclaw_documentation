---
title: Tham chiếu cấu hình bộ nhớ
source_url: https://docs.openclaw.ai/vi/reference/memory-config
scraped_at: 2026-05-25
---

Trang này liệt kê mọi núm cấu hình cho tìm kiếm bộ nhớ của OpenClaw. Để xem tổng quan khái niệm, hãy xem:

[**Tổng quan về bộ nhớ** Cách bộ nhớ hoạt động. ](</vi/concepts/memory>) [**Công cụ tích hợp sẵn** Backend SQLite mặc định. ](</vi/concepts/memory-builtin>) [**Công cụ QMD** Sidecar ưu tiên cục bộ. ](</vi/concepts/memory-qmd>) [**Tìm kiếm bộ nhớ** Quy trình tìm kiếm và tinh chỉnh. ](</vi/concepts/memory-search>) [**Active Memory** Sub-agent bộ nhớ cho phiên tương tác. ](</vi/concepts/active-memory>)

Tất cả cài đặt tìm kiếm bộ nhớ nằm trong `agents.defaults.memorySearch` ở `openclaw.json` trừ khi có ghi chú khác.

* * *

## Chọn nhà cung cấp

Khóa | Kiểu | Mặc định | Mô tả  
---|---|---|---  
`provider` | `string` | tự động phát hiện | ID adapter embedding như `bedrock`, `deepinfra`, `gemini`, `github-copilot`, `local`, `mistral`, `ollama`, `openai`, hoặc `voyage`; cũng có thể là `models.providers.<id>` đã cấu hình mà `api` trỏ tới một trong các adapter đó  
`model` | `string` | mặc định của nhà cung cấp | Tên mô hình embedding  
`fallback` | `string` | `"none"` | ID adapter dự phòng khi adapter chính thất bại  
`enabled` | `boolean` | `true` | Bật hoặc tắt tìm kiếm bộ nhớ  
  
### Thứ tự tự động phát hiện

Khi `provider` không được đặt, OpenClaw chọn mục khả dụng đầu tiên:

* ### local

Được chọn nếu `memorySearch.local.modelPath` đã cấu hình và tệp tồn tại.

* ### github-copilot

Được chọn nếu có thể phân giải token GitHub Copilot (biến môi trường hoặc hồ sơ xác thực).

* ### openai

Được chọn nếu có thể phân giải khóa OpenAI.

* ### gemini

Được chọn nếu có thể phân giải khóa Gemini.

* ### voyage

Được chọn nếu có thể phân giải khóa Voyage.

* ### mistral

Được chọn nếu có thể phân giải khóa Mistral.

* ### deepinfra

Được chọn nếu có thể phân giải khóa DeepInfra.

* ### bedrock

Được chọn nếu chuỗi thông tin xác thực AWS SDK phân giải được (vai trò instance, khóa truy cập, hồ sơ, SSO, web identity, hoặc cấu hình dùng chung).

`ollama` được hỗ trợ nhưng không được tự động phát hiện (hãy đặt rõ ràng).

### ID nhà cung cấp tùy chỉnh

`memorySearch.provider` có thể trỏ tới một mục `models.providers.<id>` tùy chỉnh. OpenClaw phân giải chủ sở hữu `api` của nhà cung cấp đó cho adapter embedding trong khi vẫn giữ ID nhà cung cấp tùy chỉnh để xử lý endpoint, xác thực, và tiền tố mô hình. Điều này cho phép các thiết lập nhiều GPU hoặc nhiều host dành riêng embedding bộ nhớ cho một endpoint cục bộ cụ thể:

json5Copy code
[code]
    {  models: {    providers: {      "ollama-5080": {        api: "ollama",        baseUrl: "http://gpu-box.local:11435",        apiKey: "ollama-local",        models: [{ id: "qwen3-embedding:0.6b" }],      },    },  },  agents: {    defaults: {      memorySearch: {        provider: "ollama-5080",        model: "qwen3-embedding:0.6b",      },    },  },}
[/code]

### Phân giải khóa API

Embedding từ xa yêu cầu khóa API. Thay vào đó, Bedrock dùng chuỗi thông tin xác thực mặc định của AWS SDK (vai trò instance, SSO, khóa truy cập).

Nhà cung cấp | Biến môi trường | Khóa cấu hình  
---|---|---  
Bedrock | Chuỗi thông tin xác thực AWS | Không cần khóa API  
DeepInfra | `DEEPINFRA_API_KEY` | `models.providers.deepinfra.apiKey`  
Gemini | `GEMINI_API_KEY` | `models.providers.google.apiKey`  
GitHub Copilot | `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN` | Hồ sơ xác thực qua đăng nhập thiết bị  
Mistral | `MISTRAL_API_KEY` | `models.providers.mistral.apiKey`  
Ollama | `OLLAMA_API_KEY` (phần giữ chỗ) | \--  
OpenAI | `OPENAI_API_KEY` | `models.providers.openai.apiKey`  
Voyage | `VOYAGE_API_KEY` | `models.providers.voyage.apiKey`  
  
* * *

## Cấu hình endpoint từ xa

Dành cho endpoint tùy chỉnh tương thích OpenAI hoặc ghi đè mặc định của nhà cung cấp:

URL cơ sở API tùy chỉnh.

Ghi đè khóa API.

Header HTTP bổ sung (được hợp nhất với mặc định của nhà cung cấp).

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        model: "text-embedding-3-small",        remote: {          baseUrl: "https://api.example.com/v1/",          apiKey: "YOUR_KEY",        },      },    },  },}
[/code]

* * *

## Cấu hình theo nhà cung cấp

Gemini Khóa | Kiểu | Mặc định | Mô tả  
---|---|---|---  
`model` | `string` | `gemini-embedding-001` | Cũng hỗ trợ `gemini-embedding-2-preview`  
`outputDimensionality` | `number` | `3072` | Với Embedding 2: 768, 1536, hoặc 3072  
Kiểu đầu vào tương thích OpenAI

Endpoint embedding tương thích OpenAI có thể chọn dùng các trường yêu cầu `input_type` theo nhà cung cấp. Điều này hữu ích cho các mô hình embedding bất đối xứng yêu cầu nhãn khác nhau cho embedding truy vấn và tài liệu.

Khóa | Kiểu | Mặc định | Mô tả  
---|---|---|---  
`inputType` | `string` | chưa đặt | `input_type` dùng chung cho embedding truy vấn và tài liệu  
`queryInputType` | `string` | chưa đặt | `input_type` tại thời điểm truy vấn; ghi đè `inputType`  
`documentInputType` | `string` | chưa đặt | `input_type` chỉ mục/tài liệu; ghi đè `inputType`  
json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",        remote: {          baseUrl: "https://embeddings.example/v1",          apiKey: "env:EMBEDDINGS_API_KEY",        },        model: "asymmetric-embedder",        queryInputType: "query",        documentInputType: "passage",      },    },  },}
[/code]

Việc thay đổi các giá trị này ảnh hưởng tới danh tính cache embedding cho lập chỉ mục theo lô của nhà cung cấp và nên được theo sau bằng việc lập chỉ mục lại bộ nhớ khi mô hình upstream xử lý các nhãn khác nhau.

Bedrock

### Cấu hình embedding Bedrock

Bedrock dùng chuỗi thông tin xác thực mặc định của AWS SDK — không cần khóa API. Nếu OpenClaw chạy trên EC2 với vai trò instance đã bật Bedrock, chỉ cần đặt nhà cung cấp và mô hình:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0",      },    },  },}
[/code]

Khóa | Kiểu | Mặc định | Mô tả  
---|---|---|---  
`model` | `string` | `amazon.titan-embed-text-v2:0` | Bất kỳ ID mô hình embedding Bedrock nào  
`outputDimensionality` | `number` | mặc định của mô hình | Với Titan V2: 256, 512, hoặc 1024  
  
**Mô hình được hỗ trợ** (có phát hiện họ và mặc định kích thước):

ID mô hình | Nhà cung cấp | Số chiều mặc định | Số chiều có thể cấu hình  
---|---|---|---  
`amazon.titan-embed-text-v2:0` | Amazon | 1024 | 256, 512, 1024  
`amazon.titan-embed-text-v1` | Amazon | 1536 | \--  
`amazon.titan-embed-g1-text-02` | Amazon | 1536 | \--  
`amazon.titan-embed-image-v1` | Amazon | 1024 | \--  
`amazon.nova-2-multimodal-embeddings-v1:0` | Amazon | 1024 | 256, 384, 1024, 3072  
`cohere.embed-english-v3` | Cohere | 1024 | \--  
`cohere.embed-multilingual-v3` | Cohere | 1024 | \--  
`cohere.embed-v4:0` | Cohere | 1536 | 256-1536  
`twelvelabs.marengo-embed-3-0-v1:0` | TwelveLabs | 512 | \--  
`twelvelabs.marengo-embed-2-7-v1:0` | TwelveLabs | 1024 | \--  
  
Các biến thể có hậu tố thông lượng (ví dụ: `amazon.titan-embed-text-v1:2:8k`) kế thừa cấu hình của mô hình cơ sở.

**Xác thực:** xác thực Bedrock dùng thứ tự phân giải thông tin xác thực AWS SDK tiêu chuẩn:

  1. Biến môi trường (`AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`)
  2. Cache token SSO
  3. Thông tin xác thực token web identity
  4. Tệp thông tin xác thực và cấu hình dùng chung
  5. Thông tin xác thực metadata ECS hoặc EC2


Vùng được phân giải từ `AWS_REGION`, `AWS_DEFAULT_REGION`, `baseUrl` của nhà cung cấp `amazon-bedrock`, hoặc mặc định là `us-east-1`.

**Quyền IAM:** vai trò hoặc người dùng IAM cần:

jsonCopy code
[code]
    {  "Effect": "Allow",  "Action": "bedrock:InvokeModel",  "Resource": "*"}
[/code]

Để dùng đặc quyền tối thiểu, giới hạn phạm vi `InvokeModel` cho mô hình cụ thể:

CodeCopy code
[code]
    arn:aws:bedrock:*::foundation-model/amazon.titan-embed-text-v2:0
[/code]

Cục bộ (GGUF + node-llama-cpp) Khóa | Loại | Mặc định | Mô tả  
---|---|---|---  
`local.modelPath` | `string` | tự động tải xuống | Đường dẫn đến tệp mô hình GGUF  
`local.modelCacheDir` | `string` | mặc định node-llama-cpp | Thư mục bộ nhớ đệm cho các mô hình đã tải xuống  
`local.contextSize` | `number | "auto"` | `4096` | Kích thước cửa sổ ngữ cảnh cho ngữ cảnh embedding. 4096 bao phủ các đoạn điển hình (128–512 token) đồng thời giới hạn VRAM không phải trọng số. Giảm xuống 1024–2048 trên các máy chủ bị hạn chế tài nguyên. `"auto"` dùng mức tối đa đã huấn luyện của mô hình — không khuyến nghị cho mô hình 8B+ (Qwen3-Embedding-8B: 40 960 token → ~32 GB VRAM so với ~8.8 GB ở 4096).  
  
Mô hình mặc định: `embeddinggemma-300m-qat-Q8_0.gguf` (~0.6 GB, tự động tải xuống). Các bản checkout từ mã nguồn vẫn yêu cầu phê duyệt bản dựng native: `pnpm approve-builds`, sau đó `pnpm rebuild node-llama-cpp`.

Dùng CLI độc lập để xác minh cùng đường dẫn provider mà Gateway sử dụng:

bashCopy code
[code]
    openclaw memory status --deep --agent mainopenclaw memory index --force --agent main
[/code]

Nếu `provider` là `auto`, `local` chỉ được chọn khi `local.modelPath` trỏ đến một tệp cục bộ hiện có. Các tham chiếu mô hình `hf:` và HTTP(S) vẫn có thể được dùng rõ ràng với `provider: "local"`, nhưng chúng không khiến `auto` chọn local trước khi mô hình có sẵn trên đĩa.

### Thời gian chờ embedding nội tuyến

Ghi đè thời gian chờ cho các lô embedding nội tuyến trong quá trình lập chỉ mục bộ nhớ.

Khi chưa đặt, giá trị mặc định của provider được dùng: 600 giây cho các provider cục bộ/tự lưu trữ như `local`, `ollama`, và `lmstudio`, và 120 giây cho các provider được lưu trữ. Tăng giá trị này khi các lô embedding chạy bằng CPU cục bộ hoạt động bình thường nhưng chậm.

* * *

## Cấu hình tìm kiếm lai

Tất cả nằm dưới `memorySearch.query.hybrid`:

Khóa | Loại | Mặc định | Mô tả  
---|---|---|---  
`enabled` | `boolean` | `true` | Bật tìm kiếm lai BM25 + vector  
`vectorWeight` | `number` | `0.7` | Trọng số cho điểm vector (0-1)  
`textWeight` | `number` | `0.3` | Trọng số cho điểm BM25 (0-1)  
`candidateMultiplier` | `number` | `4` | Hệ số nhân kích thước nhóm ứng viên  
  
### MMR (đa dạng)

Khóa | Loại | Mặc định | Mô tả  
---|---|---|---  
`mmr.enabled` | `boolean` | `false` | Bật xếp hạng lại bằng MMR  
`mmr.lambda` | `number` | `0.7` | 0 = đa dạng tối đa, 1 = liên quan tối đa  
  
### Suy giảm theo thời gian (gần đây)

Khóa | Loại | Mặc định | Mô tả  
---|---|---|---  
`temporalDecay.enabled` | `boolean` | `false` | Bật tăng điểm theo độ gần đây  
`temporalDecay.halfLifeDays` | `number` | `30` | Điểm giảm một nửa sau mỗi N ngày  
  
Các tệp evergreen (`MEMORY.md`, các tệp không có ngày trong `memory/`) không bao giờ bị suy giảm điểm.

### Ví dụ đầy đủ

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        query: {          hybrid: {            vectorWeight: 0.7,            textWeight: 0.3,            mmr: { enabled: true, lambda: 0.7 },            temporalDecay: { enabled: true, halfLifeDays: 30 },          },        },      },    },  },}
[/code]

* * *

## Đường dẫn bộ nhớ bổ sung

Khóa | Loại | Mô tả  
---|---|---  
`extraPaths` | `string[]` | Các thư mục hoặc tệp bổ sung để lập chỉ mục  
json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        extraPaths: ["../team-docs", "/srv/shared-notes"],      },    },  },}
[/code]

Đường dẫn có thể là tuyệt đối hoặc tương đối với workspace. Các thư mục được quét đệ quy để tìm tệp `.md`. Cách xử lý symlink phụ thuộc vào backend đang hoạt động: engine tích hợp bỏ qua symlink, còn QMD tuân theo hành vi của trình quét QMD bên dưới.

Đối với tìm kiếm bản ghi xuyên tác tử trong phạm vi tác tử, hãy dùng `agents.list[].memorySearch.qmd.extraCollections` thay vì `memory.qmd.paths`. Các bộ sưu tập bổ sung đó có cùng dạng `{ path, name, pattern? }`, nhưng được hợp nhất theo từng tác tử và có thể giữ lại tên chia sẻ rõ ràng khi đường dẫn trỏ ra ngoài workspace hiện tại. Nếu cùng một đường dẫn đã phân giải xuất hiện trong cả `memory.qmd.paths` và `memorySearch.qmd.extraCollections`, QMD giữ mục đầu tiên và bỏ qua mục trùng lặp.

* * *

## Bộ nhớ đa phương thức (Gemini)

Lập chỉ mục hình ảnh và âm thanh cùng với Markdown bằng Gemini Embedding 2:

Khóa | Loại | Mặc định | Mô tả  
---|---|---|---  
`multimodal.enabled` | `boolean` | `false` | Bật lập chỉ mục đa phương thức  
`multimodal.modalities` | `string[]` | \-- | `["image"]`, `["audio"]`, hoặc `["all"]`  
`multimodal.maxFileBytes` | `number` | `10000000` | Kích thước tệp tối đa để lập chỉ mục  
  
Định dạng được hỗ trợ: `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`, `.heic`, `.heif` (hình ảnh); `.mp3`, `.wav`, `.ogg`, `.opus`, `.m4a`, `.aac`, `.flac` (âm thanh).

* * *

## Bộ nhớ đệm embedding

Khóa | Kiểu | Mặc định | Mô tả  
---|---|---|---  
`cache.enabled` | `boolean` | `false` | Lưu embedding của chunk vào SQLite  
`cache.maxEntries` | `number` | `50000` | Số embedding được lưu tối đa  
  
Ngăn việc tạo lại embedding cho văn bản không đổi trong quá trình lập chỉ mục lại hoặc cập nhật bản ghi phiên.

* * *

## Lập chỉ mục theo lô

Khóa | Kiểu | Mặc định | Mô tả  
---|---|---|---  
`remote.nonBatchConcurrency` | `number` | `4` | Embedding nội tuyến song song  
`remote.batch.enabled` | `boolean` | `false` | Bật API embedding theo lô  
`remote.batch.concurrency` | `number` | `2` | Tác vụ theo lô song song  
`remote.batch.wait` | `boolean` | `true` | Chờ hoàn tất lô  
`remote.batch.pollIntervalMs` | `number` | \-- | Khoảng thời gian thăm dò  
`remote.batch.timeoutMinutes` | `number` | \-- | Thời gian chờ tối đa của lô  
  
Có sẵn cho `openai`, `gemini` và `voyage`. Lô OpenAI thường nhanh nhất và rẻ nhất cho các lần điền ngược dữ liệu lớn.

`remote.nonBatchConcurrency` kiểm soát các lệnh gọi embedding nội tuyến được dùng bởi nhà cung cấp cục bộ/tự lưu trữ và nhà cung cấp được lưu trữ khi API theo lô của nhà cung cấp không hoạt động. Ollama mặc định là `1` cho lập chỉ mục không theo lô để tránh làm quá tải các máy chủ cục bộ nhỏ hơn; đặt giá trị cao hơn trên máy mạnh hơn.

Thiết lập này tách biệt với `sync.embeddingBatchTimeoutSeconds`, vốn kiểm soát thời gian chờ cho các lệnh gọi embedding nội tuyến.

* * *

## Tìm kiếm bộ nhớ phiên (thử nghiệm)

Lập chỉ mục bản ghi phiên và hiển thị chúng qua `memory_search`:

Khóa | Kiểu | Mặc định | Mô tả  
---|---|---|---  
`experimental.sessionMemory` | `boolean` | `false` | Bật lập chỉ mục phiên  
`sources` | `string[]` | `["memory"]` | Thêm `"sessions"` để bao gồm bản ghi phiên  
`sync.sessions.deltaBytes` | `number` | `100000` | Ngưỡng byte để lập chỉ mục lại  
`sync.sessions.deltaMessages` | `number` | `50` | Ngưỡng tin nhắn để lập chỉ mục lại  
  
* * *

## Tăng tốc vector SQLite (sqlite-vec)

Khóa | Kiểu | Mặc định | Mô tả  
---|---|---|---  
`store.vector.enabled` | `boolean` | `true` | Dùng sqlite-vec cho truy vấn vector  
`store.vector.extensionPath` | `string` | đi kèm | Ghi đè đường dẫn sqlite-vec  
  
Khi sqlite-vec không khả dụng, OpenClaw tự động chuyển về độ tương đồng cosine trong tiến trình.

* * *

## Lưu trữ chỉ mục

Khóa | Kiểu | Mặc định | Mô tả  
---|---|---|---  
`store.path` | `string` | `~/.openclaw/memory/{agentId}.sqlite` | Vị trí chỉ mục (hỗ trợ token `{agentId}`)  
`store.fts.tokenizer` | `string` | `unicode61` | Bộ tách token FTS5 (`unicode61` hoặc `trigram`)  
  
* * *

## Cấu hình backend QMD

Đặt `memory.backend = "qmd"` để bật. Tất cả thiết lập QMD nằm dưới `memory.qmd`:

Khóa | Kiểu | Mặc định | Mô tả  
---|---|---|---  
`command` | `string` | `qmd` | Đường dẫn tệp thực thi QMD; đặt đường dẫn tuyệt đối khi `PATH` của dịch vụ khác shell của bạn  
`searchMode` | `string` | `search` | Lệnh tìm kiếm: `search`, `vsearch`, `query`  
`includeDefaultMemory` | `boolean` | `true` | Tự động lập chỉ mục `MEMORY.md` \+ `memory/**/*.md`  
`paths[]` | `array` | \-- | Đường dẫn bổ sung: `{ name, path, pattern? }`  
`sessions.enabled` | `boolean` | `false` | Lập chỉ mục bản ghi phiên  
`sessions.retentionDays` | `number` | \-- | Thời gian lưu giữ bản ghi  
`sessions.exportDir` | `string` | \-- | Thư mục xuất  
  
`searchMode: "search"` chỉ dùng lexical/BM25. OpenClaw không chạy các probe sẵn sàng vector ngữ nghĩa hoặc bảo trì embedding QMD cho chế độ đó, kể cả trong `memory status --deep`; `vsearch` và `query` vẫn tiếp tục yêu cầu QMD vector readiness và embeddings.

OpenClaw ưu tiên collection QMD hiện tại và các dạng truy vấn MCP, nhưng vẫn giữ cho các bản phát hành QMD cũ hoạt động bằng cách thử các cờ mẫu collection tương thích và tên công cụ MCP cũ hơn khi cần. Khi QMD cho biết có hỗ trợ nhiều bộ lọc collection, các collection cùng nguồn được tìm kiếm bằng một tiến trình QMD; các bản dựng QMD cũ hơn giữ đường dẫn tương thích theo từng collection. Cùng nguồn nghĩa là các collection bộ nhớ bền vững được nhóm lại với nhau, trong khi các collection bản ghi phiên vẫn là một nhóm riêng để đa dạng hóa nguồn vẫn có cả hai đầu vào.

Lịch cập nhật Khóa | Loại | Mặc định | Mô tả  
---|---|---|---  
`update.interval` | `string` | `5m` | Khoảng thời gian làm mới  
`update.debounceMs` | `number` | `15000` | Debounce thay đổi tệp  
`update.onBoot` | `boolean` | `true` | Làm mới khi trình quản lý QMD chạy lâu dài mở; cũng kiểm soát làm mới khi khởi động theo cơ chế opt-in  
`update.startup` | `string` | `off` | Làm mới tùy chọn khi gateway khởi động: `off`, `idle` hoặc `immediate`  
`update.startupDelayMs` | `number` | `120000` | Độ trễ trước khi làm mới `startup: "idle"` chạy  
`update.waitForBootSync` | `boolean` | `false` | Chặn việc mở trình quản lý cho đến khi lần làm mới ban đầu hoàn tất  
`update.embedInterval` | `string` | \-- | Nhịp embed riêng  
`update.commandTimeoutMs` | `number` | \-- | Thời gian chờ cho các lệnh QMD  
`update.updateTimeoutMs` | `number` | \-- | Thời gian chờ cho các thao tác cập nhật QMD  
`update.embedTimeoutMs` | `number` | \-- | Thời gian chờ cho các thao tác embed QMD  
Giới hạn Khóa | Loại | Mặc định | Mô tả  
---|---|---|---  
`limits.maxResults` | `number` | `6` | Số kết quả tìm kiếm tối đa  
`limits.maxSnippetChars` | `number` | \-- | Giới hạn độ dài snippet  
`limits.maxInjectedChars` | `number` | \-- | Giới hạn tổng số ký tự được chèn  
`limits.timeoutMs` | `number` | `4000` | Thời gian chờ tìm kiếm  
Phạm vi

Kiểm soát những phiên nào có thể nhận kết quả tìm kiếm QMD. Cùng schema với [`session.sendPolicy`](</vi/gateway/config-agents#session>):

json5Copy code
[code]
    {  memory: {    qmd: {      scope: {        default: "deny",        rules: [{ action: "allow", match: { chatType: "direct" } }],      },    },  },}
[/code]

Mặc định được phát hành cho phép phiên trực tiếp và phiên kênh, trong khi vẫn từ chối nhóm.

Mặc định chỉ DM. `match.keyPrefix` khớp với khóa phiên đã chuẩn hóa; `match.rawKeyPrefix` khớp với khóa thô bao gồm `agent:<id>:`.

Trích dẫn

`memory.citations` áp dụng cho mọi backend:

Giá trị | Hành vi  
---|---  
`auto` (mặc định) | Bao gồm footer `Source: <path#line>` trong snippet  
`on` | Luôn bao gồm footer  
`off` | Bỏ qua footer (đường dẫn vẫn được truyền nội bộ cho agent)  
  
Các lần làm mới khi khởi động QMD dùng đường dẫn tiến trình con one-shot trong lúc gateway khởi động. Trình quản lý QMD chạy lâu dài vẫn sở hữu file watcher thông thường và các bộ hẹn giờ interval khi tìm kiếm bộ nhớ được mở để sử dụng tương tác.

### Ví dụ QMD đầy đủ

json5Copy code
[code]
    {  memory: {    backend: "qmd",    citations: "auto",    qmd: {      includeDefaultMemory: true,      update: { interval: "5m", debounceMs: 15000 },      limits: { maxResults: 6, timeoutMs: 4000 },      scope: {        default: "deny",        rules: [{ action: "allow", match: { chatType: "direct" } }],      },      paths: [{ name: "docs", path: "~/notes", pattern: "**/*.md" }],    },  },}
[/code]

* * *

## Dreaming

Dreaming được cấu hình dưới `plugins.entries.memory-core.config.dreaming`, không phải dưới `agents.defaults.memorySearch`.

Dreaming chạy như một lượt quét được lập lịch và sử dụng các pha light/deep/REM nội bộ như một chi tiết triển khai.

Để biết hành vi khái niệm và các lệnh slash, hãy xem [Dreaming](</vi/concepts/dreaming>).

### Cài đặt người dùng

Khóa | Loại | Mặc định | Mô tả  
---|---|---|---  
`enabled` | `boolean` | `false` | Bật hoặc tắt hoàn toàn Dreaming  
`frequency` | `string` | `0 3 * * *` | Nhịp cron tùy chọn cho toàn bộ lượt quét Dreaming  
`model` | `string` | mô hình mặc định | Ghi đè mô hình subagent Dream Diary tùy chọn  
  
### Ví dụ

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-core": {        subagent: {          allowModelOverride: true,          allowedModels: ["anthropic/claude-sonnet-4-6"],        },        config: {          dreaming: {            enabled: true,            frequency: "0 3 * * *",            model: "anthropic/claude-sonnet-4-6",          },        },      },    },  },}
[/code]

## Liên quan

  * [Tham chiếu cấu hình](</vi/gateway/configuration-reference>)
  * [Tổng quan về bộ nhớ](</vi/concepts/memory>)
  * [Tìm kiếm bộ nhớ](</vi/concepts/memory-search>)


Was this useful?YesNo