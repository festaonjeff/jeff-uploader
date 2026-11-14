"""Zohobkmail 사이트 생성기 — 11-15 틱톡 심사 거절(아이콘 불일치 · 랜딩 페이지) 대응.
모든 페이지가 같은 머리(파비콘·OG)·메뉴·바닥글을 쓴다. 실행: python3 _build.py (이 폴더에서)."""
import re, pathlib
ROOT = pathlib.Path(__file__).parent
NAV = [("Features", "/features/"), ("How it works", "/how-it-works/"), ("Pricing", "/pricing/"),
       ("Docs", "/docs/"), ("FAQ", "/faq/"), ("Support", "/support/")]

def page(title, desc, body, path, lang="en"):
    url = "https://zohobkmail.com" + path
    nav = "".join(f'<a href="{h}">{t}</a>' for t, h in NAV)
    html = f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon.ico" sizes="any"><link rel="icon" type="image/png" sizes="32x32" href="/icon-32.png"><link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
<link rel="apple-touch-icon" href="/icon-180.png"><link rel="manifest" href="/site.webmanifest"><meta name="theme-color" content="#7c3aed">
<meta property="og:site_name" content="Zohobkmail"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="https://zohobkmail.com/og.png"><meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/style.css"></head><body>
<header class="top"><div class="wrap"><a class="brand" href="/"><img src="/icon-192.png" alt="Zohobkmail" width="36" height="36">Zohobkmail</a>
<nav>{nav}<a class="btn" href="/app/">Open app</a></nav></div></header>
<main class="wrap">
{body}
</main>
<footer><div class="wrap"><div class="cols">
<div><a class="brand" href="/"><img src="/icon-192.png" alt="" width="28" height="28">Zohobkmail</a><p class="d">Publish short videos to TikTok and YouTube from one place.</p></div>
<div><b>Product</b><a href="/features/">Features</a><a href="/how-it-works/">How it works</a><a href="/pricing/">Pricing</a><a href="/changelog/">Changelog</a></div>
<div><b>Resources</b><a href="/docs/">Documentation</a><a href="/faq/">FAQ</a><a href="/support/">Support</a><a href="/about/">About</a></div>
<div><b>Legal</b><a href="/privacy-policy/">Privacy Policy</a><a href="/terms-of-service/">Terms of Service</a></div>
</div><p class="d">© 2026 Zohobkmail · zohobkmail.com · <a href="mailto:contact@zohobkmail.com">contact@zohobkmail.com</a></p></div></footer>
</body></html>
"""
    out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")

def inner(old):
    """옛 약관·개인정보 페이지에서 <h1> 부터 </main> 앞까지 본문만 꺼낸다."""
    t = (ROOT / old).read_text(encoding="utf-8")
    t = t[t.index("<h1>"):]
    for cut in ("<footer>", "</main>"):
        if cut in t:
            t = t[:t.index(cut)]
    return t

# ── 홈
page("Zohobkmail — Publish short videos to TikTok and YouTube", "Zohobkmail is a video publishing tool for short-form creators: connect your accounts, pick a finished video, write the caption, choose privacy settings, and publish or schedule it from one place.", """
<section class="hero"><div>
<h1>One place to publish your short videos.</h1>
<p class="lead">Connect TikTok and YouTube with their official sign-in, pick a finished video, write the caption, set who can see it, and publish — or schedule it for later. Nothing to learn, nothing to re-upload twice.</p>
<p><a class="btn big" href="/app/">Open the app</a> <a class="btn ghost big" href="/how-it-works/">See how it works</a></p>
<p class="d">Works with TikTok Content Posting API (Direct Post) and YouTube Data API. Your tokens stay on your own computer.</p>
</div><div class="shot"><div class="win"><div class="bar"><i></i><i></i><i></i></div>
<div class="row"><span class="chip ok">TikTok · @yourname</span><span class="chip ok">YouTube · Your channel</span></div>
<div class="row"><div class="thumb"></div><div><b>1025_1559.mp4</b><br><span class="d">0:58 · 1080×1920 · 233 MB</span></div></div>
<div class="row"><label>Caption</label><div class="field">When the rain finally stopped… #shorts #story</div></div>
<div class="row"><label>Who can view</label><div class="field">Only me ▾</div><label>Comments</label><div class="field">On</div></div>
<div class="row"><span class="btn">Publish now</span><span class="btn ghost">Schedule</span></div>
</div></div></section>

<section class="grid3">
<div><h3>Official sign-in only</h3><p>You authorize Zohobkmail through TikTok Login Kit and Google sign-in. We never ask for your password and you can revoke access any time.</p></div>
<div><h3>Direct Post, your rules</h3><p>Choose the privacy level, allow or block comments, duet and stitch, and mark branded content — exactly the options TikTok offers in the app.</p></div>
<div><h3>Schedule a queue</h3><p>Set a time and let the app post for you. Posts go out in order and you see the status of each one on the dashboard.</p></div>
<div><h3>Same video, both platforms</h3><p>Publish one finished file to TikTok and YouTube Shorts with separate captions and privacy settings for each.</p></div>
<div><h3>Local-first privacy</h3><p>Tokens, captions and files are kept on your computer. Zohobkmail has no cloud account and does not store your media.</p></div>
<div><h3>Clear status, no surprises</h3><p>Every post shows its publishing state and a link to the post in TikTok Studio or YouTube Studio once it is live.</p></div>
</section>

<section class="steps"><h2>How it works</h2><ol>
<li><b>Connect.</b> Sign in to TikTok with Login Kit and authorize Zohobkmail. The app receives only the permissions needed to publish and read status.</li>
<li><b>Prepare.</b> Pick a finished video, write a caption and hashtags, and choose privacy level and interaction settings.</li>
<li><b>Publish.</b> Zohobkmail posts it to your TikTok profile through the Content Posting API — now or at the scheduled time — and shows the result.</li>
</ol><p><a href="/docs/">Read the documentation →</a></p></section>

<section class="cta"><h2>Ready to publish?</h2><p>Zohobkmail is free for personal use. <a href="/pricing/">See plans</a> or <a href="/app/">open the app</a>.</p></section>
""", "/")

# ── 기능
page("Features — Zohobkmail", "What Zohobkmail does: official sign-in, TikTok Direct Post with privacy and interaction settings, scheduling, YouTube Shorts, local-first storage.", """
<h1>Features</h1><p class="lead">Everything you need to get a finished short video from your computer onto your channels, and nothing you don't.</p>
<h2>Accounts</h2><ul>
<li><b>TikTok Login Kit</b> — connect your TikTok account with the official sign-in. Scopes requested: <code>user.info.basic</code> (show which account is connected) and <code>video.publish</code> (post videos). You can disconnect from the app or from TikTok → Settings → Security → Manage app permissions.</li>
<li><b>YouTube</b> — connect a channel with Google sign-in to publish Shorts and regular videos.</li>
<li>Connect several accounts and pick the destination per post.</li></ul>
<h2>Publishing to TikTok (Content Posting API · Direct Post)</h2><ul>
<li>Caption with hashtags and mentions (up to the TikTok limit shown live).</li>
<li><b>Who can view this video</b>: the exact privacy levels your account allows (Public, Friends, Only me…), fetched from TikTok each time.</li>
<li><b>Interactions</b>: allow comments, duet and stitch — each on or off.</li>
<li><b>Content disclosure</b>: mark Your brand / Branded content when the post is promotional, as required by TikTok.</li>
<li>Publishing status is polled and shown until TikTok reports the post as live, with a link to open it.</li></ul>
<h2>Scheduling</h2><ul><li>Pick a date and time; the app posts automatically.</li><li>Queue view with upcoming, posted and failed items; failed posts explain why.</li></ul>
<h2>Privacy by design</h2><ul><li>Runs on your own computer. Access tokens, captions and video files never leave it except to the platform you publish to.</li><li>No analytics, no advertising SDKs, no third-party sharing. See the <a href="/privacy-policy/">Privacy Policy</a>.</li></ul>
<h2>Requirements</h2><ul><li>macOS 13+ or Windows 10+, a modern browser, and a TikTok or YouTube account you own.</li><li>Videos: MP4 (H.264/AAC), vertical 9:16 recommended, up to the size and length limits of each platform.</li></ul>
""", "/features/")

# ── 사용법
page("How it works — Zohobkmail", "Step-by-step: connect your TikTok account, prepare a post, publish or schedule, and check status.", """
<h1>How it works</h1>
<h2>1. Connect your account</h2><p>Open the app and press <b>Connect TikTok account</b>. TikTok shows its own authorization screen listing the permissions Zohobkmail asks for. After you approve, you return to the app and see your username and avatar.</p>
<h2>2. Prepare the post</h2><p>Choose a finished video file. Write the caption, then choose <b>Who can view this video</b>, whether to allow <b>comments, duet and stitch</b>, and whether to disclose <b>branded content</b>. The app shows the limits of your account (video length, privacy options) before you post.</p>
<h2>3. Publish or schedule</h2><p>Press <b>Publish now</b>, or set a time and press <b>Schedule</b>. The video is uploaded to TikTok through the Content Posting API and the app shows the publishing status until it is live.</p>
<h2>4. Check status</h2><p>The dashboard lists every post with its state (queued, uploading, processing, posted, failed) and a link to the post. Failed posts show TikTok's reason so you can fix and retry.</p>
<h2>Disconnecting</h2><p>Press <b>Disconnect</b> in the app to remove the token from your computer, or revoke Zohobkmail from TikTok → Settings and privacy → Security → Manage app permissions.</p>
<p><a class="btn" href="/app/">Open the app</a></p>
""", "/how-it-works/")

# ── 요금
page("Pricing — Zohobkmail", "Zohobkmail plans: Free for personal use, Creator and Studio for teams.", """
<h1>Pricing</h1><p class="lead">Simple plans. No per-post fees.</p>
<section class="plans">
<div><h3>Free</h3><p class="price">$0</p><ul><li>1 TikTok account · 1 YouTube channel</li><li>Publish now</li><li>Up to 10 scheduled posts</li><li>Community support</li></ul><a class="btn" href="/app/">Get started</a></div>
<div class="hi"><h3>Creator</h3><p class="price">$9<span>/month</span></p><ul><li>Up to 3 accounts per platform</li><li>Unlimited scheduling</li><li>Post history export (CSV)</li><li>E-mail support</li></ul><a class="btn" href="/support/">Contact us</a></div>
<div><h3>Studio</h3><p class="price">$29<span>/month</span></p><ul><li>Up to 10 accounts per platform</li><li>Team seats</li><li>Priority support</li></ul><a class="btn" href="/support/">Contact us</a></div>
</section>
<p class="d">Prices in USD. Paid plans are billed monthly and can be cancelled any time. Platform limits (daily posts, video length) always apply.</p>
""", "/pricing/")

# ── 문서
page("Documentation — Zohobkmail", "Zohobkmail documentation: connecting TikTok, posting options, scheduling, troubleshooting and data handling.", """
<h1>Documentation</h1>
<h2>Connecting TikTok</h2><p>Zohobkmail uses <b>TikTok Login Kit</b>. Press <i>Connect TikTok account</i>; TikTok opens its authorization page and shows the requested permissions:</p>
<table><tr><th>Scope</th><th>Why</th></tr><tr><td><code>user.info.basic</code></td><td>Show the connected account's name and avatar in the app.</td></tr><tr><td><code>video.publish</code></td><td>Post the video you chose to your profile (Direct Post).</td></tr></table>
<p>After approval TikTok redirects to <code>https://zohobkmail.com/callback/</code>, which hands the authorization code back to the app running on your computer. The code is exchanged for a token locally; nothing is stored on this website.</p>
<h2>Posting options</h2><table>
<tr><th>Option</th><th>Values</th></tr>
<tr><td>Caption</td><td>Text, #hashtags, @mentions · TikTok length limit shown live</td></tr>
<tr><td>Who can view</td><td>Privacy levels allowed for your account (queried from TikTok)</td></tr>
<tr><td>Comments / Duet / Stitch</td><td>On or off, each</td></tr>
<tr><td>Content disclosure</td><td>Off · Your brand · Branded content</td></tr>
<tr><td>Schedule</td><td>Now, or a date and time</td></tr></table>
<h2>Video requirements</h2><ul><li>MP4 (H.264 video, AAC audio) · vertical 9:16 recommended.</li><li>Length and file size follow the limits TikTok reports for your account (the app checks before posting).</li></ul>
<h2>Status and errors</h2><p>Posts move through <i>queued → uploading → processing → posted</i>. If TikTok rejects a post, the reason is shown next to it (for example an unsupported privacy level or a video that is too long). Fix the post and retry; nothing is published twice.</p>
<h2>Disconnecting and data</h2><ul><li>Disconnect in the app deletes the token from your computer.</li><li>Revoke from TikTok: Settings and privacy → Security → Manage app permissions → Zohobkmail.</li><li>What we store and for how long: see the <a href="/privacy-policy/">Privacy Policy</a>.</li></ul>
""", "/docs/")

# ── FAQ
page("FAQ — Zohobkmail", "Frequently asked questions about Zohobkmail.", """
<h1>Frequently asked questions</h1>
<details open><summary>Is Zohobkmail an official TikTok or YouTube product?</summary><p>No. Zohobkmail is an independent tool that uses the official TikTok Content Posting API and YouTube Data API. TikTok and YouTube are trademarks of their owners.</p></details>
<details><summary>Do you need my TikTok password?</summary><p>No. You sign in on TikTok's own page (Login Kit). Zohobkmail only receives a token you can revoke at any time.</p></details>
<details><summary>Where are my videos and tokens stored?</summary><p>On your computer. The app runs locally and sends the video only to the platform you publish to. This website stores nothing.</p></details>
<details><summary>Can I choose who sees the video?</summary><p>Yes. The app shows the privacy levels your TikTok account allows and you pick one for each post. You also control comments, duet and stitch.</p></details>
<details><summary>Can I schedule posts?</summary><p>Yes. Set a date and time; the app posts automatically and shows the result.</p></details>
<details><summary>Why did my post fail?</summary><p>The app shows TikTok's reason next to the post — usually video length, size, or a privacy level not available to the account. Fix it and retry.</p></details>
<details><summary>How do I disconnect?</summary><p>Press Disconnect in the app, or revoke Zohobkmail under TikTok → Settings and privacy → Security → Manage app permissions.</p></details>
<details><summary>How do I contact you?</summary><p>E-mail <a href="mailto:contact@zohobkmail.com">contact@zohobkmail.com</a> or use the <a href="/support/">support page</a>.</p></details>
""", "/faq/")

# ── 지원
page("Support — Zohobkmail", "Get help with Zohobkmail: e-mail support, response times and what to include.", """
<h1>Support</h1>
<p class="lead">We answer e-mail within two business days.</p>
<p><a class="btn big" href="mailto:contact@zohobkmail.com?subject=Zohobkmail%20support">contact@zohobkmail.com</a></p>
<h2>What to include</h2><ul><li>Your operating system and app version (shown at the bottom of the app).</li><li>The platform (TikTok / YouTube) and what you tried to do.</li><li>The error text shown next to the post, if any.</li></ul>
<h2>Account and data requests</h2><p>To disconnect, use the app or revoke access on the platform. To ask what data we hold or to request deletion, e-mail us from the address associated with your account. See the <a href="/privacy-policy/">Privacy Policy</a>.</p>
<h2>Status</h2><p>All systems operational. Publishing depends on TikTok and YouTube availability; platform incidents are shown inside the app.</p>
""", "/support/")

# ── 소개
page("About — Zohobkmail", "About Zohobkmail and how to reach us.", """
<h1>About Zohobkmail</h1>
<p class="lead">Zohobkmail is a small publishing tool built for creators who finish videos on a computer and want to post them to TikTok and YouTube without juggling phones, transfers and re-typed captions.</p>
<p>It started as an internal tool for a short-form studio publishing several videos a day across channels, and is now offered to other creators. The product uses only official platform APIs and follows each platform's developer terms.</p>
<h2>Principles</h2><ul><li><b>Official sign-in only</b> — never passwords.</li><li><b>Local first</b> — your tokens and files stay on your computer.</li><li><b>Your rules</b> — privacy level, comments, duet, stitch and disclosure are always your choice, per post.</li></ul>
<h2>Contact</h2><p>Zohobkmail · <a href="mailto:contact@zohobkmail.com">contact@zohobkmail.com</a> · <a href="https://zohobkmail.com">zohobkmail.com</a></p>
""", "/about/")

# ── 변경 기록
page("Changelog — Zohobkmail", "Release notes for Zohobkmail.", """
<h1>Changelog</h1>
<h2>1.2 — November 2026</h2><ul><li>New app icon and website.</li><li>Documentation, FAQ and support pages.</li><li>Post status now links to the live post in TikTok Studio / YouTube Studio.</li></ul>
<h2>1.1 — October 2026</h2><ul><li>TikTok Content Posting API (Direct Post): privacy level, comments, duet, stitch and content disclosure per post.</li><li>Scheduling queue with retry.</li></ul>
<h2>1.0 — September 2026</h2><ul><li>First release: YouTube publishing and scheduling, TikTok Login Kit connection.</li></ul>
""", "/changelog/")

# ── 앱 들어가기(로그인 페이지 — 약관·개인정보 링크가 보여야 한다)
page("Open the app — Zohobkmail", "Open Zohobkmail on your computer or download it.", """
<h1>Open the app</h1>
<p class="lead">Zohobkmail runs on your own computer. If it is installed, the button below opens it; otherwise download it first.</p>
<p><a class="btn big" href="http://127.0.0.1:8787/tiktok">Open Zohobkmail on this computer</a></p>
<p class="d">Not installed? Download for <a href="/support/">macOS</a> · <a href="/support/">Windows</a> (sent by e-mail while we are in limited release).</p>
<h2>Sign in</h2><p>Inside the app, press <b>Connect TikTok account</b> or <b>Connect YouTube</b>. Sign-in happens on the platform's own page; Zohobkmail never sees your password.</p>
<p class="d">By using Zohobkmail you agree to the <a href="/terms-of-service/">Terms of Service</a> and <a href="/privacy-policy/">Privacy Policy</a>.</p>
""", "/app/")

# ── 약관·개인정보 (본문 유지 · 새 틀)
page("Privacy Policy — Zohobkmail", "How Zohobkmail handles your data.", inner("privacy-policy/index.html"), "/privacy-policy/")
page("Terms of Service — Zohobkmail", "Terms for using Zohobkmail.", inner("terms-of-service/index.html"), "/terms-of-service/")

# ── 404
page("Page not found — Zohobkmail", "Page not found.", "<h1>Page not found</h1><p>The page you asked for does not exist. <a href='/'>Go to the home page</a>.</p>", "/404/")
(ROOT / "404.html").write_text((ROOT / "404/index.html").read_text(encoding="utf-8"), encoding="utf-8")

(ROOT / "site.webmanifest").write_text('{"name":"Zohobkmail","short_name":"Zohobkmail","icons":[{"src":"/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"/icon-512.png","sizes":"512x512","type":"image/png"}],"theme_color":"#7c3aed","background_color":"#ffffff","display":"standalone","start_url":"/"}', encoding="utf-8")
(ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://zohobkmail.com/sitemap.xml\n", encoding="utf-8")
urls = ["/", "/features/", "/how-it-works/", "/pricing/", "/docs/", "/faq/", "/support/", "/about/", "/changelog/", "/app/", "/privacy-policy/", "/terms-of-service/"]
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>https://zohobkmail.com{u}</loc></url>" for u in urls) + "</urlset>\n", encoding="utf-8")
print("built", len(urls), "pages")
