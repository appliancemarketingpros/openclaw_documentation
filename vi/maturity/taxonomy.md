---
title: Phân loại mức độ trưởng thành
source_url: https://docs.openclaw.ai/vi/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Phân loại mức độ hoàn thiện

mô hình đứng sau bảng điểm

Bề mặt > danh mục > năng lực > bằng chứng.

50 bề mặt được nhóm thành 4 nhóm, trong đó mỗi danh mục đều liên kết lại với tài liệu chuẩn và mã ID phạm vi QA.

Duyệt các lĩnh vực sản phẩm / Mở phân loại chi tiết / [Xem điểm](</vi/maturity/scorecard>)

## Cách đọc trang này

Bề mặt là một lĩnh vực sản phẩm như runtime Gateway, Discord, hoặc ứng dụng macOS. Mỗi bề mặt chứa các danh mục, và mỗi danh mục chứa các kiểm tra ở cấp năng lực mà các kịch bản QA bao phủ. Hãy dùng bảng điểm để đánh giá ở cấp phát hành; dùng trang này để kiểm tra mô hình bên dưới bảng điểm.

## Mức độ hoàn thiện

M0Đã lên kế hoạchĐịnh hướng đã rõ, nhưng chưa có đường dẫn người dùng được hỗ trợ.Thăng cấp: Có vấn đề thiết kế, chủ sở hữu, và bề mặt mục tiêu.

M1Thử nghiệmĐược triển khai kèm các lưu ý, cờ, bản dựng từ mã nguồn, hoặc luồng chỉ dành cho maintainer.Thăng cấp: Maintainer có thể chạy kịch bản từ main hiện tại.

M2AlphaNgười dùng thực có thể dùng thử, nhưng có thể có thay đổi phá vỡ tương thích và UX chưa hoàn chỉnh.Thăng cấp: Thiết lập có tài liệu, kiểm thử cơ bản, lưu ý đã biết, và ít nhất một bằng chứng trong môi trường thực.

M3BetaCó đường dẫn công khai và quy trình làm việc chính dùng được với các lưu ý có giới hạn.Thăng cấp: Tài liệu cài đặt/cập nhật, kiểm thử hồi quy, runbook hỗ trợ, và bằng chứng kịch bản thành công trên môi trường kỳ vọng.

M4Ổn địnhĐường dẫn được khuyến nghị cho người dùng thông thường. Lỗi được xem là hồi quy.Thăng cấp: Cổng phát hành, đường dẫn doctor/khắc phục sự cố, tài liệu rộng, và bằng chứng thực tế lặp lại.

M5ClawesomeĐược trau chuốt, dễ dùng, có đo lường tốt, và cạnh tranh với quy trình làm việc tương đương tốt nhất.Thăng cấp: Ổn định cộng với đạt bảng điểm người dùng trên các nhóm người dùng đại diện.

## Lĩnh vực sản phẩm

### Lõi

CLI M4Ổn định7 lĩnh vực - hoàn thành 90% runtime Gateway M4Ổn định13 lĩnh vực - hoàn thành 89% Runtime tác tử M3Beta9 lĩnh vực - hoàn thành 79% Phiên, bộ nhớ, và công cụ ngữ cảnh M3Beta9 lĩnh vực - hoàn thành 79% Khung kênh M3Beta8 lĩnh vực - hoàn thành 79% Khả năng quan sát M3Beta5 lĩnh vực - hoàn thành 79% Ứng dụng Web Gateway M3Beta6 lĩnh vực - hoàn thành 79% Plugin M3Beta9 lĩnh vực - hoàn tất 79% Bảo mật, xác thực, ghép nối và bí mật M3Beta6 lĩnh vực - hoàn tất 79% Tự động hóa: cron, hook, tác vụ, thăm dò M3Beta6 lĩnh vực - hoàn tất 79% Hiểu phương tiện và tạo sinh phương tiện M2Alpha6 lĩnh vực - hoàn tất 68% Giọng nói và trò chuyện thời gian thực M2Alpha6 lĩnh vực - hoàn tất 68% TUI M2Alpha5 lĩnh vực - hoàn tất 66% ClawHub M2Alpha4 lĩnh vực - hoàn tất 62% OpenClaw App SDK M2Alpha6 lĩnh vực - hoàn tất 53%

### Nền tảng

Máy chủ Gateway Linux M4Ổn định5 lĩnh vực - hoàn tất 89% Máy chủ Gateway macOS M4Ổn định7 lĩnh vực - hoàn tất 88% Lưu trữ bằng Docker và Podman M3Beta4 lĩnh vực - hoàn tất 79% Windows qua WSL2 M3Beta6 lĩnh vực - hoàn tất 79% Raspberry Pi và thiết bị Linux nhỏ M3Beta4 lĩnh vực - hoàn tất 79% Ứng dụng đồng hành macOS M3Beta8 lĩnh vực - hoàn tất 78% Ứng dụng Android M2Alpha7 lĩnh vực - hoàn tất 66% Windows gốc M2Alpha4 khu vực - hoàn thành 66% Lưu trữ Kubernetes M2Alpha4 khu vực - hoàn thành 61% Ứng dụng iOS M1Thử nghiệm8 khu vực - hoàn thành 44% Đường dẫn cài đặt Nix M1Thử nghiệm5 khu vực - hoàn thành 44% Bề mặt đồng hành watchOS M1Thử nghiệm5 khu vực - hoàn thành 44% Ứng dụng đồng hành Linux M0Đã lên kế hoạch5 khu vực - hoàn thành 21% Ứng dụng đồng hành Windows gốc M0Đã lên kế hoạch5 khu vực - hoàn thành 21%

### Kênh

Discord M4Ổn định6 khu vực - hoàn thành 87% Telegram M3Beta5 khu vực - hoàn thành 78% Slack M3Beta5 khu vực - hoàn thành 78% iMessage và BlueBubbles M3Beta5 khu vực - hoàn thành 78% WhatsApp M3Beta5 khu vực - hoàn thành 78% Matrix M2Alpha6 khu vực - hoàn thành 67% Google Chat M2Alpha5 khu vực - hoàn thành 66% Microsoft Teams M2Alpha5 khu vực - hoàn thành 66% Signal M2Alpha5 khu vực - hoàn thành 66% Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, kênh khu vực M2Alpha4 khu vực - hoàn thành 58% Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Alpha4 khu vực - hoàn thành 54% Kênh cuộc gọi thoại M1Thử nghiệm5 khu vực - hoàn thành 44%

### Nhà cung cấp và công cụ

Công cụ tự động hóa trình duyệt, exec và sandbox M3Beta3 khu vực - hoàn thành 79% Đường dẫn nhà cung cấp OpenAI và Codex M3Beta5 khu vực - hoàn thành 79% Công cụ tìm kiếm web M3Beta4 khu vực - hoàn thành 79% Đường dẫn nhà cung cấp Anthropic M3Beta5 khu vực - hoàn thành 78% Đường dẫn nhà cung cấp Google M3Beta5 khu vực - hoàn thành 78% Đường dẫn nhà cung cấp OpenRouter M3Beta4 khu vực - hoàn thành 78% Công cụ tạo hình ảnh, video và âm nhạc M2Alpha5 khu vực - hoàn thành 68% Nhà cung cấp mô hình cục bộ: Ollama, vLLM, SGLang, LM Studio M2Alpha5 khu vực - hoàn thành 68% Nhà cung cấp được lưu trữ đuôi dài M2Alpha3 khu vực - hoàn thành 68%

## Chi tiết

### Lõi

CLI - M4 Ổn định - 7 khu vực

Các đường dẫn thiết lập và sửa chữa thông thường được ghi lại trong tài liệu cài đặt, CLI và gateway. Các đường dẫn dành riêng cho nền tảng Windows được theo dõi trong các hàng Windows qua WSL2 và Windows gốc.

Phạm vi Thử nghiệm - 4%Chất lượng Ổn định - 83%Mức độ hoàn thiện Ổn định - 90%Một phần - 6

Thiết lập CLI 6 năng lực / được hỗ trợ LTS

Thử nghiệm17%

Ổn định89%

Ổn định90%

[Chỉ mục](</vi/install>), [Trình cài đặt](</vi/install/installer>), [Node](</vi/install/node>), [Cập nhật](</vi/install/updating>)

Thiết lập khởi động và xác thực 5 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Thiết lập ban đầu](</vi/cli/onboard>), [Cấu hình](</vi/cli/configure>), [Tổng quan thiết lập ban đầu](</vi/start/onboarding-overview>)

Thiết lập Plugin và kênh 5 năng lực

Thử nghiệm0%

Beta75%

Ổn định89%

[Thiết lập ban đầu](</vi/cli/onboard>), [Plugin](</vi/cli/plugins>), [Kênh](</vi/cli/channels>)

Quản lý dịch vụ Gateway 5 năng lực / được hỗ trợ LTS

Thử nghiệm14%

Ổn định87%

Ổn định90%

[Gateway](</vi/cli/gateway>), [Cập nhật](</vi/install/updating>), [Khắc phục sự cố](</vi/gateway/troubleshooting>)

Khả năng quan sát CLI 5 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Ổn định89%

Ổn định90%

[Trạng thái](</vi/cli/status>), [Sức khỏe](</vi/cli/health>), [Nhật ký](</vi/cli/logs>), [Chẩn đoán](</vi/gateway/diagnostics>)

Trình kiểm tra 10 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Ổn định89%

Ổn định90%

[Trình kiểm tra](</vi/cli/doctor>), [Trình kiểm tra](</vi/gateway/doctor>), [Bí mật](</vi/gateway/secrets>), [Khắc phục sự cố](</vi/gateway/troubleshooting>)

Cập nhật và nâng cấp 5 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Cập nhật](</vi/install/updating>), [Cập nhật](</vi/cli/update>), [Khắc phục sự cố](</vi/gateway/troubleshooting>)

Thời gian chạy Gateway - M4 Ổn định - 13 khu vực

Kiến trúc lõi, xác thực, ghép nối, tài liệu giao thức, tài liệu daemon và runbook CLI đều bao quát rộng và hiện hành.

Mức bao phủ Thử nghiệm - 6%Chất lượng Ổn định - 81%Mức hoàn thiện Ổn định - 89%Một phần - 12

Phê duyệt và thực thi từ xa 6 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Giao thức](</vi/gateway/protocol>), [Chỉ mục](</vi/gateway/security>)

API HTTP 4 năng lực / được hỗ trợ LTS

Thử nghiệm25%

Ổn định90%

Ổn định90%

[Chỉ mục](</vi/gateway>), [API HTTP OpenAI](</vi/gateway/openai-http-api>), [API HTTP OpenResponses](</vi/gateway/openresponses-http-api>), [API HTTP gọi công cụ](</vi/gateway/tools-invoke-http-api>), [Hook](</vi/automation/hooks>), [Chỉ mục](</vi/web>)

Bề mặt web được lưu trữ 4 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Ổn định89%

Ổn định90%

[Chỉ mục](</vi/gateway>), [Kiến trúc](</vi/concepts/architecture>), [Giao diện điều khiển](</vi/web/control-ui>), [Trò chuyện web](</vi/web/webchat>), [Canvas](</vi/refactor/canvas>)

API RPC và sự kiện của Gateway 20 năng lực / được hỗ trợ LTS

Thử nghiệm9%

Ổn định90%

Ổn định90%

[Giao thức](</vi/gateway/protocol>), [Chỉ mục](</vi/gateway>), [Kiến trúc](</vi/concepts/architecture>)

Xác thực và ghép nối thiết bị 10 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Giao thức](</vi/gateway/protocol>), [Ghép nối](</vi/gateway/pairing>), [Chỉ mục](</vi/gateway/security>)

Truy cập và khám phá mạng 6 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Chỉ mục](</vi/gateway>), [Khám phá](</vi/gateway/discovery>), [Giao thức](</vi/gateway/protocol>)

Các Node và năng lực từ xa 8 năng lực

Thử nghiệm0%

Beta75%

Ổn định89%

[Giao thức](</vi/gateway/protocol>), [Kiến trúc](</vi/concepts/architecture>), [Chỉ mục](</vi/nodes>)

Sức khỏe, chẩn đoán và sửa chữa 7 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Chỉ mục](</vi/gateway>), [Chẩn đoán](</vi/gateway/diagnostics>), [Doctor](</vi/gateway/doctor>)

Khả năng tương thích giao thức 7 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Giao thức](</vi/gateway/protocol>), [Kiến trúc](</vi/concepts/architecture>), [Typebox](</vi/concepts/typebox>), [Giao thức cầu nối](</vi/gateway/bridge-protocol>)

Vai trò và quyền 5 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Giao thức](</vi/gateway/protocol>), [Chỉ mục](</vi/gateway/security>)

Vòng đời Gateway 7 năng lực / được hỗ trợ LTS

Thử nghiệm33%

Ổn định90%

Ổn định90%

[Chỉ mục](</vi/gateway>), [Kiến trúc](</vi/concepts/architecture>)

Kiểm soát bảo mật 6 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Chỉ mục](</vi/gateway/security>), [Giao thức](</vi/gateway/protocol>), [Khám phá](</vi/gateway/discovery>)

Kết nối WebSocket 8 năng lực / được hỗ trợ LTS

Thử nghiệm13%

Ổn định90%

Ổn định90%

[Giao thức](</vi/gateway/protocol>), [Kiến trúc](</vi/concepts/architecture>)

Thời gian chạy của tác tử - M3 Beta - 9 lĩnh vực

Vòng lặp chính, mô hình, định tuyến nhà cung cấp và truyền luồng công cụ là các thành phần hạng nhất, nhưng hành vi của nhà cung cấp thay đổi hằng tuần và cần bằng chứng kịch bản cho mỗi bản phát hành.

Phạm vi Thử nghiệm - 33%Chất lượng Beta - 78%Mức độ hoàn thiện Beta - 79%Một phần - 6

Thực thi lượt tác tử 3 khả năng / được hỗ trợ LTS

Thử nghiệm29%

Beta79%

Beta79%

[Vòng lặp tác tử](</vi/concepts/agent-loop>), [Tác tử](</vi/cli/agent>), [Runtime của tác tử](</vi/concepts/agent-runtimes>)

Runtime bên ngoài và tác tử con 4 khả năng

Thử nghiệm30%

Beta79%

Beta79%

[Runtime của tác tử](</vi/concepts/agent-runtimes>), [Anthropic](</vi/providers/anthropic>), [Google](</vi/providers/google>), [Tác tử con](</vi/tools/subagents>)

Thực thi nhà cung cấp được lưu trữ 5 khả năng / được hỗ trợ LTS

Thử nghiệm20%

Beta79%

Beta79%

[Openai](</vi/providers/openai>), [Anthropic](</vi/providers/anthropic>), [Google](</vi/providers/google>), [Mô hình](</vi/concepts/models>)

Nhà cung cấp cục bộ và tự lưu trữ 5 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[Ollama](</vi/providers/ollama>), [Mô hình](</vi/concepts/models>), [Tác tử](</vi/cli/agent>)

Lựa chọn mô hình và runtime 4 khả năng / được hỗ trợ LTS

Thử nghiệm25%

Beta79%

Beta79%

[Mô hình](</vi/concepts/models>), [Mô hình](</vi/cli/models>), [Openai](</vi/providers/openai>), [Runtime của tác tử](</vi/concepts/agent-runtimes>)

Xác thực nhà cung cấp 10 khả năng / được hỗ trợ LTS

Thử nghiệm24%

Beta79%

Beta79%

[Mô hình](</vi/concepts/models>), [Tác tử](</vi/cli/agent>), [Mô hình](</vi/cli/models>), [Openai](</vi/providers/openai>), [Anthropic](</vi/providers/anthropic>), [Google](</vi/providers/google>), [Tác tử con](</vi/tools/subagents>)

Streaming và tiến trình 2 khả năng

Alpha56%

Beta79%

Beta79%

[Streaming](</vi/concepts/streaming>), [Vòng lặp tác tử](</vi/concepts/agent-loop>)

Lệnh gọi công cụ và xử lý phản hồi 3 khả năng / được hỗ trợ LTS

Alpha65%

Beta79%

Beta79%

[Vòng lặp tác tử](</vi/concepts/agent-loop>), [Ollama](</vi/providers/ollama>)

Điều khiển thực thi công cụ 6 khả năng / được hỗ trợ LTS

Alpha50%

Beta79%

Beta79%

[Hộp cát so với chính sách công cụ so với quyền nâng cao](</vi/gateway/sandbox-vs-tool-policy-vs-elevated>), [Vòng lặp tác nhân](</vi/concepts/agent-loop>), [Tác nhân con](</vi/tools/subagents>)

Phiên, bộ nhớ và bộ máy ngữ cảnh - M3 Beta - 9 lĩnh vực

Tài liệu vững chắc và triển khai đang hoạt động. Mức độ trưởng thành phụ thuộc vào độ bền của transcript, chất lượng Compaction và tính tương đương giữa các client.

Độ bao phủ Thử nghiệm - 30%Chất lượng Beta - 77%Mức độ hoàn chỉnh Beta - 79%Một phần - 6

Quản lý phiên CLI và bản ghi phiên 2 khả năng / được hỗ trợ LTS

Thử nghiệm0%

Alpha68%

Beta79%

[Phiên](</vi/concepts/session>), [Compaction quản lý phiên](</vi/reference/session-management-compaction>), [Phiên](</vi/cli/sessions>)

Quản lý token 3 khả năng / được hỗ trợ LTS

Thử nghiệm20%

Beta79%

Beta79%

[Compaction](</vi/concepts/compaction>), [Ngữ cảnh](</vi/concepts/context>), [Compaction quản lý phiên](</vi/reference/session-management-compaction>)

Công cụ ngữ cảnh 2 khả năng / được hỗ trợ LTS

Alpha57%

Beta79%

Beta79%

[Ngữ cảnh](</vi/concepts/context>), [Công cụ ngữ cảnh](</vi/concepts/context-engine>), [Harness công cụ ngữ cảnh Codex](</vi/plan/codex-context-engine-harness>)

Lịch sử liên ứng dụng khách và tính tương đương phiên 2 khả năng

Thử nghiệm40%

Beta79%

Beta79%

[Trò chuyện web](</vi/web/webchat>), [Android](</vi/platforms/android>), [Định tuyến kênh](</vi/channels/channel-routing>)

Chẩn đoán, bảo trì và khôi phục 3 khả năng

Thử nghiệm40%

Beta79%

Beta79%

[Chẩn đoán](</vi/gateway/diagnostics>), [Compaction quản lý phiên](</vi/reference/session-management-compaction>), [Cờ](</vi/diagnostics/flags>)

Prompt lõi và ngữ cảnh 2 khả năng / được hỗ trợ LTS

Thử nghiệm38%

Beta79%

Beta79%

[Ngữ cảnh](</vi/concepts/context>), [Vệ sinh bản ghi phiên](</vi/reference/transcript-hygiene>), [Discord](</vi/channels/discord>)

Bộ nhớ 5 khả năng

Thử nghiệm46%

Beta79%

Beta79%

[Cấu hình bộ nhớ](</vi/reference/memory-config>), [Bộ nhớ Qmd](</vi/concepts/memory-qmd>), [Bộ nhớ](</vi/concepts/memory>), [Discord](</vi/channels/discord>)

Định tuyến phiên 2 khả năng / được hỗ trợ LTS

Thử nghiệm25%

Beta79%

Beta79%

[Phiên](</vi/concepts/session>), [Định tuyến kênh](</vi/channels/channel-routing>), [Discord](</vi/channels/discord>)

Lưu giữ bản ghi phiên 2 năng lực / được LTS hỗ trợ

Thử nghiệm0%

Alpha68%

Beta79%

[Compaction quản lý phiên](</vi/reference/session-management-compaction>), [Vệ sinh bản ghi phiên](</vi/reference/transcript-hygiene>)

Khung kênh - M3 Beta - 8 lĩnh vực

Nhiều kênh dùng chung các hợp đồng phân phối và định tuyến của Gateway, nhưng hành vi của kênh thay đổi tùy theo API thượng nguồn và các ràng buộc chính sách tài khoản.

Mức bao phủ Thử nghiệm - 13%Chất lượng Beta - 76%Mức hoàn chỉnh Beta - 79%Một phần - 5

Lệnh hành động kênh và phê duyệt 5 khả năng

Thử nghiệm0%

Beta79%

Beta79%

[Nhóm](</vi/channels/groups>), [Discord](</vi/channels/discord>), [Googlechat](</vi/channels/googlechat>), [Signal](</vi/channels/signal>), [Matrix](</vi/channels/matrix>)

Thiết lập kênh 5 khả năng / được hỗ trợ LTS

Thử nghiệm14%

Beta79%

Beta79%

[Chỉ mục](</vi/channels>), [Ghép đôi](</vi/channels/pairing>), [Khắc phục sự cố](</vi/channels/troubleshooting>), [Plugin kênh SDK](</vi/plugins/sdk-channel-plugins>)

Luồng nhóm và hành vi phòng xung quanh 5 khả năng

Thử nghiệm36%

Beta79%

Beta79%

[Nhóm](</vi/channels/groups>), [Tin nhắn nhóm](</vi/channels/group-messages>), [Sự kiện phòng xung quanh](</vi/channels/ambient-room-events>), [Nhóm phát sóng](</vi/channels/broadcast-groups>), [Discord](</vi/channels/discord>)

Truy cập đầu vào và cổng danh tính 5 khả năng / được hỗ trợ LTS

Thử nghiệm0%

Alpha68%

Beta79%

[Nhóm truy cập](</vi/channels/access-groups>), [Nhóm](</vi/channels/groups>), [Discord](</vi/channels/discord>), [LINE](</vi/channels/line>)

Tệp đính kèm phương tiện và dữ liệu kênh phong phú 4 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[LINE](</vi/channels/line>), [Signal](</vi/channels/signal>), [Googlechat](</vi/channels/googlechat>), [Matrix](</vi/channels/matrix>), [Discord](</vi/channels/discord>)

Phân phối đầu ra và quy trình trả lời 4 khả năng / được hỗ trợ LTS

Thử nghiệm38%

Beta79%

Beta79%

[Nhóm](</vi/channels/groups>), [Sự kiện phòng xung quanh](</vi/channels/ambient-room-events>), [Discord](</vi/channels/discord>), [Matrix](</vi/channels/matrix>), [Kênh cấu hình](</vi/gateway/config-channels>)

Định tuyến và phân phối cuộc trò chuyện 10 khả năng / được hỗ trợ LTS

Thử nghiệm19%

Beta79%

Beta79%

[Định tuyến kênh](</vi/channels/channel-routing>), [Nhóm](</vi/channels/groups>), [Discord](</vi/channels/discord>), [Matrix](</vi/channels/matrix>), [Khắc phục sự cố](</vi/channels/troubleshooting>), [Tài liệu tham chiếu cấu hình](</vi/gateway/configuration-reference>)

Tình trạng trạng thái và điều khiển của người vận hành 4 khả năng / được hỗ trợ LTS

Thử nghiệm0%

Beta79%

Beta79%

[Tình trạng](</vi/gateway/health>), [Tham chiếu cấu hình](</vi/gateway/configuration-reference>), [Khắc phục sự cố](</vi/channels/troubleshooting>), [Discord](</vi/channels/discord>)

Observability - M3 Beta - 5 areas

Tài liệu về OTel, Prometheus, ghi log và chẩn đoán đã có. Cần một lượt hoàn thiện công khai về “người vận hành nên xem gì trước tiên”.

Phạm vi bao phủ Thử nghiệm - 18%Chất lượng Beta - 75%Mức độ hoàn thiện Beta - 79%Một phần - 3

Sức khỏe và sửa chữa 12 năng lực / được LTS hỗ trợ

Thử nghiệm28%

Beta79%

Beta79%

[Sức khỏe](</vi/gateway/health>), [Telegram](</vi/channels/telegram>), [Doctor](</vi/cli/doctor>), [Doctor](</vi/gateway/doctor>), [Đường dẫn con SDK](</vi/plugins/sdk-subpaths>), [Sức khỏe](</vi/cli/health>), [Giao thức](</vi/gateway/protocol>)

Ghi nhật ký 5 năng lực / được LTS hỗ trợ

Thử nghiệm0%

Alpha68%

Beta79%

[Ghi nhật ký](</vi/logging>), [Ghi nhật ký](</vi/gateway/logging>), [Nhật ký](</vi/cli/logs>)

Thu thập chẩn đoán 8 năng lực

Thử nghiệm30%

Beta79%

Beta79%

[Chẩn đoán](</vi/gateway/diagnostics>), [Sức khỏe](</vi/gateway/health>), [Codex Harness](</vi/plugins/codex-harness>), [Giao thức](</vi/gateway/protocol>)

Xuất telemetry 13 năng lực

Thử nghiệm33%

Beta79%

Beta79%

[Hook](</vi/plugins/hooks>), [Opentelemetry](</vi/gateway/opentelemetry>), [Ghi nhật ký](</vi/logging>), [Đường dẫn con SDK](</vi/plugins/sdk-subpaths>), [Diagnostics Otel](</vi/plugins/reference/diagnostics-otel>), [Prometheus](</vi/gateway/prometheus>), [Diagnostics Prometheus](</vi/plugins/reference/diagnostics-prometheus>)

Chẩn đoán phiên 4 năng lực / được LTS hỗ trợ

Thử nghiệm0%

Alpha68%

Beta79%

[Opentelemetry](</vi/gateway/opentelemetry>), [Prometheus](</vi/gateway/prometheus>), [Chẩn đoán](</vi/gateway/diagnostics>), [Giao thức](</vi/gateway/protocol>)

Ứng dụng web Gateway - M3 Beta - 6 khu vực

Giao diện web được ghi tài liệu với các luồng ghép đôi, trò chuyện, PWA, Talk, đẩy và Gateway từ xa. Nâng cấp sau các bảng điểm trên nhiều trình duyệt và PWA di động.

Phạm vi bao phủ Thử nghiệm - 4%Chất lượng Beta - 74%Mức độ hoàn thiện Beta - 79%Không có

Trò chuyện thời gian thực trên trình duyệt 5 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[Giao diện điều khiển](</vi/web/control-ui>), [Giao thức](</vi/gateway/protocol>), [Trò chuyện](</vi/nodes/talk>)

Quyền truy cập và độ tin cậy trên trình duyệt 5 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[Giao diện điều khiển](</vi/web/control-ui>), [Bảng điều khiển](</vi/web/dashboard>), [Tailscale](</vi/gateway/tailscale>), [Từ xa](</vi/gateway/remote>)

Cấu hình 5 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[Giao diện điều khiển](</vi/web/control-ui>), [Cấu hình](</vi/gateway/configuration>)

Giao diện trình duyệt 10 khả năng

Thử nghiệm8%

Beta79%

Beta79%

[Giao diện điều khiển](</vi/web/control-ui>), [Mục lục](</vi/web>), [Bảng điều khiển](</vi/web/dashboard>), [Giao thức](</vi/gateway/protocol>)

Cuộc trò chuyện WebChat 15 khả năng

Thử nghiệm10%

Beta79%

Beta79%

[Giao diện điều khiển](</vi/web/control-ui>), [Webchat](</vi/web/webchat>), [Bắt đầu](</vi/start/getting-started>), [Định tuyến kênh](</vi/channels/channel-routing>), [Thao tác tệp an toàn](</vi/gateway/security/secure-file-operations>)

Bảng điều khiển vận hành 10 khả năng

Thử nghiệm8%

Beta79%

Beta79%

[Giao diện điều khiển](</vi/web/control-ui>), [Tình trạng](</vi/gateway/health>), [Giao thức](</vi/gateway/protocol>), [Bảng điều khiển](</vi/web/dashboard>)

Plugin - M3 Beta - 9 mảng

Tài liệu rộng và bằng chứng runtime nội bộ vững chắc hiện có trên các manifest, khám phá, tải, kiến trúc nhà cung cấp/công cụ và ranh giới phê duyệt. Giữ hàng này ở mức beta cho đến khi bằng chứng về API/subpath SDK công khai và phân phối bên ngoài mạnh hơn.

Phạm vi bao phủ thử nghiệm - 12%Chất lượng Beta - 72%Mức độ hoàn thiện Beta - 79%Một phần - 7

Biên soạn và đóng gói Plugin 8 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha68%

Beta79%

[Xây dựng Plugin](</vi/plugins/building-plugins>), [Tổng quan SDK](</vi/plugins/sdk-overview>), [Điểm vào SDK](</vi/plugins/sdk-entrypoints>), [Đường dẫn con SDK](</vi/plugins/sdk-subpaths>), [Manifest](</vi/plugins/manifest>), [Tham chiếu](</vi/plugins/reference>)

Plugin đi kèm 5 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha68%

Beta79%

[Danh mục Plugin](</vi/plugins/plugin-inventory>), [Plugin](</vi/cli/plugins>), [Nội bộ kiến trúc](</vi/plugins/architecture-internals>)

Plugin Canvas 6 năng lực

Thử nghiệm0%

Alpha68%

Beta79%

[Canvas](</vi/plugins/reference/canvas>), [Canvas](</vi/refactor/canvas>), [Tham chiếu cấu hình](</vi/gateway/configuration-reference>)

Cài đặt và chạy Plugin 6 năng lực / được hỗ trợ LTS

Thử nghiệm35%

Beta79%

Beta79%

[Kiến trúc](</vi/plugins/architecture>), [Nội bộ kiến trúc](</vi/plugins/architecture-internals>), [Plugin](</vi/cli/plugins>)

Plugin kênh 5 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha68%

Beta79%

[Plugin kênh SDK](</vi/plugins/sdk-channel-plugins>), [Kênh SDK gửi vào](</vi/plugins/sdk-channel-inbound>), [Kênh SDK gửi ra](</vi/plugins/sdk-channel-outbound>)

Plugin nhà cung cấp và công cụ 6 năng lực / được hỗ trợ LTS

Thử nghiệm43%

Beta79%

Beta79%

[Plugin nhà cung cấp SDK](</vi/plugins/sdk-provider-plugins>), [Plugin công cụ](</vi/plugins/tool-plugins>), [Thêm năng lực](</vi/plugins/adding-capabilities>)

Phê duyệt Plugin 6 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha68%

Beta79%

[Yêu cầu quyền Plugin](</vi/plugins/plugin-permission-requests>), [Phê duyệt Exec](</vi/tools/exec-approvals>), [Plugin kênh SDK](</vi/plugins/sdk-channel-plugins>)

Phát hành Plugin 6 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha68%

Beta79%

[Plugin](</vi/cli/plugins>), [Tương thích](</vi/plugins/compatibility>), [Xuất bản](</vi/clawhub/publishing>)

Kiểm thử Plugin 6 khả năng

Thử nghiệm27%

Beta79%

Beta79%

[Kiểm thử SDK](</vi/plugins/sdk-testing>), [Thiết lập SDK](</vi/plugins/sdk-setup>), [Bộ kiểm thử Codex](</vi/plugins/codex-harness>)

Bảo mật, xác thực, ghép đôi và bí mật - M3 Beta - 6 khu vực

Các tài liệu tốt và bề mặt gia cố đã có. Hãy nâng cấp sau khi các lần chạy kịch bản nâng cấp/bảo mật định kỳ chứng minh không có hồi quy thiết lập.

Phạm vi Experimental - 16%Chất lượng Beta - 72%Độ hoàn chỉnh Beta - 79%Một phần - 5

Chính sách phê duyệt và biện pháp bảo vệ công cụ 2 năng lực / được LTS hỗ trợ

Alpha50%

Beta79%

Beta79%

[Phê duyệt Exec](</vi/tools/exec-approvals>), [Phê duyệt](</vi/cli/approvals>), [Yêu cầu quyền của Plugin](</vi/plugins/plugin-permission-requests>), [Kiểm tra kiểm toán](</vi/gateway/security/audit-checks>)

Xác thực Gateway và truy cập từ xa 9 năng lực / được LTS hỗ trợ

Experimental0%

Alpha68%

Beta79%

[Chỉ mục](</vi/gateway/security>), [Runbook phơi lộ](</vi/gateway/security/exposure-runbook>), [Xác thực proxy tin cậy](</vi/gateway/trusted-proxy-auth>), [Tailscale](</vi/gateway/tailscale>), [Từ xa](</vi/gateway/remote>), [Tham chiếu cấu hình](</vi/gateway/configuration-reference>), [Gateway](</vi/cli/gateway>), [Doctor](</vi/cli/doctor>), [Giao diện điều khiển](</vi/web/control-ui>), [Điều khiển trình duyệt](</vi/tools/browser-control>), [Kiểm tra kiểm toán](</vi/gateway/security/audit-checks>)

Kiểm soát truy cập kênh 3 năng lực / được LTS hỗ trợ

Experimental0%

Alpha68%

Beta79%

[Ghép đôi](</vi/channels/pairing>), [Telegram](</vi/channels/telegram>), [Nhóm truy cập](</vi/channels/access-groups>), [Kiểm tra kiểm toán](</vi/gateway/security/audit-checks>)

Ghép đôi thiết bị và Node 11 năng lực / được LTS hỗ trợ

Experimental0%

Alpha68%

Beta79%

[Giao thức](</vi/gateway/protocol>), [Thiết bị](</vi/cli/devices>), [Ghép đôi](</vi/channels/pairing>), [Ghép đôi](</vi/gateway/pairing>), [Phạm vi người vận hành](</vi/gateway/operator-scopes>), [Giao diện điều khiển](</vi/web/control-ui>), [Webchat](</vi/web/webchat>), [Phê duyệt](</vi/cli/approvals>)

Độ tin cậy Plugin 2 năng lực

Experimental0%

Alpha68%

Beta79%

[Manifest](</vi/plugins/manifest>), [Yêu cầu quyền của Plugin](</vi/plugins/plugin-permission-requests>), [Quản lý Plugin](</vi/plugins/manage-plugins>), [Kiểm tra kiểm toán](</vi/gateway/security/audit-checks>)

Vệ sinh thông tin xác thực và bí mật 5 năng lực / được LTS hỗ trợ

Experimental46%

Beta79%

Beta79%

[Xác thực](</vi/gateway/authentication>), [Mô hình](</vi/cli/models>), [Openai](</vi/providers/openai>), [Oauth](</vi/concepts/oauth>), [Bí mật](</vi/gateway/secrets>), [Bí mật](</vi/cli/secrets>), [Bề mặt thông tin xác thực Secretref](</vi/reference/secretref-credential-surface>), [Kiểm tra kiểm toán](</vi/gateway/security/audit-checks>)

Tự động hóa: cron, hook, tác vụ, polling - M3 Beta - 6 khu vực

Đã được ghi tài liệu và có thể sử dụng, nhưng bằng chứng kịch bản nên bao phủ việc phân phối không giám sát, thử lại và khả năng hiển thị lỗi.

Phạm vi Experimental - 2%Chất lượng Beta - 72%Độ hoàn chỉnh Beta - 79%Không có

Tác vụ Cron 15 khả năng

Thử nghiệm0%

Beta79%

Beta79%

[Tác vụ Cron](</vi/automation/cron-jobs>), [Cron](</vi/cli/cron>), [Giao thức](</vi/gateway/protocol>), [Tác vụ](</vi/automation/tasks>), [Discord](</vi/channels/discord>)

Tiếp nhận sự kiện 15 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[Telegram](</vi/channels/telegram>), [Zalo](</vi/channels/zalo>), [Khắc phục sự cố](</vi/channels/troubleshooting>), [iMessage từ Bluebubbles](</vi/channels/imessage-from-bluebubbles>), [Tích hợp Gmail Pubsub](</vi/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</vi/automation/cron-jobs>), [Webhook](</vi/cli/webhooks>), [Webhook](</vi/automation/cron-jobs#webhooks>), [Webhook](</vi/automation/cron-jobs>)

Hook tự động hóa 11 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[Hook](</vi/automation/hooks>), [Hook](</vi/cli/hooks>), [Hook](</vi/plugins/hooks>), [Yêu cầu quyền Plugin](</vi/plugins/plugin-permission-requests>), [Đường dẫn con SDK](</vi/plugins/sdk-subpaths>)

Tác vụ và luồng nền 10 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[Tác vụ](</vi/automation/tasks>), [Chỉ mục](</vi/automation>), [Tác vụ](</vi/cli/tasks>), [TaskFlow](</vi/automation/taskflow>), [Runtime SDK](</vi/plugins/sdk-runtime>)

Heartbeat 5 khả năng

Thử nghiệm14%

Beta79%

Beta79%

[Chỉ mục](</vi/automation>), [Heartbeat](</vi/gateway/heartbeat>), [Cam kết](</vi/concepts/commitments>)

Điều khiển thăm dò 10 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[Thăm dò](</vi/cli/message>), [Tin nhắn](</vi/cli/message>), [Telegram](</vi/channels/telegram>), [Microsoft Teams](</vi/channels/msteams>), [Tiến trình nền](</vi/gateway/background-process>)

Hiểu phương tiện và tạo phương tiện - M2 Alpha - 6 khu vực

Bề mặt khả năng rộng đã tồn tại, nhưng sự khác biệt giữa các nhà cung cấp, giới hạn tệp và mức tương đương giữa node/ứng dụng khiến phần này chưa ổn định.

Độ bao phủ Thử nghiệm - 2%Chất lượng Alpha - 64%Mức độ hoàn chỉnh Alpha - 68%Không có

Tiếp nhận và truy cập phương tiện 8 khả năng

Thử nghiệm0%

Alpha61%

Alpha68%

[Tổng quan phương tiện](</vi/tools/media-overview>), [Hiểu phương tiện](</vi/nodes/media-understanding>), [Thao tác tệp an toàn](</vi/gateway/security/secure-file-operations>), [PDF](</vi/tools/pdf>), [Tạo hình ảnh](</vi/tools/image-generation>), [QR](</vi/cli/qr>), [LINE](</vi/channels/line>), [WhatsApp](</vi/channels/whatsapp>)

Xử lý phương tiện của kênh 5 khả năng

Thử nghiệm0%

Alpha61%

Alpha68%

[Hình ảnh](</vi/nodes/images>), [Tổng quan phương tiện](</vi/tools/media-overview>), [Discord](</vi/channels/discord>)

Cấu hình phương tiện 1 khả năng

Thử nghiệm0%

Alpha61%

Alpha68%

[Tổng quan phương tiện](</vi/tools/media-overview>), [Tạo hình ảnh](</vi/tools/image-generation>), [Tệp kê khai](</vi/plugins/manifest>), [Bộ kiểm thử Codex](</vi/plugins/codex-harness>)

Phân phối văn bản thành giọng nói 2 khả năng

Thử nghiệm0%

Alpha61%

Alpha68%

[TTS](</vi/tools/tts>), [Tổng quan phương tiện](</vi/tools/media-overview>), [Discord](</vi/channels/discord>)

Hiểu phương tiện 12 khả năng

Thử nghiệm7%

Alpha69%

Alpha69%

[Âm thanh](</vi/nodes/audio>), [Hiểu phương tiện](</vi/nodes/media-understanding>), [Tổng quan phương tiện](</vi/tools/media-overview>), [WhatsApp](</vi/channels/whatsapp>), [Hình ảnh](</vi/nodes/images>), [Suy luận](</vi/cli/infer>), [PDF](</vi/tools/pdf>)

Tạo phương tiện 17 khả năng

Thử nghiệm5%

Alpha69%

Alpha69%

[Tạo hình ảnh](</vi/tools/image-generation>), [Tổng quan phương tiện](</vi/tools/media-overview>), [Skills](</vi/tools/skills>), [Tạo nhạc](</vi/tools/music-generation>), [Tạo video](</vi/tools/video-generation>)

Giọng nói và trò chuyện thời gian thực - M2 Alpha - 6 khu vực

Có nhiều cách triển khai trên Control UI, ứng dụng và nhà cung cấp. Cần bảng điểm về độ trễ, chế độ lỗi và thiết lập trước beta.

Mức bao phủ Thử nghiệm - 0%Chất lượng Alpha - 61%Mức hoàn thiện Alpha - 68%Không có

Nhà cung cấp đàm thoại 7 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Openai](</vi/providers/openai>), [Google](</vi/providers/google>), [Plugin nhà cung cấp SDK](</vi/plugins/sdk-provider-plugins>), [Đàm thoại](</vi/nodes/talk>), [Giao diện điều khiển](</vi/web/control-ui>)

Phiên đàm thoại thời gian thực 11 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Đàm thoại](</vi/nodes/talk>), [Giao diện điều khiển](</vi/web/control-ui>)

Giọng nói và phiên âm 5 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Đàm thoại](</vi/nodes/talk>), [Openai](</vi/providers/openai>), [Google](</vi/providers/google>)

Đàm thoại trong ứng dụng gốc 4 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Đàm thoại](</vi/nodes/talk>), [Voicewake](</vi/platforms/mac/voicewake>)

Đánh thức bằng giọng nói và định tuyến 4 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Voicewake](</vi/nodes/voicewake>), [Voicewake](</vi/platforms/mac/voicewake>), [Lớp phủ giọng nói](</vi/platforms/mac/voice-overlay>)

Khả năng quan sát đàm thoại 5 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Giao diện điều khiển](</vi/web/control-ui>), [Lớp phủ giọng nói](</vi/platforms/mac/voice-overlay>), [Đàm thoại](</vi/nodes/talk>)

TUI - M2 Alpha - 5 khu vực

Có trong tài liệu và mã nguồn, nhưng ít nổi bật hơn như một quy trình làm việc chính của người dùng. Cần định nghĩa kịch bản rõ ràng.

Mức bao phủ Thử nghiệm - 0%Chất lượng Alpha - 59%Mức hoàn thiện Alpha - 66%Không có

Chế độ runtime 14 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[TUI](</vi/cli/tui>), [TUI](</vi/web/tui>), [Chỉ mục](</vi/cli>)

Đầu vào và lệnh 8 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[TUI](</vi/web/tui>)

Quản lý phiên 3 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[TUI](</vi/web/tui>), [Phiên](</vi/cli/sessions>)

Thực thi shell cục bộ 4 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[TUI](</vi/web/tui>), [TUI](</vi/cli/tui>)

Kết xuất và an toàn đầu ra 4 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[TUI](</vi/web/tui>), [QR](</vi/cli/qr>), [Nhật ký](</vi/cli/logs>), [Hoàn thành](</vi/cli/completion>)

ClawHub - M2 Alpha - 4 khu vực

Tài liệu công khai và khái niệm hệ sinh thái đã có. Cần có thẻ điểm cho cài đặt, độ tin cậy, cập nhật, khôi phục và khả năng tương thích.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Alpha - 58%Mức độ hoàn thiện Alpha - 62%Không có

Xuất bản 7 khả năng

Thử nghiệm0%

Alpha54%

Alpha55%

[Xuất bản](</vi/clawhub/publishing>), [Tạo Skills](</vi/tools/creating-skills>), [Cộng đồng](</vi/plugins/community>)

Khám phá danh mục 5 khả năng

Thử nghiệm0%

Alpha61%

Alpha68%

[Plugin](</vi/tools/plugin>), [Plugin](</vi/cli/plugins>), [Skills](</vi/cli/skills>), [Skills](</vi/tools/skills>), [Cộng đồng](</vi/plugins/community>)

Khả năng tương thích và độ tin cậy 12 khả năng

Thử nghiệm0%

Alpha55%

Alpha56%

[Plugin](</vi/tools/plugin>), [Plugin](</vi/cli/plugins>), [Khả năng tương thích](</vi/plugins/compatibility>), [Kho Plugin](</vi/plugins/plugin-inventory>), [Xuất bản](</vi/clawhub/publishing>), [Skills](</vi/tools/skills>), [Cấu hình Skills](</vi/tools/skills-config>)

Vòng đời và tình trạng Plugin 26 khả năng

Thử nghiệm0%

Alpha61%

Alpha68%

[Plugin](</vi/tools/plugin>), [Plugin](</vi/cli/plugins>), [Skills](</vi/cli/skills>), [Skills](</vi/tools/skills>), [Giao thức](</vi/gateway/protocol>), [Gói](</vi/plugins/bundles>), [Phân giải phụ thuộc](</vi/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 khu vực

OpenClaw App SDK là một hợp đồng ứng dụng bên ngoài riêng biệt, tách khỏi runtime Gateway và Plugin SDK. Điểm số hiện tại cho thấy có đường dẫn `@openclaw/sdk` thực tế, với các khoảng trống quanh đóng gói công khai, tự động khám phá, phê duyệt, helper và khả năng tương thích.

Mức độ bao phủ Thử nghiệm - 3%Chất lượng Alpha - 54%Mức độ hoàn thiện Alpha - 53%Không có

API máy khách 4 năng lực

Thử nghiệm0%

Alpha51%

Alpha50%

[Openclaw Sdk](</vi/gateway/external-apps>), [Thiết kế API Openclaw Sdk](</vi/gateway/external-apps>)

Truy cập Gateway 5 năng lực

Thử nghiệm0%

Alpha53%

Alpha54%

[Openclaw Sdk](</vi/gateway/external-apps>), [Thiết kế API Openclaw Sdk](</vi/gateway/external-apps>), [Giao thức](</vi/gateway/protocol>), [Chỉ mục](</vi/gateway/security>)

Cuộc trò chuyện tác tử 6 năng lực

Thử nghiệm0%

Alpha52%

Alpha52%

[Openclaw Sdk](</vi/gateway/external-apps>), [Thiết kế API Openclaw Sdk](</vi/gateway/external-apps>), [Giao thức](</vi/gateway/protocol>)

Sự kiện và phê duyệt 5 năng lực

Thử nghiệm0%

Alpha52%

Alpha52%

[Openclaw Sdk](</vi/gateway/external-apps>), [Thiết kế API Openclaw Sdk](</vi/gateway/external-apps>), [Giao thức](</vi/gateway/protocol>)

Trình trợ giúp tài nguyên 5 năng lực

Thử nghiệm17%

Alpha62%

Alpha53%

[Openclaw Sdk](</vi/gateway/external-apps>), [Thiết kế API Openclaw Sdk](</vi/gateway/external-apps>)

Khả năng tương thích 5 năng lực

Thử nghiệm0%

Alpha54%

Alpha55%

[Thiết kế API Openclaw Sdk](</vi/gateway/external-apps>), [Typebox](</vi/concepts/typebox>), [Giao thức](</vi/gateway/protocol>)

### Nền tảng

Máy chủ Gateway Linux - M4 ổn định - 5 khu vực

Node runtime được khuyến nghị, dịch vụ người dùng systemd được ghi tài liệu, và hướng dẫn VPS/container có phạm vi rộng.

Phạm vi bao phủ thử nghiệm - 0%Chất lượng Beta - 75%Mức độ hoàn thiện ổn định - 89%Một phần - 4

Thiết lập và cập nhật máy chủ 4 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Mục lục](</vi/install>), [Cập nhật](</vi/install/updating>), [Linux](</vi/platforms/linux>), [Mục lục](</vi/platforms>)

Thời gian chạy Gateway và điều khiển dịch vụ 6 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Mục lục](</vi/gateway>), [Gateway](</vi/cli/gateway>), [Linux](</vi/platforms/linux>), [VPS](</vi/vps>)

Truy cập từ xa và bảo mật 6 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Từ xa](</vi/gateway/remote>), [Tailscale](</vi/gateway/tailscale>), [Sổ tay ứng phó phơi lộ](</vi/gateway/security/exposure-runbook>), [Xác thực](</vi/gateway/authentication>), [Bí mật](</vi/gateway/secrets>)

Chẩn đoán và sửa chữa 4 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta75%

Ổn định89%

[Trạng thái](</vi/cli/status>), [Nhật ký](</vi/cli/logs>), [Doctor](</vi/cli/doctor>), [Chẩn đoán](</vi/gateway/diagnostics>), [Mục lục](</vi/gateway>)

Mục tiêu triển khai 3 năng lực

Thử nghiệm0%

Beta75%

Ổn định89%

[VPS](</vi/vps>), [Docker](</vi/install/docker>), [Hetzner](</vi/install/hetzner>), [Digitalocean](</vi/install/digitalocean>), [Kubernetes](</vi/install/kubernetes>), [Podman](</vi/install/podman>)

Máy chủ Gateway macOS - M4 Ổn định - 7 lĩnh vực

Đường dẫn dịch vụ LaunchAgent, các chế độ Gateway cục bộ/từ xa, cài đặt CLI và tích hợp ứng dụng đã được ghi lại trong tài liệu.

Độ bao phủ Thử nghiệm - 0%Chất lượng Beta - 74%Mức độ hoàn thiện Ổn định - 88%Không có

Thiết lập CLI 4 khả năng

Thử nghiệm0%

Beta74%

Ổn định88%

[Macos](</vi/platforms/macos>), [Gateway tích hợp sẵn](</vi/platforms/mac/bundled-gateway>), [Trình cài đặt](</vi/install/installer>), [Node](</vi/install/node>)

Tích hợp Gateway cục bộ 9 khả năng

Thử nghiệm0%

Beta74%

Ổn định88%

[Macos](</vi/platforms/macos>), [Gateway tích hợp sẵn](</vi/platforms/mac/bundled-gateway>), [Từ xa](</vi/platforms/mac/remote>), [Mục lục](</vi/gateway>), [Gateway](</vi/cli/gateway>), [Bonjour](</vi/gateway/bonjour>)

Chế độ Gateway từ xa 5 khả năng

Thử nghiệm0%

Beta74%

Ổn định88%

[Từ xa](</vi/platforms/mac/remote>), [Từ xa](</vi/gateway/remote>), [Tailscale](</vi/gateway/tailscale>)

Vòng đời dịch vụ Gateway 10 khả năng

Thử nghiệm0%

Beta74%

Ổn định88%

[Macos](</vi/platforms/macos>), [Gateway tích hợp sẵn](</vi/platforms/mac/bundled-gateway>), [Gateway](</vi/cli/gateway>), [Mục lục](</vi/gateway>), [Cập nhật](</vi/cli/update>), [Cập nhật](</vi/install/updating>), [Gỡ cài đặt](</vi/install/uninstall>), [Khắc phục sự cố](</vi/gateway/troubleshooting>)

Chẩn đoán và khả năng quan sát 4 khả năng

Thử nghiệm0%

Beta74%

Ổn định88%

[Gateway tích hợp sẵn](</vi/platforms/mac/bundled-gateway>), [Macos](</vi/platforms/macos>), [Gateway](</vi/cli/gateway>), [Chẩn đoán](</vi/gateway/doctor>), [Khắc phục sự cố](</vi/gateway/troubleshooting>)

Quyền và khả năng gốc 4 khả năng

Thử nghiệm0%

Beta74%

Ổn định88%

[Macos](</vi/platforms/macos>), [Từ xa](</vi/platforms/mac/remote>)

Hồ sơ và cô lập 5 khả năng

Thử nghiệm0%

Beta74%

Ổn định88%

[Nhiều Gateway](</vi/gateway/multiple-gateways>), [Mục lục](</vi/gateway>), [Gateway](</vi/cli/gateway>)

Lưu trữ Docker và Podman - M3 Beta - 4 khu vực

Tài liệu cài đặt đã có và là các đường dẫn triển khai phổ biến. Nâng cấp sau khi smoke định kỳ của bản phát hành ghi nhận hành vi nâng cấp và volume.

Mức bao phủ Thử nghiệm - 7%Chất lượng Beta - 71%Mức hoàn thiện Beta - 79%Không có

Thiết lập container 6 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[Docker](</vi/install/docker>), [Podman](</vi/install/podman>)

Vận hành container 11 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[Podman](</vi/install/podman>), [Môi trường chạy Docker VM](</vi/install/docker-vm-runtime>), [Docker](</vi/install/docker>), [Hetzner](</vi/install/hetzner>), [Hostinger](</vi/install/hostinger>)

Phát hành và xác thực image 5 khả năng

Thử nghiệm29%

Beta79%

Beta79%

[Docker](</vi/install/docker>), [Môi trường chạy Docker VM](</vi/install/docker-vm-runtime>), [Xác thực bản phát hành đầy đủ](</vi/reference/full-release-validation>)

Sandbox và công cụ cho agent 3 khả năng

Thử nghiệm0%

Alpha68%

Beta79%

[Docker](</vi/install/docker>), [Môi trường chạy Docker VM](</vi/install/docker-vm-runtime>)

Windows qua WSL2 - M3 Beta - 6 khu vực

Lộ trình Windows được khuyến nghị với hướng dẫn systemd/dịch vụ người dùng và tài liệu chuỗi khởi động. Nâng cấp sau các bảng điểm cài đặt/cập nhật lặp lại.

Phạm vi bao phủ Thử nghiệm - 6%Chất lượng Alpha - 69%Mức độ hoàn thiện Beta - 79%Một phần - 5

Thiết lập WSL 6 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha67%

Beta79%

[Windows](</vi/platforms/windows>), [Bắt đầu](</vi/start/getting-started>)

CLI 8 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha67%

Beta79%

[Windows](</vi/platforms/windows>), [Bắt đầu](</vi/start/getting-started>), [Cập nhật](</vi/install/updating>), [Onboard](</vi/cli/onboard>), [Doctor](</vi/cli/doctor>), [Trạng thái](</vi/cli/status>), [Nhật ký](</vi/cli/logs>)

Vòng đời dịch vụ Gateway 10 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha67%

Beta79%

[Windows](</vi/platforms/windows>), [Chỉ mục](</vi/gateway>), [Doctor](</vi/gateway/doctor>)

Truy cập và phơi bày Gateway 11 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha67%

Beta79%

[Xác thực](</vi/gateway/authentication>), [Bí mật](</vi/gateway/secrets>), [Từ xa](</vi/gateway/remote>), [Sổ tay vận hành phơi bày](</vi/gateway/security/exposure-runbook>), [Windows](</vi/platforms/windows>)

Chẩn đoán và sửa chữa 6 năng lực / được hỗ trợ LTS

Thử nghiệm38%

Beta79%

Beta79%

[Windows](</vi/platforms/windows>), [Trạng thái](</vi/cli/status>), [Nhật ký](</vi/cli/logs>), [Doctor](</vi/cli/doctor>), [Doctor](</vi/gateway/doctor>)

Trình duyệt và giao diện điều khiển 6 năng lực

Thử nghiệm0%

Alpha67%

Beta79%

[Khắc phục sự cố CDP từ xa của trình duyệt WSL2 Windows](</vi/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Trình duyệt](</vi/tools/browser>), [Giao diện điều khiển](</vi/web/control-ui>)

Raspberry Pi và các thiết bị Linux nhỏ - M3 Beta - 4 khu vực

Tài liệu nền tảng đã có và đường dẫn Gateway dựa trên Linux. Cần bằng chứng smoke bản phát hành dành riêng cho phần cứng để chuyển lên mức cao hơn.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Alpha - 67%Mức độ hoàn thiện Beta - 79%Không có

Thiết lập và khả năng tương thích 12 năng lực

Thử nghiệm0%

Alpha67%

Beta79%

[Raspberry Pi](</vi/install/raspberry-pi>), [Chỉ mục](</vi/install>), [Câu hỏi thường gặp về lần chạy đầu tiên](</vi/help/faq-first-run>), [Câu hỏi thường gặp](</vi/help/faq>), [Linux](</vi/platforms/linux>), [Trình cài đặt](</vi/install/installer>)

Truy cập từ xa và xác thực 9 năng lực

Thử nghiệm0%

Alpha67%

Beta79%

[Raspberry Pi](</vi/install/raspberry-pi>), [Xác thực](</vi/gateway/authentication>), [Bí mật](</vi/gateway/secrets>), [Ghép nối](</vi/gateway/pairing>), [Thiết bị](</vi/cli/devices>), [Từ xa](</vi/gateway/remote>), [Tailscale](</vi/gateway/tailscale>)

Thời gian chạy Gateway 10 năng lực

Thử nghiệm0%

Alpha67%

Beta79%

[Chỉ mục](</vi/gateway>), [Gateway](</vi/cli/gateway>), [Raspberry Pi](</vi/install/raspberry-pi>), [Linux](</vi/platforms/linux>), [VPS](</vi/vps>)

Hiệu năng và chẩn đoán 5 năng lực

Thử nghiệm0%

Alpha67%

Beta79%

[Raspberry Pi](</vi/install/raspberry-pi>), [Linux](</vi/platforms/linux>), [Sức khỏe](</vi/gateway/health>), [Chẩn đoán](</vi/gateway/diagnostics>)

Ứng dụng đồng hành macOS - M3 Beta - 8 khu vực

Ứng dụng thanh menu phong phú, quyền, chế độ Node, Canvas, đánh thức bằng giọng nói, WebChat và chế độ từ xa đã có. Vẫn còn thay đổi nhanh nên chưa đạt Stable.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Alpha - 66%Mức độ hoàn chỉnh Beta - 78%Không có

Khung vẽ 4 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Khung vẽ](</vi/platforms/mac/canvas>), [macOS](</vi/platforms/macos>), [Trò chuyện web](</vi/web/webchat>)

Thiết lập cục bộ 7 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Gateway đi kèm](</vi/platforms/mac/bundled-gateway>), [macOS](</vi/platforms/macos>), [Tiến trình con](</vi/platforms/mac/child-process>), [Thiết lập phát triển](</vi/platforms/mac/dev-setup>)

Trạng thái và cài đặt 5 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Thanh menu](</vi/platforms/mac/menu-bar>), [Biểu tượng](</vi/platforms/mac/icon>), [macOS](</vi/platforms/macos>), [Tình trạng](</vi/platforms/mac/health>), [Ghi log](</vi/platforms/mac/logging>), [Từ xa](</vi/platforms/mac/remote>)

Khả năng gốc 5 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[macOS](</vi/platforms/macos>), [Xpc](</vi/platforms/mac/xpc>), [Quyền](</vi/platforms/mac/permissions>), [Ký](</vi/platforms/mac/signing>), [Peekaboo](</vi/platforms/mac/peekaboo>)

Kết nối từ xa 3 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Từ xa](</vi/platforms/mac/remote>), [macOS](</vi/platforms/macos>), [Từ xa](</vi/gateway/remote>)

Giọng nói và trò chuyện 3 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Đánh thức bằng giọng nói](</vi/platforms/mac/voicewake>), [Lớp phủ giọng nói](</vi/platforms/mac/voice-overlay>), [Trò chuyện](</vi/nodes/talk>), [macOS](</vi/platforms/macos>)

Trò chuyện web 3 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Trò chuyện web](</vi/platforms/mac/webchat>), [macOS](</vi/platforms/macos>), [Trò chuyện web](</vi/web/webchat>)

Trò chuyện web từ xa 5 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Trò chuyện web](</vi/platforms/mac/webchat>), [Từ xa](</vi/gateway/remote>), [Từ xa](</vi/platforms/mac/remote>)

Ứng dụng Android - M2 Alpha - 7 lĩnh vực

Đường dẫn Google Play công khai đã tồn tại, nhưng tài liệu ứng dụng vẫn mô tả bản dựng lại là cực kỳ alpha và nêu rõ công việc củng cố cho bản phát hành.

Mức bao phủ Thử nghiệm - 0%Chất lượng Alpha - 59%Mức độ hoàn thiện Alpha - 66%Không có

Thu phương tiện 1 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Android](</vi/platforms/android>), [Camera](</vi/nodes/camera>)

Trò chuyện di động 1 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Android](</vi/platforms/android>)

Thiết lập kết nối 1 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Android](</vi/platforms/android>), [Bonjour](</vi/gateway/bonjour>), [Ghép nối](</vi/gateway/pairing>)

Phân phối 3 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Android](</vi/platforms/android>)

Cài đặt 1 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Android](</vi/platforms/android>)

Giọng nói 1 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Android](</vi/platforms/android>), [Trò chuyện](</vi/nodes/talk>)

Runtime thiết bị 2 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Android](</vi/platforms/android>), [Khắc phục sự cố](</vi/nodes/troubleshooting>), [Giao thức](</vi/gateway/protocol>)

Windows native - M2 Alpha - 4 mảng

Các luồng CLI/Gateway cốt lõi hoạt động, nhưng tài liệu vẫn khuyến nghị WSL2 để có trải nghiệm đầy đủ và liệt kê các lưu ý khi chạy native.

Mức bao phủ Thử nghiệm - 0%Chất lượng Alpha - 58%Mức hoàn thiện Alpha - 66%Một phần - 1

CLI 9 khả năng / được hỗ trợ LTS

Thử nghiệm0%

Alpha54%

Alpha64%

[Chỉ mục](</vi/install>), [Trình cài đặt](</vi/install/installer>), [Windows](</vi/platforms/windows>), [Bắt đầu](</vi/start/getting-started>), [Onboard](</vi/cli/onboard>)

Quản lý Gateway 11 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Windows](</vi/platforms/windows>), [Chỉ mục](</vi/gateway>), [Gateway](</vi/cli/gateway>), [Doctor](</vi/cli/doctor>)

Mạng 4 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Windows](</vi/platforms/windows>), [Chỉ mục](</vi/gateway>), [Gateway](</vi/cli/gateway>)

Cập nhật 4 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Cập nhật](</vi/install/updating>), [CI](</vi/ci>)

Lưu trữ Kubernetes - M2 Alpha - 4 khu vực

Lưu trữ Kubernetes là một lộ trình triển khai cụm riêng biệt dựa trên Kustomize. Điểm số hiện tại cho thấy một lộ trình triển khai tối thiểu thực tế, với các khoảng trống quanh CI dành riêng cho Kubernetes, đóng gói ingress/TLS/NetworkPolicy, sao lưu/khôi phục và gia cố khả năng phơi bày trong môi trường sản xuất.

Mức bao phủ Thử nghiệm - 0%Chất lượng Alpha - 55%Mức hoàn thiện Alpha - 61%Không có

Thiết lập triển khai 5 năng lực

Thử nghiệm0%

Alpha55%

Alpha61%

[Kubernetes](</vi/install/kubernetes>), [Chỉ mục](</vi/install>)

Cấu hình và bí mật 5 năng lực

Thử nghiệm0%

Alpha55%

Alpha61%

[Kubernetes](</vi/install/kubernetes>), [Bí mật](</vi/gateway/secrets>), [Môi trường](</vi/help/environment>)

Truy cập và phơi lộ 5 năng lực

Thử nghiệm0%

Alpha55%

Alpha61%

[Kubernetes](</vi/install/kubernetes>), [Xác thực](</vi/gateway/authentication>), [Từ xa](</vi/gateway/remote>), [Runbook về phơi lộ](</vi/gateway/security/exposure-runbook>)

Vòng đời cụm 5 năng lực

Thử nghiệm0%

Alpha55%

Alpha61%

[Kubernetes](</vi/install/kubernetes>), [Chỉ mục](</vi/gateway>)

Ứng dụng iOS - M1 Thử nghiệm - 8 khu vực

Bản xem trước nội bộ / siêu alpha. Các luồng đẩy dựa trên TestFlight và relay đã có, nhưng chưa có phân phối công khai.

Mức bao phủ Thử nghiệm - 0%Chất lượng Thử nghiệm - 41%Mức hoàn thiện Thử nghiệm - 44%Không có

Phương tiện và chia sẻ 1 khả năng

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>), [Camera](</vi/nodes/camera>)

Canvas và màn hình 1 khả năng

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>), [Canvas](</vi/plugins/reference/canvas>)

Trò chuyện và phiên 1 khả năng

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>), [Trò chuyện web](</vi/web/webchat>), [Giao thức](</vi/gateway/protocol>)

Thiết lập và chẩn đoán Gateway 7 khả năng

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>), [Ghép nối](</vi/channels/pairing>)

Phân phối 1 khả năng

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>)

Lệnh thiết bị 2 khả năng

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>), [Giao thức](</vi/gateway/protocol>)

Thông báo và nền 1 khả năng

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>), [Cấu hình](</vi/gateway/configuration>)

Giọng nói 1 khả năng

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>), [Talk](</vi/nodes/talk>)

Nix install path - M1 Experimental - 5 areas

Quy trình cài đặt tùy chọn. Cần cam kết hỗ trợ rõ ràng hơn trước khi quảng bá lên alpha/beta.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Thử nghiệm - 41%Mức độ hoàn thiện Thử nghiệm - 44%Không có

Bàn giao cài đặt 4 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Nix](</vi/install/nix>), [Mục lục](</vi/install>), [Thư mục tài liệu](</vi/start/docs-directory>)

Vòng đời Plugin 4 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Quản lý Plugin](</vi/plugins/manage-plugins>), [Plugin](</vi/tools/plugin>), [Nix](</vi/install/nix>)

Kích hoạt và trải nghiệm người dùng ứng dụng 7 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Nix](</vi/install/nix>)

Cấu hình và trạng thái 7 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Nix](</vi/install/nix>), [Thiết lập](</vi/cli/setup>), [Môi trường](</vi/help/environment>)

Thời gian chạy dịch vụ và cơ chế bảo vệ 8 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Nix](</vi/install/nix>), [Thiết lập](</vi/cli/setup>), [Doctor](</vi/cli/doctor>), [Cập nhật](</vi/cli/update>)

bề mặt đồng hành watchOS - M1 Thử nghiệm - 5 khu vực

Nguồn có các bề mặt ứng dụng/tiện ích mở rộng Watch; tài liệu công khai chưa trình bày nội dung này như một tính năng dành cho người dùng.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Thử nghiệm - 41%Mức độ hoàn chỉnh Thử nghiệm - 44%Không có

Phân phối và khôi phục 7 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>)

Phê duyệt thực thi 3 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Phê duyệt thực thi](</vi/tools/exec-approvals>), [Ios](</vi/platforms/ios>)

Phân phối và hỗ trợ 6 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>)

Thông báo và trả lời 7 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>)

Giao diện ứng dụng đồng hồ 3 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Ios](</vi/platforms/ios>)

Ứng dụng đồng hành Linux - M0 Đã lên kế hoạch - 5 khu vực

Tài liệu cho biết các ứng dụng đồng hành Linux gốc đã được lên kế hoạch; Gateway là đường dẫn Linux được hỗ trợ hiện nay.

Phạm vi Thử nghiệm - 0%Chất lượng Thử nghiệm - 19%Mức độ hoàn chỉnh Thử nghiệm - 21%Không có

Phân phối ứng dụng 3 năng lực

Thử nghiệm0%

Thử nghiệm19%

Thử nghiệm21%

[Linux](</vi/platforms/linux>), [Chỉ mục](</vi/platforms>), [Chỉ mục](</vi/install>)

Kết nối Gateway 4 năng lực

Thử nghiệm0%

Thử nghiệm19%

Thử nghiệm21%

[Linux](</vi/platforms/linux>), [Chỉ mục](</vi/gateway>), [Ghép nối](</vi/gateway/pairing>), [Từ xa](</vi/gateway/remote>)

Trò chuyện và phiên 3 năng lực

Thử nghiệm0%

Thử nghiệm19%

Thử nghiệm21%

[Linux](</vi/platforms/linux>), [Giao thức](</vi/gateway/protocol>), [Trò chuyện web](</vi/web/webchat>)

Năng lực desktop 9 năng lực

Thử nghiệm0%

Thử nghiệm19%

Thử nghiệm21%

[Linux](</vi/platforms/linux>), [Phê duyệt thực thi](</vi/tools/exec-approvals>), [Bí mật](</vi/gateway/secrets>), [Chỉ mục](</vi/nodes>), [Thực thi](</vi/tools/exec>), [Nói chuyện](</vi/nodes/talk>), [Camera](</vi/nodes/camera>)

Trạng thái và chẩn đoán 7 năng lực

Thử nghiệm0%

Thử nghiệm19%

Thử nghiệm21%

[Linux](</vi/platforms/linux>), [OpenClaw](</vi/start/openclaw>), [Doctor](</vi/gateway/doctor>)

Ứng dụng đồng hành gốc cho Windows - M0 Đã lên kế hoạch - 5 khu vực

Chỉ mới được lên kế hoạch.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Thử nghiệm - 19%Mức độ hoàn thiện Thử nghiệm - 21%Không có

Cài đặt và cập nhật 4 khả năng

Thử nghiệm0%

Thử nghiệm19%

Thử nghiệm21%

[Windows](</vi/platforms/windows>), [Chỉ mục](</vi/install>)

Kết nối Gateway 3 khả năng

Thử nghiệm0%

Thử nghiệm19%

Thử nghiệm21%

[Windows](</vi/platforms/windows>), [Chỉ mục](</vi/gateway>), [Ghép nối](</vi/gateway/pairing>), [Từ xa](</vi/gateway/remote>)

Phiên trò chuyện 2 khả năng

Thử nghiệm0%

Thử nghiệm19%

Thử nghiệm21%

[Windows](</vi/platforms/windows>), [Giao thức](</vi/gateway/protocol>)

Trạng thái và sửa chữa 5 khả năng

Thử nghiệm0%

Thử nghiệm19%

Thử nghiệm21%

[Windows](</vi/platforms/windows>), [Doctor](</vi/gateway/doctor>), [Chỉ mục](</vi/gateway>)

Công cụ desktop và quyền 10 khả năng

Thử nghiệm0%

Thử nghiệm19%

Thử nghiệm21%

[Windows](</vi/platforms/windows>), [Chỉ mục](</vi/nodes>), [Exec](</vi/tools/exec>), [Phê duyệt Exec](</vi/tools/exec-approvals>), [Chỉ mục](</vi/gateway/security>)

### Kênh

Discord - M4 Ổn định - 6 mảng

Tài liệu chuyên sâu và độ bao phủ tính năng rộng. Các luồng thoại/ủy quyền nên tiếp tục được chấm điểm riêng là beta/alpha.

Độ bao phủ Thử nghiệm - 0%Chất lượng Beta - 73%Mức độ hoàn chỉnh Ổn định - 87%Một phần - 4

Thiết lập và vận hành kênh 10 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta73%

Ổn định87%

[Discord](</vi/channels/discord>), [Discord](</vi/plugins/reference/discord>), [Fly](</vi/install/fly>), [Lệnh Slash](</vi/tools/slash-commands>), [Sức khỏe](</vi/gateway/health>), [Kênh](</vi/cli/channels>), [Cấu hình kênh](</vi/gateway/config-channels>)

Truy cập và danh tính 6 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta73%

Ổn định87%

[Discord](</vi/channels/discord>), [Ghép nối](</vi/channels/pairing>), [Nhóm truy cập](</vi/channels/access-groups>), [Nhóm](</vi/channels/groups>)

Định tuyến và phân phối cuộc trò chuyện 12 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta73%

Ổn định87%

[Discord](</vi/channels/discord>), [Định tuyến kênh](</vi/channels/channel-routing>), [Nhóm](</vi/channels/groups>), [Nhóm truy cập](</vi/channels/access-groups>), [Tác nhân ACP](</vi/tools/acp-agents>), [Tác nhân con](</vi/tools/subagents>)

Phương tiện và nội dung phong phú 1 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta73%

Ổn định87%

[Discord](</vi/channels/discord>)

Điều khiển gốc và phê duyệt 5 năng lực

Thử nghiệm0%

Beta73%

Ổn định87%

[Discord](</vi/channels/discord>), [Lệnh Slash](</vi/tools/slash-commands>)

Thoại và cuộc gọi thời gian thực 5 năng lực

Thử nghiệm0%

Beta73%

Ổn định87%

[Discord](</vi/channels/discord>), [Openai](</vi/providers/openai>), [Elevenlabs](</vi/providers/elevenlabs>), [Tự động hóa QA E2E](</vi/concepts/qa-e2e-automation>), [Cấu hình kênh](</vi/gateway/config-channels>)

Telegram - M3 Beta - 5 khu vực

Kênh lõi đã đủ trưởng thành để sử dụng thường xuyên, nhưng UX có độ biến thiên cao và các trường hợp biên về phương tiện cần bằng chứng kịch bản định kỳ.

Độ phủ Thử nghiệm - 0%Chất lượng Alpha - 68%Mức hoàn thiện Beta - 78%Đầy đủ - 5

Thiết lập và vận hành kênh 10 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha66%

Beta78%

[Telegram](</vi/channels/telegram>), [Kênh cấu hình](</vi/gateway/config-channels>), [Kênh](</vi/cli/channels>)

Quyền truy cập và danh tính 10 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha66%

Beta78%

[Telegram](</vi/channels/telegram>), [Ghép nối](</vi/channels/pairing>), [Nhóm truy cập](</vi/channels/access-groups>), [Nhóm](</vi/channels/groups>), [Đa tác nhân](</vi/concepts/multi-agent>)

Định tuyến và phân phối hội thoại 1 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha66%

Beta78%

[Telegram](</vi/channels/telegram>), [Nhóm](</vi/channels/groups>), [Đa tác nhân](</vi/concepts/multi-agent>)

Phương tiện và nội dung phong phú 1 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha66%

Beta78%

[Telegram](</vi/channels/telegram>), [Vị trí](</vi/channels/location>)

Điều khiển gốc và phê duyệt 9 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Beta77%

Beta79%

[Telegram](</vi/channels/telegram>), [Phê duyệt thực thi](</vi/tools/exec-approvals>), [Phản ứng](</vi/tools/reactions>)

Slack - M3 Beta - 5 khu vực

Tài liệu kênh và bề mặt định tuyến hạng nhất. Cần bảng điểm kịch bản cài đặt/quản trị không gian làm việc.

Mức bao phủ Thử nghiệm - 0%Chất lượng Alpha - 66%Mức hoàn thiện Beta - 78%Đầy đủ - 5

Thiết lập và vận hành kênh 10 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha66%

Beta78%

[Slack](</vi/channels/slack>), [Slack](</vi/plugins/reference/slack>), [Bí mật](</vi/gateway/secrets>), [Tự động hóa QA E2E](</vi/concepts/qa-e2e-automation>), [Khắc phục sự cố](</vi/channels/troubleshooting>)

Quyền truy cập và danh tính 1 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha66%

Beta78%

[Slack](</vi/channels/slack>), [Ghép đôi](</vi/channels/pairing>)

Định tuyến và phân phối cuộc trò chuyện 5 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha66%

Beta78%

[Slack](</vi/channels/slack>), [Bảo vệ vòng lặp bot](</vi/channels/bot-loop-protection>), [Ghép đôi](</vi/channels/pairing>)

Phương tiện và nội dung phong phú 1 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha66%

Beta78%

[Slack](</vi/channels/slack>), [Tự động hóa QA E2E](</vi/concepts/qa-e2e-automation>)

Điều khiển gốc và phê duyệt 8 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha66%

Beta78%

[Slack](</vi/channels/slack>), [Lệnh slash](</vi/tools/slash-commands>), [Phê duyệt thực thi](</vi/tools/exec-approvals>)

iMessage và BlueBubbles - M3 Beta - 5 khu vực

iMessage được hỗ trợ chạy qua imsg trên máy chủ macOS Messages đã đăng nhập; các cấu hình BlueBubbles cũ cần được di chuyển. Hãy hiển thị rõ các lưu ý về quyền macOS, trình bao bọc SSH, SIP/API riêng tư và di chuyển.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Alpha - 66%Mức độ hoàn thiện Beta - 78%Không có

Thiết lập và vận hành kênh 11 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Bluebubbles Imessage](</vi/announcements/bluebubbles-imessage>), [Imessage từ Bluebubbles](</vi/channels/imessage-from-bluebubbles>), [Cấu hình kênh](</vi/gateway/config-channels>), [Imessage](</vi/channels/imessage>)

Truy cập và danh tính 6 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Imessage](</vi/channels/imessage>), [Imessage từ Bluebubbles](</vi/channels/imessage-from-bluebubbles>), [Cấu hình kênh](</vi/gateway/config-channels>)

Định tuyến và phân phối cuộc trò chuyện 4 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Imessage](</vi/channels/imessage>)

Phương tiện và nội dung phong phú 7 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Imessage](</vi/channels/imessage>), [Imessage từ Bluebubbles](</vi/channels/imessage-from-bluebubbles>), [Cấu hình kênh](</vi/gateway/config-channels>)

Điều khiển gốc và phê duyệt 3 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Imessage](</vi/channels/imessage>)

WhatsApp - M3 Beta - 5 khu vực

Đường dẫn lõi quan trọng và đã được ghi tài liệu; tính biến động của Baileys/phiên thượng nguồn khiến nó vẫn ở dưới mức Ổn định.

Độ bao phủ Thử nghiệm - 0%Chất lượng Alpha - 66%Mức độ hoàn chỉnh Beta - 78%Không có

Thiết lập và vận hành kênh 5 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[WhatsApp](</vi/channels/whatsapp>), [Cấu hình kênh](</vi/gateway/config-channels>), [WhatsApp](</vi/plugins/reference/whatsapp>), [Tự động hóa QA E2E](</vi/concepts/qa-e2e-automation>), [Doctor](</vi/gateway/doctor>)

Truy cập và danh tính 7 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[WhatsApp](</vi/channels/whatsapp>), [Cấu hình kênh](</vi/gateway/config-channels>), [Tự động hóa QA E2E](</vi/concepts/qa-e2e-automation>), [Ghép đôi](</vi/channels/pairing>)

Định tuyến và phân phối cuộc trò chuyện 4 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[WhatsApp](</vi/channels/whatsapp>), [Tin nhắn nhóm](</vi/channels/group-messages>)

Phương tiện và nội dung phong phú 2 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[WhatsApp](</vi/channels/whatsapp>)

Điều khiển gốc và phê duyệt 2 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[WhatsApp](</vi/channels/whatsapp>)

Matrix - M2 Alpha - 6 lĩnh vực

Được hỗ trợ thông qua Plugin đi kèm. Cần bảng điểm cho cầu nối, xác thực và vòng đời phòng.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Alpha - 60%Mức độ hoàn thiện Alpha - 67%Không có

Thiết lập và vận hành kênh 5 năng lực

Thử nghiệm0%

Alpha60%

Alpha67%

[Matrix](</vi/channels/matrix>), [Di chuyển Matrix](</vi/channels/matrix-migration>)

Truy cập và danh tính 7 năng lực

Thử nghiệm0%

Alpha60%

Alpha67%

[Matrix](</vi/channels/matrix>), [Nhóm](</vi/channels/groups>), [Bảo vệ chống vòng lặp bot](</vi/channels/bot-loop-protection>)

Định tuyến và phân phối hội thoại 1 năng lực

Thử nghiệm0%

Alpha60%

Alpha67%

[Matrix](</vi/channels/matrix>)

Phương tiện và nội dung phong phú 1 năng lực

Thử nghiệm0%

Alpha60%

Alpha67%

[Matrix](</vi/channels/matrix>)

Điều khiển gốc và phê duyệt 6 năng lực

Thử nghiệm0%

Alpha60%

Alpha67%

[Matrix](</vi/channels/matrix>)

Mã hóa và xác minh 3 năng lực

Thử nghiệm0%

Alpha60%

Alpha67%

[Matrix](</vi/channels/matrix>), [Di chuyển Matrix](</vi/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 areas

Kênh đã được ghi tài liệu, nhưng việc thiết lập doanh nghiệp/quản trị làm tăng rủi ro về mức độ trưởng thành.

Độ phủ Thử nghiệm - 0%Chất lượng Alpha - 59%Mức độ hoàn thiện Alpha - 66%Không có

Thiết lập và vận hành kênh 16 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[Googlechat](</vi/channels/googlechat>), [Googlechat](</vi/plugins/reference/googlechat>), [Cấu hình kênh](</vi/gateway/config-channels>), [Tham chiếu Wizard CLI](</vi/start/wizard-cli-reference>), [Bí mật](</vi/gateway/secrets>), [Bề mặt thông tin xác thực Secretref](</vi/reference/secretref-credential-surface>), [Sức khỏe](</vi/gateway/health>), [Kho Plugin](</vi/plugins/plugin-inventory>), [Chỉ mục](</vi/channels>)

Truy cập và danh tính 11 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[Googlechat](</vi/channels/googlechat>), [Ghép nối](</vi/channels/pairing>), [Nhóm truy cập](</vi/channels/access-groups>), [Cấu hình kênh](</vi/gateway/config-channels>), [Bảo vệ vòng lặp bot](</vi/channels/bot-loop-protection>), [Định tuyến kênh](</vi/channels/channel-routing>)

Định tuyến và phân phối cuộc trò chuyện 1 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[Googlechat](</vi/channels/googlechat>), [Bảo vệ vòng lặp bot](</vi/channels/bot-loop-protection>), [Nhóm truy cập](</vi/channels/access-groups>), [Định tuyến kênh](</vi/channels/channel-routing>)

Phương tiện và nội dung phong phú 1 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[Googlechat](</vi/channels/googlechat>), [Tin nhắn](</vi/cli/message>), [Hiểu phương tiện](</vi/nodes/media-understanding>), [Bề mặt thông tin xác thực Secretref](</vi/reference/secretref-credential-surface>)

Điều khiển gốc và phê duyệt 16 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[Googlechat](</vi/channels/googlechat>), [Tin nhắn](</vi/cli/message>), [Hiểu phương tiện](</vi/nodes/media-understanding>), [Bề mặt thông tin xác thực Secretref](</vi/reference/secretref-credential-surface>), [Phản ứng](</vi/tools/reactions>), [Lệnh gạch chéo](</vi/tools/slash-commands>), [Cấu hình tác nhân](</vi/gateway/config-agents>), [Tái cấu trúc vòng đời tin nhắn](</vi/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 khu vực

Các luồng xác thực/quản trị doanh nghiệp cần bằng chứng kịch bản rõ ràng.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Alpha - 59%Mức độ hoàn chỉnh Alpha - 66%Không có

Thiết lập và vận hành kênh 9 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[Msteams](</vi/channels/msteams>), [Msteams](</vi/plugins/reference/msteams>), [Cấu hình kênh](</vi/gateway/config-channels>), [Tình trạng](</vi/gateway/health>)

Truy cập và danh tính 9 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[Msteams](</vi/channels/msteams>), [Ghép nối](</vi/channels/pairing>), [Nhóm truy cập](</vi/channels/access-groups>)

Định tuyến và chuyển phát hội thoại 5 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[Msteams](</vi/channels/msteams>), [Nhóm](</vi/channels/groups>), [Định tuyến kênh](</vi/channels/channel-routing>)

Phương tiện và nội dung phong phú 5 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[Msteams](</vi/channels/msteams>)

Điều khiển và phê duyệt gốc 5 năng lực

Thử nghiệm0%

Alpha59%

Alpha66%

[Msteams](</vi/channels/msteams>), [Phê duyệt thực thi nâng cao](</vi/tools/exec-approvals-advanced>)

Signal - M2 Alpha - 5 khu vực

Tài liệu kênh được hỗ trợ đã có; cần bằng chứng cài đặt và kết nối lại mạnh hơn.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Alpha - 59%Mức độ hoàn thiện Alpha - 66%Không có

Thiết lập và vận hành kênh 7 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Signal](</vi/channels/signal>), [Signal](</vi/plugins/reference/signal>)

Truy cập và danh tính 6 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Signal](</vi/channels/signal>)

Định tuyến và phân phối cuộc trò chuyện 1 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Signal](</vi/channels/signal>)

Nội dung đa phương tiện và phong phú 7 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Signal](</vi/channels/signal>)

Điều khiển gốc và phê duyệt 3 khả năng

Thử nghiệm0%

Alpha59%

Alpha66%

[Signal](</vi/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, kênh khu vực - M2 Alpha - 4 khu vực

Phạm vi bao phủ khu vực quan trọng, nhưng mức hỗ trợ công khai nên được hiệu chỉnh theo từng loại tài khoản, phê duyệt từ thượng nguồn và bằng chứng của người bảo trì.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Alpha - 55%Mức độ hoàn thiện Alpha - 58%Không có

Thiết lập và vận hành kênh 6 khả năng

Thử nghiệm0%

Alpha61%

Alpha68%

[Chỉ mục](</vi/channels>), [Ghép nối](</vi/channels/pairing>), [Feishu](</vi/plugins/reference/feishu>), [Nội bộ kiến trúc](</vi/plugins/architecture-internals>)

Quyền truy cập và danh tính 1 khả năng

Thử nghiệm0%

Alpha53%

Alpha54%

Không có tài liệu được liên kết

Định tuyến và phân phối cuộc trò chuyện 1 khả năng

Thử nghiệm0%

Alpha53%

Alpha54%

Không có tài liệu được liên kết

Phương tiện và nội dung phong phú 1 khả năng

Thử nghiệm0%

Alpha53%

Alpha54%

Không có tài liệu được liên kết

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 khu vực

Các bề mặt được hỗ trợ đã tồn tại, nhưng mức độ trưởng thành có thể thay đổi tùy theo thượng nguồn và phạm vi bao phủ của người bảo trì. Chấm điểm riêng từng mục sau.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Alpha - 53%Mức độ hoàn chỉnh Alpha - 54%Không có

Thiết lập và vận hành kênh 1 năng lực

Thử nghiệm0%

Alpha53%

Alpha54%

Không có tài liệu được liên kết

Quyền truy cập và danh tính 1 năng lực

Thử nghiệm0%

Alpha53%

Alpha54%

Không có tài liệu được liên kết

Định tuyến và phân phối cuộc trò chuyện 1 năng lực

Thử nghiệm0%

Alpha53%

Alpha54%

Không có tài liệu được liên kết

Phương tiện và nội dung phong phú 1 năng lực

Thử nghiệm0%

Alpha53%

Alpha54%

Không có tài liệu được liên kết

Kênh cuộc gọi thoại - M1 Thử nghiệm - 5 lĩnh vực

Đường dẫn tùy chọn/Plugin với hành vi thời gian thực phức tạp. Cần bảng điểm kịch bản trước khi beta công khai.

Mức bao phủ Thử nghiệm - 0%Chất lượng Thử nghiệm - 41%Mức độ hoàn thiện Thử nghiệm - 44%Không có

Thiết lập và vận hành kênh 2 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Cuộc gọi thoại](</vi/cli/voicecall>), [Cuộc gọi thoại](</vi/plugins/voice-call>), [Giao thức](</vi/gateway/protocol>)

Truy cập và danh tính 1 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Cuộc gọi thoại](</vi/plugins/voice-call>), [Cuộc gọi thoại](</vi/cli/voicecall>)

Định tuyến và chuyển phát cuộc trò chuyện 1 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Cuộc gọi thoại](</vi/plugins/voice-call>)

Phương tiện và nội dung phong phú 2 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Cuộc gọi thoại](</vi/plugins/voice-call>), [Bản kiểm kê Plugin](</vi/plugins/plugin-inventory>)

Giọng nói và cuộc gọi thời gian thực 2 năng lực

Thử nghiệm0%

Thử nghiệm41%

Thử nghiệm44%

[Cuộc gọi thoại](</vi/plugins/voice-call>)

### Nhà cung cấp và công cụ

Tự động hóa trình duyệt, exec và công cụ sandbox - M3 Beta - 3 khu vực

Các công cụ cốt lõi đã được ghi tài liệu, nhưng bảo mật máy chủ và trải nghiệm người dùng về quyền nên tiếp tục được rà soát tích cực trong bảng điểm.

Mức bao phủ Thử nghiệm - 21%Chất lượng Beta - 75%Mức độ hoàn thiện Beta - 79%Một phần - 2

Tự động hóa trình duyệt 8 năng lực

Thử nghiệm13%

Beta79%

Beta79%

[Điều khiển trình duyệt](</vi/tools/browser-control>), [Kiểm thử](</vi/help/testing>), [Trình duyệt](</vi/tools/browser>), [Chỉ mục](</vi/gateway/security>), [Kiểm tra kiểm toán](</vi/gateway/security/audit-checks>)

Gọi và thực thi công cụ 6 năng lực / được hỗ trợ LTS

Alpha50%

Beta79%

Beta79%

[Thực thi](</vi/tools/exec>), [Tiến trình nền](</vi/gateway/background-process>), [API HTTP gọi công cụ](</vi/gateway/tools-invoke-http-api>), [Phạm vi toán tử](</vi/gateway/operator-scopes>), [Giao thức](</vi/gateway/protocol>), [Phê duyệt thực thi](</vi/tools/exec-approvals>), [Phê duyệt thực thi nâng cao](</vi/tools/exec-approvals-advanced>), [Nâng quyền](</vi/tools/elevated>)

Sandbox và chính sách công cụ 6 năng lực / được hỗ trợ LTS

Thử nghiệm0%

Alpha68%

Beta79%

[Cơ chế sandbox](</vi/gateway/sandboxing>), [Sandbox so với chính sách công cụ so với nâng quyền](</vi/gateway/sandbox-vs-tool-policy-vs-elevated>), [Công cụ sandbox đa tác tử](</vi/tools/multi-agent-sandbox-tools>), [Tham chiếu bộ khung Codex](</vi/plugins/codex-harness-reference>), [Công cụ cấu hình](</vi/gateway/config-tools>)

Đường dẫn nhà cung cấp OpenAI và Codex - M3 Beta - 5 khu vực

Tài liệu chuyên sâu, đường dẫn OAuth/gói đăng ký, giọng nói thời gian thực, hình ảnh và hành vi tương thích. Sự biến động của nhà cung cấp khiến phần này chưa đạt Ổn định nếu không có bằng chứng bảng điểm phát hành.

Phạm vi bao phủ Thử nghiệm - 26%Chất lượng Beta - 74%Mức độ hoàn thiện Beta - 79%Một phần - 3

Mô hình và xác thực 6 năng lực / được hỗ trợ LTS

Thử nghiệm44%

Beta79%

Beta79%

[Openai](</vi/providers/openai>), [Codex Harness](</vi/plugins/codex-harness>), [Mô hình](</vi/concepts/models>), [Oauth](</vi/concepts/oauth>), [Tham chiếu Codex Harness](</vi/plugins/codex-harness-reference>), [Giám sát xác thực](</vi/gateway/authentication>)

Phản hồi và khả năng tương thích công cụ 4 năng lực / được hỗ trợ LTS

Thử nghiệm40%

Beta79%

Beta79%

[Openai](</vi/providers/openai>), [API HTTP Openresponses](</vi/gateway/openresponses-http-api>), [API HTTP Openai](</vi/gateway/openai-http-api>), [Plugin gốc Codex](</vi/plugins/codex-native-plugins>)

Codex Harness gốc 2 năng lực / được hỗ trợ LTS

Thử nghiệm44%

Beta79%

Beta79%

[Codex Harness](</vi/plugins/codex-harness>), [Thời gian chạy Codex Harness](</vi/plugins/codex-harness-runtime>), [Tham chiếu Codex Harness](</vi/plugins/codex-harness-reference>), [Plugin gốc Codex](</vi/plugins/codex-native-plugins>)

Đầu vào hình ảnh và đa phương thức 2 năng lực

Thử nghiệm0%

Alpha67%

Beta79%

[Openai](</vi/providers/openai>), [Tạo hình ảnh](</vi/tools/image-generation>), [Hình ảnh](</vi/nodes/images>)

Giọng nói và âm thanh thời gian thực 2 năng lực

Thử nghiệm0%

Alpha67%

Beta79%

[Openai](</vi/providers/openai>), [Discord](</vi/channels/discord>), [Cuộc gọi thoại](</vi/plugins/voice-call>)

Công cụ tìm kiếm web - M3 Beta - 4 lĩnh vực

Có nhiều nhà cung cấp và tài liệu. Cần bằng chứng về hạn mức/lỗi/SSRF cho từng nhóm nhà cung cấp.

Phạm vi Thử nghiệm - 9%Chất lượng Beta - 74%Mức độ hoàn chỉnh Beta - 79%Không có

Nhà cung cấp tìm kiếm 19 năng lực

Thử nghiệm11%

Bản beta79%

Bản beta79%

[Web](</vi/tools/web>), [Brave Search](</vi/tools/brave-search>), [Tavily](</vi/tools/tavily>), [Exa Search](</vi/tools/exa-search>), [Firecrawl](</vi/tools/firecrawl>), [Perplexity Search](</vi/tools/perplexity-search>), [Duckduckgo Search](</vi/tools/duckduckgo-search>), [Searxng Search](</vi/tools/searxng-search>), [Gemini Search](</vi/tools/gemini-search>), [Grok Search](</vi/tools/grok-search>), [Kimi Search](</vi/tools/kimi-search>), [Minimax Search](</vi/tools/minimax-search>), [Ollama Search](</vi/tools/ollama-search>), [Đường dẫn phụ SDK](</vi/plugins/sdk-subpaths>), [Tổng quan SDK](</vi/plugins/sdk-overview>), [Manifest](</vi/plugins/manifest>)

Thiết lập và chẩn đoán 9 năng lực

Thử nghiệm0%

Bản alpha68%

Bản beta79%

[Web](</vi/tools/web>), [Tìm nạp Web](</vi/tools/web-fetch>), [Câu hỏi thường gặp](</vi/help/faq>), [Chi phí sử dụng API](</vi/reference/api-usage-costs>), [Brave Search](</vi/tools/brave-search>), [Perplexity Search](</vi/tools/perplexity-search>), [Tavily](</vi/tools/tavily>), [Firecrawl](</vi/tools/firecrawl>)

An toàn mạng 4 năng lực

Thử nghiệm0%

Bản alpha68%

Bản beta79%

[Web](</vi/tools/web>), [Tìm nạp Web](</vi/tools/web-fetch>), [Firecrawl](</vi/tools/firecrawl>), [Searxng Search](</vi/tools/searxng-search>)

Khả dụng công cụ và tìm nạp 11 năng lực

Thử nghiệm25%

Bản beta79%

Bản beta79%

[Cấu hình công cụ](</vi/gateway/config-tools>), [Tìm nạp Web](</vi/tools/web-fetch>), [Web](</vi/tools/web>), [Câu hỏi thường gặp](</vi/help/faq>)

Đường dẫn nhà cung cấp Anthropic - M3 Beta - 5 khu vực

Nhà cung cấp mô hình hạng nhất. Cần bằng chứng kịch bản định kỳ cho xác thực/danh mục/lệnh gọi công cụ.

Mức bao phủ thử nghiệm - 0%Chất lượng bản beta - 71%Mức hoàn thiện bản beta - 78%Không có

Xác thực nhà cung cấp và khôi phục 9 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[Anthropic](</vi/providers/anthropic>), [Doctor](</vi/gateway/doctor>), [Ví dụ cấu hình](</vi/gateway/configuration-examples>), [Khắc phục sự cố](</vi/gateway/troubleshooting>), [Bộ nhớ đệm prompt](</vi/reference/prompt-caching>)

Lựa chọn mô hình và runtime 10 năng lực

Thử nghiệm0%

Beta78%

Beta79%

[Anthropic](</vi/providers/anthropic>), [Tác tử cấu hình](</vi/gateway/config-agents>), [Mô hình](</vi/concepts/models>), [Backend CLI](</vi/gateway/cli-backends>)

Truyền tải yêu cầu và ngữ nghĩa lượt 10 năng lực

Thử nghiệm0%

Beta77%

Beta79%

[Anthropic](</vi/providers/anthropic>), [Bộ nhớ đệm prompt](</vi/reference/prompt-caching>), [Khắc phục sự cố](</vi/gateway/troubleshooting>), [Backend CLI](</vi/gateway/cli-backends>), [Nhà cung cấp mô hình](</vi/concepts/model-providers>)

Bộ nhớ đệm prompt và ngữ cảnh 5 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[Anthropic](</vi/providers/anthropic>), [Bộ nhớ đệm prompt](</vi/reference/prompt-caching>), [Khắc phục sự cố](</vi/gateway/troubleshooting>), [Heartbeat](</vi/gateway/heartbeat>)

Đầu vào phương tiện 4 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[Anthropic](</vi/providers/anthropic>), [Tác tử cấu hình](</vi/gateway/config-agents>)

Đường dẫn nhà cung cấp Google - M3 Beta - 5 lĩnh vực

Nhà cung cấp hạng nhất với các bề mặt mô hình và thời gian thực. Cần chấm điểm riêng cho Live/Talk.

Phạm vi bao phủ Thử nghiệm - 0%Chất lượng Alpha - 66%Mức độ hoàn thiện Beta - 78%Không có

Thiết lập nhà cung cấp và thông tin xác thực 10 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[Google](</vi/providers/google>), [Nhà cung cấp mô hình](</vi/concepts/model-providers>)

Định tuyến mô hình và điểm cuối 10 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[Google](</vi/providers/google>), [Nhà cung cấp mô hình](</vi/concepts/model-providers>), [Google](</vi/plugins/reference/google>), [Tìm kiếm Gemini](</vi/tools/gemini-search>)

Runtime Gemini trực tiếp 9 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[Google](</vi/providers/google>), [Nhà cung cấp mô hình](</vi/concepts/model-providers>), [Câu hỏi thường gặp về mô hình](</vi/help/faq-models>), [Kiểm thử trực tiếp](</vi/help/testing-live>)

Phương tiện, tìm kiếm và thời gian thực 10 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[Google](</vi/plugins/reference/google>), [Google](</vi/providers/google>)

Lưu bộ nhớ đệm prompt 5 năng lực

Thử nghiệm0%

Alpha66%

Beta78%

[Lưu bộ nhớ đệm prompt](</vi/reference/prompt-caching>), [Google](</vi/providers/google>), [Nhà cung cấp mô hình](</vi/concepts/model-providers>), [Mức sử dụng token](</vi/reference/token-use>)

Đường dẫn nhà cung cấp OpenRouter - M3 Beta - 4 khu vực

Đường dẫn nhà cung cấp hợp nhất đã được ghi lại trong tài liệu và có giá trị, nhưng hành vi theo từng mô hình có khác biệt.

Mức bao phủ Thử nghiệm - 0%Chất lượng Alpha - 66%Mức hoàn thiện Beta - 78%Không có

Thiết lập nhà cung cấp và xác thực 14 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Openrouter](</vi/providers/openrouter>), [Nhà cung cấp mô hình](</vi/concepts/model-providers>), [Cấu hình](</vi/cli/configure>), [Xác thực](</vi/gateway/authentication>), [Môi trường](</vi/help/environment>), [Mô hình](</vi/cli/models>), [Mô hình](</vi/concepts/models>)

Thời gian chạy trò chuyện và chuẩn hóa 15 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Openrouter](</vi/providers/openrouter>), [Nhà cung cấp mô hình](</vi/concepts/model-providers>), [Lưu bộ nhớ đệm lời nhắc](</vi/reference/prompt-caching>)

Khôi phục và chẩn đoán nhà cung cấp 5 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Chuyển đổi dự phòng mô hình](</vi/concepts/model-failover>), [Openrouter](</vi/providers/openrouter>), [Mô hình](</vi/cli/models>)

Tạo phương tiện và giọng nói 7 khả năng

Thử nghiệm0%

Alpha66%

Beta78%

[Openrouter](</vi/providers/openrouter>), [Tạo hình ảnh](</vi/tools/image-generation>), [Tạo nhạc](</vi/tools/music-generation>), [Tổng quan về phương tiện](</vi/tools/media-overview>), [Tạo video](</vi/tools/video-generation>), [TTS](</vi/tools/tts>)

Công cụ tạo hình ảnh, video và nhạc - M2 Alpha - 5 lĩnh vực

Khả năng này tồn tại trên nhiều nhà cung cấp, nhưng chất lượng, độ trễ và mức độ tương thích tham số khác nhau quá nhiều để đạt beta nếu không có bằng chứng theo từng nhà cung cấp.

Mức độ bao phủ Thử nghiệm - 0%Chất lượng Alpha - 61%Mức độ hoàn thiện Alpha - 68%Không có

Định tuyến và khám phá phương tiện 4 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Tác tử cấu hình](</vi/gateway/config-agents>), [Tạo hình ảnh](</vi/tools/image-generation>), [Tạo video](</vi/tools/video-generation>), [Tạo nhạc](</vi/tools/music-generation>)

Vòng đời và phân phối tác vụ 12 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Tổng quan về phương tiện](</vi/tools/media-overview>), [Tạo hình ảnh](</vi/tools/image-generation>), [Tạo video](</vi/tools/video-generation>), [Tạo nhạc](</vi/tools/music-generation>)

Tạo hình ảnh 9 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Tạo hình ảnh](</vi/tools/image-generation>), [Suy luận](</vi/cli/infer>), [Tổng quan về phương tiện](</vi/tools/media-overview>)

Tạo video 11 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Tạo video](</vi/tools/video-generation>), [Runway](</vi/providers/runway>), [Pixverse](</vi/providers/pixverse>), [Fal](</vi/providers/fal>), [Openrouter](</vi/providers/openrouter>)

Tạo nhạc 6 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Tạo nhạc](</vi/tools/music-generation>)

Nhà cung cấp mô hình cục bộ: Ollama, vLLM, SGLang, LM Studio - M2 Alpha - 5 lĩnh vực

Hữu ích và có tài liệu, nhưng mức độ khác biệt giữa các môi trường rất cao.

Mức độ bao phủ Thử nghiệm - 0%Chất lượng Alpha - 61%Mức độ hoàn thiện Alpha - 68%Không có

Thiết lập nhà cung cấp, vòng đời và chẩn đoán 12 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Mô hình cục bộ](</vi/gateway/local-models>), [Lmstudio](</vi/providers/lmstudio>), [Ollama](</vi/providers/ollama>), [Vllm](</vi/providers/vllm>), [Dịch vụ mô hình cục bộ](</vi/gateway/local-model-services>), [Cấu hình tác nhân](</vi/gateway/config-agents>), [Khắc phục sự cố](</vi/gateway/troubleshooting>), [Doctor](</vi/gateway/doctor>)

Plugin nhà cung cấp gốc 10 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Ollama](</vi/providers/ollama>), [Lmstudio](</vi/providers/lmstudio>)

Khả năng tương thích runtime tương thích với OpenAI 8 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Vllm](</vi/providers/vllm>), [Sglang](</vi/providers/sglang>), [Mô hình cục bộ](</vi/gateway/local-models>), [Lmstudio](</vi/providers/lmstudio>)

Bộ nhớ cục bộ và biểu diễn nhúng 5 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Bộ nhớ](</vi/concepts/memory>), [Doctor](</vi/gateway/doctor>)

An toàn mạng và kiểm soát lời nhắc 2 năng lực

Thử nghiệm0%

Alpha61%

Alpha68%

[Chỉ mục](</vi/gateway/security>), [Cấu hình công cụ](</vi/gateway/config-tools>), [Mô hình cục bộ](</vi/gateway/local-models>)

Nhà cung cấp được lưu trữ ít phổ biến - M2 Alpha - 3 khu vực

Có nhiều trang tài liệu/tham chiếu; điểm số nên được tạo từ siêu dữ liệu nhà cung cấp cộng với độ bao phủ kiểm thử nhanh trực tiếp.

Độ bao phủ Thử nghiệm - 0%Chất lượng Alpha - 61%Mức độ hoàn chỉnh Alpha - 68%Không có

Nhà cung cấp LLM lưu trữ 12 khả năng

Thử nghiệm0%

Alpha61%

Alpha68%

[Chỉ mục](</vi/providers>), [Nhà cung cấp mô hình](</vi/concepts/model-providers>), [Kiểm thử trực tiếp](</vi/help/testing-live>), [Thiết lập ban đầu](</vi/cli/onboard>)

Nhà cung cấp phương tiện lưu trữ 8 khả năng

Thử nghiệm0%

Alpha61%

Alpha68%

[Tệp kê khai](</vi/plugins/manifest>), [Kiểm thử trực tiếp](</vi/help/testing-live>), [Chỉ mục](</vi/providers>)

Vận hành nhà cung cấp 12 khả năng

Thử nghiệm0%

Alpha61%

Alpha68%

[Chỉ mục](</vi/providers>), [Nhà cung cấp mô hình](</vi/concepts/model-providers>), [Tệp kê khai](</vi/plugins/manifest>), [Kiểm thử trực tiếp](</vi/help/testing-live>), [Mô hình](</vi/cli/models>)

Was this useful?YesNo

Open issue