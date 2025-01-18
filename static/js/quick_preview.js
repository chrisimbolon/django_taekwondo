document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".coach-card");

  cards.forEach((card) => {
    const cardTop = card.querySelector(".card-top");
    const quickPreview = card.querySelector(".quick-preview");

    if (cardTop && quickPreview) {
      // Show quick preview on card-top hover
      cardTop.addEventListener("mouseenter", () => {
        quickPreview.style.display = "flex";
        quickPreview.style.pointerEvents = "auto"; // Allow interaction
      });

      // Hide quick preview on card-top mouseleave
      cardTop.addEventListener("mouseleave", () => {
        quickPreview.style.display = "none";
        quickPreview.style.pointerEvents = "none"; // Disable interaction
      });

      // Ensure hovering over the preview doesn’t glitch (optional)
      quickPreview.addEventListener("mouseenter", () => {
        quickPreview.style.display = "flex";
        quickPreview.style.pointerEvents = "auto";
      });
      quickPreview.addEventListener("mouseleave", () => {
        quickPreview.style.display = "none";
        quickPreview.style.pointerEvents = "none";
      });
    }
  });
});
