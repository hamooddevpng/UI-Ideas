from pathlib import Path

p=Path('42.html')
s=p.read_text()

old='''<meta name="robots" content="noindex,nofollow">\n<meta name="theme-color" content="#061925">\n<title>Telikom PNG | Design 42 Horizon</title>'''
if old not in s:
    raise SystemExit('expected legacy SEO head block not found')

seo='''<!-- Primary SEO -->
<meta name="description" content="Telikom PNG connects people, communities and businesses across Papua New Guinea with mobile, fixed broadband, VSAT, voice, Self Care and enterprise connectivity services.">
<meta name="keywords" content="Telikom PNG, Papua New Guinea telecommunications, PNG mobile, PNG broadband, VSAT Papua New Guinea, business internet PNG, Telikom Self Care, fixed voice, MPLS, web hosting PNG">
<meta name="author" content="Telikom PNG">
<meta name="creator" content="Telikom PNG">
<meta name="publisher" content="Telikom PNG">
<meta name="copyright" content="Telikom PNG">
<meta name="application-name" content="Telikom PNG">
<meta name="language" content="English">
<meta http-equiv="content-language" content="en-PG">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="googlebot" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="bingbot" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="format-detection" content="telephone=no">
<meta name="theme-color" content="#f5fafc">
<meta name="color-scheme" content="light">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Telikom PNG">
<meta name="msapplication-TileColor" content="#0875c9">
<meta name="geo.region" content="PG">
<meta name="geo.placename" content="Papua New Guinea">
<title>Telikom PNG | Mobile, Broadband, VSAT &amp; Business Connectivity</title>

<!-- Canonical and language targeting -->
<link rel="canonical" href="https://www.telikom.com.pg/">
<link rel="alternate" hreflang="en-PG" href="https://www.telikom.com.pg/">
<link rel="alternate" hreflang="x-default" href="https://www.telikom.com.pg/">

<!-- Brand icons and priority image -->
<link rel="icon" type="image/png" href="https://www.telikom.com.pg/assets/misc/TPNGLOGO.png">
<link rel="apple-touch-icon" href="https://www.telikom.com.pg/assets/misc/TPNGLOGO.png">
<link rel="preload" as="image" href="assets/design42/png-selfcare-fao.jpg" fetchpriority="high">

<!-- Open Graph / Facebook / LinkedIn -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.telikom.com.pg/">
<meta property="og:site_name" content="Telikom PNG">
<meta property="og:title" content="Telikom PNG | Connecting Papua New Guinea">
<meta property="og:description" content="Mobile, broadband, VSAT, voice, Self Care and enterprise connectivity for customers, communities and businesses across Papua New Guinea.">
<meta property="og:locale" content="en_PG">
<meta property="og:image" content="https://www.telikom.com.pg/assets/misc/TPNGLOGO.png">
<meta property="og:image:secure_url" content="https://www.telikom.com.pg/assets/misc/TPNGLOGO.png">
<meta property="og:image:type" content="image/png">
<meta property="og:image:alt" content="Telikom PNG logo">

<!-- Twitter / X -->
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Telikom PNG | Connecting Papua New Guinea">
<meta name="twitter:description" content="Mobile, broadband, VSAT, voice, Self Care and enterprise connectivity across Papua New Guinea.">
<meta name="twitter:image" content="https://www.telikom.com.pg/assets/misc/TPNGLOGO.png">
<meta name="twitter:image:alt" content="Telikom PNG logo">

<!-- Generic rich-result metadata -->
<meta itemprop="name" content="Telikom PNG">
<meta itemprop="description" content="Telecommunications and connectivity services for people, communities and businesses across Papua New Guinea.">
<meta itemprop="image" content="https://www.telikom.com.pg/assets/misc/TPNGLOGO.png">'''

s=s.replace(old,seo,1)

schema='''\n<script type="application/ld+json" id="telikomSeoSchema">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.telikom.com.pg/#organization",
      "name": "Telikom PNG",
      "url": "https://www.telikom.com.pg/",
      "logo": {
        "@type": "ImageObject",
        "url": "https://www.telikom.com.pg/assets/misc/TPNGLOGO.png"
      },
      "telephone": "+67576003555",
      "contactPoint": [
        {
          "@type": "ContactPoint",
          "telephone": "+67576003555",
          "contactType": "customer service",
          "areaServed": "PG"
        }
      ],
      "areaServed": {
        "@type": "Country",
        "name": "Papua New Guinea"
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://www.telikom.com.pg/#website",
      "url": "https://www.telikom.com.pg/",
      "name": "Telikom PNG",
      "description": "Connectivity and telecommunications services across Papua New Guinea.",
      "publisher": {"@id": "https://www.telikom.com.pg/#organization"},
      "inLanguage": "en-PG"
    },
    {
      "@type": "WebPage",
      "@id": "https://www.telikom.com.pg/#webpage",
      "url": "https://www.telikom.com.pg/",
      "name": "Telikom PNG | Mobile, Broadband, VSAT & Business Connectivity",
      "description": "Telikom PNG connects people, communities and businesses across Papua New Guinea with mobile, fixed broadband, VSAT, voice, Self Care and enterprise connectivity services.",
      "isPartOf": {"@id": "https://www.telikom.com.pg/#website"},
      "about": {"@id": "https://www.telikom.com.pg/#organization"},
      "primaryImageOfPage": {
        "@type": "ImageObject",
        "url": "https://www.telikom.com.pg/assets/misc/TPNGLOGO.png"
      },
      "inLanguage": "en-PG"
    },
    {
      "@type": "ItemList",
      "@id": "https://www.telikom.com.pg/#services",
      "name": "Telikom PNG services",
      "numberOfItems": 7,
      "itemListElement": [
        {"@type":"ListItem","position":1,"item":{"@type":"Service","name":"Mobile Services","provider":{"@id":"https://www.telikom.com.pg/#organization"},"areaServed":{"@type":"Country","name":"Papua New Guinea"}}},
        {"@type":"ListItem","position":2,"item":{"@type":"Service","name":"Fixed Broadband","provider":{"@id":"https://www.telikom.com.pg/#organization"},"areaServed":{"@type":"Country","name":"Papua New Guinea"}}},
        {"@type":"ListItem","position":3,"item":{"@type":"Service","name":"VSAT Services","provider":{"@id":"https://www.telikom.com.pg/#organization"},"areaServed":{"@type":"Country","name":"Papua New Guinea"}}},
        {"@type":"ListItem","position":4,"item":{"@type":"Service","name":"Business Data and MPLS","provider":{"@id":"https://www.telikom.com.pg/#organization"},"areaServed":{"@type":"Country","name":"Papua New Guinea"}}},
        {"@type":"ListItem","position":5,"item":{"@type":"Service","name":"Business Systems","provider":{"@id":"https://www.telikom.com.pg/#organization"},"areaServed":{"@type":"Country","name":"Papua New Guinea"}}},
        {"@type":"ListItem","position":6,"item":{"@type":"Service","name":"Web and Hosting","provider":{"@id":"https://www.telikom.com.pg/#organization"},"areaServed":{"@type":"Country","name":"Papua New Guinea"}}},
        {"@type":"ListItem","position":7,"item":{"@type":"Service","name":"Telikom Self Care","provider":{"@id":"https://www.telikom.com.pg/#organization"},"areaServed":{"@type":"Country","name":"Papua New Guinea"}}}
      ]
    }
  ]
}
</script>\n'''

if 'id="telikomSeoSchema"' in s:
    raise SystemExit('SEO schema already present')
marker='<link rel="preconnect" href="https://fonts.googleapis.com">'
if marker not in s:
    raise SystemExit('font preconnect marker not found')
s=s.replace(marker,schema+marker,1)

p.write_text(s)
