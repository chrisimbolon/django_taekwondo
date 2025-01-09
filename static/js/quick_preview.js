document.querySelectorAll(".coach-card").forEach((card) => {
  // Desktop hover
  card.addEventListener("mouseenter", () => {
    const preview = card.querySelector(".quick-preview");
    preview.style.display = "flex";
  });

  card.addEventListener("mouseleave", () => {
    const preview = card.querySelector(".quick-preview");
    preview.style.display = "none";
  });

  // Mobile click/tap
  card.addEventListener("click", (event) => {
    const preview = card.querySelector(".quick-preview");
    const isVisible = preview.style.display === "flex";
    preview.style.display = isVisible ? "none" : "flex";
    event.stopPropagation();
  });
});

// Close all previews when clicking outside
document.body.addEventListener("click", () => {
  document.querySelectorAll(".quick-preview").forEach((preview) => {
    preview.style.display = "none";
  });
});
