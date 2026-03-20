---
title: Node.js
source_url: https://docs.openclaw.ai/install/node
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Install overview

Node.js

# 

​

Node.js

OpenClaw requires **Node 22.16 or newer**. **Node 24 is the default and recommended runtime** for installs, CI, and release workflows. Node 22 remains supported via the active LTS line. The [installer script](</install#alternative-install-methods>) will detect and install Node automatically — this page is for when you want to set up Node yourself and make sure everything is wired up correctly (versions, PATH, global installs).

## 

​

Check your version

Copy
[code]
    node -v
    
[/code]

If this prints `v24.x.x` or higher, you’re on the recommended default. If it prints `v22.16.x` or higher, you’re on the supported Node 22 LTS path, but we still recommend upgrading to Node 24 when convenient. If Node isn’t installed or the version is too old, pick an install method below.

## 

​

Install Node

  * macOS

  * Linux

  * Windows


**Homebrew** (recommended):

Copy
[code]
    brew install node
    
[/code]

Or download the macOS installer from [nodejs.org](<https://nodejs.org/>).

**Ubuntu / Debian:**

Copy
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -
    sudo apt-get install -y nodejs
    
[/code]

**Fedora / RHEL:**

Copy
[code]
    sudo dnf install nodejs
    
[/code]

Or use a version manager (see below).

**winget** (recommended):

Copy
[code]
    winget install OpenJS.NodeJS.LTS
    
[/code]

**Chocolatey:**

Copy
[code]
    choco install nodejs-lts
    
[/code]

Or download the Windows installer from [nodejs.org](<https://nodejs.org/>).

Using a version manager (nvm, fnm, mise, asdf)

Version managers let you switch between Node versions easily. Popular options:

  * [**fnm**](<https://github.com/Schniz/fnm>) — fast, cross-platform
  * [**nvm**](<https://github.com/nvm-sh/nvm>) — widely used on macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) — polyglot (Node, Python, Ruby, etc.)

Example with fnm:

Copy
[code]
    fnm install 24
    fnm use 24
    
[/code]

Make sure your version manager is initialized in your shell startup file (`~/.zshrc` or `~/.bashrc`). If it isn’t, `openclaw` may not be found in new terminal sessions because the PATH won’t include Node’s bin directory.

## 

​

Troubleshooting

### 

​

`openclaw: command not found`

This almost always means npm’s global bin directory isn’t on your PATH.

1

Find your global npm prefix

Copy
[code]
    npm prefix -g
    
[/code]

2

Check if it's on your PATH

Copy
[code]
    echo "$PATH"
    
[/code]

Look for `<npm-prefix>/bin` (macOS/Linux) or `<npm-prefix>` (Windows) in the output.

3

Add it to your shell startup file

  * macOS / Linux

  * Windows


Add to `~/.zshrc` or `~/.bashrc`:

Copy
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
    
[/code]

Then open a new terminal (or run `rehash` in zsh / `hash -r` in bash).

Add the output of `npm prefix -g` to your system PATH via Settings → System → Environment Variables.

### 

​

Permission errors on `npm install -g` (Linux)

If you see `EACCES` errors, switch npm’s global prefix to a user-writable directory:

Copy
[code]
    mkdir -p "$HOME/.npm-global"
    npm config set prefix "$HOME/.npm-global"
    export PATH="$HOME/.npm-global/bin:$PATH"
    
[/code]

Add the `export PATH=...` line to your `~/.bashrc` or `~/.zshrc` to make it permanent.

[Installer Internals](</install/installer>)[Ansible](</install/ansible>)

⌘I