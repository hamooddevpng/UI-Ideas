# Page Design Reference QA Report

Automated QA screen for the expanded Telikom Page Design visual research. This is intentionally conservative: obvious failures are excluded, blank-title/small-image cases are held for contact-sheet review, and structural recommendations still require manual visual review.

| Cohort | Captured | Candidate-valid | Needs visual review | Excluded | Gate |
|---|---:|---:|---:|---:|---|
| About Us (`about-us`) | 21 | 17 | 2 | 2 | PASS |
| Affordable Home Data (`affordable-home-data`) | 21 | 17 | 1 | 3 | PASS |
| Business - Fixed (`business-fixed`) | 21 | 18 | 0 | 3 | PASS |
| Business - Mobile (`business-mobile`) | 21 | 18 | 0 | 3 | PASS |
| Careers (`careers`) | 21 | 18 | 0 | 3 | PASS |
| Contact (`contact`) | 21 | 16 | 1 | 4 | PASS |
| PNG Business Context (`context-png-businesses`) | 21 | 17 | 0 | 4 | PASS |
| PNG Government & Public Sector Context (`context-png-public-sector`) | 18 | 15 | 1 | 2 | PASS |
| Devices (`devices`) | 29 | 16 | 3 | 10 | PASS |
| FAQs (`faqs`) | 21 | 19 | 0 | 2 | PASS |
| Home Entertainment (`home-entertainment`) | 21 | 17 | 0 | 4 | PASS |
| News & Media (`news-media`) | 23 | 16 | 1 | 6 | PASS |
| Personal - Mobile (`personal-mobile`) | 21 | 15 | 2 | 4 | PASS |
| Services Hub (`services-hub`) | 21 | 18 | 1 | 2 | PASS |
| Special Home Passes (`special-home-passes`) | 27 | 19 | 2 | 6 | PASS |
| Store Locator (`store-locator`) | 22 | 17 | 0 | 5 | PASS |
| U-TOKMoa (`u-tokmoa`) | 21 | 17 | 1 | 3 | PASS |

## Exclusions and review flags

### About Us
**Excluded:**
- `air-niugini` — capture status=partial
- `kina-bank` — capture status=error; screenshot missing
**Manual visual review required:**
- `bt-about` — very small screenshot file; inspect for blank/partial render
- `verizon-about` — very small screenshot file; inspect for blank/partial render

### Affordable Home Data
**Excluded:**
- `globe-home` — blocked/error title: Just a moment...
- `optus-internet` — capture status=partial
- `spark-broadband` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect
**Manual visual review required:**
- `giffgaff-broadband` — blank document title; visual confirmation required

### Business - Fixed
**Excluded:**
- `comcast-business` — capture status=partial
- `optus-enterprise` — capture status=partial
- `spark-business` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect

### Business - Mobile
**Excluded:**
- `kina-bank` — capture status=error; screenshot missing
- `optus-business-mobile` — capture status=partial
- `spark-business-mobile` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect

### Careers
**Excluded:**
- `air-niugini` — capture status=partial
- `kina-bank` — capture status=partial
- `verizon-careers` — blocked/error title: Just a moment...; security verification page rather than careers content

### Contact
**Excluded:**
- `air-niugini` — capture status=partial
- `bankpng` — blocked/error title: Just a moment...
- `kina-bank` — capture status=partial
- `verizon-contact` — error page rather than contact experience
**Manual visual review required:**
- `ee-contact` — blank document title; visual confirmation required

### PNG Business Context
**Excluded:**
- `air-niugini` — capture status=partial
- `brian-bell` — capture status=partial
- `credit-corp` — blocked/error title: Just a moment...
- `kina-bank` — capture status=partial

### PNG Government & Public Sector Context
**Excluded:**
- `bankpng` — blocked/error title: Just a moment...
- `finance-png` — capture status=error
**Manual visual review required:**
- `png-customs` — very small screenshot file; inspect for blank/partial render

### Devices
**Excluded:**
- `brian-bell` — capture status=partial
- `globe-devices` — blocked/error title: Just a moment...
- `jio-devices` — capture status=error
- `one-nz-phones` — blocked/error title: 404 - Page Not Found
- `optus-phones` — capture status=partial
- `samsung-smartphones` — capture status=partial
- `sony-smartphones` — blocked/error title: Access Denied
- `spark-phones` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect
- `vodafone-png-broadband-devices` — capture status=error; incomplete/failed local devices capture
- `xiaomi-uk-mobile` — blocked/error title: Access Denied
**Manual visual review required:**
- `giffgaff-phones` — blank document title; visual confirmation required
- `singtel-phones` — very small screenshot file; inspect for blank/partial render
- `smart-devices` — very small screenshot file; inspect for blank/partial render; blank document title; visual confirmation required

### FAQs
**Excluded:**
- `optus-support` — capture status=error
- `spark-help` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect

### Home Entertainment
**Excluded:**
- `att-tv` — capture status=partial
- `globe-home` — blocked/error title: Just a moment...
- `optus-subhub` — capture status=partial
- `spark-entertainment` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect

### News & Media
**Excluded:**
- `air-niugini` — capture status=partial
- `att-newsroom` — blocked/error title: Access Denied
- `bankpng` — blocked/error title: Just a moment...
- `kina-bank` — capture status=error; screenshot missing
- `orange-newsroom` — cookie consent overlay obstructs the page
- `verizon-press` — pathological over-expanded/infinite listing capture
**Manual visual review required:**
- `verizon-news` — very small screenshot file; inspect for blank/partial render

### Personal - Mobile
**Excluded:**
- `globe-prepaid` — blocked/error title: Just a moment...
- `one-nz-prepay` — blocked/error title: 404 - Page Not Found
- `optus-prepaid` — capture status=partial
- `spark-prepaid` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect
**Manual visual review required:**
- `giffgaff-payg` — blank document title; visual confirmation required
- `smart-prepaid` — very small screenshot file; inspect for blank/partial render; blank document title; visual confirmation required

### Services Hub
**Excluded:**
- `optus-consumer` — capture status=partial
- `spark-nz` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect
**Manual visual review required:**
- `smart-ph` — very small screenshot file; inspect for blank/partial render; blank document title; visual confirmation required

### Special Home Passes
**Excluded:**
- `globe-promos` — blocked/error title: Just a moment...
- `lebara-mobile` — blocked/error title: Just a moment...
- `one-nz-offers` — blocked/error title: 404 - Page Not Found
- `optus-deals` — capture status=partial
- `singtel-promotions` — blocked/error title: Page Not Found
- `spark-deals` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect
**Manual visual review required:**
- `giffgaff-payg` — blank document title; visual confirmation required
- `smart-promos` — very small screenshot file; inspect for blank/partial render; blank document title; visual confirmation required

### Store Locator
**Excluded:**
- `brian-bell` — capture status=partial
- `kina-bank` — capture status=partial
- `one-nz-stores` — blocked/error title: 404 - Page Not Found
- `optus-stores` — capture status=partial
- `spark-stores` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect

### U-TOKMoa
**Excluded:**
- `globe-home` — blocked/error title: Just a moment...
- `optus-home-internet` — capture status=partial
- `spark-landline` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect
**Manual visual review required:**
- `giffgaff-plans` — blank document title; visual confirmation required

