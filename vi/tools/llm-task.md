---
title: Tác vụ LLM
source_url: https://docs.openclaw.ai/vi/tools/llm-task
scraped_at: 2026-05-25
---

`llm-task` là một **công cụ Plugin tùy chọn** chạy một tác vụ LLM chỉ JSON và trả về đầu ra có cấu trúc (tùy chọn xác thực theo Lược đồ JSON).

Điều này lý tưởng cho các công cụ workflow như Lobster: bạn có thể thêm một bước LLM duy nhất mà không cần viết mã OpenClaw tùy chỉnh cho từng workflow.

## Bật Plugin

  1. Bật Plugin:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  }}
[/code]

  2. Cho phép công cụ tùy chọn:

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["llm-task"]  }}
[/code]

Chỉ dùng `tools.allow` khi bạn muốn chế độ danh sách cho phép hạn chế.

## Cấu hình (tùy chọn)

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": {        "enabled": true,        "config": {          "defaultProvider": "openai-codex",          "defaultModel": "gpt-5.5",          "defaultAuthProfileId": "main",          "allowedModels": ["openai/gpt-5.4"],          "maxTokens": 800,          "timeoutMs": 30000        }      }    }  }}
[/code]

`allowedModels` là danh sách cho phép gồm các chuỗi `provider/model`. Nếu được đặt, mọi yêu cầu nằm ngoài danh sách sẽ bị từ chối.

## Tham số công cụ

  * `prompt` (chuỗi, bắt buộc)
  * `input` (bất kỳ, tùy chọn)
  * `schema` (đối tượng, Lược đồ JSON tùy chọn)
  * `provider` (chuỗi, tùy chọn)
  * `model` (chuỗi, tùy chọn)
  * `thinking` (chuỗi, tùy chọn)
  * `authProfileId` (chuỗi, tùy chọn)
  * `temperature` (số, tùy chọn)
  * `maxTokens` (số, tùy chọn)
  * `timeoutMs` (số, tùy chọn)


`thinking` chấp nhận các preset suy luận tiêu chuẩn của OpenClaw, chẳng hạn như `low` hoặc `medium`.

## Đầu ra

Trả về `details.json` chứa JSON đã phân tích cú pháp (và xác thực theo `schema` khi được cung cấp).

## Ví dụ: bước workflow Lobster

### Giới hạn quan trọng

Ví dụ bên dưới giả định **CLI Lobster độc lập** đang chạy trong một môi trường mà `openclaw.invoke` đã có đúng URL Gateway/ngữ cảnh xác thực.

Đối với trình chạy Lobster **nhúng** được đóng gói bên trong OpenClaw, mẫu CLI lồng nhau này **hiện chưa đáng tin cậy** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

Cho đến khi Lobster nhúng có cầu nối được hỗ trợ cho luồng này, hãy ưu tiên một trong hai cách:

  * gọi trực tiếp công cụ `llm-task` bên ngoài Lobster, hoặc
  * các bước Lobster không phụ thuộc vào lệnh gọi `openclaw.invoke` lồng nhau.


Ví dụ CLI Lobster độc lập:

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": {    "subject": "Hello",    "body": "Can you help?"  },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

## Ghi chú an toàn

  * Công cụ này **chỉ JSON** và chỉ dẫn mô hình chỉ xuất JSON (không có khối mã, không có bình luận).
  * Không có công cụ nào được hiển thị cho mô hình trong lần chạy này.
  * Hãy coi đầu ra là không đáng tin cậy trừ khi bạn xác thực bằng `schema`.
  * Đặt phê duyệt trước mọi bước có tác dụng phụ (gửi, đăng, thực thi).


## Liên quan

  * [Mức độ suy luận](</vi/tools/thinking>)
  * [Tác nhân phụ](</vi/tools/subagents>)
  * [Lệnh slash](</vi/tools/slash-commands>)


Was this useful?YesNo