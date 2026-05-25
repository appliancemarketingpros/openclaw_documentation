---
title: Cơ chế sandbox
source_url: https://docs.openclaw.ai/vi/gateway/sandboxing
scraped_at: 2026-05-25
---

OpenClaw có thể chạy **công cụ bên trong các phần phụ trợ môi trường cách ly** để giảm phạm vi ảnh hưởng. Đây là tính năng **tùy chọn** và được kiểm soát bằng cấu hình (`agents.defaults.sandbox` hoặc `agents.list[].sandbox`). Nếu tắt cách ly, công cụ chạy trên máy chủ. Gateway vẫn ở trên máy chủ; việc thực thi công cụ chạy trong một môi trường cách ly riêng khi được bật.

## Những gì được cách ly

  * Thực thi công cụ (`exec`, `read`, `write`, `edit`, `apply_patch`, `process`, v.v.).
  * Trình duyệt được cách ly tùy chọn (`agents.defaults.sandbox.browser`).


Chi tiết trình duyệt được cách ly

  * Theo mặc định, trình duyệt trong môi trường cách ly tự khởi động (đảm bảo CDP có thể truy cập được) khi công cụ trình duyệt cần đến nó. Cấu hình qua `agents.defaults.sandbox.browser.autoStart` và `agents.defaults.sandbox.browser.autoStartTimeoutMs`.
  * Theo mặc định, các container trình duyệt trong môi trường cách ly dùng một mạng Docker chuyên dụng (`openclaw-sandbox-browser`) thay vì mạng `bridge` toàn cục. Cấu hình bằng `agents.defaults.sandbox.browser.network`.
  * `agents.defaults.sandbox.browser.cdpSourceRange` tùy chọn giới hạn luồng vào CDP ở rìa container bằng danh sách cho phép CIDR (ví dụ `172.21.0.1/32`).
  * Quyền truy cập quan sát noVNC được bảo vệ bằng mật khẩu theo mặc định; OpenClaw phát một URL token ngắn hạn phục vụ trang khởi động cục bộ và mở noVNC với mật khẩu trong phân đoạn URL (không nằm trong nhật ký truy vấn/header).
  * `agents.defaults.sandbox.browser.allowHostControl` cho phép các phiên được cách ly nhắm rõ ràng tới trình duyệt trên máy chủ.
  * Danh sách cho phép tùy chọn kiểm soát `target: "custom"`: `allowedControlUrls`, `allowedControlHosts`, `allowedControlPorts`.


Không được cách ly:

  * Chính tiến trình Gateway.
  * Bất kỳ công cụ nào được cho phép rõ ràng để chạy bên ngoài môi trường cách ly (ví dụ `tools.elevated`). 
    * **Exec nâng quyền bỏ qua cách ly và dùng đường thoát đã cấu hình (`gateway` theo mặc định, hoặc `node` khi đích exec là `node`).**
    * Nếu tắt cách ly, `tools.elevated` không thay đổi cách thực thi (vốn đã ở trên máy chủ). Xem [Chế độ nâng quyền](</vi/tools/elevated>).


## Chế độ

`agents.defaults.sandbox.mode` kiểm soát **khi nào** cách ly được sử dụng:

### off

Không cách ly.

### non-main

Chỉ cách ly các phiên **không phải main** (mặc định nếu bạn muốn các cuộc trò chuyện thông thường chạy trên máy chủ).

`"non-main"` dựa trên `session.mainKey` (mặc định `"main"`), không phải id tác nhân. Các phiên nhóm/kênh dùng khóa riêng, nên chúng được tính là không phải main và sẽ được cách ly.

### all

Mọi phiên đều chạy trong môi trường cách ly.

## Phạm vi

`agents.defaults.sandbox.scope` kiểm soát **số lượng container** được tạo:

  * `"agent"` (mặc định): một container cho mỗi tác nhân.
  * `"session"`: một container cho mỗi phiên.
  * `"shared"`: một container dùng chung cho tất cả các phiên được cách ly.


## Phần phụ trợ

`agents.defaults.sandbox.backend` kiểm soát **runtime nào** cung cấp môi trường cách ly:

  * `"docker"` (mặc định khi bật cách ly): runtime môi trường cách ly dựa trên Docker cục bộ.
  * `"ssh"`: runtime môi trường cách ly từ xa chung dựa trên SSH.
  * `"openshell"`: runtime môi trường cách ly dựa trên OpenShell.


Cấu hình riêng cho SSH nằm dưới `agents.defaults.sandbox.ssh`. Cấu hình riêng cho OpenShell nằm dưới `plugins.entries.openshell.config`.

### Chọn phần phụ trợ

| Docker | SSH | OpenShell  
---|---|---|---  
**Nơi chạy** | Container cục bộ | Bất kỳ máy chủ nào truy cập được qua SSH | Môi trường cách ly do OpenShell quản lý  
**Thiết lập** | `scripts/sandbox-setup.sh` | Khóa SSH + máy chủ đích | Plugin OpenShell đã bật  
**Mô hình workspace** | Gắn kết bind hoặc sao chép | Chuẩn từ xa (gieo một lần) | `mirror` hoặc `remote`  
**Kiểm soát mạng** | `docker.network` (mặc định: không có) | Phụ thuộc vào máy chủ từ xa | Phụ thuộc vào OpenShell  
**Môi trường cách ly trình duyệt** | Được hỗ trợ | Không được hỗ trợ | Chưa được hỗ trợ  
**Gắn kết bind** | `docker.binds` | N/A | N/A  
**Phù hợp nhất cho** | Phát triển cục bộ, cách ly đầy đủ | Chuyển tải sang máy từ xa | Môi trường cách ly từ xa được quản lý với đồng bộ hai chiều tùy chọn  
  
### Phần phụ trợ Docker

Cách ly bị tắt theo mặc định. Nếu bạn bật cách ly và không chọn phần phụ trợ, OpenClaw dùng phần phụ trợ Docker. Nó thực thi công cụ và trình duyệt trong môi trường cách ly cục bộ thông qua socket daemon Docker (`/var/run/docker.sock`). Mức cách ly của container môi trường cách ly do namespace Docker quyết định.

Để cho môi trường cách ly Docker truy cập GPU trên máy chủ, đặt `agents.defaults.sandbox.docker.gpus` hoặc ghi đè theo từng tác nhân bằng `agents.list[].sandbox.docker.gpus`. Giá trị được truyền vào cờ `--gpus` của Docker dưới dạng đối số riêng, ví dụ `"all"` hoặc `"device=GPU-uuid"`, và yêu cầu runtime máy chủ tương thích như NVIDIA Container Toolkit.

### Phần phụ trợ SSH

Dùng `backend: "ssh"` khi bạn muốn OpenClaw cách ly `exec`, công cụ tệp và đọc phương tiện trên một máy bất kỳ có thể truy cập qua SSH.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "ssh",        scope: "session",        workspaceAccess: "rw",        ssh: {          target: "user@gateway-host:22",          workspaceRoot: "/tmp/openclaw-sandboxes",          strictHostKeyChecking: true,          updateHostKeys: true,          identityFile: "~/.ssh/id_ed25519",          certificateFile: "~/.ssh/id_ed25519-cert.pub",          knownHostsFile: "~/.ssh/known_hosts",          // Or use SecretRefs / inline contents instead of local files:          // identityData: { source: "env", provider: "default", id: "SSH_IDENTITY" },          // certificateData: { source: "env", provider: "default", id: "SSH_CERTIFICATE" },          // knownHostsData: { source: "env", provider: "default", id: "SSH_KNOWN_HOSTS" },        },      },    },  },}
[/code]

Cách hoạt động

  * OpenClaw tạo một gốc từ xa theo phạm vi dưới `sandbox.ssh.workspaceRoot`.
  * Trong lần dùng đầu tiên sau khi tạo hoặc tạo lại, OpenClaw gieo workspace từ xa đó từ workspace cục bộ một lần.
  * Sau đó, `exec`, `read`, `write`, `edit`, `apply_patch`, đọc phương tiện trong prompt và staging phương tiện đầu vào chạy trực tiếp trên workspace từ xa qua SSH.
  * OpenClaw không tự động đồng bộ các thay đổi từ xa trở lại workspace cục bộ.

Vật liệu xác thực

  * `identityFile`, `certificateFile`, `knownHostsFile`: dùng các tệp cục bộ hiện có và truyền chúng qua cấu hình OpenSSH.
  * `identityData`, `certificateData`, `knownHostsData`: dùng chuỗi inline hoặc SecretRefs. OpenClaw phân giải chúng thông qua snapshot runtime bí mật thông thường, ghi chúng vào tệp tạm với `0600`, rồi xóa chúng khi phiên SSH kết thúc.
  * Nếu cả `*File` và `*Data` được đặt cho cùng một mục, `*Data` thắng trong phiên SSH đó.

Hệ quả của chuẩn từ xa

Đây là mô hình **chuẩn từ xa**. Workspace SSH từ xa trở thành trạng thái môi trường cách ly thực sau bước gieo ban đầu.

  * Các chỉnh sửa cục bộ trên máy chủ được thực hiện bên ngoài OpenClaw sau bước gieo sẽ không hiển thị từ xa cho đến khi bạn tạo lại môi trường cách ly.
  * `openclaw sandbox recreate` xóa gốc từ xa theo phạm vi và gieo lại từ cục bộ trong lần dùng tiếp theo.
  * Môi trường cách ly trình duyệt không được hỗ trợ trên phần phụ trợ SSH.
  * Thiết lập `sandbox.docker.*` không áp dụng cho phần phụ trợ SSH.


### Phần phụ trợ OpenShell

Dùng `backend: "openshell"` khi bạn muốn OpenClaw cách ly công cụ trong một môi trường từ xa do OpenShell quản lý. Để xem hướng dẫn thiết lập đầy đủ, tham chiếu cấu hình và so sánh chế độ workspace, xem [trang OpenShell](</vi/gateway/openshell>) riêng.

OpenShell tái sử dụng cùng lõi truyền tải SSH và cầu nối hệ thống tệp từ xa như phần phụ trợ SSH chung, đồng thời thêm vòng đời riêng của OpenShell (`sandbox create/get/delete`, `sandbox ssh-config`) cùng chế độ workspace `mirror` tùy chọn.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "openshell",        scope: "session",        workspaceAccess: "rw",      },    },  },  plugins: {    entries: {      openshell: {        enabled: true,        config: {          from: "openclaw",          mode: "remote", // mirror | remote          remoteWorkspaceDir: "/sandbox",          remoteAgentWorkspaceDir: "/agent",        },      },    },  },}
[/code]

Chế độ OpenShell:

  * `mirror` (mặc định): workspace cục bộ vẫn là chuẩn. OpenClaw đồng bộ tệp cục bộ vào OpenShell trước khi exec và đồng bộ workspace từ xa trở lại sau khi exec.
  * `remote`: workspace OpenShell là chuẩn sau khi môi trường cách ly được tạo. OpenClaw gieo workspace từ xa một lần từ workspace cục bộ, sau đó công cụ tệp và exec chạy trực tiếp trên môi trường cách ly từ xa mà không đồng bộ thay đổi trở lại.


Chi tiết truyền tải từ xa

  * OpenClaw yêu cầu OpenShell cung cấp cấu hình SSH riêng cho môi trường cách ly qua `openshell sandbox ssh-config <name>`.
  * Core ghi cấu hình SSH đó vào tệp tạm, mở phiên SSH và tái sử dụng cùng cầu nối hệ thống tệp từ xa dùng bởi `backend: "ssh"`.
  * Chỉ trong chế độ `mirror`, vòng đời mới khác: đồng bộ cục bộ sang từ xa trước khi exec, rồi đồng bộ trở lại sau khi exec.

Giới hạn hiện tại của OpenShell

  * môi trường cách ly trình duyệt chưa được hỗ trợ
  * `sandbox.docker.binds` không được hỗ trợ trên phần phụ trợ OpenShell
  * các núm runtime riêng của Docker dưới `sandbox.docker.*` vẫn chỉ áp dụng cho phần phụ trợ Docker


#### Chế độ workspace

OpenShell có hai mô hình workspace. Đây là phần quan trọng nhất trong thực tế.

### mirror (cục bộ là chuẩn)

Dùng `plugins.entries.openshell.config.mode: "mirror"` khi bạn muốn **workspace cục bộ vẫn là chuẩn**.

Hành vi:

  * Trước `exec`, OpenClaw đồng bộ workspace cục bộ vào sandbox OpenShell.
  * Sau `exec`, OpenClaw đồng bộ workspace từ xa trở lại workspace cục bộ.
  * Các công cụ tệp vẫn hoạt động qua cầu nối sandbox, nhưng workspace cục bộ vẫn là nguồn sự thật giữa các lượt.


Dùng chế độ này khi:

  * bạn chỉnh sửa tệp cục bộ bên ngoài OpenClaw và muốn các thay đổi đó tự động xuất hiện trong sandbox
  * bạn muốn sandbox OpenShell hoạt động giống backend Docker nhất có thể
  * bạn muốn workspace máy chủ phản ánh các lần ghi trong sandbox sau mỗi lượt exec


Đánh đổi: thêm chi phí đồng bộ trước và sau exec.

### remote (OpenShell canonical)

Dùng `plugins.entries.openshell.config.mode: "remote"` khi bạn muốn **workspace OpenShell trở thành chuẩn chính**.

Hành vi:

  * Khi sandbox được tạo lần đầu, OpenClaw khởi tạo workspace từ xa từ workspace cục bộ một lần.
  * Sau đó, `exec`, `read`, `write`, `edit`, và `apply_patch` hoạt động trực tiếp trên workspace OpenShell từ xa.
  * OpenClaw **không** đồng bộ các thay đổi từ xa trở lại workspace cục bộ sau exec.
  * Các lần đọc media tại thời điểm tạo prompt vẫn hoạt động vì công cụ tệp và media đọc qua cầu nối sandbox thay vì giả định một đường dẫn máy chủ cục bộ.
  * Transport là SSH vào sandbox OpenShell do `openshell sandbox ssh-config` trả về.


Hệ quả quan trọng:

  * Nếu bạn chỉnh sửa tệp trên máy chủ bên ngoài OpenClaw sau bước khởi tạo, sandbox từ xa sẽ **không** tự động thấy các thay đổi đó.
  * Nếu sandbox được tạo lại, workspace từ xa được khởi tạo lại từ workspace cục bộ.
  * Với `scope: "agent"` hoặc `scope: "shared"`, workspace từ xa đó được chia sẻ trong cùng phạm vi đó.


Dùng chế độ này khi:

  * sandbox nên chủ yếu nằm ở phía OpenShell từ xa
  * bạn muốn giảm chi phí đồng bộ mỗi lượt
  * bạn không muốn các chỉnh sửa cục bộ trên máy chủ âm thầm ghi đè trạng thái sandbox từ xa


Chọn `mirror` nếu bạn xem sandbox là môi trường thực thi tạm thời. Chọn `remote` nếu bạn xem sandbox là workspace thật.

#### Vòng đời OpenShell

Sandbox OpenShell vẫn được quản lý thông qua vòng đời sandbox thông thường:

  * `openclaw sandbox list` hiển thị runtime OpenShell cũng như runtime Docker
  * `openclaw sandbox recreate` xóa runtime hiện tại và để OpenClaw tạo lại nó trong lần dùng tiếp theo
  * logic dọn dẹp cũng nhận biết backend


Với chế độ `remote`, việc tạo lại đặc biệt quan trọng:

  * tạo lại sẽ xóa workspace từ xa chuẩn chính cho phạm vi đó
  * lần dùng tiếp theo khởi tạo một workspace từ xa mới từ workspace cục bộ


Với chế độ `mirror`, việc tạo lại chủ yếu đặt lại môi trường thực thi từ xa vì dù sao workspace cục bộ vẫn là chuẩn chính.

## Truy cập workspace

`agents.defaults.sandbox.workspaceAccess` kiểm soát **sandbox có thể thấy gì** :

### none (default)

Công cụ thấy một workspace sandbox dưới `~/.openclaw/sandboxes`.

### ro

Gắn workspace của agent ở chế độ chỉ đọc tại `/agent` (vô hiệu hóa `write`/`edit`/`apply_patch`).

### rw

Gắn workspace của agent ở chế độ đọc/ghi tại `/workspace`.

Với backend OpenShell:

  * chế độ `mirror` vẫn dùng workspace cục bộ làm nguồn chuẩn chính giữa các lượt exec
  * chế độ `remote` dùng workspace OpenShell từ xa làm nguồn chuẩn chính sau lần khởi tạo ban đầu
  * `workspaceAccess: "ro"` và `"none"` vẫn hạn chế hành vi ghi theo cùng cách


Media đến được sao chép vào workspace sandbox đang hoạt động (`media/inbound/*`).

## Mount bind tùy chỉnh

`agents.defaults.sandbox.docker.binds` gắn thêm các thư mục máy chủ vào container. Định dạng: `host:container:mode` (ví dụ: `"/home/user/source:/source:rw"`).

Bind toàn cục và theo từng agent được **hợp nhất** (không thay thế). Dưới `scope: "shared"`, bind theo từng agent bị bỏ qua.

`agents.defaults.sandbox.browser.binds` chỉ gắn thêm các thư mục máy chủ vào container **trình duyệt sandbox**.

  * Khi được đặt (bao gồm `[]`), nó thay thế `agents.defaults.sandbox.docker.binds` cho container trình duyệt.
  * Khi bị bỏ qua, container trình duyệt dùng lại `agents.defaults.sandbox.docker.binds` (tương thích ngược).


Ví dụ (nguồn chỉ đọc + một thư mục dữ liệu bổ sung):

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        docker: {          binds: ["/home/user/source:/source:ro", "/var/data/myapp:/data:ro"],        },      },    },    list: [      {        id: "build",        sandbox: {          docker: {            binds: ["/mnt/cache:/cache:rw"],          },        },      },    ],  },}
[/code]

## Image và thiết lập

Image Docker mặc định: `openclaw-sandbox:bookworm-slim`

* ### Build image mặc định

Từ checkout nguồn:

bashCopy code
[code]
    scripts/sandbox-setup.sh
[/code]

Từ bản cài npm (không cần checkout nguồn):

bashCopy code
[code]
    docker build -t openclaw-sandbox:bookworm-slim - <<'DOCKERFILE'FROM debian:bookworm-slimENV DEBIAN_FRONTEND=noninteractiveRUN apt-get update && apt-get install -y --no-install-recommends \  bash ca-certificates curl git jq python3 ripgrep \  && rm -rf /var/lib/apt/lists/*RUN useradd --create-home --shell /bin/bash sandboxUSER sandboxWORKDIR /home/sandboxCMD ["sleep", "infinity"]DOCKERFILE
[/code]

Image mặc định **không** bao gồm Node. Nếu một skill cần Node (hoặc runtime khác), hãy bake một image tùy chỉnh hoặc cài đặt qua `sandbox.docker.setupCommand` (yêu cầu egress mạng + root ghi được + người dùng root).

OpenClaw không âm thầm thay thế bằng `debian:bookworm-slim` thuần khi thiếu `openclaw-sandbox:bookworm-slim`. Các lần chạy sandbox nhắm đến image mặc định sẽ thất bại nhanh kèm hướng dẫn build cho đến khi bạn build nó, vì image đi kèm chứa `python3` cho các helper ghi/sửa sandbox.

* ### Tùy chọn: build image chung

Để có image sandbox nhiều chức năng hơn với công cụ phổ biến (ví dụ `curl`, `jq`, `nodejs`, `python3`, `git`):

Từ checkout nguồn:

bashCopy code
[code]
    scripts/sandbox-common-setup.sh
[/code]

Từ bản cài npm, trước tiên build image mặc định (xem ở trên), sau đó build image chung ở trên nó bằng [`scripts/docker/sandbox/Dockerfile.common`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.common>) từ kho lưu trữ.

Sau đó đặt `agents.defaults.sandbox.docker.image` thành `openclaw-sandbox-common:bookworm-slim`.

* ### Tùy chọn: build image trình duyệt sandbox

Từ checkout nguồn:

bashCopy code
[code]
    scripts/sandbox-browser-setup.sh
[/code]

Từ bản cài npm, build bằng [`scripts/docker/sandbox/Dockerfile.browser`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.browser>) từ kho lưu trữ.

Theo mặc định, container sandbox Docker chạy với **không có mạng**. Ghi đè bằng `agents.defaults.sandbox.docker.network`.

Mặc định Chromium của trình duyệt sandbox

Image trình duyệt sandbox đi kèm cũng áp dụng các mặc định khởi động Chromium thận trọng cho workload chạy trong container. Các mặc định container hiện tại bao gồm:

  * `--remote-debugging-address=127.0.0.1`
  * `--remote-debugging-port=<derived from OPENCLAW_BROWSER_CDP_PORT>`
  * `--user-data-dir=${HOME}/.chrome`
  * `--no-first-run`
  * `--no-default-browser-check`
  * `--disable-3d-apis`
  * `--disable-gpu`
  * `--disable-dev-shm-usage`
  * `--disable-background-networking`
  * `--disable-extensions`
  * `--disable-features=TranslateUI`
  * `--disable-breakpad`
  * `--disable-crash-reporter`
  * `--disable-software-rasterizer`
  * `--no-zygote`
  * `--metrics-recording-only`
  * `--renderer-process-limit=2`
  * `--no-sandbox` khi `noSandbox` được bật.
  * Ba cờ gia cố đồ họa (`--disable-3d-apis`, `--disable-software-rasterizer`, `--disable-gpu`) là tùy chọn và hữu ích khi container thiếu hỗ trợ GPU. Đặt `OPENCLAW_BROWSER_DISABLE_GRAPHICS_FLAGS=0` nếu workload của bạn cần WebGL hoặc các tính năng 3D/trình duyệt khác.
  * `--disable-extensions` được bật theo mặc định và có thể tắt bằng `OPENCLAW_BROWSER_DISABLE_EXTENSIONS=0` cho các luồng phụ thuộc vào extension.
  * `--renderer-process-limit=2` được kiểm soát bởi `OPENCLAW_BROWSER_RENDERER_PROCESS_LIMIT=&lt;N&gt;`, trong đó `0` giữ mặc định của Chromium.


Nếu bạn cần một hồ sơ runtime khác, hãy dùng image trình duyệt tùy chỉnh và cung cấp entrypoint riêng. Với hồ sơ Chromium cục bộ (không container), dùng `browser.extraArgs` để nối thêm các cờ khởi động.

Mặc định bảo mật mạng

  * `network: "host"` bị chặn.
  * `network: "container:<id>"` bị chặn theo mặc định (rủi ro bỏ qua bằng cách join namespace).
  * Ghi đè khẩn cấp: `agents.defaults.sandbox.docker.dangerouslyAllowContainerNamespaceJoin: true`.


Các bản cài Docker và Gateway chạy trong container nằm tại đây: [Docker](</vi/install/docker>)

Với triển khai Gateway Docker, `scripts/docker/setup.sh` có thể bootstrap cấu hình sandbox. Đặt `OPENCLAW_SANDBOX=1` (hoặc `true`/`yes`/`on`) để bật đường dẫn đó. Bạn có thể ghi đè vị trí socket bằng `OPENCLAW_DOCKER_SOCKET`. Thiết lập đầy đủ và tham chiếu env: [Docker](</vi/install/docker#agent-sandbox>).

## setupCommand (thiết lập container một lần)

`setupCommand` chạy **một lần** sau khi container sandbox được tạo (không phải mỗi lần chạy). Nó thực thi bên trong container qua `sh -lc`.

Đường dẫn:

  * Toàn cục: `agents.defaults.sandbox.docker.setupCommand`
  * Theo từng agent: `agents.list[].sandbox.docker.setupCommand`


Common pitfalls

  * `docker.network` mặc định là `"none"` (không có lưu lượng ra ngoài), nên việc cài đặt gói sẽ thất bại.
  * `docker.network: "container:<id>"` yêu cầu `dangerouslyAllowContainerNamespaceJoin: true` và chỉ dùng trong trường hợp khẩn cấp.
  * `readOnlyRoot: true` ngăn việc ghi; đặt `readOnlyRoot: false` hoặc tạo sẵn một image tùy chỉnh.
  * `user` phải là root để cài đặt gói (bỏ qua `user` hoặc đặt `user: "0:0"`).
  * Lệnh thực thi trong môi trường cô lập **không** kế thừa `process.env` của máy chủ. Dùng `agents.defaults.sandbox.docker.env` (hoặc một image tùy chỉnh) cho khóa API của skill.


## Chính sách công cụ và lối thoát

Chính sách cho phép/từ chối công cụ vẫn được áp dụng trước các quy tắc môi trường cô lập. Nếu một công cụ bị từ chối trên toàn cục hoặc theo từng agent, môi trường cô lập sẽ không khôi phục công cụ đó.

`tools.elevated` là một lối thoát rõ ràng chạy `exec` bên ngoài môi trường cô lập (`gateway` theo mặc định, hoặc `node` khi mục tiêu thực thi là `node`). Chỉ thị `/exec` chỉ áp dụng cho người gửi được ủy quyền và được duy trì theo từng phiên; để vô hiệu hóa cứng `exec`, hãy dùng chính sách từ chối công cụ (xem [Môi trường cô lập so với Chính sách công cụ so với Quyền nâng cao](</vi/gateway/sandbox-vs-tool-policy-vs-elevated>)).

Gỡ lỗi:

  * Dùng `openclaw sandbox explain` để kiểm tra chế độ môi trường cô lập hiệu lực, chính sách công cụ và các khóa cấu hình khắc phục.
  * Xem [Môi trường cô lập so với Chính sách công cụ so với Quyền nâng cao](</vi/gateway/sandbox-vs-tool-policy-vs-elevated>) để hiểu mô hình tư duy "tại sao điều này bị chặn?".


Giữ chặt cấu hình bảo vệ.

## Ghi đè đa agent

Mỗi agent có thể ghi đè môi trường cô lập + công cụ: `agents.list[].sandbox` và `agents.list[].tools` (cộng với `agents.list[].tools.sandbox.tools` cho chính sách công cụ trong môi trường cô lập). Xem [Môi trường cô lập & Công cụ đa agent](</vi/tools/multi-agent-sandbox-tools>) để biết thứ tự ưu tiên.

## Ví dụ bật tối thiểu

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",        scope: "session",        workspaceAccess: "none",      },    },  },}
[/code]

## Liên quan

  * [Môi trường cô lập & Công cụ đa agent](</vi/tools/multi-agent-sandbox-tools>) — ghi đè theo từng agent và thứ tự ưu tiên
  * [OpenShell](</vi/gateway/openshell>) — thiết lập backend môi trường cô lập được quản lý, chế độ workspace và tham chiếu cấu hình
  * [Cấu hình môi trường cô lập](</vi/gateway/config-agents#agentsdefaultssandbox>)
  * [Môi trường cô lập so với Chính sách công cụ so với Quyền nâng cao](</vi/gateway/sandbox-vs-tool-policy-vs-elevated>) — gỡ lỗi "tại sao điều này bị chặn?"
  * [Bảo mật](</vi/gateway/security>)


Was this useful?YesNo