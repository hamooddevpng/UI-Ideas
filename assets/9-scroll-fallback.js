(() => {
  'use strict';

  const T = window.TELIKOM_STORY = {};
  T.clamp = (value, min = 0, max = 1) => Math.max(min, Math.min(max, value));
  T.lerp = (a, b, amount) => a + (b - a) * amount;
  T.smooth = (value) => value * value * (3 - 2 * value);
  T.smoothRange = (start, end, value) => T.smooth(T.clamp((value - start) / (end - start)));
  T.reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  T.stops = [0, 0.14, 0.28, 0.42, 0.56, 0.70, 0.84, 1];

  T.chapters = [...document.querySelectorAll('.chapter')];
  T.timeline = [...document.querySelectorAll('.timeline button')];
  T.progressFill = document.getElementById('progressFill');
  T.progressText = document.getElementById('progressText');
  T.assetState = document.getElementById('assetState');
  T.newsStack = document.getElementById('newsStack');
  T.newsCards = [...document.querySelectorAll('.news-card')];
  T.warp = document.getElementById('warp');
  T.state = { targetP: 0, p: 0, tmx: 0, tmy: 0, mx: 0, my: 0, activeIndex: -1 };

  document.documentElement.style.overflowY = 'auto';
  document.body.style.overflowY = 'auto';
  document.body.style.minHeight = '900vh';
  const scrollSpace = document.querySelector('.scroll-space');
  if (scrollSpace) scrollSpace.style.height = '900vh';

  T.maxScroll = () => Math.max(1, document.documentElement.scrollHeight - window.innerHeight);
  T.go = (index) => {
    const i = T.clamp(Number(index) || 0, 0, T.stops.length - 1);
    window.scrollTo({ top: T.stops[i] * T.maxScroll(), behavior: T.reduce ? 'auto' : 'smooth' });
  };

  T.nearestStop = (value) => {
    let bestIndex = 0;
    let bestDistance = Infinity;
    T.stops.forEach((stop, index) => {
      const distance = Math.abs(value - stop);
      if (distance < bestDistance) {
        bestDistance = distance;
        bestIndex = index;
      }
    });
    return bestIndex;
  };

  T.updateUI = () => {
    const p = T.state.p;
    const activeIndex = T.nearestStop(p);
    T.state.activeIndex = activeIndex;
    T.timeline.forEach((button, index) => button.classList.toggle('active', index === activeIndex));

    T.chapters.forEach((chapter, index) => {
      const distance = Math.abs(p - T.stops[index]);
      const span = (index === 0 || index === T.stops.length - 1) ? 0.15 : 0.115;
      const amount = T.smooth(T.clamp(1 - distance / span));
      const direction = p < T.stops[index] ? 1 : -1;
      const mobile = window.innerWidth <= 700;
      chapter.style.opacity = amount.toFixed(3);
      chapter.style.filter = T.reduce ? 'none' : `blur(${((1 - amount) * 10).toFixed(2)}px)`;
      chapter.style.pointerEvents = index === activeIndex ? 'auto' : 'none';
      chapter.classList.toggle('active', index === activeIndex);
      chapter.style.transform = mobile
        ? `translate3d(${direction * (1 - amount) * 24}px,${(1 - amount) * 18}px,0) scale(${0.97 + amount * 0.03})`
        : `translate3d(${direction * (1 - amount) * 42}px,calc(-50% + ${direction * (1 - amount) * 24}px),0) scale(${0.94 + amount * 0.06})`;
    });

    if (T.progressFill) T.progressFill.style.width = `${(p * 100).toFixed(2)}%`;
    if (T.progressText) T.progressText.textContent = `${String(Math.round(p * 100)).padStart(2, '0')}%`;

    const newsAmount = T.smoothRange(0.73, 0.88, p) * (1 - T.smoothRange(0.89, 0.98, p));
    if (T.newsStack) T.newsStack.classList.toggle('show', newsAmount > 0.03);
    if (newsAmount > 0.02 && T.newsCards.length) {
      const sub = T.clamp((p - 0.74) / 0.13);
      const scaled = sub * (T.newsCards.length - 0.001);
      T.newsCards.forEach((card, index) => {
        const delta = index - scaled;
        const distance = Math.abs(delta);
        const opacity = T.clamp(1 - distance * 1.15);
        card.style.opacity = opacity.toFixed(3);
        card.style.transform = `translate3d(${delta * 105}px,${distance * 28}px,0) rotate(${delta * 2.6}deg) scale(${1 - distance * 0.06})`;
        card.style.filter = T.reduce ? 'none' : `blur(${Math.min(10, distance * 7)}px)`;
      });
    }

    if (T.warp) {
      const spaceAmount = T.smoothRange(0.58, 0.66, p) * (1 - T.smoothRange(0.88, 0.98, p));
      T.warp.style.opacity = (spaceAmount * 0.36).toFixed(3);
      T.warp.style.transform = `scale(${1.35 + spaceAmount * 0.4}) rotate(${p * 14}deg)`;
    }
  };

  document.querySelectorAll('[data-go]').forEach((element) => {
    element.addEventListener('click', (event) => {
      event.preventDefault();
      T.go(element.dataset.go);
    });
  });

  window.addEventListener('pointermove', (event) => {
    if (event.pointerType === 'touch') return;
    T.state.tmx = event.clientX / window.innerWidth * 2 - 1;
    T.state.tmy = event.clientY / window.innerHeight * 2 - 1;
  }, { passive: true });

  const chat = document.getElementById('chat');
  const chatLaunch = document.getElementById('chatLaunch');
  if (chat && chatLaunch) chatLaunch.addEventListener('click', () => chat.classList.toggle('open'));

  T.state.p = T.state.targetP = T.clamp(window.scrollY / T.maxScroll());

  function uiFrame() {
    T.state.targetP = T.clamp(window.scrollY / T.maxScroll());
    T.state.p = T.lerp(T.state.p, T.state.targetP, T.reduce ? 1 : 0.09);
    T.updateUI();
    window.requestAnimationFrame(uiFrame);
  }

  uiFrame();
})();