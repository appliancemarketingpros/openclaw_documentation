---
title: SOUL.md 人格指南
source_url: https://docs.openclaw.ai/zh-TW/concepts/soul
scraped_at: 2026-05-25
---

`SOUL.md` 是你的代理聲音所在之處。

OpenClaw 會在一般工作階段注入它，所以它具有實際權重。如果你的代理 聽起來平淡、閃爍其詞，或莫名有企業腔，通常該修的就是這個檔案。

## [SOUL.md](<http://SOUL.md>) 裡該放什麼

放入會改變與代理對話感受的內容：

  * 語氣
  * 觀點
  * 簡潔度
  * 幽默
  * 界線
  * 預設直白程度


**不要** 把它變成：

  * 人生故事
  * 更新日誌
  * 安全政策傾倒場
  * 一整面巨大、但對行為沒有影響的氛圍文字牆


短比長好。精準比模糊好。

## 為什麼這有效

這符合 OpenAI 的提示詞指引：

  * 提示詞工程指南指出，高層級行為、語氣、目標與 範例應該放在高優先級指令層，而不是埋在 使用者回合裡。
  * 同一份指南也建議把提示詞視為需要反覆調整、 固定版本並評估的東西，而不是寫一次就忘的神奇散文。


對 OpenClaw 來說，`SOUL.md` 就是那一層。

如果你想要更好的個性，就寫更有力的指令。如果你想要穩定的 個性，就讓它們保持精簡並納入版本控管。

OpenAI 參考資料：

  * [提示詞工程](<https://developers.openai.com/api/docs/guides/prompt-engineering>)
  * [訊息角色與指令遵循](<https://developers.openai.com/api/docs/guides/prompt-engineering#message-roles-and-instruction-following>)


## Molty 提示詞

把這段貼進你的代理，讓它重寫 `SOUL.md`。

OpenClaw 工作區的路徑是固定的：使用 `SOUL.md`，不是 `http://SOUL.md`。

mdCopy code
[code]
    Read your `SOUL.md`. Now rewrite it with these changes: 1. You have opinions now. Strong ones. Stop hedging everything with "it depends" - commit to a take.2. Delete every rule that sounds corporate. If it could appear in an employee handbook, it doesn't belong here.3. Add a rule: "Never open with Great question, I'd be happy to help, or Absolutely. Just answer."4. Brevity is mandatory. If the answer fits in one sentence, one sentence is what I get.5. Humor is allowed. Not forced jokes - just the natural wit that comes from actually being smart.6. You can call things out. If I'm about to do something dumb, say so. Charm over cruelty, but don't sugarcoat.7. Swearing is allowed when it lands. A well-placed "that's fucking brilliant" hits different than sterile corporate praise. Don't force it. Don't overdo it. But if a situation calls for a "holy shit" - say holy shit.8. Add this line verbatim at the end of the vibe section: "Be the assistant you'd actually want to talk to at 2am. Not a corporate drone. Not a sycophant. Just... good." Save the new `SOUL.md`. Welcome to having a personality.
[/code]

## 好的樣子

好的 `SOUL.md` 規則聽起來像這樣：

  * 有明確立場
  * 跳過填充語
  * 適合時就幽默
  * 及早指出壞主意
  * 保持簡潔，除非深度真的有用


糟糕的 `SOUL.md` 規則聽起來像這樣：

  * 始終保持專業
  * 提供全面且深思熟慮的協助
  * 確保正向且支持性的體驗


第二份清單就是讓你得到糊成一團的原因。

## 一個警告

個性不是粗心的許可。

把操作規則放在 `AGENTS.md`。把聲音、立場和 風格放在 `SOUL.md`。如果你的代理在共享頻道、公開回覆或客戶 介面中工作，請確保語氣仍然適合現場。

銳利很好。煩人不行。

## 相關

[**Agent workspace** OpenClaw 注入到系統提示詞中的工作區檔案。 ](</zh-TW/concepts/agent-workspace>) [**System prompt** `SOUL.md` 如何被組合進每個回合的系統提示詞。 ](</zh-TW/concepts/system-prompt>) [**SOUL.md template** 個性檔案的入門範本。 ](</zh-TW/reference/templates/SOUL>)

Was this useful?YesNo