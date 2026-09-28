---
title: Release validation workflows
source_url: https://docs.openclaw.ai/ci/release-validation
scraped_at: 2026-09-28
---

ContributingTesting and CI

This page is an index. Release validation is documented on five pages, one per reader job. Open the page that matches your task.

Full Release Validation retains all six Docker seed lanes, QA Smoke, and Control UI performance through its normal CI child. Every admitted canonical main run keeps the published-upgrade survivor; the other five Docker seed lanes run in ordinary manual/release validation, including npm qualification scopes. Pull requests and exact-head PR fallbacks omit Docker seed and QA Smoke. See [full release coverage](</ci/release-validation/full-release-validation>) for the exact survivor contract and target compatibility limits.

Page | Read it when  
---|---  
[Full Release Validation](</ci/release-validation/full-release-validation>) | The release umbrella: Validation/Tooling SHA binding, release publish, Docker Release, profiles, and recovery.  
[Live and E2E shards](</ci/release-validation/live-and-e2e-shards>) | The named live/E2E shards, their coverage, and the images they run in.  
[Package Acceptance](</ci/release-validation/package-acceptance>) | Validating one installable tarball: jobs, candidate sources, suite profiles, and examples.  
[Install smoke and Docker E2E](</ci/release-validation/install-smoke-and-docker-e2e>) | Install Smoke coverage, the local Docker E2E aggregate and tunables, and release-path chunks.  
[Plugin Prerelease](</ci/release-validation/plugin-prerelease>) | The separate, more expensive plugin product/package suite and when it is dispatched.  
  
The [bounded hybrid hosted offload](</ci/capacity#bounded-hybrid-hosted-offload>) applies only to automatic CI first attempts. Full Release Validation, candidate/artifact workflows, and frozen-target workloads retain their existing coverage and runner routes.

## Where each section moved

Every section heading from the previous single-page version keeps its anchor here, so an existing link such as `/ci/release-validation#suite-profiles` still resolves. Each entry points at the page that now holds the content.

  * [Full Release Validation](</ci/release-validation/full-release-validation#full-release-validation>)
  * [Live and E2E shards](</ci/release-validation/live-and-e2e-shards#live-and-e2e-shards>)
  * [Package Acceptance](</ci/release-validation/package-acceptance#package-acceptance>)
  * [Jobs](</ci/release-validation/package-acceptance#jobs>)
  * [Candidate sources](</ci/release-validation/package-acceptance#candidate-sources>)
  * [Suite profiles](</ci/release-validation/package-acceptance#suite-profiles>)
  * [Legacy compatibility windows](</ci/release-validation/package-acceptance#legacy-compatibility-windows>)
  * [Examples](</ci/release-validation/package-acceptance#examples>)
  * [Install smoke](</ci/release-validation/install-smoke-and-docker-e2e#install-smoke>)
  * [Local Docker E2E](</ci/release-validation/install-smoke-and-docker-e2e#local-docker-e2e>)
  * [Tunables](</ci/release-validation/install-smoke-and-docker-e2e#tunables>)
  * [Reusable live/E2E workflow](</ci/release-validation/install-smoke-and-docker-e2e#reusable-live%2Fe2e-workflow>)
  * [Release-path chunks](</ci/release-validation/install-smoke-and-docker-e2e#release-path-chunks>)
  * [Plugin Prerelease](</ci/release-validation/plugin-prerelease#plugin-prerelease>)


## Related

  * [Install overview](</install>)
  * [Release channels](</install/development-channels>)


Was this useful?YesNo

Open issue