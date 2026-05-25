---
title: Ansible
source_url: https://docs.openclaw.ai/ja-JP/install/ansible
scraped_at: 2026-05-25
---

OpenClaw を本番サーバーへデプロイするには **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** を使用します -- セキュリティファーストのアーキテクチャを備えた自動インストーラーです。

## 前提条件

要件 | 詳細  
---|---  
**OS** | Debian 11+ または Ubuntu 20.04+  
**アクセス** | root または sudo 権限  
**ネットワーク** | パッケージインストール用のインターネット接続  
**Ansible** | 2.14+（クイックスタートスクリプトにより自動インストール）  
  
## 得られるもの

  * **Firewall-first セキュリティ** \-- UFW + Docker 分離（SSH + Tailscale のみアクセス可能）
  * **Tailscale VPN** \-- サービスを公開せずに安全なリモートアクセス
  * **Docker** \-- 分離されたサンドボックスコンテナ、localhost のみのバインディング
  * **多層防御** \-- 4 層のセキュリティアーキテクチャ
  * **Systemd 統合** \-- ハードニング付きで起動時に自動開始
  * **ワンコマンドセットアップ** \-- 数分でデプロイ完了


## クイックスタート

ワンコマンドインストール:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## インストールされるもの

Ansible プレイブックは以下をインストールして設定します:

  1. **Tailscale** \-- 安全なリモートアクセス用のメッシュ VPN
  2. **UFW ファイアウォール** \-- SSH + Tailscale ポートのみ
  3. **Docker CE + Compose V2** \-- デフォルトのエージェントサンドボックスバックエンド用
  4. **Node.js 24 + pnpm** \-- ランタイム依存関係（Node 22 LTS、現在は `22.16+` も引き続きサポート）
  5. **OpenClaw** \-- ホストベースで、コンテナ化されていない
  6. **Systemd サービス** \-- セキュリティハードニング付きで自動開始


## インストール後のセットアップ

* ### openclaw ユーザーに切り替える

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### オンボーディングウィザードを実行する

インストール後スクリプトが、OpenClaw 設定の構成を案内します。

* ### メッセージングプロバイダーを接続する

WhatsApp、Telegram、Discord、または Signal にログインします:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### インストールを確認する

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Tailscale に接続する

安全なリモートアクセスのために VPN メッシュへ参加します。

### クイックコマンド

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## セキュリティアーキテクチャ

このデプロイは 4 層の防御モデルを使用します:

  1. **ファイアウォール（UFW）** \-- SSH（22）+ Tailscale（41641/udp）のみを公開
  2. **VPN（Tailscale）** \-- Gateway は VPN メッシュ経由でのみアクセス可能
  3. **Docker 分離** \-- DOCKER-USER iptables チェーンが外部ポートの公開を防止
  4. **Systemd ハードニング** \-- NoNewPrivileges、PrivateTmp、非特権ユーザー


外部攻撃対象領域を確認するには:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

ポート 22（SSH）のみが開いているはずです。その他すべてのサービス（Gateway、Docker）はロックダウンされています。

Docker はエージェントサンドボックス（分離されたツール実行）のためにインストールされるもので、Gateway 自体を実行するためではありません。サンドボックス設定については [マルチエージェントサンドボックスとツール](</ja-JP/tools/multi-agent-sandbox-tools>) を参照してください。

## 手動インストール

自動化よりも手動制御を優先する場合:

* ### 前提条件をインストールする

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### リポジトリをクローンする

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Ansible コレクションをインストールする

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### プレイブックを実行する

bashCopy code
[code]
    ./run-playbook.sh
[/code]

または、直接実行してから、後でセットアップスクリプトを手動で実行します:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## 更新

Ansible インストーラーは、OpenClaw を手動更新できるようにセットアップします。標準の更新フローについては [更新](</ja-JP/install/updating>) を参照してください。

Ansible プレイブックを再実行するには（たとえば設定変更のため）:

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

これは冪等であり、複数回実行しても安全です。

## トラブルシューティング

ファイアウォールが接続をブロックする

  * まず Tailscale VPN 経由でアクセスできることを確認する
  * SSH アクセス（ポート 22）は常に許可される
  * Gateway は設計上、Tailscale 経由でのみアクセス可能

サービスが起動しない bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Docker サンドボックスの問題 bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

プロバイダーログインに失敗する

`openclaw` ユーザーとして実行していることを確認してください:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## 高度な設定

詳細なセキュリティアーキテクチャとトラブルシューティングについては、openclaw-ansible リポジトリを参照してください:

  * [セキュリティアーキテクチャ](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [技術詳細](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [トラブルシューティングガイド](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## 関連

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- 完全なデプロイガイド
  * [Docker](</ja-JP/install/docker>) \-- コンテナ化された Gateway セットアップ
  * [サンドボックス化](</ja-JP/gateway/sandboxing>) \-- エージェントサンドボックス設定
  * [マルチエージェントサンドボックスとツール](</ja-JP/tools/multi-agent-sandbox-tools>) \-- エージェントごとの分離


Was this useful?YesNo