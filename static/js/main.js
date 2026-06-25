(() => {
  const internalLinks = document.querySelectorAll('a[href^="#"]');

  internalLinks.forEach((link) => {
    link.addEventListener("click", () => {
      const activeToggle = document.querySelector(".navbar-collapse.show");

      if (activeToggle && window.bootstrap) {
        window.bootstrap.Collapse.getOrCreateInstance(activeToggle).hide();
      }
    });
  });
})();
