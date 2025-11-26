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

    // expose a programmatic next action for buttons
    const nextButton = document.getElementById('research-carousel-next');
    if (nextButton) {
      nextButton.addEventListener('click', function(e){
        // manual advance should pause the auto-scroll briefly
        stop();
        slideUp();
        // restart after a short delay
        setTimeout(start, 1200);
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
        stop();
        slideDown();
        setTimeout(start, 1200);
      });
    }

    // Keyboard support: ArrowUp => prev, ArrowDown => next
    document.addEventListener('keydown', function(e){
      if (e.key === 'ArrowUp') {
        e.preventDefault(); stop(); slideDown(); setTimeout(start, 1200);
      } else if (e.key === 'ArrowDown') {
        e.preventDefault(); stop(); slideUp(); setTimeout(start, 1200);
      }
    });

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
