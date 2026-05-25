---
title: 展示专区
source_url: https://docs.openclaw.ai/zh-CN/start/showcase
scraped_at: 2026-05-25
---

OpenClaw 项目并不是玩具演示。人们正在从他们早已使用的渠道中交付 PR 审查循环、移动应用、家庭自动化、语音系统、开发工具以及重记忆工作流——基于 Telegram、WhatsApp、Discord 和终端的聊天原生构建；无需等待 API 的真实预订、购物和支持自动化；以及与打印机、扫地机器人、摄像头和家庭系统的物理世界集成。

## 视频

如果你想用最短路径从“这是什么？”到“好，我懂了”，请从这里开始。

[**完整设置演练** VelvetShark，28 分钟。安装、新手引导，并端到端完成第一个可运行助手。 ](<https://www.youtube.com/watch?v=SaWSPZoPX34>) [**社区展示集锦** 更快地浏览围绕 OpenClaw 构建的真实项目、界面和工作流。 ](<https://www.youtube.com/watch?v=mMSKQvlmFuQ>) [**真实世界中的项目** 来自社区的示例，从聊天原生编码循环到硬件和个人自动化。 ](<https://www.youtube.com/watch?v=5kkIJNUGFho>)

## Discord 新鲜内容

近期在编码、开发工具、移动端和聊天原生产品构建方面的亮点。

[**从 PR 审查到 Telegram 反馈** **@bangnokia** • `review` `github` `telegram` OpenCode 完成更改并创建 PR，OpenClaw 审查 Diff，并在 Telegram 中回复建议以及清晰的合并结论。 ![在 Telegram 中交付的 OpenClaw PR 审查反馈](/assets/showcase/pr-review-telegram.jpg) ](<https://x.com/i/status/2010878524543131691>) [**几分钟内构建葡萄酒酒窖 Skill** **@prades_maxime** • `skills` `local` `csv` 向 “Robby” (@openclaw) 请求一个本地葡萄酒酒窖 skill。它会请求一份示例 CSV 导出和一个存储路径，然后构建并测试这个 skill（示例中有 962 瓶酒）。 ![OpenClaw 从 CSV 构建本地葡萄酒酒窖 skill](/assets/showcase/wine-cellar-skill.jpg) ](<https://x.com/i/status/2010916352454791216>) [**Tesco 购物自动驾驶** **@marchattonhere** • `automation` `browser` `shopping` 每周餐食计划、常购商品、预订配送时段、确认订单。无需 API，只用浏览器控制。 ![通过聊天进行 Tesco 购物自动化](/assets/showcase/tesco-shop.jpg) ](<https://x.com/i/status/2009724862470689131>) [**SNAG 截图转 Markdown** **@am-will** • `devtools` `screenshots` `markdown` 快捷键选取屏幕区域，Gemini vision，即时将 Markdown 放入你的剪贴板。 ![SNAG 截图转 Markdown 工具](/assets/showcase/snag.png) ](<https://github.com/am-will/snag>) [**Agents UI** **@kitze** • `ui` `skills` `sync` 用于在 Agents、Claude、Codex 和 OpenClaw 之间管理 skills 和命令的桌面应用。 ![Agents UI 应用](/assets/showcase/agents-ui.jpg) ](<https://releaseflow.net/kitze/agents-ui>) [**Telegram 语音消息（papla.media）** **Community** • `voice` `tts` `telegram` 封装 papla.media TTS，并将结果作为 Telegram 语音消息发送（不会有烦人的自动播放）。 ![来自 TTS 的 Telegram 语音消息输出](/assets/showcase/papla-tts.jpg) ](<https://papla.media/docs>) [**CodexMonitor** **@odrobnik** • `devtools` `codex` `brew` 通过 Homebrew 安装的辅助工具，用于列出、检查和监视本地 OpenAI Codex 会话（CLI + VS Code）。 ![ClawHub 上的 CodexMonitor](/assets/showcase/codexmonitor.png) ](<https://clawhub.ai/odrobnik/codexmonitor>) [**Bambu 3D 打印机控制** **@tobiasbischoff** • `hardware` `3d-printing` `skill` 控制并排查 BambuLab 打印机：状态、任务、摄像头、AMS、校准等。 ![ClawHub 上的 Bambu CLI skill](/assets/showcase/bambu-cli.png) ](<https://clawhub.ai/tobiasbischoff/bambu-cli>) [**维也纳交通（Wiener Linien）** **@hjanuschka** • `travel` `transport` `skill` 提供维也纳公共交通的实时发车信息、中断、电梯状态和路线规划。 ![Wiener Linien skill](/assets/showcase/wienerlinien.png) ](<https://clawhub.ai/hjanuschka/wienerlinien>) **ParentPay 学校餐食** **@George5562** • `automation` `browser` `parenting` 通过 ParentPay 自动预订英国学校餐食。使用鼠标坐标可靠点击表格单元格。 [**R2 上传（Send Me My Files）** **@julianengel** • `files` `r2` `presigned-urls` 上传到 Cloudflare R2/S3，并生成安全的预签名下载链接。对远程 OpenClaw 实例很有用。 ](<https://clawhub.ai/skills/r2-upload>) **通过 Telegram 构建 iOS 应用** **@coard** • `ios` `xcode` `testflight` 完全通过 Telegram 聊天构建了一个带地图和语音录制的完整 iOS 应用，并部署到 TestFlight。 ![TestFlight 上的 iOS 应用](/assets/showcase/ios-testflight.jpg) **Oura Ring 健康助手** **@AS** • `health` `oura` `calendar` 个人 AI 健康助手，将 Oura ring 数据与日历、预约和健身计划集成。 ![Oura ring 健康助手](/assets/showcase/oura-health.png) [**Kev's Dream Team（14+ 个智能体）** **@adam91holt** • `multi-agent` `orchestration` 一个 Gateway 网关下的 14+ 个智能体，由 Opus 4.5 编排器委派给 Codex worker。参见[技术说明](<https://github.com/adam91holt/orchestrated-ai-articles>)和用于智能体沙箱隔离的 [Clawdspace](<https://github.com/adam91holt/clawdspace>)。 ](<https://github.com/adam91holt/orchestrated-ai-articles>) [**Linear CLI** **@NessZerra** • `devtools` `linear` `cli` 用于 Linear 的 CLI，可与智能体工作流（Claude Code、OpenClaw）集成。在终端中管理 issue、项目和工作流。 ](<https://github.com/Finesssee/linear-cli>) [**Beeper CLI** **@jules** • `messaging` `beeper` `cli` 通过 Beeper Desktop 读取、发送和归档消息。使用 Beeper 本地 MCP API，因此智能体可以在一个地方管理你的所有聊天（iMessage、WhatsApp 等）。 ](<https://github.com/blqke/beepcli>)

## 自动化与工作流

调度、浏览器控制、支持循环，以及“直接帮我把任务做完”的产品侧能力。

[**Winix 空气净化器控制** **@antonplex** • `automation` `hardware` `air-quality` Claude Code 发现并确认了净化器控制方式，然后 OpenClaw 接手管理房间空气质量。 ![通过 OpenClaw 控制 Winix 空气净化器](/assets/showcase/winix-air-purifier.jpg) ](<https://x.com/antonplex/status/2010518442471006253>) [**漂亮天空相机抓拍** **@signalgaining** • `automation` `camera` `skill` 由屋顶摄像头触发：当天空看起来很漂亮时，请 OpenClaw 拍一张天空照片。它设计了一个 skill 并完成了拍摄。 ![由 OpenClaw 拍摄的屋顶摄像头天空快照](/assets/showcase/roof-camera-sky.jpg) ](<https://x.com/signalgaining/status/2010523120604746151>) [**晨间简报视觉场景** **@buddyhadry** • `automation` `briefing` `telegram` 通过定时提示，每天早晨由一个 OpenClaw persona 生成一张场景图像（天气、任务、日期、喜爱的帖子或引语）。 ](<https://x.com/buddyhadry/status/2010005331925954739>) [**Padel 球场预订** **@joshp123** • `automation` `booking` `cli` Playtomic 可用时段检查器加预订 CLI。再也不会错过空闲球场。 ![padel-cli 截图](/assets/showcase/padel-screenshot.jpg) ](<https://github.com/joshp123/padel-cli>) **会计资料收集** **Community** • `automation` `email` `pdf` 从电子邮件中收集 PDF，并为税务顾问准备文档。每月会计流程自动驾驶。 [**沙发土豆开发模式** **@davekiss** • `telegram` `migration` `astro` 一边看 Netflix，一边通过 Telegram 重建整个个人网站——从 Notion 到 Astro，迁移了 18 篇文章，DNS 切到 Cloudflare。全程没打开笔记本电脑。 ](<https://davekiss.com>) **求职智能体** **@attol8** • `automation` `api` `skill` 搜索职位列表，与简历关键词匹配，并返回附带链接的相关机会。使用 JSearch API，在 30 分钟内构建完成。 [**Jira skill 构建器** **@jdrhyne** • `jira` `skill` `devtools` OpenClaw 连接到 Jira，然后即时生成了一个新的 skill（当时它甚至还不存在于 ClawHub 中）。 ](<https://x.com/jdrhyne/status/2008336434827002232>) [**通过 Telegram 使用 Todoist skill** **@iamsubhrajyoti** • `todoist` `skill` `telegram` 实现 Todoist 任务自动化，并让 OpenClaw 直接在 Telegram 聊天中生成该 skill。 ](<https://x.com/iamsubhrajyoti/status/2009949389884920153>) **TradingView 分析** **@bheem1798** • `finance` `browser` `automation` 通过浏览器自动化登录 TradingView、截取图表，并按需执行技术分析。无需 API——只要浏览器控制即可。 **Slack 自动支持** **@henrymascot** • `slack` `automation` `support` 监视公司的 Slack 渠道，提供有帮助的回复，并将通知转发到 Telegram。甚至在无人要求的情况下，自主修复了已部署应用中的一个生产 bug。

## 知识与记忆

用于索引、搜索、记忆并对个人或团队知识进行推理的系统。

[**xuezh 中文学习** **@joshp123** • `learning` `voice` `skill` 通过 OpenClaw 提供发音反馈和学习流程的中文学习引擎。 ![xuezh 发音反馈](/assets/showcase/xuezh-pronunciation.jpeg) ](<https://github.com/joshp123/xuezh>) **WhatsApp 记忆金库** **Community** • `memory` `transcription` `indexing` 导入完整 WhatsApp 导出，转写 1k+ 条语音消息，与 git 日志交叉核对，并输出带链接的 Markdown 报告。 [**Karakeep 语义搜索** **@jamesbrooksco** • `search` `vector` `bookmarks` 使用 Qdrant 加 OpenAI 或 Ollama embeddings，为 Karakeep 书签增加向量搜索。 ](<https://github.com/jamesbrooksco/karakeep-semantic-search>) **《头脑特工队 2》式记忆** **Community** • `memory` `beliefs` `self-model` 一个独立的记忆管理器，将会话文件转化为记忆，再转化为信念，最终形成不断演化的自我模型。

## 语音与电话

以语音为先的入口、电话桥接，以及以转写为核心的工作流。

[**Clawdia 电话桥接** **@alejandroOPI** • `voice` `vapi` `bridge` 从 Vapi 语音助手到 OpenClaw HTTP 的桥接。让你与智能体进行接近实时的电话通话。 ](<https://github.com/alejandroOPI/clawdia-bridge>) [**OpenRouter 转写** **@obviyus** • `transcription` `multilingual` `skill` 通过 OpenRouter 进行多语言音频转写（Gemini 等）。可在 ClawHub 上获取。 ](<https://clawhub.ai/obviyus/openrouter-transcribe>)

## 基础设施与部署

让 OpenClaw 更易于运行和扩展的打包、部署与集成。

[**Home Assistant 插件** **@ngutman** • `homeassistant` `docker` `raspberry-pi` 运行在 Home Assistant OS 上的 OpenClaw gateway，支持 SSH 隧道和持久化状态。 ](<https://github.com/ngutman/openclaw-ha-addon>) [**Home Assistant skill** **ClawHub** • `homeassistant` `skill` `automation` 通过自然语言控制和自动化 Home Assistant 设备。 ](<https://clawhub.ai/skills/homeassistant>) [**Nix 打包** **@openclaw** • `nix` `packaging` `deployment` 开箱即用的 nix 化 OpenClaw 配置，用于可复现部署。 ](<https://github.com/openclaw/nix-openclaw>) [**CalDAV 日历** **ClawHub** • `calendar` `caldav` `skill` 使用 khal 和 vdirsyncer 的日历 skill。自托管日历集成。 ](<https://clawhub.ai/skills/caldav-calendar>)

## 家庭与硬件

OpenClaw 面向物理世界的一面：家庭、传感器、摄像头、扫地机器人及其他设备。

[**GoHome 自动化** **@joshp123** • `home` `nix` `grafana` 以 Nix 原生方式实现家庭自动化，并以 OpenClaw 作为交互界面，同时提供 Grafana 仪表板。 ![GoHome Grafana 仪表板](/assets/showcase/gohome-grafana.png) ](<https://github.com/joshp123/gohome>) [**Roborock 扫地机器人** **@joshp123** • `vacuum` `iot` `plugin` 通过自然对话控制你的 Roborock 扫地机器人。 ![Roborock 状态](/assets/showcase/roborock-screenshot.jpg) ](<https://github.com/joshp123/gohome/tree/main/plugins/roborock>)

## 社区项目

那些已经超越单一工作流，成长为更广泛产品或生态的项目。

[**StarSwap 市场** **Community** • `marketplace` `astronomy` `webapp` 完整的天文器材交易市场。基于 OpenClaw 生态并围绕其构建。 ](<https://star-swap.com/>)

## 提交你的项目

* ### 分享它

在 [Discord 的 #self-promotion](<https://discord.gg/clawd>) 中发帖，或 [在 X 上提及 @openclaw](<https://x.com/openclaw>)。

* ### 附上细节

告诉我们它是做什么的，附上仓库或演示链接，如果有截图也请一并分享。

* ### 获得展示

我们会将突出的项目加入本页面。

## 相关内容

  * [入门指南](</zh-CN/start/getting-started>)
  * [OpenClaw](</zh-CN/start/openclaw>)


Was this useful?YesNo