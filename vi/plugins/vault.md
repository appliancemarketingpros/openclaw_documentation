---
title: SecretRef của kho bí mật
source_url: https://docs.openclaw.ai/vi/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# SecretRef của Vault

Plugin Vault đi kèm cho phép OpenClaw phân giải SecretRef `exec` từ HashiCorp Vault khi Gateway khởi động và khi tải lại. OpenClaw lưu các tham chiếu Vault trong cấu hình, giữ các giá trị đã phân giải trong ảnh chụp nhanh bí mật trong bộ nhớ và không ghi các khóa API đã phân giải trở lại `openclaw.json`.

Sử dụng tính năng này khi bạn đã vận hành Vault hoặc muốn lưu khóa của nhà cung cấp mô hình bên ngoài các tệp cấu hình OpenClaw. Để tìm hiểu mô hình thời gian chạy SecretRef, hãy xem [Quản lý bí mật](</vi/gateway/secrets>).

## Trước khi bắt đầu

Bạn cần:

  * OpenClaw có sẵn plugin `vault` đi kèm
  * một máy chủ Vault có thể truy cập
  * phương thức xác thực Vault có thể tạo mã thông báo máy khách với quyền đọc các đường dẫn bí mật mà OpenClaw cần phân giải
  * môi trường khởi động Gateway phải chứa `VAULT_ADDR` và một trong các lựa chọn: `VAULT_TOKEN`, `OPENCLAW_VAULT_AUTH_METHOD=token_file` cùng với `VAULT_TOKEN_FILE`, hoặc thông tin đăng nhập JWT/Kubernetes đã cấu hình


Trình phân giải giao tiếp với Vault qua HTTP từ Node. Gateway không cần Vault CLI để phân giải SecretRef.

Bật plugin đi kèm trước khi chạy các lệnh `openclaw vault`:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## Lưu khóa nhà cung cấp trong Vault

Theo mặc định, OpenClaw sử dụng KV v2 được gắn tại `secret`, tương ứng với các ví dụ máy chủ phát triển Vault. Đối với Vault dùng trong môi trường sản xuất, hãy đặt `OPENCLAW_VAULT_KV_MOUNT` thành đường dẫn gắn KV thực tế trước khi tạo ID SecretRef. Với các giá trị mặc định của OpenClaw, ID SecretRef này:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

đọc trường Vault sau:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

Một cách để tạo trường này bằng Vault CLI là:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

Hãy sử dụng mã thông báo máy khách có phạm vi giới hạn cho OpenClaw, không dùng mã thông báo gốc. Với bố cục KV v2 mặc định, một chính sách tối thiểu cho các khóa nhà cung cấp mô hình có dạng:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## Cho phép Gateway truy cập Vault

Đối với Gateway cục bộ không chạy trong vùng chứa, hãy xuất các thiết lập Vault trong cùng trình bao dùng để khởi động OpenClaw. Phương thức xác thực mặc định đọc mã thông báo máy khách Vault từ `VAULT_TOKEN`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

Nếu Vault Agent ghi tệp đích chứa mã thông báo, hãy sử dụng phương thức xác thực bằng tệp mã thông báo:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

Đối với máy chủ Vault được ký bằng CA riêng, hãy cài đặt CA đó vào kho tin cậy của máy chủ và bật kho tin cậy hệ thống của Node:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

Hoặc cung cấp trực tiếp một gói PEM:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

Các biến này phải tồn tại khi OpenClaw khởi động. Plugin Vault chuyển tiếp chúng đến tiến trình phân giải của mình.

Đối với xác thực JWT không tương tác, hãy sử dụng tệp JWT của tải công việc và một vai trò Vault thuộc loại `jwt`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

Tệp JWT phải là mã thông báo tải công việc được chiếu vào, chẳng hạn như mã thông báo tài khoản dịch vụ Kubernetes có đối tượng nhận được vai trò Vault chấp nhận. Đăng nhập OIDC tương tác qua trình duyệt hữu ích cho người dùng, nhưng thời gian chạy Gateway cần đăng nhập JWT không tương tác hoặc tệp mã thông báo.

Đối với phương thức xác thực Kubernetes của Vault, hãy sử dụng `kubernetes`. Phương thức này dành cho các Gateway chạy dưới dạng Pod; điểm gắn mặc định là `kubernetes`, còn tệp JWT mặc định là đường dẫn mã thông báo tài khoản dịch vụ tiêu chuẩn:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

Chỉ đặt `OPENCLAW_VAULT_AUTH_MOUNT` khi Vault gắn phương thức xác thực Kubernetes ở vị trí khác `auth/kubernetes`. Chỉ đặt `OPENCLAW_VAULT_JWT_FILE` khi mã thông báo tài khoản dịch vụ được chiếu vào một đường dẫn tùy chỉnh.

Các thiết lập tùy chọn:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

Kiểm tra những gì trình bao hiện tại có thể truy cập:

bashCopy code
[code]
    openclaw vault status
[/code]

Khi cấu hình nhiều hơn một nhà cung cấp bí mật dựa trên Vault, hãy chọn một nhà cung cấp theo bí danh:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

`openclaw vault status` không bao giờ in `VAULT_TOKEN`; lệnh này chỉ báo cáo liệu mã thông báo, tệp mã thông báo và tệp JWT đã được đặt hay chưa.

## Tạo và áp dụng kế hoạch SecretRef

Tạo một kế hoạch ánh xạ khóa API của nhà cung cấp mô hình OpenRouter sang Vault:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

Áp dụng và xác minh kế hoạch:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

Sử dụng `--allow-exec` vì plugin Vault phân giải thông qua một nhà cung cấp SecretRef `exec` do OpenClaw quản lý.

Nếu Gateway chưa chạy, hãy khởi động Gateway theo cách thông thường sau khi áp dụng kế hoạch thay vì chạy `openclaw secrets reload`.

## Cấu hình thêm khóa nhà cung cấp

Các lối tắt tích hợp sẵn:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

Nhiều khóa nhà cung cấp trong một kế hoạch:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

Các nhà cung cấp đi kèm không có lối tắt, hoặc các nhà cung cấp mô hình tùy chỉnh và tương thích với OpenAI đã được cấu hình, sử dụng `--provider-key`:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

Mỗi `--provider-key <provider=id>` ghi một SecretRef vào `models.providers.<provider>.apiKey`. Đối với nhà cung cấp tùy chỉnh, lệnh này không tạo các thiết lập `baseUrl`, `api` hoặc `models` của nhà cung cấp; hãy cấu hình các thiết lập đó trước.

Sử dụng `--target <path=id>` cho bất kỳ đường dẫn đích SecretRef đã biết nào:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

Các đường dẫn đích thuần túy áp dụng cho `openclaw.json`. Sử dụng `auth-profiles:<agentId>:<path>` cho các đích `auth-profiles.json` hiện có. Đường dẫn đích phải là một đích SecretRef đã đăng ký của OpenClaw. Lệnh thiết lập không tạo các bí mật có tên tùy ý trong OpenClaw; Vault vẫn là kho bí mật và OpenClaw chỉ lưu SecretRef trên các trường cấu hình được hỗ trợ.

## Định dạng ID SecretRef

ID SecretRef của Vault sử dụng quy ước sau:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

Ví dụ:

ID SecretRef | Thao tác đọc Vault KV v2 mặc định | Trường trả về  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
Trường Vault được trả về phải là một chuỗi.

Đối với KV v1, hãy đặt:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

Khi đó, `providers/openrouter/apiKey` đọc:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## Dữ liệu OpenClaw lưu trữ

Việc áp dụng kế hoạch thiết lập Vault sẽ lưu một nhà cung cấp do plugin quản lý:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

Các trường thông tin xác thực trỏ đến nhà cung cấp đó:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

Giá trị đã phân giải chỉ tồn tại trong ảnh chụp nhanh bí mật của thời gian chạy đang hoạt động.

## Vùng chứa và triển khai được quản lý

Các Gateway chạy trong vùng chứa vẫn sử dụng cùng plugin và cấu hình SecretRef. Vùng chứa phải nhận:

  * `VAULT_ADDR`
  * một nguồn xác thực: 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` cùng với `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` cùng với `OPENCLAW_VAULT_AUTH_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` và `OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` cùng với `OPENCLAW_VAULT_AUTH_ROLE`; có thể tùy chọn ghi đè `OPENCLAW_VAULT_AUTH_MOUNT` hoặc `OPENCLAW_VAULT_JWT_FILE`
  * `VAULT_NAMESPACE`, `OPENCLAW_VAULT_KV_MOUNT` và `OPENCLAW_VAULT_KV_VERSION` là tùy chọn


Khi sử dụng Kubernetes, ưu tiên `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` nếu Vault đã cấu hình phương thức xác thực Kubernetes cho cụm. Chỉ sử dụng `OPENCLAW_VAULT_AUTH_METHOD=jwt` khi Vault được cấu hình để coi cụm là một nhà phát hành JWT/OIDC thông thường. Cả hai lựa chọn đều tốt hơn việc lưu mã thông báo Vault có thời hạn dài trong Kubernetes Secret. Các triển khai dùng sidecar hoặc bộ chèn Vault Agent có thể sử dụng `token_file`.

Đối với thiết lập Vault nhiều đối tượng thuê, hãy giữ việc định tuyến đối tượng thuê trong chính sách Vault và cấu hình triển khai. OpenClaw không yêu cầu điểm gắn, vai trò hoặc đường dẫn cố định: mỗi môi trường Gateway có thể đặt `OPENCLAW_VAULT_KV_MOUNT`, `OPENCLAW_VAULT_AUTH_ROLE` và ID SecretRef riêng. Nếu một Gateway dùng chung phải đồng thời phân giải nhiều người dùng Vault khác nhau, hãy sử dụng các nhà cung cấp `exec` được cấu hình thủ công để bao bọc các môi trường xác thực riêng biệt, hoặc phân tách đối tượng thuê giữa các môi trường Gateway với môi trường Vault riêng.

## Liên quan

  * [Quản lý bí mật](</vi/gateway/secrets>)
  * [`openclaw secrets`](</vi/cli/secrets>)
  * [Danh mục Plugin](</vi/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue