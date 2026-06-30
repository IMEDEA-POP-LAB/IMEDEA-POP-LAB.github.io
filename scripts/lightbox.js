(function () {
  function initLightbox() {
    var grid = document.querySelector('.album-photos-grid');
    if (!grid) return;

    var images = Array.from(grid.querySelectorAll('.album-photo-item img'));
    if (!images.length) return;

    var current = 0;

    // Build overlay
    var overlay = document.createElement('div');
    overlay.id = 'lb-overlay';
    overlay.innerHTML = [
      '<button id="lb-close" aria-label="Close">✕</button>',
      '<button id="lb-prev" aria-label="Previous">&#8592;</button>',
      '<div id="lb-img-wrap"><img id="lb-img" src="" alt=""></div>',
      '<button id="lb-next" aria-label="Next">&#8594;</button>',
      '<div id="lb-counter"></div>'
    ].join('');
    document.body.appendChild(overlay);

    var lbImg     = document.getElementById('lb-img');
    var lbCounter = document.getElementById('lb-counter');
    var lbClose   = document.getElementById('lb-close');
    var lbPrev    = document.getElementById('lb-prev');
    var lbNext    = document.getElementById('lb-next');

    function show(index) {
      current = (index + images.length) % images.length;
      lbImg.src = images[current].src;
      lbImg.alt = images[current].alt;
      lbCounter.textContent = (current + 1) + ' / ' + images.length;
      overlay.classList.add('lb-visible');
      document.body.style.overflow = 'hidden';
    }

    function hide() {
      overlay.classList.remove('lb-visible');
      document.body.style.overflow = '';
    }

    // Click on photo opens lightbox
    images.forEach(function (img, i) {
      img.parentElement.style.cursor = 'zoom-in';
      img.parentElement.addEventListener('click', function () { show(i); });
    });

    lbClose.addEventListener('click', hide);
    lbPrev.addEventListener('click', function () { show(current - 1); });
    lbNext.addEventListener('click', function () { show(current + 1); });

    // Click outside image closes
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) hide();
    });

    // Keyboard navigation
    document.addEventListener('keydown', function (e) {
      if (!overlay.classList.contains('lb-visible')) return;
      if (e.key === 'ArrowRight') show(current + 1);
      if (e.key === 'ArrowLeft')  show(current - 1);
      if (e.key === 'Escape')     hide();
    });

    // Touch/swipe support
    var touchStartX = 0;
    overlay.addEventListener('touchstart', function (e) {
      touchStartX = e.changedTouches[0].clientX;
    }, { passive: true });
    overlay.addEventListener('touchend', function (e) {
      var diff = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 40) {
        if (diff > 0) show(current + 1);
        else          show(current - 1);
      }
    }, { passive: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLightbox);
  } else {
    initLightbox();
  }
})();
