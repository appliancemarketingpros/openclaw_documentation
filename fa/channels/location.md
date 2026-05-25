---
title: تجزیه مکان کانال
source_url: https://docs.openclaw.ai/fa/channels/location
scraped_at: 2026-05-25
---

OpenClaw مکان‌های اشتراکی از کانال‌های چت را به این موارد عادی‌سازی می‌کند:

  * متن مختصر مختصات که به بدنه ورودی افزوده می‌شود، و
  * فیلدهای ساختاریافته در بار زمینه پاسخ خودکار. برچسب‌ها، نشانی‌ها و شرح‌ها/نظرهای ارائه‌شده توسط کانال، نه به‌صورت درون‌خطی در بدنه کاربر، بلکه توسط بلوک JSON فراداده نامطمئن مشترک در پرامپت رندر می‌شوند.


در حال حاضر پشتیبانی می‌شود:

  * **Telegram** (پین‌های مکان + مکان‌ها + مکان‌های زنده)
  * **WhatsApp** (locationMessage + liveLocationMessage)
  * **Matrix** (`m.location` با `geo_uri`)


## قالب‌بندی متن

مکان‌ها به‌صورت خط‌های خوانا و بدون براکت رندر می‌شوند:

  * پین: 
    * `📍 48.858844, 2.294351 ±12m`
  * مکان نام‌دار: 
    * `📍 48.858844, 2.294351 ±12m`
  * اشتراک‌گذاری زنده: 
    * `🛰 Live location: 48.858844, 2.294351 ±12m`


اگر کانال شامل برچسب، نشانی، یا شرح/نظر باشد، در بار زمینه حفظ می‌شود و در پرامپت به‌صورت JSON نامطمئن محصورشده ظاهر می‌شود:

textCopy code
[code]
    Location (untrusted metadata):```json{  "latitude": 48.858844,  "longitude": 2.294351,  "name": "Eiffel Tower",  "address": "Champ de Mars, Paris",  "caption": "Meet here"}```
[/code]

## فیلدهای زمینه

وقتی مکانی وجود داشته باشد، این فیلدها به `ctx` افزوده می‌شوند:

  * `LocationLat` (عدد)
  * `LocationLon` (عدد)
  * `LocationAccuracy` (عدد، متر؛ اختیاری)
  * `LocationName` (رشته؛ اختیاری)
  * `LocationAddress` (رشته؛ اختیاری)
  * `LocationSource` (`pin | place | live`)
  * `LocationIsLive` (بولی)
  * `LocationCaption` (رشته؛ اختیاری)


رندرکننده پرامپت، `LocationName`، `LocationAddress` و `LocationCaption` را به‌عنوان فراداده نامطمئن در نظر می‌گیرد و آن‌ها را از طریق همان مسیر JSON محدودشده‌ای سریال‌سازی می‌کند که برای سایر زمینه‌های کانال استفاده می‌شود.

## یادداشت‌های کانال

  * **Telegram** : مکان‌ها به `LocationName/LocationAddress` نگاشت می‌شوند؛ مکان‌های زنده از `live_period` استفاده می‌کنند.
  * **WhatsApp** : `locationMessage.comment` و `liveLocationMessage.caption` مقدار `LocationCaption` را پر می‌کنند.
  * **Matrix** : `geo_uri` به‌عنوان مکان پین‌شده تجزیه می‌شود؛ ارتفاع نادیده گرفته می‌شود و `LocationIsLive` همیشه false است.


## مرتبط

  * [دستور مکان (گره‌ها)](</fa/nodes/location-command>)
  * [ثبت تصویر با دوربین](</fa/nodes/camera>)
  * [درک رسانه](</fa/nodes/media-understanding>)


Was this useful?YesNo