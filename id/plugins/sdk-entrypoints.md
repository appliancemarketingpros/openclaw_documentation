---
title: Titik masuk Plugin
source_url: https://docs.openclaw.ai/id/plugins/sdk-entrypoints
scraped_at: 2026-05-25
---

Setiap plugin mengekspor objek entri default. SDK menyediakan tiga helper untuk membuatnya.

Untuk plugin yang terpasang, `package.json` harus mengarahkan pemuatan runtime ke JavaScript yang sudah dibangun saat tersedia:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["./src/index.ts"],    "runtimeExtensions": ["./dist/index.js"],    "setupEntry": "./src/setup-entry.ts",    "runtimeSetupEntry": "./dist/setup-entry.js"  }}
[/code]

`extensions` dan `setupEntry` tetap valid sebagai entri sumber untuk pengembangan workspace dan git checkout. `runtimeExtensions` dan `runtimeSetupEntry` lebih disarankan saat OpenClaw memuat paket yang terpasang dan memungkinkan paket npm menghindari kompilasi TypeScript saat runtime. Entri runtime eksplisit wajib: `runtimeSetupEntry` memerlukan `setupEntry`, dan artefak `runtimeExtensions` atau `runtimeSetupEntry` yang hilang akan menggagalkan pemasangan/penemuan alih-alih diam-diam kembali ke sumber. Jika paket yang terpasang hanya mendeklarasikan entri sumber TypeScript, OpenClaw akan menggunakan peer `dist/*.js` hasil build yang sesuai saat ada, lalu kembali ke sumber TypeScript.

Semua jalur entri harus tetap berada di dalam direktori paket plugin. Entri runtime dan peer JavaScript hasil build yang disimpulkan tidak membuat jalur sumber `extensions` atau `setupEntry` yang keluar direktori menjadi valid.

## `definePluginEntry`

**Impor:** `openclaw/plugin-sdk/plugin-entry`

Untuk plugin provider, plugin tool, plugin hook, dan apa pun yang **bukan** channel pesan.

typescriptCopy code
[code]
     export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Short summary",  register(api) {    api.registerProvider({      /* ... */    });    api.registerTool({      /* ... */    });  },});
[/code]

Field | Type | Required | Default  
---|---|---|---  
`id` | `string` | Ya | -  
`name` | `string` | Ya | -  
`description` | `string` | Ya | -  
`kind` | `string` | Tidak | -  
`configSchema` | `OpenClawPluginConfigSchema | () => OpenClawPluginConfigSchema` | Tidak | Skema objek kosong  
`register` | `(api: OpenClawPluginApi) => void` | Ya | -  
  
  * `id` harus cocok dengan manifes `openclaw.plugin.json` Anda.
  * `kind` digunakan untuk slot eksklusif: `"memory"` atau `"context-engine"`.
  * `configSchema` dapat berupa fungsi untuk evaluasi lazy.
  * OpenClaw menyelesaikan dan mememoisasi skema tersebut pada akses pertama, sehingga pembangun skema yang mahal hanya berjalan sekali.


## `defineChannelPluginEntry`

**Impor:** `openclaw/plugin-sdk/channel-core`

Membungkus `definePluginEntry` dengan wiring khusus channel. Secara otomatis memanggil `api.registerChannel({ plugin })`, mengekspos seam metadata CLI bantuan root opsional, dan membatasi `registerFull` berdasarkan mode pendaftaran.

typescriptCopy code
[code]
     export default defineChannelPluginEntry({  id: "my-channel",  name: "My Channel",  description: "Short summary",  plugin: myChannelPlugin,  setRuntime: setMyRuntime,  registerCliMetadata(api) {    api.registerCli(/* ... */);  },  registerFull(api) {    api.registerGatewayMethod(/* ... */);  },});
[/code]

Field | Type | Required | Default  
---|---|---|---  
`id` | `string` | Ya | -  
`name` | `string` | Ya | -  
`description` | `string` | Ya | -  
`plugin` | `ChannelPlugin` | Ya | -  
`configSchema` | `OpenClawPluginConfigSchema | () => OpenClawPluginConfigSchema` | Tidak | Skema objek kosong  
`setRuntime` | `(runtime: PluginRuntime) => void` | Tidak | -  
`registerCliMetadata` | `(api: OpenClawPluginApi) => void` | Tidak | -  
`registerFull` | `(api: OpenClawPluginApi) => void` | Tidak | -  
  
  * `setRuntime` dipanggil selama pendaftaran sehingga Anda dapat menyimpan referensi runtime (biasanya melalui `createPluginRuntimeStore`). Ini dilewati selama pengambilan metadata CLI.
  * `registerCliMetadata` berjalan selama `api.registrationMode === "cli-metadata"`, `api.registrationMode === "discovery"`, dan `api.registrationMode === "full"`. Gunakan ini sebagai tempat kanonis untuk deskriptor CLI milik channel sehingga bantuan root tetap tidak mengaktifkan, snapshot penemuan menyertakan metadata perintah statis, dan pendaftaran perintah CLI normal tetap kompatibel dengan pemuatan plugin penuh.
  * Pendaftaran penemuan tidak mengaktifkan, bukan bebas impor. OpenClaw dapat mengevaluasi entri plugin tepercaya dan modul plugin channel untuk membangun snapshot, jadi jaga agar impor tingkat atas bebas efek samping dan tempatkan socket, klien, worker, dan layanan di balik jalur khusus `"full"`.
  * `registerFull` hanya berjalan saat `api.registrationMode === "full"`. Ini dilewati selama pemuatan khusus setup.
  * Seperti `definePluginEntry`, `configSchema` dapat berupa factory lazy dan OpenClaw mememoisasi skema yang diselesaikan pada akses pertama.
  * Untuk perintah CLI root milik plugin, pilih `api.registerCli(..., { descriptors: [...] })` saat Anda ingin perintah tetap dimuat secara lazy tanpa menghilang dari pohon parse CLI root. Untuk perintah fitur node berpasangan, pilih `api.registerNodeCliFeature(...)` agar perintah ditempatkan di bawah `openclaw nodes`. Untuk perintah plugin bersarang lainnya, tambahkan `parentPath` dan daftarkan perintah pada objek `program` yang diteruskan ke registrar; OpenClaw menyelesaikannya ke perintah induk sebelum memanggil plugin. Untuk plugin channel, pilih mendaftarkan deskriptor tersebut dari `registerCliMetadata(...)` dan jaga agar `registerFull(...)` fokus pada pekerjaan khusus runtime.
  * Jika `registerFull(...)` juga mendaftarkan metode RPC gateway, pertahankan pada prefiks khusus plugin. Namespace admin inti yang dicadangkan (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) selalu dipaksa menjadi `operator.admin`.


## `defineSetupPluginEntry`

**Impor:** `openclaw/plugin-sdk/channel-core`

Untuk file `setup-entry.ts` yang ringan. Mengembalikan hanya `{ plugin }` tanpa wiring runtime atau CLI.

typescriptCopy code
[code]
     export default defineSetupPluginEntry(myChannelPlugin);
[/code]

OpenClaw memuat ini alih-alih entri penuh saat channel dinonaktifkan, belum dikonfigurasi, atau saat pemuatan tertunda diaktifkan. Lihat [Setup dan Konfigurasi](</id/plugins/sdk-setup#setup-entry>) untuk kapan ini penting.

Dalam praktiknya, pasangkan `defineSetupPluginEntry(...)` dengan keluarga helper setup yang sempit:

  * `openclaw/plugin-sdk/setup-runtime` untuk helper setup yang aman runtime seperti adapter patch setup yang aman impor, output lookup-note, `promptResolvedAllowFrom`, `splitSetupEntries`, dan proxy setup yang didelegasikan
  * `openclaw/plugin-sdk/channel-setup` untuk surface setup pemasangan opsional
  * `openclaw/plugin-sdk/setup-tools` untuk helper setup/install CLI/archive/docs


Simpan SDK berat, pendaftaran CLI, dan layanan runtime berumur panjang di entri penuh.

Channel workspace bawaan yang memisahkan surface setup dan runtime dapat menggunakan `defineBundledChannelSetupEntry(...)` dari `openclaw/plugin-sdk/channel-entry-contract` sebagai gantinya. Kontrak tersebut memungkinkan entri setup mempertahankan ekspor plugin/secret yang aman untuk setup sekaligus tetap mengekspos setter runtime:

typescriptCopy code
[code]
     export default defineBundledChannelSetupEntry({  importMetaUrl: import.meta.url,  plugin: {    specifier: "./channel-plugin-api.js",    exportName: "myChannelPlugin",  },  runtime: {    specifier: "./runtime-api.js",    exportName: "setMyChannelRuntime",  },});
[/code]

Gunakan kontrak bawaan tersebut hanya saat alur setup benar-benar memerlukan setter runtime yang ringan sebelum entri channel penuh dimuat.

## Mode pendaftaran

`api.registrationMode` memberi tahu plugin Anda bagaimana ia dimuat:

Mode | Kapan | Apa yang didaftarkan  
---|---|---  
`"full"` | Startup gateway normal | Semuanya  
`"discovery"` | Penemuan kapabilitas baca-saja | Pendaftaran channel plus deskriptor CLI statis; kode entri dapat dimuat, tetapi lewati socket, worker, klien, dan layanan  
`"setup-only"` | Channel dinonaktifkan/belum dikonfigurasi | Hanya pendaftaran channel  
`"setup-runtime"` | Alur setup dengan runtime tersedia | Pendaftaran channel plus hanya runtime ringan yang diperlukan sebelum entri penuh dimuat  
`"cli-metadata"` | Bantuan root / pengambilan metadata CLI | Hanya deskriptor CLI  
  
`defineChannelPluginEntry` menangani pemisahan ini secara otomatis. Jika Anda menggunakan `definePluginEntry` langsung untuk channel, periksa sendiri modenya:

typescriptCopy code
[code]
    register(api) {  if (    api.registrationMode === "cli-metadata" ||    api.registrationMode === "discovery" ||    api.registrationMode === "full"  ) {    api.registerCli(/* ... */);    if (api.registrationMode === "cli-metadata") return;  }   api.registerChannel({ plugin: myPlugin });  if (api.registrationMode !== "full") return;   // Heavy runtime-only registrations  api.registerService(/* ... */);}
[/code]

Mode penemuan membangun snapshot registry yang tidak mengaktifkan. Mode ini tetap dapat mengevaluasi entri plugin dan objek plugin channel agar OpenClaw dapat mendaftarkan kapabilitas channel dan deskriptor CLI statis. Perlakukan evaluasi modul dalam penemuan sebagai tepercaya tetapi ringan: tidak ada klien jaringan, subprocess, listener, koneksi database, worker latar belakang, pembacaan kredensial, atau efek samping runtime hidup lainnya di tingkat atas.

Perlakukan `"setup-runtime"` sebagai jendela ketika surface startup khusus setup harus ada tanpa masuk kembali ke runtime channel bawaan penuh. Kecocokan yang baik adalah pendaftaran channel, route HTTP yang aman untuk setup, metode gateway yang aman untuk setup, dan helper setup yang didelegasikan. Layanan latar belakang berat, registrar CLI, dan bootstrap SDK provider/klien tetap berada di `"full"`.

Khusus untuk registrar CLI:

  * gunakan `descriptors` saat registrar memiliki satu atau beberapa perintah root dan Anda ingin OpenClaw memuat lambat modul CLI asli pada pemanggilan pertama
  * pastikan descriptor tersebut mencakup setiap root perintah tingkat atas yang diekspos oleh registrar
  * batasi nama perintah descriptor pada huruf, angka, tanda hubung, dan garis bawah, dimulai dengan huruf atau angka; OpenClaw menolak nama descriptor di luar bentuk tersebut dan menghapus urutan kontrol terminal dari deskripsi sebelum merender bantuan
  * gunakan `commands` saja hanya untuk jalur kompatibilitas eager


## Bentuk Plugin

OpenClaw mengklasifikasikan plugin yang dimuat berdasarkan perilaku pendaftarannya:

Bentuk | Deskripsi  
---|---  
**plain-capability** | Satu jenis kapabilitas (mis. hanya provider)  
**hybrid-capability** | Beberapa jenis kapabilitas (mis. provider + speech)  
**hook-only** | Hanya hook, tanpa kapabilitas  
**non-capability** | Alat/perintah/layanan tetapi tanpa kapabilitas  
  
Gunakan `openclaw plugins inspect <id>` untuk melihat bentuk sebuah plugin.

## Terkait

  * [Ikhtisar SDK](</id/plugins/sdk-overview>) \- API pendaftaran dan referensi subpath
  * [Pembantu Runtime](</id/plugins/sdk-runtime>) \- `api.runtime` dan `createPluginRuntimeStore`
  * [Penyiapan dan Konfigurasi](</id/plugins/sdk-setup>) \- manifest, entri penyiapan, pemuatan tertunda
  * [Plugin Channel](</id/plugins/sdk-channel-plugins>) \- membangun objek `ChannelPlugin`
  * [Plugin Provider](</id/plugins/sdk-provider-plugins>) \- pendaftaran provider dan hook


Was this useful?YesNo