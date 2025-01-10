document.addEventListener("DOMContentLoaded", () => {
  // Select all cards with quick preview sections
  const cards = document.querySelectorAll(".coach-card");

  cards.forEach((card) => {
    const cardTop = card.querySelector(".card-top"); // Only the card-top section
    const quickPreview = card.querySelector(".quick-preview");

    if (cardTop && quickPreview) {
      // Show Quick Preview on mouseover (true boundary crossing)
      cardTop.addEventListener("mouseover", (event) => {
        if (!cardTop.contains(event.relatedTarget)) {
          console.log("Quick preview shown");
          quickPreview.style.display = "flex";
        }
      });

      // Hide Quick Preview on mouseout (true boundary crossing)
      cardTop.addEventListener("mouseout", (event) => {
        if (!cardTop.contains(event.relatedTarget)) {
          console.log("Quick preview hidden");
          quickPreview.style.display = "none";
        }
      });
    }
  });
});
