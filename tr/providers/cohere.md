---
title: Cohere
source_url: https://docs.openclaw.ai/tr/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>), Compatibility API aracılığıyla OpenAI uyumlu çıkarım sağlar. OpenClaw, dışsallaştırma geçişi sırasında Cohere sağlayıcısını paketli olarak sunar ve ayrıca Command A model kataloğuyla resmi bir harici Plugin olarak yayımlar.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `cohere`  
Plugin | geçiş sırasında paketli; resmi harici paket  
Kimlik doğrulama env var | `COHERE_API_KEY`  
Onboarding bayrağı | `--auth-choice cohere-api-key`  
Doğrudan CLI bayrağı | `--cohere-api-key <key>`  
API | OpenAI uyumlu (`openai-completions`)  
Temel URL | `https://api.cohere.ai/compatibility/v1`  
Varsayılan model | `cohere/command-a-03-2025`  
  
## Başlayın

  1. Cohere, mevcut OpenClaw paketlerine dahildir. Kullanılamıyorsa harici paketi kurun ve Gateway'i yeniden başlatın:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Bir Cohere API anahtarı oluşturun.
  3. Onboarding'i çalıştırın:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Kataloğun kullanılabilir olduğunu doğrulayın:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

Varsayılan model yalnızca birincil model zaten yapılandırılmamışsa ayarlanır.

## Yalnızca ortamla kurulum

`COHERE_API_KEY` değerini Gateway işlemi için kullanılabilir hale getirin, ardından Cohere modelini seçin:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## İlgili

  * [Model sağlayıcıları](</tr/concepts/model-providers>)
  * [Models CLI](</tr/cli/models>)
  * [Sağlayıcı dizini](</tr/providers>)


Was this useful?YesNo

Open issue