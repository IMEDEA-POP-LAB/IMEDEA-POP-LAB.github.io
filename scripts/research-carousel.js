(function(){
  // Vertical carousel: shows 4 items in a column and auto-scrolls upwards
  document.addEventListener('DOMContentLoaded', function(){
    const track = document.getElementById('research-carousel');
    if (!track) return;

    const viewport = track.parentElement;
    const intervalMs = 3000;
    let timer = null;
    let isAnimating = false;

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

    function start() {
      if (timer) return;
      timer = setInterval(slideUp, intervalMs);
    }
    function stop() {
      if (!timer) return;
      clearInterval(timer);
      timer = null;
    }

    // Pause on hover
    viewport.addEventListener('mouseenter', stop);
    viewport.addEventListener('focusin', stop);
    viewport.addEventListener('mouseleave', start);
    viewport.addEventListener('focusout', start);

    // Start
    start();
  });
})();
