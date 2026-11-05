import json
import re
import hashlib
import zipfile
from pathlib import Path
from PIL import Image

root=Path(__file__).parent
html_path=root/'region-viii-emt.html'
with zipfile.ZipFile(root/'../recovered/saltysec_studyguides_github_pages.zip') as original:
    s=original.read('region-viii-emt.html').decode()
data=json.loads((root/'questions_v4.json').read_text())
assert len(data['cases'])==133

data_start=s.index('const DATA=')+len('const DATA=')
_,data_len=json.JSONDecoder().raw_decode(s[data_start:])
s=s[:data_start]+json.dumps(data,ensure_ascii=False,separators=(',',':')).replace('</','<\\/')+s[data_start+data_len:]

themes_css='''
:root,[data-theme="harbor"]{--bg:#0b1922;--surface:#112631;--line:#31515b;--ink:#ecf4f2;--muted:#afc6c8;--aqua:#83dfca;--btn:#193640;--input:#0b1d27;--hover:#25424c;--order:#0c202a;--pearl:#183b40;--check:#214039;--checkline:#527669;--stat:#193440;--feedback:#173a3c;--correct:#21443b;--wrong:#532d35;--dialog:#102630;--onaccent:#09222a}
[data-theme="light"]{--bg:#f2f6f5;--surface:#fff;--line:#bdcdd0;--ink:#152c34;--muted:#415d65;--aqua:#087e72;--btn:#e7f1f0;--input:#f7faf9;--hover:#e1eff0;--order:#f8faf9;--pearl:#e5f5f0;--check:#e4f5e9;--checkline:#9bc9a6;--stat:#e9f1f2;--feedback:#e5f4f2;--correct:#d9f3df;--wrong:#f7dfe0;--dialog:#fff;--onaccent:#fff}
[data-theme="midnight"]{--bg:#070a17;--surface:#111a2b;--line:#334662;--ink:#eef3ff;--muted:#afbfdd;--aqua:#87bfff;--btn:#1b2c47;--input:#0b1324;--hover:#263c5b;--order:#0a1529;--pearl:#1b3152;--check:#203650;--checkline:#5980aa;--stat:#1a2b46;--feedback:#1b3553;--correct:#1b463e;--wrong:#512d41;--dialog:#111a2b;--onaccent:#061426}
[data-theme="charcoal"]{--bg:#18191b;--surface:#252629;--line:#555557;--ink:#f6f0e9;--muted:#c9bbb0;--aqua:#ff9e4a;--btn:#383534;--input:#1d1e20;--hover:#4b4038;--order:#1e1f21;--pearl:#3c3028;--check:#3d352b;--checkline:#a0784f;--stat:#34302c;--feedback:#3f3329;--correct:#2d4539;--wrong:#523236;--dialog:#252629;--onaccent:#21140c}
[data-theme="forest"]{--bg:#101d18;--surface:#1b2e26;--line:#486454;--ink:#f0f7eb;--muted:#bfcebd;--aqua:#d3e77e;--btn:#2b4134;--input:#16251e;--hover:#3b5845;--order:#14241c;--pearl:#314333;--check:#2b4635;--checkline:#73956d;--stat:#294036;--feedback:#2f4b37;--correct:#2b513c;--wrong:#603b3c;--dialog:#1b2e26;--onaccent:#172017}
html,body{background:var(--bg);color:var(--ink)}.theme-control{display:flex;align-items:center;gap:9px;margin-left:auto;color:var(--muted);font-size:.88rem}.theme-control select{background:var(--input);color:var(--ink);border:1px solid var(--line);padding:9px 11px;border-radius:9px;min-width:142px}.theme-control select:focus-visible{outline:2px solid var(--aqua)}.notice a{color:var(--aqua)}.scope{font-size:.8rem;padding:4px 8px;border:1px solid var(--line);border-radius:999px;color:var(--aqua)}
'''
sty_start=s.index('<style>')+len('<style>');sty_end=s.index('</style>');sty=s[sty_start:sty_end]
# Theme all surfaces, including form controls and PDF modal.
subs={'#0b1922':'var(--bg)','#112631':'var(--surface)','#31515b':'var(--line)','#ecf4f2':'var(--ink)','#afc6c8':'var(--muted)','#83dfca':'var(--aqua)','#193640':'var(--btn)','#0b1d27':'var(--input)','#25424c':'var(--hover)','#0c202a':'var(--order)','#183b40':'var(--pearl)','#214039':'var(--check)','#527669':'var(--checkline)','#193440':'var(--stat)','#173a3c':'var(--feedback)','#21443b':'var(--correct)','#532d35':'var(--wrong)','#102630':'var(--dialog)','#09222a':'var(--onaccent)'}
for old,new in subs.items():sty=sty.replace(old,new)
sty=sty.replace('--surface:var(--surface);--line:var(--line);--muted:var(--muted);--aqua:var(--aqua)','')
sty=sty.replace('color:#fff','color:var(--ink)').replace('color:#e8f1ef','color:var(--ink)').replace('color:#fff','color:var(--ink)')
sty=sty.replace('background:#2a444d','background:var(--line)').replace('background:#000b','background:#000b')
sty=sty.replace('border-color:#85dca4','border-color:#65c987').replace('border-color:#ed9999','border-color:#e98484')
sty=sty.replace('color:#fff;width:min(1050px','color:var(--ink);width:min(1050px')
s=s[:sty_start]+sty+themes_css+s[sty_end:]
s=s.replace('<a class="btn source" href="./region-viii-standing-medical-orders.pdf"', '<label class="theme-control" for="themeSelect">Theme <select id="themeSelect" aria-label="Color theme"><option value="harbor">Harbor · default</option><option value="light">Light</option><option value="midnight">Midnight</option><option value="charcoal">Charcoal & orange</option><option value="forest">Forest</option></select></label><a class="btn source" href="./region-viii-standing-medical-orders.pdf"')
s=s.replace('The medication appendix is separate.', 'The medication appendix is separate. <strong>This is the June 2024 edition; Loyola currently lists a newer revision.</strong> <a href="https://www.loyolamedicine.org/ems/resources/policies-smos" target="_blank" rel="noopener">Check the current SMOs ↗</a>')
s=s.replace('Hard scenarios test specific decision points.', '133 source-checked scenarios test tight thresholds and nearby protocol branches, including 80 medication-related items. The scope label distinguishes EMT/BLS actions from ALS awareness. Hard scenarios test specific decision points.')
s=s.replace('${esc(q.cat)} · ${esc(c.title)}</p><h2>', '${esc(q.cat)} · ${esc(c.title)} <span class="scope">${esc(q.scope||"All levels")}</span></p><h2>')
s=s.replace('function save(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch{}}', 'function save(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch{}}const THEME_KEY="region8-theme";let chosenTheme="harbor";try{chosenTheme=localStorage.getItem(THEME_KEY)||"harbor"}catch{};if(!["harbor","light","midnight","charcoal","forest"].includes(chosenTheme))chosenTheme="harbor";document.documentElement.dataset.theme=chosenTheme;document.getElementById("themeSelect").value=chosenTheme;document.getElementById("themeSelect").onchange=e=>{document.documentElement.dataset.theme=e.target.value;try{localStorage.setItem(THEME_KEY,e.target.value)}catch{}};')
# Scope note is on questions; assessed answers must still link to source.
assert s.count('data-theme="')>=5 and s.count('kind":"mcq"')==133
html_path.write_text(s)
(root/'index.html').write_text((root/'index.html').read_text().replace('90 advanced scenarios','133 source-checked scenarios'))
with zipfile.ZipFile(root/'../recovered/saltysec_studyguides_github_pages.zip') as original:
    readme=original.read('README.md').decode()
(root/'README.md').write_text(readme+"\nThe Region VIII guide loads protocol page images from `region8-pages/`. Upload that entire folder alongside `region-viii-emt.html`. The questions reference the June 2024 PDF bundled here; check Loyola's current edition for clinical use.\n")
(root/'../region8_webp_images.zip').unlink(missing_ok=True)
with zipfile.ZipFile(root/'../region8_webp_images.zip','w',zipfile.ZIP_STORED) as z:
    files=sorted((root/'region8-pages').glob('*.webp'),key=lambda p:int(p.stem))
    assert len(files)==191
    for p in files:
        assert p.stat().st_size>1000,p
        with Image.open(p) as im:im.verify()
        z.write(p,'region8-pages/'+p.name)
with zipfile.ZipFile(root/'../saltysec_studyguides_github_pages.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in root.rglob('*'):
        if p.is_file():z.write(p,p.relative_to(root))
print('html',len(s),'questions',len(data['cases']),'images',len(files))
