from pathlib import Path
import re

p = Path('41.html')
s = p.read_text(encoding='utf-8')

ASSET = 'assets/design41/'


def replace_img_by_alt(html, old_alt, new_src, new_alt):
    pat = re.compile(r'<img\b(?=[^>]*\balt="' + re.escape(old_alt) + r'")[^>]*>')
    m = pat.search(html)
    if not m:
        raise SystemExit(f'Image with alt not found: {old_alt}')
    tag = m.group(0)
    tag = re.sub(r'\bsrc="[^"]*"', f'src="{new_src}"', tag, count=1)
    tag = re.sub(r'\s+onerror="[^"]*"', '', tag)
    tag = re.sub(r'\balt="[^"]*"', f'alt="{new_alt}"', tag, count=1)
    return html[:m.start()] + tag + html[m.end():]


def replace_img_by_id(html, image_id, new_src, new_alt):
    pat = re.compile(r'<img\b(?=[^>]*\bid="' + re.escape(image_id) + r'")[^>]*>')
    m = pat.search(html)
    if not m:
        raise SystemExit(f'Image id not found: {image_id}')
    tag = m.group(0)
    tag = re.sub(r'\bsrc="[^"]*"', f'src="{new_src}"', tag, count=1)
    tag = re.sub(r'\s+onerror="[^"]*"', '', tag)
    if re.search(r'\balt="[^"]*"', tag):
        tag = re.sub(r'\balt="[^"]*"', f'alt="{new_alt}"', tag, count=1)
    else:
        tag = tag[:-1] + f' alt="{new_alt}">'
    return html[:m.start()] + tag + html[m.end():]


static_images = [
    ('Papua New Guinea mobile connectivity', ASSET + 'gerehu-market-wide.jpg', 'People at Gerehu Market in Port Moresby, Papua New Guinea'),
    ('Telecommunications tower in Papua New Guinea', ASSET + 'png-electricians.jpg', 'PNG electricians and trainees in Port Moresby'),
    ('Telikom team and community', ASSET + 'village-people.jpg', 'Papua New Guinea village community'),
    ('Telikom 4G event in Papua New Guinea', ASSET + 'gerehu-market-2.jpg', 'Market life in Port Moresby, Papua New Guinea'),
    ('PNG mobile user', ASSET + 'upng-students-wide.jpg', 'UPNG medical students in Port Moresby, Papua New Guinea'),
    ('PNG network tower', ASSET + 'aptc-graduates.jpg', 'Papua New Guinea technical college graduates'),
    ('PNG community', ASSET + 'png-locals-meeting.jpg', 'Papua New Guinea community meeting'),
    ('PNG network landscape', ASSET + 'mt-hagen-people.jpg', 'Person at the Mount Hagen cultural festival in Papua New Guinea'),
    ('Telikom community', ASSET + 'medical-students.jpg', 'Medical students in Port Moresby, Papua New Guinea'),
    ('PNG telecom tower', ASSET + 'gerehu-market-portrait.jpg', 'People at Gerehu Market in Port Moresby, Papua New Guinea'),
]
for old_alt, src, alt in static_images:
    s = replace_img_by_alt(s, old_alt, src, alt)

s = replace_img_by_id(s, 'serviceImage', ASSET + 'goroka-market.jpg', 'People at Goroka Market, Papua New Guinea')
s = replace_img_by_id(s, 'enterpriseImage', ASSET + 'education-png.jpg', 'Education community in Papua New Guinea')
s = replace_img_by_id(s, 'storyMainImage', ASSET + 'png-locals-meeting.jpg', 'Papua New Guinea community meeting')

service_new = "const serviceData={mobile:['01','Mobile','Calls, data and everyday mobile services with a direct, practical journey.','assets/design41/goroka-market.jpg'],internet:['02','Home Internet','Availability, plan choice, setup and support in one path.','assets/design41/village-people.jpg'],devices:['03','Devices & Routers','Hardware next to the service it enables.','assets/design41/png-electricians.jpg'],enterprise:['04','Enterprise Connectivity','Business-grade connectivity for organisations.','assets/design41/aptc-graduates.jpg'],help:['05','Support Services','Troubleshooting, account help and locations together.','assets/design41/medical-students.jpg']};const setService="
s, n = re.subn(r"const serviceData=\{.*?\};const setService=", service_new, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not replace serviceData')

ent_new = "const ent={business:['Connectivity for teams, offices and organisations that need dependable access and clearer support.','assets/design41/education-png.jpg'],government:['A dedicated public-sector pathway for connectivity, managed services and support.','assets/design41/png-locals-meeting.jpg']};const setEnt="
s, n = re.subn(r"const ent=\{.*?\};const setEnt=", ent_new, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not replace enterprise image data')

story_new = "const story=[[\"Telikom's story is people, communities, cities, coastlines and highlands linked by practical services.\",'assets/design41/png-locals-meeting.jpg'],['PNG geography makes connection meaningful, from highlands to remote communities.','assets/design41/mt-hagen-people.jpg'],['Telikom is also a visible local institution, present in communities and everyday life.','assets/design41/gerehu-market-2.jpg']];const setStory="
s, n = re.subn(r"const story=\[.*?\];const setStory=", story_new, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit('Could not replace story image data')

photo_css = r'''
/* Design 41 photo refresh: give the secondary offer imagery real visual weight. */
@media(min-width:761px){
  .offer-stack{grid-template-rows:repeat(2,minmax(0,1fr))}
  .offer-card{display:grid;grid-template-columns:minmax(165px,.82fr) 1.18fr;grid-template-rows:auto auto 1fr auto;column-gap:18px;row-gap:4px;padding:14px;align-items:start}
  .offer-card .thumb{grid-column:1;grid-row:1/5;height:100%;min-height:0;margin:0;border-radius:19px}
  .offer-card>.micro,.offer-card>h3,.offer-card>p,.offer-card>.link-arrow{grid-column:2}
  .offer-card h3{font-size:clamp(23px,2.3vw,36px);margin:5px 0 3px}
  .offer-card p{margin:2px 0;font-size:10px;line-height:1.5;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
  .offer-card .link-arrow{margin-top:5px;padding-top:9px;align-self:end}
  .offer-card[data-plan="home"] .thumb img{object-position:center 38%}
  .offer-card[data-plan="remote"] .thumb img{object-position:center 42%}
}
@media(max-width:760px){
  .offer-card .thumb{height:210px;min-height:210px}
}
'''
if 'Design 41 photo refresh:' not in s:
    s = s.replace('</style>', photo_css + '</style>', 1)

external_imgs = re.findall(r'<img\b[^>]*\bsrc="https?://[^"]+"', s)
if external_imgs:
    raise SystemExit('External image sources remain after patch: ' + str(external_imgs[:3]))

required = [
    'assets/design41/gerehu-market-wide.jpg',
    'assets/design41/png-electricians.jpg',
    'assets/design41/upng-students-wide.jpg',
    'assets/design41/png-locals-meeting.jpg',
    'Design 41 photo refresh:',
    'grid-template-columns:minmax(165px,.82fr) 1.18fr',
    'height:80vh',
]
for token in required:
    if token not in s:
        raise SystemExit(f'Missing expected token: {token}')

p.write_text(s, encoding='utf-8')

sources = '''# Design 41 PNG photo sources\n\nThese images were downloaded into the repository for the Design 41 prototype so the page does not depend on third-party hotlinks. Check each linked source page for the exact attribution and license terms.\n\n- `gerehu-market-wide.jpg`: Wikimedia Commons, Gerehu Markets Port Moresby, Papua New Guinea (10697424025).jpg\n  https://commons.wikimedia.org/wiki/File:Gerehu_Markets_Port_Moresby,_Papua_New_Guinea_(10697424025).jpg\n- `gerehu-market-2.jpg`: Wikimedia Commons, Gerehu Markets Port Moresby, Papua New Guinea (10697555344).jpg\n  https://commons.wikimedia.org/wiki/File:Gerehu_Markets_Port_Moresby,_Papua_New_Guinea_(10697555344).jpg\n- `gerehu-market-portrait.jpg`: Wikimedia Commons, Gerehu Markets Port Moresby, Papua New Guinea (10697727534).jpg\n  https://commons.wikimedia.org/wiki/File:Gerehu_Markets_Port_Moresby,_Papua_New_Guinea_(10697727534).jpg\n- `png-electricians.jpg`: Wikimedia Commons, Australia provides training for PNG electricians (10673381114).jpg\n  https://commons.wikimedia.org/wiki/File:Australia_provides_training_for_PNG_electricians_(10673381114).jpg\n- `upng-students-wide.jpg`: Wikimedia Commons, Second year medical students from the UPNG School of Medicine and Health Science, Port Moresby General Hospital, PNG (10720542195).jpg\n  https://commons.wikimedia.org/wiki/File:Second_year_medical_students_from_the_UPNG_School_of_Medicine_and_Health_Science._Port_Moresby_General_Hospital,_PNG._(10720542195).jpg\n- `medical-students.jpg`: Wikimedia Commons, Second year medical students from the UPNG School of Medicine and Health Science, Port Moresby General Hospital, PNG (10720493845).jpg\n  https://commons.wikimedia.org/wiki/File:Second_year_medical_students_from_the_UPNG_School_of_Medicine_and_Health_Science._Port_Moresby_General_Hospital,_PNG._(10720493845).jpg\n- `village-people.jpg`: Wikimedia Commons, Village people in Papua New Guinea.jpg\n  https://commons.wikimedia.org/wiki/File:Village_people_in_Papua_New_Guinea.jpg\n- `goroka-market.jpg`: Wikimedia Commons, GorokaMarket.jpg\n  https://commons.wikimedia.org/wiki/File:GorokaMarket.jpg\n- `png-locals-meeting.jpg`: Wikimedia Commons, PNG Investigation Mission - Meeting with Locals in Village and Market (8605587).jpg, U.S. Army / DVIDS public-domain source.\n  https://commons.wikimedia.org/wiki/File:PNG_Investigation_Mission-_Meeting_with_Locals_in_Village_and_Market_(8605587).jpg\n- `education-png.jpg`: Wikimedia Commons, Education in PNG (10694200225).jpg\n  https://commons.wikimedia.org/wiki/File:Education_in_PNG_(10694200225).jpg\n- `aptc-graduates.jpg`: Wikimedia Commons, Australia-Pacific Technical College graduates (10673645196).jpg\n  https://commons.wikimedia.org/wiki/File:Australia-Pacific_Technical_College_graduates_(10673645196).jpg\n- `mt-hagen-people.jpg`: Wikimedia Commons, People of Papua New Guinea (48990314113).jpg\n  https://commons.wikimedia.org/wiki/File:People_of_Papua_New_Guinea_(48990314113).jpg\n'''
Path('assets/design41').mkdir(parents=True, exist_ok=True)
Path('assets/design41/SOURCES.md').write_text(sources, encoding='utf-8')
print('Patched Design 41 photo layout and image map.')
