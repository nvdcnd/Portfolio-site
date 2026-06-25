(() => {
  const navbar = document.querySelector("[data-navbar]");

  if (!navbar) {
    return;
  }

  const updateNavbarState = () => {
    navbar.classList.toggle("is-scrolled", window.scrollY > 8);
  };

  updateNavbarState();
  window.addEventListener("scroll", updateNavbarState, { passive: true });
})();
