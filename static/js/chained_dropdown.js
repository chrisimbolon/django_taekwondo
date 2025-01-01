document.addEventListener("DOMContentLoaded", function () {
  const countryDropdown = document.getElementById("id_country");
  const provinceDropdown = document.getElementById("id_province");
  const cityDropdown = document.getElementById("id_city");

  if (countryDropdown) {
    countryDropdown.addEventListener("change", function () {
      const countryCode = this.value;

      // Clear provinces and cities
      provinceDropdown.innerHTML =
        '<option value="" disabled selected>-- Select Province --</option>';
      cityDropdown.innerHTML =
        '<option value="" disabled selected>-- Select City --</option>';

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
          })
          .catch((error) => console.error("Error fetching provinces:", error));
      }
    });
  }

  if (provinceDropdown) {
    provinceDropdown.addEventListener("change", function () {
      const provinceId = this.value;

      // Clear cities
      cityDropdown.innerHTML =
        '<option value="" disabled selected>-- Select City --</option>';

      if (provinceId) {
        fetch(`/filter-cities/?province_id=${provinceId}`)
          .then((response) => response.json())
          .then((data) => {
            data.forEach((city) => {
              const option = document.createElement("option");
              option.value = city.id;
              option.textContent = city.city_name;
              cityDropdown.appendChild(option);
            });
          })
          .catch((error) => console.error("Error fetching cities:", error));
      }
    });
  }
});
