# 2. Static HTML site with no build step or framework

Date: 2026-08-31

## Status

Accepted (documenting existing/inherited decision)

## Context

The site (28 HTML pages plus a `courses/` tree) is written as plain HTML with
inline CSS and JavaScript per page, and deployed via Cloudflare Pages-style
`_headers` and `_redirects` files. There is no `package.json`, bundler, or
templating layer — shared elements (nav, fonts, design tokens) are
duplicated across files rather than componentized.

## Decision

Keep the site as hand-authored static HTML for now. This decision is being
recorded rather than newly made — it reflects the state the project was
already in when this repo was set up — so that a future change away from it
is a deliberate decision rather than a default drift.

## Consequences

**Pros:** zero build tooling, trivial to deploy anywhere that serves static
files, no dependency/version management overhead, fast page loads.

**Cons:** shared UI (nav, footer, design tokens) is duplicated per file, so
changes to shared elements require multi-file edits and are easy to make
inconsistently. As the page count grows, this is the most likely thing to
force a revisit (e.g. introducing a lightweight templating/build step, or a
static site generator).
