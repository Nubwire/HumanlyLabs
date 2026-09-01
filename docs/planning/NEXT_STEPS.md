# Next Steps

Living checklist of where this project stands and what's next. Update this
file (don't just append to the session log) whenever priorities change, so
it always reflects current reality — the session log below is the history,
this section is the plan.

_Last updated: 2026-08-31_

## Current state

- Repo initialized with the v41 site export (28 HTML pages + `courses/`
  tree + assets), committed to `main`.
- `docs/` and `adr/` scaffolding added: architecture overview, deployment
  notes, and 3 ADRs (see `adr/README.md`).
- Site has not yet been verified as actually deployed anywhere from this
  repo — `_headers`/`_redirects` are present but no confirmed live Cloudflare
  Pages project is linked in this repo.
- Completed a full bug sweep (see `SESSION_LOG.md` for details) — fixed a
  critical bug that was silently breaking the entire homepage tools grid,
  removed dead payment-modal code, and fixed a missing-`noopener` security
  issue on 11 external/internal links. If this repo is already connected to
  a live Cloudflare Pages deployment, **this fix should ship as soon as
  possible** — the homepage tool/course grid has likely been invisible to
  every visitor until now.
- **The Social Landing course is fully built out** — all 20 lessons across
  6 modules are written, published, and linked from the curriculum page. See
  `docs/scripts/build-social-landing-lessons.py` for how to edit/regenerate
  lesson content.
- **The Confidence Blueprint course is fully built out** — all 18 lessons
  across 6 modules are written, published, and linked from the curriculum
  page. See `docs/scripts/build-confidence-blueprint-lessons.py`. This
  course covers CBT/exposure-therapy content for social anxiety — the
  existing "not a substitute for therapy" disclaimer from the landing
  page's FAQ is echoed in Lesson 1, and Lesson 17 addresses when to seek
  professional support.
- **Friendship Revival is the last course left** — still shows its full
  curriculum (19 lessons) as "Coming soon." Same process: individual lesson
  pages, ~900–1000-word lessons with exercises, linked from
  `content/index.html`, generator script in `docs/scripts/`.

## Open questions (need answers before more work should land)

1. **Is this repo actually connected to a live Cloudflare Pages (or Netlify)
   deployment?** If yes — what's the project name / URL, and is `main`
   already the deploy branch? If no — deployment setup is itself a next step.
2. **Payment provider** — `_redirects` references `/quiz/success` and
   `/courses/*/success` paths, implying a checkout flow (Stripe? Gumroad?
   something else?) that isn't in this repo. Where does that live, and does
   it need to be documented or vendored here?
3. **Client-side Anthropic API calls** — see `adr/0003`. Needs a decision
   before the affected tool pages can be trusted in production.
4. **What changed in this specific export ("v41-new-email")?** The zip this
   repo was seeded from was named with "new-email" — the only email-related
   content found was the `hello@humanlylabs.org` contact address and a Tally
   newsletter signup embed on the homepage. Worth confirming with whoever
   generated the export whether there's a specific email change (e.g. a new
   transactional email flow, a changed address, a new capture form) that
   should be called out explicitly, since it wasn't obvious from a diff-free
   read of the files.

## Suggested next steps (in rough priority order)

- [ ] Build out Friendship Revival (19 lessons) — same pattern as the other
      two courses.
- [ ] Confirm deployment target and, if not yet connected, connect this repo
      to Cloudflare Pages (or wherever it should live).
- [ ] Resolve ADR-0003 (client-side API key exposure) — pick an approach and
      implement it, or explicitly mark it out of scope.
- [ ] Document (or vendor) the payment/checkout integration referenced by
      `_redirects`.
- [ ] Establish what actually changed in the "new-email" export vs. the
      previous version, so future exports can be diffed meaningfully instead
      of re-uploaded wholesale each time.
- [ ] Consider whether shared UI (nav/footer/design tokens duplicated across
      28+ files) is worth extracting — see ADR-0002 consequences.

## How to keep this useful across sessions

Each working session should, before finishing:
1. Update the checklist above to reflect what actually changed.
2. Add a dated entry to `SESSION_LOG.md` summarizing what was done and why.
3. Commit both alongside the code changes, so the next session (with no
   memory of this one) can `git log` and read straight into context.
