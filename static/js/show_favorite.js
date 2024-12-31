document.addEventListener("DOMContentLoaded", () => {
  // Initialize favorites from localStorage
  let favorites = JSON.parse(localStorage.getItem("favorites")) || [];
  const viewFavoritesBtn = document.querySelector("#viewFavoritesBtn");
  const coachCards = document.querySelectorAll(".coach-card");

  // Helper: Save favorites to localStorage
  const saveFavorites = () => {
    localStorage.setItem("favorites", JSON.stringify(favorites));
  };

  // Helper: Update the UI dynamically
  const updateFavoritesUI = () => {
    coachCards.forEach((card) => {
      const coachId = card.dataset.coachId;
      const isFavorited = favorites.includes(coachId);
      const favoriteBtn = card.querySelector(".favorite-btn");

      // Update heart icon state
      if (favoriteBtn) {
        favoriteBtn.classList.toggle("favorited", isFavorited);
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
      updateFavoritesUI(); // Update UI immediately
    }
  });

  // Handle "View Favorites" button click
  viewFavoritesBtn.addEventListener("click", () => {
    if (viewFavoritesBtn.textContent === "View Favorites") {
      if (favorites.length === 0) {
        alert("No favorites selected!");
        return;
      }

      coachCards.forEach((card) => {
        const coachId = card.dataset.coachId;
        if (!favorites.includes(coachId)) {
          card.classList.add("hidden"); // Add hidden class
        } else {
          card.classList.remove("hidden"); // Remove hidden class
        }
      });

      viewFavoritesBtn.textContent = "Show All";
    } else {
      coachCards.forEach((card) => card.classList.remove("hidden")); // Show all cards
      viewFavoritesBtn.textContent = "View Favorites";
    }
  });

  // Initial UI update on page load
  updateFavoritesUI();
});
