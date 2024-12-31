document.addEventListener("DOMContentLoaded", () => {
  // Initialize favorites from localStorage
  let favorites = JSON.parse(localStorage.getItem("favorites")) || [];
  const viewFavoritesBtn = document.querySelector("#viewFavoritesBtn");
  const coachCards = document.querySelectorAll(".coach-card");
  const coachContainer = document.querySelector(".coaches-page .row"); // Parent container for cards

  // Helper: Save favorites to localStorage
  const saveFavorites = () => {
    localStorage.setItem("favorites", JSON.stringify(favorites));
  };

  // Helper: Clear and rebuild the card list
  const rebuildCards = (showFavoritesOnly) => {
    // Clear current cards
    coachContainer.innerHTML = "";

    // Filter and re-add cards
    coachCards.forEach((card) => {
      const coachId = card.dataset.coachId;

      if (!showFavoritesOnly || favorites.includes(coachId)) {
        coachContainer.appendChild(card); // Add back to the DOM
      }
    });
  };

  // Handle click on favorite buttons
  document.addEventListener("click", (e) => {
    if (e.target.closest(".favorite-btn")) {
      const card = e.target.closest(".coach-card");
      const coachId = card.dataset.coachId;

      if (favorites.includes(coachId)) {
        // Remove from favorites
        favorites = favorites.filter((id) => id !== coachId);
      } else {
        // Add to favorites
        favorites.push(coachId);
      }

      saveFavorites(); // Save updated favorites to localStorage
    }
  });

  // Handle "View Favorites" button click
  viewFavoritesBtn.addEventListener("click", () => {
    const isViewingFavorites =
      viewFavoritesBtn.textContent === "View Favorites";

    // Rebuild cards based on the view mode
    rebuildCards(isViewingFavorites);

    // Update button text
    viewFavoritesBtn.textContent = isViewingFavorites
      ? "Show All"
      : "View Favorites";
  });

  // Initial UI setup: Show all cards on page load
  rebuildCards(false);
});
