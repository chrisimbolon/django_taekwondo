document.addEventListener("DOMContentLoaded", () => {
  const favoriteBtns = document.querySelectorAll(".favorite-btn");

  // Load favorites from localStorage
  const favorites = JSON.parse(localStorage.getItem("favorites")) || [];

  // Highlight already favorited coaches
  favoriteBtns.forEach((btn) => {
    const coachId = btn.dataset.coachId;
    if (favorites.includes(coachId)) {
      btn.querySelector("i").classList.replace("far", "fas");
    }

    // Add click event
    btn.addEventListener("click", () => {
      const icon = btn.querySelector("i");
      if (favorites.includes(coachId)) {
        // Remove from favorites
        favorites.splice(favorites.indexOf(coachId), 1);
        icon.classList.replace("fas", "far");
      } else {
        // Add to favorites
        favorites.push(coachId);
        icon.classList.replace("far", "fas");
      }
      // Update localStorage
      localStorage.setItem("favorites", JSON.stringify(favorites));
    });
  });
});
