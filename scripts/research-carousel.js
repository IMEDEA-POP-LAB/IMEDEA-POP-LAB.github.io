(function(){
  // Vertical carousel: shows 4 items in a column and auto-scrolls upwards
  document.addEventListener('DOMContentLoaded', function(){
    const track = document.getElementById('research-carousel');
    if (!track) return;

    const viewport = track.parentElement;
    const photoGallery = viewport.closest('.photo-gallery');
    const intervalMs = 3000;
    let timer = null;
    let isAnimating = false;

    // Adjust carousel item size to match Recent Publications column height
    function adjustToPublications() {
      try {
        const recent = document.querySelector('.recent-publications');
        const aboutMain = document.querySelector('.about-main');
        // Prefer the full about main column height so the gallery fills the
        // visible page area; fall back to recent publications if not present.
        const target = aboutMain || recent;
        if (!target || !photoGallery) return;

        const gapStr = getComputedStyle(photoGallery).getPropertyValue('--gallery-item-gap') || '14';
        const gap = parseFloat(gapStr) || 14;
        const targetH = target.getBoundingClientRect().height;
        // compute item height so 4 items + gaps fit the target height
        let itemH = Math.floor((targetH - gap * 3) / 4);
        // clamp to reasonable bounds
        itemH = Math.max(80, Math.min(260, itemH));
        // set CSS variable on the photoGallery so styles react
        photoGallery.style.setProperty('--gallery-item-fixed-height', itemH + 'px');
        // Also explicitly set the viewport height so we can add a small
        // visual extension (a little bit longer) without changing item size.
        // Choose visible count based on small-screen breakpoint (match SCSS @media).
        const visibleCount = (window.innerWidth <= 640) ? 3 : 4;
        // add a slightly larger extra padding so the gallery appears taller
        // (increase from ~8% to ~16% of the item height, minimum 22px)
        const extra = Math.max(22, Math.round(itemH * 0.16));
        const viewportH = (itemH + gap) * visibleCount - gap + extra;
        viewport.style.height = viewportH + 'px';
      } catch (e) {
        // silent
      }
    }

    // debounce resize
    let resizeTimer = null;
    function onResize() {
      clearTimeout(resizeTimer);
      resizeTimer = setTimeout(adjustToPublications, 150);
    }

    // run once now (allow the layout a short moment to settle)
    setTimeout(adjustToPublications, 60);
    window.addEventListener('resize', onResize);

    function getItemFullHeight(el) {
      const rect = el.getBoundingClientRect();
      const style = getComputedStyle(el);
      const mb = parseFloat(style.marginBottom) || 0;
      return rect.height + mb;
    }

    function slideUp() {
      if (isAnimating) return;
      const first = track.children[0];
      if (!first) return;
      const itemH = getItemFullHeight(first);
      isAnimating = true;
      track.style.transition = 'transform 600ms ease';
      track.style.transform = `translateY(-${itemH}px)`;
      setTimeout(()=>{
        track.style.transition = 'none';
        track.style.transform = 'translateY(0)';
        track.appendChild(first);
        // allow the browser a tick before enabling animations again
        setTimeout(()=>{ isAnimating = false; }, 50);
      }, 610);
    }

    // expose a programmatic next action for buttons
    const nextButton = document.getElementById('research-carousel-next');
    if (nextButton) {
      nextButton.addEventListener('click', function(e){
        // manual advance via button only
        slideUp();
      });
    }

    // Prev button: animate downward by prepending last child then transitioning
    const prevButton = document.getElementById('research-carousel-prev');
    function slideDown() {
      if (isAnimating) return;
      const last = track.children[track.children.length - 1];
      if (!last) return;
      const itemH = getItemFullHeight(last);
      isAnimating = true;
      // move last to front and set initial offset
      track.style.transition = 'none';
      track.insertBefore(last, track.firstChild);
      track.style.transform = `translateY(-${itemH}px)`;
      // animate to 0
      requestAnimationFrame(()=>{
        track.style.transition = 'transform 600ms ease';
        track.style.transform = 'translateY(0)';
      });
      setTimeout(()=>{
        track.style.transition = 'none';
        // reset transform ensures consistent state
        track.style.transform = 'translateY(0)';
        setTimeout(()=>{ isAnimating = false; }, 50);
      }, 610);
    }

    if (prevButton) {
      prevButton.addEventListener('click', function(e){
        // manual previous via button only
        slideDown();
      });
    }

    // Keyboard support: ArrowUp => prev, ArrowDown => next (manual only)
    document.addEventListener('keydown', function(e){
      if (e.key === 'ArrowUp') {
        e.preventDefault(); slideDown();
      } else if (e.key === 'ArrowDown') {
        e.preventDefault(); slideUp();
      }
    });

    // Auto-advance disabled: navigation happens only via buttons/keyboard.
    function start() { /* intentionally left empty */ }
    function stop() { /* intentionally left empty */ }
  });
})();
