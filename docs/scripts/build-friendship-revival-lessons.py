#!/usr/bin/env python3
"""
Generates the 18 individual lesson pages for The Friendship Revival course.
Run from its own directory: python3 build-friendship-revival-lessons.py
Source of truth for lesson content lives in this file (LESSONS list below).
"""
import os

OUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "courses", "friendship-revival", "content", "lessons",
)

TOOL_LINKS = {
    "Friendship Audit": ("🗺️", "/friendship-audit"),
    "Attachment Style Quiz": ("🌱", "/attachment-quiz"),
    "Check-In Generator": ("✉️", "/checkin-generator"),
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{lesson_title} — The Friendship Revival — Humanly Labs</title>
  <meta name="robots" content="noindex, nofollow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="preload" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Instrument+Sans:wght@400;500;600&display=swap" as="style" />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --c-bg: #F7F3EC; --c-surface: #FDFCF9;
      --c-ink: #1A1714; --c-ink-2: #4A453F; --c-ink-3: #9B948A;
      --c-border: rgba(26,23,20,.10); --shadow: 0 2px 12px rgba(26,23,20,.07);
      --c-brown: #7A3B19; --c-brown-l: #FEF0E6; --c-brown-b: #E8B48A;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Instrument Sans', sans-serif; background: var(--c-bg); color: var(--c-ink); line-height: 1.65; }}
    nav {{ background: rgba(247,243,236,.95); border-bottom: 1px solid var(--c-border); padding: 0 2rem; position: sticky; top: 0; z-index: 100; }}
    .nav-inner {{ max-width: 760px; margin: 0 auto; height: 60px; display: flex; align-items: center; justify-content: space-between; }}
    .logo {{ font-family: 'Playfair Display', serif; font-size: 20px; color: var(--c-ink); text-decoration: none; }}
    .logo em {{ font-style: italic; color: var(--c-brown); }}
    .logo sup {{ font-size: 9px; color: var(--c-ink-3); vertical-align: super; margin-left: 2px; }}
    .main {{ max-width: 760px; margin: 0 auto; padding: 2.5rem 2rem 6rem; }}
    .breadcrumb {{ font-size: .8rem; color: var(--c-ink-3); margin-bottom: 1.5rem; }}
    .breadcrumb a {{ color: var(--c-brown); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .lesson-meta {{ display: flex; align-items: center; gap: .6rem; margin-bottom: .75rem; flex-wrap: wrap; }}
    .module-badge {{ background: var(--c-brown); color: #fff; border-radius: 8px; padding: 4px 10px; font-size: 11px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; }}
    .lesson-num-badge {{ font-size: 11px; font-weight: 600; color: var(--c-ink-3); }}
    h1.lesson-title {{ font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 500; line-height: 1.25; margin-bottom: .6rem; }}
    .lesson-sub {{ font-size: 1rem; color: var(--c-ink-2); margin-bottom: 2.5rem; padding-bottom: 2rem; border-bottom: 1px solid var(--c-border); }}
    .lesson-body h2 {{ font-family: 'Playfair Display', serif; font-size: 1.35rem; font-weight: 500; margin: 2.25rem 0 .9rem; color: var(--c-ink); }}
    .lesson-body p {{ margin-bottom: 1.1rem; color: var(--c-ink-2); font-size: .98rem; }}
    .lesson-body ul, .lesson-body ol {{ margin: 0 0 1.1rem 1.3rem; color: var(--c-ink-2); font-size: .98rem; }}
    .lesson-body li {{ margin-bottom: .5rem; }}
    .lesson-body strong {{ color: var(--c-ink); }}
    .exercise-box {{ background: var(--c-surface); border: 1px solid var(--c-border); border-left: 4px solid var(--c-brown); border-radius: 12px; padding: 1.5rem 1.75rem; margin: 2rem 0; box-shadow: var(--shadow); }}
    .exercise-box .exercise-label {{ font-size: 11px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: var(--c-brown); margin-bottom: .6rem; }}
    .exercise-box p:last-child {{ margin-bottom: 0; }}
    .tool-box {{ background: var(--c-brown-l); border: 1px solid var(--c-brown-b); border-radius: 12px; padding: 1.25rem 1.5rem; margin: 2rem 0; display: flex; align-items: center; gap: 1rem; }}
    .tool-box .tool-emoji {{ font-size: 1.75rem; flex-shrink: 0; }}
    .tool-box .tool-copy {{ flex: 1; font-size: .9rem; color: var(--c-ink-2); }}
    .tool-box .tool-copy strong {{ color: var(--c-ink); display: block; margin-bottom: 2px; }}
    .tool-box a {{ background: var(--c-brown); color: #fff; text-decoration: none; font-size: .85rem; font-weight: 500; padding: 8px 16px; border-radius: 999px; white-space: nowrap; flex-shrink: 0; }}
    .lesson-nav {{ display: flex; justify-content: space-between; gap: 1rem; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--c-border); }}
    .lesson-nav a {{ font-size: .875rem; color: var(--c-brown); text-decoration: none; font-weight: 500; }}
    .lesson-nav a:hover {{ text-decoration: underline; }}
    .lesson-nav .nav-placeholder {{ color: var(--c-ink-3); font-size: .875rem; }}
    .support-box {{ background: var(--c-surface); border: 1px solid var(--c-border); border-radius: 14px; padding: 1.5rem; margin-top: 3rem; text-align: center; }}
    .support-box p {{ font-size: .875rem; color: var(--c-ink-2); }}
    .support-box a {{ color: var(--c-brown); }}
    footer {{ text-align: center; padding: 2rem; font-size: 12px; color: var(--c-ink-3); border-top: 1px solid var(--c-border); }}
    footer a {{ color: var(--c-ink-3); text-decoration: none; }}
    @media (max-width: 600px) {{ .main {{ padding: 2rem 1.25rem 4rem; }} h1.lesson-title {{ font-size: 1.6rem; }} .tool-box {{ flex-direction: column; align-items: flex-start; }} }}
    a:focus-visible, button:focus-visible {{ outline: 2px solid var(--c-brown); outline-offset: 3px; border-radius: 4px; }}
    @media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} *, *::before, *::after {{ animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }} }}
  </style>
<script>if(location.hostname.endsWith(".pages.dev"))location.replace("https://humanlylabs.org"+location.pathname+location.search+location.hash);</script>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-KMFL61V2FD"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-KMFL61V2FD');
  </script>
  <script src="https://analytics.ahrefs.com/analytics.js" data-key="t8y/ixuqB+gg+9ePJ5VDUA" async></script>
</head>
<body>
<nav>
  <div class="nav-inner">
    <a class="logo" href="/"><em>humanly</em><sup>labs</sup></a>
    <span style="font-size:13px;color:var(--c-ink-3)">🌱 The Friendship Revival</span>
  </div>
</nav>
<main class="main">
  <div class="breadcrumb"><a href="/courses/friendship-revival/content/">← Back to course overview</a></div>
  <div class="lesson-meta">
    <span class="module-badge">Module {module_num} · {module_title}</span>
    <span class="lesson-num-badge">Lesson {lesson_num} of 18</span>
  </div>
  <h1 class="lesson-title">{lesson_title}</h1>
  <p class="lesson-sub">{lesson_sub}</p>
  <div class="lesson-body">
{body}
  </div>
{tool_box}
  <div class="lesson-nav">
    {prev_link}
    {next_link}
  </div>
  <div class="support-box">
    <p>🔒 &nbsp;This page is private — please don't share the URL.<br>
    Questions or issues? <a href="mailto:hello@humanlylabs.org">hello@humanlylabs.org</a></p>
  </div>
</main>
<footer>
  <a href="/">Humanly Labs</a> &nbsp;·&nbsp; <a href="/privacy">Privacy</a> &nbsp;·&nbsp; <a href="/contact">Contact</a>
</footer>
</body>
</html>
"""

LESSONS = []

LESSONS.append({
    "lesson_num": 1, "module_num": 1, "module_title": "The Friendship Audit",
    "lesson_title": "Why Adult Friendships Fade",
    "lesson_sub": "The science of friendship drift and why it accelerates after 30",
    "tool": None,
    "body": """
    <p>If you've noticed your friendships thinning out over the years — fewer close friends than you had a decade ago, relationships that used to feel effortless now requiring real work to sustain, or a nagging sense that your social world has quietly shrunk without any single dramatic cause — you're describing one of the most common, least-discussed patterns of adult life. This course exists because friendship drift is real, well-documented, and, importantly, reversible. This first lesson lays out why it happens, so the rest of the course makes sense as a response to a specific, understood problem rather than a vague effort to "be more social."</p>

    <h2>The structural reasons friendship gets harder</h2>
    <p>Childhood and early adulthood friendships often form and sustain themselves almost automatically, through structures that do most of the work for you: school, university, early shared living situations, a social calendar with far fewer competing demands. These structures provide what researchers call "closed networks" — repeated, low-effort contact with the same people over long stretches of time, which is exactly the condition friendship formation depends on most.</p>
    <p>Adult life systematically removes these structures. Careers, partnerships, children, geographic moves, and the sheer increase in life responsibilities all compete directly for the unstructured time that friendship used to occupy by default. This isn't a personal failing or a sign you've become worse at maintaining relationships — it's a structural, near-universal shift in circumstances that happens to almost everyone, usually accelerating specifically in the decade after 30, when careers, partnerships, and parenting responsibilities tend to compound at once.</p>

    <h2>Why friendship specifically, rather than other relationships</h2>
    <p>It's worth noting why friendship, among all relationship types, tends to erode fastest under this pressure. Romantic partnerships and family relationships often come with built-in structural reinforcement — shared living space, legal or familial obligation, ongoing contact that doesn't require much deliberate effort to sustain. Friendship, by contrast, is almost entirely voluntary and unstructured; nothing forces continued contact the way marriage or parenthood does. This makes it uniquely vulnerable to the busyness and structural changes of adult life — not because friendship matters less, but because it has the least built-in scaffolding holding it in place once life gets more demanding.</p>

    <h2>Drift is usually mutual and rarely anyone's fault</h2>
    <p>One of the more relieving things to understand about friendship drift is that it's almost always a two-sided, gradual process rather than a deliberate choice by either person. Two people who were once close don't typically decide to stop being friends — they simply both get busier, both let contact space out slightly, and that slight spacing compounds over months and years into significant distance, without either person ever consciously deciding this outcome. Understanding this mutual, structural nature of drift matters because it removes a lot of unnecessary shame from the equation — reaching back out to a drifted friend isn't admitting a personal failure; it's addressing a completely ordinary structural gap that affects nearly everyone.</p>

    <h2>The good news: this course's entire premise</h2>
    <p>Because friendship drift is largely structural rather than personal, it responds well to structural intervention — which is exactly what this course provides. You can't simply wait for your twenties' social conditions to return, but you can deliberately rebuild the elements that made friendship easy back then: regular contact, shared activity, and lower-effort ways of staying connected that fit realistically into an adult schedule. The rest of this course is built around that principle, module by module.</p>

    <h2>What this course won't ask of you</h2>
    <p>This isn't a course about manufacturing an artificially large social circle or treating every relationship as a project to optimise. It's built around a much simpler premise: friendship, like most valuable things in adult life, tends to require deliberate maintenance once the automatic structures of youth fall away, and deliberate maintenance is a learnable skill, not a personality trait some people have and others simply lack. You'll work through this at your own pace, focused on the specific relationships that matter most to you, not an abstract goal of maximising your total number of connections.</p>
    <p>It's also worth being upfront that this course draws on established research in social psychology and relationship science — attachment theory, self-disclosure research, weak-tie and dormant-tie studies — translated into practical steps you can actually apply. None of it requires you to become a fundamentally different, more extroverted person. The goal throughout is a social world that genuinely fits your actual life and personality, not an imagined ideal borrowed from somewhere else.</p>

    <h2>How this course is organised</h2>
    <p>Each module builds on the one before it: Module 1 gives you an honest map of your current social world, Module 2 helps you understand your own relational patterns, Module 3 focuses on reviving connections that have gone quiet, Module 4 on deepening the ones you already have, Module 5 on forming genuinely new ones, and Module 6 on maintaining everything you've built well beyond this course's twelve weeks. Working through them in this order matters, since later modules assume the self-understanding and mapping work from the earlier ones — even if a later module feels more urgently relevant to your current situation, the groundwork pays off.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Think of one friendship that's drifted over the past few years — someone you were once close to but rarely speak with now. Write one honest sentence about what structural change (a move, a job shift, a new relationship, kids) most likely explains the drift, rather than any personal falling-out.</p>
    </div>

    <p>The next lesson turns this understanding into something concrete: a full audit of your current social world, so you have a clear, honest map to work from for the rest of the course.</p>
    """,
})

LESSONS.append({
    "lesson_num": 2, "module_num": 1, "module_title": "The Friendship Audit",
    "lesson_title": "Your Social World Map",
    "lesson_sub": "Audit your current relationships: who nourishes, who drains, who's been lost",
    "tool": "Friendship Audit",
    "body": """
    <p>With the structural picture from Lesson 1 in mind, this lesson is about building an honest, specific map of your current social world — not a vague sense of "I don't have enough friends," but a concrete inventory you can actually work with for the rest of this course. Most people carry around an impression of their social life that's considerably less accurate than they assume, usually skewed toward either overestimating how connected they are (based on a large but shallow contact list) or underestimating it (based on how few people they've seen recently, ignoring dormant but real relationships).</p>

    <h2>Three categories worth mapping</h2>
    <p>As you build your map, it's useful to sort your current and past relationships into three categories, since each calls for a different kind of attention in the modules ahead:</p>
    <ul>
      <li><strong>Nourishing relationships</strong> — people who leave you feeling energised, supported, or genuinely glad you spent time with them, whether you see them often or rarely.</li>
      <li><strong>Draining relationships</strong> — people you maintain contact with more out of habit or obligation than genuine desire, where interactions leave you feeling depleted rather than restored.</li>
      <li><strong>Dormant relationships</strong> — people you were once genuinely close to, where the connection has simply gone quiet through the structural drift covered in Lesson 1, rather than through any conflict or genuine falling-out.</li>
    </ul>
    <p>Most people's honest social maps contain a mix of all three, often in surprising proportions — it's common to discover more dormant, genuinely revivable relationships than expected, and to notice one or two draining relationships that have simply been running on autopilot far longer than they've actually been enjoyable.</p>

    <h2>Why nourishing vs. draining matters for this course</h2>
    <p>It's worth being honest about the draining category specifically, since a lot of people carry some guilt around even acknowledging it. Not every relationship needs equal ongoing investment, and recognising that a specific relationship has become more obligation than genuine connection isn't a character flaw — it's useful, accurate information. This course isn't about maximising the total number of relationships you maintain; it's about deliberately investing more in the ones worth investing in, which requires being honest about which ones those actually are.</p>

    <h2>Don't rush past the dormant category</h2>
    <p>The dormant category deserves particular attention, because it's usually the most underrated resource in most people's social world. A friendship that was once genuinely close but has gone quiet for years still carries real accumulated history and trust — the "200 hours" or more of shared time that built the original closeness doesn't fully disappear just because contact has lapsed. Module 3 of this course is built entirely around this category, because reviving a dormant tie is often, counterintuitively, considerably easier than building a brand-new friendship from nothing.</p>

    <h2>Use the Friendship Audit for a structured version of this map</h2>
    <p>The Friendship Audit tool below runs a more structured, thorough version of this mapping process than you can easily do from memory alone — helping you systematically categorise your current relationships and surface people, especially in the dormant category, who might not have come to mind unprompted. Take it now, and be honest rather than aspirational about where each relationship currently sits.</p>

    <h2>Common surprises when people actually do this exercise</h2>
    <p>A few patterns show up often enough to be worth naming in advance. People frequently discover they have more nourishing relationships than their day-to-day mood suggests, simply because the most recent or most vivid interactions (which might have been mildly draining) skew the overall impression more than the quieter, steadier nourishing ones do. People also often discover a genuine surprise in the dormant category — a name they hadn't consciously thought about in a while, but who, once written down, clearly still carries real weight and warmth. And it's common to find one or two long-standing relationships in the draining category that have simply never been questioned, purely out of habit or a sense of obligation built up over years.</p>
    <p>None of these discoveries require immediate action — the point of this lesson is accurate mapping, not immediate restructuring of your entire social world. The action comes in later modules, once you have a genuinely honest map to work from.</p>

    <h2>Keep the map private and honest</h2>
    <p>Since this map involves being genuinely honest about relationships, including uncomfortable admissions like a long-standing friendship having become more draining than nourishing, it's worth keeping this particular exercise private rather than something you'd share directly with the people involved. The value here is in your own clear-eyed understanding, which then informs how you choose to invest your time and energy going forward — not in delivering blunt feedback to anyone about where they currently sit in your assessment.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>After completing the audit, pick three names total — one nourishing relationship you'd like to invest more in, one draining relationship worth reconsidering, and one dormant relationship you'd genuinely like to revive. Keep this list; it becomes working material for the rest of the course.</p>
    </div>

    <p>The next lesson refines this map further, looking specifically at which relationships have real depth potential versus which are likely to stay comfortably surface-level — a distinction that will shape where you focus your energy in the modules ahead.</p>
    """,
})

LESSONS.append({
    "lesson_num": 3, "module_num": 1, "module_title": "The Friendship Audit",
    "lesson_title": "The Intimacy Gap",
    "lesson_sub": "Identifying which relationships have depth potential vs true acquaintances",
    "tool": None,
    "body": """
    <p>Not every relationship in your social world is meant to become, or capable of becoming, a deep friendship — and recognising this distinction clearly is genuinely useful, because it prevents you from either neglecting relationships with real depth potential or over-investing in ones that are unlikely to go there regardless of effort. This lesson is about identifying the difference, using a framework that will keep showing up throughout the rest of the course.</p>

    <h2>The intimacy gap defined</h2>
    <p>Every relationship carries some gap between its current level of depth and its potential depth — how close it could plausibly become if both people invested in it. A workplace acquaintance you enjoy talking to but have never seen outside work might have real, unexplored potential; a friendly neighbour you exchange pleasantries with might have already reached close to their realistic ceiling of depth given the nature of the relationship. Neither is a problem — the issue only arises when you're investing effort as though a relationship has more potential than it realistically does, or neglecting one that has real, untapped potential simply because it hasn't been actively pursued yet.</p>

    <h2>Signals of genuine depth potential</h2>
    <p>A few signals are worth weighing when assessing a specific relationship's potential, though none is decisive on its own:</p>
    <ul>
      <li><strong>Reciprocal curiosity</strong> — do they ask about your life, follow up on things you've mentioned, seem genuinely interested rather than just polite?</li>
      <li><strong>Comfortable silence or informality</strong> — can the interaction relax into something less performed, or does it stay consistently surface-level and formal no matter how many times you interact?</li>
      <li><strong>Shared values or genuine overlap</strong> — beyond the specific context you know them from (work, a class, a mutual friend), is there a real point of connection that could sustain a relationship outside that context?</li>
      <li><strong>Willingness to extend beyond the original context</strong> — have they shown any interest in interacting outside the setting where you originally met, even in small ways?</li>
    </ul>
    <p>A relationship showing several of these signals is usually worth deliberate investment; one showing few of them, despite pleasant regular contact, may simply be a well-functioning acquaintance-level relationship, which is a genuinely fine thing for a relationship to be — not everything needs to become a close friendship to have value.</p>

    <h2>True acquaintances have real value too</h2>
    <p>It's worth pushing back directly on the implicit idea that only close friendships count as worthwhile connection. A wide network of pleasant acquaintances contributes meaningfully to a sense of belonging and community, provides the kind of casual social contact covered in the concept of social loneliness elsewhere on this platform, and, per weak-tie research, is often more useful than close friends for practical things like introductions, recommendations, and general life texture. This course focuses heavily on deepening relationships with real potential, but that doesn't mean acquaintance-level relationships are lesser or in need of "fixing" — they're simply a different, equally legitimate category.</p>

    <h2>Applying this to your Lesson 2 map</h2>
    <p>Go back through the relationships you mapped in Lesson 2, particularly anything you marked as nourishing or dormant, and apply the intimacy-gap lens: which ones show real signals of unexplored depth potential, worth the deliberate investment covered in Modules 3 and 4? Which ones are functioning well exactly as they are, at their current level, with no particular need to push further? Being honest about this distinction now will make the rest of the course's advice land much more precisely, since deepening techniques work best applied to relationships that genuinely have room to deepen.</p>

    <h2>Potential can be misjudged in both directions</h2>
    <p>It's worth being aware that this assessment is genuinely fallible in both directions. Sometimes a relationship that seems purely surface-level turns out to have real depth potential once someone actually tests it with a slightly more personal question or a genuine invitation — the surface quality was simply a function of neither person having tried yet, not a fixed ceiling. Conversely, a relationship that seems to have obvious potential on paper (shared interests, pleasant regular contact) can sometimes plateau despite real effort, for reasons that have more to do with the other person's current capacity or life circumstances than anything about the relationship's inherent potential. Treat your initial assessment as a reasonable starting hypothesis, worth testing through actual effort in the modules ahead, rather than a fixed and final verdict.</p>

    <h2>Context can mask or reveal potential</h2>
    <p>It's worth noting that the specific context you know someone from can sometimes obscure real potential rather than reveal it — a work relationship, for instance, often stays within a narrower professional register regardless of genuine underlying compatibility, simply because the context doesn't naturally invite anything more personal. This means context alone is a weak signal on its own; the more reliable signals are the ones listed above, which can show up even within a fairly formal or narrow original context, hinting at potential the setting itself hasn't yet allowed to surface.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Pick two relationships from your Lesson 2 map — one you suspect has real depth potential, one you suspect is comfortably at its ceiling as an acquaintance. Write one sentence for each explaining your read, using the signals above. You'll return to this distinction directly in Module 4.</p>
    </div>

    <p>You now have a full, honest map of your social world and a framework for where real depth potential exists. Module 2 turns inward — looking at your own relational patterns, specifically your attachment style, and how it shapes the way you form and sustain friendships.</p>
    """,
})

LESSONS.append({
    "lesson_num": 4, "module_num": 2, "module_title": "Understanding Your Pattern",
    "lesson_title": "Your Attachment Style",
    "lesson_sub": "How early relational patterns shape how you form friendships today",
    "tool": "Attachment Style Quiz",
    "body": """
    <p>Attachment theory was originally developed to describe the bond between infants and caregivers, but decades of subsequent research have shown that the same underlying patterns — how comfortable we are with closeness, how we handle uncertainty in a relationship, how we respond to distance or conflict — show up throughout adult relationships, friendships very much included, not just romantic partnerships. This lesson introduces the framework, since it'll be genuinely useful context for the rest of this module and much of what follows.</p>

    <h2>A brief note on how to use this framework</h2>
    <p>Before going further, it's worth being clear about what attachment style is and isn't. It's a descriptive framework for a general pattern of tendencies, not a fixed, permanent label or a clinical diagnosis. Most people show some blend of tendencies rather than fitting neatly into one pure category, and — importantly, and covered directly in Lesson 6 — attachment patterns are not fixed for life. They're shaped by early experience but remain genuinely responsive to new experience throughout adulthood, which is the entire premise behind this module being useful at all.</p>

    <h2>The three broad patterns</h2>
    <p><strong>Secure attachment</strong> generally involves relative comfort with both closeness and independence — reasonably confident that relationships are stable, able to communicate needs directly, not overly anxious about a friend pulling back and not automatically avoidant of getting close. This is the pattern most associated with straightforward, low-friction friendship formation and maintenance.</p>
    <p><strong>Anxious attachment</strong> tends to involve a heightened sensitivity to signs of distance or rejection, a stronger need for reassurance and consistent contact, and sometimes a tendency to read ambiguous signals (a slow reply, a cancelled plan) in a more threatening light than the situation necessarily warrants.</p>
    <p><strong>Avoidant attachment</strong> tends to involve more discomfort with closeness and vulnerability, a stronger pull toward independence and self-reliance even when connection is genuinely wanted, and sometimes a tendency to create distance — consciously or not — when a relationship starts feeling too close or demanding.</p>
    <p>The next lesson goes into much more depth on how each of these specifically shows up in adult friendship, and where each tends to get stuck.</p>

    <h2>Why this matters for the rest of the course</h2>
    <p>Understanding your own general pattern helps make sense of specific difficulties you might already recognise in your friendship history — a recurring tendency to pull away once a friendship starts feeling significant, a recurring pattern of anxiety when a friend goes quiet, or a general sense of unease around vulnerability that keeps relationships comfortably shallow. None of these patterns are character flaws; they're learned tendencies, shaped by early relational experience, and — like the other patterns covered throughout this course — genuinely responsive to deliberate, informed effort.</p>

    <h2>Use the Attachment Style Quiz for a structured read</h2>
    <p>The Attachment Style Quiz tool below gives you a structured assessment of your own general tendencies, rather than relying on self-diagnosis from a brief lesson description. Take it now, answering based on your general pattern across relationships (not just one specific friendship), and hold the result loosely — as a useful starting lens, not a fixed identity.</p>

    <h2>Where these patterns originally come from</h2>
    <p>Without going too deep into developmental theory, it's worth knowing the general origin story: these patterns are thought to develop through early, repeated experiences of how reliably a caregiver responded to a child's needs for closeness and comfort. Consistent, attuned responsiveness tends to produce a more secure baseline; inconsistent or unpredictable responsiveness tends to produce a more anxious baseline; consistently dismissive or unavailable responsiveness tends to produce a more avoidant baseline. None of this is about blame — caregiving happens under real constraints, and the resulting pattern is simply an adaptive response to whatever conditions were actually present, not a reflection of anyone's failure, including your own as an adult navigating the pattern you inherited.</p>

    <h2>Attachment style and social anxiety are related but distinct</h2>
    <p>If you're familiar with the social-anxiety-focused course material elsewhere on this platform, it's worth distinguishing attachment style from social anxiety directly, since they can sometimes look similar from the outside. Social anxiety is primarily about fear of judgment and evaluation in social performance situations; attachment style is primarily about comfort with closeness and vulnerability specifically within ongoing relationships. It's entirely possible to have low social anxiety (comfortable meeting new people, fine speaking in groups) while still carrying a more anxious or avoidant attachment pattern once a relationship starts requiring genuine emotional closeness, and vice versa. They can compound each other, but they're separate systems worth understanding on their own terms.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Before taking the quiz, jot down your own guess at your dominant pattern, based on the three descriptions above. After taking it, compare your guess to the result — noting any surprise is itself useful information about blind spots in your own self-perception.</p>
    </div>

    <p>The next lesson goes deeper into how each of these three patterns specifically plays out in adult friendship — not just in the abstract, but in the concrete moments and decisions that shape how a friendship develops or stalls.</p>
    """,
})

LESSONS.append({
    "lesson_num": 5, "module_num": 2, "module_title": "Understanding Your Pattern",
    "lesson_title": "Anxious, Avoidant & Secure",
    "lesson_sub": "What each style looks like in adult friendship and where it gets stuck",
    "tool": None,
    "body": """
    <p>Now that you have a working sense of your own general pattern from Lesson 4, this lesson gets specific about how each attachment style actually shows up in the day-to-day reality of adult friendship — the concrete moments, decisions, and sticking points, rather than the abstract description. Recognising your own specific patterns in these examples tends to be far more useful than the general framework alone.</p>

    <h2>Anxious patterns in friendship</h2>
    <p>In practice, an anxious pattern in friendship often looks like: reading a delayed reply as a sign of waning interest rather than simple busyness; feeling a strong pull to reach out repeatedly for reassurance when a friendship feels uncertain; over-analysing a friend's tone or wording for hidden meaning; feeling disproportionately hurt by a cancelled plan; or sometimes overextending yourself for a friend's approval in a way that isn't sustainable. The underlying difficulty here isn't caring too much — caring about friendships is a strength — it's a heightened, often inaccurate threat-detection system around connection, similar in structure to the social-anxiety patterns covered elsewhere on this platform, but specifically triggered by relational uncertainty rather than social performance.</p>
    <p>The specific sticking point for this pattern tends to be: genuine closeness is available, but it's accompanied by enough anxiety and need for reassurance that it can, ironically, strain the very relationships it's trying hardest to protect.</p>

    <h2>Avoidant patterns in friendship</h2>
    <p>An avoidant pattern often looks like: pulling back or creating distance once a friendship starts feeling significant or demanding; strong discomfort with vulnerability or emotional conversation, often redirecting toward lighter or more practical topics; a tendency to let friendships lapse rather than actively working through a moment of friction; genuinely valuing friendship while still finding consistent closeness effortful or slightly threatening to a sense of independence. This isn't the same as simply being introverted or preferring less social contact — plenty of people with avoidant patterns want closeness and connection, but something in the pattern makes sustained closeness feel effortful or even risky, leading to a kind of unconscious self-sabotage of relationships they do genuinely value.</p>
    <p>The specific sticking point here tends to be: friendships plateau at a comfortable, moderate depth and rarely progress further, not because the other person isn't interested in going deeper, but because the avoidant pattern quietly resists the vulnerability that deeper connection requires.</p>

    <h2>Secure patterns in friendship</h2>
    <p>A secure pattern tends to look like: reasonable comfort with both closeness and independence; a default assumption that ambiguous signals (a slow reply, a quiet stretch) don't mean something is wrong, absent clearer evidence; a willingness to communicate directly about a friendship issue rather than either anxious escalation or avoidant withdrawal; general resilience in the face of normal relationship friction. It's worth being clear that secure attachment isn't the absence of relational difficulty — securely attached people still navigate real friendship challenges — it's more that the underlying interpretive lens tends to be more accurate and less threat-oriented by default.</p>

    <h2>Most people show a mix</h2>
    <p>It's genuinely common to show a more secure pattern in some relationships and a more anxious or avoidant pattern in others, depending on the specific history and dynamics with that particular person — your pattern with an old childhood friend might look quite different from your pattern with a newer connection still being established. This variability is normal and worth noting as you go through the rest of this module, rather than assuming a single fixed pattern applies uniformly across your entire social world.</p>

    <h2>Why naming your pattern accurately matters</h2>
    <p>It's worth being honest that recognising your own pattern in these descriptions can occasionally feel uncomfortable, or even a bit like a diagnosis of a personal flaw. It's worth resisting that framing directly. Every one of these patterns represents an understandable, once-adaptive response to real early circumstances, and every one of them is genuinely workable, per the next lesson. Accurate recognition is the necessary first step toward change — a pattern that stays unnamed and unexamined tends to keep running on autopilot indefinitely, while a clearly named pattern becomes something you can actually work with deliberately.</p>

    <h2>How each pattern experiences the other</h2>
    <p>It's worth noting a specific, common dynamic: an anxious and an avoidant pattern paired together in a friendship can inadvertently reinforce each other's difficulties, since the anxious person's pursuit of reassurance can feel overwhelming to the avoidant person, prompting more withdrawal, which in turn heightens the anxious person's alarm, prompting more pursuit. Recognising this specific dynamic, if it applies to a friendship in your own life, is useful precisely because it explains a frustrating pattern that can otherwise feel confusing or seem like evidence the relationship simply isn't working, when it's really just two understandable patterns interacting in a predictable, nameable way.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Pick one friendship where you notice a clear pattern — anxious, avoidant, or otherwise — and write down one specific recent moment where that pattern showed up concretely (a message you over-analysed, a conversation you steered away from something vulnerable, a plan you avoided making). Specificity here will make the next lesson's techniques far more directly applicable.</p>
    </div>

    <p>The final lesson in this module addresses the genuinely important question this naturally raises: can these patterns actually change, and if so, how? The evidence-based answer is yes, and the next lesson covers exactly how.</p>
    """,
})

LESSONS.append({
    "lesson_num": 6, "module_num": 2, "module_title": "Understanding Your Pattern",
    "lesson_title": "Changing the Pattern",
    "lesson_sub": "Evidence-based strategies for earned security in adult relationships",
    "tool": None,
    "body": """
    <p>Attachment patterns, formed largely through early experience, can feel like fixed facts about who you are — but a substantial body of research on what's often called "earned security" shows clearly that these patterns remain genuinely changeable throughout adulthood, through consistent new relational experience and deliberate effort. This closing lesson of Module 2 is about the practical mechanics of that change, since understanding your pattern (Lessons 4 and 5) is only useful if paired with an actual path toward working with it differently.</p>

    <h2>What "earned security" actually means</h2>
    <p>Earned security describes the process by which someone with a more anxious or avoidant baseline pattern develops meaningfully more secure functioning over time, typically through some combination of consistent, trustworthy relational experiences (friendships, partnerships, or therapeutic relationships that repeatedly disconfirm the old anxious or avoidant predictions) and deliberate, conscious effort to notice and interrupt the old pattern in real time. This isn't a quick process, and it isn't about erasing the original pattern entirely — it's closer to building a more secure pattern alongside the old one, which gradually becomes the more dominant, default response with enough consistent practice and reinforcement.</p>

    <h2>Practical strategies for an anxious pattern</h2>
    <p>If Lesson 5's anxious pattern resonated, a few concrete practices tend to help: deliberately pausing before acting on an anxious interpretation of an ambiguous signal (a slow reply, a quiet stretch) and considering at least one alternative, more benign explanation before responding; communicating a need directly rather than through indirect signals or repeated reassurance-seeking ("I've noticed I get a bit anxious when plans are vague — could we set a specific time?" tends to land far better than passive-aggressive hints or repeated check-ins); and practising tolerating some genuine uncertainty in a relationship without needing it immediately resolved, building the evidence over time that uncertainty doesn't automatically mean something is wrong.</p>

    <h2>Practical strategies for an avoidant pattern</h2>
    <p>If Lesson 5's avoidant pattern resonated more, useful practices include: deliberately staying present in a conversation that's starting to feel too vulnerable or close, rather than automatically redirecting to lighter territory, even when it feels uncomfortable; practising small, low-stakes moments of genuine disclosure rather than either full avoidance or overwhelming oversharing (Lesson 11 covers this specific skill in depth); and noticing the urge to create distance when a friendship starts feeling significant, and experimenting with staying engaged instead, even briefly, as a way of building new evidence against the underlying belief that closeness is inherently threatening or overwhelming.</p>

    <h2>This is gradual, evidence-based work, not a mindset shift</h2>
    <p>It's worth being realistic about the timeline here: attachment patterns built over years or decades don't shift after a single conscious effort or a single good conversation. Like the exposure-based work covered in other Humanly Labs courses, earned security tends to build through repeated, consistent practice and repeated disconfirming evidence, not through insight alone. Understanding your pattern intellectually, from Lessons 4 and 5, is a genuinely useful start, but the actual change comes from applying these practical strategies repeatedly, in real relationships, over an extended period.</p>

    <h2>A note on relationships that reinforce the old pattern</h2>
    <p>It's worth being honest that not every relationship supports this kind of growth equally well. A friendship with someone who's reliably dismissive of vulnerability, or reliably inconsistent in a way that reinforces anxious hypervigilance, makes earned security considerably harder to build within that specific relationship, regardless of your own effort. This is part of why Lesson 3's intimacy-gap assessment matters — investing your growth-oriented effort in relationships that are genuinely capable of supporting it tends to produce far better results than trying to force change within a relationship that structurally works against it.</p>

    <h2>Progress here is measured in reduced frequency, not elimination</h2>
    <p>It's worth setting a realistic marker of progress for this specific work: you're unlikely to eliminate an anxious or avoidant pattern entirely, and that's not actually the goal. A more realistic and genuinely meaningful marker of progress is noticing the old pattern activate less often, catching it more quickly when it does, and having a wider range of alternative responses available in the moment, rather than defaulting automatically to the old pattern every time. Over months of consistent practice, per the earned-security research, this gradual shift compounds into a genuinely different default way of relating, even without ever reaching some final, permanent state of pure security.</p>

    <h2>A note on when outside support helps this work</h2>
    <p>For patterns that feel especially entrenched, or that trace back to more significant early relational difficulty, working through this specifically with a therapist — particularly one experienced in attachment-focused approaches — can meaningfully accelerate the earned-security process beyond what self-directed practice alone typically achieves. This isn't a sign the self-directed approach in this lesson doesn't work; it's simply that a skilled outside perspective can sometimes see patterns and offer real-time practice that's harder to access working entirely on your own.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Using the specific moment you identified in Lesson 5's exercise, write one sentence describing what you'd do differently next time using the strategies above — a specific, concrete alternative response, not a general intention to "be more secure."</p>
    </div>

    <p>You now understand your own relational patterns and have concrete strategies for working with them. Module 3 puts this self-understanding into direct action — reviving the dormant connections you identified back in Lesson 2.</p>
    """,
})

LESSONS.append({
    "lesson_num": 7, "module_num": 3, "module_title": "Reviving Dormant Connections",
    "lesson_title": "The Dormant Tie Opportunity",
    "lesson_sub": "Why reconnecting with old friends is often easier than forming new ones",
    "tool": None,
    "body": """
    <p>Of everything in your Lesson 2 social world map, the dormant category is arguably the most underused resource most people have available to them — and this lesson makes the case, directly and specifically, for why reviving an old friendship is often genuinely easier and faster than building a new one from nothing, even though it can feel more daunting at first.</p>

    <h2>What actually stays intact during dormancy</h2>
    <p>When a friendship goes quiet through the structural drift covered in Lesson 1, a lot of what made it valuable doesn't actually disappear — it goes dormant, not extinct. Shared history, established trust, inside knowledge of each other's personality and life, a track record of enjoying each other's company: all of this remains largely intact, simply unused for a stretch of time. This is fundamentally different from starting a new friendship from zero, which requires building all of this from scratch, typically over the "50 to 200 hours" timeline that friendship formation research commonly cites.</p>

    <h2>Research on dormant ties</h2>
    <p>Organisational psychology research on "dormant ties" — a term originally used to describe professional networks, but with clear parallels to personal friendship — has found something worth knowing directly: people often significantly underestimate how valuable and how receptive dormant connections are, and correspondingly underestimate how well a re-connection will be received. The awkwardness anticipated before reaching out to a long-silent friend is, in study after study, consistently rated as far higher beforehand than it's rated as having actually been, after the fact, by the people who do the reaching out.</p>

    <h2>Why the anticipation feels so much worse than the reality</h2>
    <p>A few specific anxious predictions tend to drive the hesitation around reaching out to a dormant tie: "too much time has passed, it'll be awkward," "they've probably moved on and don't think about me," "reaching out after so long will seem strange or out of nowhere." Each of these deserves scrutiny. Time alone rarely erodes genuine past closeness as much as it feels like it should — the shared history doesn't expire. Most people, when reflecting honestly, still think fondly of former close friends even after years of silence, simply because the drift wasn't a conscious rejection (per Lesson 1) but a structural, mutual lapse. And an unprompted, warm reach-out after time apart is, for most people, a pleasant surprise rather than a strange intrusion — it's far more common to be flattered that someone thought of you after time apart than to be bothered by it.</p>

    <h2>Which dormant ties are worth prioritising</h2>
    <p>Not every dormant tie is equally worth reviving — the same intimacy-gap thinking from Lesson 3 applies here. The strongest candidates tend to be relationships that had genuine depth before going quiet (not just proximity-based acquaintances who happened to fade, per the natural course of things), relationships that ended through structural drift rather than genuine conflict or incompatibility, and relationships you find yourself still thinking about occasionally, which is often a reliable signal of real remaining value even after years of no contact.</p>

    <h2>Setting realistic expectations for the revival itself</h2>
    <p>It's worth noting that reviving a dormant tie doesn't necessarily mean picking up exactly where you left off immediately — there's often a brief re-acclimation period, catching each other up on years of life change, before the relationship settles back into something comfortable. This is normal and expected, not a sign the revival isn't working. The underlying trust and history tend to make this re-acclimation considerably faster than building trust from zero, but it's rarely instantaneous.</p>

    <h2>A specific example worth holding onto</h2>
    <p>It can help to picture a concrete version of this: someone you were genuinely close to years ago — maybe from an earlier job, an earlier city, an earlier life stage — who you haven't spoken to in a long stretch, not because anything went wrong, but because life simply pulled you in different directions. The version of that person who knew you well, laughed at the same things, understood context about your life that newer acquaintances don't have — that version hasn't disappeared. It's simply been waiting, largely intact, for renewed contact. This is worth holding onto specifically because it's easy to unconsciously picture a dormant tie as something that has decayed or expired, when the more accurate picture is closer to something paused, fully available to pick back up.</p>

    <h2>Dormant ties as an underused resource in general</h2>
    <p>It's worth zooming out briefly: across an average adult life, most people accumulate a genuinely large number of dormant ties — friendships from school, earlier jobs, earlier cities, earlier life stages — far more than the small number of active friendships they currently maintain. This means the dormant category isn't just one or two names; for most people, it's a substantial, largely untapped reservoir of relationships with real accumulated history, available to draw on well beyond just the single most obvious candidate.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>From your Lesson 2 dormant list, pick the one relationship you find yourself thinking about most, or feel the strongest pull to reconnect with. Write down what specifically drew you to them originally — this becomes useful material for the actual message in the next lesson.</p>
    </div>

    <p>The next lesson gets practical: exactly how to write and send that first message after a long silence, in a way that feels natural rather than strange.</p>
    """,
})

LESSONS.append({
    "lesson_num": 8, "module_num": 3, "module_title": "Reviving Dormant Connections",
    "lesson_title": "The First Message",
    "lesson_sub": "How to reach out after years of silence without it feeling strange",
    "tool": "Check-In Generator",
    "body": """
    <p>Understanding that dormant ties are genuinely worth reviving, from Lesson 7, is one thing — actually writing and sending that first message after a long silence is another, and it's a common place for good intentions to stall out indefinitely. This lesson gives you concrete guidance for that specific message.</p>

    <h2>What makes a reconnection message land well</h2>
    <p>A few consistent elements distinguish a message that lands naturally from one that feels awkward or is easy to leave unanswered:</p>
    <ul>
      <li><strong>Acknowledge the gap briefly, without over-apologising</strong> — "it's been way too long" is enough; an elaborate, guilty explanation for the silence tends to add unnecessary weight rather than lightening the message.</li>
      <li><strong>Reference something specific and genuine</strong> — a shared memory, something that reminded you of them recently, a genuine reason you thought of them. This does far more work than a generic "hey, how are you," which is easy to leave sitting unanswered.</li>
      <li><strong>Keep the ask small and low-pressure</strong> — you're not asking to rebuild the whole friendship in one message; a simple "would love to catch up sometime" or a specific, easy suggestion is enough for a first message.</li>
      <li><strong>Warmth over cleverness</strong> — this isn't a moment for a perfectly crafted message; genuine warmth reads far better than anything overly polished or performative.</li>
    </ul>

    <h2>A worked example</h2>
    <p>Something like: "Hey! I was just thinking about [specific shared memory or reference] and it made me realise it's been way too long since we caught up. How have you been? Would genuinely love to hear what's new with you sometime." This covers all four elements above — brief acknowledgment, specific reference, warmth, and a low-pressure opening rather than an immediate demand for a scheduled hangout.</p>

    <h2>Handling the anxious predictions directly</h2>
    <p>If sending this message feels harder than it seems like it should, per the research covered in Lesson 7, it's worth explicitly naming the specific anxious prediction driving the hesitation and checking it against the evidence: what's actually likely to happen if you send this, versus what your anxious prediction assumes? In the vast majority of cases, the realistic range of outcomes runs from "a warm, genuinely happy response" to, at worst, "a slower or more lukewarm response than hoped, for reasons that likely have nothing to do with you specifically." Very rarely does reaching out after time apart produce a genuinely negative reaction — the actual downside risk is much smaller than anticipatory anxiety tends to suggest.</p>

    <h2>What if there's no response, or a slow one?</h2>
    <p>It's worth preparing for this possibility without over-interpreting it. People are busy, message notifications get buried, and a slow or absent response says considerably less about the relationship's potential than it feels like it does in the moment. A reasonable approach: if there's no response after a week or two, it's fine to leave it there without pressure, or to send one more brief, equally low-pressure follow-up later. Either way, a single non-response isn't strong evidence the relationship isn't worth pursuing — treat it the same way you'd treat any other single data point, not a final verdict.</p>

    <h2>Use the Check-In Generator for a starting draft</h2>
    <p>The Check-In Generator tool below can help you draft this specific message if you're finding it hard to get started — describe who you're reaching out to and roughly how long it's been, and it'll generate a few natural options you can adjust to sound genuinely like you, rather than staring at a blank message box indefinitely.</p>

    <h2>What to avoid in a first message</h2>
    <p>A few things tend to work against a good first message, worth avoiding deliberately: an overly formal or stiff tone that doesn't match how you actually used to talk to this person; a message so long and detailed it reads more like a life update essay than an invitation to reconnect, which can feel like a lot to respond to; or an immediate, specific plan request before any actual back-and-forth has happened ("free for dinner Thursday?" cold, with no preceding exchange, can feel like a bigger ask than the relationship currently supports after a long silence). A shorter, warmer, more open message tends to outperform a longer, more detailed one at this specific stage.</p>

    <h2>Adjusting the tone for different lengths of silence</h2>
    <p>The basic structure above scales reasonably well from a silence of a year to one of a decade or more, but it's worth acknowledging the length more directly the longer the gap has been — a brief, light "it's been way too long" works fine for a year or two of silence, while acknowledging it a bit more explicitly ("I can't believe it's been this many years") tends to feel more genuine for a much longer gap, rather than treating a decade of silence with the same casual brevity you'd use for a few months.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Using the person you identified in Lesson 7's exercise, draft and actually send a first message this week, following the pattern above. Notice, afterward, how the actual experience of sending it compares to how daunting it felt beforehand.</p>
    </div>

    <p>The next lesson addresses what happens after that first message lands — how to tell which revived connections are worth continuing to pursue, and which might be better let go of gracefully.</p>
    """,
})

LESSONS.append({
    "lesson_num": 9, "module_num": 3, "module_title": "Reviving Dormant Connections",
    "lesson_title": "Reviving vs Releasing",
    "lesson_sub": "How to tell which dormant friendships are worth pursuing",
    "tool": None,
    "body": """
    <p>Not every dormant tie you reach out to will turn out to be worth actively reviving, and that's a completely normal, expected outcome rather than a failure of the process covered in the last two lessons. This closing lesson of Module 3 is about reading the early signals honestly, so you invest your limited time and energy in the revivals that genuinely have momentum, while gracefully letting go of the ones that don't.</p>

    <h2>Signals worth reviving</h2>
    <p>A few things tend to indicate genuine mutual momentum after that first message: a warm, reasonably prompt response that shows genuine engagement, not just politeness; the other person asking questions back, showing real curiosity about your life now; some willingness on their part to actually make plans, not just exchange pleasant messages indefinitely; a conversation that, once it gets going, still has some of the old ease or humour that characterised the original friendship. None of these need to be perfect or immediate — some re-acclimation, as noted in Lesson 7, is normal — but genuine warmth and reciprocal effort are worth taking as encouraging signals to continue investing.</p>

    <h2>Signals it may be better released</h2>
    <p>On the other side, a few patterns are worth reading honestly rather than explaining away indefinitely: a consistently slow, minimal, or purely polite response with no real engagement or follow-up questions; repeated difficulty actually landing on a plan despite several attempts; a conversation that, once resumed, reveals the two of you have simply grown in different directions with less genuine overlap than the shared history originally provided. None of this means the original friendship wasn't real or valuable — people and circumstances change, and it's entirely possible for a friendship to have been genuinely great in its original context while no longer being a strong fit now. Recognising this isn't a failure of the revival attempt; it's accurate, useful information.</p>

    <h2>The value of attempting, regardless of outcome</h2>
    <p>It's worth naming directly that reaching out is worthwhile even for relationships that don't end up reviving into an active friendship. At minimum, it closes a loop that may have been sitting unresolved, often provides a genuinely pleasant, low-stakes exchange even if it doesn't lead further, and occasionally plants a seed that resurfaces again later, even after this specific attempt doesn't lead anywhere immediate. Treating each outreach as valuable in itself — not solely contingent on producing an actively revived friendship — makes the whole process considerably lower-stakes and easier to actually follow through on.</p>

    <h2>Giving a promising revival real time to develop</h2>
    <p>For the connections that do show genuine early momentum, it's worth applying the same patience covered in other Humanly Labs material on friendship formation: a promising first exchange is a good start, not a finished revival. Give it a few more rounds of contact — a follow-up plan, an actual hangout if geography allows, continued low-effort check-ins — before either fully committing significant energy or concluding it's run its course. The genuine advantage of a dormant tie over a brand-new connection is a faster path back to real closeness, not an instant one.</p>

    <h2>Releasing gracefully, without a formal goodbye</h2>
    <p>If a revival attempt does turn out to be worth releasing, it's worth knowing that this rarely requires any explicit, formal closure — no need for a message explaining that you've decided not to pursue things further. Simply allowing the exchange to remain a pleasant, low-key one-off, without continued pursuit, is a completely normal and low-conflict way to let a revival attempt settle back into dormancy, this time with the loop consciously closed on your end rather than left as an open question you keep wondering about.</p>

    <h2>Don't judge too quickly from a single exchange</h2>
    <p>It's worth being cautious about drawing firm conclusions from just one exchange, however it goes. A slow or lukewarm first response might reflect the other person genuinely being caught off guard, busy, or simply needing a bit more time to warm back up to the idea of reconnecting, rather than a clear signal of disinterest. Similarly, one warm exchange doesn't guarantee a genuinely revived friendship if it isn't followed up with real, continued reciprocal effort. Give a promising or ambiguous signal at least a second round of contact before settling on a firm read either way.</p>

    <h2>What this teaches you about your other relationships</h2>
    <p>Beyond the specific dormant tie you're assessing, running through this reviving-versus-releasing process tends to sharpen your judgment for the intimacy-gap assessment from Lesson 3 more broadly. Learning to read genuine reciprocal engagement versus polite but limited response is a transferable skill, useful for evaluating any relationship's real potential — not just the dormant ones you're actively working to revive through this specific module.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>If you've already sent your Lesson 8 message and received a response, assess it honestly against the signals above. If it's promising, suggest a specific, low-pressure next step (a call, a coffee if geography allows) this week. If it's not, it's completely fine to let it rest there without pressure or guilt.</p>
    </div>

    <p>You now have a complete process for identifying and reviving dormant connections. Module 4 shifts focus to relationships you're already actively maintaining — how to deepen them from comfortable but surface-level into something with real substance.</p>
    """,
})

LESSONS.append({
    "lesson_num": 10, "module_num": 4, "module_title": "Deepening Existing Relationships",
    "lesson_title": "The Depth Gradient",
    "lesson_sub": "How to move conversations and relationships from surface to substance",
    "tool": None,
    "body": """
    <p>Many adult friendships settle into a comfortable but fairly surface-level rhythm — logistics, light updates, shared activities — without much genuine depth, even after years of regular contact. This isn't a failure; plenty of relationships are fine staying there, per the acquaintance-value point from Lesson 3. But for relationships you identified as having real depth potential, this lesson introduces a framework for deliberately moving them further along what's often called the depth gradient — the spectrum from surface small talk to genuine substance.</p>

    <h2>The gradient itself</h2>
    <p>It helps to think of conversational and relational depth as a rough gradient rather than a binary: <strong>facts</strong> (logistics, updates, surface information) → <strong>opinions</strong> (what you think about things, revealing more of your actual perspective) → <strong>feelings</strong> (how you actually feel about your circumstances, not just what's happening in them) → <strong>needs</strong> (what you actually want or are struggling with, the deepest and most vulnerable layer). Most surface-level friendships stay comfortably in the facts and light-opinions range; genuine closeness tends to require at least occasional movement into feelings and, in the closest friendships, needs.</p>

    <h2>Why relationships get stuck at the fact level</h2>
    <p>A few common patterns keep otherwise promising relationships stuck at the surface: both people defaulting to logistics and updates because it's comfortable and low-risk; a mutual, unspoken assumption that moving deeper would be awkward or inappropriate for this particular relationship, even when there's no real reason it would be; simply never having the occasion or the conversational opening to move further, since depth rarely happens automatically without at least one person nudging the conversation there.</p>

    <h2>Moving one level deeper, deliberately</h2>
    <p>The practical technique here is straightforward in concept, if it requires a bit of intentionality in practice: in a conversation currently sitting at the facts level, ask a question or make a comment that invites the opinion level ("what did you actually think about that, though?" rather than just accepting a factual update at face value). In a conversation at the opinion level, invite the feelings level ("how has that actually been feeling for you?" rather than just discussing the logistics or your shared opinion on it). This doesn't require an abrupt, heavy shift — often a single well-placed follow-up question is enough to open the door, and the other person will frequently step through it if the relationship has real depth potential, per the Lesson 3 signals.</p>

    <h2>Reciprocity matters here too</h2>
    <p>Moving a conversation deeper works best as a two-way process — offering some of your own opinion or feeling alongside inviting theirs, rather than only asking probing questions of the other person while staying guarded yourself. This connects directly to the reciprocal self-disclosure principle covered in the next lesson: depth tends to build through a back-and-forth exchange at roughly matched levels, not through one person doing all the revealing while the other stays at the surface.</p>

    <h2>Not every relationship needs to reach "needs"</h2>
    <p>It's worth being clear that the goal isn't to push every relationship all the way to the deepest level — that would be neither realistic nor appropriate for most friendships. The goal is simply to notice when a relationship with real depth potential is stuck at a shallower level than it's capable of, and to deliberately, gently invite it further, rather than assuming the current level is a fixed ceiling simply because it's where things have always been.</p>

    <h2>A quick way to notice when you're stuck at facts</h2>
    <p>A useful, quick diagnostic: think back over your last several conversations with a specific friend and ask whether you could summarise most of them as "catching up on what's been happening" versus "actually discussing how something feels or what someone genuinely thinks about it." If the honest answer skews heavily toward the former, that's a reasonably clear sign the relationship has settled at the facts level, regardless of how warm or frequent the contact has been — warmth and frequency don't automatically produce depth on their own; they simply create the opportunity for it.</p>

    <h2>Depth doesn't require heaviness</h2>
    <p>It's worth being clear that moving deeper along this gradient doesn't mean every conversation needs to become serious or emotionally weighty. Plenty of genuinely deep friendships are also light, funny, and easygoing most of the time — depth here refers to a willingness to occasionally move past the surface when it's relevant, not a requirement to constantly probe for emotional significance in every exchange. The goal is having the depth available within the relationship when it matters, not making every single conversation heavier than it needs to be.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>In your next conversation with someone you identified as having depth potential in Lesson 3, deliberately ask one question that moves one level deeper than where the conversation naturally sits — from facts toward opinion, or opinion toward feeling. Notice how it's received.</p>
    </div>

    <p>The next lesson goes deeper into the mechanics of appropriate vulnerability specifically — since moving toward the feelings and needs levels of the gradient requires some genuine self-disclosure, and getting the pacing right matters.</p>
    """,
})

LESSONS.append({
    "lesson_num": 11, "module_num": 4, "module_title": "Deepening Existing Relationships",
    "lesson_title": "Vulnerability Without Oversharing",
    "lesson_sub": "The art of appropriate self-disclosure in adult friendship",
    "tool": None,
    "body": """
    <p>Moving a relationship deeper along the gradient from the last lesson requires some genuine vulnerability — sharing more of your actual thoughts, feelings, and struggles than surface-level friendship typically involves. But vulnerability done poorly, either too little or too much, can actually work against building closeness. This lesson is about getting the calibration right.</p>

    <h2>Reciprocal self-disclosure</h2>
    <p>Psychological research on how closeness actually builds points consistently to a principle called reciprocal self-disclosure: trust and intimacy tend to develop through a gradual, matched back-and-forth exchange, where each person shares roughly proportional to what the other has shared, deepening incrementally over time rather than all at once. This is the mechanism behind why deep friendships usually take real time to build — it's not simply about accumulating hours together, but about this repeated cycle of matched, increasingly personal exchange.</p>

    <h2>Undersharing keeps relationships shallow</h2>
    <p>If your own pattern, per Module 2, tends toward avoidant tendencies, the more likely failure mode is undersharing — staying consistently guarded even when the other person has opened up, which can leave a friendship feeling one-sided and can eventually discourage the other person from continuing to invest their own vulnerability without it being reciprocated. If you notice a friend has shared something reasonably personal and your instinct is to redirect to a lighter topic, that's often exactly the moment worth pushing through the discomfort and reciprocating at a similar level instead.</p>

    <h2>Oversharing can overwhelm the pace</h2>
    <p>The opposite failure mode, more associated with anxious tendencies from Module 2, is oversharing — disclosing something quite personal well before the relationship or the specific moment has built up to match that level, which can feel like a mismatch in pace to the other person, even when it's well-intentioned. This doesn't mean vulnerability is ever wrong to offer; it means timing and proportion matter. A useful practical guideline: disclose slightly more than the relationship's current established depth, rather than dramatically more, inviting the other person to match and gradually deepen together rather than overshooting well ahead of where the relationship currently sits.</p>

    <h2>What appropriate vulnerability actually sounds like</h2>
    <p>In practice, appropriate vulnerability with a friend at an early-to-moderate depth level might sound like sharing a genuine worry or uncertainty rather than only the polished, resolved version of a situation; admitting to a mistake or a struggle rather than only presenting successes; naming an actual feeling ("honestly, that's been stressing me out more than I've let on") rather than staying purely in factual or logistical territory. None of this requires dramatic, heavy disclosure — small, genuine moments of honesty, offered consistently over time, do more to build real closeness than occasional large, intense disclosures.</p>

    <h2>Reading the other person's response</h2>
    <p>After offering some vulnerability, it's worth paying attention to how it's received — genuine engagement and reciprocal openness are a good sign to continue; a somewhat deflecting or purely sympathetic-but-distant response might simply mean this particular relationship, or this particular moment, isn't quite ready for that level yet, which is useful information rather than a rejection. Either way, a single instance of vulnerability that doesn't land perfectly isn't a failure — it's one data point in an ongoing, gradual process.</p>

    <h2>Vulnerability isn't the same as venting</h2>
    <p>It's worth drawing one more distinction here: genuine vulnerability, in the sense this lesson means, is different from simply venting at length about a problem. Venting can be a normal part of friendship, but repeated, one-directional venting without much reciprocal exchange or genuine reflection can start to feel more like using the friendship as an outlet than building mutual closeness through it. The kind of disclosure that builds real connection tends to involve some genuine reflection or feeling alongside the content, not just an unfiltered download of whatever's currently stressful, and it comes paired with real curiosity about the other person's own experience in return.</p>

    <h2>Cultural and individual variation matters here</h2>
    <p>It's worth acknowledging that comfort with disclosure varies considerably across individuals and cultural backgrounds, and there's no single universal pace that applies to everyone. Some people and contexts move toward emotional disclosure faster than others as a simple matter of style, independent of attachment pattern. The reciprocal principle still holds regardless — match roughly what the other person offers rather than significantly overshooting or undershooting — but the absolute pace that feels comfortable will reasonably differ from one friendship to another, and that variation is normal rather than a sign something's off.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>In your next conversation with a friend you're actively trying to deepen, share one genuine, moderately personal thing — a real worry, an admitted struggle, an honest feeling — slightly beyond your usual level with that person, and notice how it's received.</p>
    </div>

    <p>The final lesson in this module looks at a different but complementary way of building depth: creating shared experience together, which builds closeness through a mechanism separate from conversation and disclosure alone.</p>
    """,
})

LESSONS.append({
    "lesson_num": 12, "module_num": 4, "module_title": "Deepening Existing Relationships",
    "lesson_title": "Creating Shared Experience",
    "lesson_sub": "Why doing things together is more powerful than talking about it",
    "tool": None,
    "body": """
    <p>The last two lessons focused on conversation and disclosure as the primary route to depth — but they're not the only route, and for some relationships and some people, they're not even the most effective one. This lesson covers a complementary mechanism: building closeness through genuinely shared experience, doing things together rather than only talking.</p>

    <h2>Why shared experience builds connection independent of conversation</h2>
    <p>A significant amount of research on relationship-building points to shared activity — particularly novel, engaging, or effortful shared experience — as a powerful bonding mechanism in its own right, somewhat independent of how deep the accompanying conversation is. Working through something together, navigating a shared challenge, or simply spending extended time doing an activity side by side tends to build a kind of easy familiarity and trust that pure conversation, however deep, doesn't fully replicate on its own. This is part of why friendships formed through shared activity (a sports team, a class, a shared project) so often feel disproportionately close relative to the amount of explicit personal disclosure involved.</p>

    <h2>Novelty and effort both matter</h2>
    <p>Not all shared experience is equally bonding. Research on relationship-building activities suggests that novel and moderately effortful shared experiences — trying something neither of you has done before, working through a shared physical or mental challenge — tend to build connection more powerfully than familiar, low-effort ones. This doesn't mean routine hangouts have no value (the consistency principle from earlier Humanly Labs material still applies), but it does suggest that occasionally choosing something more novel or effortful over the default, easy option can meaningfully accelerate depth in a relationship you're actively trying to build.</p>

    <h2>Side-by-side vs. face-to-face</h2>
    <p>It's worth noting a specific dynamic that makes shared activity especially useful for certain people and certain relationships: side-by-side activity (a hike, a project, a drive) often lowers the pressure of direct, face-to-face conversation, which can make it considerably easier to have a genuinely vulnerable exchange than a deliberate, sit-down conversation would. This is particularly useful for relationships involving a more avoidant pattern from Module 2, where direct, focused vulnerability can feel more threatening than the same disclosure offered more naturally during a shared activity.</p>

    <h2>Practical ideas for building shared experience</h2>
    <p>A few concrete approaches: suggesting an activity neither of you has tried before, rather than defaulting to the same familiar hangout every time; taking on a small shared project or challenge together (a class, a physical challenge, planning something together); travelling together, even briefly, which reliably produces disproportionate bonding relative to its time cost, largely through the combination of novelty and extended, uninterrupted time together; simply doing an ordinary activity but committing to doing it together regularly enough that it becomes a genuine shared rhythm rather than a one-off.</p>

    <h2>This complements, not replaces, the conversational work</h2>
    <p>It's worth being clear that shared experience and the conversational depth work from Lessons 10 and 11 work best together, not as substitutes for each other. Shared activity alone, without any accompanying openness, can produce a pleasant but still fairly surface-level friendship; conversational depth alone, without any shared activity, can feel intense or effortful without the easier, natural bonding that doing things together provides. Combining both — occasional novel shared experiences alongside a genuine willingness to move the conversational depth gradient, per Lessons 10 and 11 — tends to produce the most robust results.</p>

    <h2>Shared experience works well alongside attachment-pattern work</h2>
    <p>It's worth connecting this back directly to Module 2: for a more avoidant pattern specifically, leading with shared activity rather than a direct, sit-down vulnerable conversation is often a genuinely easier on-ramp toward real closeness, since it doesn't require confronting the discomfort of direct emotional exchange head-on. For a more anxious pattern, shared activity can also help by providing a lower-pressure context where reassurance and connection happen more naturally through the activity itself, rather than depending entirely on how a specific conversation goes.</p>

    <h2>Shared experience doesn't need to be expensive or elaborate</h2>
    <p>It's worth countering a common assumption that meaningful shared experience requires significant expense or elaborate planning — travel, expensive activities, major events. In reality, novelty and effort are relative to what you'd normally do together, not absolute. Cooking a meal neither of you has attempted before, trying a new walking route, taking on a small home project together, or learning a skill neither of you knows can all provide genuine novelty and shared effort without requiring significant cost or logistics, making this approach accessible regardless of budget or schedule constraints.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Suggest one activity to a friend you're deepening that's genuinely new for at least one of you — not the default, familiar hangout. Notice, afterward, whether the shared novelty produced a different quality of connection than your usual routine together does.</p>
    </div>

    <p>You now have a complete toolkit for deepening existing relationships: moving along the depth gradient, calibrating vulnerability, and building shared experience. Module 5 turns to a different challenge — forming genuinely new friendships as an adult, working with the structural realities covered back in Lesson 1 rather than against them.</p>
    """,
})

LESSONS.append({
    "lesson_num": 13, "module_num": 5, "module_title": "Building New Friendships as an Adult",
    "lesson_title": "Why Adult Friendship Formation is Different",
    "lesson_sub": "And how to work with that reality rather than against it",
    "tool": None,
    "body": """
    <p>Modules 3 and 4 focused on relationships you already have some connection to — dormant or existing. This module turns to something that often feels considerably harder as an adult: forming genuinely new friendships from nothing. This lesson sets realistic expectations for why it's different now than it was earlier in life, so the specific tactics in the next two lessons land with the right context.</p>

    <h2>The structures are gone, and they're not coming back the same way</h2>
    <p>Recall from Lesson 1 that early-life friendship formation relies heavily on structures — school, shared living situations, a less demanding calendar — that provide effortless, repeated, low-stakes contact with the same people. Adult life doesn't reliably offer these structures, and waiting for something equivalent to simply reappear is usually a losing strategy. The realistic path forward isn't finding a replacement for those structures passively; it's deliberately building substitute structures of your own, which is exactly what this module covers.</p>

    <h2>Adults have less unstructured time, and that shifts the strategy</h2>
    <p>Beyond the structural point, adult schedules are simply more full — work, existing relationships, family obligations, and general life admin all compete for the same limited hours that new friendship formation would otherwise use. This means adult friendship formation typically has to be more deliberate and efficient than it needed to be earlier in life, when there was more unstructured time to let things develop organically. This isn't a discouraging fact — it's a practical one that shapes which strategies (covered in the next two lessons) tend to actually work, favouring approaches that fit into an already full life rather than ones that require large amounts of newly freed-up time.</p>

    <h2>The self-consciousness factor</h2>
    <p>It's worth naming something many adults feel but rarely say out loud: actively trying to make friends can feel slightly embarrassing or juvenile in a way it didn't as a kid or in college, where it was simply assumed to be part of normal life. This self-consciousness is worth examining rather than accepting as a valid reason to avoid deliberate effort — making friends as an adult is an extremely common, ordinary pursuit, not an unusual or immature one, even though it can feel that way given how little adults tend to openly discuss it. The near-universal nature of the friendship drift covered in Lesson 1 means you are very much not alone in actively working on this.</p>

    <h2>What tends to actually work for adults</h2>
    <p>Given these realities, effective adult friendship formation strategies tend to share a few features: they piggyback on existing structure rather than requiring entirely new time (Lesson 14 covers this directly); they favour consistency and repetition over single big attempts, similar to the exposure and consistency principles covered in other Humanly Labs course material; and they accept a somewhat longer, more deliberate timeline than the effortless early-life version of friendship formation, without treating that longer timeline as evidence something is wrong.</p>

    <h2>Reframing the goal for this module</h2>
    <p>Rather than expecting new adult friendships to feel exactly as effortless as childhood ones did, a more useful goal is: building a small number of genuinely promising new connections, through deliberate, repeated effort, over a realistic multi-month timeline. That's a genuinely achievable goal, and it's what the next two lessons are built to help you accomplish.</p>

    <h2>Comparing yourself to your own younger self is a trap</h2>
    <p>A specific version of unhelpful comparison worth naming directly: measuring your current adult friendship-forming ability against how easy it felt at university or earlier in life, and concluding you've somehow gotten worse at it. This comparison is rarely fair or accurate — what changed is overwhelmingly the surrounding structure and available time, not your underlying capacity for connection. The same person who made friends easily in a dorm hallway hasn't lost that capacity; they've simply lost the dorm hallway. Recognising this distinction directly tends to remove a significant amount of unnecessary self-doubt from the process.</p>

    <h2>The upside of adult friendship formation</h2>
    <p>It's worth balancing the challenges covered above with a genuine upside: adult friendships, once formed, often benefit from a level of self-knowledge and intentionality that's harder to access earlier in life. You generally have a clearer sense of your own values, what you're actually looking for in a friendship, and better judgment about compatibility than you likely did at eighteen or twenty-two. This means adult friendship formation, while requiring more deliberate effort to get off the ground, can often result in relationships that are a better long-term fit than some of the more circumstantial friendships formed simply through youthful proximity.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Write one honest sentence about any self-consciousness you feel around actively trying to make new friends as an adult. Naming it explicitly tends to loosen its grip somewhat, the same way naming an anxious thought does in other contexts.</p>
    </div>

    <p>The next lesson gets specific about where, in your actual current life, new friendships are most likely to form — working with your existing structure rather than needing to invent something entirely new.</p>
    """,
})

LESSONS.append({
    "lesson_num": 14, "module_num": 5, "module_title": "Building New Friendships as an Adult",
    "lesson_title": "The Proximity Principle",
    "lesson_sub": "Identifying where in your current life new friendships are most likely to form",
    "tool": None,
    "body": """
    <p>Given the reality from Lesson 13 that adult life offers less built-in structure for friendship formation, this lesson is about deliberately identifying where in your actual current life — not an imagined ideal life — repeated, low-effort proximity to the same people already exists or could reasonably be built, since proximity plus repetition remains the single most reliable driver of new friendship formation, the same mere-exposure mechanism covered in Lesson 11 of the earlier depth-focused module.</p>

    <h2>Auditing your current proximity sources</h2>
    <p>Rather than starting from nothing, it's worth taking honest stock of where you already have some repeated proximity to the same people, even if you haven't been actively leveraging it for friendship: your workplace, a regular class or hobby group, your gym or fitness routine, your neighbourhood, your children's activities if you have kids, a regular volunteer commitment, a recurring social or interest group you attend but haven't deeply engaged with. Many people are sitting on more existing proximity than they initially realise — the gap is often less about lacking opportunity and more about not deliberately leveraging the opportunity that's already there.</p>

    <h2>From proximity to actual friendship</h2>
    <p>Simply being repeatedly near the same people isn't sufficient on its own — plenty of people have years of proximity to coworkers or neighbours without forming genuine friendships with any of them. The proximity principle works best combined with the entering, conversational, and follow-through skills covered elsewhere on this platform — proximity creates the opportunity and lowers the initial barrier, but converting it into actual friendship still requires the deliberate steps of noticing a promising connection, extending it beyond the original context, and following through consistently.</p>

    <h2>Building new proximity deliberately</h2>
    <p>If an honest audit reveals limited existing proximity sources, it's worth deliberately building new ones — choosing a recurring class, group, or activity specifically because it offers repeated contact with the same people over time, rather than a one-off event. The key selection criterion is repetition: a weekly class beats an occasional drop-in event, because the mere-exposure effect that builds real familiarity depends on that consistent repeated contact, not any single high-quality interaction.</p>

    <h2>Quality of proximity matters too</h2>
    <p>Beyond simple repetition, it's worth favouring proximity sources that also offer some genuine alignment with your interests or values — the same principle covered in relocation-focused Humanly Labs material: would you keep doing this activity even if it never led to a friendship? If yes, it's a strong candidate, since you'll show up consistently regardless of social payoff, which is exactly what builds the repeated exposure friendship depends on. If the honest answer is no, the proximity source is more likely to fizzle before it has a chance to produce real connection.</p>

    <h2>Picking two or three to focus on</h2>
    <p>Rather than trying to leverage every possible proximity source at once, it's more effective to pick two or three genuinely promising ones and commit to consistent engagement with them over the coming months — the same "depth over breadth" logic that applies to relocation-based friendship building applies equally here. Spreading limited social energy across too many low-commitment sources tends to produce shallow contact everywhere rather than real connection anywhere.</p>

    <h2>Digital and hybrid proximity count too</h2>
    <p>It's worth noting that proximity doesn't have to be purely physical. Active participation in an online community built around a genuine shared interest, a recurring virtual group or class, or hybrid arrangements that combine occasional in-person contact with more frequent digital touchpoints can all provide the repeated exposure that friendship formation depends on, particularly for people whose circumstances (geography, schedule, mobility) limit purely in-person options. The underlying mechanism — repeated, low-effort contact with the same people over time — matters more than the specific medium it happens through.</p>

    <h2>What to do if your honest audit comes up genuinely thin</h2>
    <p>If your honest audit reveals very few existing proximity sources with real repetition potential, that's useful, actionable information rather than a discouraging dead end — it simply means Lesson 14's "build new proximity deliberately" section is your priority, rather than leveraging what already exists. Choosing one new recurring commitment — a class, a club, a regular volunteer shift — specifically for its repetition potential, even before you know whether you'll form close friendships through it, is a reasonable and often necessary first step when existing proximity is genuinely limited.</p>

    <h2>Patience with proximity sources too</h2>
    <p>It's worth applying the same patience to proximity-based friendship formation that applies elsewhere in this course — a new recurring group or class rarely produces a close friendship within the first few sessions. The mere-exposure benefit of proximity accumulates gradually across weeks and months of repeated contact, not immediately, so it's worth committing to a proximity source for a reasonable stretch of time before judging whether it's producing real friendship potential.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>List every existing proximity source in your current life, then circle the two or three with both genuine repetition potential and real personal interest. Commit to more deliberate engagement with those specific two or three over the coming month.</p>
    </div>

    <p>The final lesson in this module gets tactical about the actual moves that turn a promising acquaintance, met through this proximity, into a genuine friend.</p>
    """,
})

LESSONS.append({
    "lesson_num": 15, "module_num": 5, "module_title": "Building New Friendships as an Adult",
    "lesson_title": "From Acquaintance to Friend",
    "lesson_sub": "The specific moves that transform casual contacts into real friendships",
    "tool": "Check-In Generator",
    "body": """
    <p>With proximity sources identified in Lesson 14, this lesson covers the specific, concrete moves that actually convert a pleasant acquaintance — someone you see regularly and enjoy talking to within a specific context — into a genuine friendship that exists outside that original context. This transition doesn't happen automatically through repeated proximity alone; it requires a deliberate, specific set of actions.</p>

    <h2>The context-extension move</h2>
    <p>The single most important move here is extending the relationship beyond its original container. Two people who only ever interact at the gym, or only at work, or only at a weekly class, are — however friendly and familiar — still technically contained within that original context, not yet a friendship in the fuller sense. The extension happens when someone proposes interaction outside that container: a coffee, a specific plan, an invitation to something unrelated to the original setting. As covered elsewhere on this platform regarding invitations, someone has to be the one to make this move, and being willing to be that person, even occasionally, disproportionately accelerates new friendship formation.</p>

    <h2>Reading the signals before extending</h2>
    <p>Before proposing an extension beyond the original context, it's worth reading for a few encouraging signals from your repeated proximity contact: do they seem genuinely engaged rather than just polite during your regular interactions? Do they ever bring up topics or details from outside the shared context, suggesting some interest in knowing you more broadly? Is there some genuine rapport or humour that's developed over repeated contact? None of these need to be dramatic — even modest positive signals are usually enough grounds for a low-stakes extension attempt.</p>

    <h2>Making the extension low-stakes</h2>
    <p>The extension itself works best kept specific and low-pressure, following the same pattern covered for invitations elsewhere on this platform: a concrete, easy-to-accept suggestion ("want to grab coffee sometime before/after our usual class?") rather than something vague or heavy. Framing it around a shared interest already established through the proximity context makes it feel like a natural continuation rather than an abrupt shift — "I always enjoy our conversations at trivia, would love to actually catch up properly sometime" references the existing context while still proposing something new.</p>

    <h2>Consistency after the first extension</h2>
    <p>A single successful extension — one coffee, one hangout outside the original context — is a genuinely good sign, but it's still early. The same consistency principle that applies to any new relationship applies here: following up again, extending a second and third invitation over the following weeks, and continuing the original proximity contact alongside the new, extended contact. This combination — ongoing proximity plus periodic extension beyond it — tends to build toward genuine friendship considerably faster than either alone.</p>

    <h2>Use the Check-In Generator for extension messages too</h2>
    <p>The Check-In Generator tool, already introduced for reviving dormant ties in Module 3, works just as well here — describe the person and the context you know them from, and it can help draft a natural, specific extension message if you're finding the wording harder to land on your own.</p>

    <h2>What if the extension doesn't lead anywhere?</h2>
    <p>As with dormant tie revival in Lesson 9, not every promising acquaintance will turn into a genuine friendship, even with a well-executed extension. That's a normal part of the process, not a failure — treat each attempt as a reasonable, low-cost bet rather than a guaranteed outcome, and continue applying the same approach across your other proximity sources from Lesson 14 rather than reading a single non-conversion as broader evidence about your ability to make friends.</p>

    <h2>This is where all the earlier modules converge</h2>
    <p>It's worth noticing that this final skill draws directly on nearly everything covered earlier in the course: reading signals accurately connects to the intimacy-gap assessment from Lesson 3, extending an invitation draws on the same courage covered in the dormant-tie outreach in Module 3, and building genuine depth once the extension succeeds relies directly on the depth-gradient and vulnerability skills from Module 4. Adult friendship formation isn't really a separate skill set from everything else in this course — it's the same underlying skills, applied to a person you're meeting for the first time rather than one you already have history with.</p>

    <h2>It's fine to be the one who initiates repeatedly at first</h2>
    <p>Especially in the early stages of a forming friendship, it's genuinely common for one person to be doing more of the initiating than the other, without that imbalance meaning much about the other person's actual interest. New friendships haven't yet built the mutual habit and momentum that make initiating feel equally natural for both people — that habit develops over time, through repeated positive experience, not immediately. Being willing to initiate more than half the time in these early stages, without reading too much into the imbalance, is often simply part of what it takes to get a new friendship established.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>From one of your Lesson 14 proximity sources, identify one person showing genuine positive signals, and extend a specific, low-pressure invitation beyond the original context this week.</p>
    </div>

    <p>You now have a complete framework for forming new adult friendships: understanding the structural reality, leveraging proximity, and making the deliberate moves that extend acquaintance into friendship. The final module brings everything in this course together into an ongoing, sustainable maintenance system.</p>
    """,
})

LESSONS.append({
    "lesson_num": 16, "module_num": 6, "module_title": "Your Friendship Maintenance System",
    "lesson_title": "The Re-Audit",
    "lesson_sub": "Revisiting your Friendship Audit to measure what's changed",
    "tool": "Friendship Audit",
    "body": """
    <p>You began this course with a full audit of your social world back in Lesson 2. This lesson is a deliberate pause to measure what's actually changed since then, using a genuine structured comparison rather than relying on memory alone — gradual relational change is, like most gradual change covered throughout this course, notoriously hard to register accurately without a concrete before-and-after to compare against.</p>

    <h2>Why this comparison matters</h2>
    <p>Across the past several modules, you've likely revived at least one dormant connection, deepened at least one existing relationship, and made progress on at least one new friendship. Individually, each of these changes might feel modest — a single revived friendship, one deeper conversation, one new acquaintance extended into something more. Viewed together, against your original Lesson 2 map, they typically add up to something more substantial than any single change felt like on its own.</p>

    <h2>Revisit your original map directly</h2>
    <p>Go back to your Lesson 2 categorisation — nourishing, draining, and dormant — and your Lesson 3 intimacy-gap assessment. For each category, ask honestly: has anything moved? Has a dormant relationship become active again? Has a nourishing relationship become genuinely deeper, per the Module 4 work? Has a draining relationship been consciously deprioritised, freeing up energy for more worthwhile investment? Has your new-friendship work from Module 5 added anyone genuinely new to the nourishing category?</p>

    <h2>Progress here is rarely dramatic all at once</h2>
    <p>It's worth setting the same honest expectation established elsewhere in this course: friendship-building operates on a timeline of months, not weeks, and twelve weeks in, you're likely to see real, genuine movement rather than a fully transformed social world. A revived friendship might still be in an early, re-acclimating stage rather than fully back to its old closeness. A new friendship from Module 5 might still be at the early acquaintance-to-friend transition rather than fully established. This is exactly on track, not a shortfall — the underlying momentum matters more at this stage than the current absolute state.</p>

    <h2>Use the Friendship Audit again for a structured comparison</h2>
    <p>The Friendship Audit tool below, the same one you used back in Lesson 2, is worth running again now — comparing the structured output directly against your original results gives you a more objective read than memory alone, and often surfaces genuine progress you hadn't consciously registered, the same way it can for any of the gradual-change processes covered throughout this course.</p>

    <h2>Be honest about what hasn't moved yet, too</h2>
    <p>Alongside recognising real progress, it's worth being honest about areas that haven't shifted much yet — a dormant tie you haven't reached out to, a deepening effort that stalled, a proximity source from Module 5 you haven't fully leveraged. This isn't a failure; it's simply useful, accurate information about where to focus continued effort, which the next two lessons help you structure into an ongoing, sustainable system rather than something that requires this course's structure to continue.</p>

    <h2>If progress looks uneven across categories</h2>
    <p>It's genuinely common for progress to be uneven across the three original categories — perhaps significant movement on deepening existing relationships, but less on reviving dormant ones, or the reverse. This doesn't indicate anything went wrong; different modules naturally suit different people's current circumstances and comfort levels differently. Uneven progress is simply useful information about where your continued effort, per the next two lessons, might be most productively focused going forward, not a sign the overall approach failed in the areas that moved less.</p>

    <h2>Sharing this with someone, if it feels right</h2>
    <p>If you have a close friend or partner who's aware you've been working through this course, it can be genuinely worthwhile to talk through this comparison with them directly. An outside perspective often notices shifts in your social life and general demeanor that you haven't fully registered yourself, and hearing that reflected back tends to reinforce the accuracy of your own assessment, particularly on the days when gradual progress is hardest to feel from the inside.</p>

    <h2>Treat this as the template for future re-audits</h2>
    <p>The specific process in this lesson — returning to a prior snapshot, comparing honestly across categories, using the tool for a structured measurement — is itself the template you'll use again in the future, per Lesson 18's recommendation to repeat this periodically. Getting comfortable with this comparison process now, while the original Lesson 2 baseline is still fresh, makes it considerably easier to repeat confidently in six months or a year, once the comparison point is further in the past.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Write a short, honest comparison between your Lesson 2 social world map and where things stand now — specific names, specific changes, not just a general sense of "better." Keep it alongside your original map as genuine evidence of the work you've done.</p>
    </div>

    <p>The next lesson turns this snapshot into an ongoing system — a simple, sustainable rhythm for continuing to maintain and grow your social world well beyond the end of this course.</p>
    """,
})

LESSONS.append({
    "lesson_num": 17, "module_num": 6, "module_title": "Your Friendship Maintenance System",
    "lesson_title": "Your Personal Maintenance Rhythm",
    "lesson_sub": "A simple, sustainable system for staying close to the people who matter",
    "tool": None,
    "body": """
    <p>Everything covered in this course — reviving dormant ties, deepening existing relationships, forming new ones — requires ongoing maintenance to actually stick over the long term. Without some kind of system, it's genuinely easy to let the same structural drift covered in Lesson 1 quietly reassert itself once this course's structure is gone. This lesson is about building a light, sustainable maintenance rhythm you can actually keep up long-term, not just during an intensive twelve-week push.</p>

    <h2>Why maintenance needs to be deliberate for adults specifically</h2>
    <p>Recall the core argument from Lesson 1: adult life removes the structural scaffolding that made friendship maintenance largely automatic earlier in life. This means ongoing maintenance, unlike in earlier life stages, generally can't be left to happen on its own — it needs some degree of deliberate, if light, structure to survive the same competing demands that caused the original drift. This isn't a sign of anything being wrong; it's simply the accurate operating reality of adult friendship.</p>

    <h2>A simple three-tier system</h2>
    <p>A workable, low-effort maintenance system typically sorts your key relationships into a few tiers with different natural contact rhythms, rather than trying to maintain uniform, high-frequency contact with everyone:</p>
    <ul>
      <li><strong>Close tier</strong> — your closest few friendships, worth more frequent, higher-effort contact: regular calls, in-person time when possible, genuine ongoing investment.</li>
      <li><strong>Valued tier</strong> — good friendships worth maintaining but not requiring the same frequency: periodic check-ins, occasional hangouts, a rhythm of contact every month or two rather than weekly.</li>
      <li><strong>Warm tier</strong> — relationships worth keeping warm without much active effort: occasional messages, engagement on social updates, contact a few times a year, enough to prevent full dormancy without requiring significant ongoing investment.</li>
    </ul>
    <p>Sorting your key relationships into these tiers, honestly and based on your Lesson 16 re-audit, makes ongoing maintenance considerably more manageable than trying to apply the same high-effort standard to every relationship in your social world.</p>

    <h2>Building in a simple, recurring check-in habit</h2>
    <p>Beyond the tiering, it helps to build a small, recurring habit — a specific day or time, even just once a month, where you briefly review your key relationships and note anyone who's gone quieter than intended, using the Check-In Generator tool from earlier modules if the actual message feels hard to start. This doesn't need to be elaborate; five or ten minutes, done consistently, does far more for long-term maintenance than an occasional, larger effort undertaken only when guilt about a lapsed friendship finally catches up with you.</p>

    <h2>Letting go of the all-or-nothing trap</h2>
    <p>A common failure mode in friendship maintenance is treating any lapse — a missed birthday, a message that went unanswered for weeks, a longer-than-intended gap — as evidence the whole relationship has failed, which can trigger avoidance rather than simple, low-key repair. In reality, per the structural, non-personal understanding of drift from Lesson 1, an occasional lapse is completely normal and easily repaired with a simple, low-pressure reach-out, not a crisis requiring an elaborate apology or explanation.</p>

    <h2>Tiers aren't permanent assignments</h2>
    <p>It's worth treating these tiers as fluid rather than fixed — a valued-tier relationship can naturally move into the close tier as circumstances allow more contact, or a close-tier relationship might temporarily shift toward valued during an especially demanding life stretch, on either side. Revisiting the tiering occasionally, rather than setting it once and leaving it static indefinitely, keeps the system responsive to how your relationships and life actually evolve, rather than becoming its own rigid obligation to maintain.</p>

    <h2>Keeping the system itself low-effort</h2>
    <p>The system described in this lesson is deliberately lightweight by design — a simple three-way sort and a brief monthly review, not an elaborate tracking spreadsheet or a rigid schedule of mandatory contact. An overly complicated maintenance system tends to collapse under its own weight fairly quickly, the same way an overly ambitious exercise or diet plan often does; a simple system you'll actually keep up with consistently beats a sophisticated one you abandon after a few weeks.</p>

    <h2>What to do when the monthly review reveals a gap</h2>
    <p>When your review surfaces someone who's gone quieter than intended for their tier, the response doesn't need to be elaborate — a brief, warm, specific message, following the same pattern covered in Lesson 8, is usually enough to close the gap before it turns into genuine dormancy. Treating this as routine, low-stakes upkeep, rather than an overdue debt requiring a big gesture to repay, keeps the whole system feeling sustainable rather than like an accumulating source of guilt.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Sort your key relationships from the Lesson 16 re-audit into the three tiers above, and pick one specific recurring day or time each month to briefly review them and reach out to anyone who's gone quieter than intended for their tier.</p>
    </div>

    <p>The final lesson closes out the course by looking beyond maintenance toward ongoing growth — keeping your social world naturally expanding as your life continues to evolve, rather than treating this course as a one-time fix to a permanent, static social world.</p>
    """,
})

LESSONS.append({
    "lesson_num": 18, "module_num": 6, "module_title": "Your Friendship Maintenance System",
    "lesson_title": "Ongoing Growth",
    "lesson_sub": "How to keep your social world expanding naturally as your life evolves",
    "tool": None,
    "body": """
    <p>This final lesson closes the course by looking beyond the maintenance rhythm from Lesson 17 toward something equally important: keeping your social world genuinely growing and evolving over time, rather than treating this course as a one-time fix that produces a fixed, permanent social world requiring no further active development.</p>

    <h2>Your social needs will keep changing</h2>
    <p>It's worth anticipating directly that your social needs, and the shape of your ideal social world, will continue to shift as your life does — a career change, a move, a new relationship, children, ageing, all reliably reshape what kind of connection you need and have capacity for. The skills covered throughout this course — auditing your social world, reviving dormant ties, deepening existing relationships, forming new ones — aren't a one-time fix for a static problem; they're durable, reusable skills for navigating an ongoing, evolving process that continues for the rest of your life.</p>

    <h2>Periodically returning to the audit</h2>
    <p>Beyond the monthly maintenance check-in from Lesson 17, it's worth periodically — perhaps once or twice a year — running through a fuller version of the Lesson 2 and Lesson 16 audit process again, since your social world's composition will keep shifting even with good maintenance habits in place. New nourishing relationships will emerge; some current ones may naturally drift toward warm or dormant status as circumstances change; new dormant ties worth reviving will accumulate over time the same way your original Lesson 2 list did. Treating this as a periodic, ongoing practice rather than a one-time course exercise keeps your social world responsive to your actual current life rather than anchored to a single snapshot from this course.</p>

    <h2>Staying open to new proximity sources</h2>
    <p>As your life circumstances change, your Module 5 proximity sources will naturally shift too — a job change alters your workplace proximity, a move alters your neighbourhood proximity, a new life stage (parenthood, retirement, a new hobby) opens up entirely new proximity sources you may not have had before. Staying alert to these shifts, and applying the same deliberate leveraging covered in Lessons 14 and 15, keeps new-friendship formation an ongoing, natural part of your life rather than something that only happened once, during this course.</p>

    <h2>The skills, not the schedule, are what you're keeping</h2>
    <p>As this course's structured, weekly format ends, it's worth being clear about what actually carries forward: not the specific twelve-week schedule, but the underlying skills — reading your social world honestly, understanding your own relational patterns, knowing how to revive a dormant tie, how to deepen an existing relationship, how to form a new one, and how to maintain what you've built without requiring a formal structure to do so. These are genuinely durable, reusable across whatever life changes come next.</p>

    <h2>A closing note</h2>
    <p>Eighteen lessons ago, your social world may have felt like something that had simply happened to you — thinned out gradually, without any clear sense of how to reverse it or whether it even could be. You've since built a genuine, structured understanding of why friendship drifts, direct experience reviving connections that had gone quiet, real progress deepening relationships that had settled at the surface, and concrete tools for forming new ones despite the genuine structural challenges of adult life. Your social world is not a fixed thing that happens to you — it's something you now know how to actively build and maintain, for as long as you keep using these tools.</p>

    <h2>If you're revisiting this during a harder stretch</h2>
    <p>If you're rereading this lesson at some future point, during a period where your social world feels thin again — after a move, a major life change, or simply a period of drift despite your best maintenance efforts — it's worth remembering directly: you've already done this once. The specific skills covered across these eighteen lessons don't expire or require this course's structure to use again. Auditing your social world, reviving what's gone dormant, deepening what's grown surface-level, and forming what's genuinely new are all skills you now have real, practiced experience with, not abstract ideas you're encountering for the first time. Whatever stage of drift or difficulty you find yourself in, the same process that got you here once can get you there again.</p>

    <h2>The tools you're carrying forward</h2>
    <p>As a practical summary: you're keeping the structural understanding of friendship drift from Lesson 1, which removes unnecessary shame from any future lapse; the self-knowledge about your own relational patterns from Module 2, which helps you recognise and work with your own tendencies as they show up in future relationships; the specific mechanics of reviving, deepening, and forming friendships from Modules 3 through 5; and the maintenance system from this final module, which keeps all of it sustainable without requiring a formal course structure to continue. None of this is time-limited to these twelve weeks — it's a durable set of skills for a lifelong, ongoing part of a good life.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Set a recurring reminder, six months from now, to run a fuller re-audit of your social world using the Friendship Audit tool — treating this not as the end of the process, but as the first of many ongoing check-ins over the years ahead.</p>
    </div>

    <p>That's the full course. Your friendships are worth the ongoing effort — keep at it.</p>
    """,
})

def slug_for(n, title):
    import re
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return f"{n:02d}-{s}"

def render_all():
    for lesson in LESSONS:
        lesson["_slug"] = slug_for(lesson["lesson_num"], lesson["lesson_title"])

    for i, lesson in enumerate(LESSONS):
        prev_l = LESSONS[i - 1] if i > 0 else None
        next_l = LESSONS[i + 1] if i < len(LESSONS) - 1 else None
        prev_link = f'<a href="/courses/friendship-revival/content/lessons/{prev_l["_slug"]}.html">← Lesson {prev_l["lesson_num"]}: {prev_l["lesson_title"]}</a>' if prev_l else '<span class="nav-placeholder">← Start of course</span>'
        next_link = f'<a href="/courses/friendship-revival/content/lessons/{next_l["_slug"]}.html">Lesson {next_l["lesson_num"]}: {next_l["lesson_title"]} →</a>' if next_l else '<a href="/courses/friendship-revival/content/">Back to course overview →</a>'

        tool_box = ""
        if lesson.get("tool"):
            emoji, link = TOOL_LINKS[lesson["tool"]]
            tool_box = f'''  <div class="tool-box">
    <div class="tool-emoji">{emoji}</div>
    <div class="tool-copy"><strong>Use the {lesson["tool"]}</strong>This lesson pairs with the {lesson["tool"]} tool — use it now while the ideas are fresh.</div>
    <a href="{link}">Open tool →</a>
  </div>
'''

        html = TEMPLATE.format(
            lesson_title=lesson["lesson_title"],
            module_num=lesson["module_num"],
            module_title=lesson["module_title"],
            lesson_num=lesson["lesson_num"],
            lesson_sub=lesson["lesson_sub"],
            body=lesson["body"],
            tool_box=tool_box,
            prev_link=prev_link,
            next_link=next_link,
        )
        fname = os.path.join(OUT_DIR, f'{lesson["_slug"]}.html')
        with open(fname, "w", encoding="utf-8") as f:
            f.write(html)
        print("wrote", fname)

if __name__ == "__main__":
    render_all()
    print(f"\n{len(LESSONS)} lessons rendered.")
