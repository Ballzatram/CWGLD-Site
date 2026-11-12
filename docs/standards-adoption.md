# Engineering standards adoption

Owner: Ballzatram. Policy: 1.0.0. Baseline source revision: `689992e69b74545034e949d1b091ce5d8abaaab3`.

Static lighting-design website: five HTML pages, shared CSS, navigation and footer JavaScript. No application server or production build is required.

## Verification

Run `uv run --project .engineering --locked python .engineering/tools/audit.py .` for structural prerequisites. Existing native test/build commands are retained in README and the workflows. `.github/workflows/engineering.yml` adds a consistent, read-only verification gate; it never deploys or uses production secrets. Review `docs/audit.md` for controls requiring manual evidence.

The command register includes existing syntax/compile checks where no full static type checker exists; these are not equivalent to strict typing. Legacy formatter/type/coverage gaps remain explicit, not silently waived. No approved exceptions have been invented. Source import/native platform requirements and hosted protections must be reviewed separately.

## Preservation

Default branches and deployed services are not changed by preparing this branch. Runtime source changes, if any, are limited to documented regression fixes and must pass the existing tests. Do not run live research, mail, payment, model generation, customer data changes or production deployment as a standards check.

## Recorded local verification

The route/resource/script contract passes for all five existing pages. Application HTML/CSS/JavaScript is unchanged.

See docs/audit.md for unresolved controls. A structural pass is not full conformance.

## Final candidate checks

See [merge verification](merge-verification.md) for current gates, commands and actual performance/coverage measurements. This supersedes the initial local-only/native-pending notes above. See .standards.json for the executable command register. Hosted feature restrictions and remaining conformance work remain explicit.
