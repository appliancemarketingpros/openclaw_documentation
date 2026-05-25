---
title: macOS izinleri
source_url: https://docs.openclaw.ai/tr/platforms/mac/permissions
scraped_at: 2026-05-25
---

macOS izinleri kırılgandır. TCC bir izin onayını uygulamanın kod imzası, bundle tanımlayıcısı ve disk üzerindeki yolu ile ilişkilendirir. Bunlardan herhangi biri değişirse macOS uygulamayı yeni kabul eder ve istemleri düşürebilir veya gizleyebilir.

## Kalıcı izinler için gereksinimler

  * Aynı yol: uygulamayı sabit bir konumdan çalıştırın (OpenClaw için `dist/OpenClaw.app`).
  * Aynı bundle tanımlayıcısı: bundle ID'yi değiştirmek yeni bir izin kimliği oluşturur.
  * İmzalı uygulama: imzasız veya ad-hoc imzalı yapılar izinleri kalıcı tutmaz.
  * Tutarlı imza: imzanın yeniden derlemeler arasında kararlı kalması için gerçek bir Apple Development veya Developer ID sertifikası kullanın.


Ad-hoc imzalar her derlemede yeni bir kimlik üretir. macOS önceki izinleri unutur ve eski girdiler temizlenene kadar istemler tamamen kaybolabilir.

## İstemler kaybolduğunda kurtarma kontrol listesi

  1. Uygulamayı kapatın.
  2. System Settings -> Privacy & Security içinde uygulama girdisini kaldırın.
  3. Uygulamayı aynı yoldan yeniden başlatın ve izinleri tekrar verin.
  4. İstem hâlâ görünmüyorsa `tccutil` ile TCC girdilerini sıfırlayın ve yeniden deneyin.
  5. Bazı izinler yalnızca tam bir macOS yeniden başlatmasından sonra yeniden görünür.


Örnek sıfırlamalar (gerekirse bundle ID'yi değiştirin):

bashCopy code
[code]
    sudo tccutil reset Accessibility ai.openclaw.macsudo tccutil reset ScreenCapture ai.openclaw.macsudo tccutil reset AppleEvents
[/code]

## Dosyalar ve klasörler izinleri (Desktop/Documents/Downloads)

macOS, terminal/arka plan süreçleri için Desktop, Documents ve Downloads dizinlerini de geçitleyebilir. Dosya okumaları veya dizin listelemeleri takılıyorsa, dosya işlemlerini gerçekleştiren aynı süreç bağlamına erişim verin (örneğin Terminal/iTerm, LaunchAgent ile başlatılan uygulama veya SSH süreci).

Geçici çözüm: klasör başına izinlerden kaçınmak istiyorsanız dosyaları OpenClaw çalışma alanına (`~/.openclaw/workspace`) taşıyın.

İzinleri test ediyorsanız her zaman gerçek bir sertifikayla imzalayın. Ad-hoc yapılar yalnızca izinlerin önemli olmadığı hızlı yerel çalıştırmalar için kabul edilebilir.

## İlgili

  * [macOS uygulaması](</tr/platforms/macos>)
  * [macOS imzalama](</tr/platforms/mac/signing>)


Was this useful?YesNo