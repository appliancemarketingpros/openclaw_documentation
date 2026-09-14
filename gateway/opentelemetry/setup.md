---
title: Set up OpenTelemetry export
source_url: https://docs.openclaw.ai/gateway/opentelemetry/setup
scraped_at: 2026-09-14
---

Gateway & OpsGateway

## Quick start

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/diagnostics-otel
[/code]

json5Copy code
[code]
    {  plugins: {    allow: ["diagnostics-otel"],    entries: {      "diagnostics-otel": { enabled: true },    },  },  diagnostics: {    enabled: true,    otel: {      enabled: true,      endpoint: "http://otel-collector:4318",      protocol: "http/protobuf",      serviceName: "openclaw-gateway",      traces: true,      metrics: true,      logs: true,      sampleRate: 0.2,      flushIntervalMs: 60000,    },  },}
[/code]

Or enable the plugin from the CLI: `openclaw plugins enable diagnostics-otel`.

With the plugin loaded, changes to `diagnostics.otel` hot-reload only its exporter service. The previous generation unsubscribes and flushes before the replacement starts with the new endpoint, headers, sampling, and signal settings. Other plugin services, channels, and Gateway connections stay running. A cleanup or startup failure requests Gateway recovery instead of leaving a partially replaced exporter.

`diagnostics.enabled` also hot-applies to the shared dispatcher and its heartbeat. The Gateway owns that process-wide heartbeat; stopping a channel leaves it running. Standalone hosts using the plugin SDK own `startDiagnosticHeartbeat` and `stopDiagnosticHeartbeat` for their process, rather than each channel owning them. Disabling it stops diagnostic sampling and recovery listeners; enabling it starts them again. Preloaded OpenTelemetry SDKs keep ownership of their providers and transport: these changes do not shut down or reconfigure the host SDK.

## Which processes export

  * **Gateway** starts the exporter at startup and exports from the Gateway process for every run it executes, including `openclaw agent` turns dispatched to it.
  * **One-shot local runs** (`openclaw agent --local`) execute in the CLI process. When OTel export is configured and the plugin is enabled, that same CLI process starts one exporter instance for the run and flushes buffered spans, metrics, and logs before the process exits. The CLI waits at most 5 seconds for the diagnostic-event queue to drain and 10 more for the flush, so an unreachable collector cannot hold the command open. A collector that accepts the connection but never answers can still delay exit until the exporter's own request timeout (`OTEL_EXPORTER_OTLP_TIMEOUT`). Plugin registration resources remain open until exporter cleanup finishes, even when either wait times out. In JSON output mode, these one-shot runs suppress only the stdout JSONL log sink so command stdout stays reserved for the JSON response; OTLP traces, metrics, and logs continue when configured.
  * `openclaw agent exec` also runs the agent embedded in the CLI process, but does not start this exporter, so its runs export no telemetry. Dispatch through the Gateway, or use `openclaw agent --local`, when you need traces from a headless run.


## Exporter health

`openclaw doctor` and `openclaw status --all` show a bounded, redacted snapshot of the running Gateway's latest trusted exporter state for each signal and transport. For `diagnostics-otel`, the snapshot distinguishes:

  * OTLP/HTTP protobuf with an endpoint supplied by config or an `OTEL_*` environment fallback.
  * OTLP/HTTP protobuf using the exporter dependency's default endpoint because no endpoint was supplied.
  * Stdout log export.
  * Trace or metric export owned by an externally preloaded OpenTelemetry SDK.


OTLP export failure and recovery transitions are recorded from the exporter's final result callback, after dependency-owned retries finish. A retryable response that later succeeds is therefore not reported as a failure. Startup, log preparation or emit, export, and shutdown failures use fixed reason categories rather than raw errors.

The snapshot never includes endpoint values, headers, certificates, payloads, or raw error messages. Transport is retained only in this local health projection. It is not added to the existing `openclaw.telemetry.exporter.events` metric attributes, and existing Prometheus label sets are unchanged.

## Without an exporter

Keep diagnostics events available to plugins or custom sinks without running `diagnostics-otel`:

json5Copy code
[code]
    {  diagnostics: { enabled: true },}
[/code]

For targeted debug output without raising `logging.level`, use diagnostics flags. Flags are case-insensitive and support wildcards (`telegram.*` or `*`):

json5Copy code
[code]
    {  diagnostics: { flags: ["telegram.http"] },}
[/code]

Or as a one-off env override:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload openclaw gateway
[/code]

Flag output goes to the standard log file (`logging.file`) and is still redacted by the always-on log redaction policy. Full guide: [Diagnostics flags](</diagnostics/flags>).

## Disable

json5Copy code
[code]
    {  diagnostics: { otel: { enabled: false } },}
[/code]

Or leave `diagnostics-otel` out of `plugins.allow`, or run `openclaw plugins disable diagnostics-otel`.

When the plugin would otherwise own NodeSDK, keep propagation available while disabling every plugin-owned exporter, listener, health route, and stdout sink:

bashCopy code
[code]
    OTEL_SDK_DISABLED=true openclaw gateway
[/code]

Was this useful?YesNo

Open issue