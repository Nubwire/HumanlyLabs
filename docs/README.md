# Humanly Labs — Docs

This folder holds working documentation for the Humanly Labs site: what it is,
how it's structured, how it's deployed, and what's still open. It's meant to
give any contributor (human or AI assistant) full context without needing to
re-derive it from the code each time.

## Contents

- [`ARCHITECTURE.md`](./ARCHITECTURE.md) — what the site is, how it's built, page inventory
- [`DEPLOYMENT.md`](./DEPLOYMENT.md) — hosting, headers, redirects
- [`planning/NEXT_STEPS.md`](./planning/NEXT_STEPS.md) — live checklist of what's next
- [`planning/SESSION_LOG.md`](./planning/SESSION_LOG.md) — dated log of what changed each working session
- [`../adr/`](../adr/) — Architecture Decision Records (why we made the calls we made)

## Quick orientation

Humanly Labs is a static marketing + tools site about friendship, social
anxiety, and social skills. It's plain HTML/CSS/JS (no build step, no
framework, no package.json) deployed as a static site with Cloudflare Pages
style `_headers` / `_redirects` files.

If you're picking this project up cold, read `planning/NEXT_STEPS.md` first —
it has the current state and the open questions that need a decision before
more work should land.
