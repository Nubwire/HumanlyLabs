#!/usr/bin/env python3
"""
Generates the 20 individual lesson pages for The Social Landing course.
Run from anywhere: python3 _build.py
Source of truth for lesson content lives in this file (LESSONS list below).
"""
import os

OUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "courses", "social-landing", "content", "lessons",
)

TOOL_LINKS = {
    "Loneliness Quiz": ("🧠", "/quiz"),
    "Social Battery": ("🔋", "/social-battery"),
    "Find Your People": ("🧩", "/find-your-people"),
    "Conversation Starter": ("💬", "/conversation-starter"),
    "Check-In Generator": ("✉️", "/checkin-generator"),
    "Friendship Audit": ("🗺️", "/friendship-audit"),
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{lesson_title} — The Social Landing — Humanly Labs</title>
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
      --c-green: #3A6B49; --c-green-l: #E8F2EC; --c-green-b: #A8CEAF;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Instrument Sans', sans-serif; background: var(--c-bg); color: var(--c-ink); line-height: 1.65; }}
    nav {{ background: rgba(247,243,236,.95); border-bottom: 1px solid var(--c-border); padding: 0 2rem; position: sticky; top: 0; z-index: 100; }}
    .nav-inner {{ max-width: 760px; margin: 0 auto; height: 60px; display: flex; align-items: center; justify-content: space-between; }}
    .logo {{ font-family: 'Playfair Display', serif; font-size: 20px; color: var(--c-ink); text-decoration: none; }}
    .logo em {{ font-style: italic; color: var(--c-green); }}
    .logo sup {{ font-size: 9px; color: var(--c-ink-3); vertical-align: super; margin-left: 2px; }}
    .main {{ max-width: 760px; margin: 0 auto; padding: 2.5rem 2rem 6rem; }}
    .breadcrumb {{ font-size: .8rem; color: var(--c-ink-3); margin-bottom: 1.5rem; }}
    .breadcrumb a {{ color: var(--c-green); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .lesson-meta {{ display: flex; align-items: center; gap: .6rem; margin-bottom: .75rem; flex-wrap: wrap; }}
    .module-badge {{ background: var(--c-green); color: #fff; border-radius: 8px; padding: 4px 10px; font-size: 11px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; }}
    .lesson-num-badge {{ font-size: 11px; font-weight: 600; color: var(--c-ink-3); }}
    h1.lesson-title {{ font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 500; line-height: 1.25; margin-bottom: .6rem; }}
    .lesson-sub {{ font-size: 1rem; color: var(--c-ink-2); margin-bottom: 2.5rem; padding-bottom: 2rem; border-bottom: 1px solid var(--c-border); }}
    .lesson-body h2 {{ font-family: 'Playfair Display', serif; font-size: 1.35rem; font-weight: 500; margin: 2.25rem 0 .9rem; color: var(--c-ink); }}
    .lesson-body p {{ margin-bottom: 1.1rem; color: var(--c-ink-2); font-size: .98rem; }}
    .lesson-body ul, .lesson-body ol {{ margin: 0 0 1.1rem 1.3rem; color: var(--c-ink-2); font-size: .98rem; }}
    .lesson-body li {{ margin-bottom: .5rem; }}
    .lesson-body strong {{ color: var(--c-ink); }}
    .exercise-box {{ background: var(--c-surface); border: 1px solid var(--c-border); border-left: 4px solid var(--c-green); border-radius: 12px; padding: 1.5rem 1.75rem; margin: 2rem 0; box-shadow: var(--shadow); }}
    .exercise-box .exercise-label {{ font-size: 11px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: var(--c-green); margin-bottom: .6rem; }}
    .exercise-box p:last-child {{ margin-bottom: 0; }}
    .tool-box {{ background: var(--c-green-l); border: 1px solid var(--c-green-b); border-radius: 12px; padding: 1.25rem 1.5rem; margin: 2rem 0; display: flex; align-items: center; gap: 1rem; }}
    .tool-box .tool-emoji {{ font-size: 1.75rem; flex-shrink: 0; }}
    .tool-box .tool-copy {{ flex: 1; font-size: .9rem; color: var(--c-ink-2); }}
    .tool-box .tool-copy strong {{ color: var(--c-ink); display: block; margin-bottom: 2px; }}
    .tool-box a {{ background: var(--c-green); color: #fff; text-decoration: none; font-size: .85rem; font-weight: 500; padding: 8px 16px; border-radius: 999px; white-space: nowrap; flex-shrink: 0; }}
    .lesson-nav {{ display: flex; justify-content: space-between; gap: 1rem; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--c-border); }}
    .lesson-nav a {{ font-size: .875rem; color: var(--c-green); text-decoration: none; font-weight: 500; }}
    .lesson-nav a:hover {{ text-decoration: underline; }}
    .lesson-nav .nav-placeholder {{ color: var(--c-ink-3); font-size: .875rem; }}
    .support-box {{ background: var(--c-surface); border: 1px solid var(--c-border); border-radius: 14px; padding: 1.5rem; margin-top: 3rem; text-align: center; }}
    .support-box p {{ font-size: .875rem; color: var(--c-ink-2); }}
    .support-box a {{ color: var(--c-green); }}
    footer {{ text-align: center; padding: 2rem; font-size: 12px; color: var(--c-ink-3); border-top: 1px solid var(--c-border); }}
    footer a {{ color: var(--c-ink-3); text-decoration: none; }}
    @media (max-width: 600px) {{ .main {{ padding: 2rem 1.25rem 4rem; }} h1.lesson-title {{ font-size: 1.6rem; }} .tool-box {{ flex-direction: column; align-items: flex-start; }} }}
    a:focus-visible, button:focus-visible {{ outline: 2px solid var(--c-green); outline-offset: 3px; border-radius: 4px; }}
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
    <span style="font-size:13px;color:var(--c-ink-3)">✈️ The Social Landing</span>
  </div>
</nav>
<main class="main">
  <div class="breadcrumb"><a href="/courses/social-landing/content/">← Back to course overview</a></div>
  <div class="lesson-meta">
    <span class="module-badge">Module {module_num} · {module_title}</span>
    <span class="lesson-num-badge">Lesson {lesson_num} of 20</span>
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

LESSONS = []  # populated below by _build_data.py content, appended in build steps

LESSONS.append({
    "lesson_num": 1, "module_num": 1, "module_title": "Preparing for Takeoff",
    "lesson_title": "The Relocation Loneliness Landscape",
    "lesson_sub": "What to expect, common pitfalls, reframing loneliness as a signal",
    "tool": None,
    "body": """
    <p>If you've relocated recently and the loneliness has hit harder than you expected, you are not doing this wrong. Relocation loneliness is one of the most common — and most under-discussed — experiences adults go through. It shows up whether you moved for a dream job, a relationship, or just a fresh start, and it shows up whether you moved across the country or across the world. This lesson sets the foundation for the next twelve weeks: what's actually happening when you feel this way, why it isn't a sign that something is wrong with you or your decision, and how to start treating it as useful information instead of a verdict.</p>

    <h2>Why this feels so much harder than you expected</h2>
    <p>Before you moved, your social world was probably invisible to you — in the way that infrastructure is invisible until it breaks. You had people who knew your coffee order, your work stress, your family's names, your Sunday routine. None of that had to be built or maintained consciously anymore; it just existed, accumulated over years. Moving doesn't just relocate your body. It quietly deletes that entire invisible support structure at once, and then asks you to rebuild it from nothing, usually while also handling a new job, a new apartment, and a hundred logistical details that leave little energy for anything else.</p>
    <p>That combination — total social reset plus high logistical load — is why relocation loneliness often feels more acute than loneliness from other causes. It's not that you're less resilient or less socially capable than you were before. It's that you're doing one of the most socially demanding things a person can do, at the exact moment you have the fewest resources to do it with.</p>

    <h2>Loneliness is a signal, not a diagnosis</h2>
    <p>Psychologists who study loneliness often describe it the same way they describe hunger or thirst: as a biological signal that something needs attention, not as evidence of a personal flaw. Hunger doesn't mean you're bad at eating. Loneliness doesn't mean you're bad at connecting. It means your brain has correctly detected a gap between the social contact you need and the social contact you currently have — and it's motivating you to close that gap.</p>
    <p>This reframe matters because of what people typically do with loneliness instead: they treat it as proof. Proof that the move was a mistake. Proof that they're somehow harder to connect with than other people. Proof that this is just how their life is going to be now. None of that follows from the feeling itself. The feeling is just information — accurate information, worth listening to, but not a life sentence and not a character assessment.</p>

    <h2>The typical shape of relocation loneliness</h2>
    <p>Most people who move go through a fairly predictable arc, even though it doesn't feel predictable while you're in it:</p>
    <ul>
      <li><strong>Weeks 1–2, the novelty phase.</strong> There's enough new-city adrenaline and logistical busyness that loneliness hasn't fully landed yet.</li>
      <li><strong>Weeks 3–8, the dip.</strong> The novelty wears off, the logistics settle down, and the absence of a social world becomes the loudest thing in the room. This is usually the hardest stretch, and it's also exactly where most people are when they start a course like this one.</li>
      <li><strong>Weeks 8–16, the slow rebuild.</strong> The first acquaintances turn into the first real connections. Progress is uneven and often invisible week to week, but it compounds.</li>
      <li><strong>Months 4–12+, consolidation.</strong> A genuine social life exists — not identical to the one you left, but real, and often surprisingly solid in its own right.</li>
    </ul>
    <p>If you're currently in the dip, this course is built to shorten it. But it helps enormously just to know the dip is a normal, time-limited phase of a well-understood process — not evidence that this is permanent.</p>

    <h2>Three pitfalls that quietly extend the dip</h2>
    <p><strong>Over-relying on your old social world.</strong> Long calls with old friends can be a lifeline, and you should keep them. But if video calls with people from your old city are your only source of connection, they can also become a way of avoiding the harder, more awkward work of building something new locally — because it feels safer to talk to people who already know you.</p>
    <p><strong>Waiting to be invited.</strong> In an established social world, invitations flow in both directions without much thought. In a new city, nobody has you in their rotation yet — not because they don't like you, but because you're not yet on their mental list of people to think of. Waiting for that to happen on its own can take a very long time. Initiating is the actual unlock, and later lessons will make it much less daunting.</p>
    <p><strong>Comparing week 3 in the new city to year 5 in the old one.</strong> This comparison is almost never fair, and it's almost always what makes people conclude "I'm just not connecting here" far too early. A more honest comparison is: how did your old social world look in its own third week, if you could rewind ten years?</p>

    <h2>What this course won't ask you to do</h2>
    <p>This isn't a course about forcing yourself to become a different, more extroverted person, or about treating every waking hour as a networking opportunity. It's about applying a small number of well-understood, learnable skills consistently enough that they compound — the same way a modest, consistent savings habit compounds into something substantial over time, even though no single deposit feels significant on its own. You'll keep your own pace, your own style, and your own definition of what a good social life looks like throughout.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Take two minutes and write down, honestly, where you think you currently are in the four-phase arc above. Then write one sentence about what would need to be true for you to feel like you'd moved into the next phase. You'll come back to this note at the end of the course.</p>
    </div>

    <p>The rest of this module builds your starting map: your specific social needs, your energy baseline, and a realistic timeline you can actually hold yourself to. From Module 2 onward, we get concrete — decoding your city, finding your people, and making first contact. For now, the only job is to let this reframe land: what you're feeling is common, temporary, and responsive to action. That's the whole premise of the next twelve weeks.</p>
    """,
})

LESSONS.append({
    "lesson_num": 2, "module_num": 1, "module_title": "Preparing for Takeoff",
    "lesson_title": "Your Social Connection Profile",
    "lesson_sub": "Identify your unique needs and preferences",
    "tool": "Loneliness Quiz",
    "body": """
    <p>Not all loneliness is the same, and not all social lives should look the same either. Before you start building yours back up, it's worth getting specific about what kind of connection you're actually missing — because the fix for "I don't have anyone to do things with" is different from the fix for "I don't have anyone who really knows me." Chasing the wrong kind of connection is one of the most common reasons people feel like they're doing "everything right" socially and still feel lonely.</p>

    <h2>The two loneliness gaps</h2>
    <p>Researchers who study loneliness generally distinguish between two related but distinct needs:</p>
    <ul>
      <li><strong>Social loneliness</strong> — a gap in your network of casual, everyday connection: people to grab coffee with, chat with at the gym, sit next to at a class. This is about quantity and texture of casual contact.</li>
      <li><strong>Emotional loneliness</strong> — a gap in deep, trusted connection: someone who knows what's actually going on with you, who you'd call at 11pm with bad news. This is about depth, not headcount.</li>
    </ul>
    <p>Most people who relocate are missing both at first, but they usually don't recover at the same rate, and they don't require the same strategy. Social loneliness tends to close faster — it's largely a function of exposure and repetition. Emotional loneliness closes more slowly, because deep trust takes real time and vulnerability to build, and it can't be manufactured through volume alone. Knowing which gap is bothering you most right now helps you set expectations that match reality instead of quietly measuring yourself against a timeline you were never on.</p>

    <h2>Your connection style</h2>
    <p>Beyond the two gaps, people also differ in what kind of social life actually satisfies them, independent of how lonely they currently feel. It's worth being honest with yourself about a few dimensions:</p>
    <p><strong>Breadth vs. depth.</strong> Some people feel resourced by a wide circle of lighter connections; others need two or three close people and find a large acquaintance network draining rather than fulfilling. Neither is more mature or more correct — but building toward the wrong one for you will leave you busy and still unsatisfied.</p>
    <p><strong>Structured vs. organic.</strong> Some people connect best through recurring structured activities (a class, a league, a club) where the social contact is a byproduct of showing up. Others find structure stifling and connect more naturally through unplanned, looser contact. Most of the tactics in this course work for both, but you'll want to weight them differently.</p>
    <p><strong>Group vs. one-on-one.</strong> Some people build trust fastest in group settings where the pressure is diffused across several people; others find one-on-one time far more bonding than group hangs, which can feel socially "thin" no matter how many of them you attend.</p>

    <h2>Use the Loneliness Quiz to get a starting profile</h2>
    <p>Rather than guessing at all of this in the abstract, take a few minutes now with the Loneliness Quiz tool linked below. It's built to identify which loneliness type best describes your current situation and gives you a personalised starting profile. Answer it honestly rather than aspirationally — based on how things actually feel right now, not how you wish they felt or think they should feel.</p>

    <h2>Your profile isn't a permanent label</h2>
    <p>It's worth holding this profile loosely rather than treating it as a fixed identity. People's connection needs shift with context — someone who was breadth-oriented in a busy college social scene might find themselves craving more depth a decade later, after a demanding job has already filled their week with plenty of casual contact. Relocation itself can temporarily shift what you need: even a naturally depth-oriented person often needs a wider net of looser contacts in the first few months, simply because depth takes time to build and the intervening months would otherwise be very quiet. Treat this lesson's profile as an honest read of where you are right now, not a permanent verdict on your personality.</p>
    <p>It's also worth distinguishing your connection style from your current loneliness level. Someone can be a genuinely depth-oriented person and still benefit from a wider net of casual contacts during the rebuilding phase — not because their underlying preference has changed, but because casual contact is often the on-ramp to the deeper connections they actually want. Few close friendships start as close; almost all of them pass through a casual, low-stakes phase first, however briefly.</p>

    <h2>A quick note on introversion and extroversion</h2>
    <p>It's worth separating your connection profile from the introvert/extrovert label specifically, since the two get conflated often. Introversion and extroversion describe where you draw energy from — solitude versus stimulation — not what kind of connection you're seeking or how many people you want in your life. A introverted person can have a strong preference for a wide, breadth-oriented social circle; an extroverted person can be entirely depth-oriented. Use the quiz's actual dimensions rather than defaulting to whatever your general personality label seems to imply.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>After you take the quiz, write two or three sentences in your own words: which gap (social or emotional) feels bigger right now, and which connection style — breadth or depth, structured or organic, group or one-on-one — sounds most like the social life you actually want, not just the one you think you're "supposed" to want. Keep this note; you'll use it again in Module 2 when you start choosing where to actually spend your time.</p>
    </div>

    <p>There's no wrong profile here. The point of this lesson isn't to diagnose a problem — it's to stop you from spending the next twelve weeks building a social life that looks good from the outside but doesn't actually meet the specific kind of connection you need.</p>
    """,
})

LESSONS.append({
    "lesson_num": 3, "module_num": 1, "module_title": "Preparing for Takeoff",
    "lesson_title": "Know Your Baseline",
    "lesson_sub": "Establish your social energy starting point",
    "tool": "Social Battery",
    "body": """
    <p>Building a social life from scratch is, honestly, exhausting — even for people who are naturally outgoing. Every interaction with someone new carries a higher cognitive load than an interaction with someone you already know well: more small talk, more effort to find common ground, more uncertainty about how it's landing. If you don't plan around your actual energy capacity, it's very easy to either burn out hard in week three, or under-do it out of self-protection and stall your progress. This lesson is about knowing your starting point so you can pace the rest of the course sustainably.</p>

    <h2>Social energy is a real, finite resource</h2>
    <p>Whether you'd call yourself an introvert, an extrovert, or somewhere in between, socialising draws on a limited daily and weekly energy budget — and right now, in a new city, that budget is under more pressure than usual, because almost every social interaction you're having is a "new person" interaction rather than a low-effort "known person" one. This isn't a flaw to fix. It's a real constraint to plan around, the same way you'd plan around a physical training capacity if you were starting to run again after time off.</p>
    <p>The mistake most people make isn't running out of social energy — it's not noticing they've run out until after they've already said something a bit flat, left an interaction early, or snapped at someone, and then quietly conclude "I'm bad at this," when really they were just past their limit for the day.</p>

    <h2>What depletes you vs. what recharges you</h2>
    <p>Two things are worth separating clearly:</p>
    <ul>
      <li><strong>Depleting activities</strong> — usually higher-stakes, higher-novelty, higher-effort interactions: meeting several new people at once, performing in a group setting, navigating unfamiliar social norms.</li>
      <li><strong>Recharging activities</strong> — time alone, low-effort contact with people who already know you well, activities that don't require performing or explaining yourself.</li>
    </ul>
    <p>Notice that "recharging" doesn't necessarily mean "alone" — for some people, low-effort time with a close friend recharges more than solitude does. The goal of this lesson isn't to fit you into a category; it's to get you specific and honest about what actually restores you, so you can build it into your week deliberately instead of accidentally running your tank to empty.</p>

    <h2>Why this matters specifically right now</h2>
    <p>During the first few months in a new city, almost everything social falls into the "depleting" column, because almost everyone you meet is new. That means your usual balance of depleting-to-recharging activity is temporarily broken, even if your overall social energy capacity hasn't changed. If you don't account for this, you'll likely either overcommit and crash — skipping the gym, the sleep, the solo time that normally keeps you steady — or undercommit out of instinctive self-protection, which slows the whole rebuilding process down.</p>
    <p>The fix isn't to push through regardless. It's to build recovery time as deliberately as you build social plans, especially in these early weeks.</p>

    <h2>Use the Social Battery tool to map your baseline</h2>
    <p>The Social Battery tool below runs a short check-in process to help you see your current energy patterns clearly — what's draining you, what's restoring you, and roughly how much social contact you can sustainably hold in a given week right now. Use it this week, and consider returning to it in Module 4 once you've got more of a social rhythm established — your capacity typically grows as connections become less effortful and more familiar.</p>

    <h2>Building a weekly energy budget</h2>
    <p>Once you have a rough sense of your baseline, it helps to translate it into something concrete rather than leaving it as a vague impression. Try sketching a simple weekly energy budget: a rough number of "social units" you can sustainably spend across the week, where a unit might be a couple of hours of new-connection interaction, and a rough sense of how many recharge units you need to balance each one out. This doesn't need to be a rigorous system — even a loose, approximate version is enough to catch the common pattern of unconsciously overcommitting in a good week and then being confused about the crash that follows a few days later.</p>
    <p>It's also worth noticing that your baseline isn't static even week to week. Poor sleep, a stressful work stretch, or unrelated life stress all shrink your available social capacity temporarily, even if your underlying tolerance for socialising hasn't changed. Checking in with yourself briefly before committing to a full week of plans — not just at the start of the course, but as an ongoing habit — helps you catch these dips before they turn into a harder crash later on.</p>

    <h2>A note for people who don't fully trust their own read</h2>
    <p>Some people, especially after a stretch of loneliness, find it hard to accurately gauge their own energy levels — either consistently pushing through depletion because slowing down feels like giving up, or consistently avoiding social contact out of anticipated exhaustion that doesn't always materialise once they're actually there. If either of these sounds familiar, treat your own energy predictions as hypotheses to test rather than fixed facts. Try showing up to a plan you predicted would drain you, and honestly note afterward whether the prediction matched the reality. Over a few weeks, this builds a far more accurate internal model than assumption alone ever will.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Before your next social plan, name out loud (or write down) one thing you'll do afterward to recharge — even something small, like twenty minutes with no phone, or an early night. Committing to the recovery in advance makes it far more likely you'll actually protect it, instead of it quietly getting crowded out.</p>
    </div>

    <p>Pacing yourself isn't the opposite of making progress — it's what makes sustained progress possible. The people who build strong social lives after a move aren't usually the ones who pushed hardest in week one. They're the ones who kept showing up, steadily, for months, because they didn't burn themselves out early on.</p>
    """,
})

LESSONS.append({
    "lesson_num": 4, "module_num": 1, "module_title": "Preparing for Takeoff",
    "lesson_title": "Setting Realistic Expectations",
    "lesson_sub": "The real timeline for friendship, celebrating small wins",
    "tool": None,
    "body": """
    <p>This is the last lesson before the course moves from groundwork into action, and it's arguably the one that prevents the most unnecessary discouragement over the next eleven weeks. Almost everyone underestimates how long real friendship actually takes to build — and that mismatch between expectation and reality is one of the biggest reasons people give up on a promising new connection right when it's about to turn a corner.</p>

    <h2>Friendship has a real, slow timeline — and that's normal</h2>
    <p>Communication researcher Jeffrey Hall's widely cited work on friendship formation estimated that it takes roughly 50 hours of shared time to move from acquaintance to casual friend, around 90 hours to become a real friend, and upward of 200 hours to become a close friend. The exact numbers matter less than the shape of the finding: meaningful friendship isn't a threshold you cross after one great conversation. It's accumulated through repeated contact, over weeks and months, well past the point where it starts to feel a bit effortful or repetitive.</p>
    <p>This matters enormously for how you interpret your own progress. If you meet someone promising, have one genuinely good hangout, and then feel like the friendship has "gone quiet" for a few weeks, the honest read is usually not "that didn't work out." It's "we're at hour eight of ninety, right on schedule." Most people quietly give up on connections at exactly this stage — not because the connection failed, but because they expected the 90-hour outcome from the 8-hour input.</p>

    <h2>What "on track" actually looks like week to week</h2>
    <p>Progress in the early months rarely looks like a straight line toward a thriving social life. It looks like this:</p>
    <ul>
      <li>Weeks where you meet several new people and none of them go anywhere in particular — this is normal attrition, not failure.</li>
      <li>One promising connection that fizzles for reasons that have nothing to do with you — schedules, life circumstances, mismatched needs.</li>
      <li>Long stretches where nothing seems to be happening, followed by a sudden cluster of connection once a few relationships cross their own thresholds at once.</li>
      <li>Acquaintances who become genuine friends only after four, five, six separate hangouts spread across two or three months.</li>
    </ul>
    <p>If your mental model expects a clean upward line, all of the above will register as discouraging. If your mental model expects this — messy, uneven, slower than you'd like, but cumulative — the exact same twelve weeks will feel like solid, visible progress.</p>

    <h2>Redefining what counts as a win</h2>
    <p>Because friendship takes so long to fully form, and because most of this course happens before that threshold is crossed, it's worth deliberately redefining what counts as progress during these twelve weeks. A win is not "I now have a close friend here." For most people, that's not a realistic twelve-week outcome, and holding yourself to it will feel like failure even while you're doing everything right. A more honest, motivating definition of a win over this course includes things like:</p>
    <ul>
      <li>Having three or four people whose names you know and who'd recognise you and say hello.</li>
      <li>Making it a habit to initiate plans rather than only waiting to be invited.</li>
      <li>Having one or two people you've hung out with one-on-one more than once.</li>
      <li>Feeling less anxious walking into a room of strangers than you did in week one.</li>
      <li>Having a rhythm — a class, a group, a regular spot — where you're becoming a familiar face.</li>
    </ul>
    <p>Every one of these is genuine, meaningful progress toward a real social life, and every one of these is realistically achievable in twelve weeks.</p>

    <h2>What to do when comparison creeps in anyway</h2>
    <p>Even with a realistic timeline in mind, it's very hard to fully avoid comparing your new social life to your old one, especially in quiet moments — a weekend with nothing planned, a holiday spent mostly alone, scrolling through old photos of a group that used to be effortless to gather. When that comparison shows up, it helps to name explicitly what's actually being compared: a social world that took years to build, against one that's a few weeks old. That's not a fair comparison, and noticing the unfairness out loud — even just to yourself — tends to take some of the sting out of it.</p>
    <p>It also helps to remember that your old social world didn't stay static either. Relationships you now think of as effortless were, at some point, also new and a little effortful — you've simply forgotten that part, because it happened gradually enough not to register as a separate phase. The friendships you're building now will follow the same arc, even though it doesn't feel that way from inside the early weeks.</p>

    <h2>Holding both things at once</h2>
    <p>A realistic timeline doesn't mean lowering your ambitions for what your social life can eventually look like — it means being accurate about the path to get there. You can hold both a genuinely high bar for the kind of connection you want and a patient, realistic sense of how long it reasonably takes to build it, without those two things being in tension. The people who sustain effort over the full twelve weeks tend to be the ones who've internalised this combination early, rather than the ones expecting either instant results or no results at all.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Write down your own personal definition of a "win" for the end of this twelve-week course — using the list above as a starting point, not a ceiling. Make it something you could realistically hit even on an average, unremarkable week. You'll check back in against this in Module 6.</p>
    </div>

    <p>With your profile, your energy baseline, and a realistic timeline in place, you're done with groundwork. Module 2 moves into action: reading your new city, finding the specific places and communities where your people actually are, and building a plan you can follow without having to reinvent it from scratch every week.</p>
    """,
})

LESSONS.append({
    "lesson_num": 5, "module_num": 2, "module_title": "Navigation Systems",
    "lesson_title": "Decoding Your New City",
    "lesson_sub": "Identifying social hubs, community resources, interest-based groups",
    "tool": None,
    "body": """
    <p>Every city has a social infrastructure — the places, events, and institutions where connection actually happens — but almost none of it is visible from the outside. In your old city, you knew this infrastructure without thinking about it: which bar had the good trivia night, which park filled up on Sundays, which coworking space had the friendly regulars. In a new city, that map doesn't exist yet, and trying to build a social life without it means relying on luck instead of strategy. This lesson is about building that map deliberately.</p>

    <h2>Three layers of social infrastructure</h2>
    <p>It helps to think about a city's social opportunities in three layers, because they require different levels of commitment and produce different kinds of connection:</p>
    <p><strong>Ambient hubs</strong> — places you visit repeatedly for a non-social reason (a gym, a coffee shop, a dog park, a library) where familiarity builds slowly just through showing up. Low effort, slow payoff, but very low-pressure.</p>
    <p><strong>Structured groups</strong> — recurring, organised activities with a built-in reason to keep showing up: sports leagues, classes, clubs, volunteer groups, professional associations. Medium effort, more reliable payoff, because the structure does a lot of the social work for you.</p>
    <p><strong>One-off events</strong> — meetups, mixers, festivals, pop-up events. Highest effort per interaction (you're always the new person), lowest reliability per single event, but useful for casting a wide net early on.</p>
    <p>A strong early strategy usually leans most heavily on structured groups, uses ambient hubs as a steady low-effort background layer, and treats one-off events as reconnaissance rather than the main plan.</p>

    <h2>Where to actually look</h2>
    <p>Rather than waiting for a comprehensive answer to appear, start pulling from a handful of concrete sources this week:</p>
    <ul>
      <li><strong>Local event and community platforms</strong> — Meetup, Eventbrite, Facebook Groups, and city-specific community apps or forums usually surface far more than you'd expect once you search your actual interests plus your neighbourhood name.</li>
      <li><strong>Reddit and local subreddits</strong> — most cities have an active subreddit, and searching it for terms like "new to the city" or "how to meet people" often surfaces threads full of specific, current recommendations from people who've done exactly what you're doing.</li>
      <li><strong>Libraries, community centres, and rec departments</strong> — chronically under-used and often free or cheap, with classes and groups that skew toward people specifically looking to meet others.</li>
      <li><strong>Your workplace, gym, or building</strong> — the people already in your daily radius are the lowest-friction starting point, because you don't need to manufacture an occasion to see them again.</li>
      <li><strong>Anyone you already know, however loosely</strong> — a former coworker's friend, a college acquaintance who happens to live nearby, a distant connection your family mentioned. These are disproportionately valuable, because they come pre-vetted and often open doors to their own social circle.</li>
    </ul>

    <h2>Build a living list, not a perfect plan</h2>
    <p>The goal this week isn't to find "the answer" — it's to build a working list of five to ten specific options across the three layers above, so that when you have energy to act (and Module 3 gives you the tools to act on it), you're not starting from a blank page. Treat this list as alive: some options will turn out to be duds, and that's fine. You're gathering options, not making commitments yet.</p>

    <h2>Reading a place beyond the obvious search results</h2>
    <p>Beyond the platforms above, a city's social texture often shows up in less obvious places: the noticeboard at a local café, the flyer wall at a community centre, a neighbourhood Facebook group that's more active than the official city page, a coworker mentioning an event in passing. These sources tend to surface smaller, more local, less algorithmically-optimised options — often exactly the kind of low-key, repeat-attendee groups that produce real connection, as opposed to the large one-off events that show up first in a generic search.</p>
    <p>It's also worth paying attention to what a place is known for informally, not just officially. Almost every city has an unofficial reputation among locals — for outdoor culture, for a strong scene around a particular hobby, for a certain kind of nightlife or daytime rhythm. Tuning into that reputation, rather than only searching your own pre-existing interests, sometimes surfaces communities you wouldn't have thought to look for, but that turn out to be a genuinely good fit once you try them.</p>

    <h2>Don't let research replace action</h2>
    <p>It's worth naming a trap that's easy to fall into at this stage: turning the research itself into a comfortable substitute for actually showing up anywhere. Building a thorough list can feel productive — and it genuinely is a useful first step — but a long list that never turns into an actual visit produces exactly zero connection. Give yourself a firm limit on research time this week (fifteen to twenty minutes is plenty to get a workable starting list) and treat anything beyond that as avoidance dressed up as preparation.</p>

    <h2>Reconciling online research with the physical city</h2>
    <p>A search result is a starting hypothesis, not a guarantee — a group that looks active online can turn out to be dormant, and a poorly-designed listing can hide a genuinely thriving community. It's worth cross-checking anything promising against a second signal where possible: recent posts or comments suggesting real, current activity, a specific meeting time you can actually verify, or simply a willingness to show up once and see for yourself rather than over-researching from behind a screen. The map is useful, but the territory is where the actual connection happens.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Spend fifteen minutes right now searching one of the sources above for your specific interests and neighbourhood. Write down at least three concrete options — a class, a group, a regular spot — with enough detail (name, day, location) that you could show up without having to search again later.</p>
    </div>

    <p>Next lesson builds directly on this list, helping you filter it down to the communities most likely to actually fit — not just the ones that happen to be easiest to find.</p>
    """,
})

LESSONS.append({
    "lesson_num": 6, "module_num": 2, "module_title": "Navigation Systems",
    "lesson_title": "The Community Compass",
    "lesson_sub": "Finding communities that align with your values and interests",
    "tool": "Find Your People",
    "body": """
    <p>Not every option on the list you built last lesson deserves your limited social energy. Showing up to five different, unrelated one-off events a week feels productive, but it usually produces a wide spray of shallow contact rather than the repeated exposure that friendship actually requires. This lesson is about narrowing your list down to a smaller number of communities that are genuinely likely to fit — so the effort you do spend compounds instead of scattering.</p>

    <h2>Alignment matters more than proximity</h2>
    <p>It's tempting to prioritise whatever's closest or easiest, but the communities most likely to produce real friendship are the ones aligned with something that actually matters to you — a shared interest, a shared value, a shared identity, or a shared activity you'd do anyway even if no one else showed up. Alignment does two things at once: it gives you a natural, non-forced topic of conversation, and it filters for people who are more likely to become genuine friends rather than just familiar faces, because you already have something real in common.</p>
    <p>A useful filter question for anything on your list: would I keep doing this even if it never led to a single friendship? If yes, it's a strong candidate — you'll show up consistently regardless of social payoff, which is exactly what builds familiarity over time. If the honest answer is no, it's more likely to fizzle within a few weeks once the novelty wears off.</p>

    <h2>Depth over breadth, at this stage</h2>
    <p>It's better to commit to two or three communities and show up consistently than to sample ten once each. Repeated exposure to the same group of people is what turns "the person I sat near at trivia" into "the person I sat near at trivia three weeks running who I now say hello to by name." A single visit rarely produces that; five visits over five weeks very often does.</p>
    <p>As a starting target: pick two structured groups and one ambient hub from your list, commit to attending consistently for the next month, and treat everything else as optional exploration rather than obligation.</p>

    <h2>Use Find Your People to widen and sharpen the search</h2>
    <p>The Find Your People tool below takes your specific interests and gives you targeted community types, formats, and a concrete first step for each — often surfacing options you wouldn't have thought to search for directly. Use it to cross-check and expand the list you built last lesson, especially if you're finding it thin.</p>

    <h2>What to do when nothing on your list feels quite right</h2>
    <p>Sometimes the honest answer, after checking your list against the "would I do this anyway" filter, is that nothing on it clears the bar — everything feels like it's there mainly for the social payoff, not because you'd genuinely want to be doing it otherwise. If that's the case, it's worth widening your search rather than settling for a weak fit. Consider interests you've let lapse since before the move, or something you've always been mildly curious about but never had the occasion to try. A new city, inconveniently, is also a genuine opportunity to pick up something you wouldn't have started otherwise — and "genuinely interested, brand new to it" is often a better social starting point than "not that interested, doing it for the people," because everyone in a beginner group is on equal footing.</p>
    <p>It's also fine for your answer to change over the following weeks. The point of the filter isn't to make a permanent decision now — it's to stop you from spreading your limited energy across ten weak options instead of concentrating it on two or three genuinely promising ones, at least for the next month.</p>

    <h2>Give an option a fair trial before judging it</h2>
    <p>First visits to a new group are almost always a little awkward, no matter how well-matched the group turns out to be — you don't know the norms yet, you don't recognise anyone, and the natural in-jokes and rhythms of an established group take a visit or two to pick up on. It's a common and understandable mistake to write off a genuinely promising community after one slightly stilted first visit. A fairer test is three visits before deciding: the first is almost always the most awkward one, and the difference between visit one and visit three is often larger than people expect. If it's still clearly not working by visit three, that's a legitimate signal to move on to something else from your list — but give it that fair a trial first.</p>

    <h2>What "alignment" doesn't mean</h2>
    <p>Alignment doesn't require finding people who are similar to you in every way, or even most ways. It means sharing one genuine point of connection substantial enough to build on — an interest, a value, an activity — while leaving plenty of room for real differences elsewhere. Some of the most durable friendships form between people who'd look, on paper, quite different from each other, held together by one strong shared thread rather than broad similarity. Don't rule out a community just because the people in it don't otherwise resemble your old friend group; the one thing you have in common may end up mattering more than everything you don't.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>From your list, circle the two or three options that pass the "would I do this anyway" test. Put a specific date and time next to each one for this coming week — not "sometime soon," an actual date on your calendar. Vague intentions rarely survive an ordinary busy week; scheduled ones usually do.</p>
    </div>

    <p>With a short, aligned list and real dates on the calendar, you're set up for the next module: actually showing up and making first contact, without the added pressure of also having to figure out where to be.</p>
    """,
})

LESSONS.append({
    "lesson_num": 7, "module_num": 2, "module_title": "Navigation Systems",
    "lesson_title": "Crafting Your Social Strategy",
    "lesson_sub": "Building a personalised plan for engaging with new people",
    "tool": None,
    "body": """
    <p>You now have a filtered list of communities and dates on the calendar. This lesson turns that into an actual weekly rhythm — something specific enough to follow on autopilot during weeks when motivation is low, which, over a twelve-week course, will happen more than once.</p>

    <h2>Why a plan beats "seeing how I feel"</h2>
    <p>Relying on daily motivation to drive your social life is a losing strategy, for a simple reason: the exact conditions that make you feel like skipping a plan — tiredness, low mood, social anxiety about walking into a room of strangers — are usually the same conditions where showing up would help most. If the plan only happens on days you feel like it, it will happen inconsistently, and inconsistency is precisely what prevents the repeated exposure that builds friendship. A concrete weekly structure removes the daily negotiation and makes showing up the default, not a decision you have to win every time.</p>

    <h2>Building your weekly structure</h2>
    <p>Using your Module 3 baseline and your Module 6 shortlist, sketch a realistic weekly rhythm with three components:</p>
    <ul>
      <li><strong>Anchor commitments</strong> — your two structured groups from last lesson, on fixed days, treated like an appointment you don't renegotiate week to week.</li>
      <li><strong>One ambient touchpoint</strong> — a regular visit to your chosen low-pressure hub (the coffee shop, the gym, the dog park), aiming for familiarity rather than any specific outcome.</li>
      <li><strong>One flexible slot</strong> — held open for whatever opportunity comes up organically: an invitation, a one-off event that looks promising, or simply a lower-energy week where you lean on the ambient touchpoint alone.</li>
    </ul>
    <p>This is deliberately modest. The goal isn't to fill every evening — it's to build a rhythm you can actually sustain through an ordinary busy week, not just an ideal one. A realistic plan you follow consistently outperforms an ambitious plan you abandon after two weeks, every time.</p>

    <h2>Plan for resistance, not just the calendar</h2>
    <p>It's worth deciding in advance how you'll handle the moment — and there will be a moment — when you don't feel like going. A few approaches that tend to work better than willpower alone:</p>
    <ul>
      <li><strong>The 20-minute rule.</strong> Commit to showing up for just twenty minutes, with full permission to leave after that if you want to. Most of the time, the hardest part is walking in the door; once you're there, you usually stay longer than planned.</li>
      <li><strong>Lower the bar for "success."</strong> On a low-energy week, success might just mean showing up and saying hello to one person, not having a great time or making a new friend. That's still a rep, and reps are what count.</li>
      <li><strong>Tie it to something you already do.</strong> Attaching a new social commitment to an existing habit (going straight from work, going straight after your usual gym time) reduces the number of separate decisions you have to make.</li>
    </ul>

    <h2>Adjusting the plan without abandoning it</h2>
    <p>A weekly rhythm isn't meant to be rigid. Life will interrupt it — a busy work week, travel, illness, simple fatigue — and the goal is to adjust the plan rather than either forcing it through regardless or dropping it entirely the first time it gets disrupted. If a week genuinely can't accommodate the full rhythm, protect the anchor commitments first and let the flexible slot and ambient touchpoint flex around them, rather than the reverse. A rhythm that bends occasionally and gets picked back up is far more durable over twelve weeks than one that has to be followed perfectly or not at all.</p>
    <p>It's also worth reviewing the rhythm itself every couple of weeks, not just following it blindly. If one of your anchor commitments consistently feels like a chore rather than something you're glad you did, it's worth swapping it for another option from your Module 5 shortlist rather than gritting your teeth through it out of a sense of obligation to the plan. The plan exists to serve the actual goal — building genuine connection — not the other way around.</p>

    <h2>Keeping the plan visible</h2>
    <p>A rhythm that only exists as a mental intention tends to lose out to whatever feels most urgent in a given moment — and after a full day, an evening on the couch will almost always feel more urgent than a plan made a week earlier for a version of you with more energy. Writing the rhythm somewhere you'll actually encounter it during the week — a recurring calendar block with a reminder, a note pinned somewhere visible — shifts the decision from "do I feel like this right now" to "this is already the plan," which is a meaningfully easier decision to follow through on.</p>

    <h2>A plan is a starting point, not a contract</h2>
    <p>It's worth explicitly giving yourself permission to revise this plan as you learn more about what actually works for you over the coming weeks. The version you write today is your best current guess, made with limited information about this specific city and these specific communities. Treat weeks two and three as a live test of the plan, not a final commitment — you'll likely swap out at least one component once you have real experience to draw on instead of best guesses.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Write your weekly rhythm out in plain terms — day, time, place, for each of the three components above. Put it somewhere you'll actually see it (a note on your phone, a calendar block) rather than just in your head. Plans that live only in your head are the easiest ones to quietly drop.</p>
    </div>

    <p>You now have a map of your city, a shortlist of communities, and a weekly rhythm to follow. Module 3 is where the strategy meets the moment — the actual skills for walking into a room of strangers, starting a conversation, and making it memorable enough to lead somewhere.</p>
    """,
})

LESSONS.append({
    "lesson_num": 8, "module_num": 3, "module_title": "First Contact",
    "lesson_title": "Overcoming Approach Anxiety",
    "lesson_sub": "Practical techniques for managing nerves and initiating conversations",
    "tool": None,
    "body": """
    <p>Almost everyone feels some version of nerves before approaching a stranger or a group they don't know — including people who look completely at ease doing it. Approach anxiety isn't a sign you're bad at this; it's a near-universal response to genuine social uncertainty. This lesson isn't about eliminating that feeling. It's about understanding where it comes from and having a few concrete tools to act despite it, because waiting for the nerves to disappear before you approach someone usually means waiting indefinitely.</p>

    <h2>Where approach anxiety actually comes from</h2>
    <p>Approach anxiety is largely driven by two overlapping fears: the fear of rejection, and the fear of an awkward, effortful interaction. Both fears tend to get inflated by a very reliable cognitive bias — we consistently overestimate both how badly things will go and how much other people will judge us if they do. Researchers who study this call it the "spotlight effect": we assume we're being watched and evaluated far more closely than we actually are, because we're the centre of our own experience, so it feels like we must be the centre of everyone else's too.</p>
    <p>In practice, this means the gap between how bad an approach feels in your head beforehand and how it actually goes is usually much larger than it seems in the moment. Most people, most of the time, are perfectly friendly to a polite stranger who approaches them — mildly flattered, if anything, that someone made the effort.</p>

    <h2>The liking gap</h2>
    <p>There's a related, well-documented finding sometimes called the "liking gap": after a conversation with someone new, people systematically underestimate how much the other person enjoyed talking to them and how much the other person liked them. If your internal read of a conversation is "that was fine, but I don't think they were that into it," the honest statistical bet is that the other person's internal read was more positive than yours — not less. This is worth remembering specifically because approach anxiety often survives a genuinely good interaction, simply by reinterpreting it after the fact as more awkward than it actually was.</p>

    <h2>Techniques that make approaching easier</h2>
    <p><strong>Lower the stakes deliberately.</strong> You're not trying to make a friend for life in the next ninety seconds — you're trying to have one small, pleasant exchange. Reducing the goal to something that small makes the approach feel far less consequential, because it is far less consequential.</p>
    <p><strong>Use the environment as your opener.</strong> A comment about something shared and present — the event, the food, the weather, the activity — is almost always easier to deliver and easier to receive than an opener that requires more social courage, because it doesn't require any personal disclosure to start.</p>
    <p><strong>Approach groups at a natural gap.</strong> Joining a circle of people mid-conversation feels intrusive; joining right after a natural pause, a laugh, or when someone glances your way is much lower-friction and rarely reads as interruption.</p>
    <p><strong>Give yourself a physical count-in.</strong> If you're standing at the edge of a room working up the nerve, give yourself a literal countdown — "I will walk over by the time I count to five" — rather than an open-ended wait for the fear to subside on its own. The fear rarely fully subsides before you act; it mostly subsides after.</p>

    <h2>Reframing rejection</h2>
    <p>Even accounting for the biases above, some approaches genuinely won't land — someone's in a rush, mid-conversation, or just not in the mood. That's not a referendum on you. Treat each approach as a rep, not a test. The people who build strong social lives quickly aren't the ones with a 100% success rate on approaches; they're the ones who did enough reps that the average outcome, not any single interaction, is what shaped their social life.</p>

    <h2>What confident-looking people are actually doing differently</h2>
    <p>It's worth debunking a common assumption directly: people who seem to approach strangers effortlessly are, in the large majority of cases, not free of the nerves described above — they've simply built a higher tolerance for acting despite them, usually through sheer repetition rather than some innate advantage. Approach anxiety doesn't disappear through confidence arriving first; confidence tends to arrive after repeated evidence that approaching went better than predicted, which only accumulates through actually doing it while still nervous. In other words, the order most people expect — get confident, then approach — usually runs backwards from how it actually works in practice.</p>
    <p>This reframe matters practically: waiting to feel ready before you approach someone is, for most people, waiting for a precondition that arrives after the behaviour, not before it. The workable strategy is closer to acting slightly ahead of your confidence, on purpose, and letting the confidence catch up over the following weeks as the evidence accumulates.</p>

    <h2>A note on social anxiety specifically</h2>
    <p>If what you experience goes meaningfully beyond ordinary nerves — a persistent, intense fear of judgment that interferes significantly with daily life, not just new-city approaches — that's worth distinguishing from the general approach anxiety this lesson addresses. The techniques here are genuinely useful for everyday nervousness, but they're not a substitute for professional support if anxiety is a significant, ongoing burden for you. There's no shame in that being true, and getting support for it is entirely compatible with everything else in this course.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>At your next scheduled social plan, set yourself a small, specific target: approach or speak first to one person you don't already know. Not five. One. Notice afterward whether the interaction actually went as badly as it felt beforehand — write down what really happened, in plain terms, and compare it to what you predicted.</p>
    </div>

    <p>Next lesson gives you the actual language for what to say once you've made the approach — moving past small talk into openers that spark real interest rather than a polite dead end.</p>
    """,
})

LESSONS.append({
    "lesson_num": 9, "module_num": 3, "module_title": "First Contact",
    "lesson_title": "The Art of the Open-Ended Opener",
    "lesson_sub": "Moving beyond small talk to spark genuine interest",
    "tool": "Conversation Starter",
    "body": """
    <p>Small talk gets an unfair reputation. It's a genuinely useful, low-risk way to establish that an interaction is friendly and safe before either person invests more. But small talk is meant to be a doorway, not a destination — and a lot of promising interactions stall out because they never move past "how do you know the host" and "what do you do" into something that actually generates real conversation. This lesson is about that transition: how to open a conversation, and then how to move it somewhere more interesting without forcing it.</p>

    <h2>Closed questions vs. open questions</h2>
    <p>The single biggest lever here is the difference between closed and open questions. A closed question invites a short factual answer and a natural conversational dead end: "Do you live nearby?" "Yep." An open question invites a story, an opinion, or an elaboration: "What brought you to this neighbourhood?" tends to produce an actual answer with texture — a job, a relationship, a specific reason — that gives you multiple threads to follow up on.</p>
    <p>You don't need to abandon small talk entirely; you need to upgrade it. Instead of "what do you do," try "what's been the most interesting part of your work lately." Instead of "how do you know [host]," try "what's the story of how you two met." Same territory, same safety, but structured to produce something you can actually build on.</p>

    <h2>The follow-the-thread technique</h2>
    <p>A genuinely good conversationalist isn't usually someone with a mental list of clever questions. They're someone who listens for the most interesting detail in what the other person just said, and follows it, rather than moving on to their next planned question. If someone mentions they moved for a job, don't just nod and move to your next topic — ask what the job actually is, or what made them say yes to the move. That single habit — following the most interesting thread instead of your own script — does more to generate a real conversation than any specific opener could.</p>

    <h2>A few reliable opener templates</h2>
    <ul>
      <li><strong>Shared-context opener:</strong> "What made you come to this one?" / "How's this compare to [similar thing] you've been to before?"</li>
      <li><strong>Curiosity opener:</strong> "What's something you've been into lately that has nothing to do with work?"</li>
      <li><strong>Light-opinion opener:</strong> "Okay, hot take — is [something low-stakes and relevant] actually good, or is everyone just being polite about it?"</li>
      <li><strong>New-in-town opener:</strong> Being genuinely new is a legitimate, effective opener in itself: "I just moved here, honestly still figuring out where everything good is — any recommendations?" People are often generous and enthusiastic when asked for local advice, and it gives them an easy, specific thing to talk about.</li>
    </ul>
    <p>None of these need to be delivered perfectly. The content matters far less than your willingness to actually ask and then genuinely listen to the answer.</p>

    <h2>Use the Conversation Starter tool to build your own set</h2>
    <p>The Conversation Starter tool below generates personalised openers based on your specific situation and interests — useful both for practising the pattern above and for having a few ready-made lines in your back pocket before a specific event where you know you'll want them.</p>

    <h2>Recovering gracefully from an opener that falls flat</h2>
    <p>Not every opener lands, and that's fine — a flat response usually says more about timing, mood, or context than about the quality of the opener itself. If a question gets a short, closed answer, it's completely acceptable to pivot rather than treating it as a dead end: "fair enough" followed by a different angle, or simply a friendly comment and a natural exit if it's genuinely not landing. Trying to force a single opener to work through sheer persistence tends to read as more awkward than gracefully moving on ever would.</p>
    <p>It also helps to remember that a flat response to an opener is a single data point, not a referendum on the whole interaction or on you. Some people are simply more reserved in first exchanges, tired, or mid-conversation with someone else already. Treating each opener as a low-stakes attempt, worth trying and easy to let go of if it doesn't land, keeps the whole process feeling lighter than if every opener carried the full weight of "will this person like me."</p>

    <h2>Avoiding the interview feeling</h2>
    <p>A common trap once people learn the open-question pattern is firing off one open question after another without sharing anything of their own — which can start to feel more like an interview than a conversation. Good conversation is a genuine back-and-forth: after someone answers, offer a bit of your own related perspective or experience before moving to the next question. This isn't about matching their story point for point; it's about making sure you're participating in the conversation, not just extracting information from it.</p>

    <h2>Openers matter less than your willingness to try more than one</h2>
    <p>No single opener has a guaranteed success rate, and treating any one line as the make-or-break moment tends to add pressure that works against you. It's more useful to think in terms of your average across several attempts rather than the outcome of any one. A handful of decent openers used with reasonable frequency will consistently outperform a search for the theoretically perfect single line, largely because volume gives the follow-the-thread technique from above more chances to actually kick in.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Before your next social plan, generate three openers using the tool and pick one you actually feel comfortable saying out loud — it should sound like you, not like a script. Use it once, on purpose, and notice what the other person says back. That response is almost always more interesting than the opener itself.</p>
    </div>

    <p>Opening a conversation is only step one. The next lesson covers what makes an interaction actually memorable enough that someone thinks of you again afterward — active listening and the follow-up that turns a good conversation into an actual connection.</p>
    """,
})

LESSONS.append({
    "lesson_num": 10, "module_num": 3, "module_title": "First Contact",
    "lesson_title": "Active Listening & Follow-Up",
    "lesson_sub": "How to ensure memorable interactions that lead to next steps",
    "tool": None,
    "body": """
    <p>A conversation can go well in the moment and still lead nowhere, simply because nothing about it made you memorable afterward, or because neither person did anything to turn a nice fifteen minutes into an actual next interaction. This lesson covers both halves of that problem: how to listen in a way that makes people genuinely enjoy talking to you, and how to follow up afterward so the connection doesn't quietly evaporate.</p>

    <h2>What active listening actually looks like</h2>
    <p>Most people, in a normal conversation, spend a fair amount of time half-listening while partly thinking about what they'll say next. It's an understandable habit, but the other person can usually tell, even if only subconsciously — through slightly delayed or generic responses. Active listening means genuinely tracking what's being said, rather than just waiting for your turn.</p>
    <p>A few concrete markers of active listening: asking a specific follow-up question that could only come from actually having heard the detail ("wait, how did the trip actually go after that flight got cancelled?"), reflecting back what someone said in your own words before responding, and resisting the urge to immediately redirect to your own similar story. That last one is worth naming specifically — matching someone's story with your own ("oh that happened to me too, so this one time...") feels like relating, but if it happens before you've fully engaged with theirs, it can read as changing the subject to yourself.</p>

    <h2>Making yourself memorable, without performing</h2>
    <p>You don't need to be the most charismatic or entertaining person in the room to be memorable. People tend to remember two things far more than cleverness: how genuinely interested you seemed in them, and any specific, concrete detail that gave the interaction texture — a shared interest, an unusual detail about your work, a strong (but not divisive) opinion, a plan you mentioned. Vague, generically pleasant conversations are the ones that get forgotten by the next day; specific ones stick.</p>

    <h2>The follow-up is not optional</h2>
    <p>A good conversation with no follow-up is, socially speaking, close to a conversation that never happened. It's easy to assume the other person will reach out, or that the connection will naturally continue at the next event — but in a new city, where neither of you has an established rhythm of running into each other, that assumption fails more often than it succeeds. The follow-up is where most of the actual relationship-building happens, not the initial conversation.</p>
    <p>A good follow-up is specific, low-pressure, and timely:</p>
    <ul>
      <li><strong>Specific</strong> — reference something from your actual conversation, not a generic "nice meeting you." "Hey, this is [name] from [event] — let me know if you ever want to check out that trail you mentioned."</li>
      <li><strong>Low-pressure</strong> — propose something small and easy to say yes to, not an ambitious commitment. A coffee, not a weekend trip.</li>
      <li><strong>Timely</strong> — within a few days, while the conversation is still fresh in both of your minds. Waiting weeks makes the message feel out of nowhere rather than a natural continuation.</li>
    </ul>
    <p>If you don't have someone's contact information yet, asking for it at the natural end of a good conversation is far less awkward than it feels in the moment — "this was fun, let's grab coffee sometime, what's your number?" is a completely normal thing to say, and most people will be glad you did.</p>

    <h2>Ending a conversation well</h2>
    <p>How a conversation ends shapes memory of it almost as much as how it went in the middle. Trailing off awkwardly or abruptly excusing yourself tends to leave a slightly flat final impression, even after a genuinely good exchange. A clean close — a warm, specific comment ("this was really fun, I'm glad we got talking") paired with a clear but low-pressure next step ("let's actually get that coffee") — tends to leave a noticeably better final impression than simply letting the conversation fizzle out or wander off toward someone else mid-sentence.</p>
    <p>It's also worth resisting the urge to over-explain why you're leaving. A brief, warm close is generally received better than an elaborate justification, which can unintentionally draw more attention to the exit than necessary. People are used to conversations at social events naturally winding down and moving on; you don't need an extensive reason.</p>

    <h2>Following up when you're unsure it landed well</h2>
    <p>Even after a conversation that felt slightly awkward or uncertain, it's usually still worth following up. Recall the liking gap from Lesson 8 — your read of how the interaction went is a biased instrument, systematically skewed toward the negative. Waiting for total certainty that a connection wants to hear from you before reaching out means, in practice, very rarely reaching out at all. A brief, low-pressure follow-up costs little even if it's not reciprocated, and it removes the second-guessing that otherwise tends to compound the longer you wait.</p>

    <h2>Listening as a two-way signal</h2>
    <p>Good listening does something else worth noticing: it tends to invite better listening back. People generally mirror the quality of attention they're given, at least somewhat — a conversation where you're genuinely engaged often, in turn, draws out a more engaged, less guarded version of the other person than a conversation where both people are just waiting their turn. This isn't a technique to deploy strategically so much as a natural side effect of actually listening well, but it's worth knowing that the benefit runs in both directions.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>After your next good conversation with someone new, send a specific, low-pressure follow-up within 48 hours — even if it feels slightly uncomfortable. Notice that the discomfort is almost always front-loaded; it fades quickly once the message is sent, regardless of the response.</p>
    </div>

    <p>You now have the full toolkit for first contact: approaching, opening, listening, and following up. Module 4 is about what happens next — turning these initial sparks into something consistent enough to actually call a friendship.</p>
    """,
})

LESSONS.append({
    "lesson_num": 11, "module_num": 4, "module_title": "Building Bridges",
    "lesson_title": "The Power of Consistency",
    "lesson_sub": "Why showing up regularly matters and how to maintain momentum",
    "tool": None,
    "body": """
    <p>You're now roughly a third of the way through the course, past the initial groundwork and into real momentum-building. This module is about the specific mechanics of turning first contacts into something durable, and it starts with what's arguably the single highest-leverage factor in the entire process: showing up consistently, over time, to the same people and places.</p>

    <h2>Mere exposure: why familiarity does most of the work</h2>
    <p>One of the most robust, well-replicated findings in social psychology is the mere exposure effect: repeated, low-stakes exposure to a person, on its own, tends to increase how much you like them — independent of any particularly deep or meaningful interaction happening. This is a big part of why people so often become close with coworkers, classmates, or gym regulars despite nothing especially dramatic ever "happening" between them. Proximity plus repetition, sustained over time, is doing most of the work.</p>
    <p>This has a very practical implication for your strategy: showing up to the same structured group or ambient hub week after week is, on its own, a genuinely effective social strategy — even on the weeks where the conversation feels unremarkable or you don't do anything you'd call "bonding." The familiarity is accumulating even when it doesn't feel like it.</p>

    <h2>Why momentum is fragile in the early weeks</h2>
    <p>Early-stage connections are disproportionately fragile, because neither person has yet built the kind of habit or trust that makes a relationship self-sustaining. A single missed week, a schedule conflict, or a bit of awkwardness can be enough to quietly derail a promising connection at this stage — not because the connection was weak, but because it hadn't yet accumulated the repetition needed to become resilient. This is exactly why consistency matters more in these early months than it will later, once relationships have their own inertia.</p>

    <h2>Building momentum without forcing it</h2>
    <p><strong>Protect your anchor commitments specifically.</strong> Of everything on your calendar, your two anchor groups from Module 7 deserve the most protection against being cancelled for something else, precisely because their value comes from repetition. A single missed one-off event costs you little; a pattern of missed anchor commitments resets your progress toward familiarity with that group.</p>
    <p><strong>Show up even on unremarkable weeks.</strong> There's a strong temptation to skip a session when nothing exciting seems likely to happen — you're tired, the week's been ordinary, you don't feel like "performing." These are often exactly the weeks where showing up matters most, because the mere exposure effect doesn't require the interaction to be exciting to work.</p>
    <p><strong>Track momentum, not just outcomes.</strong> Rather than only measuring "did I make a friend this week," track simpler momentum indicators: did I show up to my anchor commitments, did I recognise more faces than last time, do people seem to expect me now. These are the leading indicators; friendship is the lagging one.</p>

    <h2>When to persist and when to let a connection go</h2>
    <p>Consistency is powerful, but it's not unconditional — it's worth being honest about the difference between a connection that's slow-building and one that's genuinely not reciprocated. If you're consistently the only one initiating, consistently getting minimal engagement, or consistently sensing real disinterest rather than just early-stage reserve, that's useful information, not a reason to push harder out of principle. The value of consistency described in this lesson applies to relationships showing some sign of mutual investment, even a small one — not to relationships where the effort is entirely one-sided over an extended period.</p>
    <p>A reasonable rule of thumb: give a promising-seeming connection real time and a few genuine attempts before drawing conclusions, in line with the timeline from Lesson 4 — but also trust a clear, consistent pattern once you actually see one, rather than explaining it away indefinitely. Redirecting the energy from a one-sided connection toward one with more mutual momentum is not giving up; it's allocating a limited resource where it's more likely to pay off.</p>

    <h2>Consistency compounds quietly</h2>
    <p>One reason consistency is easy to underrate is that its effects rarely show up as a single dramatic moment — there's no specific fourth visit where a group suddenly, visibly decides you belong. It shows up gradually, in small shifts you might not consciously register in the moment: someone using your name without being reminded, a seat that's implicitly become "yours," being included in a side conversation without having to insert yourself. These small shifts are the actual signal that consistency is working, even when nothing dramatic seems to be happening on any single visit.</p>

    <h2>Consistency applies to yourself, too</h2>
    <p>It's worth extending this same principle inward, not just toward the people and groups you're showing up for. Being consistent with the other habits from this course — your energy check-ins, your reflection exercises, your weekly rhythm — compounds in exactly the same quiet way. None of these individual pieces feel dramatic week to week, and that's precisely why they're easy to let slide. Treat your own follow-through on the course itself with the same consistency you're building toward your new social world.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Look at your calendar for the next two weeks and identify anywhere an anchor commitment might get quietly dropped in favour of something that feels easier in the moment. Decide now — before you're tired or unmotivated — that you'll protect it. Precommitting when your motivation is high is far more effective than relying on motivation in the moment.</p>
    </div>

    <p>Consistency lays the foundation, but it isn't the whole picture — it needs to be paired with sustainable pacing, which is what the next lesson addresses directly.</p>
    """,
})

LESSONS.append({
    "lesson_num": 12, "module_num": 4, "module_title": "Building Bridges",
    "lesson_title": "Managing the Energy Cost",
    "lesson_sub": "Pace yourself so you don't burn out mid-process",
    "tool": "Social Battery",
    "body": """
    <p>By this point in the course, most people have picked up real social momentum — which brings a new risk that wasn't as present in the earlier, slower weeks: burnout. It's a common and avoidable pattern to build up a promising social rhythm over several weeks, then quietly overextend, get exhausted, and pull back hard right when things were starting to compound. This lesson is about catching that pattern before it costs you the momentum you've built.</p>

    <h2>Why burnout tends to hit around this stage specifically</h2>
    <p>In the first few weeks, social plans often felt effortful and occasional, which naturally limited how much you were doing. By Module 4, many people have several active threads going at once — two anchor groups, an ambient hub, a couple of promising new connections all wanting follow-up — and it's easy to say yes to all of it, because after weeks of scarcity, having options feels good. But new connections are still higher-effort than established ones (see Lesson 3), and a full calendar of all-new-connection socialising can quietly drain you faster than it seems like it should, especially if you're also still managing all the normal logistics of a recent move.</p>

    <h2>Recognising the early signs</h2>
    <p>Burnout rarely arrives as a dramatic crash — it usually builds gradually, and the early signs are easy to miss or explain away:</p>
    <ul>
      <li>Dreading a plan you were genuinely looking forward to a week earlier</li>
      <li>Feeling flat or going through the motions during interactions that used to feel energising</li>
      <li>Cancelling plans last-minute more often than usual</li>
      <li>Feeling relieved rather than disappointed when something gets cancelled</li>
      <li>Irritability or shorter patience in unrelated parts of your day</li>
    </ul>
    <p>Any one of these, especially if it's a new pattern rather than how you normally feel, is worth treating as a signal to recalibrate — not as evidence you're bad at this or that the whole project isn't working.</p>

    <h2>Recalibrating without losing momentum</h2>
    <p><strong>Protect anchors, trim the rest.</strong> If you need to cut back, cut from the flexible or one-off layer first, and keep your two anchor commitments intact if at all possible — they're both your highest-value activity and the thing whose momentum is most costly to interrupt.</p>
    <p><strong>Build in a genuinely low-effort week deliberately.</strong> Rather than waiting until you're depleted, consider scheduling an intentionally lighter week every few weeks — fewer new-connection interactions, more recharge time — as routine maintenance rather than a reactive retreat.</p>
    <p><strong>Reconnect with your old social world on purpose.</strong> A call with an old friend is genuinely recharging in a way that a new interaction usually isn't, precisely because it requires no effort to be understood. Use it as fuel, not avoidance — the distinction from Lesson 1 still applies, but at a sustainable level, this kind of contact is a legitimate and valuable part of your recovery, not a substitute for local connection.</p>

    <h2>Revisit your baseline</h2>
    <p>Your social capacity from Lesson 3 was a starting estimate, taken before you'd built any local momentum. It's worth returning to the Social Battery tool now that you have a few weeks of real data — your actual capacity may have grown as new-connection interactions have become somewhat less effortful, or you may find you need more recovery time than you initially estimated. Either way, working from current, accurate information beats working from a three-week-old guess.</p>

    <h2>Communicating a lighter week without over-explaining</h2>
    <p>One thing that quietly makes burnout worse is the sense that pulling back requires a big explanation or apology to the people involved — which adds social pressure on top of the exhaustion itself. In most cases, it doesn't. "Can't make it this week, next one for sure" is a completely normal, low-friction thing to say to a group or a newer connection, and it very rarely needs to be more elaborate than that. Reserving detailed context for people you're already close to, and keeping it brief with newer connections, removes one more unnecessary source of friction during a week where you're already running low.</p>
    <p>It's also worth noticing that consistently showing up, with the occasional honest, low-key skip, reads completely differently to a group than sporadic, unexplained absences do. The anchor-commitment consistency you've built over the past few weeks (Lesson 11) gives you real credit here — one lighter week against a backdrop of reliable attendance doesn't undo the familiarity you've built; it's simply read as normal, ordinary life.</p>

    <h2>Burnout in one area can bleed into others</h2>
    <p>It's worth noticing that social burnout rarely stays neatly contained to your social life. Left unaddressed, it tends to spill over into sleep, general mood, and performance at work, because the underlying resource being depleted — attention and emotional bandwidth — isn't specific to any one domain. Treating early signs of social burnout seriously isn't just about protecting your progress on this course; it's about protecting your overall wellbeing during what's already a demanding stretch of adjusting to a new city.</p>

    <h2>A brief note on physical health</h2>
    <p>Sleep, movement, and basic nutrition all directly affect how much social energy you have available, and all three are easy to let slide during a demanding stretch of relocating and rebuilding a social world at the same time. If you notice your capacity has dropped more than expected, it's worth checking these basics before assuming the drop is purely social in nature. Protecting them isn't separate from your social strategy — it's part of the same energy budget this lesson is about.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Run through the early-signs list above honestly. If two or more are showing up, deliberately lighten next week's plan before you're forced to by exhaustion — pick one thing to skip guilt-free, and protect one extra evening for recovery.</p>
    </div>

    <p>Pacing yourself protects the progress you've already made. The next lesson turns to the other side of building bridges — the specific mechanics of inviting people and being invited, which is where acquaintances actually start becoming friends.</p>
    """,
})

LESSONS.append({
    "lesson_num": 13, "module_num": 4, "module_title": "Building Bridges",
    "lesson_title": "Inviting & Being Invited",
    "lesson_sub": "Strategies for turning acquaintances into friends",
    "tool": None,
    "body": """
    <p>There's a specific transition that has to happen for an acquaintance to become a friend: the relationship has to move outside of whatever shared context first connected you. Two people who only ever interact at the same weekly class are, technically, acquaintances who see each other regularly — not yet friends. The shift happens when someone extends the relationship beyond that container: a coffee, a one-on-one hang, an invitation to something unrelated to the original context. This lesson is about becoming the person who makes that extension happen, rather than always waiting for someone else to.</p>

    <h2>Why so few people extend the invitation first</h2>
    <p>In almost every group — a class, a team, a friend group — there's a small number of people who consistently do the inviting, and a much larger number who wait to be invited. This isn't because the waiters don't want more connection; it's because extending an invitation carries a small, specific risk of rejection that waiting doesn't. But someone has to be the one to extend it, or the relationship stays locked inside its original container indefinitely. Being willing to be that person, even occasionally, disproportionately accelerates how quickly your social life develops — because you're not depending on someone else to take the risk first.</p>

    <h2>Making the invitation genuinely easy to say yes to</h2>
    <p>The biggest lever for a successful invitation isn't confidence — it's specificity. A vague invitation ("we should hang out sometime") requires the other person to do all the work of turning it into a real plan, and vague invitations very often just quietly die. A specific invitation removes that friction:</p>
    <ul>
      <li><strong>Vague:</strong> "We should get coffee sometime." <strong>Specific:</strong> "Want to grab coffee Thursday morning before work, that place near the office?"</li>
      <li><strong>Vague:</strong> "We should hang out." <strong>Specific:</strong> "A few of us are doing trivia Tuesday, want to come?"</li>
    </ul>
    <p>Specific invitations are also lower-stakes to send, somewhat counterintuitively, because they're framed around a concrete activity rather than the relationship itself — you're proposing coffee, not proposing friendship, even though the second one is really what's happening.</p>

    <h2>Being a good person to invite</h2>
    <p>The flip side matters just as much: when someone does extend an invitation to you, how you respond shapes whether they'll do it again. A few things that make you easy — and rewarding — to invite:</p>
    <ul>
      <li><strong>Respond promptly</strong> — a slow or vague response reads as low interest, even when it's really just a busy inbox.</li>
      <li><strong>If you can't make it, offer an alternative</strong> — "can't Thursday, but I'm free Saturday if that works" keeps the door open, rather than leaving a flat no as the last word.</li>
      <li><strong>Show genuine enthusiasm when you say yes</strong> — a simple "yes, I'd love that" does more relational work than it seems like it should.</li>
      <li><strong>Reciprocate over time</strong> — if someone has invited you a few times and you haven't yet initiated back, that's worth noticing. Reciprocity is part of what signals the relationship is mutual, not one-sided.</li>
    </ul>

    <h2>Handling the fear that you're being "too much"</h2>
    <p>A common, quiet worry that stops people from extending invitations is the fear of coming across as overly eager, needy, or intense — especially early in a connection, and especially for people newer to actively initiating. It's worth naming this fear directly, because it's rarely calibrated to reality: one well-placed, specific, low-pressure invitation is a completely normal social move, not an intense one, and the large majority of people receive it exactly that way. The version of "too much" that actually damages a connection tends to involve a pattern — excessive frequency, disregard for a lack of response, pressure when someone says no — not a single, ordinary invitation extended in a reasonable way.</p>
    <p>If you do send an invitation and it goes unanswered or gets a no, the appropriate response is simple: accept it gracefully, without over-apologising or withdrawing entirely from the relationship. A single unanswered invitation is not a verdict on the whole connection, and continuing to be a normal, friendly presence afterward — without immediately re-extending another invitation — tends to keep the door open far better than either repeated pursuit or a sudden cold withdrawal.</p>

    <h2>Invitations get easier with repetition</h2>
    <p>Like approaching a stranger in Module 3, extending an invitation tends to feel disproportionately difficult the first couple of times and then noticeably easier after that, once you have a small amount of direct evidence that it generally goes fine. The discomfort here is front-loaded, not constant — it's worth pushing through the first few instances specifically because of how quickly it tends to ease once you have a few real data points of your own to draw on, rather than relying on the anticipated version in your head.</p>

    <h2>Invitations as a two-way audition</h2>
    <p>It's worth remembering that extending an invitation isn't only you being evaluated — you're also finding out something real about whether this connection has mutual momentum. A warm, prompt yes is genuinely useful information, and so, in its own way, is a pattern of decline. Framing invitations as mutual information-gathering, rather than a one-sided test of your own worth, tends to make them feel considerably lower-stakes to send.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Pick one person from an anchor group or ambient hub who you'd genuinely like to know better, and send them a specific, low-pressure invitation this week — using the specific-vs-vague pattern above. If the idea of doing this makes you want to skip it, that's a strong sign it's exactly the rep worth doing.</p>
    </div>

    <p>Extending the first few invitations is often the hardest part of this whole course, and also one of the most directly effective. The next lesson looks at what happens after — understanding the stages a friendship actually moves through as it deepens.</p>
    """,
})

LESSONS.append({
    "lesson_num": 14, "module_num": 4, "module_title": "Building Bridges",
    "lesson_title": "Navigating Early Friendships",
    "lesson_sub": "Understanding the stages of friendship development",
    "tool": None,
    "body": """
    <p>Once a connection has moved outside its original context — coffee's happened, plans are being made directly rather than only inside a group setting — it enters a genuinely new phase, with its own dynamics and its own common pitfalls. This lesson is a map of what typically happens next, so the normal bumps of early friendship don't get mistaken for signs that something's wrong.</p>

    <h2>The rough stages of an emerging friendship</h2>
    <p><strong>Stage one: testing the waters.</strong> Both people are still somewhat careful — conversation stays relatively light, plans are proposed tentatively, there's a bit of mutual politeness. This is completely normal and not a sign of low interest; it's how most friendships begin.</p>
    <p><strong>Stage two: increasing disclosure.</strong> Conversation starts to include more personal material — opinions, minor vulnerabilities, references to other parts of each person's life. Psychologists call this reciprocal self-disclosure, and it tends to happen gradually and roughly in step: one person shares something a bit more personal, the other reciprocates at a similar depth, and trust builds through that back-and-forth rather than all at once.</p>
    <p><strong>Stage three: testing reliability.</strong> Smaller moments start to test whether the relationship holds up under mild friction — a cancelled plan, a slow response, a minor disagreement. How both people handle these small tests matters more than it seems; handled with basic grace, they tend to build trust rather than damage it.</p>
    <p><strong>Stage four: established friendship.</strong> The relationship no longer needs a specific occasion to continue — it has its own gravity, plans happen more easily, and the friendship extends into more of both people's lives.</p>
    <p>This isn't a strict, linear checklist — real friendships move through these stages unevenly, sometimes skipping around, sometimes stalling at one stage for a while before moving forward. But recognising the general shape helps you correctly interpret where a specific connection currently sits.</p>

    <h2>Common early-friendship worries — and why they're usually not signals</h2>
    <p><strong>"They took a while to text back."</strong> Response time is a weak and unreliable signal of interest, especially early on, when neither person has yet built a rhythm of prioritising the other's messages. Read it charitably unless a clear pattern emerges over multiple interactions, not from a single instance.</p>
    <p><strong>"The last hangout felt a bit flat."</strong> Not every hangout in an emerging friendship will feel electric — some will be genuinely unremarkable, and that's fine. Consistency over time matters far more than any single interaction's quality.</p>
    <p><strong>"I always seem to be the one suggesting plans."</strong> Worth noticing, and worth naming honestly to yourself — but also worth remembering that some people are simply less likely to initiate regardless of their level of interest (see Lesson 13). Give it a few more data points before drawing a firm conclusion.</p>

    <h2>Matching disclosure pace, not forcing it</h2>
    <p>It's worth being mindful of the self-disclosure pattern from stage two specifically. Sharing something quite personal very early, before the other person has reciprocated at a similar depth, can occasionally feel like a mismatch in pace, even when it's well-intentioned. The generally reliable approach is to disclose slightly more than the other person has, rather than significantly more — inviting them to match rather than overshooting.</p>

    <h2>When the pace mismatches</h2>
    <p>Sometimes two people move through these stages at genuinely different speeds — one person feels ready for stage two disclosure while the other is still comfortably in stage one, or one person is initiating stage-three-level plans while the other still seems tentative. This isn't automatically a bad sign; people vary quite a bit in how quickly they open up, independent of how much they actually value the connection. A slower pace from the other side is often more about their general disposition or how many other close relationships they're currently managing than about how they feel about you specifically.</p>
    <p>The practical response to a pace mismatch isn't to force the faster pace onto the relationship, nor to assume the slower pace means the connection isn't worth continuing. It's to keep showing up consistently, at a pace slightly ahead of theirs rather than dramatically ahead, and let the relationship find its own speed. Some of the strongest friendships take noticeably longer than average to move through these stages, and are no less real or lasting for it.</p>

    <h2>Friendships don't all look the same shape</h2>
    <p>It's worth adding that not every good, real friendship needs to progress all the way to stage four to be genuinely valuable. Some of the most enjoyable relationships in a person's life settle comfortably at stage two or three — reliable, warm, mutually enjoyed, without ever becoming an every-week, tell-them-everything kind of closeness. Treating stage four as the only "real" outcome can make perfectly good stage-two and stage-three relationships feel like they're falling short, when they're often exactly what they're meant to be.</p>

    <h2>Trust your own read over the stage labels</h2>
    <p>These stages are a useful general map, not a precise diagnostic tool to apply rigidly to every relationship. Some connections skip a stage almost entirely; others move through them in a different order. If a relationship feels genuinely good and is moving forward in its own way, don't force it to match this framework exactly. Use the stages as a way to interpret uncertainty and doubt, not as a checklist that overrides your own direct experience of how a specific friendship is actually going.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Think of one connection currently in progress and honestly place it on the four-stage map above. Write one sentence about what a natural next step would look like to move it forward — a slightly more personal conversation, a repeat hangout, an invitation to something a bit further outside the original context.</p>
    </div>

    <p>You now understand both how to build new connections and how they typically develop over time. Module 5 shifts focus to what comes after the early stage — sustaining and expanding a network that's starting to take real shape.</p>
    """,
})

LESSONS.append({
    "lesson_num": 15, "module_num": 5, "module_title": "Sustaining Your Network",
    "lesson_title": "The Friendship Check-In",
    "lesson_sub": "Proactive ways to maintain connections and show appreciation",
    "tool": "Check-In Generator",
    "body": """
    <p>By this stage of the course, you likely have several connections in progress at once — some solidly established, some still emerging, a few that have gone quiet without any real falling-out. This module is about maintenance: the ongoing, mostly unglamorous work of keeping a growing social world actually alive, rather than letting new connections quietly compete with each other for attention until several fade at once.</p>

    <h2>Why connections go quiet without anything going wrong</h2>
    <p>Most friendships that fade don't fade because of conflict — they fade from simple neglect, usually on both sides at once, with neither person deciding to end things so much as both quietly deprioritising a connection that isn't yet on autopilot. This is especially common with connections still in stage one or two of the friendship arc from Lesson 14, before the relationship has built its own momentum. A single unreturned message, an uncommented life update, a missed catch-up — none of it fatal individually, but the pattern adds up.</p>
    <p>The fix isn't complicated, but it does require being proactive rather than assuming things will maintain themselves. A short, well-timed check-in message is disproportionately effective at keeping a connection alive relative to how little effort it takes to send.</p>

    <h2>What makes a check-in land well</h2>
    <p>The best check-ins share a few features: they reference something specific rather than being generic, they don't require an elaborate response, and they show genuine interest rather than reading as an obligation being discharged. "Hey, thinking of you, hope you're well" is well-intentioned but easy to leave unanswered, because it doesn't invite a specific response. "Hey, how did that work presentation go, the one you were stressed about?" is easy to reply to, because it references something concrete and shows you actually remembered.</p>
    <p>Timing matters too. A check-in doesn't need a special occasion — in fact, unprompted check-ins ("no particular reason, just thought of you") often land better than ones that feel obligatory, because they read as genuine rather than dutiful.</p>

    <h2>Building a light maintenance habit</h2>
    <p>Rather than relying on memory alone, it helps to build a small, low-effort system: a short mental or written list of the people you want to stay in touch with, and a loose rhythm for checking in — not rigid scheduling, but enough structure that connections don't slip through the cracks simply because you got busy. Even reaching out to one or two people a week, briefly, keeps a growing network genuinely alive rather than slowly thinning out.</p>

    <h2>Use the Check-In Generator when the words don't come easily</h2>
    <p>It's a very common experience to want to reach out to someone and then get stuck on exactly how to phrase it — worried about sounding random, needy, or out of nowhere. The Check-In Generator tool below takes who you want to reach out to and how long it's been, and produces a few natural, low-pressure message options, so the blank page doesn't become the reason the message never gets sent.</p>

    <h2>Check-ins work in both directions</h2>
    <p>It's worth remembering that maintenance isn't only about the messages you send — noticing and responding well to check-ins you receive matters just as much. A friend or new connection who reaches out deserves the same specificity and genuine engagement you're aiming for in your own messages: replying with real content rather than a bare "good, you?", and occasionally being the one to suggest turning the check-in into an actual plan rather than letting it stay purely conversational. A pattern of check-ins that never turn into plans can, over time, start to feel like the relationship is stuck at a surface level — worth noticing if it becomes a repeated pattern.</p>
    <p>It also helps to vary the kind of check-in you send rather than defaulting to the same message every time. A specific question about something ongoing in their life, a relevant article or recommendation that made you think of them, an actual invitation rather than just a conversational check-in — mixing these up keeps the relationship feeling attentive rather than routine, and gives you more natural ways to stay present in someone's life beyond a repeating script.</p>

    <h2>Maintenance matters most for the connections that aren't fully established yet</h2>
    <p>It's worth prioritising your check-in effort deliberately rather than spreading it evenly. Established, stage-four friendships (see Lesson 14) tend to have their own resilience and can usually survive a quiet stretch without much damage. Newer, stage-one or stage-two connections are far more fragile, and are exactly where a well-timed check-in does the most good — helping a promising but not-yet-solid connection survive the vulnerable early period rather than quietly fading before it's had the chance to become established.</p>

    <h2>Don't wait for a "big" reason</h2>
    <p>Many people implicitly wait for a significant occasion — a birthday, a major life update, a special event — before reaching out, which drastically limits how often anyone actually does it. The most sustainable maintenance habit treats an ordinary Tuesday as reason enough. In fact, an unprompted check-in with no special occasion attached often lands as more thoughtful, precisely because it signals you were thinking of someone without needing an external excuse to do so.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Think of one connection that's gone a bit quiet — not through any conflict, just drift. Send a specific, low-pressure check-in this week, referencing something real from your last interaction. Notice how much of the hesitation was really about the sending, not about the relationship itself.</p>
    </div>

    <p>Maintaining what you've built is only half the picture at this stage — the next lesson looks at deliberately expanding your circle further, using the connections you already have as a bridge to more.</p>
    """,
})

LESSONS.append({
    "lesson_num": 16, "module_num": 5, "module_title": "Sustaining Your Network",
    "lesson_title": "Expanding Your Circles",
    "lesson_sub": "How to leverage existing connections to meet even more people",
    "tool": None,
    "body": """
    <p>Once you have even a few real local connections, the work of expanding your social world gets noticeably easier — the connections you've already built become a bridge to more, rather than everything continuing to require the higher-effort work of meeting complete strangers. This lesson is about deliberately using that bridge rather than leaving it to chance.</p>

    <h2>Weak ties are more valuable than they seem</h2>
    <p>There's a well-known finding from sociology, often summarised as "the strength of weak ties": your close friends tend to know a lot of the same people you already know, because close social circles overlap heavily. Your looser acquaintances — the friendly coworker, the person from your class you don't know that well yet — are actually more likely to introduce you to genuinely new people, because their social circles don't overlap as much with yours. In practice, this means your growing list of newer, lighter local connections is a real and underused resource for expanding further, even though it doesn't feel as significant as your closer friendships.</p>

    <h2>Practical ways to leverage your existing network</h2>
    <p><strong>Ask directly, without overthinking it.</strong> "You mentioned a hiking group you're part of — would it be weird if I came along sometime?" is a completely normal, low-stakes request. Most people are glad to bring someone along to something they already enjoy; it rarely feels like an imposition unless you frame it as one.</p>
    <p><strong>Say yes to plus-one invitations.</strong> If someone invites you to something where you'll mostly know just them — a party, a group dinner, an event with their other friends — treat it as a genuine opportunity rather than a reason for anxiety. You already have one person in the room who wants you there, which is a significant head start compared to walking into a room alone.</p>
    <p><strong>Host something small yourself.</strong> Hosting flips the social dynamic in your favour — you become the connective node bringing people together rather than always being the one integrating into someone else's existing circle. It doesn't need to be elaborate: a casual dinner, a game night, a group trip to a low-key event. Even a modest gathering of four or five people, some of whom don't know each other yet, can meaningfully expand your network in a single evening.</p>
    <p><strong>Introduce people to each other.</strong> Actively connecting two people you know who might get along is a generous, low-cost act that tends to come back around — both because it strengthens your relationship with each of them, and because people who make good connectors tend to get included in more things themselves.</p>

    <h2>Balancing expansion with depth</h2>
    <p>It's worth being intentional here rather than treating expansion as an end in itself. A wider network is genuinely valuable — more resilience, more variety, more chances for a close friendship to emerge from an unexpected direction — but it shouldn't come at the direct expense of the deeper connections you're already building from Module 4. If your calendar is full of new, wide contact and nothing narrow and repeated, revisit Lesson 3's energy management and make sure your anchor relationships are still getting protected time.</p>

    <h2>Hosting without overthinking it</h2>
    <p>Hosting tends to carry an outsized intimidation factor relative to how simple it actually needs to be. It's easy to imagine hosting as requiring an impressive space, an elaborate meal, or a fully-formed friend group to invite — none of which is actually necessary. A genuinely effective first hosting attempt might be as simple as suggesting a casual potluck, inviting a few people from different parts of your still-forming network to a low-key game night, or organising a group outing to something you were going to do anyway, like a hike or a trivia night, and opening it up to a few extra people.</p>
    <p>The social value of hosting comes less from the polish of the event and more from the structural role you're taking on: you become the person who brought these specific people together, which tends to be remembered and appreciated well beyond the event itself. Even a modest, slightly imperfect gathering accomplishes this. Waiting for the "right" occasion or a fully-formed friend group to host tends to delay this disproportionately valuable move for far longer than necessary.</p>

    <h2>Quality still matters more than headcount</h2>
    <p>None of this is about maximising the raw number of people you know for its own sake. A larger, more varied network is valuable mainly because of what it enables — more paths to a genuine close friendship, more resilience if one relationship fades, more variety in your week. If expansion starts to feel like collecting contacts rather than genuinely getting to know people, it's worth returning to your Lesson 2 profile and recentring on the depth of connection you actually want, not just the width of your network.</p>

    <h2>Expansion works alongside everything else in this module</h2>
    <p>Notice how this lesson connects back to the maintenance habits from Lesson 15 — the check-ins you're sending to keep connections alive are also, indirectly, what keeps those connections willing and available to introduce you further into their world. A network that's well-maintained tends to open up more readily than one that's been left to go quiet, which is one more reason the two practices work best together rather than as separate, unrelated tasks.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Pick one existing connection and ask them directly to bring you along to something they're already part of — a group, an event, a regular hangout. If nothing comes to mind, consider hosting something small yourself in the next few weeks instead.</p>
    </div>

    <p>Expansion will occasionally come with setbacks — a plan that falls through, an invitation that doesn't lead anywhere, a connection that quietly fades despite your effort. The next lesson is about handling that resilience directly.</p>
    """,
})

LESSONS.append({
    "lesson_num": 17, "module_num": 5, "module_title": "Sustaining Your Network",
    "lesson_title": "Handling Setbacks & Rejection",
    "lesson_sub": "Developing resilience and learning from less successful interactions",
    "tool": None,
    "body": """
    <p>Not everything in this process will go well, and by this point in the course, you've likely had at least one experience that stung a bit — an invitation that got a lukewarm response, a connection that fizzled despite real effort, a plan that fell through more than once. This is a completely normal part of building a social life from scratch, not evidence that your approach is flawed. This lesson is about processing setbacks in a way that keeps you moving forward rather than pulling back.</p>

    <h2>Most setbacks aren't personal, even when they feel personal</h2>
    <p>A rejected invitation, a slow response, a connection that quietly fades — the honest base rate is that most of these have far more to do with the other person's circumstances, bandwidth, or life stage than with anything about you specifically. People are dealing with their own version of a full, complicated life: existing friendships that already take up their social bandwidth, work stress, family demands, or simply a different pace of building new relationships than you're on. None of that is visible to you in the moment, which makes it very easy to default to a personal explanation ("they just don't like me") when a circumstantial one is usually more accurate and more useful.</p>

    <h2>The difference between a setback and a pattern</h2>
    <p>A single setback is data, not a verdict — but it's also worth being honest with yourself about genuine patterns, rather than dismissing everything as bad luck. If the same specific issue shows up repeatedly across several different connections, it's worth a closer, non-judgmental look: are you consistently the one who has to initiate? Is there a particular part of conversation you tend to avoid? Are you unintentionally cancelling plans more often than you realise? The goal isn't self-criticism — it's useful information you can actually act on, which is a very different thing from a vague, global sense that "I'm bad at this."</p>

    <h2>Practical resilience tools</h2>
    <p><strong>Separate the outcome from your effort.</strong> You have real control over whether you approach, invite, and follow up. You don't have control over how someone else responds. Evaluating yourself on the things you actually control — did I make the attempt — rather than on outcomes you don't fully control keeps setbacks from feeling like personal failures.</p>
    <p><strong>Give yourself a short, deliberate reset.</strong> After a setback that stings, it's fine to take a day or two before your next attempt rather than forcing yourself back out immediately. The goal is a brief, intentional reset — not an indefinite retreat that quietly becomes avoidance.</p>
    <p><strong>Return to your win list.</strong> Revisit the realistic definition of progress you wrote in Lesson 4. A single setback rarely erases the real progress that's accumulated — it just feels, in the moment, like it does.</p>
    <p><strong>Remember the numbers game.</strong> Not every approach, invitation, or connection is meant to turn into a close friendship, and that's fine — you only need a handful of real connections to have a genuinely good social life. Treating each individual setback as expected, ordinary attrition, rather than a special failure, keeps the process from feeling more fragile than it actually is.</p>

    <h2>Processing the sting without dwelling in it</h2>
    <p>There's a difference between briefly feeling a setback and ruminating on it for days, replaying the interaction and searching for what you did wrong. A small amount of the former is normal and even useful — it's your brain flagging something worth paying attention to. Extended rumination, on the other hand, tends to produce more distorted, self-critical conclusions the longer it continues, without actually generating any more useful information than the first few minutes of reflection already provided. If you notice a setback is still occupying significant mental space after a day or two, it's often more productive to deliberately redirect — back to a scheduled anchor commitment, a check-in with an existing connection, anything that generates a small, positive counter-experience — rather than continuing to analyse the same setback from every angle.</p>
    <p>It also helps to talk it through with someone, whether an old friend from before the move or a newer local connection you trust. Saying a setback out loud to another person often reveals, almost immediately, how much smaller and more ordinary it sounds spoken than it felt while turning it over privately in your own head.</p>

    <h2>Resilience is a skill you're actively building</h2>
    <p>Every setback handled reasonably well — processed without spiralling, without abandoning the whole effort, without treating it as unique evidence of a personal flaw — is itself a form of practice, the same way approaching a stranger is practice for approaching. By the later weeks of this course, most people find setbacks sting noticeably less than they did in week one, not because fewer of them happen, but because the skill of processing them well has been building the entire time, mostly without being named as its own skill until now.</p>

    <h2>Setbacks tend to cluster near effort, not near failure</h2>
    <p>It's worth noticing, if you track it honestly, that setbacks often show up precisely during the periods you're putting in the most effort — more invitations sent, more approaches made, more attempts overall. That's not a sign the effort is backfiring; it's simple exposure. More attempts mean more chances for any single one not to land, in exactly the same way more at-bats mean more strikeouts even for a genuinely good hitter. Rising setback count alongside rising effort is closer to a sign you're doing this right than a sign something's going wrong.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Think of your most recent setback and write two short lists: what was genuinely in your control (and how you handled it), and what wasn't in your control at all. Notice how much of what stung actually falls into the second list.</p>
    </div>

    <p>You're nearing the end of the twelve weeks. The final module looks back at how far you've actually come, and forward at how to keep this going well past the end of the course.</p>
    """,
})

LESSONS.append({
    "lesson_num": 18, "module_num": 6, "module_title": "Your New Home",
    "lesson_title": "Reflecting on Your Journey",
    "lesson_sub": "Celebrating progress and recognising your growth over 90 days",
    "tool": None,
    "body": """
    <p>Twelve weeks ago, you started this course likely in the middle of the hardest stretch of the relocation loneliness arc from Lesson 1 — the dip, where the novelty has worn off and the absence of a social world feels loudest. This lesson is a deliberate pause to look back honestly at what's actually changed, before the final two lessons turn toward making it last.</p>

    <h2>Why this reflection matters more than it seems</h2>
    <p>Progress that happens gradually, week by week, is notoriously hard to feel in real time — the kind of change you only really notice when you stop and compare the start to now, rather than today to yesterday. Without a deliberate check-in, it's easy to keep operating from an outdated internal sense of "I don't really know anyone here" even after that's stopped being true, simply because the change happened too gradually to register on its own.</p>

    <h2>Revisit your own definitions</h2>
    <p>Go back to two specific things you wrote earlier in the course: your phase assessment from Lesson 1, and your personal definition of a win from Lesson 4. Read them again now, and answer honestly:</p>
    <ul>
      <li>Where are you now on the four-phase relocation arc, compared to where you were in week one?</li>
      <li>Which parts of your own "win" definition from Lesson 4 have you actually hit — fully, partially, or not yet?</li>
      <li>What's different about how you feel walking into a room of strangers now, compared to Module 3?</li>
    </ul>
    <p>Be specific and be honest in both directions — genuine progress deserves to be counted, and areas that are still a work in progress deserve to be named plainly rather than glossed over. Both are useful information for what comes next.</p>

    <h2>Progress rarely looks like what you expected at the start</h2>
    <p>It's worth naming directly: the social life you have now, twelve weeks in, is probably not identical to the one you pictured when you started — and that's completely normal, not a shortfall. Maybe the friendship you expected to form with one specific person didn't happen, but an unexpected one did, with someone from a group you almost didn't join. Maybe you don't yet have the deep, 200-hour close friendship from Lesson 4 — very few people do at the twelve-week mark — but you have real momentum with several people heading in that direction, which is exactly on schedule.</p>
    <p>Comparing your actual results to your imagined ones, rather than to a realistic twelve-week timeline, is one of the most common ways people underrate real, solid progress.</p>

    <h2>What you've actually built, even if it doesn't feel finished</h2>
    <p>Regardless of exactly where you land on the reflection above, consider what's now true that wasn't true in week one: you have a working map of your city's social infrastructure, a set of communities you know how to navigate, real experience approaching strangers and having it go better than your anxiety predicted, and — very likely — at least a few real, ongoing connections that didn't exist twelve weeks ago. That's not nothing. That's the actual infrastructure a social life is built from, and unlike your old city's invisible infrastructure, you now know exactly how you built it — which means you can build it again if you ever need to.</p>

    <h2>If the reflection is harder than expected</h2>
    <p>Not everyone finishes twelve weeks with the same amount of visible progress, and that's worth acknowledging honestly rather than glossing over. Life circumstances vary — some people had far less spare capacity during these twelve weeks than others, some cities and life stages simply make this process slower, some started from a harder place than others. If your honest reflection shows real but modest progress rather than a dramatic transformation, that's still meaningful progress, and it doesn't mean the process failed. The skills and infrastructure covered in this course don't expire at week twelve; they continue working for as long as you keep applying them, and plenty of people see their most significant progress in months four through six, well after a course like this technically ends.</p>
    <p>If the honest reflection reveals very little movement at all, it's worth a brief, non-judgmental look at which specific lessons or exercises got skipped along the way, rather than concluding the whole approach doesn't work for you. Often, a stalled twelve weeks traces back to one or two specific steps — the initial invitations from Lesson 13, the consistency from Lesson 11 — that never quite got attempted, rather than a fundamental mismatch between you and the process.</p>

    <h2>Let the reflection be genuinely mixed</h2>
    <p>An honest twelve-week reflection is rarely uniformly positive or uniformly disappointing — it's usually a mix: real wins alongside things that didn't pan out, growth in some areas alongside stagnation in others. Resist the urge to round this up into a tidy, all-good narrative or down into an all-bad one for the sake of a cleaner story. The genuinely mixed, specific version is both more accurate and more useful going forward than either polished extreme.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Write a short, honest paragraph comparing week one to now — specific names, specific plans, specific feelings, not just a general sense of "better" or "worse." Keep it. It's worth rereading on a future hard week, as concrete evidence of what you're capable of building.</p>
    </div>

    <p>The final two lessons are about what comes after this course ends — making the habits you've built sustainable for the long term, and knowing how to keep using the tools that got you here.</p>
    """,
})

LESSONS.append({
    "lesson_num": 19, "module_num": 6, "module_title": "Your New Home",
    "lesson_title": "Long-Term Connection Habits",
    "lesson_sub": "Establishing sustainable practices for ongoing social wellbeing",
    "tool": None,
    "body": """
    <p>The structure of this course ends soon, but a social life doesn't run on a twelve-week course — it runs on ongoing habits. This lesson is about which parts of what you've built are worth carrying forward permanently, so the progress from the last twelve weeks continues compounding rather than quietly reverting once the structured plan is gone.</p>

    <h2>What to keep from the course structure</h2>
    <p>Not everything from these twelve weeks needs to continue exactly as it was — some of it was scaffolding, useful specifically because you were starting from zero. But a few elements are worth deliberately keeping as ongoing habits, not just course exercises:</p>
    <ul>
      <li><strong>The anchor-commitment model.</strong> Having one or two recurring, protected social commitments — not necessarily the exact ones from this course — remains one of the most reliable ways to maintain and keep building a social life indefinitely, well past the initial relocation period.</li>
      <li><strong>Proactive check-ins.</strong> The habit from Lesson 15 of reaching out first, briefly and specifically, rather than waiting to be reached out to, is a durable skill that keeps any social network — new or old — from quietly thinning out over time.</li>
      <li><strong>Being an inviter, not just an invitee.</strong> The willingness from Lesson 13 to extend the first invitation is worth keeping as a general disposition, not a course-specific exercise — it's disproportionately valuable in any social context, for the rest of your life, not just this relocation.</li>
      <li><strong>Honest energy management.</strong> Your relationship with your own social capacity, from Lessons 3 and 12, doesn't stop mattering once you're settled. Pay attention to it on an ongoing basis, and adjust your social rhythm as your life and capacity change.</li>
    </ul>

    <h2>Letting go of the parts that were just scaffolding</h2>
    <p>Some things were genuinely useful specifically because you were starting from zero, and don't need to continue in the same form: the wide net of one-off events from Module 2 was mainly reconnaissance, useful for a from-scratch situation, not something you need to keep doing indefinitely once you have an established social world. Similarly, the deliberate, effortful pacing from Lesson 12 can relax somewhat as your local connections become more established and, per the mere exposure principle, genuinely less effortful to maintain.</p>

    <h2>Building a light long-term rhythm</h2>
    <p>Rather than either abandoning structure entirely or rigidly maintaining the exact twelve-week plan forever, aim for something in between: a light, ongoing check-in with yourself every month or two. A few honest questions to revisit periodically:</p>
    <ul>
      <li>Am I still protecting my anchor commitments, or have they quietly slipped?</li>
      <li>Is there anyone I've been meaning to check in with?</li>
      <li>Has my social capacity or my needs changed since I last really thought about it?</li>
      <li>Is there a new circle or interest worth exploring, the way I explored this city in Module 2?</li>
    </ul>
    <p>A social life, even a well-established one, benefits from this kind of light, occasional maintenance — it doesn't run entirely on autopilot indefinitely, but it needs far less deliberate effort once it has real momentum than it did at the very beginning.</p>

    <h2>Guarding against slow reversion</h2>
    <p>One realistic risk worth naming directly: without any structure at all, it's fairly common for the habits built over an intensive twelve-week period to erode slowly over the following months — not through any single decision to stop, but through the same kind of gradual neglect described in Lesson 15. A missed week here, a skipped check-in there, nothing dramatic enough to notice in the moment, until several months later the social rhythm has quietly thinned back out. This isn't a personal failing if it happens; it's simply what tends to occur when a effortful new habit loses its external structure all at once.</p>
    <p>The light periodic check-in described below is specifically designed to catch this kind of drift early, while it's still a minor correction rather than a full rebuild. Treat it as genuinely non-negotiable, in the same spirit as the anchor commitments from earlier in the course — a small, protected practice specifically because its value compounds over a much longer timeframe than any single check-in reveals on its own.</p>

    <h2>Habits that fit your actual life</h2>
    <p>The most durable version of any of these habits is the one that requires the least willpower to sustain — which usually means attaching it to something already stable in your life rather than treating it as a freestanding new discipline. An anchor commitment on the same day as an existing errand, a check-in habit tied to your regular commute, a monthly review tied to a bill you already pay around the same date. Habits that piggyback on existing structure tend to survive busy stretches far better than ones that depend entirely on remembering to do them from a blank slate.</p>

    <h2>A short permission slip</h2>
    <p>It's fine, and normal, for your long-term social life to look a bit different in month six than it did at the end of week twelve — busier some months, quieter others, shaped by whatever else is happening in your life at the time. The goal was never to reach a fixed, permanent end state and then stop paying attention. It was to build the skills and the confidence to keep adjusting a real, living social life over time, the same way anyone tends and adjusts anything else that matters to them.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Pick a recurring date — the first of every month, for example — and set a brief, standing reminder to ask yourself the four questions above. Five minutes, a couple of times a year, is enough to catch drift before it becomes a real gap.</p>
    </div>

    <p>The final lesson brings everything together — how the Humanly Labs tools you've used throughout this course fit into your ongoing social life, well beyond the twelve weeks.</p>
    """,
})

LESSONS.append({
    "lesson_num": 20, "module_num": 6, "module_title": "Your New Home",
    "lesson_title": "The Humanly Labs Ecosystem",
    "lesson_sub": "Using Friendship Audit + Social Battery for continued growth",
    "tool": "Friendship Audit",
    "body": """
    <p>This final lesson closes the course by connecting the tools you've used along the way into an ongoing system — one you can return to periodically, long after these twelve weeks are behind you, whenever your social life needs a check-up or a fresh push forward.</p>

    <h2>A quick recap of the tools in this course</h2>
    <ul>
      <li><strong>Loneliness Quiz</strong> (Lesson 2) — for understanding your specific connection needs, useful to revisit any time your circumstances change significantly.</li>
      <li><strong>Social Battery</strong> (Lessons 3 and 12) — for tracking your social energy and capacity, worth checking in with periodically as your life and rhythm evolve.</li>
      <li><strong>Find Your People</strong> (Lesson 6) — for surfacing communities aligned with your interests, useful again any time you want to deliberately expand into a new area of interest.</li>
      <li><strong>Conversation Starter</strong> (Lesson 9) — for generating openers, handy whenever you're heading into an unfamiliar social situation, not just during a relocation.</li>
      <li><strong>Check-In Generator</strong> (Lesson 15) — for maintaining connections without the friction of figuring out what to say, relevant for the rest of your social life, not just these twelve weeks.</li>
    </ul>

    <h2>Introducing the Friendship Audit</h2>
    <p>The Friendship Audit tool is the one built specifically for this stage — an ongoing check-up rather than a starting-point tool. It takes stock of your current social landscape as it actually is now: who you're connected to, how those relationships are doing, where there might be quiet gaps or connections that have drifted without you fully noticing. Where the Loneliness Quiz in Lesson 2 helped you understand what you needed at the very start, the Friendship Audit is designed to help you see, at any point going forward, what you've actually built and where it might need attention.</p>
    <p>Consider running it now, as a real snapshot of where things stand at the end of this course — and then again every few months going forward, as part of the light periodic check-in rhythm from the last lesson.</p>

    <h2>How the tools fit together as an ongoing system</h2>
    <p>Used together, these tools cover the full cycle of an ongoing social life, not just the from-scratch relocation process:</p>
    <ol>
      <li><strong>Assess</strong> — Friendship Audit, periodically, to see the current state of your network honestly.</li>
      <li><strong>Understand capacity</strong> — Social Battery, whenever your energy or rhythm shifts.</li>
      <li><strong>Expand</strong> — Find Your People, whenever you want to deliberately grow into a new area or interest.</li>
      <li><strong>Connect</strong> — Conversation Starter, whenever you're heading into a new or unfamiliar social situation.</li>
      <li><strong>Maintain</strong> — Check-In Generator, on an ongoing basis, to keep what you've built alive.</li>
    </ol>
    <p>You don't need to use all five constantly. Think of them as a toolkit to reach for at the specific moment each one is useful — the same way you'd reach for different tools at different stages of any long-term project, rather than using all of them at once, all the time.</p>

    <h2>Closing thought</h2>
    <p>Twelve weeks ago, moving to a new city with no social world in place probably felt like one of the harder things you'd taken on. You've since built a working map of your city, real experience initiating with strangers, an honest understanding of your own social energy, and — most importantly — actual relationships that didn't exist when you started. That's the real outcome of this course: not a finished, permanent social life that never needs attention again, but a working system, and the direct experience of having used it successfully once already. If you ever need to do this again — a future move, a big life change, a long stretch of drift — you now genuinely know how.</p>

    <h2>What to do if you need to relocate again someday</h2>
    <p>It's worth pointing out directly: everything covered in this course — the reframe of loneliness as a signal, the mapping of a new city's social infrastructure, the approach and conversation skills, the consistency and maintenance habits — is fully transferable to any future move, not specific to this particular relocation. The specific city changes; the underlying process doesn't. If you ever face this again, you won't be starting from the same uncertainty you started with this time. You'll already know the shape of the dip, roughly how long it tends to last, and exactly which concrete steps shorten it — which, by itself, tends to make a second relocation meaningfully less daunting than the first.</p>
    <p>The same is true even without a future move. The skills in this course apply just as directly to any major life transition that disrupts an existing social world — a career change, a new life stage like parenthood, an extended period of illness or caregiving, or simply a long stretch where an existing friend group has drifted apart. The underlying process of rebuilding a social world from a reduced starting point is the same one you've just practised directly.</p>

    <h2>One last honest note</h2>
    <p>Tools can meaningfully lower the friction of reaching out, expanding, or reflecting — but they're aids, not substitutes for the actual, sometimes uncomfortable human work of showing up, initiating, and following through that this entire course has walked you through. The real progress you've made over these twelve weeks came from you actually doing it, week after week, not from any single tool doing it for you. Keep that clear-eyed view of what these tools are for, and they'll keep being genuinely useful for as long as you need them.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Run the Friendship Audit now as your official end-of-course snapshot. Save or write down the result somewhere alongside your Lesson 18 reflection — together, they're a genuine record of what you built over these twelve weeks, worth having the next time you doubt your own progress.</p>
    </div>

    <p>That's the full course. Welcome to your new home.</p>
    """,
})

def slug_for(n, title):
    import re
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return f"{n:02d}-{s}"

def render_all():
    for i, lesson in enumerate(LESSONS):
        n = lesson["lesson_num"]
        slug = slug_for(n, lesson["lesson_title"])
        lesson["_slug"] = slug

    for i, lesson in enumerate(LESSONS):
        n = lesson["lesson_num"]
        prev_l = LESSONS[i - 1] if i > 0 else None
        next_l = LESSONS[i + 1] if i < len(LESSONS) - 1 else None
        prev_link = f'<a href="/courses/social-landing/content/lessons/{prev_l["_slug"]}.html">← Lesson {prev_l["lesson_num"]}: {prev_l["lesson_title"]}</a>' if prev_l else '<span class="nav-placeholder">← Start of course</span>'
        next_link = f'<a href="/courses/social-landing/content/lessons/{next_l["_slug"]}.html">Lesson {next_l["lesson_num"]}: {next_l["lesson_title"]} →</a>' if next_l else '<a href="/courses/social-landing/content/">Back to course overview →</a>'

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
            lesson_num=n,
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