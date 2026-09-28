---
title: Release checks stages
source_url: https://docs.openclaw.ai/reference/full-release-validation/release-checks
scraped_at: 2026-09-28
---

ReleasesRelease process

## Release checks stages

`OpenClaw Release Checks` is the largest child workflow. It resolves the target once and validates the umbrella's shared package artifact when available. A direct or focused dispatch prepares its own `release-package-under-test` artifact when package or Docker-facing stages need it.

Stage | Details  
---|---  
Release target | **Job:** `Resolve target ref`  
**Backing workflow:** none |   
**Tests:** selected ref, optional expected Validation SHA, profile, concrete release-check groups, and focused live suite filter. |   
**Rerun:** select the concrete group for the failed surface. |   
Package artifact | **Job:** `Prepare release package artifact`  
**Backing workflow:** none |   
**Tests:** validates the umbrella's immutable package tuple, or packs one candidate tarball for a direct/focused Release Checks dispatch, then exposes it to downstream package-facing checks. |   
**Rerun:** the affected package, cross-OS, or live/E2E group. |   
Install smoke | **Job:** `Run install smoke`  
**Backing workflow:** `Install Smoke` |   
**Tests:** full install path with root Dockerfile smoke image reuse, QR package install, root and gateway Docker smokes, installer Docker tests, and Bun global install plus CLI/local-agent/Gateway runtime smoke. |   
**Rerun:** `rerun_group=install-smoke`. |   
Cross-OS | **Job:** `cross_os_release_checks`  
**Backing workflow:** `OpenClaw Cross-OS Release Checks (Reusable)` |   
**Tests:** fresh and upgrade lanes on Linux, Windows, and macOS for the selected provider and mode, using the candidate tarball plus a baseline package. Linux, Windows, and macOS Gateway install and upgrade suites gate beta, stable, and full publication, with recorded pass/fail conclusions. |   
**Rerun:** `rerun_group=cross-os`. |   
Repo and live E2E | **Job:** `Run repo/live E2E validation`  
**Backing workflow:** `OpenClaw Live And E2E Checks (Reusable)` |   
**Tests:** repository E2E, live cache, OpenAI websocket streaming, native live provider and plugin shards, and Docker-backed live model/backend/gateway harnesses selected by `release_profile`. |   
**Runs:** `run_release_soak=true`, `release_profile=full`, or focused `rerun_group=live-e2e`. |   
**Rerun:** `rerun_group=live-e2e`, optionally with `live_suite_filter`. |   
Docker release path | **Job:** `Run Docker release-path validation`  
**Backing workflow:** `OpenClaw Live And E2E Checks (Reusable)` |   
**Tests:** release-path Docker chunks against the shared package artifact. |   
**Runs:** `run_release_soak=true`, `release_profile=full`, or focused `rerun_group=live-e2e`. |   
**Rerun:** `rerun_group=live-e2e`. |   
Package Acceptance | **Job:** `Run package acceptance`  
**Backing workflow:** `Package Acceptance` |   
**Tests:** offline plugin package fixtures, plugin update, and published-upgrade survivor checks against the same tarball. The canonical mock-OpenAI Telegram package E2E is deferred for beta `all` without soak; explicit `package` and soak select it by default. Blocking release checks use the default latest published baseline; soak checks (`run_release_soak=true`) resolve the latest stable baseline once and run the reported-issue upgrade fixtures against it. |   
**Rerun:** `rerun_group=package`. |   
Maturity scorecard | **Job:** `Render maturity scorecard release docs`  
**Backing workflow:** `maturity-scorecard.yml` |   
**Tests:** renders the advisory maturity scorecard docs against the target ref. Only runs when `run_maturity_scorecard=true` is passed. |   
**Rerun:** direct manual `rerun_group=qa` with `run_maturity_scorecard=true`. |   
QA parity | **Job:** `Run QA Lab parity lane` and `Run QA Lab parity report`  
**Backing workflow:** direct jobs |   
**Tests:** candidate and baseline agentic parity packs, then the parity report. |   
**Rerun:** `rerun_group=qa-parity`; direct manual child dispatch may aggregate with `qa`. |   
QA runtime parity | **Job:** `Verify QA Lab runtime-pair lanes`  
**Backing workflow:** direct job |   
**Tests:** the canonical core `openclaw`/`codex` lane (`pnpm openclaw qa suite --runtime-pair openclaw,codex --runtime-pair-lane core`) and, with `run_release_soak=true`, the soak lane. Includes the OpenClaw core restart proof. The release verifier enforces the recorded lane status. |   
**Rerun:** `rerun_group=qa-parity`; direct manual child dispatch may aggregate with `qa`. |   
QA runtime tool coverage | **Job:** `Enforce QA Lab runtime tool coverage`  
**Backing workflow:** direct job |   
**Tests:** dynamic tool drift between `openclaw` and `codex` in the canonical core runtime-pair lane (`pnpm openclaw qa coverage --tools`), using that lane's output. Blocking: this job is not advisory-overridable. |   
**Rerun:** `rerun_group=qa-parity`; direct manual child dispatch may aggregate with `qa`. |   
QA live Matrix | **Job:** `Run QA Live Matrix catalog`  
**Backing workflow:** `QA-Lab - All Lanes` reusable workflow |   
**Tests:** catalog-derived YAML scenarios through the shared Matrix live adapter in the `qa-live-shared` environment, distributed across deterministic shards. |   
**Rerun:** `rerun_group=qa-live` with `live_suite_filter=qa-live-matrix`; direct manual child dispatch may aggregate with `qa`. |   
QA live Buzz | **Job:** `Run QA Lab live Buzz lane`  
**Backing workflow:** `QA-Lab - All Lanes` reusable workflow |   
**Tests:** signed canary and mention-gating round trips through the real Buzz plugin using dedicated Convex-leased identities and a hosted relay room. |   
**Rerun:** `rerun_group=qa-live` with `live_suite_filter=qa-live-buzz`; direct manual child dispatch may aggregate with `qa`. |   
QA live Telegram | **Job:** `Run QA Lab live Telegram lane`  
**Backing workflow:** trusted `OpenClaw Release Telegram QA` dispatch |   
**Tests:** live Telegram QA with Convex CI credential leases. |   
**Rerun:** `rerun_group=qa-live`; direct manual child dispatch may aggregate with `qa`. |   
QA live Discord | **Job:** `Run QA Lab live Discord lane`  
**Backing workflow:** direct job with recorded status enforced by the release verifier |   
**Tests:** live Discord QA with Convex CI credential leases when `OPENCLAW_RELEASE_QA_DISCORD_LIVE_CI_ENABLED` is enabled. |   
**Rerun:** `rerun_group=qa-live` with `live_suite_filter=qa-live-discord`. |   
QA live WhatsApp | **Job:** `Run QA Lab live WhatsApp lane`  
**Backing workflow:** direct job with recorded status enforced by the release verifier |   
**Tests:** live WhatsApp QA with Convex CI credential leases when `OPENCLAW_RELEASE_QA_WHATSAPP_LIVE_CI_ENABLED` is enabled. |   
**Rerun:** `rerun_group=qa-live` with `live_suite_filter=qa-live-whatsapp`. |   
QA live Slack | **Job:** `Run QA Lab live Slack lane`  
**Backing workflow:** direct job with recorded status enforced by the release verifier |   
**Tests:** live Slack QA with Convex CI credential leases when `OPENCLAW_RELEASE_QA_SLACK_LIVE_CI_ENABLED` is enabled. |   
**Rerun:** `rerun_group=qa-live` with `live_suite_filter=qa-live-slack`. |   
Release verifier | **Job:** `Verify release checks`  
**Backing workflow:** none |   
**Tests:** required release-check jobs for the selected rerun group. |   
**Rerun:** rerun after focused child jobs pass. |   
  
## Docker release-path chunks

The Docker release-path stage runs these chunks when `live_suite_filter` is empty:

Chunk | Coverage  
---|---  
`core` | Core Docker release-path smoke lanes.  
`package-update-openai` | OpenAI package and tool-call proof, Codex on-demand install and live progress, root-managed VPS upgrades, and authenticated update restart.  
`package-update-onboarding` | Channel onboarding, install switching, and skill installation.  
`package-update-migrations` | Channel switching and published-package upgrade survival.  
`package-update-self-upgrade` | Local upgrade survival and compatibility with published September update drivers.  
`plugins-runtime-plugins` | Plugin runtime lanes that exercise plugin behavior.  
`plugins-runtime-services` | Service-backed and live plugin runtime lanes.  
`plugins-runtime-install-a` through `plugins-runtime-install-h` | Plugin install/runtime batches split for parallel release validation.  
`openwebui` | OpenWebUI compatibility smoke isolated on a dedicated large-disk runner when requested.  
  
All four package/update rows retain their coverage across every release profile. The provider-neutral checks are balanced across three runners, preserving each runner's npm limit. `package-update-core` and `package-update` remain aggregate manual chunk names. Root-managed VPS upgrade and authenticated restart checks run in the OpenAI row. Missing required credentials still fail the job; the diagnostic pool continues so independent non-live checks also report their results. Setup failures and cancellation do not start that pool.

Expanded published-upgrade survivor and update-migration coverage runs in baseline-specific groups of at most three scenarios, with up to 32 targeted Docker jobs active per matrix. The grouping and execution planners share the same baseline compatibility rules; package identities, fresh scenario containers, per-runner npm limits, and failure reporting remain unchanged.

Use targeted `docker_lanes=<lane[,lane]>` on the reusable live/E2E workflow when only one Docker lane failed. The release artifacts include per-lane rerun commands with package artifact and image reuse inputs when available.

Was this useful?YesNo

Open issue