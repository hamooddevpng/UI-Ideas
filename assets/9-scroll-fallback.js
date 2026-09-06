(() => {
  'use strict';

  const stops = [0, 0.14, 0.28, 0.42, 0.56, 0.70, 0.84, 1];
  const clamp = (value, min = 0, max = 1) => Math.max(min, Math.min(max, value));
  const maxScroll = () => Math.max(1, document.documentElement.scrollHeight - window.innerHeight);

  // The main story controller normally creates this object. If it loaded,
  // leave the full experience alone.
  if (window.TELIKOM_STORY) return;

  const chapters = [...document.querySelectorAll('.chapter')];
  const timeline = [...document.querySelectorAll('.timeline button')];
  const progressFill = document.getElementById('progressFill');
  const progressText = document.getElementById('progressText');
  const assetState = document.getElementById('assetState');

  // Guarantee a real scrolling document even if the remote stylesheet fails.
  document.documentElement.style.overflowY = 'auto';
  document.body.style.overflowY = 'auto';
  document.body.style.minHeight = '900vh';
  const scrollSpace = document.querySelector('.scroll-space');
  if (scrollSpace) scrollSpace.style.height = '900vh';

  const go = (index) => {
    const i = clamp(Number(index) || 0, 0, stops.length - 1);
    window.scrollTo({ top: stops[i] * maxScroll(), behavior: 'smooth' });
  };

  document.querySelectorAll('[data-go]').forEach((element) => {
    element.addEventListener('click', (event) => {
      event.preventDefault();
      go(element.dataset.go);
    });
  });

  const update = () => {
    const p = clamp(window.scrollY / maxScroll());
    let active = 0;
    let bestDistance = Infinity;

    stops.forEach((stop, index) => {
      const distance = Math.abs(p - stop);
      if (distance < bestDistance) {
        bestDistance = distance;
        active = index;
      }
    });

    chapters.forEach((chapter, index) => {
      const isActive = index === active;
      chapter.classList.toggle('active', isActive);
      chapter.style.opacity = isActive ? '1' : '0';
      chapter.style.filter = isActive ? 'none' : 'blur(8px)';
      chapter.style.pointerEvents = isActive ? 'auto' : 'none';
      chapter.style.transform = isActive
        ? 'translate3d(0,-50%,0) scale(1)'
        : 'translate3d(36px,-46%,0) scale(.96)';
    });

    timeline.forEach((button, index) => button.classList.toggle('active', index === active));
    if (progressFill) progressFill.style.width = `${(p * 100).toFixed(2)}%`;
    if (progressText) progressText.textContent = `${String(Math.round(p * 100)).padStart(2, '0')}%`;
  };

  if (assetState) assetState.textContent = 'Story mode — 3D controller unavailable';
  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update, { passive: true });
  update();
})();