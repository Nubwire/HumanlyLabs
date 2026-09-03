# Session Log

Dated, append-only log of work done on this repo, one entry per working
session. Newest entries at the top. This exists because work happens across
sessions with no shared memory — read this before starting new work.

---

## 2026-09-03 — Added a client-side access gate to all 3 courses' content

**What prompted this:** working through a real support scenario (comping a
customer, "old mate," free access to The Social Landing) surfaced that the
gated `/courses/*/content/` pages had **zero access control** — any bare
link worked permanently for anyone, since access was only ever "protected"
by not being publicly linked. Also worked through creating a 100%-off
Stripe coupon for comps along the way — see the conversation for the full
troubleshooting trail (test/live mode mismatch ruled out, wrong-account
theory ruled out, ultimately traced to the promotion code being
customer-email-restricted).

**What was done:** added a small inline gate script — first thing in
`<head>`, before anything else — to all 59 gated files (3 course
`content/index.html` pages + all 56 individual lesson pages):
`?paid=true` in the URL sets a per-course `localStorage` flag and strips
the param; otherwise, if the flag isn't set, the page redirects
immediately to the course's public landing page before rendering.
Deliberately used `localStorage`, not the `sessionStorage` the mini-tools
use — a course gets revisited over weeks, and `sessionStorage` would have
locked out a paying customer every time they closed their browser.

Updated `_redirects` so the three course success redirects
(`/courses/<slug>/success` → `.../content/`) append `?paid=true`, so a
real Stripe purchase still unlocks automatically exactly as before — no
change needed on the Stripe side.

**Documented as `adr/0004-client-side-course-access-gate.md`**, including
the honest limitations: this is friction, not real protection (anyone who
adds `?paid=true` manually still gets in); switching devices/browsers
breaks access and requires re-sending the `?paid=true` link; and the
Stripe Payment Link success-URL assumption wasn't independently verified
against the live dashboard (no Stripe access from this environment) —
worth testing the full purchase flow end-to-end once deployed.

**Verified:** JS syntax clean across all 59 modified files (and the whole
repo), zero broken links/assets repo-wide, spot-checked the gate script's
placement and logic by hand.

**Not done / worth knowing:** comping a customer now requires sending
`.../content/?paid=true` specifically, not the bare link — the earlier
guidance in this session log and conversation history about "just send
the link" is now out of date for that reason. The Stripe-coupon comp path
(a real $0 checkout) is unaffected, since Stripe's success redirect
already appends the parameter.

---

## 2026-08-31 (7) — Built out the 4 "Coming Soon" mini-app tools

**What was done:** built and shipped all four tools that were previously
`status: 'soon'` on the homepage: New In Town Planner ($4.99),
Core Values Mapper ($3.99), Solo Evening Ritual Builder ($3.99), and
Self-Compassion Reset ($3.99). Each is a standalone page
(`new-in-town.html`, `values-mapper.html`, `evening-ritual.html`,
`self-compassion.html`) matching the existing tool-page pattern: a
multi-screen quiz/interaction flow, a Stripe paywall gate with
`sessionStorage` + `?paid=true` handling, and a results screen.

**Deliberate architecture choice — no client-side API calls.** Given
ADR-0003 (the existing 7 tools call `api.anthropic.com` directly from the
browser with no key, which doesn't work in production), these four new
tools were built as fully deterministic, client-side generators instead —
local JS logic against curated content banks, keyed off the user's
answers. No external network dependency at all, so no broken-in-production
risk. Documented as an update to `adr/0003-client-side-anthropic-api-calls.md`
and recommended as the default pattern for any future new tool.

**What each tool actually does:**
- **New In Town Planner** — quiz (current phase, biggest blocker, weekly
  time budget, social style, up to 3 interests) → a personalised 4-week
  plan, week by week, with tasks pulled from an interest-keyed activity
  bank and tactics matched to the stated blocker.
- **Core Values Mapper** — a 3-round elimination process (24 values → ~10
  → 8 → 5) followed by a per-value life-alignment check (rarely/sometimes/
  often), producing a ranked top-5 with alignment badges and a concrete
  suggested action for anything not well-aligned.
- **Solo Evening Ritual Builder** — mood, energy level, what's needed
  tonight (comfort/stimulation/quiet/connection/accomplishment/rest), and
  available time (15-90 min) → a scaled sequence of 3-5 steps pulled from a
  need-keyed activity bank, opening/closing text matched to the stated
  mood.
- **Self-Compassion Reset** — situation select (loneliness/rejection/
  failure/bad day/self-criticism/other) → a guided ~10-minute, 6-step
  sequential practice (arrival, naming, common humanity, self-kindness
  phrase, sitting with it, close), each step with a suggested-time
  countdown and an optional **read-aloud toggle using the browser's
  built-in `speechSynthesis` API** — genuinely delivers on the "guided
  audio + text practice" feature claim with zero external dependency.

**Bug caught before shipping:** the Stripe link I initially wrote into
`self-compassion.html` didn't match the real one already configured in
`index.html`'s `APPS` array for that tool — cross-checked all four
pages' `STRIPE_LINK` constants against the array via script before wiring
anything up, and fixed the mismatch. A wrong Stripe link would have sent
buyers to the wrong checkout.

**Wired into the site:** flipped all four apps from `status: 'soon'` to
`status: 'live'` in `index.html`'s `APPS` array (their `page` and
`stripeUrl` fields were already correctly pre-configured, matching the
filenames and Stripe links used above) — the homepage cards now show
"Try it →" instead of "Coming Soon" automatically, no further homepage
changes needed. Added all 4 new URLs to `sitemap.xml`.

**Verified:** full repo-wide link check (zero broken links/assets), JS
syntax check across every HTML file including the 4 new ones, no duplicate
IDs, consistent analytics ID and Ahrefs key, all 4 pages correctly set
`robots: index, follow` (unlike the gated course content, these are public
marketing/product pages), sitemap.xml validated as well-formed XML.

---

## 2026-08-31 (6) — Deployment confirmed live, 3 more small bugs found and fixed

**What was done:** confirmed via user + direct verification that this repo
is connected to a live Cloudflare Pages deployment at
**humanlylabs.org** / **www.humanlylabs.org**, auto-deploying from `main`.
Fetched the live homepage and the Social Landing course landing page and
cross-checked against the repo:
- Homepage tools grid renders correctly in production — confirms the
  critical `apps.sort` → `APPS.sort` bug fix (from an earlier session) is
  live and working.
- The live Social Landing landing page's "20 lessons" hero copy confirms
  the site is serving from commit `34e1878` or later (that copy only exists
  from that commit onward) — solid evidence Cloudflare Pages is genuinely
  auto-deploying from `main`, not serving something stale or disconnected.

**Bugs found by comparing live vs. repo, then fixed:** the live/repo
Social Landing landing page (`courses/social-landing/index.html`) had two
more stale "19" references that an earlier session's "19→20 lessons" fix
had missed (a stat-counter box and a "19 in-depth lessons" list item), plus
a separate, unrelated inconsistency: descriptive copy said "Four of our
science-backed tools" and a stat box said "4" for tools included, while the
page actually lists and links six tool pills, and the "What's included"
section correctly says "6 Humanly Labs tools". Fixed all of these to `20`
lessons / `6` tools consistently. Cross-checked Confidence Blueprint and
Friendship Revival landing pages for the same pattern — both were already
internally consistent (3 tools, 18 lessons each, matching their tool-pill
lists), so no changes needed there.

**Not verified this session:** the gated `/courses/*/content/` pages and
individual lesson pages couldn't be fetched directly (they're `noindex`,
don't surface via web search, and no direct link was available to fetch
from) — worth a manual spot-check by the user to fully close this out.

---

## 2026-08-31 (5) — Built out The Friendship Revival course (18 lessons) — all three courses now complete

**What was done:** wrote and published all 18 lesson pages for *The
Friendship Revival* course (adult friendship maintenance, attachment styles,
reviving dormant ties, deepening and forming friendships), covering all 6
modules end to end. Same pattern as the other two courses:
- One standalone page per lesson, ~811–944 words each (avg ~865), with a
  "Try this" exercise box in every lesson
- Lessons pairing with a tool (Friendship Audit ×2, Attachment Style Quiz,
  Check-In Generator ×2) link out to it directly
- Terracotta/brown theme (`#7A3B19`) matching this course's existing
  branding

**Content note:** this course covers attachment theory (anxious/avoidant/
secure patterns) as a descriptive framework for relational tendencies, not
as clinical diagnosis — Lesson 4 explicitly frames it this way. No
diagnostic claims are made about the reader anywhere in the lesson content.

**Correction to a prior note:** earlier session notes in this file said
Friendship Revival had 19 lessons — that was wrong (based on a stale
grep-count early in the project). It has 18, matching what the landing page
already correctly stated. No landing-page copy bug here, unlike Social
Landing's earlier "19 lessons" typo.

**How it's built:** same generator pattern as the other two courses —
`docs/scripts/build-friendship-revival-lessons.py`.

**Wired into the site:** `courses/friendship-revival/content/index.html` —
all 18 "Coming soon" cards converted to real links with a "Start →" badge.

**Verified:** full repo-wide link check (zero broken links/assets across
the entire site — all three courses, 56 lesson pages total, plus every
other page), JS syntax check across every HTML file, `noindex` coverage,
and `target="_blank"` + `noopener` coverage — all clean.

**Course build-out is now complete.** All three Humanly Labs courses
(Social Landing — 20 lessons, Confidence Blueprint — 18 lessons, Friendship
Revival — 18 lessons; 56 lessons total) are fully written, published, and
linked. See `NEXT_STEPS.md` for what's left on the site more broadly:
deployment confirmation, the payment provider integration, and ADR-0003
(client-side API key exposure).

---

## 2026-08-31 (4) — Built out The Confidence Blueprint course (18 lessons)

**What was done:** wrote and published all 18 lesson pages for *The
Confidence Blueprint* course (CBT/exposure-based course for social anxiety),
covering all 6 modules end to end. Same pattern as The Social Landing:
- One standalone page per lesson, ~870–1040 words each (avg ~937), with a
  "Try this" exercise box in every lesson
- Lessons pairing with a tool (Social Anxiety Check, Social Battery ×2,
  Loneliness Deep Dive) link out to it directly
- Blue theme (`#1C5DAF`) to match this course's existing branding, distinct
  from Social Landing's green

**Content note — mental health topic handled carefully:** this course
covers CBT concepts (cognitive distortions, exposure hierarchies, the
spotlight effect) as psychoeducation, consistent with the course's own
existing FAQ disclaimer on the landing page ("not a substitute for
professional mental health treatment"). Lesson 1 repeats that disclaimer
up front, and Lesson 17 explicitly names when a setback is a signal to
seek professional support rather than push through alone. No diagnostic
claims are made anywhere in the lesson content.

**How it's built:** same generator pattern as Social Landing —
`docs/scripts/build-confidence-blueprint-lessons.py` holds the `LESSONS`
data and renders through a shared template into
`courses/confidence-blueprint/content/lessons/*.html`.

**Wired into the site:** `courses/confidence-blueprint/content/index.html`
— all 18 "Coming soon" cards converted to real links with a "Start →"
badge. No landing-page copy bugs found this time (lesson count was already
correct at "18 lessons").

**Verified:** full repo-wide link check (zero broken links/assets across
the whole site, including both courses' lesson pages), JS syntax check
across every HTML file, `noindex` coverage on all 18 new pages, and
`target="_blank"` + `noopener` coverage — all clean.

**Not done yet:** Friendship Revival (19 lessons) is the last of the three
courses still showing "Coming soon" for every lesson. Same pattern applies.

---

## 2026-08-31 (3) — Built out The Social Landing course (20 lessons)

**What was done:** wrote and published all 20 lesson pages for *The Social
Landing* course (relocation loneliness / making friends after a move),
covering all 6 modules end to end. Per the user's direction:
- One standalone page per lesson (not inline on the curriculum page)
- Full-length lessons (~900–1060 words each, averaging ~970) with a "Try
  this" exercise box in every lesson
- Each lesson that pairs with a Humanly Labs tool (Loneliness Quiz, Social
  Battery ×2, Find Your People, Conversation Starter, Check-In Generator,
  Friendship Audit) links out to it directly

**How it's built:** content lives as structured data in
`docs/scripts/build-social-landing-lessons.py` (a `LESSONS` list of dicts,
one per lesson, each with its full HTML body) rendered through a shared
template into `courses/social-landing/content/lessons/*.html`. To regenerate
after editing lesson content, run that script from its own directory — it
resolves the output path back to `courses/social-landing/content/lessons/`
automatically. This keeps 20 lessons' worth of content maintainable from one
file instead of hand-editing 20 near-identical HTML documents.

**Wired into the site:**
- `courses/social-landing/content/index.html` — all 20 "Coming soon" lesson
  cards converted to real links (`<a class="lesson-card">`) pointing at the
  new lesson pages, with a "Start →" status badge instead of "Coming soon"
- `courses/social-landing/index.html` — fixed a pre-existing copy bug ("6
  modules · 19 lessons" — the curriculum has always had 20)
- Every lesson page has prev/next navigation, a breadcrumb back to the
  course overview, `noindex, nofollow` (gated content, matches the pattern
  used by the other course `content/` pages), and the same nav/analytics/
  footer as the rest of the site

**Verified:** ran the repo-wide link checker after every change — zero
broken internal links or assets, including all 20 new pages and their
prev/next chains. Confirmed no JS syntax errors anywhere in the site, and
`target="_blank"` links all carry `rel="noopener noreferrer"`.

**Not done yet:** Confidence Blueprint and Friendship Revival still show
their full curriculum as "Coming soon" for every lesson — those two courses
haven't been started. See `NEXT_STEPS.md`.

---

## 2026-08-31 (2) — Site-wide bug sweep + fixes

**What was done:** ran a systematic check across every HTML file — internal
link/asset resolution, JS syntax validity (via Node), duplicate IDs, missing
`alt` text, meta description coverage, `target="_blank"` security, and
`_headers`/`_redirects`/`sitemap.xml`/`robots.txt` consistency.

**Bugs found and fixed:**
- **Critical — homepage tools grid was silently broken.** `index.html` declared
  `const APPS = [...]` but a later line called `apps.sort(...)` (lowercase).
  That's a `ReferenceError` that halts the script before the next line,
  `renderApps()`, ever runs — so the entire `#app-grid` section (all 12
  tool/course cards) never rendered on the live homepage. Fixed by correcting
  the casing to `APPS.sort(...)`.
- **Dead payment-modal code removed from `index.html`.** A whole payment
  modal (HTML, ~60 lines of CSS, `openModal()`/`closeModal()`, and a
  duplicate/inconsistent set of Stripe links per app) existed but `openModal`
  was never called from anywhere — the actual "Try it" cards link straight to
  each tool page via `<a href>`. Each tool page already has its own working,
  self-contained Stripe paywall (own `STRIPE_LINK`, own `?paid=true` +
  `sessionStorage` handling) — that's the real, live payment path. The
  homepage modal was leftover/unfinished and risked misleading a future
  editor into wiring payments through it a second time. Left the individual
  page paywalls untouched since they're the working implementation.
- **Missing `rel="noopener noreferrer"` on 11 `target="_blank"` links**
  across `mini-course.html` (7 internal tool links) and `privacy.html` (4
  external policy links) — reverse-tabnabbing / `window.opener` risk. Added
  the attribute to all of them.
- Also removed a keydown (Escape-key) handler tied to the removed modal that
  would have thrown a `TypeError` on every Escape keypress once the modal
  HTML no longer existed.

**Checked and found clean (no action needed):** all internal `href`/`src`
references resolve to real files; no JS syntax errors anywhere else in the
site; no duplicate `id` attributes; no images missing `alt`; Google Analytics
ID and Ahrefs key are consistent across all 28 pages; `admin.html` and all
three course `content/` pages correctly carry `noindex, nofollow`;
`sitemap.xml` matches the live page set and correctly excludes `/admin` and
gated content pages; `robots.txt` is consistent with the sitemap.

**Not touched / flagged instead of fixed:** the client-side Anthropic API
calls issue from ADR-0003 (still unresolved — that's a design decision, not
a quick bug fix).

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
