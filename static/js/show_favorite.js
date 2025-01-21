document.addEventListener("DOMContentLoaded", () => {
  // Initialize favorites from localStorage
  let favorites = JSON.parse(localStorage.getItem("favorites")) || [];
  const viewFavoritesBtn = document.querySelector("#viewFavoritesBtn");
  const coachCards = Array.from(document.querySelectorAll(".coach-card"));
  const coachContainer = document.querySelector(".coaches-page .row"); // Parent container for cards

  // State variable for view mode
  let isViewingFavorites = false;

  // Helper: Save favorites to localStorage
  const saveFavorites = () => {
    localStorage.setItem("favorites", JSON.stringify(favorites));
  };

  // Update UI based on favorites and view mode
  const updateFavoritesUI = () => {
    let visibleCards;

    if (isViewingFavorites) {
      // Filter for favorite cards
      visibleCards = coachCards.filter((card) =>
        favorites.includes(card.dataset.coachId)
      );

      // Show a message if no favorites exist
      if (visibleCards.length === 0) {
        coachContainer.innerHTML = `
          <div class="no-favorites-message" style="text-align: center; margin-top: 20px;">
            <p>No favorites added yet. Start selecting your favorite coaches by clicking the favorite icon!</p>
          </div>
        `;
      } else {
        // If there are favorites, show them
        coachContainer.innerHTML = ""; // Clear current cards
        visibleCards.forEach((card) => coachContainer.appendChild(card));
      }
    } else {
      // Show all cards when not viewing favorites
      visibleCards = coachCards;
      coachContainer.innerHTML = ""; // Clear current cards
      visibleCards.forEach((card) => coachContainer.appendChild(card));
    }

    // ** Always update button text based on the view mode **
    // If no favorites exist, ensure the button says "View Favorites"
    viewFavoritesBtn.textContent =
      isViewingFavorites && favorites.length > 0
        ? "Show All"
        : "View Favorites";
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
    isViewingFavorites = !isViewingFavorites; // Toggle view mode state
    updateFavoritesUI(); // Update UI
  });

  // Initial UI setup
  updateFavoritesUI();
});
