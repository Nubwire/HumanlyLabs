# Architecture

## Stack

Plain static HTML/CSS/JS. No framework, no bundler, no `package.json`, no
build step — every page is a self-contained `.html` file with inline
`<style>`/`<script>`. Fonts are loaded from Google Fonts (Fraunces + DM Sans).
Deployment target is Cloudflare Pages (see `_headers` / `_redirects` and
`DEPLOYMENT.md`).

## Page inventory

**Core / legal**
- `index.html` — homepage
- `contact.html`, `privacy.html`, `terms.html`, `404.html`
- `admin.html` — password-gated admin page (`noindex, nofollow`)
- `robots.txt`, `sitemap.xml`, `google5b29484450b089f3.html` (Search Console verification)

**Articles / content**
- `social-anxiety.html`
- `why-socialising-drains-you.html`
- `social-battery.html` / `social-battery-meaning.html`
- `lonely-in-a-relationship.html`
- `avoidant-attachment-style-signs.html`
- `how-to-make-friends-in-your-30s.html`
- `what-to-text-an-old-friend.html`

**Interactive tools** (client-side, several call the Anthropic API directly — see ADR-0003)
- `quiz.html`, `attachment-quiz.html`, `friendship-audit.html`
- `find-your-people.html`, `deep-dive.html`
- `checkin-generator.html`, `conversation-starter.html`
- `mini-course.html`

**Paid courses** — each has a landing page + gated content page
- `courses/social-landing/` (`index.html` + `content/index.html`)
- `courses/confidence-blueprint/` (`index.html` + `content/index.html`)
- `courses/friendship-revival/` (`index.html` + `content/index.html`)

**Assets**
- `images/stickman.jpg`, `og-image.png`, `favicon.svg`

## Purchase / access flow

`_redirects` shows the intended flow: a purchase completes on a payment
provider (not present in this repo — see open questions in
`planning/NEXT_STEPS.md`), which redirects to a `/success` path, which in
turn redirects into the gated `content/` page for that course or tool.

## Notable pattern to be aware of

Several of the interactive tool pages (`social-anxiety.html`,
`friendship-audit.html`, `find-your-people.html`, `checkin-generator.html`,
`conversation-starter.html`, `social-battery.html`, `deep-dive.html`) call
`https://api.anthropic.com/v1/messages` directly from client-side JavaScript
with no API key in the request. This works inside environments that inject
credentials automatically (e.g. Claude's own artifact preview), but a public
static deployment of this site has no such injection — this is flagged as an
open risk in `planning/NEXT_STEPS.md` and `adr/0003-client-side-anthropic-api-calls.md`.
