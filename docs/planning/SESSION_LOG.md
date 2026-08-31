# Session Log

Dated, append-only log of work done on this repo, one entry per working
session. Newest entries at the top. This exists because work happens across
sessions with no shared memory — read this before starting new work.

---

## 2026-08-31 — Repo bootstrap + v41 site import

**Starting point:** repo contained only a placeholder `README.md`.

**What was done:**
- Imported the site export from `humanly-v41-new-email.zip` (28 HTML pages,
  `courses/` tree with 3 paid courses, `images/`, `_headers`, `_redirects`,
  `sitemap.xml`, `robots.txt`, `favicon.svg`, `og-image.png`) into the repo
  root.
- Added `docs/` (`README.md`, `ARCHITECTURE.md`, `DEPLOYMENT.md`,
  `planning/`) and `adr/` (0001–0003) to give the project durable,
  discoverable context.
- Reviewed the site for anything specifically related to the "new-email"
  part of the export filename — found the contact address
  (`hello@humanlylabs.org`) and a Tally newsletter embed on the homepage,
  but no obvious diff-worthy "new email feature." Logged as an open question
  in `NEXT_STEPS.md` rather than guessed at.
- Noticed and documented (ADR-0003) that several interactive tool pages call
  the Anthropic API directly from client-side JS with no API key — flagged
  as a production risk, not fixed (no decision made yet on the right fix).

**Left open:** see "Open questions" in `NEXT_STEPS.md` — deployment target,
payment provider integration, the ADR-0003 decision, and confirming what the
"new-email" export actually changed.
