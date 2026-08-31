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

**Not yet confirmed / not in this repo:** which Cloudflare Pages project this
maps to, custom domain config, and the payment provider that redirects to the
`/success` paths referenced in `_redirects`. See `planning/NEXT_STEPS.md`.
