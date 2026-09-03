# Architecture Decision Records

This folder holds ADRs for Humanly Labs — short records of significant
technical decisions, the context behind them, and their consequences.

Format follows Michael Nygard's standard ADR template. Each ADR is numbered
sequentially and, once accepted, is not edited to reflect new decisions — a
new ADR supersedes it instead.

| # | Title | Status |
|---|-------|--------|
| [0001](./0001-record-architecture-decisions.md) | Record architecture decisions | Accepted |
| [0002](./0002-static-site-no-build-step.md) | Static HTML site with no build step or framework | Accepted |
| [0003](./0003-client-side-anthropic-api-calls.md) | Client-side calls to the Anthropic API from tool pages | Proposed / needs decision |
| [0004](./0004-client-side-course-access-gate.md) | Client-side (localStorage) gate on course content pages | Accepted — known limitations |

## Adding a new ADR

Copy the format of `0001`, number it sequentially, and add a row to the table
above.
