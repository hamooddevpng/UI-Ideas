const { chromium } = require(process.cwd() + '/node_modules/playwright-core');

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: '/usr/bin/google-chrome', args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));

  await page.goto('http://127.0.0.1:8000/42.html', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(1400);
  await page.evaluate(() => document.getElementById('business').scrollIntoView({ block: 'center' }));
  await page.waitForTimeout(700);

  const initial = await page.evaluate(() => ({
    height: business.getBoundingClientRect().height,
    route: businessConsole.dataset.route,
    active: [...document.querySelectorAll('.business-endpoint.active')].map(e => e.textContent.trim()),
    map: document.querySelector('.business-png-map')?.complete,
    groups: document.querySelectorAll('.business-route-g').length,
    old: !!document.querySelector('.biz-panel')
  }));
  if (initial.height > 810) throw Error('business section exceeds 90vh comfort limit ' + initial.height);
  if (initial.route !== '0' || initial.groups !== 4 || initial.old || !initial.map) throw Error('business console initial state failed ' + JSON.stringify(initial));

  await page.hover('[data-business-route="1"]');
  await page.waitForTimeout(220);
  const vsat = await page.evaluate(() => ({
    route: businessConsole.dataset.route,
    name: businessRouteName.textContent,
    active: [...document.querySelectorAll('.business-endpoint.active')].map(e => e.textContent.trim()),
    packet: getComputedStyle(document.querySelector('.business-route-g[data-route="1"] .route-packet')).opacity
  }));
  if (vsat.route !== '1' || !vsat.name.includes('VSAT') || !vsat.active.some(x => x.includes('REMOTE')) || Number(vsat.packet) < .9) throw Error('VSAT route failed ' + JSON.stringify(vsat));

  await page.click('[data-business-route="3"]');
  await page.waitForTimeout(120);
  const locked = await page.evaluate(() => ({
    route: businessConsole.dataset.route,
    locked: businessConsole.classList.contains('route-locked'),
    status: businessRouteStatus.textContent,
    dc: [...document.querySelectorAll('.business-endpoint.active')].some(e => e.textContent.includes('DATA CENTRE'))
  }));
  if (locked.route !== '3' || !locked.locked || !locked.status.includes('ROUTE LOCKED') || !locked.dc) throw Error('route lock failed ' + JSON.stringify(locked));

  const br = await page.locator('#businessConsole').boundingBox();
  await page.mouse.move(br.x + 40, br.y + 70);
  await page.waitForTimeout(120);
  const t1 = await page.evaluate(() => getComputedStyle(businessConsole).transform);
  await page.mouse.move(br.x + br.width - 40, br.y + br.height - 70);
  await page.waitForTimeout(120);
  const t2 = await page.evaluate(() => getComputedStyle(businessConsole).transform);
  if (t1 === t2) throw Error('business pointer perspective failed');

  await page.evaluate(() => scrollTo(0, 0));
  await page.waitForTimeout(220);
  await page.hover('.hero');
  await page.click('.scene-tab[data-scene="1"]');
  await page.waitForTimeout(720);
  await page.mouse.move(1080, 180);
  await page.waitForTimeout(260);
  const a = await page.evaluate(() => ({ s: getComputedStyle(document.querySelector('.satellite')).transform, d: getComputedStyle(document.querySelector('.dish-head-svg')).transform }));
  await page.mouse.move(760, 420);
  await page.waitForTimeout(260);
  const b = await page.evaluate(() => ({ s: getComputedStyle(document.querySelector('.satellite')).transform, d: getComputedStyle(document.querySelector('.dish-head-svg')).transform }));
  if (a.s === b.s || a.d === b.d) throw Error('hero satellite/dish regression');

  await page.evaluate(() => document.getElementById('services').scrollIntoView({ block: 'center' }));
  await page.waitForTimeout(950);
  const stories = await page.evaluate(() => ({ cards: document.querySelectorAll('.service-story-card').length, portal: !!document.querySelector('.service-portal') }));
  if (stories.cards !== 5 || stories.portal) throw Error('service story regression ' + JSON.stringify(stories));

  if (errors.length) throw Error(errors.join(' | '));
  console.log('Business initial', initial);
  console.log('VSAT route', vsat);
  console.log('Route lock', locked);
  console.log('Perspective changed', t1 !== t2);
  console.log('Hero and service story regressions passed');
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
