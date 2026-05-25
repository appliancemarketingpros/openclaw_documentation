---
title: Ollama web araması
source_url: https://docs.openclaw.ai/tr/tools/ollama-search
scraped_at: 2026-05-25
---

OpenClaw, paketle birlikte gelen bir `web_search` sağlayıcısı olarak **Ollama Web Search** desteği sunar. Ollama'nın web arama API'sini kullanır ve başlıklar, URL'ler ve parçacıklar içeren yapılandırılmış sonuçlar döndürür.

Yerel veya kendi barındırdığınız Ollama için bu kurulum varsayılan olarak API anahtarı gerektirmez. Şunları gerektirir:

  * OpenClaw tarafından erişilebilen bir Ollama ana makinesi
  * `ollama signin`


Doğrudan barındırılan arama için Ollama sağlayıcısının temel URL'sini `https://ollama.com` olarak ayarlayın ve gerçek bir `OLLAMA_API_KEY` sağlayın.

## Kurulum

* ### Start Ollama

Ollama'nın yüklü ve çalışır durumda olduğundan emin olun.

* ### Sign in

Çalıştırın:

bashCopy code
[code]
    ollama signin
[/code]

* ### Choose Ollama Web Search

Çalıştırın:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Ardından sağlayıcı olarak **Ollama Web Search** seçeneğini seçin.

Ollama'yı modeller için zaten kullanıyorsanız, Ollama Web Search aynı yapılandırılmış ana makineyi yeniden kullanır.

## Yapılandırma

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

İsteğe bağlı Ollama ana makinesi geçersiz kılma:

json5Copy code
[code]
    {  plugins: {    entries: {      ollama: {        config: {          webSearch: {            baseUrl: "http://ollama-host:11434",          },        },      },    },  },}
[/code]

Ollama'yı zaten bir model sağlayıcısı olarak yapılandırıyorsanız, web arama sağlayıcısı bunun yerine o ana makineyi yeniden kullanabilir:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",      },    },  },}
[/code]

Ollama model sağlayıcısı, standart anahtar olarak `baseUrl` kullanır. Web arama sağlayıcısı, OpenAI SDK tarzı yapılandırma örnekleriyle uyumluluk için `models.providers.ollama` üzerindeki `baseURL` değerini de dikkate alır.

Açık bir Ollama temel URL'si ayarlanmamışsa OpenClaw `http://127.0.0.1:11434` kullanır.

Ollama ana makineniz bearer kimlik doğrulaması bekliyorsa OpenClaw, yapılandırılmış ana makineye yapılan istekler için `models.providers.ollama.apiKey` değerini (veya eşleşen ortam destekli sağlayıcı kimlik doğrulamasını) yeniden kullanır.

Doğrudan barındırılan Ollama Web Search:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",      },    },  },  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

## Notlar

  * Bu sağlayıcı için web aramaya özel bir API anahtarı alanı gerekmez.
  * Ollama ana makinesi kimlik doğrulamasıyla korunuyorsa OpenClaw, varsa normal Ollama sağlayıcısı API anahtarını yeniden kullanır.
  * `baseUrl` `https://ollama.com` ise OpenClaw doğrudan `https://ollama.com/api/web_search` çağırır ve yapılandırılmış Ollama API anahtarını bearer kimlik doğrulaması olarak gönderir.
  * Yapılandırılmış ana makine web aramayı sunmuyorsa ve `OLLAMA_API_KEY` ayarlanmışsa OpenClaw, bu ortam anahtarını yerel ana makineye göndermeden `https://ollama.com/api/web_search` adresine geri dönebilir.
  * OpenClaw, kurulum sırasında Ollama'ya erişilemiyorsa veya oturum açılmamışsa uyarı verir, ancak seçimi engellemez.
  * Çalışma zamanı otomatik algılama, daha yüksek öncelikli kimlik bilgili bir sağlayıcı yapılandırılmamışsa Ollama Web Search'e geri dönebilir.
  * Yerel Ollama daemon ana makineleri, Ollama Cloud'a imzalayıp ileten yerel proxy uç noktası `/api/experimental/web_search` kullanır.
  * `https://ollama.com` ana makineleri, bearer API anahtarı kimlik doğrulamasıyla doğrudan genel barındırılan uç nokta `/api/web_search` kullanır.


## İlgili

  * [Web Search genel bakış](</tr/tools/web>) \-- tüm sağlayıcılar ve otomatik algılama
  * [Ollama](</tr/providers/ollama>) \-- Ollama model kurulumu ve bulut/yerel modlar


Was this useful?YesNo