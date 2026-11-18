#!/usr/bin/env python3
# Builds variant-a..e.html + board index.html for the generic Akihabara welcome page.
import pathlib
W = pathlib.Path(__file__).parent

PIN = '<svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z" fill="#fff"/></svg>'
def CLOCK(c): return f'<svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><circle cx="8" cy="8" r="6.5" fill="none" stroke="{c}" stroke-width="2"/><path d="M8 4.5V8l2.5 1.8" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"/></svg>'
MAP_MEET = "https://www.google.com/maps/search/?api=1&amp;query=Vie+de+France+BiTO+AKIBA+PLAZA"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLScm_VkR8xnl5CxdyTR0NYIED2mp-mLKmR5w8jNWIkxk82U8Uw/viewform"

PLACES = [
 # no, genre, name, hours, img, alt, maps query, text, tile tag
 ("01","Figures, cards, hobby shops","RADIO KAIKAN","10:00&ndash;20:00","img/radio-kaikan.jpg","Akihabara Radio Kaikan building","Akihabara+Radio+Kaikan",
  "The ten-floor landmark right outside the Electric Town exit. Floors of figures, trading cards, dolls and model kits &mdash; if it exists in Akihabara, it is probably somewhere in this building.","The landmark tower"),
 ("02","Second-hand manga &amp; toys","MANDARAKE COMPLEX","12:00&ndash;20:00","img/mandarake.jpg","Mandarake Complex building in Akihabara","Mandarake+Complex+Akihabara",
  "Eight floors of pre-owned manga, doujinshi, toys, animation cels and cards. This is the place to hunt for the rare thing that sold out everywhere else years ago.","Second-hand treasures"),
 ("03","New releases &amp; goods","ANIMATE AKIHABARA","10:00&ndash;21:00","img/animate.jpg","Animate Akihabara building","Animate+Akihabara",
  "Animate&rsquo;s Akihabara flagship, renewed in 2026: new manga, anime discs, music and character goods across two buildings, with event floors for whatever is airing now.","New &amp; official goods"),
 ("04","Game centre","SILK HAT AKIHABARA","10:00&ndash;24:00","img/gigo.jpg","The big red arcade building by Akihabara Station","SILK+HAT+Akihabara",
  "The famous red arcade tower right by the station &mdash; crane games, rhythm games and fighters over eight floors. It was SEGA, then GiGO, for over thirty years; GiGO&rsquo;s other Akihabara buildings are a short walk away.","The big red arcade"),
 ("05","Retro games","SUPER POTATO","11:00&ndash;20:00","img/potato.jpg","Super Potato retro game shop, Akihabara","Super+Potato+Akihabara",
  "Three floors of Famicom, Mega Drive and PlayStation history, with a retro arcade corner on the top floor. Pure nostalgia &mdash; and nearly all of it is playable and buyable.","Retro game heaven"),
 ("06","Capsule toys","AKIHABARA GACHAPON KAIKAN","11:00&ndash;20:00","img/gashapon.jpg","Rows of gashapon capsule machines in Akihabara","Akihabara+Gachapon+Kaikan",
  "Around 500 capsule machines packed into one narrow shop, with new series landing every month (Sundays it closes at 19:00). Bring 100-yen coins &mdash; you will want more than one try.","500 capsule machines"),
]

# Final page (index.html) line-up, decided 2026-11-18: 04-06 swapped to BOOK OFF / namco / Trader.
FINAL_PLACES = [
 # Card 01 uses the un-mosaicked Stephen Kelly night shot on the final page only;
 # PLACES[0] (John Seb Barber "ed" derivative, billboard pixelated on Commons) stays for variants A-E.
 ("01","Figures, cards, hobby shops","RADIO KAIKAN","10:00&ndash;20:00","img/radio-kaikan-night.jpg","Akihabara Radio Kaikan building","Akihabara+Radio+Kaikan",
  "The ten-floor landmark right outside the Electric Town exit. Floors of figures, trading cards, dolls and model kits &mdash; if it exists in Akihabara, it is probably somewhere in this building.","The landmark tower"),
 PLACES[1], PLACES[2],
 ("04","Second-hand books, games &amp; cards","BOOKOFF AKIHABARA EKIMAE","10:00&ndash;22:00","img/bookoff.jpg","Inside BOOK OFF Akihabara Ekimae, shelves of second-hand CDs","BOOKOFF+Akihabara+Ekimae",
  "A big second-hand store one minute from the station, with used manga, games, CDs, DVDs and trading cards across several floors.","Second-hand everything"),
 ("05","Game centre","NAMCO AKIHABARA","10:00&ndash;23:00","img/namco-akiba.jpg","The namco Akihabara building at night, with its big red sign","namco+Akihabara",
  "Bandai Namco&rsquo;s own game centre, one minute from the Electric Town exit: crane games and gashapon floors, plus the official Ichibankuji and Bandai card game shops.","Bandai Namco's arcade"),
 ("06","Second-hand games &amp; figures","TRADER AKIHABARA","11:00&ndash;20:00","img/trader-figures.jpg","Shelves of second-hand anime figures in an Akihabara shop","Trader+Akihabara",
  "A Chuo-dori institution for used games: floor after floor of pre-owned and retro games, with whole floors of figures too.","Used games institution"),
]

def tiles(idxs, red_first=False):
    out=[]
    for i in idxs:
        no,genre,name,hrs,img,alt,q,tx,tag = PLACES[i]
        cls = ' class="tile r"' if (red_first and i==idxs[0]) else ' class="tile"'
        out.append(f'<a{cls} href="#p{i+1}"><img src="{img}" alt="" loading="lazy"><b class="no">{no}</b><span class="tt">{tag}</span><span class="tn">{name}</span></a>')
    return "".join(out)

def cards(clock_color):
    out=[]
    for i,(no,genre,name,hrs,img,alt,q,tx,tag) in enumerate(PLACES):
        r = ' r' if i%2==0 else ''
        out.append(f'''<article class="card{r}" id="p{i+1}"><div class="hd"><span class="big">{no}</span><div><span class="genre">{genre}</span><div class="nm"><h3>{name}</h3><span class="hrs2">{CLOCK(clock_color)}{hrs}</span></div></div></div><div class="phw"><img class="ph" src="{img}" alt="{alt}" loading="lazy"><a class="mapbtn" href="https://www.google.com/maps/search/?api=1&amp;query={q}" target="_blank" rel="noopener" aria-label="Open {name} in Google Maps">{PIN}</a></div><p class="tx">{tx}</p></article>''')
    return "\n".join(out)

BODY = """<div class="col"><div class="top"><span>GUEST GUIDE</span><span>AKIHABARA &middot; 6 PLACES</span></div>
<h1>Your <em>Akihabara</em> Anime Tour</h1></div>
<div class="col" style="padding:0"><div class="hero"><div class="hero3"><img src="img/street-day.jpg" alt="Akihabara's Chuo-dori street in the daytime"><img src="img/street-night.jpg" alt="Akihabara at night, neon signs"><img src="img/alley.jpg" alt="A back alley in Akihabara with small shops"></div></div>
<div class="hb"><span>About 4 hours &middot; flexible</span><b>Meet at VIE DE FRANCE, BiTO AKIBA 1F</b></div></div>
<div class="col"><div class="facts"><div><b>Guide</b><span>Yuuki &mdash; a local otaku guide</span></div><div><b>Meet</b><span>VIE DE FRANCE bakery caf&eacute;, BiTO AKIBA building 1F, inside the caf&eacute;</span></div><div><b>Time</b><span>About 4 hours, flexible</span></div><div><b>Style</b><span>Private tour, built around your favourite series</span></div></div>
<article class="card meet" id="meet"><div class="hd"><div><span class="genre">Meeting point</span><div class="nm"><h3>VIE DE FRANCE &mdash; BiTO AKIBA PLAZA</h3></div></div></div>
<div class="wall w1"><div class="tile"><img src="img/station-exit.jpg" alt="The Electric Town exit of JR Akihabara Station" loading="lazy"><span class="tt">Start here: the Electric Town exit</span></div></div>
<p class="tx" style="margin-top:14px"><b>How to find it:</b> come out of JR Akihabara Station at the <b>Electric Town exit</b> &mdash; the caf&eacute; is about <b>1 minute</b> away, on the 1st floor of the BiTO AKIBA building. Please come inside the caf&eacute; and look for me there. <b>There is another Vie de France nearby</b>, so please check the map.</p>
<div class="bt"><a class="btn" href="__MAP_MEET__" target="_blank" rel="noopener">Open in Google Maps</a></div></article>
<section><div class="bar r"><h2>THE BIG THREE</h2><span>1&ndash;3</span></div><div class="wall w3">__TILES_A__</div></section>
<section><div class="bar"><h2>PLAY &amp; TREASURES</h2><span>4&ndash;6</span></div><div class="wall w3">__TILES_B__</div></section>
__CARDS__
</div>
<div class="cta"><div class="col"><h2>TELL ME WHAT YOU LOVE</h2><p>The tour is built around your favourite series. Tell me what you love, what you are hunting for, and anything you especially want to see &mdash; it takes about three minutes, and it makes the day yours.</p><div class="bt"><a class="btn big" href="__FORM__" target="_blank" rel="noopener">Open the questionnaire</a></div></div></div>
<div class="know"><div class="col"><h2>GOOD TO KNOW</h2><ul><li><b>No fixed route.</b> We choose the shops together on the day, around what you love.</li><li><b>Bring some cash</b> &mdash; 100-yen coins especially. Game centres and gashapon machines are coin-hungry, and some small shops are cash only.</li><li><b>Photos:</b> I take photos during the tour and share an album with you afterwards.</li><li><b>Questions before the day?</b> Message me on WhatsApp: <b>+81 90 4494 1989</b>.</li></ul></div></div>
<details class="crd"><summary>Photo credits and sources</summary><p class="cr">Photos via Wikimedia Commons: Akihabara street (day) by Nickdrj (public domain); Akihabara at night by ElHeineken (CC BY 4.0); Akihabara alley by Nir Yaniv (CC BY-SA 4.0); JR Akihabara Station Electric Town exit by Matthide127 (CC0); Radio Kaikan by John Seb Barber (CC BY 4.0); Mandarake Complex by &#27491;&#21644; (CC BY-SA 3.0); Animate Akihabara by Dick Thomas Johnson (CC BY 2.0); the red arcade building (now Silk Hat, formerly SEGA/GiGO) by Tokumeigakarinoaoshima (CC BY-SA 4.0); Super Potato by iqremix (CC BY-SA 2.0); gashapon shop by Ubahnverleih (CC0). Opening hours checked against the shops&rsquo; official sites on 18 November 2026. Hours can change; we will confirm together on the day.</p></details>"""

def body(clock_color):
    b = BODY.replace("__MAP_MEET__", MAP_MEET).replace("__FORM__", FORM)
    b = b.replace("__TILES_A__", tiles([0,1,2], red_first=True)).replace("__TILES_B__", tiles([3,4,5]))
    b = b.replace("__CARDS__", cards(clock_color))
    return b

HEAD = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>Your Akihabara Anime Tour</title><meta name="robots" content="noindex,nofollow">
<meta name="description" content="Welcome to your private Akihabara anime tour with Yuuki: where we meet, the shops we can explore, and a short questionnaire so the day is built around your favourite series.">
<meta property="og:title" content="Your Akihabara Anime Tour"><meta property="og:description" content="Where we meet, the places we can explore, and a short questionnaire before your tour."><meta property="og:image" content="https://yukitchy.github.io/akiba-tour-welcome/og.jpg"><meta property="og:url" content="https://yukitchy.github.io/akiba-tour-welcome/">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 64 64%22%3E%3Crect width=%2264%22 height=%2264%22 fill=%22__ACC__%22/%3E%3C/svg%3E">
__FONTS__
<style>__CSS__</style></head><body>__BODY__</body></html>"""

FONT_ARCHIVO = '<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Noto+Sans+JP:wght@500;700;900&display=swap" rel="stylesheet">'
FONT_E = '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;700;900&family=VT323&family=Noto+Sans+JP:wght@500;700&display=swap" rel="stylesheet">'

BASE = """
*{box-sizing:border-box}html{scroll-behavior:smooth}
.col{max-width:640px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
h1,h2,h3,.big,.tn,.no{letter-spacing:-.01em;text-transform:uppercase}
.top{display:flex;justify-content:space-between;font-weight:800;font-size:13px;letter-spacing:.14em;padding:18px 0 8px}
h1{white-space:nowrap}
.hero3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:3px}.hero3 img{width:100%;height:100%;object-fit:cover;aspect-ratio:4/5}
.facts div{display:flex;gap:12px;padding:9px 0;font-size:15px}.facts b{flex:none;width:58px;font-size:12px;letter-spacing:.1em;text-transform:uppercase;padding-top:3px}.facts span{font-weight:700}
.hb{display:flex;justify-content:space-between;flex-wrap:wrap;gap:2px 14px;padding:14px 16px;font-weight:800;font-size:14px;letter-spacing:.06em;text-transform:uppercase}
.bar{display:flex;justify-content:space-between;align-items:baseline;margin:34px 0 10px}.bar h2{margin:0;font-size:29px}.bar span{font-weight:800;font-size:15px}
.wall{display:grid;gap:3px}.wall.w3{grid-template-columns:repeat(3,1fr)}.wall.w1 .tile{grid-column:1/-1;aspect-ratio:2.4/1}
.tile{position:relative;display:block;aspect-ratio:1/1;overflow:hidden;color:#fff;text-decoration:none;background:#222}
.tile img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.tile:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.85))}
.no{position:absolute;left:0;top:0;z-index:2;padding:3px 9px;font-size:26px;line-height:1.1}
.tt{position:absolute;left:8px;right:8px;bottom:28px;z-index:2;width:max-content;max-width:calc(100% - 16px);font-size:12px;font-weight:900;letter-spacing:.05em;text-transform:uppercase;padding:5px 7px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.tn{position:absolute;left:8px;right:8px;bottom:8px;z-index:2;font-size:13px;line-height:1.05;font-weight:800;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.card{padding:22px 0 24px;scroll-margin-top:8px}
.hd{display:flex;gap:12px;align-items:center;margin-bottom:10px}.big{font-size:70px;line-height:.85}
.hd h3{margin:6px 0 0;font-size:21px;line-height:1.05}
.genre{display:inline-block;font-size:13px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;padding:6px 9px}
.ph{display:block;width:100%;aspect-ratio:16/10;object-fit:cover}
.nm{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}.nm h3{flex:1;min-width:0}
.hrs2{flex:none;display:flex;align-items:center;gap:5px;font-size:13px;font-weight:800;letter-spacing:.02em;padding-top:6px;white-space:nowrap}
.phw{position:relative}.mapbtn{position:absolute;top:10px;right:10px;width:46px;height:46px;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,.35);z-index:2}
.tx{margin:12px 0 10px;font-size:16px}
.bt{display:flex;gap:6px;margin-top:10px}.bt>*{flex:1 1 0;min-width:0}
.btn{display:flex;align-items:center;justify-content:center;gap:6px;min-height:48px;padding:0 10px;text-decoration:none;font-weight:800;font-size:14px;letter-spacing:.05em;text-transform:uppercase;text-align:center}
.know{margin-top:34px;padding:30px 0 34px}.know h2{margin:0 0 10px;font-size:32px}.know ul{margin:0;padding-left:20px}.know li{margin:9px 0}
.cta{margin-top:34px;padding:30px 0 34px}.cta h2{margin:0 0 10px;font-size:32px}.cta p{margin:0 0 8px;font-size:16px}
.crd{max-width:640px;margin:0 auto;padding:18px 16px 44px}.crd summary{cursor:pointer;font-weight:800;font-size:13px;letter-spacing:.1em;text-transform:uppercase;padding:10px 0}.crd summary::-webkit-details-marker{display:none}.crd summary:before{content:"+ "}
.cr{padding:8px 0 0;font-size:13px;line-height:1.6}
@media(min-width:700px){.col,.crd{max-width:760px}}
"""

CSS_A = BASE + """
:root{--bg:#F1EFEA;--ink:#121212;--red:#D9342B;--mu:#5D5A54}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 Archivo,"Noto Sans JP",sans-serif}
h1,h2,h3,.big,.tn,.no{font-family:Archivo,"Noto Sans JP",sans-serif;font-stretch:62%;font-weight:900}
.top{border-bottom:4px solid var(--ink)}
h1{margin:14px 0;font-size:min(8.4vw,58px);line-height:.95}h1 em{font-style:normal;color:var(--red)}
.facts{margin:18px 0 4px;border-top:4px solid var(--ink)}.facts div{border-bottom:1px solid #c9c5bc}.facts b{color:var(--red)}
.hb{background:var(--ink);color:#fff}.hb b{color:#FF7A6E}
.bar.r h2{color:var(--red)}
.no{background:var(--ink)}.tile.r .no{background:var(--red)}
.tt{background:var(--red);color:#fff}.tile.r .tt{background:#fff;color:var(--ink)}
.card{border-bottom:4px solid var(--ink)}.card.meet{border-bottom:4px solid var(--ink)}
.big{color:var(--red)}.card.r .big{color:var(--ink)}
.genre{background:var(--red);color:#fff}.card.r .genre{background:var(--ink)}
.mapbtn{background:var(--ink)}
.btn{background:var(--ink);color:#fff;font-family:Archivo,sans-serif}
.cta{background:var(--red);color:#fff}.cta .btn{background:#fff;color:var(--ink)}
.know{background:var(--ink);color:#fff}.know h2{color:#fff}
.crd summary{color:var(--mu)}.cr{color:var(--mu)}
"""

CSS_B = BASE + """
:root{--bg:#060913;--ink:#EAF2FF;--pink:#FF3EA5;--cyan:#22D3EE;--mu:#93A4C4}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 Archivo,"Noto Sans JP",sans-serif;color-scheme:dark}
h1,h2,h3,.big,.tn,.no{font-family:Archivo,"Noto Sans JP",sans-serif;font-stretch:62%;font-weight:900}
.top{border-bottom:2px solid var(--cyan);color:var(--cyan)}
h1{margin:16px 0;font-size:min(8.4vw,58px);line-height:.95;text-shadow:0 0 18px rgba(34,211,238,.45)}h1 em{font-style:normal;color:var(--pink);text-shadow:0 0 18px rgba(255,62,165,.6)}
.facts{margin:18px 0 4px;border-top:2px solid var(--cyan)}.facts div{border-bottom:1px solid #1E2A4A}.facts b{color:var(--cyan)}
.hb{background:#0B1030;color:#fff;border-top:1px solid var(--pink);border-bottom:1px solid var(--pink)}.hb b{color:var(--pink)}
.bar h2{color:#fff}.bar.r h2{color:var(--pink)}.bar span{color:var(--cyan)}
.no{background:var(--cyan);color:#04121A}.tile.r .no{background:var(--pink);color:#1A0412}
.tt{background:var(--pink);color:#fff}.tile.r .tt{background:var(--cyan);color:#04121A}
.card{border-bottom:2px solid #1E2A4A}
.big{color:var(--cyan)}.card.r .big{color:var(--pink)}
.genre{background:var(--pink);color:#fff}.card.r .genre{background:var(--cyan);color:#04121A}
.mapbtn{background:var(--pink)}
.hrs2{color:var(--cyan)}
.btn{background:var(--cyan);color:#04121A;font-family:Archivo,sans-serif}
.cta{background:#0B1030;border-top:2px solid var(--pink);border-bottom:2px solid var(--pink);color:#fff}.cta .btn{background:var(--pink);color:#fff}
.know{background:#0B1030;color:#EAF2FF}.know h2{color:var(--cyan)}
.crd summary{color:var(--mu)}.cr{color:var(--mu)}
.tx{color:#D7E3F8}
"""

CSS_C = BASE + """
:root{--bg:#FFFFFF;--ink:#141414;--red:#E60012;--blue:#005BAC;--yel:#FFD900;--mu:#5A5A5A}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 Archivo,"Noto Sans JP",sans-serif}
h1,h2,h3,.big,.tn,.no{font-family:Archivo,"Noto Sans JP",sans-serif;font-stretch:62%;font-weight:900}
.top{border-bottom:5px solid var(--ink)}
h1{margin:14px 0;font-size:min(8.4vw,58px);line-height:.95}h1 em{font-style:normal;color:var(--red)}
.facts{margin:18px 0 4px;border-top:5px solid var(--ink)}.facts div{border-bottom:2px dotted #B9B9B9}.facts b{color:var(--blue)}
.hb{background:var(--yel);color:var(--ink);background-image:radial-gradient(rgba(20,20,20,.16) 1.6px,transparent 1.7px);background-size:11px 11px;border-top:3px solid var(--ink);border-bottom:3px solid var(--ink)}.hb b{color:var(--red)}
.bar h2{background:var(--ink);color:#fff;padding:4px 10px;box-shadow:5px 5px 0 var(--red)}.bar.r h2{box-shadow:5px 5px 0 var(--blue)}.bar span{color:var(--red)}
.no{background:var(--blue);color:#fff;border:2px solid #fff}.tile.r .no{background:var(--red)}
.tt{background:#fff;color:var(--ink);border:2.5px solid var(--ink);border-radius:14px;box-shadow:3px 3px 0 var(--ink)}.tile.r .tt{background:var(--yel)}
.card{border-bottom:3px solid var(--ink)}
.big{color:var(--red)}.card.r .big{color:var(--blue)}
.genre{background:#fff;color:var(--ink);border:2.5px solid var(--ink);border-radius:14px;box-shadow:3px 3px 0 var(--ink)}
.mapbtn{background:var(--red);border:2.5px solid #fff}
.btn{background:var(--red);color:#fff;border:3px solid var(--ink);box-shadow:4px 4px 0 var(--ink);font-family:Archivo,sans-serif}
.cta{background:#fff;background-image:radial-gradient(rgba(0,91,172,.14) 1.6px,transparent 1.7px);background-size:12px 12px;border-top:5px solid var(--ink);border-bottom:5px solid var(--ink)}.cta .btn{background:var(--blue)}
.know{background:var(--ink);color:#fff}.know h2{color:var(--yel)}
.crd summary{color:var(--mu)}.cr{color:var(--mu)}
"""

CSS_D = BASE + """
:root{--bg:#FAFAF7;--ink:#1C1C1A;--acc:#C8102E;--mu:#6E6E68;--line:#E3E3DC}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 Archivo,"Noto Sans JP",sans-serif;font-weight:400}
h1,h2,h3,.big,.tn,.no{font-family:Archivo,"Noto Sans JP",sans-serif;font-stretch:100%;letter-spacing:.01em}
h1{font-weight:800;font-size:min(7.0vw,46px);line-height:1.05;margin:22px 0 18px}h1 em{font-style:normal;color:var(--acc)}
h2{font-weight:800}h3{font-weight:800}
.top{border-bottom:1px solid var(--line);font-weight:700;color:var(--mu)}
.facts{margin:26px 0 6px;border-top:1px solid var(--line)}.facts div{border-bottom:1px solid var(--line);padding:12px 0}.facts b{color:var(--acc);font-weight:700}
.hb{background:#fff;color:var(--ink);border:1px solid var(--line);font-weight:700}.hb b{color:var(--acc)}
.bar{margin:44px 0 14px}.bar h2{font-size:24px}.bar span{color:var(--mu)}
.no{background:rgba(255,255,255,.92);color:var(--ink);font-size:20px;font-weight:800}
.tt{background:rgba(255,255,255,.92);color:var(--ink);font-weight:800}
.card{border-bottom:1px solid var(--line);padding:30px 0 34px}
.big{font-size:44px;color:var(--acc);font-weight:800}.card.r .big{color:var(--ink)}
.genre{background:transparent;color:var(--acc);padding:0;font-weight:700;letter-spacing:.14em}
.mapbtn{background:var(--acc)}
.hrs2{color:var(--mu);font-weight:700}
.btn{background:var(--acc);color:#fff;font-weight:700;border-radius:2px}
.cta{background:#F1F1EC;margin-top:44px}.cta .btn{background:var(--ink)}
.know{background:#F1F1EC;color:var(--ink);margin-top:0}.know h2{color:var(--ink)}
.crd summary{color:var(--mu)}.cr{color:var(--mu)}
.tile:after{background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.55))}
"""

CSS_E = BASE + """
:root{--bg:#0B0B0B;--ink:#F2F2F2;--amb:#FFB000;--grn:#33FF66;--mu:#9A9A8E}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 Archivo,"Noto Sans JP",sans-serif;color-scheme:dark}
h1,h2,.big,.no{font-family:"VT323",monospace;text-transform:uppercase;letter-spacing:.02em}
h3,.tn{font-family:Archivo,"Noto Sans JP",sans-serif;font-weight:900}
.top{border-bottom:3px dashed var(--amb);color:var(--amb)}
h1{margin:12px 0;font-size:min(7.2vw,54px);line-height:.9;font-weight:400}h1 em{font-style:normal;color:var(--grn)}
.facts{margin:18px 0 4px;border-top:3px dashed var(--amb)}.facts div{border-bottom:1px solid #2C2C26}.facts b{color:var(--grn);font-family:"VT323",monospace;font-size:17px}
.hb{background:#141410;color:var(--amb);border-top:2px solid var(--amb);border-bottom:2px solid var(--amb)}.hb b{color:var(--grn)}
.bar h2{font-size:34px;color:#fff}.bar.r h2{color:var(--amb)}.bar span{color:var(--grn);font-family:"VT323",monospace;font-size:22px}
.no{background:var(--amb);color:#141005;font-size:34px}.tile.r .no{background:var(--grn)}
.tt{background:#141410;color:var(--amb);border:2px solid var(--amb)}.tile.r .tt{color:var(--grn);border-color:var(--grn)}
.card{border-bottom:2px solid #2C2C26}
.big{color:var(--amb);font-size:88px}.card.r .big{color:var(--grn)}
.genre{background:var(--amb);color:#141005}.card.r .genre{background:var(--grn);color:#06130A}
.mapbtn{background:var(--amb)}.mapbtn svg path{fill:#141005}
.hrs2{color:var(--amb);font-family:"VT323",monospace;font-size:19px}
.btn{background:var(--amb);color:#141005;font-family:"VT323",monospace;font-size:22px;letter-spacing:.06em}
.cta{background:#101408;border-top:3px dashed var(--grn);border-bottom:3px dashed var(--grn)}.cta h2{color:var(--grn);font-size:32px}.cta .btn{background:var(--grn);color:#06130A}
.know{background:#141410;color:#F2F2F2}.know h2{color:var(--amb);font-size:36px}
.crd summary{color:var(--mu)}.cr{color:var(--mu)}
.tx{color:#E4E4DA}
"""

VARIANTS = [
 ("variant-a.html", CSS_A, FONT_ARCHIVO, "%23D9342B", "#D9342B"),
 ("variant-b.html", CSS_B, FONT_ARCHIVO, "%23FF3EA5", "#FF3EA5"),
 ("variant-c.html", CSS_C, FONT_ARCHIVO, "%23E60012", "#E60012"),
 ("variant-d.html", CSS_D, FONT_ARCHIVO, "%23C8102E", "#C8102E"),
 ("variant-e.html", CSS_E, FONT_E, "%23FFB000", "#FFB000"),
]
for fname, css, fonts, acc_url, clock in VARIANTS:
    html = HEAD.replace("__FONTS__", fonts).replace("__CSS__", css).replace("__ACC__", acc_url).replace("__BODY__", body(clock))
    (W/fname).write_text(html)
    print("wrote", fname, len(html))

# ---------- comparison board ----------
BOARD_CARDS = [
 ("A","variant-a.html","Yuria-style standard","Cream, red and black — the house style of the guest pages."),
 ("B","variant-b.html","Night neon","Dark navy with neon pink and cyan — Akihabara after dark."),
 ("C","variant-c.html","Pop manga","White with halftone dots, bold primaries and speech-bubble labels."),
 ("D","variant-d.html","Clean minimal","Light and quiet, one red accent, lots of breathing room."),
 ("E","variant-e.html","Retro arcade","Black with amber and green, chunky pixel-type headlines."),
]
cards_html = ""
for letter, fn, name, desc in BOARD_CARDS:
    cards_html += f'''<section class="v"><div class="vh"><span class="letter">{letter}</span><div><h2>{name}</h2><p>{desc}</p></div><a class="open" href="{fn}">Open full page &rarr;</a></div><div class="frame"><iframe src="{fn}" title="Design {letter}: {name}" loading="lazy" scrolling="no"></iframe></div></section>'''
board = """<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>Akihabara Welcome Page — 5 Design Ideas</title><meta name="robots" content="noindex,nofollow">
<meta property="og:title" content="Akihabara Welcome Page — 5 Design Ideas"><meta property="og:description" content="Five designs for the generic Akihabara tour welcome page. Pick one in chat."><meta property="og:image" content="https://yukitchy.github.io/akiba-tour-welcome/og.jpg"><meta property="og:url" content="https://yukitchy.github.io/akiba-tour-welcome/">
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Noto+Sans+JP:wght@500;700;900&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box}body{margin:0;background:#F1EFEA;color:#121212;font:16px/1.5 Archivo,"Noto Sans JP",sans-serif}
.col{max-width:860px;margin:0 auto;padding:0 16px}
.top{display:flex;justify-content:space-between;font-weight:800;font-size:13px;letter-spacing:.14em;padding:18px 0 8px;border-bottom:4px solid #121212}
h1{font-family:Archivo,sans-serif;font-stretch:62%;font-weight:900;text-transform:uppercase;margin:16px 0 6px;font-size:min(9vw,52px);line-height:.95;white-space:nowrap}
h1 em{font-style:normal;color:#D9342B}
.sub{color:#5D5A54;margin:0 0 8px;font-size:15px}
.v{margin:34px 0 44px}.vh{display:flex;gap:14px;align-items:flex-start;margin-bottom:12px}
.letter{flex:none;width:52px;height:52px;background:#D9342B;color:#fff;font:900 30px/52px Archivo,sans-serif;text-align:center}
.vh h2{margin:2px 0 2px;font-size:22px;text-transform:uppercase;font-stretch:62%;font-weight:900}
.vh p{margin:0;color:#5D5A54;font-size:14.5px}
.open{flex:none;margin-left:auto;background:#121212;color:#fff;text-decoration:none;font-weight:800;font-size:13px;letter-spacing:.05em;text-transform:uppercase;padding:12px 14px;white-space:nowrap}
.frame{position:relative;height:560px;overflow:hidden;border:4px solid #121212;background:#fff}
.frame iframe{position:absolute;left:50%;top:0;width:390px;height:1180px;border:0;transform:translateX(-50%) scale(.475);transform-origin:top center;pointer-events:none}
.note{border-top:4px solid #121212;padding:14px 0 40px;color:#5D5A54;font-size:14px}
@media(max-width:560px){.open{padding:10px;font-size:12px}.letter{width:44px;height:44px;line-height:44px;font-size:25px}}
</style></head><body><div class="col">
<div class="top"><span>DESIGN BOARD</span><span>AKIHABARA WELCOME PAGE</span></div>
<h1>Pick a <em>design</em></h1>
<p class="sub">Five designs, one page: the generic welcome page every Akihabara guest gets with their booking email. Same words and photos in all five &mdash; only the skin changes. Tell me the letter in chat.</p>
__CARDS__
<p class="note">Previews are scaled-down live copies of each page. Use &ldquo;Open full page&rdquo; to see a design at real size.</p>
</div></body></html>"""
(W/"board.html").write_text(board.replace("__CARDS__", cards_html))
print("wrote board.html", len(board))

# ---------- FINAL PAGE: shortened variant A + questionnaire block -> index.html ----------
SHORT_TX = [
 "Ten floors of figures, trading cards, dolls and model kits, right outside the Electric Town exit &mdash; if it exists in Akihabara, it is probably in here.",
 "Eight floors of pre-owned manga, doujinshi, toys, animation cels and cards &mdash; the place to hunt for the rare thing that sold out years ago.",
 "Animate&rsquo;s flagship, renewed in 2026: new manga, discs, music and character goods, plus event floors for whatever is airing now.",
 "A big second-hand store one minute from the station: used manga, games, CDs, DVDs and trading cards across several floors &mdash; half the fun is never knowing what you will find.",
 "Bandai Namco&rsquo;s own game centre, one minute from the Electric Town exit: crane games and gashapon floors, plus the official Ichibankuji shop and a Bandai card game shop.",
 "A Chuo-dori institution for used games: floor after floor of pre-owned and retro games, with whole floors of figures too. The stock turns over fast, so every visit is a fresh hunt.",
]
def cards_short(clock_color):
    out=[]
    for i,(no,genre,name,hrs,img,alt,q,tx,tag) in enumerate(FINAL_PLACES):
        r = ' r' if i%2==0 else ''
        out.append(f'''<article class="card{r}" id="p{i+1}"><div class="hd"><span class="big">{no}</span><div><span class="genre">{genre}</span><div class="nm"><h3>{name}</h3><span class="hrs2">{CLOCK(clock_color)}{hrs}</span></div></div></div><div class="phw"><img class="ph" src="{img}" alt="{alt}" loading="lazy"><a class="mapbtn" href="https://www.google.com/maps/search/?api=1&amp;query={q}" target="_blank" rel="noopener" aria-label="Open {name} in Google Maps">{PIN}</a></div><p class="tx">{SHORT_TX[i]}</p></article>''')
    return "\n".join(out)

FINAL_BODY = """<div class="col"><div class="top"><span>GUEST GUIDE</span><span>AKIHABARA &middot; 6 PLACES</span></div>
<h1>Your <em>Akihabara</em> Anime Tour</h1></div>
<div class="col" style="padding:0"><div class="hero"><div class="hero3"><img src="img/street-day.jpg" alt="Akihabara's Chuo-dori street in the daytime"><img src="img/street-night.jpg" alt="Akihabara at night, neon signs"><img src="img/hero-figures.jpg" alt="A display case full of anime figures in an Akihabara shop"></div></div>
<div class="hb"><span>About 4 hours &middot; flexible</span><b>Meet at VIE DE FRANCE, BiTO AKIBA 1F</b></div></div>
<div class="col"><div class="facts"><div><b>Guide</b><span>Yuuki &mdash; a local otaku guide</span></div><div><b>Meet</b><span>VIE DE FRANCE bakery caf&eacute;, BiTO AKIBA building 1F, inside the caf&eacute;</span></div><div><b>Time</b><span>About 4 hours, flexible</span></div><div><b>Style</b><span>Private tour, built around your favourite series</span></div></div></div>
<div class="survey"><div class="col"><h2>Before your tour</h2><p>Tell me your favourite series and what you want to see &mdash; I will plan the afternoon around them.</p><div class="bt"><a class="btn big" href="__FORM__" target="_blank" rel="noopener">Answer the questionnaire</a></div></div></div>
<div class="col">
<article class="card meet" id="meet"><div class="hd"><div><span class="genre">Meeting point</span><div class="nm"><h3>VIE DE FRANCE &mdash; BiTO AKIBA PLAZA</h3></div></div></div>
<div class="wall w1"><div class="tile"><img src="img/meeting-cafe.jpg" alt="The Vie de France bakery café on the 1st floor of the BiTO AKIBA building" loading="lazy"><span class="tt">Meet here: the café</span></div></div>
<p class="tx" style="margin-top:14px"><b>How to find it:</b> come out of JR Akihabara Station at the <b>Electric Town exit</b> &mdash; the caf&eacute; is about <b>1 minute</b> away, on the 1st floor of the BiTO AKIBA building. Please come inside the caf&eacute; and look for me there. <b>There is another Vie de France nearby</b>, so please check the map.</p>
<div class="bt"><a class="btn" href="__MAP_MEET__" target="_blank" rel="noopener">Open in Google Maps</a></div></article>
__CARDS_SHORT__
</div>
<div class="know"><div class="col"><h2>GOOD TO KNOW</h2><ul><li><b>The plan is flexible.</b> We choose the shops together on the day, around what you love.</li><li><b>Bring some cash</b> &mdash; 100-yen coins especially, for game centres and gashapon machines.</li><li><b>Photos:</b> I take photos during the tour and share an album with you afterwards.</li><li><b>Questions?</b> Message me on WhatsApp: <b>+81 90 4494 1989</b>.</li></ul></div></div>
<details class="crd"><summary>Photo credits and sources</summary><p class="cr">Photos via Wikimedia Commons: Akihabara street (day) by Nickdrj (public domain); Akihabara at night by ElHeineken (CC BY 4.0); Radio Kaikan at night by Stephen Kelly (CC BY 2.0); Mandarake Complex by &#27491;&#21644; (CC BY-SA 3.0); Animate Akihabara by Dick Thomas Johnson (CC BY 2.0); inside BOOK OFF Akihabara Ekimae by Matthide127 (CC0). The figure display case, the Vie de France caf&eacute; at BiTO AKIBA, the namco Akihabara building and a case of second-hand figures are the guide&rsquo;s own photos. Opening hours checked against the shops&rsquo; official sites on 18 November 2026. Hours can change; we will confirm together on the day.</p></details>"""

CSS_FINAL = CSS_A + """
.survey{background:var(--ink);color:#fff;margin-top:26px;padding:30px 0 34px}
.survey h2{margin:0 0 10px;font-size:32px}
.survey p{margin:0 0 8px;font-size:16px}
.survey .btn{background:var(--red);color:#fff}
"""
fb = FINAL_BODY.replace("__MAP_MEET__", MAP_MEET).replace("__FORM__", FORM).replace("__CARDS_SHORT__", cards_short("#D9342B"))
final_html = HEAD.replace("__FONTS__", FONT_ARCHIVO).replace("__CSS__", CSS_FINAL).replace("__ACC__", "%23D9342B").replace("__BODY__", fb)
final_html = final_html.replace("https://yukitchy.github.io/akiba-tour-welcome/og.jpg", "https://yukitchy.github.io/akiba-tour-welcome/img/og-red.jpg")
(W/"index.html").write_text(final_html)
print("wrote index.html (final)", len(final_html))
