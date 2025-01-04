document.addEventListener("DOMContentLoaded", function () {
  const countryDropdown = document.getElementById("id_country");
  const provinceDropdown = document.getElementById("id_province");
  const cityDropdown = document.getElementById("id_city");

  // Helper to preselect a value in a dropdown
  const preselectDropdown = (dropdown, value) => {
    Array.from(dropdown.options).forEach((option) => {
      if (option.value === value) {
        option.selected = true;
      }
    });
  };

  // Populate provinces dynamically based on the selected country
  const populateProvinces = (countryCode, selectedProvince) => {
    provinceDropdown.innerHTML =
      '<option value="" disabled selected>-- Select Province --</option>';
    cityDropdown.innerHTML =
      '<option value="" disabled selected>-- Select City --</option>'; // Clear cities

    if (countryCode) {
      fetch(`/filter-provinces/?country_code=${countryCode}`)
        .then((response) => response.json())
        .then((data) => {
          data.forEach((province) => {
            const option = document.createElement("option");
            option.value = province.id;
            option.textContent = province.province_name;
            provinceDropdown.appendChild(option);
          });
          if (selectedProvince) {
            preselectDropdown(provinceDropdown, selectedProvince);
            populateCities(selectedProvince); // Trigger city population
          }
        })
        .catch((error) => console.error("Error fetching provinces:", error));
    }
  };

  // Populate cities dynamically based on the selected province
  const populateCities = (provinceId, selectedCity) => {
    cityDropdown.innerHTML =
      '<option value="" disabled selected>-- Select City --</option>'; // Always reset cities

    if (provinceId) {
      fetch(`/filter-cities/?province_id=${provinceId}`)
        .then((response) => response.json())
        .then((data) => {
          // Populate cities based on response
          data.forEach((city) => {
            const option = document.createElement("option");
            option.value = city.id;
            option.textContent = city.city_name;
            cityDropdown.appendChild(option);
          });
          if (selectedCity) {
            preselectDropdown(cityDropdown, selectedCity); // Preselect stored value
          }
        })
        .catch((error) => console.error("Error fetching cities:", error));
    }
  };

  // Initialize the dropdowns with preselected values
  const initializeDropdowns = () => {
    const selectedCountry = countryDropdown.dataset.selected;
    const selectedProvince = provinceDropdown.dataset.selected;
    const selectedCity = cityDropdown.dataset.selected;

    if (selectedCountry) {
      populateProvinces(selectedCountry, selectedProvince);
    }
    if (selectedProvince) {
      populateCities(selectedProvince, selectedCity);
    }
  };

  // Event listener for country changes
  if (countryDropdown) {
    countryDropdown.addEventListener("change", function () {
      const countryCode = this.value;

      // Reset provinces and cities
      provinceDropdown.innerHTML =
        '<option value="" disabled selected>-- Select Province --</option>';
      cityDropdown.innerHTML =
        '<option value="" disabled selected>-- Select City --</option>';

      if (countryCode) {
        populateProvinces(countryCode); // Fetch provinces for new country
      }
    });
  }

  // Event listener for province changes
  if (provinceDropdown) {
    provinceDropdown.addEventListener("change", function () {
      const provinceId = this.value;

      // Reset cities
      cityDropdown.innerHTML =
        '<option value="" disabled selected>-- Select City --</option>';

      if (provinceId) {
        populateCities(provinceId); // Fetch cities for the selected province
      }
    });
  }

  // Initialize dropdowns on page load
  initializeDropdowns();
});
