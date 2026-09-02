# Deployment

The `_headers` and `_redirects` files use Cloudflare Pages syntax (Netlify
uses the same file names/format, so this would also work there with no
changes).

## `_headers`

- Security headers (`X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`,
  `Referrer-Policy: strict-origin-when-cross-origin`, a restrictive
  `Permissions-Policy`) applied to every path.
- HTML and `/`/`/courses/*/` responses are set to `no-cache, must-revalidate`
  so pages are always revalidated.
- `sitemap.xml` and `robots.txt` get a 1‑hour cache.
- Static assets (`svg`, `ico`, `png`, `webp`, `jpg/jpeg`, `woff/woff2`, `js`,
  `css`) are cached for a year as `immutable`.

## `_redirects`

- `/cmd_sco` and `/cmd_sco/` → `/` (301) — cleaning up a broken inbound link seen in analytics.
- `/quiz/success` → `/quiz?paid=true` (302)
- `/courses/<slug>/success` → `/courses/<slug>/content/` (302) for all three courses.
- Legacy root-level course URLs (`/course-<slug>` and `/course-<slug>.html`) → `/courses/<slug>/` (301 permanent).

## Deploying

1. Push to the `main` branch of this repo.
2. Connect the repo in the Cloudflare Pages dashboard (build command: none;
   output directory: repo root) if not already connected.
3. Cloudflare Pages picks up `_headers` and `_redirects` automatically from
   the root of the deployed output.

## Confirmed live (2026-08-31)

This repo is confirmed connected to a live Cloudflare Pages deployment at
**humanlylabs.org** (canonical) / **www.humanlylabs.org**, auto-deploying
from `main`. Verified by fetching the live site and cross-checking against
the repo:
- The homepage tools grid renders correctly (confirms the `apps.sort` →
  `APPS.sort` critical bug fix from an earlier session is live)
- The Social Landing course landing page reflects course-build-out commits
  (its "20 lessons" hero copy only exists from commit `34e1878` onward)
- Fetching the gated `/content/` pages and individual lesson pages directly
  wasn't possible in that session (they're `noindex`, so they don't surface
  via search, and there was no direct link to fetch from) — worth a manual
  spot-check to fully confirm those render correctly in production.

Cross-checking the live site against the repo also surfaced 3 small stat/
copy bugs on the Social Landing landing page (stray "19"/"4" stats that
hadn't been updated when the course lesson count was fixed) — see
`SESSION_LOG.md` for details.
