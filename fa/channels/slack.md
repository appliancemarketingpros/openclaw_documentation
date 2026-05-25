---
title: Slack
source_url: https://docs.openclaw.ai/fa/channels/slack
scraped_at: 2026-05-25
---

آمادهٔ استفاده در محیط تولید برای پیام‌های خصوصی و کانال‌ها از طریق یکپارچه‌سازی‌های برنامهٔ Slack. حالت پیش‌فرض Socket Mode است؛ URLهای درخواست HTTP نیز پشتیبانی می‌شوند.

[**Pairing** پیام‌های خصوصی Slack به‌طور پیش‌فرض روی حالت جفت‌سازی هستند. ](</fa/channels/pairing>) [**Slash commands** رفتار فرمان بومی و کاتالوگ فرمان‌ها. ](</fa/tools/slash-commands>) [**Channel troubleshooting** عیب‌یابی میان‌کانالی و راهنماهای تعمیر. ](</fa/channels/troubleshooting>)

## انتخاب Socket Mode یا URLهای درخواست HTTP

هر دو انتقال برای تولید آماده‌اند و برای پیام‌رسانی، فرمان‌های اسلش، App Home و تعامل‌پذیری به برابری قابلیت می‌رسند. انتخاب را بر اساس شکل استقرار انجام دهید، نه قابلیت‌ها.

دغدغه | Socket Mode (پیش‌فرض) | URLهای درخواست HTTP  
---|---|---  
URL عمومی Gateway | لازم نیست | لازم است (DNS، TLS، پراکسی معکوس یا تونل)  
شبکهٔ خروجی | WSS خروجی به `wss-primary.slack.com` باید قابل دسترسی باشد | بدون WS خروجی؛ فقط HTTPS ورودی  
توکن‌های لازم | توکن بات (`xoxb-...`) + توکن سطح برنامه (`xapp-...`) با `connections:write` | توکن بات (`xoxb-...`) + Signing Secret  
لپ‌تاپ توسعه / پشت فایروال | بدون تغییر کار می‌کند | به یک تونل عمومی (ngrok، Cloudflare Tunnel، Tailscale Funnel) یا Gateway مرحله‌بندی نیاز دارد  
مقیاس‌پذیری افقی | یک نشست Socket Mode برای هر برنامه در هر میزبان؛ چند Gateway به برنامه‌های Slack جداگانه نیاز دارند | هندلر POST بدون حالت؛ چند رپلیکای Gateway می‌توانند پشت یک load balancer از یک برنامه مشترک استفاده کنند  
چند حساب روی یک Gateway | پشتیبانی می‌شود؛ هر حساب WS خودش را باز می‌کند | پشتیبانی می‌شود؛ هر حساب به یک `webhookPath` یکتا نیاز دارد (پیش‌فرض `/slack/events`) تا ثبت‌ها تداخل نکنند  
انتقال فرمان اسلش | از طریق اتصال WS تحویل داده می‌شود؛ `slash_commands[].url` نادیده گرفته می‌شود | Slack به `slash_commands[].url` درخواست POST می‌فرستد؛ این فیلد برای ارسال فرمان لازم است  
امضای درخواست | استفاده نمی‌شود (احراز هویت با توکن سطح برنامه است) | Slack هر درخواست را امضا می‌کند؛ OpenClaw با `signingSecret` آن را بررسی می‌کند  
بازیابی پس از قطع اتصال | SDK Slack به‌طور خودکار دوباره وصل می‌شود؛ تنظیم حمل‌ونقل pong-timeout در Gateway اعمال می‌شود | اتصال پایدار برای قطع شدن وجود ندارد؛ تلاش‌های مجدد برای هر درخواست از سمت Slack انجام می‌شوند  
  
## راه‌اندازی سریع

### Socket Mode (default)

* ### Create a new Slack app

[api.slack.com/apps](<https://api.slack.com/apps/new>) را باز کنید → **Create New App** → **From a manifest** → فضای کاری خود را انتخاب کنید → یکی از manifestهای زیر را بچسبانید → **Next** → **Create**.

RecommendedCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","emoji:read","files:read","files:write","groups:history","groups:read","im:history","im:read","im:write","mpim:history","mpim:read","mpim:write","pins:read","pins:write","reactions:read","reactions:write","usergroups:read","users:read"]}},"settings": {"socket_mode_enabled": true,"event_subscriptions": {"bot_events": ["app_home_opened","app_mention","channel_rename","member_joined_channel","member_left_channel","message.channels","message.groups","message.im","message.mpim","pin_added","pin_removed","reaction_added","reaction_removed"]}}}
[/code]

MinimalCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","groups:history","groups:read","im:history","im:read","im:write","users:read"]}},"settings": {"socket_mode_enabled": true,"event_subscriptions": {"bot_events": ["app_home_opened","app_mention","message.channels","message.groups","message.im"]}}}
[/code]

پس از اینکه Slack برنامه را ایجاد کرد:

  * **Basic Information → App-Level Tokens → Generate Token and Scopes** : `connections:write` را اضافه کنید، ذخیره کنید، مقدار `xapp-...` را کپی کنید.
  * **Install App → Install to Workspace** : توکن Bot User OAuth با مقدار `xoxb-...` را کپی کنید.


* ### Configure OpenClaw

راه‌اندازی پیشنهادی SecretRef:

bashCopy code
[code]
    export SLACK_APP_TOKEN=xapp-...export SLACK_BOT_TOKEN=xoxb-...cat > slack.socket.patch.json5 <<'JSON5'{channels: {slack: {enabled: true,mode: "socket",appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },},},}JSON5openclaw config patch --file ./slack.socket.patch.json5 --dry-runopenclaw config patch --file ./slack.socket.patch.json5
[/code]

جایگزین env (فقط حساب پیش‌فرض):

bashCopy code
[code]
    SLACK_APP_TOKEN=xapp-...SLACK_BOT_TOKEN=xoxb-...
[/code]

* ### Start gateway

bashCopy code
[code]
    openclaw gateway
[/code]

### HTTP Request URLs

* ### Create a new Slack app

[api.slack.com/apps](<https://api.slack.com/apps/new>) را باز کنید → **Create New App** → **From a manifest** → فضای کاری خود را انتخاب کنید → یکی از manifestهای زیر را بچسبانید → `https://gateway-host.example.com/slack/events` را با URL عمومی Gateway خود جایگزین کنید → **Next** → **Create**.

RecommendedCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false,"url": "https://gateway-host.example.com/slack/events"}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","emoji:read","files:read","files:write","groups:history","groups:read","im:history","im:read","im:write","mpim:history","mpim:read","mpim:write","pins:read","pins:write","reactions:read","reactions:write","usergroups:read","users:read"]}},"settings": {"event_subscriptions": {"request_url": "https://gateway-host.example.com/slack/events","bot_events": ["app_home_opened","app_mention","channel_rename","member_joined_channel","member_left_channel","message.channels","message.groups","message.im","message.mpim","pin_added","pin_removed","reaction_added","reaction_removed"]},"interactivity": {"is_enabled": true,"request_url": "https://gateway-host.example.com/slack/events","message_menu_options_url": "https://gateway-host.example.com/slack/events"}}}
[/code]

MinimalCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false,"url": "https://gateway-host.example.com/slack/events"}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","groups:history","groups:read","im:history","im:read","im:write","users:read"]}},"settings": {"event_subscriptions": {"request_url": "https://gateway-host.example.com/slack/events","bot_events": ["app_home_opened","app_mention","message.channels","message.groups","message.im"]},"interactivity": {"is_enabled": true,"request_url": "https://gateway-host.example.com/slack/events","message_menu_options_url": "https://gateway-host.example.com/slack/events"}}}
[/code]

پس از اینکه Slack برنامه را ایجاد کرد:

  * **Basic Information → App Credentials** : برای راستی‌آزمایی درخواست، **Signing Secret** را کپی کنید.
  * **Install App → Install to Workspace** : توکن OAuth کاربر Bot با قالب `xoxb-...` را کپی کنید.


* ### Configure OpenClaw

راه‌اندازی پیشنهادی SecretRef:

bashCopy code
[code]
    export SLACK_BOT_TOKEN=xoxb-...export SLACK_SIGNING_SECRET=...cat > slack.http.patch.json5 <<'JSON5'{channels: {slack: {enabled: true,mode: "http",botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },signingSecret: { source: "env", provider: "default", id: "SLACK_SIGNING_SECRET" },webhookPath: "/slack/events",},},}JSON5openclaw config patch --file ./slack.http.patch.json5 --dry-runopenclaw config patch --file ./slack.http.patch.json5
[/code]

* ### Start gateway

bashCopy code
[code]
    openclaw gateway
[/code]

## تنظیم transport در Socket Mode

OpenClaw به‌طور پیش‌فرض، timeout مربوط به pong در client کیت توسعه Slack را برای Socket Mode روی ۱۵ ثانیه تنظیم می‌کند. تنظیمات transport را فقط زمانی override کنید که به تنظیمات ویژه فضای کاری یا میزبان نیاز دارید:

json5Copy code
[code]
    {  channels: {    slack: {      mode: "socket",      socketMode: {        clientPingTimeout: 20000,        serverPingTimeout: 30000,        pingPongLoggingEnabled: false,      },    },  },}
[/code]

این را فقط برای فضاهای کاری Socket Mode استفاده کنید که timeoutهای مربوط به pong یا server-ping در websocketهای Slack را ثبت می‌کنند، یا روی میزبان‌هایی اجرا می‌شوند که دچار کمبود شناخته‌شده در event loop هستند. `clientPingTimeout` زمان انتظار برای pong پس از ارسال client ping توسط SDK است؛ `serverPingTimeout` زمان انتظار برای pingهای سرور Slack است. پیام‌ها و رویدادهای برنامه همچنان وضعیت برنامه هستند، نه سیگنال‌های زنده‌بودن transport.

## چک‌لیست manifest و scope

manifest پایه برنامه Slack برای Socket Mode و HTTP Request URLs یکسان است. فقط بلوک `settings` (و `url` فرمان slash) متفاوت است.

manifest پایه (پیش‌فرض Socket Mode):

jsonCopy code
[code]
    {  "display_information": {    "name": "OpenClaw",    "description": "Slack connector for OpenClaw"  },  "features": {    "bot_user": { "display_name": "OpenClaw", "always_online": true },    "app_home": {      "home_tab_enabled": true,      "messages_tab_enabled": true,      "messages_tab_read_only_enabled": false    },    "slash_commands": [      {        "command": "/openclaw",        "description": "Send a message to OpenClaw",        "should_escape": false      }    ]  },  "oauth_config": {    "scopes": {      "bot": [        "app_mentions:read",        "assistant:write",        "channels:history",        "channels:read",        "chat:write",        "commands",        "emoji:read",        "files:read",        "files:write",        "groups:history",        "groups:read",        "im:history",        "im:read",        "im:write",        "mpim:history",        "mpim:read",        "mpim:write",        "pins:read",        "pins:write",        "reactions:read",        "reactions:write",        "usergroups:read",        "users:read"      ]    }  },  "settings": {    "socket_mode_enabled": true,    "event_subscriptions": {      "bot_events": [        "app_home_opened",        "app_mention",        "channel_rename",        "member_joined_channel",        "member_left_channel",        "message.channels",        "message.groups",        "message.im",        "message.mpim",        "pin_added",        "pin_removed",        "reaction_added",        "reaction_removed"      ]    }  }}
[/code]

برای **حالت HTTP Request URLs** ، `settings` را با گونه HTTP جایگزین کنید و به هر فرمان slash مقدار `url` اضافه کنید. URL عمومی لازم است:

jsonCopy code
[code]
    {  "features": {    "slash_commands": [      {        "command": "/openclaw",        "description": "Send a message to OpenClaw",        "should_escape": false,        "url": "https://gateway-host.example.com/slack/events"      }    ]  },  "settings": {    "event_subscriptions": {      "request_url": "https://gateway-host.example.com/slack/events",      "bot_events": [        "app_home_opened",        "app_mention",        "channel_rename",        "member_joined_channel",        "member_left_channel",        "message.channels",        "message.groups",        "message.im",        "message.mpim",        "pin_added",        "pin_removed",        "reaction_added",        "reaction_removed"      ]    },    "interactivity": {      "is_enabled": true,      "request_url": "https://gateway-host.example.com/slack/events",      "message_menu_options_url": "https://gateway-host.example.com/slack/events"    }  }}
[/code]

### تنظیمات تکمیلی manifest

قابلیت‌های متفاوتی را ارائه می‌کند که پیش‌فرض‌های بالا را گسترش می‌دهند.

manifest پیش‌فرض، زبانه **Home** در Slack App Home را فعال می‌کند و در `app_home_opened` مشترک می‌شود. وقتی عضوی از فضای کاری زبانه Home را باز می‌کند، OpenClaw با `views.publish` یک نمای Home پیش‌فرض و امن منتشر می‌کند؛ هیچ payload مکالمه یا پیکربندی خصوصی در آن گنجانده نمی‌شود. زبانه **Messages** برای پیام‌های مستقیم Slack فعال می‌ماند.

Optional native slash commands

می‌توان به‌جای یک فرمان پیکربندی‌شده واحد، چند فرمان slash بومی را با این نکات استفاده کرد:

  * از `/agentstatus` به‌جای `/status` استفاده کنید، زیرا فرمان `/status` رزرو شده است.
  * بیش از ۲۵ فرمان slash را نمی‌توان هم‌زمان در دسترس قرار داد.


بخش موجود `features.slash_commands` خود را با زیرمجموعه‌ای از [فرمان‌های موجود](</fa/tools/slash-commands#command-list>) جایگزین کنید:

### Socket Mode (default)

jsonCopy code
[code]
    {"slash_commands": [{"command": "/new","description": "Start a new session","usage_hint": "[model]"},{"command": "/reset","description": "Reset the current session"},{"command": "/compact","description": "Compact the session context","usage_hint": "[instructions]"},{"command": "/stop","description": "Stop the current run"},{"command": "/session","description": "Manage thread-binding expiry","usage_hint": "idle <duration|off> or max-age <duration|off>"},{"command": "/think","description": "Set the thinking level","usage_hint": "<level>"},{"command": "/verbose","description": "Toggle verbose output","usage_hint": "on|off|full"},{"command": "/fast","description": "Show or set fast mode","usage_hint": "[status|on|off]"},{"command": "/reasoning","description": "Toggle reasoning visibility","usage_hint": "[on|off|stream]"},{"command": "/elevated","description": "Toggle elevated mode","usage_hint": "[on|off|ask|full]"},{"command": "/exec","description": "Show or set exec defaults","usage_hint": "host=<auto|sandbox|gateway|node> security=<deny|allowlist|full> ask=<off|on-miss|always> node=<id>"},{"command": "/model","description": "Show or set the model","usage_hint": "[name|#|status]"},{"command": "/models","description": "List providers/models","usage_hint": "[provider] [page] [limit=<n>|size=<n>|all]"},{"command": "/help","description": "Show the short help summary"},{"command": "/commands","description": "Show the generated command catalog"},{"command": "/tools","description": "Show what the current agent can use right now","usage_hint": "[compact|verbose]"},{"command": "/agentstatus","description": "Show runtime status, including provider usage/quota when available"},{"command": "/tasks","description": "List active/recent background tasks for the current session"},{"command": "/context","description": "Explain how context is assembled","usage_hint": "[list|detail|json]"},{"command": "/whoami","description": "Show your sender identity"},{"command": "/skill","description": "Run a skill by name","usage_hint": "<name> [input]"},{"command": "/btw","description": "Ask a side question without changing session context","usage_hint": "<question>"},{"command": "/side","description": "Ask a side question without changing session context","usage_hint": "<question>"},{"command": "/usage","description": "Control the usage footer or show cost summary","usage_hint": "off|tokens|full|cost"}]}
[/code]

### HTTP Request URLs

همان فهرست `slash_commands` در Socket Mode بالا را استفاده کنید، و به هر ورودی `"url": "https://gateway-host.example.com/slack/events"` را اضافه کنید. نمونه:

jsonCopy code
[code]
    {"slash_commands": [{"command": "/new","description": "Start a new session","usage_hint": "[model]","url": "https://gateway-host.example.com/slack/events"},{"command": "/help","description": "Show the short help summary","url": "https://gateway-host.example.com/slack/events"}]}
[/code]

آن مقدار `url` را برای هر فرمان در فهرست تکرار کنید.

دامنه‌های اختیاری نویسندگی (عملیات نوشتن)

اگر می‌خواهید پیام‌های خروجی به‌جای هویت پیش‌فرض برنامه Slack از هویت عامل فعال (نام کاربری و آیکون سفارشی) استفاده کنند، دامنه بات `chat:write.customize` را اضافه کنید.

اگر از آیکون ایموجی استفاده می‌کنید، Slack انتظار نحو `:emoji_name:` را دارد.

دامنه‌های اختیاری توکن کاربر (عملیات خواندن)

اگر `channels.slack.userToken` را پیکربندی کنید، دامنه‌های معمول خواندن عبارت‌اند از:

  * `channels:history`, `groups:history`, `im:history`, `mpim:history`
  * `channels:read`, `groups:read`, `im:read`, `mpim:read`
  * `users:read`
  * `reactions:read`
  * `pins:read`
  * `emoji:read`
  * `search:read` (اگر به خواندن‌های جست‌وجوی Slack وابسته هستید)


## مدل توکن

  * `botToken` \+ `appToken` برای Socket Mode الزامی هستند.
  * حالت HTTP به `botToken` \+ `signingSecret` نیاز دارد.
  * `botToken`، `appToken`، `signingSecret` و `userToken` رشته‌های متن ساده یا اشیای SecretRef را می‌پذیرند.
  * توکن‌های پیکربندی، جایگزین پشتیبان env می‌شوند.
  * پشتیبان env با `SLACK_BOT_TOKEN` / `SLACK_APP_TOKEN` فقط برای حساب پیش‌فرض اعمال می‌شود.
  * `userToken` (`xoxp-...`) فقط از طریق پیکربندی است (بدون پشتیبان env) و به‌طور پیش‌فرض رفتار فقط‌خواندنی دارد (`userTokenReadOnly: true`).


رفتار عکس‌برداری وضعیت:

  * بازرسی حساب Slack فیلدهای `*Source` و `*Status` را برای هر اعتبارنامه ردیابی می‌کند (`botToken`، `appToken`، `signingSecret`، `userToken`).
  * وضعیت `available`، `configured_unavailable` یا `missing` است.
  * `configured_unavailable` یعنی حساب از طریق SecretRef یا منبع محرمانه غیرخطی دیگری پیکربندی شده است، اما مسیر دستور/زمان اجرای فعلی نتوانسته مقدار واقعی را resolve کند.
  * در حالت HTTP، `signingSecretStatus` گنجانده می‌شود؛ در Socket Mode، جفت الزامی `botTokenStatus` \+ `appTokenStatus` است.


## کنش‌ها و گیت‌ها

کنش‌های Slack با `channels.slack.actions.*` کنترل می‌شوند.

گروه‌های کنش موجود در ابزارهای فعلی Slack:

گروه | پیش‌فرض  
---|---  
messages | فعال  
reactions | فعال  
pins | فعال  
memberInfo | فعال  
emojiList | فعال  
  
کنش‌های پیام فعلی Slack شامل `send`، `upload-file`، `download-file`، `read`، `edit`، `delete`، `pin`، `unpin`، `list-pins`، `member-info` و `emoji-list` هستند. `download-file` شناسه‌های فایل Slack را که در placeholderهای فایل ورودی نشان داده می‌شوند می‌پذیرد و برای تصاویر پیش‌نمایش تصویر یا برای انواع فایل دیگر فراداده فایل محلی برمی‌گرداند.

## کنترل دسترسی و مسیریابی

### سیاست DM

`channels.slack.dmPolicy` دسترسی DM را کنترل می‌کند. `channels.slack.allowFrom` allowlist کانونی DM است.

  * `pairing` (پیش‌فرض)
  * `allowlist`
  * `open` (نیاز دارد `channels.slack.allowFrom` شامل `"*"` باشد)
  * `disabled`


پرچم‌های DM:

  * `dm.enabled` (پیش‌فرض true)
  * `channels.slack.allowFrom`
  * `dm.allowFrom` (قدیمی)
  * `dm.groupEnabled` (DMهای گروهی به‌طور پیش‌فرض false)
  * `dm.groupChannels` (allowlist اختیاری MPIM)


اولویت چندحسابی:

  * `channels.slack.accounts.default.allowFrom` فقط برای حساب `default` اعمال می‌شود.
  * حساب‌های نام‌دار، وقتی `allowFrom` خودشان تنظیم نشده باشد، `channels.slack.allowFrom` را به ارث می‌برند.
  * حساب‌های نام‌دار `channels.slack.accounts.default.allowFrom` را به ارث نمی‌برند.


`channels.slack.dm.policy` و `channels.slack.dm.allowFrom` قدیمی همچنان برای سازگاری خوانده می‌شوند. `openclaw doctor --fix` وقتی بتواند بدون تغییر دسترسی این کار را انجام دهد، آن‌ها را به `dmPolicy` و `allowFrom` مهاجرت می‌دهد.

جفت‌سازی در DMها از `openclaw pairing approve slack <code>` استفاده می‌کند.

### سیاست کانال

`channels.slack.groupPolicy` مدیریت کانال را کنترل می‌کند:

  * `open`
  * `allowlist`
  * `disabled`


allowlist کانال زیر `channels.slack.channels` قرار دارد و **باید از شناسه‌های پایدار کانال Slack** (برای مثال `C12345678`) به‌عنوان کلیدهای پیکربندی استفاده کند.

نکته زمان اجرا: اگر `channels.slack` کاملا وجود نداشته باشد (راه‌اندازی فقط با env)، زمان اجرا به `groupPolicy="allowlist"` برمی‌گردد و یک هشدار ثبت می‌کند (حتی اگر `channels.defaults.groupPolicy` تنظیم شده باشد).

resolve نام/شناسه:

  * ورودی‌های allowlist کانال و ورودی‌های allowlist DM هنگام راه‌اندازی، وقتی دسترسی توکن اجازه دهد، resolve می‌شوند
  * ورودی‌های resolveنشده نام کانال همان‌طور که پیکربندی شده‌اند نگه داشته می‌شوند، اما به‌طور پیش‌فرض برای مسیریابی نادیده گرفته می‌شوند
  * مجوزدهی ورودی و مسیریابی کانال به‌طور پیش‌فرض شناسه‌اول هستند؛ تطبیق مستقیم نام کاربری/slug نیازمند `channels.slack.dangerouslyAllowNameMatching: true` است


### اشاره‌ها و کاربران کانال

پیام‌های کانال به‌طور پیش‌فرض با اشاره gating می‌شوند.

منابع اشاره:

  * اشاره صریح برنامه (`<@botId>`)
  * اشاره گروه کاربری Slack (`<!subteam^S...>`) وقتی کاربر بات عضو آن گروه کاربری باشد؛ نیازمند `usergroups:read`
  * الگوهای regex اشاره (`agents.list[].groupChat.mentionPatterns`، پشتیبان `messages.groupChat.mentionPatterns`)
  * رفتار ضمنی پاسخ‌به-بات در رشته (وقتی `thread.requireExplicitMention` برابر `true` باشد غیرفعال است)


کنترل‌های هر کانال (`channels.slack.channels.<id>`؛ نام‌ها فقط از طریق resolve هنگام راه‌اندازی یا `dangerouslyAllowNameMatching`):

  * `requireMention`
  * `users` (allowlist)
  * `allowBots`
  * `skills`
  * `systemPrompt`
  * `tools`, `toolsBySender`
  * قالب کلید `toolsBySender`: `channel:`، `id:`، `e164:`، `username:`، `name:`، یا wildcard `"*"` (کلیدهای قدیمی بدون پیشوند همچنان فقط به `id:` نگاشت می‌شوند)


`allowBots` برای کانال‌ها و کانال‌های خصوصی محافظه‌کارانه است: پیام‌های اتاق که توسط بات نوشته شده‌اند فقط زمانی پذیرفته می‌شوند که بات فرستنده صراحتا در allowlist `users` همان اتاق فهرست شده باشد، یا وقتی حداقل یک شناسه صریح مالک Slack از `channels.slack.allowFrom` در حال حاضر عضو اتاق باشد. wildcardها و ورودی‌های مالک با نام نمایشی، حضور مالک را برآورده نمی‌کنند. حضور مالک از Slack `conversations.members` استفاده می‌کند؛ مطمئن شوید برنامه دامنه خواندن متناظر را برای نوع اتاق دارد (`channels:read` برای کانال‌های عمومی، `groups:read` برای کانال‌های خصوصی). اگر جست‌وجوی عضو شکست بخورد، OpenClaw پیام اتاق نوشته‌شده توسط بات را حذف می‌کند.

## رشته‌بندی، نشست‌ها و برچسب‌های پاسخ

  * DMها به‌صورت `direct` مسیریابی می‌شوند؛ کانال‌ها به‌صورت `channel`؛ MPIMها به‌صورت `group`.
  * bindingهای مسیر Slack شناسه‌های خام peer به‌علاوه فرم‌های هدف Slack مانند `channel:C12345678`، `user:U12345678` و `<@U12345678>` را می‌پذیرند.
  * با `session.dmScope=main` پیش‌فرض، DMهای Slack به نشست اصلی عامل collapse می‌شوند.
  * نشست‌های کانال: `agent:<agentId>:slack:channel:<channelId>`.
  * پاسخ‌های رشته می‌توانند در صورت کاربرد، پسوندهای نشست رشته (`:thread:<threadTs>`) ایجاد کنند.
  * در کانال‌هایی که OpenClaw پیام‌های سطح بالا را بدون نیاز به اشاره صریح مدیریت می‌کند، `replyToMode` غیر از `off` هر root مدیریت‌شده را به `agent:<agentId>:slack:channel:<channelId>:thread:<rootTs>` مسیریابی می‌کند تا رشته قابل مشاهده Slack از نخستین نوبت به یک نشست OpenClaw نگاشت شود.
  * مقدار پیش‌فرض `channels.slack.thread.historyScope` برابر `thread` است؛ مقدار پیش‌فرض `thread.inheritParent` برابر `false` است.
  * `channels.slack.thread.initialHistoryLimit` کنترل می‌کند هنگام شروع یک نشست رشته جدید چند پیام موجود رشته واکشی شود (پیش‌فرض `20`؛ برای غیرفعال‌سازی روی `0` تنظیم کنید).
  * `channels.slack.thread.requireExplicitMention` (پیش‌فرض `false`): وقتی `true` باشد، اشاره‌های ضمنی رشته را سرکوب می‌کند تا بات فقط به اشاره‌های صریح `@bot` داخل رشته‌ها پاسخ دهد، حتی وقتی بات قبلا در رشته مشارکت کرده باشد. بدون این، پاسخ‌ها در رشته‌ای که بات در آن مشارکت داشته است، gating مربوط به `requireMention` را دور می‌زنند.


کنترل‌های رشته‌بندی پاسخ:

  * `channels.slack.replyToMode`: `off|first|all|batched` (پیش‌فرض `off`)
  * `channels.slack.replyToModeByChatType`: برای هر `direct|group|channel`
  * پشتیبان قدیمی برای چت‌های مستقیم: `channels.slack.dm.replyToMode`


برچسب‌های پاسخ دستی پشتیبانی می‌شوند:

  * `[[reply_to_current]]`
  * `[[reply_to:<id>]]`


برای پاسخ‌های صریح رشته Slack از ابزار `message`، `replyBroadcast: true` را همراه با `action: "send"` و `threadId` یا `replyTo` تنظیم کنید تا از Slack بخواهید پاسخ رشته را در کانال والد نیز broadcast کند. این به پرچم `reply_broadcast` در `chat.postMessage` Slack نگاشت می‌شود و فقط برای ارسال‌های متن یا Block Kit پشتیبانی می‌شود، نه بارگذاری رسانه.

وقتی فراخوانی ابزار `message` داخل یک رشته Slack اجرا می‌شود و همان کانال را هدف می‌گیرد، OpenClaw معمولا رشته فعلی Slack را طبق `replyToMode` به ارث می‌برد. برای اجبار به پیام جدید در کانال والد، `topLevel: true` را روی `action: "send"` یا `action: "upload-file"` تنظیم کنید. `threadId: null` نیز به‌عنوان همان opt-out سطح بالا پذیرفته می‌شود.

## واکنش‌های تأیید

`ackReaction` هنگام پردازش یک پیام ورودی توسط OpenClaw، یک ایموجی تأیید ارسال می‌کند.

ترتیب resolve:

  * `channels.slack.accounts.<accountId>.ackReaction`
  * `channels.slack.ackReaction`
  * `messages.ackReaction`
  * پشتیبان ایموجی هویت عامل (`agents.list[].identity.emoji`، وگرنه "👀")


نکته‌ها:

  * Slack انتظار shortcodeها را دارد (برای مثال `"eyes"`).
  * برای غیرفعال‌سازی واکنش برای حساب Slack یا به‌صورت سراسری، از `""` استفاده کنید.


## پخش جریانی متن

`channels.slack.streaming` رفتار پیش‌نمایش زنده را کنترل می‌کند:

  * `off`: پخش جریانی پیش‌نمایش زنده را غیرفعال می‌کند.
  * `partial` (پیش‌فرض): متن پیش‌نمایش را با آخرین خروجی جزئی جایگزین می‌کند.
  * `block`: به‌روزرسانی‌های پیش‌نمایش chunkشده را اضافه می‌کند.
  * `progress`: هنگام تولید، متن وضعیت پیشرفت را نشان می‌دهد، سپس متن نهایی را ارسال می‌کند.
  * `streaming.preview.toolProgress`: وقتی پیش‌نمایش draft فعال است، به‌روزرسانی‌های ابزار/پیشرفت را به همان پیام پیش‌نمایش ویرایش‌شده هدایت می‌کند (پیش‌فرض: `true`). برای نگه‌داشتن پیام‌های جداگانه ابزار/پیشرفت، روی `false` تنظیم کنید.
  * `streaming.preview.commandText` / `streaming.progress.commandText`: برای نگه‌داشتن خط‌های فشرده پیشرفت ابزار هنگام پنهان‌کردن متن خام دستور/exec، روی `status` تنظیم کنید (پیش‌فرض: `raw`).


پنهان‌کردن متن خام دستور/exec در حالی که خط‌های فشرده پیشرفت حفظ شوند:

jsonCopy code
[code]
    {  "channels": {    "slack": {      "streaming": {        "mode": "progress",        "progress": {          "toolProgress": true,          "commandText": "status"        }      }    }  }}
[/code]

`channels.slack.streaming.nativeTransport` پخش جریانی متن بومی Slack را زمانی کنترل می‌کند که `channels.slack.streaming.mode` برابر `partial` باشد (پیش‌فرض: `true`).

  * برای نمایش استریم متن بومی و وضعیت رشتهٔ دستیار Slack، باید یک رشتهٔ پاسخ در دسترس باشد. انتخاب رشته همچنان از `replyToMode` پیروی می‌کند.
  * ریشه‌های کانال، گفت‌وگوی گروهی، و DM سطح بالا همچنان می‌توانند وقتی استریم بومی در دسترس نیست یا هیچ رشتهٔ پاسخی وجود ندارد از پیش‌نمایش پیش‌نویس معمولی استفاده کنند.
  * DMهای سطح بالای Slack به‌طور پیش‌فرض خارج از رشته می‌مانند، بنابراین پیش‌نمایش استریم/وضعیت بومی سبک رشته‌ای Slack را نشان نمی‌دهند؛ OpenClaw به‌جای آن یک پیش‌نمایش پیش‌نویس را در DM ارسال و ویرایش می‌کند.
  * رسانه و بارهای دادهٔ غیرمتنی به تحویل معمولی برمی‌گردند.
  * نهایی‌های رسانه/خطا ویرایش‌های معلق پیش‌نمایش را لغو می‌کنند؛ نهایی‌های متن/بلوک واجد شرایط فقط وقتی ارسال نهایی می‌شوند که بتوانند پیش‌نمایش را درجا ویرایش کنند.
  * اگر استریم در میانهٔ پاسخ شکست بخورد، OpenClaw برای بارهای دادهٔ باقی‌مانده به تحویل معمولی برمی‌گردد.


به‌جای استریم متن بومی Slack از پیش‌نمایش پیش‌نویس استفاده کنید:

json5Copy code
[code]
    {  channels: {    slack: {      streaming: {        mode: "partial",        nativeTransport: false,      },    },  },}
[/code]

کلیدهای قدیمی:

  * `channels.slack.streamMode` (`replace | status_final | append`) یک نام مستعار قدیمی زمان اجرا برای `channels.slack.streaming.mode` است.
  * بولی `channels.slack.streaming` یک نام مستعار قدیمی زمان اجرا برای `channels.slack.streaming.mode` و `channels.slack.streaming.nativeTransport` است.
  * `channels.slack.nativeStreaming` قدیمی یک نام مستعار زمان اجرا برای `channels.slack.streaming.nativeTransport` است.
  * برای بازنویسی پیکربندی ذخیره‌شدهٔ استریم Slack به کلیدهای کانونی، `openclaw doctor --fix` را اجرا کنید.


## مسیر جایگزین واکنش تایپ

`typingReaction` هنگام پردازش پاسخ توسط OpenClaw یک واکنش موقت به پیام ورودی Slack اضافه می‌کند و پس از پایان اجرا آن را حذف می‌کند. این بیشتر خارج از پاسخ‌های رشته‌ای مفید است، چون پاسخ‌های رشته‌ای از نشانگر وضعیت پیش‌فرض «در حال تایپ است...» استفاده می‌کنند.

ترتیب حل:

  * `channels.slack.accounts.<accountId>.typingReaction`
  * `channels.slack.typingReaction`


نکته‌ها:

  * Slack انتظار کدهای کوتاه را دارد (برای مثال `"hourglass_flowing_sand"`).
  * واکنش با بهترین تلاش انجام می‌شود و پس از تکمیل مسیر پاسخ یا شکست، پاک‌سازی به‌طور خودکار تلاش می‌شود.


## رسانه، تکه‌سازی، و تحویل

پیوست‌های ورودی

پیوست‌های فایل Slack از URLهای خصوصی میزبانی‌شده توسط Slack (جریان درخواست احراز هویت‌شده با توکن) دانلود می‌شوند و وقتی واکشی موفق باشد و محدودیت‌های اندازه اجازه دهند، در مخزن رسانه نوشته می‌شوند. جای‌نگهدارهای فایل شامل `fileId` مربوط به Slack هستند تا عامل‌ها بتوانند فایل اصلی را با `download-file` واکشی کنند.

دانلودها از مهلت‌های زمانی محدود برای بیکاری و کل فرایند استفاده می‌کنند. اگر بازیابی فایل Slack متوقف شود یا شکست بخورد، OpenClaw پردازش پیام را ادامه می‌دهد و به جای‌نگهدار فایل برمی‌گردد.

سقف اندازهٔ ورودی در زمان اجرا به‌طور پیش‌فرض `20MB` است، مگر اینکه با `channels.slack.mediaMaxMb` بازنویسی شود.

متن و فایل‌های خروجی

  * تکه‌های متن از `channels.slack.textChunkLimit` استفاده می‌کنند (پیش‌فرض 4000)
  * `channels.slack.chunkMode="newline"` تقسیم‌بندی با اولویت پاراگراف را فعال می‌کند
  * ارسال فایل‌ها از APIهای بارگذاری Slack استفاده می‌کند و می‌تواند شامل پاسخ‌های رشته‌ای (`thread_ts`) باشد
  * سقف رسانهٔ خروجی، وقتی پیکربندی شده باشد، از `channels.slack.mediaMaxMb` پیروی می‌کند؛ در غیر این صورت ارسال‌های کانال از پیش‌فرض‌های نوع MIME در خط لولهٔ رسانه استفاده می‌کنند

مقصدهای تحویل

مقصدهای صریح ترجیحی:

  * `user:<id>` برای DMها
  * `channel:<id>` برای کانال‌ها


DMهای Slack که فقط متن/بلوک دارند می‌توانند مستقیماً به IDهای کاربر ارسال کنند؛ بارگذاری فایل و ارسال‌های رشته‌ای ابتدا DM را از طریق APIهای گفت‌وگوی Slack باز می‌کنند، چون این مسیرها به یک ID گفت‌وگوی مشخص نیاز دارند.

## فرمان‌ها و رفتار اسلش

فرمان‌های اسلش در Slack یا به‌صورت یک فرمان پیکربندی‌شدهٔ واحد یا چند فرمان بومی ظاهر می‌شوند. برای تغییر پیش‌فرض‌های فرمان، `channels.slack.slashCommand` را پیکربندی کنید:

  * `enabled: false`
  * `name: "openclaw"`
  * `sessionPrefix: "slack:slash"`
  * `ephemeral: true`

txtCopy code
[code]
    /openclaw /help
[/code]

فرمان‌های بومی به تنظیمات اضافی manifest در اپ Slack شما نیاز دارند و به‌جای آن با `channels.slack.commands.native: true` یا `commands.native: true` در پیکربندی‌های سراسری فعال می‌شوند.

  * حالت خودکار فرمان بومی برای Slack **خاموش** است، بنابراین `commands.native: "auto"` فرمان‌های بومی Slack را فعال نمی‌کند.

txtCopy code
[code]
    /help
[/code]

منوهای آرگومان بومی از یک راهبرد رندر تطبیقی استفاده می‌کنند که پیش از ارسال مقدار گزینهٔ انتخاب‌شده، یک modal تأیید نشان می‌دهد:

  * تا 5 گزینه: بلوک‌های دکمه
  * 6-100 گزینه: منوی انتخاب ایستا
  * بیش از 100 گزینه: انتخاب خارجی با فیلتر async گزینه‌ها وقتی هندلرهای گزینه‌های تعامل‌پذیری در دسترس باشند
  * فراتر رفتن از محدودیت‌های Slack: مقدارهای گزینهٔ کدگذاری‌شده به دکمه‌ها برمی‌گردند

txtCopy code
[code]
    /think
[/code]

نشست‌های اسلش از کلیدهای جداگانه‌ای مانند `agent:<agentId>:slack:slash:<userId>` استفاده می‌کنند و همچنان اجرای فرمان‌ها را با استفاده از `CommandTargetSessionKey` به نشست گفت‌وگوی مقصد مسیریابی می‌کنند.

## پاسخ‌های تعاملی

Slack می‌تواند کنترل‌های پاسخ تعاملی نوشته‌شده توسط عامل را رندر کند، اما این قابلیت به‌طور پیش‌فرض غیرفعال است.

فعال‌سازی سراسری:

json5Copy code
[code]
    {  channels: {    slack: {      capabilities: {        interactiveReplies: true,      },    },  },}
[/code]

یا فقط برای یک حساب Slack فعال کنید:

json5Copy code
[code]
    {  channels: {    slack: {      accounts: {        ops: {          capabilities: {            interactiveReplies: true,          },        },      },    },  },}
[/code]

وقتی فعال باشد، عامل‌ها می‌توانند دستورالعمل‌های پاسخ مختص Slack منتشر کنند:

  * `[[slack_buttons: Approve:approve, Reject:reject]]`
  * `[[slack_select: Choose a target | Canary:canary, Production:production]]`


این دستورالعمل‌ها به Slack Block Kit کامپایل می‌شوند و کلیک‌ها یا انتخاب‌ها را از مسیر رویداد تعامل موجود Slack برمی‌گردانند.

نکته‌ها:

  * این رابط کاربری مختص Slack است. کانال‌های دیگر دستورالعمل‌های Slack Block Kit را به سیستم‌های دکمهٔ خودشان ترجمه نمی‌کنند.
  * مقدارهای callback تعاملی، توکن‌های مات تولیدشده توسط OpenClaw هستند، نه مقدارهای خام نوشته‌شده توسط عامل.
  * اگر بلوک‌های تعاملی تولیدشده از محدودیت‌های Slack Block Kit فراتر بروند، OpenClaw به‌جای ارسال بار دادهٔ blocks نامعتبر، به پاسخ متنی اصلی برمی‌گردد.


## تأییدهای اجرا در Slack

Slack می‌تواند به‌جای برگشتن به رابط کاربری وب یا ترمینال، به‌عنوان یک کلاینت تأیید بومی با دکمه‌ها و تعامل‌های تعاملی عمل کند.

  * تأییدهای اجرا از `channels.slack.execApprovals.*` برای مسیریابی بومی DM/کانال استفاده می‌کنند.
  * تأییدهای Plugin همچنان می‌توانند از همان سطح دکمهٔ بومی Slack حل شوند، وقتی درخواست از قبل در Slack فرود آمده باشد و نوع ID تأیید `plugin:` باشد.
  * مجوز تأییدکننده همچنان اعمال می‌شود: فقط کاربرانی که به‌عنوان تأییدکننده شناسایی شده‌اند می‌توانند از طریق Slack درخواست‌ها را تأیید یا رد کنند.


این از همان سطح مشترک دکمهٔ تأیید مانند کانال‌های دیگر استفاده می‌کند. وقتی `interactivity` در تنظیمات اپ Slack شما فعال باشد، اعلان‌های تأیید مستقیماً در گفت‌وگو به‌صورت دکمه‌های Block Kit رندر می‌شوند. وقتی آن دکمه‌ها وجود دارند، تجربهٔ کاربری اصلی تأیید هستند؛ OpenClaw فقط وقتی باید فرمان دستی `/approve` را شامل کند که نتیجهٔ ابزار بگوید تأییدهای چت در دسترس نیستند یا تأیید دستی تنها مسیر است.

مسیر پیکربندی:

  * `channels.slack.execApprovals.enabled`
  * `channels.slack.execApprovals.approvers` (اختیاری؛ وقتی ممکن باشد به `commands.ownerAllowFrom` برمی‌گردد)
  * `channels.slack.execApprovals.target` (`dm` | `channel` | `both`، پیش‌فرض: `dm`)
  * `agentFilter`, `sessionFilter`


وقتی `enabled` تنظیم نشده باشد یا `"auto"` باشد و دست‌کم یک تأییدکننده حل شود، Slack تأییدهای اجرای بومی را به‌طور خودکار فعال می‌کند. برای غیرفعال‌سازی صریح Slack به‌عنوان کلاینت تأیید بومی، `enabled: false` را تنظیم کنید. برای اجبار به روشن بودن تأییدهای بومی وقتی تأییدکننده‌ها حل می‌شوند، `enabled: true` را تنظیم کنید.

رفتار پیش‌فرض بدون پیکربندی صریح تأیید اجرای Slack:

json5Copy code
[code]
    {  commands: {    ownerAllowFrom: ["slack:U12345678"],  },}
[/code]

پیکربندی صریح بومی Slack فقط وقتی لازم است که بخواهید تأییدکننده‌ها را بازنویسی کنید، فیلتر اضافه کنید، یا تحویل به گفت‌وگوی مبدأ را انتخاب کنید:

json5Copy code
[code]
    {  channels: {    slack: {      execApprovals: {        enabled: true,        approvers: ["U12345678"],        target: "both",      },    },  },}
[/code]

ارسال مشترک `approvals.exec` جداگانه است. فقط وقتی از آن استفاده کنید که اعلان‌های تأیید اجرا باید علاوه بر این به چت‌های دیگر یا مقصدهای صریح خارج از مسیر هم مسیریابی شوند. ارسال مشترک `approvals.plugin` نیز جداگانه است؛ دکمه‌های بومی Slack همچنان می‌توانند تأییدهای Plugin را وقتی آن درخواست‌ها از قبل در Slack فرود آمده‌اند حل کنند.

`/approve` در همان گفت‌وگو نیز در کانال‌ها و DMهای Slack که از قبل از فرمان‌ها پشتیبانی می‌کنند کار می‌کند. برای مدل کامل ارسال تأیید، [تأییدهای اجرا](</fa/tools/exec-approvals>) را ببینید.

## رویدادها و رفتار عملیاتی

  * ویرایش/حذف پیام‌ها به رویدادهای سیستمی نگاشت می‌شوند.
  * پخش‌های رشته‌ای (پاسخ‌های رشته‌ای «همچنین به کانال ارسال شود») به‌عنوان پیام‌های معمولی کاربر پردازش می‌شوند.
  * رویدادهای افزودن/حذف واکنش به رویدادهای سیستمی نگاشت می‌شوند.
  * رویدادهای عضویت/خروج عضو، ایجاد/تغییرنام کانال، و افزودن/حذف pin به رویدادهای سیستمی نگاشت می‌شوند.
  * وقتی `configWrites` فعال باشد، `channel_id_changed` می‌تواند کلیدهای پیکربندی کانال را مهاجرت دهد.
  * فرادادهٔ موضوع/هدف کانال به‌عنوان زمینهٔ نامطمئن در نظر گرفته می‌شود و می‌تواند به زمینهٔ مسیریابی تزریق شود.
  * شروع‌کنندهٔ رشته و کاشت اولیهٔ زمینهٔ تاریخچهٔ رشته، در صورت کاربرد، با فهرست‌های مجاز فرستندهٔ پیکربندی‌شده فیلتر می‌شوند.
  * اکشن‌های بلوک و تعامل‌های modal رویدادهای سیستمی ساخت‌یافتهٔ `Slack interaction: ...` را با فیلدهای غنی بار داده منتشر می‌کنند: 
    * اکشن‌های بلوک: مقدارهای انتخاب‌شده، برچسب‌ها، مقدارهای انتخاب‌گر، و فرادادهٔ `workflow_*`
    * رویدادهای modal `view_submission` و `view_closed` با فرادادهٔ کانال مسیریابی‌شده و ورودی‌های فرم


## مرجع پیکربندی

مرجع اصلی: [مرجع پیکربندی - Slack](</fa/gateway/config-channels#slack>).

فیلدهای مهم Slack

  * حالت/احراز هویت: `mode`, `botToken`, `appToken`, `signingSecret`, `webhookPath`, `accounts.*`
  * دسترسی DM: `dm.enabled`, `dmPolicy`, `allowFrom` (قدیمی: `dm.policy`, `dm.allowFrom`), `dm.groupEnabled`, `dm.groupChannels`
  * کلید تغییر سازگاری: `dangerouslyAllowNameMatching` (مسیر اضطراری؛ مگر در صورت نیاز خاموش نگه دارید)
  * دسترسی کانال: `groupPolicy`, `channels.*`, `channels.*.users`, `channels.*.requireMention`
  * رشته/تاریخچه: `replyToMode`, `replyToModeByChatType`, `thread.*`, `historyLimit`, `dmHistoryLimit`, `dms.*.historyLimit`
  * تحویل: `textChunkLimit`, `chunkMode`, `mediaMaxMb`, `streaming`, `streaming.nativeTransport`, `streaming.preview.toolProgress`
  * پیش‌نمایش‌ها: `unfurlLinks`, `unfurlMedia` برای کنترل پیش‌نمایش لینک/رسانهٔ `chat.postMessage`
  * عملیات/قابلیت‌ها: `configWrites`, `commands.native`, `slashCommand.*`, `actions.*`, `userToken`, `userTokenReadOnly`


## عیب‌یابی

پاسخی در کانال‌ها نیست

به‌ترتیب بررسی کنید:

  * `groupPolicy`
  * فهرست مجاز کانال (`channels.slack.channels`) — **کلیدها باید ID کانال باشند** (`C12345678`)، نه نام‌ها (`#channel-name`). کلیدهای مبتنی بر نام تحت `groupPolicy: "allowlist"` بی‌صدا شکست می‌خورند، چون مسیریابی کانال به‌طور پیش‌فرض ابتدا بر اساس ID است. برای یافتن ID: روی کانال در Slack راست‌کلیک کنید ← **کپی لینک** — مقدار `C...` در انتهای URL همان ID کانال است.
  * `requireMention`
  * فهرست مجاز `users` مخصوص هر کانال


فرمان‌های مفید:

bashCopy code
[code]
    openclaw channels status --probeopenclaw logs --followopenclaw doctor
[/code]

پیام‌های DM نادیده گرفته می‌شوند

بررسی کنید:

  * `channels.slack.dm.enabled`
  * `channels.slack.dmPolicy` (یا `channels.slack.dm.policy` قدیمی)
  * تأییدهای جفت‌سازی / ورودی‌های فهرست مجاز
  * رویدادهای DM دستیار Slack: لاگ‌های پرجزئیاتی که به `drop message_changed` اشاره می‌کنند معمولاً یعنی Slack یک رویداد ویرایش‌شدهٔ رشتهٔ دستیار فرستاده است بدون فرستندهٔ انسانی قابل بازیابی در فرادادهٔ پیام

bashCopy code
[code]
    openclaw pairing list slack
[/code]

Socket Mode وصل نمی‌شود

توکن‌های bot + app و فعال بودن Socket Mode را در تنظیمات اپ Slack اعتبارسنجی کنید.

اگر `openclaw channels status --probe --json` مقدار `botTokenStatus` یا `appTokenStatus: "configured_unavailable"` را نشان می‌دهد، حساب Slack پیکربندی شده اما زمان اجرای فعلی نتوانسته مقدار پشتیبانی‌شده با SecretRef را حل کند.

حالت HTTP رویدادها را دریافت نمی‌کند

اعتبارسنجی کنید:

  * راز امضا
  * مسیر webhook
  * URLهای درخواست Slack (رویدادها + تعامل‌پذیری + دستورات اسلش)
  * `webhookPath` یکتا برای هر حساب HTTP


اگر `signingSecretStatus: "configured_unavailable"` در snapshotهای حساب ظاهر شود، حساب HTTP پیکربندی شده است، اما runtime فعلی نتوانسته راز امضای مبتنی بر SecretRef را resolve کند.

دستورات بومی/اسلش اجرا نمی‌شوند

بررسی کنید آیا منظورتان این بوده است:

  * حالت دستور بومی (`channels.slack.commands.native: true`) همراه با دستورات اسلش متناظر ثبت‌شده در Slack
  * یا حالت دستور اسلش تکی (`channels.slack.slashCommand.enabled: true`)


همچنین `commands.useAccessGroups` و allowlistهای کانال/کاربر را بررسی کنید.

## مرجع بینایی پیوست‌ها

Slack می‌تواند وقتی دانلود فایل‌های Slack موفق باشد و محدودیت‌های اندازه اجازه دهند، رسانه دانلودشده را به نوبت عامل پیوست کند. فایل‌های تصویری می‌توانند از مسیر درک رسانه عبور داده شوند یا مستقیماً به یک مدل پاسخ‌گوی دارای قابلیت بینایی فرستاده شوند؛ فایل‌های دیگر به‌عنوان زمینه فایل قابل دانلود نگه داشته می‌شوند، نه اینکه به‌عنوان ورودی تصویر پردازش شوند.

### انواع رسانه پشتیبانی‌شده

نوع رسانه | منبع | رفتار فعلی | یادداشت‌ها  
---|---|---|---  
تصاویر JPEG / PNG / GIF / WebP | URL فایل Slack | دانلود شده و برای پردازش دارای قابلیت بینایی به نوبت پیوست می‌شود | سقف هر فایل: `channels.slack.mediaMaxMb` (پیش‌فرض 20 MB)  
فایل‌های PDF | URL فایل Slack | دانلود شده و به‌عنوان زمینه فایل برای ابزارهایی مانند `download-file` یا `pdf` ارائه می‌شود | ورودی Slack به‌طور خودکار PDFها را به ورودی بینایی تصویر تبدیل نمی‌کند  
فایل‌های دیگر | URL فایل Slack | در صورت امکان دانلود شده و به‌عنوان زمینه فایل ارائه می‌شود | فایل‌های باینری به‌عنوان ورودی تصویر پردازش نمی‌شوند  
پاسخ‌های thread | فایل‌های آغازگر thread | فایل‌های پیام ریشه وقتی پاسخ رسانه مستقیم ندارد می‌توانند به‌عنوان زمینه hydrate شوند | آغازگرهای فقط-فایل از placeholder پیوست استفاده می‌کنند  
پیام‌های چندتصویری | چند فایل Slack | هر فایل به‌صورت مستقل ارزیابی می‌شود | پردازش Slack به هشت فایل در هر پیام محدود است  
  
### pipeline ورودی

وقتی یک پیام Slack همراه با پیوست‌های فایل وارد می‌شود:

  1. OpenClaw فایل را از URL خصوصی Slack با استفاده از توکن ربات (`xoxb-...`) دانلود می‌کند.
  2. فایل در صورت موفقیت در مخزن رسانه نوشته می‌شود.
  3. مسیرهای رسانه دانلودشده و انواع محتوا به زمینه ورودی اضافه می‌شوند.
  4. مسیرهای مدل/ابزار دارای قابلیت تصویر می‌توانند از پیوست‌های تصویر آن زمینه استفاده کنند.
  5. فایل‌های غیرتصویری برای ابزارهایی که می‌توانند آن‌ها را مدیریت کنند، به‌صورت metadata فایل یا ارجاع رسانه در دسترس می‌مانند.


### وراثت پیوست از ریشه thread

وقتی پیامی در یک thread وارد می‌شود (دارای والد `thread_ts` است):

  * اگر خود پاسخ رسانه مستقیم نداشته باشد و پیام ریشه شامل فایل باشد، Slack می‌تواند فایل‌های ریشه را به‌عنوان زمینه آغازگر thread hydrate کند.
  * پیوست‌های مستقیم پاسخ بر پیوست‌های پیام ریشه اولویت دارند.
  * پیام ریشه‌ای که فقط فایل دارد و متن ندارد، با یک placeholder پیوست نمایش داده می‌شود تا fallback همچنان بتواند فایل‌های آن را شامل شود.


### مدیریت چند پیوست

وقتی یک پیام Slack شامل چند پیوست فایل باشد:

  * هر پیوست به‌صورت مستقل از طریق pipeline رسانه پردازش می‌شود.
  * ارجاع‌های رسانه دانلودشده در زمینه پیام تجمیع می‌شوند.
  * ترتیب پردازش از ترتیب فایل‌های Slack در payload رویداد پیروی می‌کند.
  * شکست در دانلود یک پیوست، سایر پیوست‌ها را مسدود نمی‌کند.


### محدودیت‌های اندازه، دانلود و مدل

  * **سقف اندازه** : پیش‌فرض 20 MB برای هر فایل. از طریق `channels.slack.mediaMaxMb` قابل پیکربندی است.
  * **شکست‌های دانلود** : فایل‌هایی که Slack نمی‌تواند ارائه کند، URLهای منقضی‌شده، فایل‌های غیرقابل دسترس، فایل‌های بیش‌ازحد بزرگ، و پاسخ‌های HTML مربوط به احراز هویت/ورود Slack به‌جای گزارش شدن به‌عنوان قالب‌های پشتیبانی‌نشده، نادیده گرفته می‌شوند.
  * **مدل بینایی** : تحلیل تصویر وقتی مدل پاسخ فعال از بینایی پشتیبانی کند از همان مدل استفاده می‌کند، یا از مدل تصویر پیکربندی‌شده در `agents.defaults.imageModel`.


### محدودیت‌های شناخته‌شده

سناریو | رفتار فعلی | راهکار جایگزین  
---|---|---  
URL فایل Slack منقضی‌شده | فایل نادیده گرفته می‌شود؛ خطایی نمایش داده نمی‌شود | فایل را دوباره در Slack بارگذاری کنید  
مدل بینایی پیکربندی نشده است | پیوست‌های تصویر به‌عنوان ارجاع‌های رسانه ذخیره می‌شوند، اما به‌عنوان تصویر تحلیل نمی‌شوند | `agents.defaults.imageModel` را پیکربندی کنید یا از مدل پاسخ دارای قابلیت بینایی استفاده کنید  
تصاویر بسیار بزرگ (> 20 MB به‌صورت پیش‌فرض) | طبق سقف اندازه نادیده گرفته می‌شوند | اگر Slack اجازه می‌دهد، `channels.slack.mediaMaxMb` را افزایش دهید  
پیوست‌های forward/shared | متن و رسانه تصویر/فایل میزبانی‌شده در Slack به‌صورت بهترین تلاش پردازش می‌شوند | مستقیماً در thread مربوط به OpenClaw دوباره share کنید  
پیوست‌های PDF | به‌عنوان زمینه فایل/رسانه ذخیره می‌شوند، نه اینکه به‌طور خودکار از مسیر بینایی تصویر عبور داده شوند | برای metadata فایل از `download-file` یا برای تحلیل PDF از ابزار `pdf` استفاده کنید  
  
### مستندات مرتبط

  * [pipeline درک رسانه](</fa/nodes/media-understanding>)
  * [ابزار PDF](</fa/tools/pdf>)
  * Epic: [#51349](<https://github.com/openclaw/openclaw/issues/51349>) — فعال‌سازی بینایی پیوست‌های Slack
  * آزمون‌های regression: [#51353](<https://github.com/openclaw/openclaw/issues/51353>)
  * راستی‌آزمایی زنده: [#51354](<https://github.com/openclaw/openclaw/issues/51354>)


## مرتبط

[**Pairing** یک کاربر Slack را با Gateway جفت کنید. ](</fa/channels/pairing>) [**گروه‌ها** رفتار کانال و DM گروهی. ](</fa/channels/groups>) [**مسیریابی کانال** پیام‌های ورودی را به عامل‌ها مسیریابی کنید. ](</fa/channels/channel-routing>) [**امنیت** مدل تهدید و مقاوم‌سازی. ](</fa/gateway/security>) [**پیکربندی** چیدمان پیکربندی و تقدم. ](</fa/gateway/configuration>) [**دستورات اسلش** catalog دستور و رفتار. ](</fa/tools/slash-commands>)

Was this useful?YesNo