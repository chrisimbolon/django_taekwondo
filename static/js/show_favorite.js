document.addEventListener("DOMContentLoaded", () => {
  // Initialize favorites from localStorage
  let favorites = JSON.parse(localStorage.getItem("favorites")) || [];
  const viewFavoritesBtn = document.querySelector("#viewFavoritesBtn");
  const coachCards = Array.from(document.querySelectorAll(".coach-card"));
  const coachContainer = document.querySelector(".coaches-page .row"); // Parent container for cards

  // Helper: Save favorites to localStorage
  const saveFavorites = () => {
    localStorage.setItem("favorites", JSON.stringify(favorites));
  };

  // Update UI based on favorites and view mode
  const updateFavoritesUI = () => {
    const isViewingFavorites =
      viewFavoritesBtn.textContent === "View Favorites";

    const visibleCards = isViewingFavorites
      ? coachCards.filter((card) => favorites.includes(card.dataset.coachId)) // Show only favorites
      : coachCards; // Show all

    coachContainer.innerHTML = ""; // Clear current cards
    visibleCards.forEach((card) => coachContainer.appendChild(card)); // Add visible cards
  };

  // Handle click on favorite buttons
  document.addEventListener("click", (e) => {
    if (e.target.closest(".favorite-btn")) {
      const card = e.target.closest(".coach-card");
      const coachId = card.dataset.coachId;

      if (favorites.includes(coachId)) {
        favorites = favorites.filter((id) => id !== coachId); // Remove from favorites
      } else {
        favorites.push(coachId); // Add to favorites
      }

      saveFavorites(); // Save updated favorites
      updateFavoritesUI(); // Update UI
    }
  });

  // Handle "View Favorites" button click
  viewFavoritesBtn.addEventListener("click", () => {
    viewFavoritesBtn.textContent =
      viewFavoritesBtn.textContent === "View Favorites"
        ? "Show All"
        : "View Favorites";
    updateFavoritesUI(); // Update UI
  });

  // Initial UI setup
  updateFavoritesUI();
});
