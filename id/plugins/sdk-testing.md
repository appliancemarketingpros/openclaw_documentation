---
title: Pengujian Plugin
source_url: https://docs.openclaw.ai/id/plugins/sdk-testing
scraped_at: 2026-05-25
---

Referensi untuk utilitas pengujian, pola, dan penegakan lint untuk Plugin OpenClaw.

## Utilitas pengujian

Subjalur pembantu pengujian ini adalah entrypoint sumber lokal repo untuk pengujian Plugin bawaan OpenClaw sendiri. Ini bukan ekspor paket untuk Plugin pihak ketiga.

**Impor mock API Plugin:** `openclaw/plugin-sdk/plugin-test-api`

**Impor kontrak runtime agen:** `openclaw/plugin-sdk/agent-runtime-test-contracts`

**Impor kontrak saluran:** `openclaw/plugin-sdk/channel-contract-testing`

**Impor pembantu pengujian saluran:** `openclaw/plugin-sdk/channel-test-helpers`

**Impor pengujian target saluran:** `openclaw/plugin-sdk/channel-target-testing`

**Impor kontrak Plugin:** `openclaw/plugin-sdk/plugin-test-contracts`

**Impor pengujian runtime Plugin:** `openclaw/plugin-sdk/plugin-test-runtime`

**Impor kontrak penyedia:** `openclaw/plugin-sdk/provider-test-contracts`

**Impor mock HTTP penyedia:** `openclaw/plugin-sdk/provider-http-test-mocks`

**Impor pengujian lingkungan/jaringan:** `openclaw/plugin-sdk/test-env`

**Impor fixture generik:** `openclaw/plugin-sdk/test-fixtures`

**Impor mock bawaan Node:** `openclaw/plugin-sdk/test-node-mocks`

Utamakan subjalur terfokus di bawah ini untuk pengujian Plugin baru. Barrel luas `openclaw/plugin-sdk/testing` hanya untuk kompatibilitas lama. Guardrail repo menolak impor nyata baru dari `plugin-sdk/testing` dan `plugin-sdk/test-utils`; nama-nama tersebut tetap ada hanya sebagai permukaan kompatibilitas usang untuk pengujian catatan kompatibilitas.

typescriptCopy code
[code]
       shouldAckReaction,  removeAckReactionAfterReply,} from "openclaw/plugin-sdk/channel-feedback";             bundledPluginRoot,  createCliRuntimeCapture,  typedCases,} from "openclaw/plugin-sdk/test-fixtures"; 
[/code]

### Ekspor yang tersedia

Ekspor | Tujuan  
---|---  
`createTestPluginApi` | Membuat tiruan API Plugin minimal untuk uji unit registrasi langsung. Impor dari `plugin-sdk/plugin-test-api`  
`AUTH_PROFILE_RUNTIME_CONTRACT` | Fixture kontrak profil auth bersama untuk adapter runtime agen native. Impor dari `plugin-sdk/agent-runtime-test-contracts`  
`DELIVERY_NO_REPLY_RUNTIME_CONTRACT` | Fixture kontrak supresi pengiriman bersama untuk adapter runtime agen native. Impor dari `plugin-sdk/agent-runtime-test-contracts`  
`OUTCOME_FALLBACK_RUNTIME_CONTRACT` | Fixture kontrak klasifikasi fallback bersama untuk adapter runtime agen native. Impor dari `plugin-sdk/agent-runtime-test-contracts`  
`createParameterFreeTool` | Membuat fixture skema alat dinamis untuk uji kontrak runtime native. Impor dari `plugin-sdk/agent-runtime-test-contracts`  
`expectChannelInboundContextContract` | Memastikan bentuk konteks masuk kanal. Impor dari `plugin-sdk/channel-contract-testing`  
`installChannelOutboundPayloadContractSuite` | Memasang kasus kontrak payload keluar kanal. Impor dari `plugin-sdk/channel-contract-testing`  
`createStartAccountContext` | Membuat konteks siklus hidup akun kanal. Impor dari `plugin-sdk/channel-test-helpers`  
`installChannelActionsContractSuite` | Memasang kasus kontrak aksi pesan kanal generik. Impor dari `plugin-sdk/channel-test-helpers`  
`installChannelSetupContractSuite` | Memasang kasus kontrak penyiapan kanal generik. Impor dari `plugin-sdk/channel-test-helpers`  
`installChannelStatusContractSuite` | Memasang kasus kontrak status kanal generik. Impor dari `plugin-sdk/channel-test-helpers`  
`expectDirectoryIds` | Memastikan id direktori kanal dari fungsi daftar direktori. Impor dari `plugin-sdk/channel-test-helpers`  
`assertBundledChannelEntries` | Memastikan entrypoint kanal terbundel mengekspos kontrak publik yang diharapkan. Impor dari `plugin-sdk/channel-test-helpers`  
`formatEnvelopeTimestamp` | Memformat stempel waktu envelope deterministik. Impor dari `plugin-sdk/channel-test-helpers`  
`expectPairingReplyText` | Memastikan teks balasan pairing kanal dan mengekstrak kodenya. Impor dari `plugin-sdk/channel-test-helpers`  
`describePluginRegistrationContract` | Memasang pemeriksaan kontrak registrasi Plugin. Impor dari `plugin-sdk/plugin-test-contracts`  
`registerSingleProviderPlugin` | Mendaftarkan satu Plugin penyedia dalam uji asap loader. Impor dari `plugin-sdk/plugin-test-runtime`  
`registerProviderPlugin` | Menangkap semua jenis penyedia dari satu Plugin. Impor dari `plugin-sdk/plugin-test-runtime`  
`registerProviderPlugins` | Menangkap registrasi penyedia di beberapa Plugin. Impor dari `plugin-sdk/plugin-test-runtime`  
`requireRegisteredProvider` | Memastikan koleksi penyedia berisi sebuah id. Impor dari `plugin-sdk/plugin-test-runtime`  
`createRuntimeEnv` | Membuat lingkungan runtime CLI/Plugin tiruan. Impor dari `plugin-sdk/plugin-test-runtime`  
`createPluginSetupWizardStatus` | Membuat helper status penyiapan untuk Plugin kanal. Impor dari `plugin-sdk/plugin-test-runtime`  
`describeOpenAIProviderRuntimeContract` | Memasang pemeriksaan kontrak runtime keluarga penyedia. Impor dari `plugin-sdk/provider-test-contracts`  
`expectPassthroughReplayPolicy` | Memastikan kebijakan replay penyedia meneruskan alat dan metadata milik penyedia. Impor dari `plugin-sdk/provider-test-contracts`  
`runRealtimeSttLiveTest` | Menjalankan uji langsung penyedia STT realtime dengan fixture audio bersama. Impor dari `plugin-sdk/provider-test-contracts`  
`normalizeTranscriptForMatch` | Menormalkan keluaran transkrip langsung sebelum asersi fuzzy. Impor dari `plugin-sdk/provider-test-contracts`  
`expectExplicitVideoGenerationCapabilities` | Memastikan penyedia video mendeklarasikan kemampuan mode pembuatan eksplisit. Impor dari `plugin-sdk/provider-test-contracts`  
`expectExplicitMusicGenerationCapabilities` | Memastikan penyedia musik mendeklarasikan kemampuan pembuatan/pengeditan eksplisit. Impor dari `plugin-sdk/provider-test-contracts`  
`mockSuccessfulDashscopeVideoTask` | Memasang respons tugas video kompatibel DashScope yang berhasil. Impor dari `plugin-sdk/provider-test-contracts`  
`getProviderHttpMocks` | Mengakses tiruan HTTP/auth Vitest penyedia yang ikut-serta. Impor dari `plugin-sdk/provider-http-test-mocks`  
`installProviderHttpMockCleanup` | Mereset tiruan HTTP/auth penyedia setelah setiap pengujian. Impor dari `plugin-sdk/provider-http-test-mocks`  
`installCommonResolveTargetErrorCases` | Kasus uji bersama untuk penanganan kesalahan resolusi target. Impor dari `plugin-sdk/channel-target-testing`  
`shouldAckReaction` | Memeriksa apakah kanal harus menambahkan reaksi ack. Impor dari `plugin-sdk/channel-feedback`  
`removeAckReactionAfterReply` | Menghapus reaksi ack setelah pengiriman balasan. Impor dari `plugin-sdk/channel-feedback`  
`createTestRegistry` | Membuat fixture registry Plugin kanal. Impor dari `plugin-sdk/plugin-test-runtime` atau `plugin-sdk/channel-test-helpers`  
`createEmptyPluginRegistry` | Membuat fixture registry Plugin kosong. Impor dari `plugin-sdk/plugin-test-runtime` atau `plugin-sdk/channel-test-helpers`  
`setActivePluginRegistry` | Memasang fixture registry untuk uji runtime Plugin. Impor dari `plugin-sdk/plugin-test-runtime` atau `plugin-sdk/channel-test-helpers`  
`createRequestCaptureJsonFetch` | Menangkap permintaan fetch JSON dalam uji helper media. Impor dari `plugin-sdk/test-env`  
`withServer` | Menjalankan pengujian terhadap server HTTP lokal sekali pakai. Impor dari `plugin-sdk/test-env`  
`createMockIncomingRequest` | Membuat objek permintaan HTTP masuk minimal. Impor dari `plugin-sdk/test-env`  
`withFetchPreconnect` | Menjalankan uji fetch dengan hook preconnect terpasang. Impor dari `plugin-sdk/test-env`  
`withEnv` / `withEnvAsync` | Menambal variabel lingkungan sementara. Impor dari `plugin-sdk/test-env`  
`createTempHomeEnv` / `withTempHome` / `withTempDir` | Membuat fixture uji sistem berkas terisolasi. Impor dari `plugin-sdk/test-env`  
`createMockServerResponse` | Membuat tiruan respons server HTTP minimal. Impor dari `plugin-sdk/test-env`  
`createCliRuntimeCapture` | Menangkap keluaran runtime CLI dalam pengujian. Impor dari `plugin-sdk/test-fixtures`  
`importFreshModule` | Mengimpor modul ESM dengan token kueri baru untuk melewati cache modul. Impor dari `plugin-sdk/test-fixtures`  
`bundledPluginRoot` / `bundledPluginFile` | Menyelesaikan path fixture sumber atau dist Plugin terbundel. Impor dari `plugin-sdk/test-fixtures`  
`mockNodeBuiltinModule` | Memasang tiruan Vitest bawaan Node yang sempit. Impor dari `plugin-sdk/test-node-mocks`  
`createSandboxTestContext` | Membuat konteks uji sandbox. Impor dari `plugin-sdk/test-fixtures`  
`writeSkill` | Menulis fixture skill. Impor dari `plugin-sdk/test-fixtures`  
`makeAgentAssistantMessage` | Membuat fixture pesan transkrip agen. Impor dari `plugin-sdk/test-fixtures`  
`peekSystemEvents` / `resetSystemEventsForTest` | Memeriksa dan mereset fixture peristiwa sistem. Impor dari `plugin-sdk/test-fixtures`  
`sanitizeTerminalText` | Membersihkan keluaran terminal untuk asersi. Impor dari `plugin-sdk/test-fixtures`  
`countLines` / `hasBalancedFences` | Memastikan bentuk keluaran chunking. Impor dari `plugin-sdk/test-fixtures`  
`runProviderCatalog` | Menjalankan hook katalog penyedia dengan dependensi uji  
`resolveProviderWizardOptions` | Menyelesaikan pilihan wizard penyiapan penyedia dalam uji kontrak  
`resolveProviderModelPickerEntries` | Menyelesaikan entri pemilih model penyedia dalam uji kontrak  
`buildProviderPluginMethodChoice` | Membuat id pilihan wizard penyedia untuk asersi  
`setProviderWizardProvidersResolverForTest` | Menyuntikkan penyedia wizard penyedia untuk pengujian terisolasi  
`createProviderUsageFetch` | Membangun fixture fetch penggunaan penyedia  
`useFrozenTime` / `useRealTime` | Membekukan dan memulihkan timer untuk pengujian yang sensitif terhadap waktu. Impor dari `plugin-sdk/test-env`  
`createTestWizardPrompter` | Membangun prompter wizard penyiapan tiruan  
`createRuntimeTaskFlow` | Membuat status alur tugas runtime yang terisolasi  
`typedCases` | Mempertahankan tipe literal untuk pengujian berbasis tabel. Impor dari `plugin-sdk/test-fixtures`  
  
Suite kontrak plugin bawaan juga menggunakan subpath pengujian SDK untuk helper fixture registri khusus tes, manifes, artefak publik, dan runtime. Suite khusus core yang bergantung pada inventaris OpenClaw bawaan tetap berada di `src/plugins/contracts`. Tempatkan tes ekstensi baru pada subpath SDK terfokus yang terdokumentasi seperti `plugin-sdk/plugin-test-api`, `plugin-sdk/channel-contract-testing`, `plugin-sdk/agent-runtime-test-contracts`, `plugin-sdk/channel-test-helpers`, `plugin-sdk/plugin-test-contracts`, `plugin-sdk/plugin-test-runtime`, `plugin-sdk/provider-test-contracts`, `plugin-sdk/provider-http-test-mocks`, `plugin-sdk/test-env`, atau `plugin-sdk/test-fixtures`, alih-alih mengimpor barrel kompatibilitas `plugin-sdk/testing` yang luas, file repo `src/**`, atau bridge repo `test/helpers/*` secara langsung.

### Tipe

Subpath pengujian terfokus juga mengekspor ulang tipe yang berguna dalam file tes:

typescriptCopy code
[code]
       ChannelAccountSnapshot,  ChannelGatewayContext,} from "openclaw/plugin-sdk/channel-contract";  
[/code]

## Menguji resolusi target

Gunakan `installCommonResolveTargetErrorCases` untuk menambahkan kasus galat standar untuk resolusi target channel:

typescriptCopy code
[code]
      describe("my-channel target resolution", () => {  installCommonResolveTargetErrorCases({    resolveTarget: ({ to, mode, allowFrom }) => {      // Your channel's target resolution logic      return myChannelResolveTarget({ to, mode, allowFrom });    },    implicitAllowFrom: ["user1", "user2"],  });   // Add channel-specific test cases  it("should resolve @username targets", () => {    // ...  });});
[/code]

## Pola pengujian

### Menguji kontrak pendaftaran

Tes unit yang meneruskan mock `api` buatan tangan ke `register(api)` tidak menguji gerbang penerimaan loader OpenClaw. Tambahkan setidaknya satu tes smoke berbasis loader untuk setiap permukaan pendaftaran yang diandalkan plugin Anda, terutama hook dan kapabilitas eksklusif seperti memory.

Loader sebenarnya menggagalkan pendaftaran plugin ketika metadata wajib hilang atau plugin memanggil API kapabilitas yang tidak dimilikinya. Misalnya, `api.registerHook(...)` memerlukan nama hook, dan `api.registerMemoryCapability(...)` mengharuskan manifes plugin atau entri yang diekspor mendeklarasikan `kind: "memory"`.

### Menguji akses konfigurasi runtime

Utamakan mock runtime plugin bersama dari `openclaw/plugin-sdk/channel-test-helpers` saat menguji plugin channel bawaan. Mock `runtime.config.loadConfig()` dan `runtime.config.writeConfigFile(...)` yang sudah usang melempar galat secara default agar tes menangkap penggunaan baru API kompatibilitas. Timpa mock tersebut hanya ketika tes secara eksplisit mencakup perilaku kompatibilitas lama.

### Pengujian unit plugin channel

typescriptCopy code
[code]
     describe("my-channel plugin", () => {  it("should resolve account from config", () => {    const cfg = {      channels: {        "my-channel": {          token: "test-token",          allowFrom: ["user1"],        },      },    };     const account = myPlugin.setup.resolveAccount(cfg, undefined);    expect(account.token).toBe("test-token");  });   it("should inspect account without materializing secrets", () => {    const cfg = {      channels: {        "my-channel": { token: "test-token" },      },    };     const inspection = myPlugin.setup.inspectAccount(cfg, undefined);    expect(inspection.configured).toBe(true);    expect(inspection.tokenStatus).toBe("available");    // No token value exposed    expect(inspection).not.toHaveProperty("token");  });});
[/code]

### Pengujian unit plugin provider

typescriptCopy code
[code]
     describe("my-provider plugin", () => {  it("should resolve dynamic models", () => {    const model = myProvider.resolveDynamicModel({      modelId: "custom-model-v2",      // ... context    });     expect(model.id).toBe("custom-model-v2");    expect(model.provider).toBe("my-provider");    expect(model.api).toBe("openai-completions");  });   it("should return catalog when API key is available", async () => {    const result = await myProvider.catalog.run({      resolveProviderApiKey: () => ({ apiKey: "test-key" }),      // ... context    });     expect(result?.provider?.models).toHaveLength(2);  });});
[/code]

### Mem-mock runtime plugin

Untuk kode yang menggunakan `createPluginRuntimeStore`, mock runtime dalam tes:

typescriptCopy code
[code]
      const store = createPluginRuntimeStore&lt;PluginRuntime&gt;({  pluginId: "test-plugin",  errorMessage: "test runtime not set",}); // In test setupconst mockRuntime = {  agent: {    resolveAgentDir: vi.fn().mockReturnValue("/tmp/agent"),    // ... other mocks  },  config: {    current: vi.fn(() => ({}) as const),    mutateConfigFile: vi.fn(),    replaceConfigFile: vi.fn(),  },  // ... other namespaces} as unknown as PluginRuntime; store.setRuntime(mockRuntime); // After testsstore.clearRuntime();
[/code]

### Menguji dengan stub per instans

Utamakan stub per instans dibanding mutasi prototipe:

typescriptCopy code
[code]
    // Preferred: per-instance stubconst client = new MyChannelClient();client.sendMessage = vi.fn().mockResolvedValue({ id: "msg-1" }); // Avoid: prototype mutation// MyChannelClient.prototype.sendMessage = vi.fn();
[/code]

## Tes kontrak (plugin dalam repo)

Plugin bawaan memiliki tes kontrak yang memverifikasi kepemilikan pendaftaran:

bashCopy code
[code]
    pnpm test -- src/plugins/contracts/
[/code]

Tes ini menegaskan:

  * Plugin mana yang mendaftarkan provider mana
  * Plugin mana yang mendaftarkan provider ucapan mana
  * Ketepatan bentuk pendaftaran
  * Kepatuhan kontrak runtime


### Menjalankan tes berscope

Untuk plugin tertentu:

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-channel/
[/code]

Untuk tes kontrak saja:

bashCopy code
[code]
    pnpm test -- src/plugins/contracts/shape.contract.test.tspnpm test -- src/plugins/contracts/auth-choice.contract.test.tspnpm test -- src/plugins/contracts/runtime-seams.contract.test.ts
[/code]

## Penegakan lint (plugin dalam repo)

Tiga aturan ditegakkan oleh `pnpm check` untuk plugin dalam repo:

  1. **Tidak ada impor root monolitik** \-- barrel root `openclaw/plugin-sdk` ditolak
  2. **Tidak ada impor`src/` langsung** \-- plugin tidak dapat mengimpor `../../src/` secara langsung
  3. **Tidak ada impor diri sendiri** \-- plugin tidak dapat mengimpor subpath `plugin-sdk/<name>` miliknya sendiri


Plugin eksternal tidak tunduk pada aturan lint ini, tetapi mengikuti pola yang sama direkomendasikan.

## Konfigurasi tes

OpenClaw menggunakan Vitest dengan ambang coverage V8. Untuk tes plugin:

bashCopy code
[code]
    # Run all testspnpm test # Run specific plugin testspnpm test -- <bundled-plugin-root>/my-channel/src/channel.test.ts # Run with a specific test name filterpnpm test -- <bundled-plugin-root>/my-channel/ -t "resolves account" # Run with coveragepnpm test:coverage
[/code]

Jika eksekusi lokal menyebabkan tekanan memori:

bashCopy code
[code]
    OPENCLAW_VITEST_MAX_WORKERS=1 pnpm test
[/code]

## Terkait

  * [Ikhtisar SDK](</id/plugins/sdk-overview>) \-- konvensi impor
  * [Plugin Channel SDK](</id/plugins/sdk-channel-plugins>) \-- antarmuka plugin channel
  * [Plugin Provider SDK](</id/plugins/sdk-provider-plugins>) \-- hook plugin provider
  * [Membangun Plugin](</id/plugins/building-plugins>) \-- panduan memulai


Was this useful?YesNo