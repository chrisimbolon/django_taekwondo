document.addEventListener("DOMContentLoaded", () => {
  const favorites = JSON.parse(localStorage.getItem("favorites")) || [];
  const viewFavoritesBtn = document.querySelector("#viewFavoritesBtn");
  const coachCards = document.querySelectorAll(".coach-card");

  // Add click event to the "View Favorites" button
  viewFavoritesBtn.addEventListener("click", () => {
    if (favorites.length === 0) {
      alert("No favorites selected!"); // Inform the user if no favorites exist
      return;
    }

    coachCards.forEach((card) => {
      const coachId = card.dataset.coachId;
      if (!favorites.includes(coachId)) {
        card.style.display = "none"; // Hide non-favorited cards
      } else {
        card.style.display = "block"; // Show favorited cards
      }
    });

    // Change button text to toggle behavior
    viewFavoritesBtn.textContent =
      viewFavoritesBtn.textContent === "View Favorites"
        ? "Show All"
        : "View Favorites";

    // Toggle display behavior
    if (viewFavoritesBtn.textContent === "View Favorites") {
      coachCards.forEach((card) => (card.style.display = "block")); // Show all cards again
    }
  });
});
