<script>
  let visible = $state(false);

  $effect(() => {
    function handleScroll() {
      visible = window.scrollY > 300;
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();

    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  });

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
</script>

<button
  class="scroll-to-top"
  class:visible
  onclick={scrollToTop}
  aria-label="Volver arriba"
>
  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="18 15 12 9 6 15"></polyline>
  </svg>
</button>

<style>
  .scroll-to-top {
    position: fixed;
    right: 1.5rem;
    bottom: 6rem;
    z-index: 900;
    width: 44px;
    height: 44px;
    border-radius: 50%;
    border: none;
    background-color: #0089D0;
    color: #fff;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    opacity: 0;
    visibility: hidden;
    transform: translateY(10px);
    transition: opacity 0.3s ease, visibility 0.3s ease, transform 0.3s ease, background-color 0.2s ease;
  }

  .scroll-to-top.visible {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }

  .scroll-to-top:hover {
    background-color: #006BA3;
  }
</style>
