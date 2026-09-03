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
- **The Friendship Revival course is fully built out** — all 18 lessons
  across 6 modules are written, published, and linked from the curriculum
  page. See `docs/scripts/build-friendship-revival-lessons.py`. Covers
  attachment theory as a descriptive framework, not diagnosis.
- **All three courses are now content-complete: 56 lessons total.** Course
  build-out, the main task this project has been focused on, is done.
- **Deployment is confirmed live** at humanlylabs.org / www.humanlylabs.org,
  auto-deploying from `main` via Cloudflare Pages. Verified the critical
  homepage bug fix and the course build-out are both live in production.
  See `DEPLOYMENT.md` for details. One thing still worth a manual check:
  the gated `/content/` and lesson pages themselves weren't directly
  verifiable from this session (noindex pages can't be reached via search).
- **The 4 previously "Coming Soon" mini-app tools are now built and live**
  in the codebase: New In Town Planner, Core Values Mapper, Solo Evening
  Ritual Builder, Self-Compassion Reset. All deterministic/client-side (no
  external API dependency — see `adr/0003` update). Once this session's
  commit is pushed, they'll go live in production the same way past pushes
  have.
- **Course content pages now have a lightweight access gate** (see
  `adr/0004`). Bare content/lesson links no longer work — access requires
  `?paid=true` on the URL, which the Stripe success redirect adds
  automatically. This is friction, not real security (documented
  honestly in the ADR); a real fix needs server-side verification.
  **Important:** the full Stripe purchase → unlock flow should be tested
  end-to-end once this is deployed, since the Payment Link success-URL
  configuration wasn't independently verified from this environment.

## Open questions (need answers before more work should land)

1. **Manually spot-check the gated `/content/` and lesson pages in
   production** — confirm at least one lesson page per course renders
   correctly, since this couldn't be verified via search/fetch (noindex
   pages don't surface in search, and there was no direct link available).
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

- [ ] After pushing, test the full Stripe purchase flow end-to-end for at
      least one course — click a real (or coupon-comped) checkout through
      to completion and confirm it lands unlocked on the content page, not
      bounced back to the landing page by the new gate.
- [ ] After pushing, spot-check the 4 new tools live in production
      (new-in-town, values-mapper, evening-ritual, self-compassion) — since
      they're deterministic/client-side only, they should work identically
      to how they behaved in this session, but worth a real confirmation.
- [ ] Manually spot-check a gated lesson page in production (see open
      question 1 above).
- [ ] Resolve ADR-0003 for the *original 7* tools (client-side API key
      exposure) — pick an approach and implement it, or explicitly mark it
      out of scope. The 4 new tools sidestep this entirely; the original 7
      still have it open.
- [ ] Document (or vendor) the payment/checkout integration referenced by
      `_redirects`.
- [ ] Establish what actually changed in the "new-email" export vs. the
      previous version, so future exports can be diffed meaningfully instead
      of re-uploaded wholesale each time.
- [ ] Consider whether shared UI (nav/footer/design tokens duplicated across
      many files) is worth extracting — see ADR-0002 consequences.
- [ ] Consider a lighter-weight review pass on the 56 published lessons —
      they were written and expanded across several sessions to hit a
      ~900+ word target per lesson; a read-through for tone consistency
      across the three courses could be worthwhile before heavy traffic.

## How to keep this useful across sessions

Each working session should, before finishing:
1. Update the checklist above to reflect what actually changed.
2. Add a dated entry to `SESSION_LOG.md` summarizing what was done and why.
3. Commit both alongside the code changes, so the next session (with no
   memory of this one) can `git log` and read straight into context.
