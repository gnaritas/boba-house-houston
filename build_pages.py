#!/usr/bin/env python3
"""Boba House — site generator (template v2 T1, t_a72eabbd, built 2026-11-24).
Custom design; facts only from the card + checkpoint evidence; zero third-party JS/CSS."""
import json, hashlib, pathlib

SLUG = "boba-house-houston"
ORIGIN = "https://boba-house-houston-demo.up.railway.app"
TEL = "+18325973205"
TEL_TXT = "(832) 597-3205"
NAP = "5353 W Alabama St Ste 100, Houston, TX 77056"
EMAIL = "info@bobahouse.us"
TOAST = "https://www.toasttab.com/local/order/boba-house-llc-6834-wilcrest-dr"
DOORDASH = "https://www.doordash.com/store/boba-house-houston-41269676/"
IG = "https://www.instagram.com/bobahouse.us/"
FB = "https://www.facebook.com/bobahouse.us/"
MAPQ = "https://www.google.com/maps?q=5353%20W%20Alabama%20St%20Ste%20100%2C%20Houston%2C%20TX%2077056&output=embed"
DIRS = "https://www.google.com/maps/dir/?api=1&destination=5353%20W%20Alabama%20St%20Ste%20100%2C%20Houston%2C%20TX%2077056"
OUT = pathlib.Path(__file__).parent / "public"

EMBLEM = ('<svg class="mark" viewBox="0 0 100 100" role="img" aria-label="Boba House emblem: a shake cup with straw and boba pearls">'
'<circle cx="50" cy="50" r="47" fill="#583a6b"/>'
'<path d="M27 31h46" stroke="#f8f1e3" stroke-width="6" stroke-linecap="round"/>'
'<path d="M64 12l-8 19" stroke="#f8f1e3" stroke-width="6" stroke-linecap="round"/>'
'<path d="M33 35h34l-3.4 41c-.3 3.4-2.4 5.5-5.6 5.5H42c-3.2 0-5.3-2.1-5.6-5.5L33 35Z" fill="none" stroke="#f8f1e3" stroke-width="5" stroke-linejoin="round"/>'
'<circle cx="44" cy="63" r="4.6" fill="#f0c987"/><circle cx="56" cy="67" r="4.6" fill="#f0c987"/><circle cx="49" cy="54" r="4.2" fill="#cf8f3f"/></svg>')

FOOTER = ('<footer><div class="wrap footline">'
'<div class="fbrand">' + EMBLEM + '<span>Boba House<small>Taste the feeling, taste the boba</small></span></div>'
'<address>Boba House<br>5353 W Alabama St Ste 100<br>Houston, TX 77056<br>Inside The Conservatory Galleria<br>'
'<a href="tel:' + TEL + '">' + TEL_TXT + '</a><br><a href="mailto:' + EMAIL + '">' + EMAIL + '</a></address>'
'<p class="fsocial"><a href="' + IG + '" rel="noopener">Instagram @bobahouse.us</a><br>'
'<a href="' + FB + '" rel="noopener">Facebook</a><br><a href="' + TOAST + '" rel="noopener">Order online — Toast</a><br>'
'<a href="' + DOORDASH + '" rel="noopener">Order via DoorDash</a></p>'
'</div><p class="wrap copy">© Boba House · Houston, Texas</p>'
'<img src="/pixel.gif" width="1" height="1" alt="" loading="lazy"></footer>')

NAV = ('<header class="top"><div class="wrap">'
'<a class="brand" href="/">' + EMBLEM + '<span class="word">Boba House<small>Boba · Milk Tea · Houston</small></span></a>'
'<nav class="main" aria-label="Main"><ul><li><a href="/menu">Menu</a></li><li><a href="/catering">Catering</a></li>'
'<li><a href="/visit">Visit</a></li><li><a class="btn" href="/contact">Contact</a></li></ul></nav>'
'<a class="tel" href="tel:' + TEL + '">' + TEL_TXT + '</a></div></header>')

HOURS_TABLE = ('<table class="hours"><tbody>'
'<tr><th>Monday</th><td>11:00 am – 10:00 pm</td></tr>'
'<tr><th>Tuesday</th><td class="closed">Closed</td></tr>'
'<tr><th>Wednesday</th><td>11:00 am – 10:00 pm</td></tr>'
'<tr><th>Thursday</th><td>11:00 am – 10:00 pm</td></tr>'
'<tr><th>Friday</th><td>11:00 am – 11:00 pm</td></tr>'
'<tr><th>Saturday</th><td>12:00 pm – 11:00 pm</td></tr>'
'<tr><th>Sunday</th><td>12:00 pm – 11:00 pm</td></tr>'
'</tbody></table>')

OPENINGS = [{"@type": "OpeningHoursSpecification", "dayOfWeek": d, "opens": o, "closes": c} for d, o, c in [
    ("Monday", "11:00", "22:00"), ("Wednesday", "11:00", "22:00"), ("Thursday", "11:00", "22:00"),
    ("Friday", "11:00", "23:00"), ("Saturday", "12:00", "23:00"), ("Sunday", "12:00", "23:00")]]

SHOP_LD = {
    "@context": "https://schema.org", "@type": "CafeOrCoffeeShop", "name": "Boba House",
    "alternateName": "Bobahouse",
    "slogan": "Taste the feeling, taste the boba",
    "description": "Boba shop inside The Conservatory Galleria food hall serving milk tea, fruit tea, blended tea and bubble tea, shaken to order.",
    "url": ORIGIN + "/", "telephone": TEL, "email": EMAIL,
    "address": {"@type": "PostalAddress", "streetAddress": "5353 W Alabama St Ste 100",
                "addressLocality": "Houston", "addressRegion": "TX", "postalCode": "77056", "addressCountry": "US"},
    "geo": {"@type": "GeoCoordinates", "latitude": 29.7379156, "longitude": -95.469563},
    "openingHoursSpecification": OPENINGS,
    "image": ORIGIN + "/og.png",
    "foundingDate": "2026-03-21",
    "hasMenu": {"@type": "Menu", "name": "Boba House drink menu", "url": ORIGIN + "/menu"},
    "sameAs": [IG, FB, TOAST, DOORDASH],
}

def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, separators=(",", ":"), ensure_ascii=False) + "</script>"

def bread(*names):
    items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": ORIGIN + ("/" if i == 0 else "/" + n.lower().split()[0].replace(" & ", "-").replace(" ", "-"))} for i, n in enumerate(names)]
    return ld({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})

def faq(qa):
    return ld({"@context": "https://schema.org", "@type": "FAQPage", "itemListElement": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]})

def head(title, desc, path, ld_blocks):
    url = ORIGIN + ("/" if path == "/" else path)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#241009">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Boba House">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{ORIGIN}/og.png">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ORIGIN}/og.png">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="stylesheet" href="/style.css">
{ld_blocks}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{NAV}
"""

def page(name, title, desc, body, ld_blocks, path=None):
    p = "" if name == "index" else "/" + name
    if path is not None:
        p = path
    html = head(title, desc, p, ld_blocks) + body + FOOTER + "\n</body>\n</html>\n"
    (OUT / (name + ".html")).write_text(html, encoding="utf-8")

# ---------------- HOME ----------------
home_faq = [
    ("Do you cater events?", "Yes — boba catering for parties, charity fundraisers and weddings. Call " + TEL_TXT + " or send a note from the catering page."),
    ("Are you open on Tuesdays?", "No — the shop is closed on Tuesdays. It pours late on Friday and Saturday nights, until 11 pm."),
    ("Where exactly is Boba House?", "5353 W Alabama St, Suite 100, inside The Conservatory Galleria food hall, Houston, TX 77056."),
]
home_body = """<main id="main">
<section class="hero"><div class="wrap">
<p class="kick">Inside The Conservatory Galleria · Houston</p>
<h1>Taste the feeling, taste the boba.</h1>
<p class="sub">Boba House is a boba and milk tea shop at 5353 West Alabama Street. Milk tea, fruit tea, blended tea and bubble tea — every cup built fresh at the counter of The Conservatory Galleria food hall.</p>
<p class="heract"><a class="btn gold" href="""" + TOAST + """">Order online</a><a class="btn ghost" href="/menu">See the menu</a></p>
</div></section>
<section class="band"><div class="wrap">
<div class="bandhead"><div><p class="kick">The drinks</p><h2>Four ways to order your cup</h2>
<p class="bandsub">Every drink starts with tea. Pick a style, then build it your way at the counter.</p></div>
<a class="btn ghost" href="/menu">Full menu</a></div>
<div class="cards">
<div class="card"><span class="cupnum">01</span><h3>Milk Tea</h3><p>Tea shaken creamy and cold. Matcha lattes are on the counter too.</p><a class="more" href="/milk-tea">Milk tea &amp; bubble tea&nbsp;→</a></div>
<div class="card"><span class="cupnum">02</span><h3>Fruit Tea</h3><p>Bright, iced and refreshing — the Honey Lemon Tea is on the menu.</p></div>
<div class="card"><span class="cupnum">03</span><h3>Blended Tea</h3><p>Thick, frosty and blended right in front of you.</p></div>
<div class="card"><span class="cupnum">04</span><h3>Bubble Tea</h3><p>The classic with boba — the shop's signature, made to order.</p></div>
</div>
<ul class="lineup" style="margin-top:22px">
<li><b>Ube Creme</b><span>straight off the Toast ordering page</span></li>
<li><b>Pink Cloud</b><span>straight off the Toast ordering page</span></li>
<li><b>Honey Lemon Tea</b><span>straight off the Toast ordering page</span></li>
</ul>
</div></section>
<section class="band milk"><div class="wrap">
<span class="tagchip">Opened with a lion dance</span>
<h2>The shop that arrived on March&nbsp;21,&nbsp;2026</h2>
<p style="max-width:64ch">Boba House opened inside The Conservatory Galleria with a lion dance at 2 in the afternoon, and the Houston Press covered the whole first day — open from 11 in the morning until 9 at night, with a buy-one-get-one free milk tea for everyone who walked in.</p>
<p style="max-width:64ch">The shop exists to be a cozy, welcoming place where every sip brings joy and satisfaction: a community of boba lovers, gathered one cup at a time.</p>
</div></section>
<section class="band"><div class="wrap">
<div class="bandhead"><div><p class="kick">More than drinks</p><h2>Snacks, treats and merch</h2></div></div>
<div class="duo">
<div class="card"><h3>Snacks &amp; treats</h3><p>Pair your drink — from crispy bites to sweet desserts.</p></div>
<div class="card"><h3>Take it home</h3><p>Apparel and accessories from Boba House, sold at the shop.</p></div>
</div>
</div></section>
<section class="band deep"><div class="wrap">
<p class="kick">Catering</p><h2>Boba House pours for your event</h2>
<p class="bandsub">Boba catering for parties, charity fundraisers and weddings — booked straight through the shop, one sip at a time.</p>
<p class="heract"><a class="btn gold" href="/catering">Catering details</a><a class="btn ghost" href="/contact">Ask about a date</a></p>
</div></section>
<section class="band"><div class="wrap mapside">
<div><p class="kick">Find the shop</p><h2>Hours &amp; directions</h2>
""" + HOURS_TABLE + """
<p style="margin-top:18px">""" + NAP + """ — inside The Conservatory Galleria.</p>
<p class="heract"><a class="btn" href="/visit">Hours, map and ordering</a><a class="btn ghost" href="tel:""" + TEL + """">Call the shop</a></p>
</div>
<div class="mapframe"><iframe title="Map showing Boba House at 5353 W Alabama Street Suite 100 in Houston, TX" src=\"""" + MAPQ + """\" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div></section>
<section class="band milk"><div class="wrap faq">
<p class="kick">Good questions</p><h2>Asked most often</h2>
""" + "".join("<details><summary>%s</summary><p>%s</p></details>" % (q, a) for q, a in home_faq) + """
</div></section>
</main>"""
page("index", "Boba & Milk Tea Shop — Boba House, Houston TX",
     "Boba House shakes boba, milk tea, fruit tea and blended tea at 5353 W Alabama St Ste 100 in The Conservatory Galleria, Houston. Hours, menu and directions.",
     home_body, ld(SHOP_LD) + "\n" + faq(home_faq) + "\n" + bread("Home"))

# ---------------- MENU ----------------
menu_body = """<main id="main">
<section class="pageband"><div class="wrap">
<p class="kick">Menu</p><h1>Milk tea, fruit tea, blended tea and bubble tea.</h1>
<p class="bandsub page">The four styles behind the counter at Boba House — tea built fresh, shaken, blended or poured.</p>
</div></section>
<section class="band"><div class="wrap">
<div class="cards">
<div class="card"><span class="cupnum">01</span><h3>Milk Tea</h3><p>Tea shaken creamy and cold over ice. Matcha lattes live in this family too.</p><a class="more" href="/milk-tea">Milk tea &amp; bubble tea&nbsp;→</a></div>
<div class="card"><span class="cupnum">02</span><h3>Fruit Tea</h3><p>Light, iced and bright — the Honey Lemon Tea is one people point at first.</p></div>
<div class="card"><span class="cupnum">03</span><h3>Blended Tea</h3><p>Frosty and thick, blended right at the open counter.</p></div>
<div class="card"><span class="cupnum">04</span><h3>Bubble Tea</h3><p>Tea, the good stuff and boba — the signature lineup of the shop.</p></div>
</div>
</div></section>
<section class="band milk"><div class="wrap">
<div class="bandhead"><div><p class="kick">Off the ordering page</p><h2>Names people ask for</h2>
<p class="bandsub">Lifted straight from the shop's Toast ordering page.</p></div></div>
<ul class="lineup">
<li><b>Ube Creme</b><span>purple yam, shaken up</span></li>
<li><b>Pink Cloud</b><span>a cup with a name like that</span></li>
<li><b>Honey Lemon Tea</b><span>fruit tea, the popular one</span></li>
</ul>
<p class="note" style="margin-top:18px">Sizes, sweetness and the full build-your-drink list — prices too — live at the counter and on the shop's Toast ordering page.</p>
</div></section>
<section class="band"><div class="wrap">
<div class="duo">
<div class="card"><h3>Snacks &amp; treats</h3><p>Crispy bites through sweet desserts, made to go with the drink.</p></div>
<div class="card"><h3>Merch</h3><p>Boba House apparel and accessories at the shop.</p></div>
</div>
</div></section>
<section class="band deep"><div class="wrap">
<p class="kick">Ready when you are</p><h2>Order ahead or come by</h2>
<p class="bandsub">Skip the line on Toast, get it delivered on DoorDash, or walk to Suite 100 at The Conservatory Galleria.</p>
<p class="heract"><a class="btn gold" href=\"""" + TOAST + """">Order on Toast</a><a class="btn ghost" href="/visit">Hours and map</a></p>
</div></section>
</main>"""
menu_ld = {"@context": "https://schema.org", "@type": "Menu", "name": "Boba House drink menu", "url": ORIGIN + "/menu",
           "hasMenuSection": [
               {"@type": "MenuSection", "name": "Milk Tea"}, {"@type": "MenuSection", "name": "Fruit Tea"},
               {"@type": "MenuSection", "name": "Blended Tea"}, {"@type": "MenuSection", "name": "Bubble Tea"},
               {"@type": "MenuSection", "name": "Named on the ordering page", "hasMenuItem": [
                   {"@type": "MenuItem", "name": "Ube Creme"}, {"@type": "MenuItem", "name": "Pink Cloud"},
                   {"@type": "MenuItem", "name": "Honey Lemon Tea"}]}]}
page("menu", "Milk Tea, Fruit Tea & Bubble Tea Menu — Boba House, Houston TX",
     "Milk tea, fruit tea, blended tea and bubble tea — the drink lineup at Boba House in The Conservatory Galleria, Houston, plus the names on the Toast ordering page.",
     menu_body, ld(menu_ld) + "\n" + bread("Home", "Menu"))

# ---------------- MILK TEA detail ----------------
mt_faq = [
    ("Do everything come with tapioca pearls?", "Bubble tea and milk tea are built with boba. Fruit tea and blended tea skip the pearls unless you ask."),
    ("Do you have matcha?", "Yes — matcha tea and matcha lattes are on the counter."),
    ("Is the milk tea made to order?", "Every cup is shaken fresh when you order it."),
]
mt_body = """<main id="main">
<section class="pageband"><div class="wrap">
<p class="kick">Milk Tea · Bubble Tea</p><h1>Milk tea and bubble tea, shaken to order.</h1>
<p class="bandsub page">The heart of the Boba House counter — tea, shaken creamy, frosted with ice, finished with boba.</p>
</div></section>
<section class="band"><div class="wrap">
<p style="max-width:64ch">Milk tea at Boba House starts the same way every time: real tea pulled strong, shaken with milk and ice until the cup goes frosty. Classic, ube, matcha — the counter walks you through the build, sweetness your call.</p>
<p style="max-width:64ch">Bubble tea is the house signature: the same shaken tea, tea-left or tea-heavy, with a spoonful of boba through the wide straw. Matcha lattes sit in the same family for the matcha regulars.</p>
<div class="duo" style="margin-top:22px">
<div class="card"><h3>How people order it</h3><p>The names off the Toast ordering page — Ube Creme and Pink Cloud — go over ice; Honey Lemon Tea is the iced side of the menu.</p></div>
<div class="card"><h3>The Galleria-Uptown cup</h3><p>Boba House shakes these cups at Suite 100 of The Conservatory Galleria, on West Alabama in the Galleria and Uptown stretch of Houston.</p></div>
</div>
<p class="heract" style="margin-top:26px"><a class="btn gold" href=\"""" + TOAST + """">Order milk tea on Toast</a><a class="btn ghost" href="tel:""" + TEL + """">Call """ + TEL_TXT + """</a></p>
</div></section>
<section class="band milk"><div class="wrap faq">
<p class="kick">Milk tea questions</p><h2>Before you order</h2>
""" + "".join("<details><summary>%s</summary><p>%s</p></details>" % (q, a) for q, a in mt_faq) + """
<p class="heract" style="margin-top:20px"><a class="btn" href="/menu">Back to the menu</a></p>
</div></section>
</main>"""
svc_milk = {"@context": "https://schema.org", "@type": "Service", "serviceType": "Milk Tea & Bubble Tea",
            "name": "Milk Tea & Bubble Tea — Boba House", "url": ORIGIN + "/milk-tea",
            "description": "Milk tea and bubble tea shaken to order, including matcha lattes, at Boba House in Houston.",
            "provider": {"@type": "CafeOrCoffeeShop", "name": "Boba House",
                         "address": {"@type": "PostalAddress", "streetAddress": "5353 W Alabama St Ste 100",
                                     "addressLocality": "Houston", "addressRegion": "TX", "postalCode": "77056", "addressCountry": "US"}},
            "areaServed": {"@type": "City", "name": "Houston"}}
page("milk-tea", "Milk Tea & Bubble Tea, Shaken to Order — Boba House, Houston TX",
     "Milk tea and bubble tea shaken fresh at Boba House in Houston — matcha lattes, boba pearls and the names people order most off the Toast menu.",
     mt_body, ld(svc_milk) + "\n" + faq(mt_faq) + "\n" + bread("Home", "Menu"))

# ---------------- CATERING detail ----------------
cat_faq = [
    ("What events does Boba House cater?", "Parties, charity fundraisers and weddings — the shop lists those three catering services itself."),
    ("How do I book a date?", "Call " + TEL_TXT + " or send a note through the contact form with your date and head count."),
    ("Where is catering served?", "Built at the shop at The Conservatory Galleria; talk through delivery and setup with the shop when you book."),
]
cat_body = """<main id="main">
<section class="pageband"><div class="wrap">
<p class="kick">Catering</p><h1>Boba for the party, the fundraiser, the wedding.</h1>
<p class="bandsub page">Boba House brings its drinks to bigger rooms — booked straight through the shop, one sip at a time.</p>
</div></section>
<section class="band"><div class="wrap">
<div class="cards tri">
<div class="card"><span class="cupnum">Service 01</span><h3>Parties &amp; events</h3><p>Boba catering for birthdays, hangouts and office parties.</p></div>
<div class="card"><span class="cupnum">Service 02</span><h3>Charity fundraisers</h3><p>A cup everyone likes at a table that raises money.</p></div>
<div class="card"><span class="cupnum">Service 03</span><h3>Weddings</h3><p>The sweet spot at the reception — shaken, not stirred.</p></div>
</div>
<p style="max-width:64ch;margin-top:26px">These are the catering services the shop runs from its own ordering pages. Quantities, flavors and setup get planned with you, cup count by cup count — the shop built itself around service and community gathering, and catering is the same idea at a bigger table.</p>
<p class="heract"><a class="btn gold" href="tel:""" + TEL + """">Call """ + TEL_TXT + """</a><a class="btn ghost" href="/contact">Send a note about your date</a></p>
</div></section>
<section class="band milk"><div class="wrap faq">
<p class="kick">Catering questions</p><h2>Plan the pour</h2>
""" + "".join("<details><summary>%s</summary><p>%s</p></details>" % (q, a) for q, a in cat_faq) + """
<p class="heract" style="margin-top:20px"><a class="btn" href="/menu">Back to the menu</a></p>
</div></section>
</main>"""
svc_cat = {"@context": "https://schema.org", "@type": "Service", "serviceType": "Catering",
           "name": "Boba Catering — Boba House", "url": ORIGIN + "/catering",
           "description": "Boba catering for parties, charity fundraisers and weddings, booked through Boba House in Houston.",
           "provider": {"@type": "CafeOrCoffeeShop", "name": "Boba House",
                        "address": {"@type": "PostalAddress", "streetAddress": "5353 W Alabama St Ste 100",
                                    "addressLocality": "Houston", "addressRegion": "TX", "postalCode": "77056", "addressCountry": "US"}},
           "areaServed": {"@type": "City", "name": "Houston"}}
page("catering", "Boba Catering for Parties & Weddings — Boba House, Houston TX",
     "Boba catering for parties, charity fundraisers and weddings — book Boba House, the Conservatory Galleria boba shop in Houston, by phone or note.",
     cat_body, ld(svc_cat) + "\n" + faq(cat_faq) + "\n" + bread("Home", "Catering"))

# ---------------- VISIT ----------------
visit_body = """<main id="main">
<section class="pageband"><div class="wrap">
<p class="kick">Visit</p><h1>Hours, directions and how to order.</h1>
<p class="bandsub page">Suite 100 of The Conservatory Galleria food hall — walk in, order ahead on Toast, or get it delivered on DoorDash.</p>
</div></section>
<section class="band"><div class="wrap mapside">
<div>""" + HOURS_TABLE + """
<address class="dup" style="margin-top:22px">Boba House<br>""" + NAP + """<br><a href="tel:""" + TEL + """">""" + TEL_TXT + """</a> · <a href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></address>
<p class="heract" style="margin-top:22px"><a class="btn gold" href=\"""" + DIRS + """">Get directions</a><a class="btn ghost" href=\"""" + TOAST + """">Order on Toast</a></p>
</div>
<div class="mapframe"><iframe title="Map showing Boba House at 5353 W Alabama Street Suite 100 in Houston, TX" src=\"""" + MAPQ + """\" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div></section>
<section class="band milk"><div class="wrap">
<div class="bandhead"><div><p class="kick">Three ways in</p><h2>Walk, tap or door-dash</h2></div></div>
<div class="cards tri">
<div class="card"><h3>At the counter</h3><p>Walk to Suite 100 and watch the shake. Hours above, closed Tuesdays.</p></div>
<div class="card"><h3>On Toast</h3><p>Order ahead from the shop's own ordering page and pick up when it's ready.</p></div>
<div class="card"><h3>On DoorDash</h3><p>Boba delivered from the Galleria area through DoorDash.</p></div>
</div>
<p class="note" style="margin-top:20px">Follow the shop on <a href=\"""" + IG + """\" rel="noopener">Instagram @bobahouse.us</a> or <a href=\"""" + FB + """\" rel="noopener">Facebook</a> for new specials.</p>
</div></section>
</main>"""
page("visit", "Hours & Directions — Boba House, Conservatory Galleria, Houston TX",
     "Hours, address and map for Boba House: 5353 W Alabama St Ste 100, Houston, TX 77056, inside The Conservatory Galleria. Order on Toast or DoorDash.",
     visit_body, ld(SHOP_LD) + "\n" + bread("Home", "Visit"))

# ---------------- CONTACT ----------------
contact_body = """<main id="main">
<section class="pageband"><div class="wrap">
<p class="kick">Contact</p><h1>Call, email, or leave a note.</h1>
<p class="bandsub page">Notes from this page go to the shop's inbox — orders, catering dates and anything else.</p>
</div></section>
<section class="band"><div class="wrap mapside">
<div>
<form class="cform" action="/contact" method="post">
<label for="f-name">Name *</label><input id="f-name" name="name" type="text" autocomplete="name" required>
<div class="two">
<div><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
<div><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
</div>
<label for="f-message">What's it about? *</label><textarea id="f-message" name="message" required></textarea>
<p class="hint">Catering asks? Put the date and head count in the note.</p>
<button class="btn" type="submit">Send the note</button>
</form>
</div>
<div>
<address class="dup">Boba House<br>""" + NAP + """<br><a href="tel:""" + TEL + """">""" + TEL_TXT + """</a><br><a href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></address>
<p class="heract" style="margin-top:18px"><a class="btn gold" href=\"""" + DIRS + """">Get directions</a></p>
<div class="mapframe"><iframe title="Map showing Boba House at 5353 W Alabama Street Suite 100 in Houston, TX" src=\"""" + MAPQ + """\" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div>
</div></section>
</main>"""
page("contact", "Contact Boba House — Houston, TX",
     "Call (832) 597-3205, email info@bobahouse.us or leave a note — contact Boba House, the boba shop inside The Conservatory Galleria in Houston.",
     contact_body, ld({"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact Boba House", "url": ORIGIN + "/contact"}) + "\n" + bread("Home", "Contact"))

# ---------------- PRIVACY ----------------
PRIV_CONTACT = '<p>Ask the shop at <a href="mailto:' + EMAIL + '">' + EMAIL + '</a> or ' + TEL_TXT + '.</p>'
priv_body = """<main id="main">
<section class="pageband"><div class="wrap">
<p class="kick">Privacy</p><h1>Privacy at Boba House.</h1>
<p class="bandsub page">Short, plain, and about this website only.</p>
</div></section>
<section class="band"><div class="wrap">
<div class="faq">
<h2>What this site collects</h2>
<p>The only personal details this site takes are the ones you type into the contact form: your name, phone, email and message. The note is sent straight to the shop's inbox so someone can answer you. Nothing is sold, and nothing is shared with advertisers.</p>
<h2>No tracking</h2>
<p>This site sets no cookies and loads no third-party scripts. The map embed is the only outside service on the page.</p>
<h2>Where it is hosted</h2>
<p>This site is hosted at """ + ORIGIN.replace("https://", "") + """.</p>
<h2>Questions</h2>
""" + PRIV_CONTACT + """
<p class="note">Updated November 24, 2026.</p>
</div>
</div></section>
</main>"""
page("privacy", "Privacy — Boba House, Houston TX",
     "How the Boba House website handles your details: one contact form, no cookies, no tracking scripts. Boba House, Houston, TX.",
     priv_body, ld({"@context": "https://schema.org", "@type": "WebPage", "name": "Privacy — Boba House", "url": ORIGIN + "/privacy"}) + "\n" + bread("Home", "Privacy"))

# ---------------- 404 + THANKS ----------------
nf_body = """<main id="main">
<section class="pageband"><div class="wrap">
<p class="kick">404</p><h1>That cup is off the menu.</h1>
<p class="bandsub page">The page you asked for isn't here. The drinks are.</p>
<p class="heract"><a class="btn gold" href="/">Back to home</a><a class="btn ghost" href="/menu">See the menu</a></p>
</div></section>
</main>"""
page("404", "Page Not Found — Boba House, Houston TX",
     "Page not found — back to the Boba House menu, hours or directions in Houston.", nf_body, "")
tk_body = """<main id="main">
<section class="pageband"><div class="wrap">
<p class="kick">Sent</p><h1>Note sent.</h1>
<p class="bandsub page">It landed in the shop's inbox. For anything time-sensitive, call """ + TEL_TXT + """.</p>
<p class="heract"><a class="btn gold" href="/">Back to home</a><a class="btn ghost" href="/menu">See the menu</a></p>
</div></section>
</main>"""
page("thanks", "Note Sent — Boba House, Houston TX",
     "Your note went to the Boba House inbox in Houston. Call (832) 597-3205 for anything time-sensitive.", tk_body, "")

# ---------------- assets ----------------
(OUT / "sitemap.xml").write_text("""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + "\n".join("<url><loc>" + ORIGIN + p + "</loc><lastmod>2026-11-24</lastmod></url>"
                for p in ["/", "/menu", "/milk-tea", "/catering", "/visit", "/contact", "/privacy"]) + """
</urlset>
""", encoding="utf-8")
(OUT / "robots.txt").write_text("""User-agent: *
Disallow: /thanks
Disallow: /404

Sitemap: """ + ORIGIN + """/sitemap.xml
""", encoding="utf-8")
(OUT / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
 '<circle cx="50" cy="50" r="50" fill="#583a6b"/>'
 '<path d="M27 31h46" stroke="#f8f1e3" stroke-width="6" stroke-linecap="round"/>'
 '<path d="M64 12l-8 19" stroke="#f8f1e3" stroke-width="6" stroke-linecap="round"/>'
 '<path d="M33 35h34l-3.4 41c-.3 3.4-2.4 5.5-5.6 5.5H42c-3.2 0-5.3-2.1-5.6-5.5L33 35Z" fill="none" stroke="#f8f1e3" stroke-width="5" stroke-linejoin="round"/>'
 '<circle cx="44" cy="63" r="4.6" fill="#f0c987"/><circle cx="56" cy="67" r="4.6" fill="#f0c987"/><circle cx="49" cy="54" r="4.2" fill="#cf8f3f"/></svg>\n', encoding="utf-8")

for f in sorted(OUT.iterdir()):
    h = hashlib.sha256(f.read_bytes()).hexdigest()[:12]
    print(f"{h}  {f.stat().st_size:>7}  {f.name}")
