document.addEventListener("DOMContentLoaded", () => {
  const navbarToggler = document.querySelector(".navbar-toggler");
  const navbarCollapse = document.querySelector("#navbarContent");

  if (navbarToggler && navbarCollapse) {
    navbarToggler.addEventListener("click", () => {
      const icon = navbarToggler.querySelector("i");

      if (navbarToggler.classList.contains("collapsed")) {
        icon.classList.remove("fa-times");
        icon.classList.add("fa-bars");
      } else {
        icon.classList.remove("fa-bars");
        icon.classList.add("fa-times");
      }
    });
  }
});
