---
title: LongCat
source_url: https://docs.openclaw.ai/tr/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>), kodlama ve ajan tabanlı iş yükleri için geliştirilmiş bir akıl yürütme modeli olan LongCat-2.0 için barındırılan bir API sağlar. OpenClaw, LongCat'in OpenAI uyumlu uç noktası için resmi `longcat` Plugin'ini sağlar.

Özellik | Değer  
---|---  
Sağlayıcı | `longcat`  
Kimlik doğrulama | `LONGCAT_API_KEY`  
API | OpenAI uyumlu Chat Completions  
Temel URL | `https://api.longcat.chat/openai`  
Model | `longcat/LongCat-2.0`  
Bağlam | 1.048.576 token  
En fazla çıktı | 131.072 token  
Girdi | Metin  
  
## Plugin'i yükleme

Resmi paketi yükleyin, ardından Gateway'i yeniden başlatın:

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## Başlarken

* ### Bir API anahtarı oluşturun

[LongCat API Platformu](<https://longcat.chat/platform/>) üzerinde oturum açın ve [API Keys](<https://longcat.chat/platform/api_keys>) sayfasında bir anahtar oluşturun.

* ### İlk kurulumu çalıştırın

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### Modeli doğrulayın

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

İlk kurulum, barındırılan kataloğu ekler ve henüz birincil model yapılandırılmamışsa `longcat/LongCat-2.0` modelini seçer.

### Etkileşimsiz kurulum

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## Akıl yürütme davranışı

LongCat, ikili düşünme denetimi sunar. OpenClaw, etkin düşünme düzeylerini `thinking: { type: "enabled" }` değerine, `/think off` komutunu ise `thinking: { type: "disabled" }` değerine eşler. LongCat şu anda `reasoning_effort` özelliğini belgelemediğinden OpenClaw bunu göndermez.

LongCat, akıl yürütmeyi `reasoning_content` alanında döndürür. OpenClaw, çok turlu ajan oturumlarının sağlayıcının beklediği mesaj biçimini koruması için asistanın araç çağrısı turlarını yeniden oynatırken bu alanı muhafaza eder.

## Fiyatlandırma

Yerleşik katalog, LongCat'in milyon token başına ABD doları cinsinden kullandıkça öde liste fiyatlarını kullanır: önbelleğe alınmamış girdi 0,75 $, önbelleğe alınmış girdi 0,015 $ ve çıktı 2,95 $. LongCat geçici indirimler sunabilir; [fiyatlandırma sayfası](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) ve faturalandırma kayıtlarınız belirleyicidir.

## Kendi sunucunuzda barındırılan LongCat-2.0

`longcat` sağlayıcısı, LongCat'in barındırılan API'sini hedefler. [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>) üzerindeki açık ağırlıkları kullanmak için modeli OpenAI uyumlu bir çalışma zamanı aracılığıyla sunun ve bunun yerine OpenClaw'ın mevcut [vLLM](</tr/providers/vllm>) veya [SGLang](</tr/providers/sglang>) sağlayıcısını kullanın.

Çalışma zamanının tam model tanımlayıcısını kendi sunucunuzda barındırılan sağlayıcı kataloğunda tutun; yerel bir dağıtımı `longcat/LongCat-2.0` üzerinden yönlendirmeyin.

## Sorun giderme

Anahtar kabukta çalışıyor ancak Gateway'de çalışmıyor

Arka plan hizmeti tarafından yönetilen Gateway işlemleri, etkileşimli kabuktaki tüm değişkenleri devralmaz. `LONGCAT_API_KEY` değişkenini `~/.openclaw/.env` dosyasına ekleyin, ilk kurulum aracılığıyla yapılandırın veya onaylanmış bir gizli bilgi referansı kullanın.

İstekler 402 veya 429 hatasıyla başarısız oluyor

`402`, hesabın token kotasının yetersiz olduğu anlamına gelir. `429`, API anahtarının hız sınırına ulaştığı anlamına gelir. [LongCat kullanımını](<https://longcat.chat/platform/usage>) kontrol edin ve hız sınırına takılan istekleri sağlayıcının geri çekilme süresi sona erdikten sonra yeniden deneyin.

Model görünmüyor

`openclaw plugins list` komutunu çalıştırıp `longcat` Plugin'inin etkin olduğunu doğrulayın, ardından `openclaw models list --provider longcat` komutunu çalıştırın.

## İlgili içerikler

[**Model sağlayıcıları** Sağlayıcı yapılandırması, model referansları ve yük devretme davranışı. ](</tr/concepts/model-providers>) [**LongCat API belgeleri** Barındırılan API uç noktaları, kimlik doğrulama, sınırlar ve örnekler. ](<https://longcat.chat/platform/docs/>) [**LongCat-2.0 model kartı** Mimari, dağıtım rehberi ve model ayrıntıları. ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**Gizli bilgiler** Sağlayıcı kimlik bilgilerini yapılandırmaya düz metin olarak gömmeden saklayın. ](</tr/gateway/secrets>)

Was this useful?YesNo

Open issue