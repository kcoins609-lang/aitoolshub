AIToolsHub – static website (HTML, CSS, JS only)

HOW TO PUBLISH (free)
1. Upload this whole folder to GitHub and import it in Vercel (or Netlify / Cloudflare Pages). No build command needed.
2. Open index.html locally to preview: all links are relative so it works offline too.

BEFORE YOU GO LIVE – CHANGE THESE
- Site name, domain and email: edit SITE_NAME, DOMAIN, CONTACT_EMAIL in gen/data.py, then run: python3 gen/build.py ./site
  (or find/replace "https://www.example.com" and "contact@example.com" in all files)
- Check that each tool's free plan details are still correct on its official site.

ADSENSE
- Apply only after the site is live on your own domain with real content.
- Paste your AdSense script in the commented block in the <head> of every page (find/replace "GOOGLE ADSENSE").
- Put the ads.txt line from Google into ads.txt.
- Empty <div class="ad-slot"></div> elements mark where ads can go. They stay hidden until filled.
- Never click your own ads.

ADDING A NEW TOOL
- Add one entry to the TOOLS list in gen/data.py, run python3 gen/build.py ./site, upload again.
