# 4. Client-side (localStorage) gate on course content pages

Date: 2026-09-03

## Status

Accepted — with known limitations documented below, not a full fix

## Context

Until this change, the gated `/courses/<slug>/content/` pages and all 56
individual lesson pages had **no access control of any kind** — they were
plain, publicly-reachable URLs, kept out of search results only via
`noindex, nofollow`. Anyone who obtained a link (forwarded by a customer,
guessed, or found some other way) had full permanent access, paid or not.

This surfaced directly in a real support scenario: comping a customer
("old mate") access by simply emailing him the bare content URL, which
works today with zero friction — and zero record that he was ever meant
to have access, unless deliberately tracked elsewhere (e.g. a Stripe
coupon redemption).

## Decision

Added a small inline script, as the very first thing in `<head>`, to
`courses/*/content/index.html` and all 56 lesson pages under
`courses/*/content/lessons/`:

- On load, if the URL has `?paid=true`, set a per-course `localStorage`
  flag (e.g. `hly_course_social_landing_unlocked`) and strip the query
  param via `history.replaceState`.
- Otherwise, check for that flag. If it's not set, `location.replace()`
  immediately back to the course's public landing page
  (`/courses/<slug>/`) — before the page has a chance to render.

`_redirects` was updated so the existing Stripe success redirects
(`/courses/<slug>/success` → `/courses/<slug>/content/`) now append
`?paid=true`, so a real purchase flows through and unlocks automatically,
same as it always has.

**`localStorage`, not `sessionStorage`.** The mini-tools use
`sessionStorage` for their paywall, which is fine for a tool used once in
a sitting — but a course is revisited over weeks. `sessionStorage` clears
on browser close, which would have locked a paying customer out every
time they closed their browser. `localStorage` persists until explicitly
cleared, matching how the product is actually used.

## Consequences

**This is friction, not real protection** — the same honest caveat that
applies to the mini-tools' paywall applies here, arguably more so since
it's now protecting something more valuable (a $97 course, not a $3.99–
$4.99 tool). Anyone who knows to add `?paid=true` to a URL, or open dev
tools and set the `localStorage` key manually, gets in regardless. This
gate stops casual link-sharing and makes "just email them the bare URL"
no longer trivially work — it does not stop a technically determined
person. A real fix requires server-side verification (a Cloudflare Worker
checking against actual purchase records, most likely synced from
Stripe), which is a meaningfully bigger project than this change and not
what this ADR implements.

**Device/browser switching breaks access.** Since the unlock is stored in
`localStorage`, a customer who switches browsers, uses a different
device, or clears site data will hit the gate again and need their
original `?paid=true` link (from their Stripe receipt email) to
re-unlock. There's currently no other recovery path — support will need
to resend a link in the `https://humanlylabs.org/courses/<slug>/content/?paid=true`
format if a customer reports losing access this way.

**Depends on the Stripe Payment Link success URL being configured as
`/courses/<slug>/success`.** This wasn't independently verified against
the live Stripe dashboard (no Stripe access from this environment) — the
`_redirects` file's pre-existing `/success` routes strongly imply this is
how the Payment Links are already configured, but the full purchase →
unlock flow should be tested end-to-end after this deploys.

**Comping a customer now requires appending `?paid=true` themselves** to
whatever content link is sent — a bare link no longer works. The
Stripe-coupon approach (running a comp through a real $0 checkout) is
unaffected and remains the cleaner option, since Stripe's existing
success redirect already appends the parameter automatically.
