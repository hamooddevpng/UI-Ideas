# Page Design Reference QA Report

Automated QA screen for the expanded Telikom Page Design visual research. This is intentionally conservative: obvious failures are excluded, blank-title/small-image cases are held for contact-sheet review, and structural recommendations still require manual visual review.

| Cohort | Captured | Candidate-valid | Needs visual review | Excluded | Gate |
|---|---:|---:|---:|---:|---|
| About Us (`about-us`) | 15 | 12 | 0 | 3 | BACKFILL REQUIRED |
| Affordable Home Data (`affordable-home-data`) | 15 | 12 | 0 | 3 | BACKFILL REQUIRED |
| Business - Fixed (`business-fixed`) | 15 | 12 | 0 | 3 | BACKFILL REQUIRED |
| Business - Mobile (`business-mobile`) | 15 | 11 | 0 | 4 | BACKFILL REQUIRED |
| Careers (`careers`) | 15 | 12 | 0 | 3 | BACKFILL REQUIRED |
| Contact (`contact`) | 15 | 11 | 0 | 4 | BACKFILL REQUIRED |
| PNG Business Context (`context-png-businesses`) | 15 | 11 | 0 | 4 | BACKFILL REQUIRED |
| PNG Government & Public Sector Context (`context-png-public-sector`) | 12 | 11 | 0 | 1 | BACKFILL REQUIRED |
| Devices (`devices`) | 15 | 6 | 2 | 7 | BACKFILL REQUIRED |
| FAQs (`faqs`) | 15 | 13 | 0 | 2 | BACKFILL REQUIRED |
| Home Entertainment (`home-entertainment`) | 15 | 11 | 0 | 4 | BACKFILL REQUIRED |
| News & Media (`news-media`) | 15 | 9 | 0 | 6 | BACKFILL REQUIRED |
| Personal - Mobile (`personal-mobile`) | 15 | 10 | 1 | 4 | BACKFILL REQUIRED |
| Services Hub (`services-hub`) | 15 | 12 | 1 | 2 | BACKFILL REQUIRED |
| Special Home Passes (`special-home-passes`) | 15 | 9 | 1 | 5 | BACKFILL REQUIRED |
| Store Locator (`store-locator`) | 15 | 10 | 0 | 5 | BACKFILL REQUIRED |
| U-TOKMoa (`u-tokmoa`) | 15 | 12 | 0 | 3 | BACKFILL REQUIRED |

## Exclusions and review flags

### About Us
**Excluded:**
- `air-niugini` — capture status=partial
- `kina-bank` — capture status=error; screenshot missing
- `vodafone-png-about` — capture status=partial

### Affordable Home Data
**Excluded:**
- `globe-home` — blocked/error title: Just a moment...
- `optus-internet` — capture status=partial
- `spark-broadband` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect

### Business - Fixed
**Excluded:**
- `optus-enterprise` — capture status=partial
- `spark-business` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect
- `vodafone-png-dedicated-internet` — capture status=error

### Business - Mobile
**Excluded:**
- `kina-bank` — capture status=error; screenshot missing
- `optus-business-mobile` — capture status=partial
- `spark-business-mobile` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect
- `vodafone-png-mobility` — capture status=error

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
- `verizon-contact` — blocked/error title: Error; error page rather than contact experience

### PNG Business Context
**Excluded:**
- `air-niugini` — capture status=partial
- `brian-bell` — capture status=partial
- `credit-corp` — blocked/error title: Just a moment...
- `kina-bank` — capture status=partial

### PNG Government & Public Sector Context
**Excluded:**
- `bankpng` — blocked/error title: Just a moment...

### Devices
**Excluded:**
- `brian-bell` — capture status=partial
- `globe-devices` — blocked/error title: Just a moment...
- `one-nz-phones` — blocked/error title: 404 - Page Not Found
- `optus-phones` — capture status=partial
- `spark-phones` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect
- `vodafone-png-broadband-devices` — capture status=error; incomplete/failed local devices capture
- `vodafone-png-devices` — capture status=error
**Manual visual review required:**
- `singtel-phones` — very small screenshot file; inspect for blank/partial render
- `smart-devices` — very small screenshot file; inspect for blank/partial render; blank document title; visual confirmation required

### FAQs
**Excluded:**
- `optus-support` — capture status=partial
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

### Personal - Mobile
**Excluded:**
- `globe-prepaid` — blocked/error title: Just a moment...
- `one-nz-prepay` — blocked/error title: 404 - Page Not Found
- `optus-prepaid` — capture status=partial
- `spark-prepaid` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect
**Manual visual review required:**
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
- `one-nz-offers` — blocked/error title: 404 - Page Not Found
- `optus-deals` — capture status=partial
- `singtel-promotions` — blocked/error title: Page Not Found
- `spark-deals` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect
**Manual visual review required:**
- `smart-promos` — very small screenshot file; inspect for blank/partial render; blank document title; visual confirmation required

### Store Locator
**Excluded:**
- `brian-bell` — capture status=partial
- `kina-bank` — capture status=error; screenshot missing
- `one-nz-stores` — blocked/error title: 404 - Page Not Found
- `optus-stores` — capture status=error; screenshot missing
- `spark-stores` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect

### U-TOKMoa
**Excluded:**
- `globe-home` — blocked/error title: Just a moment...
- `optus-home-internet` — capture status=partial
- `spark-landline` — blocked/error title: Radware Bot Manager Captcha; bot/security redirect

