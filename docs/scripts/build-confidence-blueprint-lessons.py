#!/usr/bin/env python3
"""
Generates the 18 individual lesson pages for The Confidence Blueprint course.
Run from its own directory: python3 build-confidence-blueprint-lessons.py
Source of truth for lesson content lives in this file (LESSONS list below).
"""
import os

OUT_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "courses", "confidence-blueprint", "content", "lessons",
)

TOOL_LINKS = {
    "Social Anxiety Check": ("🫁", "/social-anxiety"),
    "Social Battery": ("🔋", "/social-battery"),
    "Loneliness Deep Dive": ("🔬", "/deep-dive"),
}

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{lesson_title} — The Confidence Blueprint — Humanly Labs</title>
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
      --c-blue: #1C5DAF; --c-blue-l: #EBF2FB; --c-blue-b: #A3C0E8;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Instrument Sans', sans-serif; background: var(--c-bg); color: var(--c-ink); line-height: 1.65; }}
    nav {{ background: rgba(247,243,236,.95); border-bottom: 1px solid var(--c-border); padding: 0 2rem; position: sticky; top: 0; z-index: 100; }}
    .nav-inner {{ max-width: 760px; margin: 0 auto; height: 60px; display: flex; align-items: center; justify-content: space-between; }}
    .logo {{ font-family: 'Playfair Display', serif; font-size: 20px; color: var(--c-ink); text-decoration: none; }}
    .logo em {{ font-style: italic; color: var(--c-blue); }}
    .logo sup {{ font-size: 9px; color: var(--c-ink-3); vertical-align: super; margin-left: 2px; }}
    .main {{ max-width: 760px; margin: 0 auto; padding: 2.5rem 2rem 6rem; }}
    .breadcrumb {{ font-size: .8rem; color: var(--c-ink-3); margin-bottom: 1.5rem; }}
    .breadcrumb a {{ color: var(--c-blue); text-decoration: none; }}
    .breadcrumb a:hover {{ text-decoration: underline; }}
    .lesson-meta {{ display: flex; align-items: center; gap: .6rem; margin-bottom: .75rem; flex-wrap: wrap; }}
    .module-badge {{ background: var(--c-blue); color: #fff; border-radius: 8px; padding: 4px 10px; font-size: 11px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; }}
    .lesson-num-badge {{ font-size: 11px; font-weight: 600; color: var(--c-ink-3); }}
    h1.lesson-title {{ font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 500; line-height: 1.25; margin-bottom: .6rem; }}
    .lesson-sub {{ font-size: 1rem; color: var(--c-ink-2); margin-bottom: 2.5rem; padding-bottom: 2rem; border-bottom: 1px solid var(--c-border); }}
    .lesson-body h2 {{ font-family: 'Playfair Display', serif; font-size: 1.35rem; font-weight: 500; margin: 2.25rem 0 .9rem; color: var(--c-ink); }}
    .lesson-body p {{ margin-bottom: 1.1rem; color: var(--c-ink-2); font-size: .98rem; }}
    .lesson-body ul, .lesson-body ol {{ margin: 0 0 1.1rem 1.3rem; color: var(--c-ink-2); font-size: .98rem; }}
    .lesson-body li {{ margin-bottom: .5rem; }}
    .lesson-body strong {{ color: var(--c-ink); }}
    .exercise-box {{ background: var(--c-surface); border: 1px solid var(--c-border); border-left: 4px solid var(--c-blue); border-radius: 12px; padding: 1.5rem 1.75rem; margin: 2rem 0; box-shadow: var(--shadow); }}
    .exercise-box .exercise-label {{ font-size: 11px; font-weight: 600; letter-spacing: .06em; text-transform: uppercase; color: var(--c-blue); margin-bottom: .6rem; }}
    .exercise-box p:last-child {{ margin-bottom: 0; }}
    .note-box {{ background: var(--c-blue-l); border: 1px solid var(--c-blue-b); border-radius: 12px; padding: 1.1rem 1.4rem; margin: 2rem 0; font-size: .9rem; color: var(--c-ink-2); }}
    .note-box strong {{ color: var(--c-ink); }}
    .tool-box {{ background: var(--c-blue-l); border: 1px solid var(--c-blue-b); border-radius: 12px; padding: 1.25rem 1.5rem; margin: 2rem 0; display: flex; align-items: center; gap: 1rem; }}
    .tool-box .tool-emoji {{ font-size: 1.75rem; flex-shrink: 0; }}
    .tool-box .tool-copy {{ flex: 1; font-size: .9rem; color: var(--c-ink-2); }}
    .tool-box .tool-copy strong {{ color: var(--c-ink); display: block; margin-bottom: 2px; }}
    .tool-box a {{ background: var(--c-blue); color: #fff; text-decoration: none; font-size: .85rem; font-weight: 500; padding: 8px 16px; border-radius: 999px; white-space: nowrap; flex-shrink: 0; }}
    .lesson-nav {{ display: flex; justify-content: space-between; gap: 1rem; margin-top: 3rem; padding-top: 2rem; border-top: 1px solid var(--c-border); }}
    .lesson-nav a {{ font-size: .875rem; color: var(--c-blue); text-decoration: none; font-weight: 500; }}
    .lesson-nav a:hover {{ text-decoration: underline; }}
    .lesson-nav .nav-placeholder {{ color: var(--c-ink-3); font-size: .875rem; }}
    .support-box {{ background: var(--c-surface); border: 1px solid var(--c-border); border-radius: 14px; padding: 1.5rem; margin-top: 3rem; text-align: center; }}
    .support-box p {{ font-size: .875rem; color: var(--c-ink-2); }}
    .support-box a {{ color: var(--c-blue); }}
    footer {{ text-align: center; padding: 2rem; font-size: 12px; color: var(--c-ink-3); border-top: 1px solid var(--c-border); }}
    footer a {{ color: var(--c-ink-3); text-decoration: none; }}
    @media (max-width: 600px) {{ .main {{ padding: 2rem 1.25rem 4rem; }} h1.lesson-title {{ font-size: 1.6rem; }} .tool-box {{ flex-direction: column; align-items: flex-start; }} }}
    a:focus-visible, button:focus-visible {{ outline: 2px solid var(--c-blue); outline-offset: 3px; border-radius: 4px; }}
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
    <span style="font-size:13px;color:var(--c-ink-3)">🧠 The Confidence Blueprint</span>
  </div>
</nav>
<main class="main">
  <div class="breadcrumb"><a href="/courses/confidence-blueprint/content/">← Back to course overview</a></div>
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
    "lesson_num": 1, "module_num": 1, "module_title": "Mapping Your Anxiety",
    "lesson_title": "The Anatomy of Social Anxiety",
    "lesson_sub": "How the fear-avoidance cycle works and why it strengthens over time",
    "tool": None,
    "body": """
    <p>If social situations regularly leave you anxious, over-analysed, or wanting to disappear, you're dealing with something extremely common — social anxiety is one of the most widespread patterns of human difficulty, spanning everything from mild self-consciousness in unfamiliar settings to a persistent, life-shaping fear of judgment. This lesson lays the groundwork for the whole course: understanding the actual mechanics of how social anxiety works, so the rest of what you learn makes sense as a coherent approach rather than a disconnected list of tips.</p>

    <p>A brief, important note before we start: this course draws on well-established Cognitive Behavioural Therapy (CBT) and exposure-based principles, translated into practical steps. It's built to help with the common range of social anxiety — self-consciousness, avoidance, and persistent worry about judgment. It isn't a replacement for professional treatment. If your anxiety is severe, involves panic attacks, or is significantly limiting your life, working through this course alongside a therapist trained in CBT will get you further, faster, than either alone.</p>

    <h2>The fear-avoidance cycle</h2>
    <p>At the centre of nearly all social anxiety is a self-reinforcing pattern psychologists call the fear-avoidance cycle, and understanding its mechanics is the single most useful thing you can learn in this entire course. It runs roughly like this: a social situation triggers an anxious prediction (something bad will happen, I'll be judged, I'll embarrass myself) → the prediction produces real physical and emotional discomfort → to escape that discomfort, you avoid the situation, or endure it while doing something to protect yourself (avoiding eye contact, rehearsing exit lines, saying very little) → the relief of escaping or protecting yourself feels like confirmation that avoidance was the right call → the anxious prediction about that type of situation gets stronger for next time.</p>
    <p>The cruel trick of this cycle is that avoidance always feels like the solution in the moment — the anxiety genuinely does go down once you leave or avoid the situation — while actually being the mechanism that keeps the whole system running. Every successful avoidance is, neurologically, a rehearsal that confirms the danger was real and escaping was necessary, even when nothing bad was ever going to happen in the first place. This is why social anxiety so often gets worse over time rather than better on its own: the cycle is self-sustaining unless something deliberately interrupts it.</p>

    <h2>Why this isn't about willpower or personality</h2>
    <p>It's worth being direct about something many people carry a lot of unnecessary shame over: social anxiety is not a character flaw, a sign of weakness, or evidence that you're fundamentally bad at being around people. It's a learned pattern — sometimes shaped by specific past experiences (being embarrassed, excluded, or harshly judged), sometimes by a naturally more sensitive nervous system, often by some combination of both — and learned patterns, unlike fixed traits, can be unlearned. The entire premise of this course rests on that fact: the fear-avoidance cycle got built through repetition, and it can be dismantled the same way, through a different kind of repetition, deliberately structured rather than left to chance.</p>

    <h2>What "getting better" actually looks like</h2>
    <p>It's worth setting an honest expectation early: the goal of this course isn't to eliminate anxiety entirely, or to turn you into someone who feels nothing walking into a room of strangers. Some baseline nervousness in genuinely new or high-stakes social situations is normal for nearly everyone, anxious or not. The realistic goal — and a genuinely achievable one — is to shrink the anxiety down to a manageable level, stop it from driving avoidance, and build enough tolerance for the discomfort that it stops running your decisions. People who've worked through this kind of process typically don't describe becoming fearless; they describe the fear becoming quieter, more manageable, and much less able to dictate what they do and don't do.</p>

    <h2>What this course won't ask you to do</h2>
    <p>This isn't a course about forcing yourself to become fearless, or about treating every social interaction as a challenge to be conquered through sheer willpower. It's a structured process, grounded in well-established techniques, that works specifically because it's gradual and evidence-based rather than relying on forcing yourself through raw effort alone. You'll keep your own pace throughout, and the goal is a genuinely manageable, workable relationship with social situations — not a personality transplant into someone entirely different from who you actually are.</p>
    <p>It's also worth setting expectations about timeline. Real, durable change in anxiety patterns typically takes weeks to months of consistent work, not days. If you've tried to "just get over" social anxiety before through sheer force of will and found it didn't stick, that's not evidence you're uniquely resistant to change — it's evidence that willpower alone, without the structured cognitive and exposure techniques this course provides, usually isn't enough on its own. The structure matters as much as the effort.</p>

    <h2>How this course is structured</h2>
    <p>Each module builds directly on the one before it: Module 1 maps your specific anxiety pattern, Module 2 gives you tools for the thoughts driving it, Module 3 puts those tools into action through structured exposure, Module 4 builds the practical conversational skills that make interactions go more smoothly once anxiety is less dominant, Module 5 addresses the very real energy cost of doing this work, and Module 6 consolidates everything into a sustainable, ongoing approach. Skipping ahead rarely works well here — each module genuinely depends on groundwork from the ones before it, so working through them in order, even when a later module feels more urgently relevant to your specific struggles, will serve you better than jumping straight to it.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Think of one recent social situation you avoided, or got through only by protecting yourself somehow (staying quiet, leaving early, avoiding eye contact). Write down: what did you predict would happen if you hadn't avoided or protected yourself that way? Keep this note — you'll return to it directly in Lesson 5.</p>
    </div>

    <p>The next two lessons build your specific map: exactly which situations trigger your anxiety and how, and how your energy and nervous system respond to social demand. From Module 2 onward, we start actively working on the thoughts and predictions that drive the cycle you've just learned about.</p>
    """,
})

LESSONS.append({
    "lesson_num": 2, "module_num": 1, "module_title": "Mapping Your Anxiety",
    "lesson_title": "Your Trigger Map",
    "lesson_sub": "Identifying your specific social situations and avoidance patterns",
    "tool": "Social Anxiety Check",
    "body": """
    <p>Social anxiety rarely shows up identically in every situation — most people have a fairly specific pattern of triggers, rather than a uniform fear of all social contact. Someone might feel completely at ease one-on-one with a close friend but dread walking into a party alone. Someone else might handle groups fine but freeze up specifically when asked to speak in a meeting. Treating "social anxiety" as one undifferentiated thing makes it much harder to work on directly. This lesson is about building a specific, honest map of your own pattern, which the rest of the course will use as its working material.</p>

    <h2>Situational triggers vs. general anxiety</h2>
    <p>It helps to separate two related but distinct things: situational triggers (specific types of social contexts that reliably spike your anxiety — public speaking, group settings, one-on-one conversations with people you don't know well, authority figures, being the centre of attention) and the underlying anxious thought patterns that show up across many of those situations (fear of judgment, fear of saying something wrong, fear of visible physical anxiety symptoms). Mapping the specific situations first gives you something concrete to work with; the underlying thought patterns, which Module 2 covers directly, tend to become clearer once you can see them showing up repeatedly across your specific trigger list.</p>

    <h2>The three components of an avoidance pattern</h2>
    <p>For each trigger situation, it's worth noting three separate things, because they call for slightly different responses later in the course:</p>
    <ul>
      <li><strong>Full avoidance</strong> — situations you skip entirely: declining invitations, avoiding certain classes or events, staying home rather than risk it.</li>
      <li><strong>Safety behaviours</strong> — ways you protect yourself while still attending: over-rehearsing what you'll say, staying near the exit, checking your phone to look occupied, avoiding eye contact, staying quiet and letting others lead.</li>
      <li><strong>Post-event processing</strong> — the anxious replay afterward: mentally re-running the interaction, searching for evidence you embarrassed yourself, assuming the worst interpretation of anything ambiguous.</li>
    </ul>
    <p>All three keep the fear-avoidance cycle from Lesson 1 running, even though safety behaviours and post-event processing are much less visible than full avoidance — you might be attending plenty of social events and still be firmly stuck in the cycle, because the safety behaviours and the anxious replay afterward are doing the same maintaining work that skipping the event entirely would do.</p>

    <h2>Building your map without judgment</h2>
    <p>As you build this map, it's genuinely important to do it without self-criticism. The goal is accurate observation, not a list of personal failings. Every pattern you identify — even ones that feel embarrassing to admit, like rehearsing an entire conversation in the car beforehand, or leaving events early on a manufactured excuse — is completely ordinary anxious-mind behaviour, not evidence of some deeper flaw. The more honestly you can name these patterns now, without shame getting in the way, the more useful the rest of this course will be, because every later module builds directly on this map.</p>

    <h2>Use the Social Anxiety Check to structure your map</h2>
    <p>The Social Anxiety Check tool below runs a structured assessment of your specific triggers, safety behaviours, and typical anxiety intensity across common social situations, giving you a clear, organised starting profile rather than a vague sense of "I get anxious sometimes." Take it now, answering based on how things have actually been for you recently, not how you think they should be.</p>

    <h2>A note on how detailed to get</h2>
    <p>It's worth aiming for real specificity here rather than broad categories. "Parties" is too broad to be useful; "arriving at a party alone, after most people have already arrived and formed into small groups" is specific enough to actually work with later. The more precisely you can describe not just the situation but the exact moment or aspect of it that spikes your anxiety most, the more useful your map becomes for building the exposure ladder in Module 3 — vague categories produce vague, hard-to-execute exposure items, while specific descriptions translate directly into concrete, doable steps.</p>
    <p>It also helps to note roughly how long you've been avoiding or managing each situation this way. Some patterns are relatively recent and may loosen relatively quickly; others have been reinforced for years and may reasonably take longer. Neither timeline is a problem — it's simply useful context for setting realistic expectations about your own specific process, rather than comparing your pace to some generic timeline that may not reflect how long your particular pattern has had to become established.</p>

    <h2>Physical symptoms belong on the map too</h2>
    <p>Alongside the situations themselves, it's worth noting the specific physical symptoms that show up for you — racing heart, blushing, shaky voice, sweating, a blank mind — since these often become their own secondary source of anxiety (fear of the symptoms being visible, on top of fear of the original situation). Module 2's cognitive work and Module 3's exposure work both apply directly to this secondary layer as well, but only if it's explicitly on your map rather than left as an unexamined, background worry running underneath everything else.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>After the assessment, pick your top three trigger situations and write, for each one, what you typically do to avoid or protect yourself. This specific list becomes the raw material for your exposure ladder in Module 3 — the more concrete it is now, the more useful it'll be then.</p>
    </div>

    <p>You now have a specific map instead of a vague, overwhelming sense of "I struggle socially." That specificity is genuinely powerful — it turns an abstract feeling into a concrete, workable list, which is exactly what the rest of this course is designed to work with.</p>
    """,
})

LESSONS.append({
    "lesson_num": 3, "module_num": 1, "module_title": "Mapping Your Anxiety",
    "lesson_title": "Social Energy & Your Baseline",
    "lesson_sub": "Understanding how your nervous system responds to social demands",
    "tool": "Social Battery",
    "body": """
    <p>Social anxiety and social energy are related but genuinely distinct things, and it's worth untangling them clearly before moving further into this course. Anxiety is about a threat prediction — the anticipation that something bad will happen. Energy is about a resource being spent — the actual physiological and cognitive cost of being socially engaged, which happens regardless of whether anxiety is present. For many people dealing with social anxiety, these two things compound each other: anxious social situations are more energy-costly than calm ones, because your nervous system is doing extra work — scanning for threat, monitoring yourself, suppressing visible signs of distress — on top of the ordinary effort of the interaction itself.</p>

    <h2>Why anxious socialising is more exhausting</h2>
    <p>A calm, low-anxiety social interaction draws on your normal social effort: following the conversation, responding appropriately, reading the other person's cues. An anxious one adds a second, parallel layer of effort running the whole time: monitoring your own anxiety symptoms, worrying about how you're coming across, mentally rehearsing what to say next instead of being present, and managing whatever safety behaviours you identified in Lesson 2. This second layer is genuinely, measurably more taxing — which is why an anxious social interaction can leave you far more depleted than a calm one of the same length, even though from the outside they might look similar.</p>
    <p>This matters practically because it means your energy limits aren't fixed — they shift depending on how anxious a given interaction is, not just how long or how socially demanding it is in a neutral sense. Learning to read this accurately, rather than assuming a flat, constant social capacity, is an important skill this course will keep returning to, particularly in Module 5.</p>

    <h2>Your nervous system's actual response</h2>
    <p>The physical sensations of social anxiety — racing heart, tight chest, shaky hands, a flushed face, a mind that goes blank — are your body's fight-or-flight system activating in response to a perceived threat, the same system that would activate for a genuine physical danger. This is worth understanding clearly, because a huge amount of anxiety about anxiety comes from misinterpreting these very normal physical sensations as evidence that something is actually wrong, or as visible proof of embarrassment to others (a distortion Lesson 6 covers directly). The sensations themselves are not dangerous, however uncomfortable they feel — they're your nervous system doing exactly what it evolved to do, just in response to a threat that, in a social context, usually isn't actually there.</p>

    <h2>Establishing your baseline honestly</h2>
    <p>Before working to change anything, it's useful to have an honest read of where you currently stand: roughly how much low-anxiety social contact you can sustain in a week versus how much high-anxiety social contact, and how long recovery typically takes after each. This isn't about judging your current capacity as too low — it's simply useful information for pacing the exposure work in Module 3 sensibly, so you're neither so cautious that progress stalls, nor so aggressive that you burn out and reinforce the avoidance cycle through a bad experience early on.</p>

    <h2>Use the Social Battery tool to map your current capacity</h2>
    <p>The Social Battery tool below helps you take stock of your current energy patterns — what depletes you, what restores you, and how much social contact you can currently sustain. Use it now as a baseline, and expect to return to it in Module 5, once some of the anxiety-specific work has had a chance to shift how costly certain interactions feel.</p>

    <h2>Sleep, stress, and your anxious baseline</h2>
    <p>It's worth noting directly that your general physiological state significantly affects how much capacity your nervous system has for handling anxious activation on any given day. Poor sleep, high general stress, illness, or even just a demanding week at work can all lower your baseline resilience, making a social situation that would normally be manageable feel disproportionately difficult. This isn't a sign the anxiety work isn't holding — it's a sign your overall system is running with less spare capacity that day. Learning to factor this in, rather than assuming a bad day is purely about the social situation itself, will make your energy readings throughout this course considerably more accurate.</p>
    <p>This is also worth keeping in mind if you notice your anxiety seems worse on a day when, by your own account, "nothing anxiety-provoking is even happening." A depleted baseline can make ordinary, previously comfortable interactions feel harder than usual, independent of any change in the situations themselves — worth checking your sleep, stress, and general physical state before concluding the anxiety work has stalled or reversed.</p>

    <h2>You're not just tired — you're tired in a specific way</h2>
    <p>It's worth distinguishing social depletion from general tiredness, since they can call for different responses. General physical fatigue tends to respond well to rest and sleep; social depletion specifically responds best to the kind of recovery covered in Module 5 — time without social demand, not simply time without activity. Confusing the two can lead to "resting" in ways that don't actually restore your social capacity, only to find yourself still depleted going into the next social commitment despite having technically rested.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>After using the tool, write one sentence naming the difference, if any, between how much low-anxiety social contact you can handle versus high-anxiety social contact. This distinction will directly inform how you pace your exposure work later in the course.</p>
    </div>

    <p>You now have a full picture: how the fear-avoidance cycle works, your specific trigger map, and an honest read of your energy baseline. Module 2 turns to the thoughts themselves — the specific predictions and distortions that drive the whole cycle, and the evidence-based techniques for challenging them.</p>
    """,
})

LESSONS.append({
    "lesson_num": 4, "module_num": 2, "module_title": "Rewriting the Story",
    "lesson_title": "The Thoughts Behind the Fear",
    "lesson_sub": "Identifying the cognitive distortions that fuel social anxiety",
    "tool": None,
    "body": """
    <p>Underneath every anxious social prediction is a specific thought, even when it happens so fast it barely registers as a distinct thought at all — more like an instant, automatic sense of dread. CBT calls these automatic thoughts, and learning to notice them clearly, rather than just feeling their downstream emotional effect, is the foundation for everything the next two lessons build on. This lesson is about slowing that process down enough to actually see the thoughts driving the fear.</p>

    <h2>Automatic thoughts happen faster than you notice</h2>
    <p>In an anxious social moment, what you consciously experience is usually just the feeling — a wave of dread, an urge to leave, a blank mind — without necessarily noticing the specific thought that triggered it. That thought is still there; it's just moving fast enough, and has been repeated often enough, that it fires almost instantly and automatically, the way a well-practised skill runs without conscious thought. The first real skill of this module is learning to catch these thoughts by deliberately slowing down and asking, in the moment or immediately after: what did I just predict would happen?</p>

    <h2>Common distortions in socially anxious thinking</h2>
    <p>Certain patterns of distorted thinking show up especially often in social anxiety. Recognising your own versions of these is often the first moment things start to shift, simply because naming a distortion clearly tends to loosen its grip somewhat, even before you've done any active work to challenge it.</p>
    <p><strong>Mind reading</strong> — assuming you know what others are thinking about you ("they think I'm boring") without any actual evidence, when in reality you have no direct access to another person's thoughts at all.</p>
    <p><strong>Fortune telling</strong> — confidently predicting a negative outcome before a situation has even happened ("this is going to be awkward," "I'll have nothing to say"), treating the prediction as fact rather than as one anxious guess among many possible outcomes.</p>
    <p><strong>Catastrophising</strong> — jumping straight to the worst-case interpretation of a fairly minor social stumble (a pause, an awkward joke, a forgotten name) and treating it as a much bigger deal than it would actually register as to anyone else.</p>
    <p><strong>Discounting the positive</strong> — noticing and remembering the one slightly awkward moment in an otherwise fine interaction, while barely registering everything that went normally or well.</p>
    <p><strong>Emotional reasoning</strong> — treating the intensity of the anxious feeling itself as evidence that something is actually wrong ("I feel this anxious, so something bad must be happening"), when feeling anxious and something actually being wrong are two entirely separate things.</p>

    <h2>Why naming the distortion matters</h2>
    <p>It's easy to underestimate how much simply identifying a distortion accurately can do on its own. When an anxious thought is experienced as an undifferentiated wave of "this is bad," it feels like an unquestionable fact. When the same thought is identified specifically as "that's mind reading — I don't actually have evidence for what they're thinking," it becomes something you can examine and question, rather than something you're simply swept along by. This shift — from an unexamined feeling to a nameable, examinable thought — is the entire mechanism behind the rethinking technique covered in the next lesson.</p>

    <h2>Building your own distortion vocabulary</h2>
    <p>Over the coming week, the goal isn't to eliminate these thoughts — that's not realistic, and trying to suppress a thought directly tends to backfire and make it more persistent, not less. The goal is simply to get better at noticing and naming them as they happen, treating it almost like a specific noticing practice rather than a fight against the thoughts themselves. Most people find that a small handful of distortions account for the large majority of their own anxious thinking, once they start paying attention — you'll likely notice your own repeating pattern within just a few days of paying attention.</p>

    <h2>You'll likely find one or two dominant patterns</h2>
    <p>Most people, once they start tracking this deliberately, find that one or two of the five distortions above account for the clear majority of their anxious social thinking, rather than all five showing up with equal frequency. Someone might find mind reading is their dominant pattern, showing up in almost every social prediction, while catastrophising rarely features. Someone else might find the reverse. Identifying your own personal dominant pattern is genuinely useful, because it means the rethinking work in the next lesson can focus disproportionately on your actual most-used distortion, rather than treating all five as equally relevant to your specific situation.</p>
    <p>It's also common for the dominant pattern to shift somewhat depending on the type of situation — mind reading might dominate in one-on-one conversations, while fortune telling dominates before group events. Noting this kind of variation, rather than assuming a single uniform pattern across every context, will make the rethinking work considerably more precise and effective.</p>

    <h2>These distortions aren't unique to social anxiety</h2>
    <p>It's worth knowing that all five of these distortions show up broadly across many kinds of anxiety and low mood, not just social anxiety specifically — they're general patterns of unhelpful thinking that CBT addresses across a wide range of difficulties. Recognising them here, in the specific context of social situations, is a skill that tends to generalise usefully to other areas of life too, since the same distorted patterns often show up in worry about work, health, or other concerns in a similar form.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Over the next few days, whenever you notice social anxiety spike, pause and ask: what exact thought just went through my mind? Write it down, then match it to one of the five distortions above if it fits. Don't try to challenge it yet — for now, just build the habit of catching and naming it.</p>
    </div>

    <p>The next lesson gives you the actual technique for working with these thoughts once you've caught them — evidence-based ways to challenge anxious predictions rather than simply accepting them as fact.</p>
    """,
})

LESSONS.append({
    "lesson_num": 5, "module_num": 2, "module_title": "Rewriting the Story",
    "lesson_title": "Realistic Rethinking",
    "lesson_sub": "Evidence-based techniques for challenging anxious predictions",
    "tool": None,
    "body": """
    <p>Now that you can identify your own automatic thoughts and the distortions behind them, this lesson gives you the actual technique for working with them: realistic rethinking, the core CBT skill for loosening the grip of anxious predictions. It's worth being precise about what this technique is and isn't — it's not about forcing yourself into blind positivity or pretending everything will definitely go well. It's about examining an anxious prediction with the same rigour you'd apply to any other claim, rather than accepting it automatically just because it feels true.</p>

    <h2>The core technique: examining the evidence</h2>
    <p>For any specific anxious prediction — the kind you started collecting in Lesson 1's exercise and Lesson 4's noticing practice — the rethinking process asks a consistent set of questions:</p>
    <ul>
      <li><strong>What's the actual evidence for this prediction?</strong> Not how strongly it feels true, but what concrete evidence actually supports it.</li>
      <li><strong>What's the evidence against it?</strong> Times this exact feared outcome didn't happen, even in similar situations; other explanations for whatever evidence you did have.</li>
      <li><strong>What would I tell a friend who had this exact thought?</strong> Most people are far more balanced and generous when evaluating someone else's anxious thought than their own — this question borrows that outside perspective.</li>
      <li><strong>What's a more realistic, balanced version of this prediction?</strong> Not a falsely positive one — a version that actually fits the evidence you've gathered.</li>
    </ul>
    <p>Running through these questions, ideally in writing at first, turns an anxious prediction from something you're simply swept along by into something you actively evaluate — which is where its power to drive avoidance genuinely starts to weaken.</p>

    <h2>A worked example</h2>
    <p>Take a common anxious prediction: "if I say something in this meeting, everyone will think it's a stupid idea." Evidence for: maybe one time, months ago, a comment landed awkwardly. Evidence against: most comments people make in meetings, including plenty of imperfect ones, get a neutral or mildly positive response and are quickly forgotten; you can likely think of several times you or others said something in a meeting that wasn't remarkable and nothing negative happened at all. What you'd tell a friend: "one awkward comment months ago doesn't mean this one will go the same way — most comments just land as ordinary." A more realistic version: "there's a chance this specific comment doesn't land perfectly, but the far more likely outcome is that it's simply received as an ordinary contribution, and even an imperfect comment is very unlikely to be remembered as sharply as it feels right now."</p>
    <p>Notice that the realistic version isn't a guarantee of a good outcome — it still acknowledges some real uncertainty. That's intentional. Rethinking isn't about achieving false certainty that everything will go well; it's about replacing a distorted, worst-case certainty with an accurate, more balanced uncertainty, which is a much easier thing to act despite.</p>

    <h2>Why this needs practice to feel natural</h2>
    <p>This process will likely feel effortful and a bit mechanical at first — that's completely normal, and it doesn't mean it's not working. The automatic anxious thought has had years of repetition behind it; the rethinking process is brand new and hasn't had any repetition yet. With consistent practice, this kind of evidence-checking gradually becomes faster and more automatic itself, eventually running almost as quickly as the anxious prediction it's meant to counter — but that only happens through repeated use, not through understanding the technique intellectually on its own.</p>

    <h2>Rethinking is not the same as reassurance</h2>
    <p>It's worth distinguishing this technique clearly from simply seeking reassurance from other people ("do you think that went okay?") which can feel similar in the moment but tends to work quite differently over time. Reassurance-seeking often provides temporary relief without building any lasting skill — it depends on someone else's input each time, and can subtly reinforce the belief that you can't trust your own evaluation of a situation. Rethinking, done as a genuine skill you practise yourself, builds your own internal capacity to evaluate anxious predictions accurately, which is durable in a way that repeatedly asking others for reassurance isn't.</p>
    <p>This distinction matters practically: if you notice yourself wanting to ask someone else whether an interaction went fine, try running your own rethinking process first, in writing, before seeking outside input. Over time, this builds genuine confidence in your own judgment rather than a dependence on others to regulate your anxiety for you.</p>

    <h2>Doing this in the moment vs. afterward</h2>
    <p>When you're first learning this technique, doing it in writing after the fact — as in this lesson's exercise — is considerably more effective than trying to do it in real time during an anxious moment, since writing forces a slower, more deliberate pace than a live conversation allows. With enough repeated practice, an abbreviated version of this process can eventually run quickly enough to use in the moment itself, but that's a later-stage skill, not something to expect or demand of yourself immediately. Build the skill on paper first.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Take the anxious prediction you wrote down back in Lesson 1, and run it through the four questions above in writing. Notice, specifically, whether the realistic version feels meaningfully different to sit with than the original — even a small shift is a genuine, useful result at this stage.</p>
    </div>

    <p>The next lesson looks closely at two of the most common and specific distortions in social anxiety — the spotlight effect and its close relatives — because they're worth understanding in real depth given how central they are to most people's experience of social fear.</p>
    """,
})

LESSONS.append({
    "lesson_num": 6, "module_num": 2, "module_title": "Rewriting the Story",
    "lesson_title": "The Spotlight Effect & Other Traps",
    "lesson_sub": "Why others notice and judge you far less than you think",
    "tool": None,
    "body": """
    <p>Of all the distortions covered in Lesson 4, one shows up so consistently in social anxiety that it deserves its own dedicated lesson: the spotlight effect, the well-documented tendency to significantly overestimate how much other people notice and evaluate us. Understanding this one pattern in depth tends to do a disproportionate amount of work in loosening social anxiety's grip, because it sits underneath so many other specific fears.</p>

    <h2>What the spotlight effect actually is</h2>
    <p>The spotlight effect describes a consistent, well-replicated finding in social psychology: people systematically believe they're being watched, noticed, and evaluated far more closely by others than they actually are. This happens because each of us is, quite naturally, the centre of our own experience — we're intensely aware of our own anxiety, our own stumbles, our own perceived flaws — and that intense self-awareness gets mistakenly projected outward, as though everyone else must be noticing us just as closely as we're noticing ourselves. In reality, most people are just as absorbed in their own experience, their own self-consciousness, their own concerns, and have far less spare attention for closely monitoring you than it feels like from the inside of your own head.</p>
    <p>Classic experiments on this effect are worth knowing about directly: in one well-known study, participants wore a moderately embarrassing t-shirt into a room of strangers and estimated that roughly half the room would remember it. The actual number who noticed and later recalled it was far lower — usually less than half of what participants predicted. This gap between predicted and actual notice-taking is the spotlight effect in action, and it applies just as much to a stumbled sentence, a moment of visible nervousness, or an awkward pause as it does to a t-shirt.</p>

    <h2>Related traps worth naming specifically</h2>
    <p><strong>The illusion of transparency</strong> — the related belief that your internal anxious state is more visible to others than it actually is. Feeling intensely anxious internally does not mean it's showing on your face or in your voice nearly as clearly as it feels from the inside; internal and external experience of anxiety are far less correlated than anxious people typically assume.</p>
    <p><strong>The negativity bias in memory</strong> — even on the rare occasion someone does notice a genuine social stumble, they typically don't dwell on it or judge it nearly as harshly or for nearly as long as the anxious person imagines. Most people are quick to move past minor social imperfections in others, in large part because they're preoccupied with their own.</p>
    <p><strong>Assumed uniqueness of your anxiety</strong> — many socially anxious people believe their level of nervousness is unusually visible or unusual compared to everyone else in the room, when in reality a significant portion of any given room is managing some degree of their own social self-consciousness, largely invisible to everyone else for the same reasons yours is.</p>

    <h2>Using this practically, not just intellectually</h2>
    <p>Knowing about the spotlight effect intellectually is a start, but it tends to become genuinely useful only once you start actively applying it in the moment — specifically, noticing when a spotlight-effect thought shows up ("everyone's going to notice I'm nervous") and running it through the rethinking process from Lesson 5: what's the actual evidence that people are watching this closely, versus absorbed in their own experience? What would I actually remember about a stranger's minor stumble a week later, if I'm honest?</p>

    <h2>Why this effect persists even after you know about it</h2>
    <p>It's worth being honest that simply knowing about the spotlight effect intellectually rarely eliminates it entirely on its own — this is true of most cognitive biases, which tend to operate automatically regardless of conscious knowledge about them. The value of understanding it isn't that the knowledge alone fixes the pattern; it's that it gives you a specific, nameable thing to check for and challenge in the moment, using the rethinking process from Lesson 5, rather than being swept along by an unexamined feeling of certainty that everyone is watching and judging closely.</p>
    <p>Over repeated practice — noticing the spotlight-effect thought, naming it specifically, and running it through the evidence-checking process — most people find its grip does genuinely loosen over time, not because the bias disappears entirely, but because the automatic belief in it weakens with enough repeated disconfirming evidence, exactly the same mechanism covered for exposure in the next module.</p>

    <h2>A useful mental shortcut</h2>
    <p>Many people find it helpful to keep a simple, memorable phrase in mind for moments the spotlight effect shows up strongly: "they're thinking about themselves, not me" — a rough, quick version of the fuller evidence-checking process, useful specifically for in-the-moment situations where a full written analysis isn't practical. It's not a substitute for the deeper rethinking work, but as a quick redirect in the middle of a live interaction, it can meaningfully take the edge off in the moment itself.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Think back to the last time you were mildly embarrassed by something in a social setting. Now try to recall: can you name a specific instance of someone else visibly stumbling — a slip of the tongue, an awkward pause — in a social setting you were part of recently? For most people, this is surprisingly hard to recall in detail, which is itself direct evidence of how little these moments actually stick with observers.</p>
    </div>

    <p>You've now built the full cognitive toolkit: understanding the fear-avoidance cycle, catching automatic thoughts, rethinking them realistically, and specifically countering the spotlight effect. Module 3 puts all of this into action — structured, graded exposure to the situations you mapped back in Lesson 2.</p>
    """,
})

LESSONS.append({
    "lesson_num": 7, "module_num": 3, "module_title": "Graded Exposure",
    "lesson_title": "The Exposure Ladder",
    "lesson_sub": "How to design a step-by-step anxiety hierarchy for your specific fears",
    "tool": None,
    "body": """
    <p>Understanding the fear-avoidance cycle and rethinking anxious predictions both weaken social anxiety's grip — but the step that actually breaks the cycle directly is exposure: deliberately, repeatedly facing the situations you'd normally avoid, structured carefully enough that it builds confidence rather than reinforcing the fear. This lesson is about building your personal exposure ladder — a graded sequence from least to most anxiety-provoking — using the trigger map you built back in Lesson 2.</p>

    <h2>Why exposure works</h2>
    <p>Recall from Lesson 1 that avoidance keeps the fear-avoidance cycle running by preventing you from ever discovering that the feared outcome usually doesn't happen. Exposure directly interrupts this: by actually entering a feared situation and staying in it without your usual safety behaviours, you give yourself the chance to gather real evidence — evidence that the anxious prediction was wrong, or at least far less catastrophic than predicted, and evidence that the anxiety itself, while uncomfortable, is tolerable and does eventually settle rather than spiralling indefinitely. This new evidence, repeated enough times, is what actually retrains the automatic prediction at its source — far more effectively than reasoning about it alone, though the rethinking skills from Module 2 make the exposures considerably easier to tolerate along the way.</p>

    <h2>Why grading it matters</h2>
    <p>Jumping straight to your most feared situation rarely works well — it's more likely to produce an overwhelming experience that reinforces the very avoidance you're trying to break, precisely because an experience that's too intense tends to get remembered as confirmation of danger rather than as useful new evidence. A graded ladder — starting with situations that produce manageable, moderate anxiety and working systematically upward — lets you build a track record of success at each level before moving to the next, so that by the time you reach the harder items, you're carrying real, earned confidence rather than facing them cold.</p>

    <h2>Building your ladder</h2>
    <p>Using your Lesson 2 trigger map, list out as many specific situations as you can — aim for at least eight to ten — that touch on your core social fears, at a range of difficulty levels. For each one, rate the anxiety you'd expect on a simple 0–10 scale. A useful ladder typically spans the full range:</p>
    <ul>
      <li><strong>Low rungs (2–4):</strong> small, low-stakes exposures — making brief small talk with a cashier, asking a stranger for the time, sending a text you've been putting off.</li>
      <li><strong>Middle rungs (5–7):</strong> moderate exposures — attending a group event for a set amount of time, initiating a conversation with someone you don't know well, sharing an opinion in a small group setting.</li>
      <li><strong>Top rungs (8–10):</strong> your core, most-avoided situations — the ones from your original trigger map that carry the most weight, whatever those specifically are for you.</li>
    </ul>
    <p>Order the full list from lowest to highest anxiety rating. That ordered list is your ladder, and it's the working material for the rest of this module and much of what follows.</p>

    <h2>A few design principles</h2>
    <p><strong>Specificity matters.</strong> "Be more social" isn't a usable exposure item; "say hello to one coworker I don't usually talk to" is. Vague items are hard to actually complete and hard to judge success on.</p>
    <p><strong>Repeatability matters.</strong> Favour items you can do more than once, since repetition at each rung is what builds the confidence needed to move up — a single successful attempt is a good start, but several successful attempts at the same rung produce far more durable change.</p>
    <p><strong>No safety behaviours during exposure.</strong> An exposure item completed while still rehearsing exit lines or avoiding eye contact doesn't fully interrupt the cycle — the point is to face the situation directly enough that you actually gather evidence, not to find a way to endure it while still protecting yourself.</p>

    <h2>What to do if you're unsure how to rate something</h2>
    <p>It's common to feel uncertain about exactly where a situation belongs on the 0–10 scale, especially for items you've been avoiding for so long that you don't have recent direct experience to calibrate against. In that case, a reasonable approach is to estimate based on how you'd expect to feel walking up to the situation right now, in this moment, rather than trying to predict the whole interaction from start to finish — the anticipatory anxiety right before an exposure is usually the most intense point anyway, and a reasonable proxy for the overall difficulty rating.</p>
    <p>It's also fine, and expected, for your ratings to turn out somewhat inaccurate once you actually start attempting items — you might find a 6 was really more like a 4, or the reverse. This is useful information in itself, not a sign you did the ladder-building step wrong; simply adjust the rating and, if needed, the ordering, once you have real experience to draw on.</p>

    <h2>Your ladder is a living document</h2>
    <p>Expect to revise this ladder as you go — adding items you hadn't initially thought of, splitting an item that turns out to be harder than expected into smaller intermediate steps, or removing something once it stops producing meaningful anxiety at all. Treat the version you build now as a solid, genuinely useful starting draft rather than a fixed, final document; the ladder's value comes from actually using it and adjusting based on real experience, not from getting the initial version perfectly calibrated.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Build your own ladder now: at least eight items, rated 0–10, ordered from easiest to hardest, using your Lesson 2 trigger map as raw material. Keep it somewhere you'll return to regularly — this ladder is the backbone of the next two lessons and much of the rest of the course.</p>
    </div>

    <p>The next lesson turns your ladder into action — how to actually run your first experiments, starting at the bottom rungs, in a way that maximises what you learn from each one.</p>
    """,
})

LESSONS.append({
    "lesson_num": 8, "module_num": 3, "module_title": "Graded Exposure",
    "lesson_title": "Your First Experiments",
    "lesson_sub": "Low-stakes structured experiments to prove your predictions wrong",
    "tool": None,
    "body": """
    <p>With your ladder built, this lesson is about actually running your first exposures — treating each one as a genuine experiment rather than simply an ordeal to survive. Framing them this way matters more than it might seem: an experiment is something you run to find something out, with genuine curiosity about the result, while an ordeal is just something to endure and escape as fast as possible. The experimental framing is what turns exposure into something that actually builds new evidence, rather than just repeating the same anxious experience without learning anything new from it.</p>

    <h2>Structuring an exposure as a real experiment</h2>
    <p>Before attempting an item from your ladder, it's worth writing down three things, briefly:</p>
    <ul>
      <li><strong>The specific prediction</strong> — what exactly do you expect to happen, in concrete terms (not just "it'll go badly," but specifically what "badly" would look like)?</li>
      <li><strong>Your predicted anxiety peak</strong> — on the same 0–10 scale, how anxious do you expect to feel at the worst moment?</li>
      <li><strong>What would count as disconfirming evidence</strong> — what would actually need to happen for you to conclude your prediction was wrong, or significantly overestimated?</li>
    </ul>
    <p>After the exposure, compare what actually happened against all three. Nearly everyone finds a meaningful gap between the prediction and the reality — the feared outcome usually doesn't happen, or happens in a much milder form than predicted, and the anxiety, while genuinely uncomfortable, usually peaks lower and settles faster than expected. This comparison, done explicitly and in writing rather than left as a vague impression, is what actually produces the belief change — it's much harder for an anxious mind to dismiss a written, specific gap between prediction and outcome than a general feeling that "it wasn't that bad."</p>

    <h2>Start at the bottom, genuinely</h2>
    <p>There's often a temptation to skip the lower rungs because they feel almost too easy to bother with, or to jump ahead to a higher rung out of impatience to make faster progress. Resist this. The lower rungs aren't just warm-ups to get through quickly — they're where you build the specific skill of running the experiment structure itself (predicting, attempting, comparing) while the stakes are genuinely low, so that by the time you reach the harder items, the process feels familiar rather than being new territory on top of an already difficult exposure.</p>

    <h2>Handling a rough exposure</h2>
    <p>Not every exposure will go smoothly, and it's worth being honest about that in advance rather than being caught off guard by it. If an exposure goes worse than expected — anxiety peaks higher than predicted, or something genuinely awkward happens — that's still useful data, not a sign the whole approach has failed. A single difficult exposure doesn't erase the value of the method; it's one data point in a series, and the appropriate response is usually to repeat the same or a similar rung again soon, rather than either giving up or jumping to a much easier item out of self-protection. Repetition after a rough exposure is often exactly what turns it from a discouraging one-off into a manageable, expected part of the process.</p>

    <h2>Frequency matters more than intensity</h2>
    <p>Frequent, moderate exposures reliably produce better results than occasional, intense ones. Aim for several exposures a week rather than one big attempt followed by a long gap — momentum matters here in much the same way it matters for building any new social pattern, and long gaps between exposures tend to let some of the anxious prediction creep back in before the next attempt.</p>

    <h2>What if the exposure goes better than expected?</h2>
    <p>It's worth explicitly preparing for this outcome too, since it's actually the most common one and yet the easiest to discount. When an exposure goes noticeably better than predicted, there's a common anxious tendency to explain it away rather than let it count as real evidence — "that only went fine because it was a low-stakes situation," "I just got lucky that time," "that doesn't really prove anything." Catch this specific pattern if it shows up; it's a distortion in its own right (discounting the positive, from Lesson 4), and letting it run unchecked can quietly prevent the exposure work from producing the belief change it's actually capable of, even while you're doing everything else right.</p>
    <p>The corrective is the same explicit comparison from earlier in this lesson: write down what you predicted, write down what actually happened, and let the gap register as real, valid evidence rather than something to be explained away. Over enough repetitions, this consistent gap between prediction and outcome is what does the actual work of retraining the underlying belief.</p>

    <h2>You don't need to feel calm to run a successful exposure</h2>
    <p>A common misconception is that an exposure "worked" only if the anxiety was manageable or mild throughout. In reality, a genuinely successful exposure can involve significant, uncomfortable anxiety the entire way through — what matters for the underlying learning is that you stayed in the situation without relying on your usual safety behaviours, and that you gathered real evidence about the actual outcome, not that you felt comfortable doing it. Expecting comfort as the marker of success sets an unrealistic bar; expecting genuine, if uncomfortable, engagement with the situation is the more accurate and more achievable standard.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Pick the lowest item on your ladder and run it as a full experiment this week: write your prediction, your predicted anxiety peak, and what would count as disconfirming evidence beforehand. Afterward, write down what actually happened and compare it honestly to your prediction.</p>
    </div>

    <p>The next lesson addresses something that trips up a lot of people doing this work: how to interpret what happened afterward without falling into the same anxious distortions from Module 2 during the post-event replay.</p>
    """,
})

LESSONS.append({
    "lesson_num": 9, "module_num": 3, "module_title": "Graded Exposure",
    "lesson_title": "Processing Outcomes",
    "lesson_sub": "How to interpret social interactions without the anxious post-mortem",
    "tool": None,
    "body": """
    <p>Recall from Lesson 2 that post-event processing — the anxious mental replay after a social interaction — is one of the three components that keeps the fear-avoidance cycle running, often just as powerfully as full avoidance or safety behaviours, even though it happens entirely after the fact and is invisible to anyone else. This lesson is about interrupting that replay specifically, since it can otherwise quietly undo a lot of the genuine progress an exposure just made.</p>

    <h2>What the anxious post-mortem actually does</h2>
    <p>After a social interaction, an anxious mind often runs an automatic, distorted review: scanning for anything that might have gone wrong, replaying any awkward moment repeatedly, and interpreting ambiguous responses (a shorter reply than expected, a pause, a neutral expression) in the worst possible light. This process typically applies the exact same distortions covered in Module 2 — mind reading, catastrophising, discounting the positive — but does so retroactively, which makes it feel like an objective review of what happened rather than another round of the same distorted thinking. The effect is that even a genuinely successful exposure can get quietly reframed, hours later, into evidence that things went badly, simply through this replay process.</p>

    <h2>The specific mechanics of the replay trap</h2>
    <p>The post-mortem tends to focus disproportionately on any single imperfect moment — a stumbled word, a pause, a joke that didn't quite land — while barely registering everything that went normally or well. This is the discounting-the-positive distortion from Lesson 4 operating at full strength, precisely because it has unlimited time and no real-time social pressure to interrupt it; alone with your thoughts afterward, there's nothing stopping the anxious mind from returning to that one moment over and over, magnifying it each time, until it dominates your memory of the entire interaction far more than it dominated the interaction itself.</p>

    <h2>A structured alternative to the replay</h2>
    <p>Rather than letting the review happen automatically and uncontrolled, it helps to run a deliberate, structured version instead — closely tied to the experiment structure from Lesson 8:</p>
    <ul>
      <li><strong>What actually happened, factually</strong> — described the way a neutral observer would describe it, not the way your anxious narration frames it.</li>
      <li><strong>Compare to your prediction</strong> — go back to what you actually predicted beforehand and check the honest gap, the same comparison from Lesson 8.</li>
      <li><strong>What went fine or well</strong> — deliberately list this, since it won't surface on its own; the anxious mind doesn't spontaneously catalogue what went right.</li>
      <li><strong>One thing to adjust next time, if anything</strong> — genuinely useful feedback, if there is any, framed as calibration for next time rather than as evidence of failure.</li>
    </ul>
    <p>Doing this once, briefly, in writing, tends to be far more useful — and far less costly — than the unstructured, repeated mental replay it's meant to replace. It gives you the genuinely useful part of reflection (learning, calibration) without the distorted, repetitive part that just reinforces anxiety.</p>

    <h2>Setting a time limit on reflection</h2>
    <p>It's worth giving yourself an explicit, fairly short window for this structured review — ten minutes, once, shortly after the event — and treating anything beyond that as the replay trap reasserting itself rather than useful further reflection. If you notice yourself returning to the same interaction hours or days later, that's a good cue to consciously redirect: you've already done the useful review; anything further is the anxious cycle, not genuine learning.</p>

    <h2>Involving someone else in the check, sparingly</h2>
    <p>Occasionally, checking your factual account of an interaction against someone else's perspective — a trusted friend who was present, or simply someone you describe the situation to afterward — can help illustrate just how different the neutral, factual version sounds compared to your anxious internal narration. Use this sparingly rather than as a routine habit, though, to avoid drifting into the reassurance-seeking pattern discussed in Lesson 5; the goal is to build your own accurate internal reviewing process over time, with occasional outside perspective as a useful calibration check, not a dependency.</p>

    <h2>Why this skill compounds over the rest of the course</h2>
    <p>This processing skill becomes increasingly important as you move through more exposures in the coming weeks — each individual exposure is only as useful as the evidence you actually let yourself register from it, and an uncorrected anxious replay can quietly erode that evidence after the fact, even when the exposure itself went reasonably well in real time. Getting this skill solid now means every subsequent exposure in this course builds cleaner, more durable evidence against your anxious predictions.</p>

    <h2>What to do with a genuinely awkward moment</h2>
    <p>Sometimes the factual review does turn up a real, objectively awkward moment — everyone has these occasionally, anxious or not. When that happens, the goal isn't to pretend it wasn't awkward; it's to size it accurately rather than let it expand to dominate your memory of the whole interaction. A genuinely awkward ten-second moment in an otherwise ordinary twenty-minute conversation is a small, forgettable part of that conversation to anyone else present — worth acknowledging honestly, then filing away in proportion to how much space it actually occupied in the interaction, not the outsized space anxious memory tends to give it.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>After your next exposure or any social interaction that would normally trigger a replay, run the four-part structured review above within an hour of the event, in writing, and then deliberately set it aside. Notice whether doing this once, on purpose, reduces the pull toward revisiting it later.</p>
    </div>

    <p>You now have the complete exposure toolkit: building a ladder, running structured experiments, and processing outcomes without the anxious replay. Module 4 turns to a different but related area — the actual social skills that make conversations and interactions go more smoothly once the anxiety itself is less in the driver's seat.</p>
    """,
})

LESSONS.append({
    "lesson_num": 10, "module_num": 4, "module_title": "Social Skills That Stick",
    "lesson_title": "Conversation Fundamentals",
    "lesson_sub": "How conversations actually work and where anxious people misunderstand them",
    "tool": None,
    "body": """
    <p>With the cognitive and exposure work underway, this module turns to something practical: the actual mechanics of conversation. Social anxiety often comes bundled with specific misconceptions about what makes a conversation go well, and correcting those misconceptions directly tends to reduce anxiety on its own — a lot of conversational dread comes from believing the bar for "going well" is much higher and much harder to hit than it actually is.</p>

    <h2>The performance myth</h2>
    <p>A common belief underneath a lot of conversational anxiety is that a good conversation requires being interesting, witty, or impressive — that you're being evaluated on some kind of performance, and falling short of that bar means the interaction failed. This belief significantly overstates what other people are actually looking for. Most people, most of the time, aren't seeking a performance from a conversation partner; they're seeking to feel heard, to have an easy back-and-forth, and to enjoy a reasonably pleasant few minutes. Genuine warmth and attentiveness reliably matter more to how a conversation is remembered than cleverness does — which is good news, because warmth and attentiveness are far more learnable and far less anxiety-provoking to aim for than being consistently witty.</p>

    <h2>Conversation is a shared responsibility</h2>
    <p>Anxious conversational thinking often puts the entire burden of a good conversation on yourself — as though you alone are responsible for keeping it going, filling silences, and making it interesting. In reality, conversation is inherently a joint activity: the other person is equally responsible for their side of it, equally capable of asking a question, offering a comment, or steering the topic somewhere new. Recognising this explicitly tends to relieve a significant amount of pressure — you don't need to carry the whole interaction, because you were never actually supposed to be carrying it alone in the first place.</p>

    <h2>Silence is not automatically a failure</h2>
    <p>One of the most common anxious beliefs is that a pause in conversation is a sign something has gone wrong, and it needs to be filled immediately, at almost any cost. In reality, brief pauses are a completely normal part of natural conversation — a moment to think, a natural transition between topics, a comfortable lull between two people who aren't performing for each other. Conversations between people who know each other well are often full of comfortable silence; treating every pause as an emergency to be filled is actually a signal of anxiety, not a fix for it, and often produces the rushed, slightly frantic quality that anxious conversation can have.</p>

    <h2>What actually predicts a good conversation</h2>
    <p>Research on what makes conversations satisfying to both participants tends to converge on a small set of factors, none of which require the performance-level polish that anxious minds often assume is necessary: genuine curiosity about the other person, following up on what they actually say rather than moving through a mental script, a reasonable balance of talking and listening, and a friendly, warm tone more than clever content. None of these require eliminating anxiety first — they're behaviours you can practise directly, and doing so tends to reduce anxiety over time as evidence accumulates that conversations go fine without needing to be a performance.</p>

    <h2>Reframing the goal</h2>
    <p>Rather than aiming for "impressive" or "smooth," a more realistic and genuinely more effective goal for any given conversation is simply: was I reasonably present, reasonably curious, and reasonably kind. That's a bar nearly anyone can clear on an average day, anxious or not, and clearing it consistently is what actually builds real connection over time — not any single dazzling exchange.</p>

    <h2>Where the performance myth typically comes from</h2>
    <p>It's worth understanding why this belief takes hold so persistently for a lot of anxious people. It often traces back to a small number of specific memories — a joke that fell flat, a comment that got a lukewarm response, a comparison to someone who seemed effortlessly charismatic — that get generalised into a sweeping rule about what conversation requires. A handful of specific, sometimes years-old memories end up quietly running an entire ongoing belief system about social interaction, largely unexamined. Naming this origin explicitly can help loosen the belief's grip: it's not an accurate rule about how conversation actually works: it's an overgeneralisation from limited, often outdated evidence.</p>

    <h2>This lesson connects directly to your exposure work</h2>
    <p>Everything covered here is worth carrying directly into your Module 3 exposures. If your ladder includes conversational items, going into them with an accurate understanding of what actually makes a conversation go well — rather than the anxious performance-based standard — makes the exposure itself considerably more approachable, and makes it easier to accurately register success afterward using the Lesson 9 review process, since you're evaluating against a realistic bar rather than an unreasonably high one.</p>

    <h2>What genuine curiosity looks like in practice</h2>
    <p>Genuine curiosity is worth distinguishing from performed interest, since anxious minds often default to the latter — asking a question because it's expected, rather than because you're actually interested in the answer. The distinction shows in the follow-up: genuine curiosity naturally produces a follow-up question based on what someone actually said, while performed interest tends to move straight to your next planned question regardless of their answer. Practising the follow-the-thread habit — asking about whatever detail actually caught your attention in their response — is a reliable, low-effort way to build genuine curiosity as an active habit rather than something you either have naturally or don't.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>In your next conversation, deliberately let one silence sit for a couple of extra seconds rather than immediately rushing to fill it. Notice what actually happens — usually far less than the anxious prediction, and often the other person fills it just as naturally as you would have.</p>
    </div>

    <p>The next lesson gets specific about two moments that carry disproportionate anxiety for a lot of people: entering a conversation or group, and leaving one gracefully.</p>
    """,
})

LESSONS.append({
    "lesson_num": 11, "module_num": 4, "module_title": "Social Skills That Stick",
    "lesson_title": "Entering & Exiting Gracefully",
    "lesson_sub": "Strategies for joining groups and leaving without it being awkward",
    "tool": None,
    "body": """
    <p>Two specific moments carry a disproportionate share of social anxiety for a lot of people: the entrance (walking up to a group or starting a conversation) and the exit (leaving without it feeling abrupt or rude). Both feel high-stakes because they're transition points, visible and a bit exposed by nature — but both are also far more routine and far less scrutinised by others than anxious anticipation makes them feel. This lesson gives you concrete, practical approaches for both.</p>

    <h2>Entering a group</h2>
    <p>Joining an existing group conversation is a common trigger, largely because it feels like interrupting something already in motion. A few things make it noticeably easier:</p>
    <ul>
      <li><strong>Approach at a natural pause</strong> — right after a laugh, a topic shift, or a lull, rather than mid-sentence. This isn't about finding a perfect moment (there's rarely one that feels fully "safe"), just a reasonably natural one.</li>
      <li><strong>You don't need an opening line prepared</strong> — simply standing nearby, making eye contact, and offering a small nonverbal acknowledgment (a nod, a smile) is often enough of an entry; most groups will naturally include someone who does this, without needing a scripted line.</li>
      <li><strong>Listen before contributing</strong> — give yourself permission to just take in the topic for a minute before saying anything. There's no rule requiring an immediate contribution the moment you join.</li>
      <li><strong>A simple, genuine question works better than a clever comment</strong> — "what are you all talking about?" or a direct follow-up question on the current topic is low-risk and almost always well received.</li>
    </ul>
    <p>It's worth directly naming the anxious prediction that usually accompanies this: that the group will notice the interruption and judge it. In reality, groups absorb new arrivals constantly and with far less scrutiny than it feels like from the anxious perspective of the person joining — this is the spotlight effect from Lesson 6, showing up again in a specific, common situation.</p>

    <h2>Exiting gracefully</h2>
    <p>Leaving a conversation or group carries its own anxious weight — a fear of seeming rude, of the exit being awkward, or of not having a good enough reason. A few reliable approaches:</p>
    <ul>
      <li><strong>A simple, warm close is enough</strong> — "it was great talking to you, I'm going to go say hi to a few other people" or "I should get going, but this was really nice" covers the vast majority of situations cleanly.</li>
      <li><strong>You don't need an elaborate justification</strong> — over-explaining an exit tends to draw more attention to it than a brief, confident one does. A short reason, or sometimes no explicit reason at all, is completely normal and accepted.</li>
      <li><strong>Physical cues help signal the transition</strong> — a small step back, glancing toward where you're headed, or standing up (if seated) all naturally cue that the conversation is winding down, which most people read easily without needing it stated outright.</li>
      <li><strong>It's fine to exit mid-lull</strong> — you don't need to wait for a natural high point in the conversation; a comfortable, ordinary moment is a perfectly fine time to close things out.</li>
    </ul>

    <h2>Both get easier with repetition</h2>
    <p>Like most of the skills in this course, entering and exiting feel far more effortful and high-stakes the first several times than they do after some repetition. This is a natural, direct application of the exposure principle from Module 3 — treat both as items on your ladder if they're not already there, and expect the anxiety around them to decrease noticeably with practice, the same way it does for any other exposure item.</p>

    <h2>Treating these as ladder items</h2>
    <p>If entering groups or exiting conversations rated fairly high on your original exposure ladder from Module 3, it's worth explicitly returning to that ladder now with these specific techniques in hand. Facing a high-anxiety item armed with a concrete approach, rather than facing it with nothing but the vague instruction to "just do it," tends to make a meaningful difference in how manageable it feels — the techniques in this lesson aren't a replacement for exposure, they're tools that make the exposure itself more approachable and more likely to go well.</p>
    <p>It's also worth noting that these two skills — entering and exiting — often generalise well once you've practised them a handful of times in one context. Confidence built entering a work event, for instance, tends to transfer at least partially to entering a social gathering outside of work, since the underlying mechanics (approaching at a natural pause, not needing an elaborate opener) are largely the same regardless of the specific setting.</p>

    <h2>What if you're not sure whether an exit felt abrupt?</h2>
    <p>A common lingering worry after an exit is uncertainty about whether it came across as abrupt or rude, even when it followed the guidance above. Here, the same rethinking process from Lesson 5 applies directly: what's the actual evidence it was abrupt, versus the anxious assumption? In most cases, a warm, brief close following ordinary social conventions registers to the other person as completely unremarkable — people generally aren't tracking the precise wording or timing of how a conversation ended nearly as closely as the anxious mind assumes.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>At your next opportunity, practise one deliberate entrance and one deliberate exit using the approaches above. Afterward, note whether either felt as high-stakes in reality as it did in anticipation — for most people, this gap is one of the more noticeable ones in the whole course.</p>
    </div>

    <p>Entering and exiting well gets you into and out of conversations smoothly — the next lesson addresses what happens between those two points across multiple interactions: turning a single good conversation into an actual ongoing relationship.</p>
    """,
})

LESSONS.append({
    "lesson_num": 12, "module_num": 4, "module_title": "Social Skills That Stick",
    "lesson_title": "The Art of Follow-Through",
    "lesson_sub": "How to move from single interaction to actual relationship",
    "tool": None,
    "body": """
    <p>A single good conversation, however well it goes, doesn't automatically become a relationship — that requires a deliberate next step, and this is often where social anxiety reasserts itself in a slightly different form: not fear of the interaction itself, but fear of the follow-up. This lesson addresses that specific transition directly, since it's a common place for otherwise real progress to stall out.</p>

    <h2>Why follow-through feels harder than the original conversation</h2>
    <p>The original conversation had some natural cover — a shared context (an event, a class, a mutual setting) that made the interaction feel low-stakes and easy to justify. A follow-up message, by contrast, is a more exposed, deliberate act: you're choosing to reach out with no built-in occasion, which can feel like it carries more of your own investment and therefore more risk of rejection. This is a real shift in the nature of the anxiety, not a sign you've regressed — it's simply a new, specific trigger worth recognising and working with directly, the same way you've worked with others throughout this course.</p>

    <h2>Common anxious predictions about following up</h2>
    <p>A few predictions show up especially often here, worth naming and rethinking specifically using the Module 2 technique: "they were probably just being polite and don't actually want to hear from me," "reaching out will seem overly eager or needy," "if they don't respond quickly, it means they don't want to talk to me." Each of these is worth running through the evidence-checking process from Lesson 5 directly — in nearly every case, the evidence for these predictions is thin (a general anxious sense, not any specific signal from the actual interaction), while the evidence against includes the interaction itself typically going fine, and the base rate of people being glad to hear from someone they had a decent conversation with being considerably higher than anxious prediction assumes.</p>

    <h2>Making the follow-up itself lower-stakes</h2>
    <p>A few practical approaches make this specific step easier to actually take:</p>
    <ul>
      <li><strong>Reference something specific</strong> — a message tied to something from the actual conversation ("hey, this is [name] from [context] — you mentioned that trail, would still love the name of it") feels much more natural and lower-stakes than a generic "hey, nice meeting you."</li>
      <li><strong>Keep the ask small</strong> — a low-pressure, easy-to-answer suggestion (coffee, a specific small plan) is easier to send and easier for the other person to say yes to than something more open-ended or ambiguous.</li>
      <li><strong>Send it reasonably soon</strong> — within a few days, while the interaction is still fresh for both of you, rather than waiting for a version of yourself with less anxiety about it, which often doesn't arrive on its own.</li>
      <li><strong>Treat the sending itself as the exposure</strong> — much like other items on your ladder, the anxiety peaks right before sending and tends to drop quickly afterward, regardless of the response.</li>
    </ul>

    <h2>Handling silence or a slow response</h2>
    <p>If a follow-up doesn't get an immediate or enthusiastic response, it's worth applying the same processing skills from Lesson 9 rather than letting an anxious post-mortem take over: what's the actual evidence about why, versus the anxious story filling in the gap? People are busy, distracted, or simply slow responders for reasons that usually have little to do with you. A single quiet or slow response is one data point, not a verdict — and, following the consistency principle relevant to any new relationship, it's often still worth a second, low-pressure attempt before drawing firm conclusions.</p>

    <h2>Follow-through applies to existing relationships too</h2>
    <p>Everything in this lesson applies just as directly to maintaining relationships you already have, not just new ones formed during your exposure work. Social anxiety often quietly erodes existing connections too — through delayed responses, declined invitations, or a general pulling back during a harder anxious stretch. If you notice an existing relationship has gone a bit quiet during your work through this course, the same principles apply: a specific, low-pressure reach-out, sent soon, treated as its own small exposure if it feels anxiety-provoking to send.</p>
    <p>It's worth explicitly checking, as you go through this course, whether any existing relationships have quietly thinned during a harder stretch of avoidance, and treating reconnecting with them as genuinely part of this work, not a separate task outside of it.</p>

    <h2>Follow-through as its own exposure ladder item</h2>
    <p>If sending follow-up messages consistently ranks as one of your harder items, consider explicitly adding a graded set of follow-through exposures to your Module 3 ladder — starting with lower-stakes versions (a brief message to someone you already know reasonably well) before building up to reaching out to someone from a single recent interaction. Treating this as its own deliberate progression, rather than a single high-stakes category, applies the same graded-exposure logic that's worked for other trigger types throughout this course.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>If there's a follow-up message you've been putting off, send it this week — specific, low-pressure, and soon. Beforehand, write down your anxious prediction about the response; afterward, compare what actually happened, the same experiment structure from Module 3.</p>
    </div>

    <p>You now have both halves of the social skills toolkit: the mechanics of a good conversation, and how to carry it forward into something ongoing. Module 5 turns back to something covered briefly in Lesson 3 — managing your energy and avoiding overwhelm as you keep applying everything you've learned so far.</p>
    """,
})

LESSONS.append({
    "lesson_num": 13, "module_num": 5, "module_title": "Managing Energy & Overwhelm",
    "lesson_title": "Reading Your Social Battery",
    "lesson_sub": "Learning to recognise your energy limits before they collapse",
    "tool": "Social Battery",
    "body": """
    <p>By this stage in the course, you're likely doing considerably more active socialising and exposure work than when you started — which is real progress, but it also means energy management, first introduced back in Lesson 3, matters more now than it did at the beginning. This lesson is about learning to read your own limits accurately and proactively, rather than discovering them only after you've already gone past them.</p>

    <h2>Why anxious socialising depletes faster</h2>
    <p>As covered in Lesson 3, anxious social interactions carry a second layer of cognitive effort — self-monitoring, threat-scanning, managing safety behaviours — on top of the ordinary effort any interaction requires. As you're doing more exposure work, you're likely spending more time in situations that still carry at least some of this extra load, even as the intensity of the anxiety itself decreases with each successful exposure. This means your energy expenditure doesn't necessarily drop as fast as your anxiety does, especially in the middle stretch of this process — a genuinely common and easy-to-miss pattern that can make it feel like you're "still struggling" even as the underlying anxiety is measurably improving.</p>

    <h2>The gap between capability and capacity</h2>
    <p>It's worth distinguishing clearly between what you're now capable of and how much of it you can sustainably do. The exposure work in Module 3 has likely expanded what situations you're capable of handling — genuinely difficult evidence to argue with. But being capable of handling a situation doesn't mean doing five of them in a row, back to back, all week, is sustainable or necessary. Progress in this course is measured by capability expanding, not by maximising volume; pushing volume past what your energy can sustain tends to produce exhaustion that can look, from the inside, disconcertingly similar to relapse, even when the underlying anxiety work is genuinely holding.</p>

    <h2>Learning your specific warning signs</h2>
    <p>Social depletion tends to show up through a specific, fairly recognisable set of signals, worth learning to notice early rather than only in hindsight:</p>
    <ul>
      <li>Conversation starting to feel effortful in a way it didn't earlier in the day or week</li>
      <li>Patience thinning — irritability with people or situations that wouldn't normally bother you</li>
      <li>A pull toward cancelling plans that you were previously looking forward to</li>
      <li>Anxiety symptoms that seem disproportionate to the specific situation, suggesting an already-depleted baseline rather than the situation itself being unusually hard</li>
      <li>A flat, going-through-the-motions quality to interactions that would normally feel more engaged</li>
    </ul>
    <p>These are worth treating as genuine data, not as a sign the exposure work has failed — noticing them accurately and responding by pacing appropriately is itself part of doing this work well, not a departure from it.</p>

    <h2>Building the check-in habit</h2>
    <p>Rather than waiting for an obvious crash, it helps to build a brief, regular check-in — a quick, honest read of your current energy before committing to another social plan or exposure attempt, similar in spirit to the check-ins from your original Module 1 baseline. This isn't about avoiding difficulty; it's about choosing difficulty deliberately, from a place of actually having the capacity for it, rather than pushing through depletion in a way that risks turning a genuinely valuable exposure into an overwhelming, poorly-timed one.</p>

    <h2>Use the Social Battery tool again, now with more data</h2>
    <p>Return to the Social Battery tool now that you have several weeks of real exposure and social-skills practice behind you. Your patterns have likely shifted since your Lesson 3 baseline — many people find their capacity for previously anxiety-heavy situations has genuinely grown, even while their overall energy limits remain real and worth respecting.</p>

    <h2>A common, confusing pattern worth naming</h2>
    <p>Many people going through this process notice something that initially seems contradictory: their anxiety in a given situation has genuinely decreased, yet they still feel tired afterward, sometimes even more tired than they expected given how much less anxious the situation felt. This isn't a sign the anxiety work isn't real — it typically reflects that you're now doing more, and staying in situations longer, than you would have during the avoidance-heavy period before this course. More total social exposure, even at lower anxiety per interaction, can still add up to more total energy expenditure across a week. Recognising this pattern for what it is — a sign of expanded activity, not failed progress — prevents it from being misread as a setback.</p>

    <h2>Energy management is a skill, not a character trait</h2>
    <p>It's worth framing this the same way the rest of the course frames anxiety itself: reading and managing your social energy accurately is a learnable skill, not a fixed trait you either have or don't. Some people naturally track this more intuitively than others, but everyone can get considerably better at it with deliberate attention, the same way everyone can get better at recognising and rethinking automatic thoughts with practice. Don't assume poor energy awareness now means it'll always be difficult to read — it's simply an area that, like the others in this course, responds well to consistent, deliberate practice.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Before your next planned exposure or social commitment, do a brief, honest energy check using the warning-signs list above. If two or more are present, it's a reasonable, non-defeatist choice to either scale the plan down or reschedule — not a step backward in your progress.</p>
    </div>

    <p>The next lesson goes further into recovery specifically — how to actually recharge effectively, so social exertion doesn't leave you depleted for days at a time.</p>
    """,
})

LESSONS.append({
    "lesson_num": 14, "module_num": 5, "module_title": "Managing Energy & Overwhelm",
    "lesson_title": "Recovery Rituals",
    "lesson_sub": "How to recharge effectively so social exertion doesn't deplete you for days",
    "tool": None,
    "body": """
    <p>Recognising depletion, covered in the last lesson, is only half of managing your energy well — the other half is actually recovering from it effectively, so that a demanding social stretch costs you a reasonable, bounded amount of time rather than bleeding into days of feeling flat and depleted. This lesson is about building genuinely effective recovery practices, since not everything that feels like rest actually functions as recovery.</p>

    <h2>Not all rest is equally restorative</h2>
    <p>It's a common and understandable mistake to assume that any downtime — scrolling a phone, half-watching something, lying on the couch without much intention — counts as recovery, simply because it isn't actively demanding. In practice, a lot of passive downtime doesn't actually restore social or cognitive capacity very effectively; it can leave you technically rested in terms of physical stillness while still cognitively depleted, particularly if the downtime itself involves low-grade social input (scrolling social media, for instance, is a surprisingly poor recovery activity for social depletion specifically, since it's still a form of social processing, just a passive and often comparison-heavy one).</p>

    <h2>What tends to actually restore social capacity</h2>
    <p>Genuinely restorative recovery tends to share a few features: minimal social processing demand, a sense of full permission to disengage (not multitasking or half-attending to something else), and some degree of active choice rather than passive drift. A few reliably effective options, though the specific mix that works best varies by person:</p>
    <ul>
      <li><strong>True solitude</strong> — time genuinely alone, without needing to perform or explain yourself to anyone, even briefly.</li>
      <li><strong>Physical movement</strong> — a walk, exercise, anything that shifts attention into the body rather than continued cognitive/social processing.</li>
      <li><strong>Low-effort contact with people who already know you well</strong> — time with someone where you don't need to manage self-presentation, which recharges for many people even though it's technically social.</li>
      <li><strong>Absorbing, non-social activities</strong> — reading, a hobby, anything that occupies attention fully enough to genuinely displace the anxious replay processes from Lesson 9.</li>
    </ul>
    <p>It's worth experimenting deliberately with which of these actually leave you feeling recharged versus which just pass the time — the two aren't always the same, and the difference is worth learning about your own specific patterns rather than assuming.</p>

    <h2>Building recovery in proactively, not reactively</h2>
    <p>The most effective approach treats recovery as scheduled maintenance, built into your week in advance, rather than something you scramble for only after you've already noticed depletion. If you know a particular day or stretch will involve significant social exertion — several exposures, a demanding event, a full day of socially effortful interaction — pairing it with deliberately protected recovery time afterward, decided in advance, tends to prevent the multi-day bleed-over that unmanaged depletion can otherwise produce.</p>

    <h2>Recovery isn't avoidance</h2>
    <p>It's worth being clear about an important distinction: deliberate, planned recovery time is not the same thing as the avoidance covered back in Module 1, even though both involve stepping back from social demand. Avoidance is driven by anxious prediction and prevents you from gathering disconfirming evidence; recovery is driven by an accurate read of genuine depletion, planned in service of sustaining the broader effort, not escaping it. The test is roughly this: are you stepping back because a specific situation feels threatening, or because you're genuinely, measurably depleted and need to recharge before continuing? The first is worth examining and often gently pushing through, per Module 3; the second is worth honouring.</p>

    <h2>Recovery needs vary by person, and that's fine</h2>
    <p>It's worth resisting the temptation to adopt someone else's recovery routine wholesale just because it's commonly recommended. What restores one person — a long solo walk, say — might not do much for someone whose most restorative activity is actually quiet time with a close friend. The genuinely useful approach is treating your own recovery preferences as worth investigating directly, through honest observation of what actually leaves you feeling recharged versus what just occupies time, rather than assuming a generic list applies equally to everyone.</p>
    <p>It also helps to notice that recovery needs can shift depending on the specific type of depletion. Recovering from an anxiety-heavy exposure might call for something different than recovering from simple social fatigue after a long, pleasant but tiring event. Paying attention to this distinction over time will sharpen your own personal recovery toolkit considerably.</p>

    <h2>Recovery and exposure work together, not against each other</h2>
    <p>It's worth being explicit that good recovery practice actively supports the exposure work from Module 3, rather than being a separate, unrelated concern. An exposure attempted from a well-recovered baseline tends to go better and produce cleaner, more convincing evidence than the same exposure attempted while already running on empty — where genuine depletion can make an ordinary level of anxiety feel more overwhelming than it would otherwise, muddying the useful comparison between prediction and outcome. Good recovery isn't separate from the anxiety work; it's part of what makes the anxiety work actually effective.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Identify your single most reliably restorative recovery activity from the list above, based on your own honest experience, and schedule it proactively after your next demanding social commitment — decided in advance, not left to chance.</p>
    </div>

    <p>The final lesson in this module brings recognition and recovery together into an overall sustainable pace — building a social rhythm that energises rather than exhausts you over the longer term.</p>
    """,
})

LESSONS.append({
    "lesson_num": 15, "module_num": 5, "module_title": "Managing Energy & Overwhelm",
    "lesson_title": "Setting the Right Pace",
    "lesson_sub": "Building a social life that energises rather than exhausts you",
    "tool": None,
    "body": """
    <p>This lesson closes out the energy management module by pulling recognition and recovery together into an overall sustainable rhythm — a pace of social engagement and exposure work that continues building your confidence without running you into the ground. Pace is worth thinking about deliberately, because both too little and too much carry real costs, in different ways.</p>

    <h2>The two failure modes of pacing</h2>
    <p><strong>Too slow.</strong> Under-pacing — doing exposure work only occasionally, with long gaps between attempts — tends to let some of the anxious prediction creep back in between exposures, slowing progress and sometimes making each new attempt feel almost like starting over. This often comes from an understandable but ultimately counterproductive instinct toward excessive caution, treating every exposure as something to recover fully from before considering another.</p>
    <p><strong>Too fast.</strong> Over-pacing — pushing through consistent depletion, taking on more exposures and social commitments than your actual energy can sustain — risks the kind of overwhelming experience discussed in Module 3, which can get remembered as confirming evidence for the anxiety rather than disconfirming it, effectively working against the very progress you're trying to build.</p>
    <p>The right pace sits between these: frequent enough that momentum builds and doesn't stall, but respectful enough of your actual energy capacity that each attempt has a genuine chance to go well rather than being undermined by exhaustion going in.</p>

    <h2>What sustainable pacing actually looks like</h2>
    <p>In practice, this usually means several moderate exposures or social commitments spread across a week, rather than either one isolated attempt or an overloaded schedule, with deliberate recovery time built in around the more demanding ones per the last lesson. It also means being willing to adjust week to week based on an honest energy check-in, rather than rigidly following a fixed schedule regardless of how you're actually doing — pacing is a living, adjustable thing, not a plan set once and never revisited.</p>

    <h2>Progress isn't linear, and pace shouldn't pretend it is</h2>
    <p>It's worth expecting your actual capacity to fluctuate — some weeks will have more available energy than others, for reasons that may have nothing to do with your anxiety work specifically (sleep, general life stress, physical health). A sustainable approach to pacing treats this as normal and expected, scaling activity up and down with actual capacity, rather than treating any week with reduced output as a failure or a step backward. The overall trend across months, not the variation week to week, is what actually matters for genuine progress.</p>

    <h2>A simple framework for weekly planning</h2>
    <p>At the start of each week, it's worth briefly answering three questions: what's my current energy baseline this week (using the warning-signs awareness from Lesson 13), what ladder items make sense to attempt given that baseline, and what recovery time needs to be protected around the more demanding ones. This doesn't need to be an elaborate process — a few minutes of honest planning tends to produce a noticeably more sustainable week than simply reacting to whatever comes up, without any deliberate pacing at all.</p>

    <h2>Pace will naturally shift as the course progresses</h2>
    <p>It's worth expecting your sustainable pace to change over the twelve weeks, not stay fixed from the start. Early on, even relatively small exposures may carry significant energy cost, given how much anxiety and unfamiliarity is involved. As situations move down your ladder from difficult to manageable to comfortable, the same activities generally become far less energy-intensive, which usually means your overall sustainable capacity for social contact increases over the course, not just your tolerance for any single situation. Tracking this shift explicitly — noticing that what used to require careful pacing now happens almost without thinking about it — is itself good evidence of genuine progress.</p>

    <h2>Pace is personal — resist comparing yours to anyone else's</h2>
    <p>It's worth explicitly warning against comparing your own pace to anyone else's, including other people's accounts of working through similar anxiety, or even an imagined "ideal" version of how fast this should go. Genuine, appropriate pace depends on your specific starting point, your specific triggers, your available time and energy, and factors entirely outside this course's control. A pace that looks slower on paper but is genuinely sustainable for you will produce better long-term results than a faster pace borrowed from someone else's circumstances and pushed through unsustainably.</p>

    <h2>Trust the process over any single week's results</h2>
    <p>Any individual week may look uneven relative to your plan — an exposure that went harder than expected, a recovery period that took longer than budgeted, an energy dip that forced a lighter week than intended. None of this, taken in isolation, indicates the overall approach isn't working. What matters far more than any single week is the trend across the full twelve weeks: are the same categories of situations, on the whole, requiring less deliberate pacing and producing less anxiety than they did a month or two earlier? That broader trend is the real signal worth tracking, not the noise of any individual week.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Using the three-question framework above, plan out this coming week: your current energy baseline, one or two specific ladder items that fit it, and where you'll protect recovery time. Revisit and adjust it partway through the week if your actual capacity turns out different from what you expected.</p>
    </div>

    <p>You now have the full picture of sustainable progress: recognising depletion, recovering from it effectively, and pacing your overall effort so it builds rather than burns you out. The final module looks at where you've come from, and how to sustain what you've built well beyond the end of this course.</p>
    """,
})

LESSONS.append({
    "lesson_num": 16, "module_num": 6, "module_title": "Your Confident Life",
    "lesson_title": "Your Loneliness Profile Revisited",
    "lesson_sub": "Measuring how your needs and patterns have shifted",
    "tool": "Loneliness Deep Dive",
    "body": """
    <p>You started this course by mapping your anxiety in detail back in Module 1. This lesson is a deliberate pause to look at how things have actually shifted since then — using a genuine tool-based comparison rather than relying purely on memory, which tends to underrate gradual change the same way it did for the relocation-focused course covered elsewhere on Humanly Labs.</p>

    <h2>Why gradual change is hard to feel</h2>
    <p>Anxiety reduction through consistent exposure work happens gradually, week by week, which makes it notoriously difficult to register in the moment — you're far more likely to notice today feeling similar to yesterday than to notice today compared clearly against week one. Without a deliberate comparison, it's easy to keep carrying an outdated internal sense of "I'm still that anxious person" well after the actual evidence, built through months of exposures, has meaningfully shifted.</p>

    <h2>Revisit your Module 1 material directly</h2>
    <p>Go back to your Lesson 1 exercise (the situation you avoided and what you predicted), your Lesson 2 trigger map, and your Lesson 7 exposure ladder. Read through them now, and answer honestly:</p>
    <ul>
      <li>Which items on your original trigger map or ladder no longer produce much anxiety at all?</li>
      <li>Which items have moved down significantly in intensity, even if they're not fully resolved?</li>
      <li>Are there items you'd now rate quite differently than your original 0–10 scores?</li>
      <li>How does your current use of safety behaviours and post-event processing compare to when you first identified them in Lesson 2?</li>
    </ul>
    <p>Be honest in both directions here — genuine progress deserves to be recognised clearly, and areas that are still difficult deserve to be named plainly rather than glossed over. Both are useful, and it would be inaccurate — not encouraging — to pretend everything has resolved if it hasn't.</p>

    <h2>Use the Loneliness Deep Dive as a fresh, structured measure</h2>
    <p>The Loneliness Deep Dive tool below runs a more thorough assessment of your current social needs and patterns than the initial Social Anxiety Check from Module 1 — useful now specifically because your relationship to social contact has likely shifted meaningfully over the course, not just in terms of anxiety intensity, but in terms of what kind of connection you actually want and pursue. Running it now gives you a genuine, structured snapshot to compare against where you started.</p>

    <h2>Progress rarely looks exactly like the original goal</h2>
    <p>It's worth naming directly: the version of "less anxious" you have now, twelve weeks in, likely doesn't look exactly like what you imagined when you started. Maybe a specific feared situation you focused on early is still genuinely hard, while a different one you barely thought about has become completely comfortable. Maybe the anxiety hasn't disappeared, but your relationship to it has changed — less avoidance, faster recovery, more willingness to act despite it. All of that counts as real, substantial progress, even when it doesn't match a tidy, imagined before-and-after.</p>

    <h2>If the comparison reveals uneven progress</h2>
    <p>It's genuinely common for progress to be uneven across your original trigger map — significant improvement in some areas, much more modest change in others. This doesn't indicate the course "didn't work" for the harder areas; some anxiety patterns are simply more deeply established than others and reasonably take longer than twelve weeks to shift substantially. If specific items remain quite difficult, that's useful, actionable information: those are exactly the items worth continuing to work on deliberately using the same tools, past the formal end of this course, rather than assuming the process has run its course simply because the structured lessons are ending.</p>

    <h2>Sharing your progress, if you want to</h2>
    <p>If you've told anyone close to you about working through this course, it can be genuinely worthwhile to share some of this comparison with them directly. People who've watched you avoid certain situations for a long time often notice change even before you fully register it yourself, and hearing an outside perspective can add useful confirmation to your own internal assessment. This isn't the reassurance-seeking pattern warned about in Lesson 5 — a one-time, genuine conversation about real progress is different from a repeated, anxious need for validation after each interaction.</p>

    <h2>What to do with this measurement going forward</h2>
    <p>Beyond the immediate comparison, this fresh assessment is worth treating as a new baseline in its own right — something to compare against again in a few months, the same way your Module 1 baseline served this comparison. Anxiety and social needs both continue to shift with life circumstances well beyond the end of this course, and having a periodic, structured measurement rather than relying purely on memory keeps your sense of your own progress grounded in something more reliable than how any single recent week happened to feel.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Write a short, honest comparison between your Lesson 1 and Lesson 2 material and where things stand now — specific situations, specific ratings, not just a general sense of "better." Keep it. It's genuinely useful evidence to revisit on a future harder week.</p>
    </div>

    <p>The final two lessons look forward — how to sustain this progress for the long term, and how to build an ongoing social life shaped around your actual personality rather than around managing anxiety.</p>
    """,
})

LESSONS.append({
    "lesson_num": 17, "module_num": 6, "module_title": "Your Confident Life",
    "lesson_title": "Maintaining Progress",
    "lesson_sub": "How to sustain gains and handle setbacks without spiralling",
    "tool": None,
    "body": """
    <p>The structured part of this course is ending soon, but the underlying skills — cognitive rethinking, graded exposure, energy management — don't stop being relevant once the twelve weeks are over. This lesson is about what to actively carry forward, and specifically how to handle the inevitable difficult moments ahead without letting a single setback undo months of genuine progress.</p>

    <h2>Setbacks are normal, not evidence of relapse</h2>
    <p>It's worth setting this expectation clearly and directly: even after real, substantial progress, there will be future moments where anxiety spikes higher than expected, where you fall back into an old safety behaviour without quite noticing, or where you avoid something you'd normally handle fine. This is a completely normal part of any long-term change process, not evidence that the work didn't take or that you're back to where you started. The critical skill here is how you interpret a setback, not whether one happens — treating a single difficult moment as proof of total relapse is itself one of the cognitive distortions from Module 2 (catastrophising, discounting the positive) showing up in a new context.</p>

    <h2>A structured approach to a setback</h2>
    <p>When a setback happens, the same tools from earlier in the course apply directly:</p>
    <ul>
      <li><strong>Notice the automatic thought</strong> — likely something like "I'm back to square one" or "none of this actually worked." Name it specifically, the way you learned in Lesson 4.</li>
      <li><strong>Check the evidence</strong> — run it through the Lesson 5 process. What's the actual evidence for "back to square one," versus the accumulated evidence of genuine progress over the past months?</li>
      <li><strong>Treat it as one data point</strong> — a single difficult exposure or a single avoided situation is exactly that: one data point, not a trend, especially against a backdrop of many successful ones.</li>
      <li><strong>Get back to the relevant exposure soon</strong> — rather than avoiding it going forward out of self-protection, which would simply restart the fear-avoidance cycle from Lesson 1 for that specific situation.</li>
    </ul>

    <h2>Which practices are worth keeping as ongoing habits</h2>
    <p>Not everything from this course needs to continue in exactly its original form, but a few elements are worth deliberately maintaining, even in a lighter, less structured way than during the course itself:</p>
    <ul>
      <li><strong>Occasional exposure to harder situations</strong> — continuing to face genuinely difficult social situations periodically, rather than settling into a narrower comfort zone once the course structure is gone.</li>
      <li><strong>Catching and rethinking automatic thoughts</strong> — this becomes faster and more automatic with continued use; letting the skill go unused entirely tends to let old patterns creep back gradually.</li>
      <li><strong>Honest energy check-ins</strong> — your relationship to social energy will keep evolving as your life changes; periodically checking in with it, rather than assuming it's fixed, keeps your pacing accurate.</li>
    </ul>

    <h2>Building a light, ongoing maintenance rhythm</h2>
    <p>Rather than either abandoning the structure entirely or rigidly maintaining the full twelve-week intensity forever, a light periodic check-in works well — every month or so, briefly ask yourself: has avoidance quietly crept back into any specific area? Am I still occasionally challenging myself, or has my world narrowed without my fully noticing? Is there a current stressor making things harder than usual that's worth accounting for? A few honest minutes, periodically, tends to catch drift long before it becomes a significant setback.</p>

    <h2>Knowing when a setback is actually a signal to seek more support</h2>
    <p>Most setbacks, handled with the process above, resolve on their own with continued practice. Occasionally, though, a setback is significant enough, or persistent enough, to be worth more than self-directed tools — a return of anxiety severe enough to significantly disrupt daily functioning again, or a stretch of avoidance that isn't responding to your own efforts to work through it using this course's methods. If that happens, it's worth taking seriously rather than pushing through indefinitely alone; reaching out to a therapist trained in CBT, per the note back in Lesson 1, is a reasonable and appropriate response, not a sign this course failed you or that you failed at using it.</p>

    <h2>A permission slip for the future</h2>
    <p>It's worth explicitly giving yourself permission, in advance, for a future setback to happen without treating it as a crisis. Anxiety patterns are rarely permanently and completely eliminated in a way that guarantees they'll never resurface under any future stress or circumstance. Knowing this ahead of time — rather than being caught off guard and reading a future setback as proof the work "didn't really work" — makes it considerably easier to respond calmly and effectively using the structured approach above, rather than spiralling into the same catastrophic interpretation the setback itself might otherwise trigger.</p>

    <h2>Keeping the tools accessible</h2>
    <p>It's genuinely worth keeping your written material from this course somewhere easy to find — your trigger map, your exposure ladder, your rethinking exercises — rather than letting it disappear into old notes you'd have to search for. A future setback is much easier to work through when you can quickly reread exactly how you approached similar difficulties before, in your own words, rather than having to reconstruct the whole process again from a vaguer memory of having done this work at some point.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Pick a recurring check-in date — monthly is reasonable — and set a brief reminder to run through the three maintenance questions above. Treat it as genuine, ongoing upkeep, the same way you'd think about maintaining any other skill or habit you've worked hard to build.</p>
    </div>

    <p>The final lesson looks at the bigger picture — designing an ongoing social life that actually fits who you are, rather than one built entirely around managing or working around anxiety.</p>
    """,
})

LESSONS.append({
    "lesson_num": 18, "module_num": 6, "module_title": "Your Confident Life",
    "lesson_title": "Building a Life That Feels Social",
    "lesson_sub": "Designing your ongoing social world around your real personality",
    "tool": None,
    "body": """
    <p>This final lesson closes the course by shifting the frame slightly: from actively managing and working on anxiety, toward simply building a social life that genuinely fits who you are. The goal was never to turn you into a different, more extroverted person, or to make you comfortable in every possible social situation regardless of whether you'd actually want to be there. It was to remove anxiety as the thing making that choice for you, so you can build a social life based on your actual preferences instead.</p>

    <h2>Distinguishing anxiety from genuine preference</h2>
    <p>After months of active anxiety work, it's worth pausing on an important distinction: not every instance of choosing quiet, low-key, or limited social contact is anxiety avoidance. Plenty of people, entirely independent of any anxiety, genuinely prefer smaller gatherings over large ones, or need significant solitude to feel their best, or would rather have two close friends than a wide circle of acquaintances. The goal of this course was never to eliminate these genuine preferences — it was to make sure they're actually genuine preferences, freely chosen, rather than anxiety wearing the disguise of a preference. A useful test: does the choice come with relief and a sense of "this is what I actually want," or does it come with a lingering, guilty sense of "I'm doing this because I'm scared of the alternative"? The first is a preference worth honouring; the second is worth continuing to examine using the tools from this course.</p>

    <h2>Designing a social life around your real personality</h2>
    <p>With anxiety less in the driver's seat, it's worth deliberately thinking through what kind of social life you actually want, rather than defaulting to either the anxious, avoidant version from before this course or an imagined "confident person" version that doesn't actually fit you either. Consider: what breadth versus depth of connection genuinely appeals to you? What kinds of social settings do you find yourself enjoying, now that the anxiety around them has eased, versus which ones you can now handle but still don't particularly enjoy and don't need to seek out? There's no requirement to seek out every kind of social situation just because you're now capable of it — capability and genuine desire are different things, and this course has primarily been about building the former, so you're free to choose the latter deliberately.</p>

    <h2>Confidence as a foundation, not a destination</h2>
    <p>It's worth closing with an honest reframe of what "confidence" actually means, in light of everything covered in this course. It isn't the absence of nervousness, and it isn't a permanent, unshakable state you arrive at and then keep forever without further effort. It's closer to a working relationship with your own anxiety — an ability to notice it, understand where it's coming from, and choose your actions based on your actual values and preferences rather than automatically deferring to what the anxiety demands. That relationship, built over these eighteen lessons, is genuinely durable, but it's also something you'll keep actively using, in smaller ways, for the rest of your life — the same way any well-learned skill needs occasional, ongoing use to stay sharp.</p>

    <h2>A closing note</h2>
    <p>Eighteen lessons ago, the situations on your original trigger map likely felt fixed and unchangeable — just how things were, and probably always would be. You've since built a genuine, evidence-based understanding of how the fear-avoidance cycle works, real tools for challenging anxious thoughts, direct experience facing situations that used to feel impossible, and a much clearer sense of your own actual social preferences underneath the anxiety. That's not a small thing. If avoidance ever starts creeping back into some part of your life in the future, you now genuinely know how to work through it again — you've already done it once.</p>

    <h2>The tools you're keeping</h2>
    <p>As a final, practical summary: you're carrying forward the fear-avoidance framework from Lesson 1, which helps you understand any new anxious pattern that arises; the cognitive rethinking skills from Module 2, for examining anxious predictions rather than accepting them automatically; the exposure and experiment structure from Module 3, for facing new difficult situations deliberately rather than avoiding them; the conversational and relational skills from Module 4; and the energy-management awareness from Module 5. None of these require this course's structure to keep using — they're skills now, not a program you've completed and set aside.</p>

    <h2>If you're reading this at the start of a hard week</h2>
    <p>If you're revisiting this lesson at some point in the future during a genuinely difficult stretch, it's worth remembering directly: the tools you built through these eighteen lessons are still yours, fully available, regardless of how long it's been since you actively used them or how far the current difficulty feels from where you left off. A gap in active practice doesn't erase the underlying skill — it simply means picking the tools back up, starting wherever feels most relevant right now, whether that's the fear-avoidance cycle from Lesson 1 or a specific technique from later in the course. You've done this work once already; that's real, durable evidence you can do it again.</p>

    <div class="exercise-box">
      <div class="exercise-label">Try this</div>
      <p>Write a short, honest description of the social life you actually want going forward — not the anxious, avoidant version, and not an imagined "should" version, but the one that genuinely fits your real preferences now that anxiety has less control over the choice. Keep it somewhere you'll revisit occasionally.</p>
    </div>

    <p>That's the full course. You built this — carry it forward.</p>
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
        prev_link = f'<a href="/courses/confidence-blueprint/content/lessons/{prev_l["_slug"]}.html">← Lesson {prev_l["lesson_num"]}: {prev_l["lesson_title"]}</a>' if prev_l else '<span class="nav-placeholder">← Start of course</span>'
        next_link = f'<a href="/courses/confidence-blueprint/content/lessons/{next_l["_slug"]}.html">Lesson {next_l["lesson_num"]}: {next_l["lesson_title"]} →</a>' if next_l else '<a href="/courses/confidence-blueprint/content/">Back to course overview →</a>'

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
