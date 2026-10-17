import os, shutil, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import *

OUT = sys.argv[1]
if os.path.exists(OUT):
    shutil.rmtree(OUT)
for d in ["", "css", "js", "tools", "category", "guides"]:
    os.makedirs(os.path.join(OUT, d), exist_ok=True)

CSS = r"""
:root{--bg:#f7f8fc;--card:#fff;--text:#1b1f33;--muted:#5d6482;--line:#e3e6f2;--brand:#5b4bff;--brand2:#00b8d9;--ok:#12a36b;--bad:#d9534f;--radius:16px;--shadow:0 6px 24px rgba(40,50,120,.08)}
:root[data-theme=dark]{--bg:#0e1020;--card:#171a30;--text:#eef0ff;--muted:#a3a9cc;--line:#262a48;--shadow:0 6px 24px rgba(0,0,0,.4)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.65}
a{color:var(--brand);text-decoration:none}a:hover{text-decoration:underline}
img,svg{max-width:100%}
.wrap{max-width:1120px;margin:0 auto;padding:0 20px}
header.site{position:sticky;top:0;z-index:50;background:color-mix(in srgb,var(--bg) 88%,transparent);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;justify-content:space-between;height:64px;gap:16px}
.logo{font-weight:800;font-size:1.25rem;color:var(--text);display:flex;align-items:center;gap:8px}
.logo span.dot{width:28px;height:28px;border-radius:9px;background:linear-gradient(135deg,var(--brand),var(--brand2));display:inline-block}
.logo:hover{text-decoration:none}
nav.links{display:flex;gap:6px;align-items:center}
nav.links a{color:var(--text);padding:8px 12px;border-radius:10px;font-weight:500;font-size:.95rem}
nav.links a:hover,nav.links a.active{background:var(--line);text-decoration:none}
.icon-btn{background:var(--card);border:1px solid var(--line);color:var(--text);border-radius:10px;width:40px;height:40px;cursor:pointer;font-size:1rem}
.menu-btn{display:none}
@media(max-width:820px){.menu-btn{display:inline-block}nav.links{display:none;position:absolute;left:0;right:0;top:64px;background:var(--bg);border-bottom:1px solid var(--line);flex-direction:column;align-items:stretch;padding:12px 20px}nav.links.open{display:flex}}
.hero{padding:72px 0 40px;text-align:center}
.hero h1{font-size:clamp(2rem,5vw,3.4rem);line-height:1.15;margin:0 0 16px;letter-spacing:-.02em}
.hero h1 em{font-style:normal;background:linear-gradient(135deg,var(--brand),var(--brand2));-webkit-background-clip:text;background-clip:text;color:transparent}
.hero p{color:var(--muted);max-width:640px;margin:0 auto 28px;font-size:1.1rem}
.search{max-width:560px;margin:0 auto;position:relative}
.search input{width:100%;padding:16px 20px;border-radius:14px;border:1px solid var(--line);background:var(--card);color:var(--text);font-size:1rem;box-shadow:var(--shadow);outline:none}
.search input:focus{border-color:var(--brand)}
.stats{display:flex;gap:28px;justify-content:center;flex-wrap:wrap;margin-top:28px;color:var(--muted);font-size:.95rem}
.stats b{color:var(--text);font-size:1.3rem;display:block}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:28px 0 8px}
.chip{border:1px solid var(--line);background:var(--card);color:var(--text);padding:8px 14px;border-radius:999px;cursor:pointer;font-size:.9rem}
.chip.on{background:var(--brand);color:#fff;border-color:var(--brand)}
h2.sec{font-size:1.6rem;margin:48px 0 8px}
p.lead{color:var(--muted);margin:0 0 20px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:20px;box-shadow:var(--shadow);display:flex;flex-direction:column;gap:8px;transition:transform .15s,border-color .15s;color:var(--text)}
.card:hover{transform:translateY(-3px);border-color:var(--brand);text-decoration:none}
.card h3{margin:0;font-size:1.1rem}
.card p{margin:0;color:var(--muted);font-size:.93rem}
.badge{display:inline-block;font-size:.75rem;padding:3px 10px;border-radius:999px;background:var(--line);color:var(--muted);font-weight:600;align-self:flex-start}
.badge.free{background:color-mix(in srgb,var(--ok) 15%,transparent);color:var(--ok)}
.cat-card .ico{font-size:1.8rem}
.crumbs{font-size:.88rem;color:var(--muted);padding:22px 0 0}
.crumbs a{color:var(--muted)}
.page-head{padding:12px 0 8px}
.page-head h1{font-size:clamp(1.8rem,4vw,2.6rem);margin:8px 0;line-height:1.2}
.page-head p{color:var(--muted);font-size:1.08rem;margin:0 0 16px}
.btn{display:inline-block;background:linear-gradient(135deg,var(--brand),var(--brand2));color:#fff;padding:13px 22px;border-radius:12px;font-weight:700;border:0;cursor:pointer;font-size:1rem}
.btn:hover{text-decoration:none;filter:brightness(1.07)}
.layout{display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:32px;margin-top:20px}
@media(max-width:900px){.layout{grid-template-columns:1fr}}
.panel{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:24px;margin-bottom:20px}
.panel h2{margin:0 0 10px;font-size:1.3rem}
.panel ul,.panel ol{padding-left:22px;margin:8px 0}
.panel li{margin:6px 0}
.proscons{display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media(max-width:600px){.proscons{grid-template-columns:1fr}}
.pros h3{color:var(--ok)}.cons h3{color:var(--bad)}
.proscons h3{margin:0 0 6px;font-size:1rem}
aside .panel{padding:18px}
aside h3{margin:0 0 10px;font-size:1rem}
aside ul{list-style:none;padding:0;margin:0}aside li{padding:7px 0;border-bottom:1px solid var(--line)}aside li:last-child{border:0}
.facts dt{font-size:.78rem;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;margin-top:10px}
.facts dd{margin:2px 0 0;font-weight:600}
.note{font-size:.85rem;color:var(--muted);background:var(--card);border:1px dashed var(--line);border-radius:12px;padding:12px 14px;margin:16px 0}
.prose{max-width:760px}
.prose h2{margin-top:32px}
.prose p,.prose li{font-size:1.04rem}
.ad-slot:empty{display:none}
.ad-slot{margin:24px 0;text-align:center;min-height:90px}
footer.site{margin-top:72px;border-top:1px solid var(--line);padding:40px 0 28px;color:var(--muted);font-size:.93rem}
.fgrid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:28px}
@media(max-width:760px){.fgrid{grid-template-columns:1fr 1fr}}
footer h4{color:var(--text);margin:0 0 10px}footer a{color:var(--muted);display:block;padding:3px 0}
.copy{margin-top:28px;padding-top:18px;border-top:1px solid var(--line);font-size:.85rem}
.hidden{display:none!important}
.logo-tile{position:relative;display:inline-flex;width:52px;height:52px;border-radius:14px;background:#fff;border:1px solid var(--line);box-shadow:0 4px 14px rgba(20,20,60,.12);overflow:hidden;flex:none}
.logo-tile img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;padding:9px;background:#fff}
.logo-tile b{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:1.3rem;color:#fff;background:linear-gradient(135deg,var(--c),color-mix(in srgb,var(--c) 55%,#000))}
.logo-tile.lg{width:92px;height:92px;border-radius:24px}.logo-tile.lg img{padding:16px}.logo-tile.lg b{font-size:2.2rem}
.logo-tile.sm{width:34px;height:34px;border-radius:10px}.logo-tile.sm img{padding:5px}.logo-tile.sm b{font-size:.95rem}
.card{border-top:4px solid var(--c,var(--brand));position:relative}
.card-top{display:flex;align-items:center;gap:14px}
.card-top h3{font-size:1.15rem}
.card .go{margin-top:auto;font-weight:700;font-size:.9rem;color:var(--c,var(--brand))}
.card:hover{box-shadow:0 14px 34px color-mix(in srgb,var(--c,var(--brand)) 25%,transparent)}
.cat-card .ico{width:60px;height:60px;border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:1.8rem;background:color-mix(in srgb,var(--c) 18%,transparent);margin-bottom:4px}
.hero{margin-top:22px;border-radius:30px;padding:76px 24px 52px;position:relative;overflow:hidden;background:radial-gradient(circle at 12% 18%,rgba(255,92,168,.22),transparent 38%),radial-gradient(circle at 88% 12%,rgba(0,184,217,.25),transparent 40%),radial-gradient(circle at 70% 95%,rgba(255,138,61,.18),transparent 40%),linear-gradient(135deg,rgba(91,75,255,.18),rgba(0,184,217,.10));border:1px solid var(--line)}
.pill{display:inline-block;background:var(--card);border:1px solid var(--line);border-radius:999px;padding:6px 14px;font-size:.85rem;font-weight:600;margin-bottom:18px;box-shadow:var(--shadow)}
.logo-strip{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:30px}
.logo-strip a:hover{transform:translateY(-3px);text-decoration:none}.logo-strip a{transition:transform .15s}
.tool-head{display:flex;gap:22px;align-items:center;flex-wrap:wrap;margin:10px 0 6px}
.page-head .badge{background:color-mix(in srgb,var(--c,var(--brand)) 16%,transparent);color:var(--c,var(--brand))}
.sec-head{display:flex;align-items:center;gap:12px;margin:48px 0 6px}.sec-head h2{margin:0;font-size:1.6rem}
.bar{height:6px;border-radius:6px;background:linear-gradient(90deg,var(--c,var(--brand)),var(--brand2));margin:0 0 14px;width:70px}
aside .logo-row{display:flex;align-items:center;gap:10px}
.btn{box-shadow:0 8px 20px rgba(91,75,255,.35)}

.empty{text-align:center;color:var(--muted);padding:40px 0}
form.contact{display:grid;gap:14px;max-width:560px}
form.contact input,form.contact textarea{padding:13px 14px;border-radius:12px;border:1px solid var(--line);background:var(--card);color:var(--text);font:inherit}
"""

JS = r"""
(function(){
var root=document.documentElement;
try{var t=localStorage.getItem('theme');if(t)root.setAttribute('data-theme',t);}catch(e){}
document.addEventListener('DOMContentLoaded',function(){
  var tb=document.getElementById('themeBtn');
  if(tb){tb.addEventListener('click',function(){
    var n=root.getAttribute('data-theme')==='dark'?'light':'dark';
    root.setAttribute('data-theme',n);try{localStorage.setItem('theme',n);}catch(e){}
  });}
  var mb=document.getElementById('menuBtn'),nl=document.getElementById('navLinks');
  if(mb&&nl){mb.addEventListener('click',function(){nl.classList.toggle('open');});}
  var q=document.getElementById('q'),cards=document.querySelectorAll('[data-tool]'),chips=document.querySelectorAll('.chip'),empty=document.getElementById('empty');
  if(q&&cards.length){
    var cat='all';
    function apply(){
      var term=q.value.trim().toLowerCase(),shown=0;
      cards.forEach(function(c){
        var ok=(cat==='all'||c.dataset.cat===cat)&&(!term||c.dataset.text.indexOf(term)>-1);
        c.classList.toggle('hidden',!ok);if(ok)shown++;
      });
      if(empty)empty.classList.toggle('hidden',shown>0);
    }
    q.addEventListener('input',apply);
    chips.forEach(function(ch){ch.addEventListener('click',function(){
      chips.forEach(function(x){x.classList.remove('on');});ch.classList.add('on');cat=ch.dataset.cat;apply();
    });});
  }
});
})();
"""

cats = CATEGORIES
by_slug = {t["slug"]: t for t in TOOLS}

def pre(depth):
    return "../" * depth

def head(title, desc, depth, path, extra=""):
    p = pre(depth)
    url = f"{DOMAIN}/{path}" if path else DOMAIN + "/"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta name="theme-color" content="#5b4bff">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='28' fill='%235b4bff'/%3E%3Ctext x='50' y='68' font-size='56' text-anchor='middle' fill='white' font-family='Arial' font-weight='700'%3EAI%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="{p}css/style.css">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
<!-- GOOGLE ADSENSE: paste your AdSense script here after your account is approved
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXXXXXXXXXXX" crossorigin="anonymous"></script>
-->
{extra}</head>
<body>
"""

def header(depth, active=""):
    p = pre(depth)
    def a(href, label, key):
        cls = ' class="active"' if active == key else ""
        return f'<a href="{p}{href}"{cls}>{label}</a>'
    return f"""<header class="site"><div class="wrap nav">
<a class="logo" href="{p}index.html"><span class="dot"></span>{SITE_NAME}</a>
<nav class="links" id="navLinks">
{a("index.html","Home","home")}
{a("tools.html","All Tools","tools")}
{a("guides.html","Guides","guides")}
{a("about.html","About","about")}
{a("contact.html","Contact","contact")}
</nav>
<div style="display:flex;gap:8px"><button class="icon-btn" id="themeBtn" aria-label="Toggle dark mode">◐</button><button class="icon-btn menu-btn" id="menuBtn" aria-label="Menu">☰</button></div>
</div></header>
"""

def footer(depth):
    p = pre(depth)
    cat_links = "".join(f'<a href="{p}category/{s}.html">{v[0]}</a>' for s, v in list(cats.items()))
    return f"""<footer class="site"><div class="wrap">
<div class="fgrid">
<div><h4>{SITE_NAME}</h4><p>Your guide to the best free AI tools, with simple tutorials and honest information for beginners.</p></div>
<div><h4>Categories</h4>{cat_links}</div>
<div><h4>Explore</h4><a href="{p}tools.html">All tools</a><a href="{p}guides.html">Guides</a><a href="{p}about.html">About</a><a href="{p}contact.html">Contact</a></div>
<div><h4>Legal</h4><a href="{p}privacy-policy.html">Privacy Policy</a><a href="{p}terms.html">Terms of Use</a><a href="{p}disclaimer.html">Disclaimer</a><a href="{p}sitemap.xml">Sitemap</a></div>
</div>
<div class="copy">© {YEAR} {SITE_NAME}. All tool names and logos belong to their respective owners. We are not affiliated with the tools listed. Free plans, limits and features can change, so always confirm on the official website.</div>
</div></footer>
<script src="{p}js/main.js"></script>
</body></html>
"""

def write(path, html):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)

CATCOL = {"chatbots":"#5b4bff","image":"#ff4d94","video":"#ff8a3d","audio":"#12b886","writing":"#3b82f6","productivity":"#e8a900","dev":"#8b5cf6"}
from urllib.parse import urlparse
def logo(t, cls=""):
    host = urlparse(t["url"]).netloc
    col = CATCOL[t["cat"]]
    ini = t["name"][0].upper()
    return (f'<span class="logo-tile {cls}" style="--c:{col}"><b>{ini}</b>'
            f'<img src="https://www.google.com/s2/favicons?domain={host}&sz=128" alt="{t["name"]} logo" loading="lazy" referrerpolicy="no-referrer" onerror="this.remove()"></span>')

def tool_card(t, depth):
    p = pre(depth)
    c = cats[t["cat"]]
    text = f'{t["name"]} {t["tag"]} {c[0]} {t["desc"]}'.lower().replace('"', "")
    free = "free" if "free" in t["price"].lower() else ""
    return f'''<a class="card" style="--c:{CATCOL[t["cat"]]}" data-tool data-cat="{t["cat"]}" data-text="{text}" href="{p}tools/{t["slug"]}.html">
<div class="card-top">{logo(t)}<div><h3>{t["name"]}</h3><span class="badge {free}">{t["price"]}</span></div></div><p>{t["tag"]}</p><span class="go">View details →</span></a>'''

# ---------------- CSS / JS ----------------
write("css/style.css", CSS)
write("js/main.js", JS)

urls = []

# ---------------- HOME ----------------
n_tools = len(TOOLS)
cat_cards = "".join(
    f'<a class="card cat-card" style="--c:{CATCOL[s]}" href="category/{s}.html"><span class="ico">{v[2]}</span><h3>{v[0]}</h3><p>{v[1]}</p><span class="badge">{sum(1 for t in TOOLS if t["cat"]==s)} tools</span></a>'
    for s, v in cats.items())
featured = [by_slug[s] for s in ["chatgpt","claude","canva","capcut","elevenlabs","notebooklm","perplexity","leonardo-ai"]]
feat_cards = "".join(tool_card(t, 0) for t in featured)
guide_cards = "".join(
    f'<a class="card" href="guides/{g["slug"]}.html"><span class="badge">Guide</span><h3>{g["title"]}</h3><p>{g["desc"]}</p></a>' for g in GUIDES)
h = head(f"{SITE_NAME} – Best Free AI Tools, Tutorials and Guides ({YEAR})",
         "Discover the best free AI tools for writing, images, video, audio and productivity, with simple explanations, pros and cons and official links.", 0, "")
h += header(0, "home")
h += f"""<main class="wrap">
<section class="hero"><span class="pill">✨ Updated for {YEAR} · 100% free to browse</span><h1>Find the best <em>free AI tools</em> and learn to use them</h1>
<p>Simple, honest guides to {n_tools}+ AI tools for writing, images, video, voice and more. Every tool has its own page with features, pros, cons and the official link.</p>
<div class="search"><input id="q" type="search" placeholder="Search tools, e.g. video, voice, image..." aria-label="Search tools"></div>
<div class="logo-strip">{"".join(f'<a href="tools/{x["slug"]}.html" title="{x["name"]}">{logo(x,"")}</a>' for x in [by_slug[k] for k in ["chatgpt","claude","google-gemini","perplexity","canva","capcut","elevenlabs","notebooklm","leonardo-ai","hugging-face"]])}</div>
<div class="stats"><div><b>{n_tools}+</b>AI tools</div><div><b>{len(cats)}</b>categories</div><div><b>{len(GUIDES)}</b>beginner guides</div></div>
</section>
<div id="searchResults">
<div class="chips" id="chips"><button class="chip on" data-cat="all">All</button>{"".join(f'<button class="chip" data-cat="{s}">{v[0]}</button>' for s,v in cats.items())}</div>
<div class="grid" id="toolGrid">{"".join(tool_card(t,0) for t in TOOLS)}</div>
<div class="empty hidden" id="empty">No tools match your search. Try another word.</div>
</div>
<div class="ad-slot"></div>
<h2 class="sec">Browse by category</h2><p class="lead">Pick what you want to create and see the best free tools for it.</p>
<div class="grid">{cat_cards}</div>
<h2 class="sec">Popular starting points</h2><p class="lead">Beginner friendly tools most people try first.</p>
<div class="grid">{feat_cards}</div>
<h2 class="sec">Beginner guides</h2><p class="lead">Short tutorials that help you get better results.</p>
<div class="grid">{guide_cards}</div>
</main>
"""
h += footer(0)
write("index.html", h); urls.append("")

# ---------------- ALL TOOLS ----------------
h = head(f"All Free AI Tools ({n_tools}) – {SITE_NAME}", "Browse every free AI tool in our directory with search and category filters.", 0, "tools.html")
h += header(0, "tools")
h += f"""<main class="wrap"><div class="crumbs"><a href="index.html">Home</a> › All tools</div>
<div class="page-head"><h1>All free AI tools</h1><p>Search or filter the full directory. Click any tool to read its full page.</p></div>
<div class="search" style="margin:0"><input id="q" type="search" placeholder="Search all tools..." aria-label="Search tools"></div>
<div class="chips"><button class="chip on" data-cat="all">All</button>{"".join(f'<button class="chip" data-cat="{s}">{v[0]}</button>' for s,v in cats.items())}</div>
<div class="grid">{"".join(tool_card(t,0) for t in TOOLS)}</div>
<div class="empty hidden" id="empty">No tools match your search.</div>
</main>"""
h += footer(0)
write("tools.html", h); urls.append("tools.html")

# ---------------- CATEGORY PAGES ----------------
for s, v in cats.items():
    items = [t for t in TOOLS if t["cat"] == s]
    h = head(f"Best Free {v[0]} Tools ({YEAR}) – {SITE_NAME}", f"{v[1]} Explore {len(items)} free {v[0].lower()} tools with features, pros and cons.".replace("&amp;", "and"), 1, f"category/{s}.html")
    h += header(1)
    h += f"""<main class="wrap"><div class="crumbs"><a href="../index.html">Home</a> › <a href="../tools.html">Tools</a> › {v[0]}</div>
<div class="page-head" style="--c:{CATCOL[s]}"><div class="tool-head"><span class="cat-card"><span class="ico" style="--c:{CATCOL[s]}">{v[2]}</span></span><h1 style="margin:0">{v[0]}</h1></div><div class="bar"></div><p>{v[1]}</p></div>
<div class="ad-slot"></div>
<div class="grid">{"".join(tool_card(t,1) for t in items)}</div>
<div class="note">Free plans, credit limits and features change often. Open the official website to confirm the latest details before you sign up.</div>
<h2 class="sec">Other categories</h2>
<div class="chips" style="margin-top:8px">{"".join(f'<a class="chip" href="{k}.html">{c[0]}</a>' for k,c in cats.items() if k!=s)}</div>
</main>"""
    h += footer(1)
    write(f"category/{s}.html", h); urls.append(f"category/{s}.html")

# ---------------- TOOL PAGES ----------------
for t in TOOLS:
    c = cats[t["cat"]]
    similar = [x for x in TOOLS if x["cat"] == t["cat"] and x["slug"] != t["slug"]][:5]
    sim_html = "".join(f'<li><a class="logo-row" href="{x["slug"]}.html">{logo(x,"sm")}<span>{x["name"]}</span></a></li>' for x in similar) or "<li>More tools coming soon</li>"
    feats = "".join(f"<li>{x}</li>" for x in t["features"])
    pros = "".join(f"<li>{x}</li>" for x in t["pros"])
    cons = "".join(f"<li>{x}</li>" for x in t["cons"])
    steps = "".join(f"<li>{x}</li>" for x in t["steps"])
    ld = json.dumps({"@context": "https://schema.org", "@type": "SoftwareApplication", "name": t["name"],
                     "applicationCategory": "AI tool", "description": t["tag"], "url": t["url"]})
    extra = f'<script type="application/ld+json">{ld}</script>\n'
    h = head(f"{t['name']} Review: Free Plan, Features, Pros and Cons ({YEAR}) – {SITE_NAME}",
             f"{t['name']}: {t['tag']} Learn what it does, who it is best for and how to start for free.", 1, f"tools/{t['slug']}.html", extra)
    h += header(1)
    h += f"""<main class="wrap"><div class="crumbs"><a href="../index.html">Home</a> › <a href="../category/{t['cat']}.html">{c[0]}</a> › {t['name']}</div>
<div class="page-head" style="--c:{CATCOL[t['cat']]}"><div class="tool-head">{logo(t,"lg")}<div><span class="badge">{c[0]}</span><h1 style="margin:6px 0 0">{t['name']}</h1></div></div><div class="bar"></div><p>{t['tag']}</p>
<a class="btn" href="{t['url']}" target="_blank" rel="noopener noreferrer nofollow">Visit official website →</a></div>
<div class="layout"><article>
<div class="panel"><h2>What is {t['name']}?</h2><p>{t['desc']}</p></div>
<div class="ad-slot"></div>
<div class="panel"><h2>Key features</h2><ul>{feats}</ul></div>
<div class="panel"><h2>Who is it best for?</h2><p>{t['best']}</p></div>
<div class="panel proscons"><div class="pros"><h3>👍 Pros</h3><ul>{pros}</ul></div><div class="cons"><h3>👎 Cons</h3><ul>{cons}</ul></div></div>
<div class="panel"><h2>How to get started</h2><ol>{steps}</ol></div>
<div class="note">Plans, free limits and features can change at any time. Confirm current details on the <a href="{t['url']}" target="_blank" rel="noopener noreferrer nofollow">official {t['name']} website</a>.</div>
</article>
<aside>
<div class="panel"><h3>Quick facts</h3><dl class="facts"><dt>Category</dt><dd>{c[0]}</dd><dt>Pricing</dt><dd>{t['price']}</dd><dt>Official site</dt><dd><a href="{t['url']}" target="_blank" rel="noopener noreferrer nofollow">Open website</a></dd></dl></div>
<div class="panel"><h3>Similar tools</h3><ul>{sim_html}</ul></div>
<div class="panel"><h3>Learn more</h3><ul><li><a href="../guides/how-to-write-better-ai-prompts.html">How to write better prompts</a></li><li><a href="../guides/using-ai-tools-safely.html">Using AI tools safely</a></li></ul></div>
<div class="ad-slot"></div>
</aside></div></main>"""
    h += footer(1)
    write(f"tools/{t['slug']}.html", h); urls.append(f"tools/{t['slug']}.html")

# ---------------- GUIDES ----------------
h = head(f"AI Tool Guides for Beginners – {SITE_NAME}", "Beginner friendly guides on prompts, choosing tools, free vs paid plans and safe AI use.", 0, "guides.html")
h += header(0, "guides")
h += f"""<main class="wrap"><div class="crumbs"><a href="index.html">Home</a> › Guides</div>
<div class="page-head"><h1>Beginner guides</h1><p>Short, practical tutorials to help you get more from AI tools.</p></div>
<div class="grid">{"".join(f'<a class="card" href="guides/{g["slug"]}.html"><span class="badge">Guide</span><h3>{g["title"]}</h3><p>{g["desc"]}</p></a>' for g in GUIDES)}</div></main>"""
h += footer(0)
write("guides.html", h); urls.append("guides.html")

for g in GUIDES:
    body = ""
    for kind, val in g["body"]:
        if kind == "h2": body += f"<h2>{val}</h2>"
        elif kind == "p": body += f"<p>{val}</p>"
        elif kind == "ul": body += "<ul>" + "".join(f"<li>{x}</li>" for x in val) + "</ul>"
    h = head(f"{g['title']} – {SITE_NAME}", g["desc"], 1, f"guides/{g['slug']}.html")
    h += header(1, "guides")
    h += f"""<main class="wrap"><div class="crumbs"><a href="../index.html">Home</a> › <a href="../guides.html">Guides</a> › {g['title']}</div>
<div class="page-head"><h1>{g['title']}</h1><p>{g['desc']}</p></div>
<div class="layout"><article class="prose panel">{body}<div class="ad-slot"></div></article>
<aside><div class="panel"><h3>Popular tools</h3><ul>
<li><a href="../tools/chatgpt.html">ChatGPT</a></li><li><a href="../tools/claude.html">Claude</a></li><li><a href="../tools/canva.html">Canva</a></li><li><a href="../tools/capcut.html">CapCut</a></li><li><a href="../tools/notebooklm.html">NotebookLM</a></li></ul></div>
<div class="panel"><h3>More guides</h3><ul>{"".join(f'<li><a href="{x["slug"]}.html">{x["title"]}</a></li>' for x in GUIDES if x["slug"]!=g["slug"])}</ul></div></aside></div></main>"""
    h += footer(1)
    write(f"guides/{g['slug']}.html", h); urls.append(f"guides/{g['slug']}.html")

# ---------------- STATIC PAGES ----------------
def simple(path, title, desc, inner, active=""):
    h = head(f"{title} – {SITE_NAME}", desc, 0, path)
    h += header(0, active)
    h += f"""<main class="wrap"><div class="crumbs"><a href="index.html">Home</a> › {title}</div>
<div class="page-head"><h1>{title}</h1></div><div class="panel prose">{inner}</div></main>"""
    h += footer(0)
    write(path, h); urls.append(path)

simple("about.html", "About Us", f"About {SITE_NAME} and how we review free AI tools.", f"""
<p>{SITE_NAME} is an independent website that helps beginners discover and understand free AI tools. AI tools appear every week, and it is hard to know which ones are worth your time. We collect them in one place and explain them in simple language.</p>
<h2>What you will find here</h2>
<ul><li>A directory of AI tools sorted by what you want to do</li><li>A page for each tool with features, pros, cons and getting started steps</li><li>Beginner guides on prompts, choosing tools and using AI safely</li><li>Direct links to the official website of every tool</li></ul>
<h2>How we choose tools</h2>
<p>We look for tools that have a free plan or free trial, a clear purpose, and an active official website. We explain what a tool does in our own words and we try to mention limits honestly.</p>
<h2>Our promise</h2>
<p>We aim to keep information accurate, but AI products change quickly. Prices, limits and features may be different by the time you visit, so please confirm details on the official site. If you notice something outdated, <a href="contact.html">tell us</a> and we will fix it.</p>
""", "about")

simple("contact.html", "Contact Us", f"Contact {SITE_NAME} for corrections, suggestions or business enquiries.", f"""
<p>Have a tool suggestion, a correction, or a question? We would love to hear from you.</p>
<p>Email: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
<form class="contact" action="mailto:{CONTACT_EMAIL}" method="post" enctype="text/plain">
<input name="name" placeholder="Your name" required><input name="email" type="email" placeholder="Your email" required>
<textarea name="message" rows="5" placeholder="Your message" required></textarea>
<button class="btn" type="submit">Send message</button></form>
<p class="note">This form opens your email app. We usually reply within a few days.</p>
""", "contact")

simple("privacy-policy.html", "Privacy Policy", f"Privacy Policy for {SITE_NAME}.", f"""
<p><em>Last updated: {YEAR}</em></p>
<p>This Privacy Policy explains how {SITE_NAME} ("we", "our") handles information when you visit our website.</p>
<h2>Information we collect</h2>
<p>We do not require you to create an account. We may collect non-personal information such as browser type, device type, pages visited and approximate location through analytics and advertising services.</p>
<h2>Cookies</h2>
<p>We and our partners use cookies to improve the website, remember settings such as dark mode, measure traffic and show advertising. You can control or delete cookies in your browser settings.</p>
<h2>Advertising</h2>
<p>We may use Google AdSense or other advertising partners. Third party vendors, including Google, use cookies to serve ads based on your previous visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visit to our site and other sites on the internet. You can opt out of personalised advertising by visiting Google Ads Settings.</p>
<h2>External links</h2>
<p>Our pages link to the official websites of AI tools. We are not responsible for the content or privacy practices of other websites.</p>
<h2>Children</h2>
<p>This website is not directed to children under 13 and we do not knowingly collect their personal information.</p>
<h2>Your choices</h2>
<p>Depending on where you live, you may have rights to access or delete personal data. Contact us at <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a> with any request.</p>
<h2>Changes</h2>
<p>We may update this policy from time to time. The latest version will always be on this page.</p>
""")

simple("terms.html", "Terms of Use", f"Terms of Use for {SITE_NAME}.", f"""
<p><em>Last updated: {YEAR}</em></p>
<p>By using {SITE_NAME} you agree to these terms.</p>
<h2>Use of content</h2>
<p>Content on this website is for general information. You may read and share links to our pages, but you may not copy large parts of our content without permission.</p>
<h2>Third party tools</h2>
<p>We list tools owned by other companies. We do not own or control them. Your use of any tool is governed by that tool's own terms and privacy policy.</p>
<h2>No guarantees</h2>
<p>We try to keep information correct and current, but we do not guarantee accuracy, availability, pricing or features of any listed tool.</p>
<h2>Limitation of liability</h2>
<p>We are not liable for any loss or damage resulting from the use of this website or any tool mentioned on it.</p>
<h2>Contact</h2>
<p>Questions about these terms? Email <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>
""")

simple("disclaimer.html", "Disclaimer", f"Disclaimer for {SITE_NAME}.", f"""
<p>The information on {SITE_NAME} is provided for general informational purposes only. We are not affiliated with, endorsed by, or sponsored by any of the AI tools or companies mentioned.</p>
<h2>Accuracy</h2>
<p>AI products change quickly. Pricing, free limits and features may change without notice. Always confirm details on the official website.</p>
<h2>No professional advice</h2>
<p>Nothing on this website is legal, financial, medical or professional advice.</p>
<h2>Trademarks</h2>
<p>All product names, logos and brands are the property of their respective owners and are used here only for identification.</p>
<h2>Advertising</h2>
<p>This website may display advertisements. Some links may become affiliate links in the future, and if so we will clearly say so.</p>
""")

# 404
h = head(f"Page not found – {SITE_NAME}", "Page not found", 0, "404.html")
h += header(0)
h += """<main class="wrap"><div class="hero"><h1>404 – page not found</h1><p>The page you are looking for does not exist.</p><a class="btn" href="/index.html">Go to homepage</a></div></main>"""
h += footer(0)
write("404.html", h)

# sitemap, robots, ads.txt, vercel
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for u in urls:
    sm += f"  <url><loc>{DOMAIN}/{u}</loc></url>\n"
sm += "</urlset>\n"
write("sitemap.xml", sm)
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
write("ads.txt", "# After AdSense approval, replace this line with the one Google gives you, for example:\n# google.com, pub-XXXXXXXXXXXXXXXX, DIRECT, f08c47fec0942fa0\n")
write("vercel.json", json.dumps({"cleanUrls": False, "trailingSlash": False}, indent=2) + "\n")
write("README.txt", f"""{SITE_NAME} – static website (HTML, CSS, JS only)

HOW TO PUBLISH (free)
1. Upload this whole folder to GitHub and import it in Vercel (or Netlify / Cloudflare Pages). No build command needed.
2. Open index.html locally to preview: all links are relative so it works offline too.

BEFORE YOU GO LIVE – CHANGE THESE
- Site name, domain and email: edit SITE_NAME, DOMAIN, CONTACT_EMAIL in gen/data.py, then run: python3 gen/build.py ./site
  (or find/replace "{DOMAIN}" and "{CONTACT_EMAIL}" in all files)
- Check that each tool's free plan details are still correct on its official site.

ADSENSE
- Apply only after the site is live on your own domain with real content.
- Paste your AdSense script in the commented block in the <head> of every page (find/replace "GOOGLE ADSENSE").
- Put the ads.txt line from Google into ads.txt.
- Empty <div class="ad-slot"></div> elements mark where ads can go. They stay hidden until filled.
- Never click your own ads.

ADDING A NEW TOOL
- Add one entry to the TOOLS list in gen/data.py, run python3 gen/build.py ./site, upload again.
""")

print("pages:", len(urls) + 1, "tools:", len(TOOLS))
