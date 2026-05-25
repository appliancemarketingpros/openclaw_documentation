---
title: Azure
source_url: https://docs.openclaw.ai/vi/install/azure
scraped_at: 2026-05-25
---

Hướng dẫn này thiết lập một máy ảo Azure Linux bằng Azure CLI, áp dụng gia cố Network Security Group (NSG), cấu hình Azure Bastion để truy cập SSH, và cài đặt OpenClaw.

## Bạn sẽ thực hiện

  * Tạo tài nguyên mạng Azure (VNet, subnet, NSG) và tài nguyên điện toán bằng Azure CLI
  * Áp dụng quy tắc Network Security Group để SSH vào máy ảo chỉ được phép từ Azure Bastion
  * Sử dụng Azure Bastion để truy cập SSH (không có IP công khai trên máy ảo)
  * Cài đặt OpenClaw bằng script cài đặt
  * Xác minh Gateway


## Bạn cần có

  * Một gói đăng ký Azure có quyền tạo tài nguyên điện toán và mạng
  * Đã cài đặt Azure CLI (xem [các bước cài đặt Azure CLI](<https://learn.microsoft.com/cli/azure/install-azure-cli>) nếu cần)
  * Một cặp khóa SSH (hướng dẫn này có bao gồm cách tạo nếu cần)
  * ~20-30 phút


## Cấu hình triển khai

* ### Đăng nhập vào Azure CLI

bashCopy code
[code]
    az loginaz extension add -n ssh
[/code]

Phần mở rộng `ssh` là bắt buộc để tạo đường hầm SSH gốc qua Azure Bastion.

* ### Đăng ký các nhà cung cấp tài nguyên bắt buộc (một lần)

bashCopy code
[code]
    az provider register --namespace Microsoft.Computeaz provider register --namespace Microsoft.Network
[/code]

Xác minh đăng ký. Chờ cho đến khi cả hai đều hiển thị `Registered`.

bashCopy code
[code]
    az provider show --namespace Microsoft.Compute --query registrationState -o tsvaz provider show --namespace Microsoft.Network --query registrationState -o tsv
[/code]

* ### Thiết lập biến triển khai

bashCopy code
[code]
    RG="rg-openclaw"LOCATION="westus2"VNET_NAME="vnet-openclaw"VNET_PREFIX="10.40.0.0/16"VM_SUBNET_NAME="snet-openclaw-vm"VM_SUBNET_PREFIX="10.40.2.0/24"BASTION_SUBNET_PREFIX="10.40.1.0/26"NSG_NAME="nsg-openclaw-vm"VM_NAME="vm-openclaw"ADMIN_USERNAME="openclaw"BASTION_NAME="bas-openclaw"BASTION_PIP_NAME="pip-openclaw-bastion"
[/code]

Điều chỉnh tên và dải CIDR cho phù hợp với môi trường của bạn. Subnet Bastion phải có kích thước ít nhất là `/26`.

* ### Chọn khóa SSH

Sử dụng khóa công khai hiện có nếu bạn đã có:

bashCopy code
[code]
    SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

Nếu bạn chưa có khóa SSH, hãy tạo một khóa:

bashCopy code
[code]
    ssh-keygen -t ed25519 -a 100 -f ~/.ssh/id_ed25519 -C "you@example.com"SSH_PUB_KEY="$(cat ~/.ssh/id_ed25519.pub)"
[/code]

* ### Chọn kích thước máy ảo và kích thước đĩa hệ điều hành

bashCopy code
[code]
    VM_SIZE="Standard_B2as_v2"OS_DISK_SIZE_GB=64
[/code]

Chọn kích thước máy ảo và kích thước đĩa hệ điều hành có sẵn trong gói đăng ký và khu vực của bạn:

  * Bắt đầu nhỏ hơn cho nhu cầu sử dụng nhẹ và mở rộng sau
  * Dùng thêm vCPU/RAM/đĩa cho tự động hóa nặng hơn, nhiều kênh hơn, hoặc khối lượng công việc mô hình/công cụ lớn hơn
  * Nếu một kích thước máy ảo không có sẵn trong khu vực hoặc hạn ngạch gói đăng ký của bạn, hãy chọn SKU gần nhất có sẵn


Liệt kê các kích thước máy ảo có sẵn trong khu vực đích của bạn:

bashCopy code
[code]
    az vm list-skus --location "${LOCATION}" --resource-type virtualMachines -o table
[/code]

Kiểm tra mức sử dụng/hạn ngạch vCPU và đĩa hiện tại của bạn:

bashCopy code
[code]
    az vm list-usage --location "${LOCATION}" -o table
[/code]

## Triển khai tài nguyên Azure

* ### Tạo nhóm tài nguyên

bashCopy code
[code]
    az group create -n "${RG}" -l "${LOCATION}"
[/code]

* ### Tạo nhóm bảo mật mạng

Tạo NSG và thêm quy tắc để chỉ subnet Bastion có thể SSH vào máy ảo.

bashCopy code
[code]
    az network nsg create \  -g "${RG}" -n "${NSG_NAME}" -l "${LOCATION}" # Allow SSH from the Bastion subnet onlyaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n AllowSshFromBastionSubnet --priority 100 \  --access Allow --direction Inbound --protocol Tcp \  --source-address-prefixes "${BASTION_SUBNET_PREFIX}" \  --destination-port-ranges 22 # Deny SSH from the public internetaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyInternetSsh --priority 110 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes Internet \  --destination-port-ranges 22 # Deny SSH from other VNet sourcesaz network nsg rule create \  -g "${RG}" --nsg-name "${NSG_NAME}" \  -n DenyVnetSsh --priority 120 \  --access Deny --direction Inbound --protocol Tcp \  --source-address-prefixes VirtualNetwork \  --destination-port-ranges 22
[/code]

Các quy tắc được đánh giá theo mức ưu tiên (số nhỏ nhất trước): lưu lượng Bastion được cho phép ở 100, sau đó mọi SSH khác bị chặn ở 110 và 120.

* ### Tạo mạng ảo và các subnet

Tạo VNet với subnet máy ảo (đã gắn NSG), rồi thêm subnet Bastion.

bashCopy code
[code]
    az network vnet create \  -g "${RG}" -n "${VNET_NAME}" -l "${LOCATION}" \  --address-prefixes "${VNET_PREFIX}" \  --subnet-name "${VM_SUBNET_NAME}" \  --subnet-prefixes "${VM_SUBNET_PREFIX}" # Attach the NSG to the VM subnetaz network vnet subnet update \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n "${VM_SUBNET_NAME}" --nsg "${NSG_NAME}" # AzureBastionSubnet — name is required by Azureaz network vnet subnet create \  -g "${RG}" --vnet-name "${VNET_NAME}" \  -n AzureBastionSubnet \  --address-prefixes "${BASTION_SUBNET_PREFIX}"
[/code]

* ### Tạo máy ảo

Máy ảo không có IP công khai. Truy cập SSH chỉ thông qua Azure Bastion.

bashCopy code
[code]
    az vm create \  -g "${RG}" -n "${VM_NAME}" -l "${LOCATION}" \  --image "Canonical:ubuntu-24_04-lts:server:latest" \  --size "${VM_SIZE}" \  --os-disk-size-gb "${OS_DISK_SIZE_GB}" \  --storage-sku StandardSSD_LRS \  --admin-username "${ADMIN_USERNAME}" \  --ssh-key-values "${SSH_PUB_KEY}" \  --vnet-name "${VNET_NAME}" \  --subnet "${VM_SUBNET_NAME}" \  --public-ip-address "" \  --nsg ""
[/code]

`--public-ip-address ""` ngăn việc gán IP công khai. `--nsg ""` bỏ qua việc tạo NSG riêng cho từng NIC (NSG cấp subnet xử lý bảo mật).

**Khả năng tái lập:** Lệnh ở trên dùng `latest` cho image Ubuntu. Để ghim một phiên bản cụ thể, hãy liệt kê các phiên bản có sẵn và thay thế `latest`:

bashCopy code
[code]
    az vm image list \  --publisher Canonical --offer ubuntu-24_04-lts \  --sku server --all -o table
[/code]

* ### Tạo Azure Bastion

Azure Bastion cung cấp quyền truy cập SSH được quản lý vào máy ảo mà không để lộ IP công khai. Cần SKU Standard có hỗ trợ tạo đường hầm để dùng `az network bastion ssh` dựa trên CLI.

bashCopy code
[code]
    az network public-ip create \  -g "${RG}" -n "${BASTION_PIP_NAME}" -l "${LOCATION}" \  --sku Standard --allocation-method Static az network bastion create \  -g "${RG}" -n "${BASTION_NAME}" -l "${LOCATION}" \  --vnet-name "${VNET_NAME}" \  --public-ip-address "${BASTION_PIP_NAME}" \  --sku Standard --enable-tunneling true
[/code]

Việc cấp phát Bastion thường mất 5-10 phút nhưng có thể mất tới 15-30 phút ở một số khu vực.

## Cài đặt OpenClaw

* ### SSH vào máy ảo qua Azure Bastion

bashCopy code
[code]
    VM_ID="$(az vm show -g "${RG}" -n "${VM_NAME}" --query id -o tsv)" az network bastion ssh \  --name "${BASTION_NAME}" \  --resource-group "${RG}" \  --target-resource-id "${VM_ID}" \  --auth-type ssh-key \  --username "${ADMIN_USERNAME}" \  --ssh-key ~/.ssh/id_ed25519
[/code]

* ### Cài đặt OpenClaw (trong shell của máy ảo)

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh -o /tmp/install.shbash /tmp/install.shrm -f /tmp/install.sh
[/code]

Trình cài đặt sẽ cài Node LTS và các phụ thuộc nếu chưa có, cài OpenClaw, và khởi chạy trình hướng dẫn onboarding. Xem [Cài đặt](</vi/install>) để biết chi tiết.

* ### Xác minh Gateway

Sau khi onboarding hoàn tất:

bashCopy code
[code]
    openclaw gateway status
[/code]

Hầu hết các nhóm Azure doanh nghiệp đã có giấy phép GitHub Copilot. Nếu đây là trường hợp của bạn, chúng tôi khuyến nghị chọn nhà cung cấp GitHub Copilot trong trình hướng dẫn onboarding của OpenClaw. Xem [Nhà cung cấp GitHub Copilot](</vi/providers/github-copilot>).

## Cân nhắc chi phí

Azure Bastion SKU Standard chạy khoảng **$140/tháng** và máy ảo (Standard_B2as_v2) chạy khoảng **$55/tháng**.

Để giảm chi phí:

  * **Giải cấp phát máy ảo** khi không sử dụng (dừng tính phí điện toán; phí đĩa vẫn còn). OpenClaw Gateway sẽ không thể truy cập được trong khi máy ảo bị giải cấp phát — hãy khởi động lại khi bạn cần nó hoạt động trực tuyến trở lại:

bashCopy code
[code]az vm deallocate -g "${RG}" -n "${VM_NAME}"az vm start -g "${RG}" -n "${VM_NAME}"   # restart later
[/code]

  * **Xóa Bastion khi không cần** và tạo lại khi bạn cần truy cập SSH. Bastion là thành phần chi phí lớn nhất và chỉ mất vài phút để cấp phát.

  * **Dùng SKU Basic Bastion** (~$38/tháng) nếu bạn chỉ cần SSH dựa trên Portal và không cần tạo đường hầm CLI (`az network bastion ssh`).


## Dọn dẹp

Để xóa tất cả tài nguyên được tạo bởi hướng dẫn này:

bashCopy code
[code]
    az group delete -n "${RG}" --yes --no-wait
[/code]

Lệnh này xóa nhóm tài nguyên và mọi thứ bên trong nó (máy ảo, VNet, NSG, Bastion, IP công khai).

## Các bước tiếp theo

  * Thiết lập các kênh nhắn tin: [Kênh](</vi/channels>)
  * Ghép nối thiết bị cục bộ làm nút: [Nút](</vi/nodes>)
  * Cấu hình Gateway: [Cấu hình Gateway](</vi/gateway/configuration>)
  * Để biết thêm chi tiết về triển khai OpenClaw trên Azure với nhà cung cấp mô hình GitHub Copilot: [OpenClaw trên Azure với GitHub Copilot](<https://github.com/johnsonshi/openclaw-azure-github-copilot>)


## Liên quan

  * [Tổng quan cài đặt](</vi/install>)
  * [GCP](</vi/install/gcp>)
  * [DigitalOcean](</vi/install/digitalocean>)


Was this useful?YesNo