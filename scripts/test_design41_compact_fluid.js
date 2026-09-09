const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  try {
    for (const viewport of [{width:1440,height:900},{width:1366,height:768}]) {
      const page = await browser.newPage({ viewport });
      const errors = [];
      page.on('pageerror', e => errors.push('pageerror: ' + e.message));
      await page.goto('http://127.0.0.1:4173/41.html', { waitUntil: 'domcontentloaded', timeout: 30000 });
      await page.waitForTimeout(1200);

      const heights = await page.evaluate(() => [...document.querySelectorAll('main > section')].map(el => ({
        id: el.id || el.className,
        height: el.getBoundingClientRect().height,
        limit: innerHeight * .8
      })));
      for (const item of heights) {
        if (item.height > item.limit + 2) {
          throw new Error(`Section ${item.id} is ${item.height}px, above 80vh limit ${item.limit}px at ${viewport.width}x${viewport.height}`);
        }
      }

      const before = await page.evaluate(() => {
        const hero = document.querySelector('.hero-copy');
        const quick = document.querySelector('.quick-action');
        return {
          heroX: parseFloat(hero.style.getPropertyValue('--px')) || 0,
          heroY: parseFloat(hero.style.getPropertyValue('--py')) || 0,
          quickX: parseFloat(quick.style.getPropertyValue('--px')) || 0,
          quickY: parseFloat(quick.style.getPropertyValue('--py')) || 0,
          heroTransform: getComputedStyle(hero).transform,
          quickTransform: getComputedStyle(quick).transform
        };
      });

      await page.mouse.move(viewport.width * .88, viewport.height * .32);
      await page.waitForTimeout(900);
      const after = await page.evaluate(() => {
        const hero = document.querySelector('.hero-copy');
        const quick = document.querySelector('.quick-action');
        return {
          heroX: parseFloat(hero.style.getPropertyValue('--px')) || 0,
          heroY: parseFloat(hero.style.getPropertyValue('--py')) || 0,
          quickX: parseFloat(quick.style.getPropertyValue('--px')) || 0,
          quickY: parseFloat(quick.style.getPropertyValue('--py')) || 0,
          heroTransform: getComputedStyle(hero).transform,
          quickTransform: getComputedStyle(quick).transform
        };
      });
      const heroDelta = Math.hypot(after.heroX - before.heroX, after.heroY - before.heroY);
      const quickDelta = Math.hypot(after.quickX - before.quickX, after.quickY - before.quickY);
      if (heroDelta < 2) throw new Error(`Hero fluid movement too small: ${heroDelta.toFixed(2)}px`);
      if (quickDelta < 1.2) throw new Error(`Quick Action fluid movement too small: ${quickDelta.toFixed(2)}px`);
      if (after.heroTransform === 'none' || after.quickTransform === 'none') throw new Error('Fluid transform is not being applied');

      // Core interactions should still work.
      await page.click('.quick-action[data-action="recharge"]');
      await page.waitForTimeout(150);
      if (!await page.locator('.drawer').evaluate(el => el.classList.contains('open'))) throw new Error('Recharge drawer no longer opens');
      await page.click('.drawer-close');
      await page.click('[data-search-open]');
      await page.waitForTimeout(120);
      if (!await page.locator('.search-overlay').evaluate(el => el.classList.contains('open'))) throw new Error('Search overlay no longer opens');
      await page.click('[data-search-close]');
      await page.hover('.service-row[data-service="internet"]');
      await page.waitForTimeout(260);
      const serviceTitle = await page.textContent('#serviceTitle');
      if (!/Home Internet/i.test(serviceTitle || '')) throw new Error('Service switching no longer works');

      if (errors.length) throw new Error(errors.join('\n'));
      console.log('PASS', viewport, { heights, heroDelta, quickDelta });
      await page.close();
    }
  } finally {
    await browser.close();
  }
})();
