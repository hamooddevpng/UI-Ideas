from pathlib import Path
import re

p = Path('41.html')
s = p.read_text(encoding='utf-8')

# Replace risky / foreign-context imagery with clearly PNG-rooted imagery.
replacements = {
    'assets/design41/png-electricians.jpg': 'assets/design41/moresby-kastom-dancers-2.jpg',
    'assets/design41/village-people.jpg': 'assets/design41/mount-hagen-sing-sing-2019.jpg',
    'assets/design41/aptc-graduates.jpg': 'assets/design41/kopar-village-child.jpg',
    'assets/design41/education-png.jpg': 'assets/design41/telikom-retail-team.jpg',
    'assets/design41/png-locals-meeting.jpg': 'assets/design41/asaro-goroka-performers.jpg',
}
for old, new in replacements.items():
    s = s.replace(old, new)

# Improve alt text so every image is unambiguously tied to PNG.
alt_replacements = {
    'PNG electricians and trainees in Port Moresby': 'Kastom dancers at a cultural event in Port Moresby, Papua New Guinea',
    'Papua New Guinea village community': 'People at the Mount Hagen Sing Sing in Papua New Guinea',
    'Papua New Guinea technical college graduates': 'Child in traditional dress at Kopar Village on the Sepik River, Papua New Guinea',
    'Education community in Papua New Guinea': 'Telikom Limited team at a Telikom retail location in Papua New Guinea',
    'Papua New Guinea community meeting': 'Asaro performers with a crowd in Goroka, Papua New Guinea',
}
for old, new in alt_replacements.items():
    s = s.replace(old, new)

# Update dynamic service / enterprise / story image maps too.
s = s.replace("'assets/design41/png-electricians.jpg'", "'assets/design41/moresby-kastom-dancers-13.jpg'")
s = s.replace("'assets/design41/education-png.jpg'", "'assets/design41/telikom-retail-team.jpg'")
s = s.replace("'assets/design41/png-locals-meeting.jpg'", "'assets/design41/asaro-goroka-performers.jpg'")
s = s.replace("'assets/design41/village-people.jpg'", "'assets/design41/village-men-festival-day.jpg'")
s = s.replace("'assets/design41/aptc-graduates.jpg'", "'assets/design41/mount-hagen-sing-sing-portrait.jpg'")

# Add a tiny crop tune for the new portraits without changing layout height.
css = r'''
/* PNG identity photo curation */
.hero-slide:nth-child(2) .hero-photo img{object-position:center 42%}
.hero-slide:nth-child(3) .hero-photo img{object-position:center 38%}
.offer-card[data-plan="remote"] .thumb img{object-position:center 32%}
.enterprise-media img{object-position:center 36%}
.story-main img{object-position:center 42%}
'''
if 'PNG identity photo curation' not in s:
    s = s.replace('</style>', css + '</style>', 1)

banned = [
    'assets/design41/village-people.jpg',
    'assets/design41/education-png.jpg',
    'assets/design41/png-electricians.jpg',
    'assets/design41/aptc-graduates.jpg',
    'assets/design41/png-locals-meeting.jpg',
]
for token in banned:
    if token in s:
        raise SystemExit(f'Banned risky image still referenced: {token}')

required = [
    'assets/design41/moresby-kastom-dancers-2.jpg',
    'assets/design41/mount-hagen-sing-sing-2019.jpg',
    'assets/design41/kopar-village-child.jpg',
    'assets/design41/telikom-retail-team.jpg',
    'assets/design41/asaro-goroka-performers.jpg',
    'PNG identity photo curation',
]
for token in required:
    if token not in s:
        raise SystemExit(f'Missing required curated image: {token}')

p.write_text(s, encoding='utf-8')

sources = '''# Design 41 PNG-specific photo sources\n\nThis set intentionally excludes imagery with visible foreign flags, foreign military context, or foreign-government delegation context.\n\n## Wikimedia Commons\n\n- `moresby-kastom-dancers-2.jpg`\n  Kastom dancers at a cultural event in Port Moresby celebrating Manus Province, Papua New Guinea.\n  https://commons.wikimedia.org/wiki/File:Moresby-kastom-dancers-2.jpg\n\n- `moresby-kastom-dancers-13.jpg`\n  Kastom dancers at a cultural event in Port Moresby celebrating Manus Province, Papua New Guinea.\n  https://commons.wikimedia.org/wiki/File:Moresby-kastom-dancers-13.jpg\n\n- `mount-hagen-sing-sing-2019.jpg`\n  Mount Hagen Sing Sing 2019, Papua New Guinea.\n  https://commons.wikimedia.org/wiki/File:Mount_Hagen_Sing_Sing_2019_(49059928568).jpg\n\n- `mount-hagen-sing-sing-portrait.jpg`\n  Mount Hagen Sing Sing 2019, Papua New Guinea.\n  https://commons.wikimedia.org/wiki/File:Mount_Hagen_Sing_Sing_2019_(49060446801).jpg\n\n- `kopar-village-child.jpg`\n  Child in traditional dress at Kopar Village near the Sepik River, Papua New Guinea.\n  https://commons.wikimedia.org/wiki/File:Kopar_Village_Child.jpg\n\n- `asaro-goroka-performers.jpg`\n  Asaro tribe Holosa performers in front of a crowd in Goroka, Papua New Guinea.\n  https://commons.wikimedia.org/wiki/File:(Asaro_tribe%27s_Holosa_performers_in_front_of_a_crowd_in_Goroka,_Papua_New_Guinea)_-_DPLA_-_79504f62140a72cc67da936dbd885d4b.jpg\n\n- `village-men-festival-day.jpg`\n  Village men on festival day, Papua New Guinea.\n  https://commons.wikimedia.org/wiki/File:Village_Men,_festival_day._(48646582447).jpg\n\n## Official Telikom\n\n- `telikom-retail-team.jpg`\n  Telikom Limited retail partnership/team image published on Telikom's own PNG website.\n  https://www.telikom.com.pg/assets/news/308723936_1146629262939133_7327105151876426519_n.jpg\n'''
Path('assets/design41/PNG_SOURCES.md').write_text(sources, encoding='utf-8')
print('Design 41 PNG-specific photo curation patch validated.')
