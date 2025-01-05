document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.querySelector("#loginModalForm");
  const loginModal = document.getElementById("loginModal");

  if (!loginModal) return; // Guard clause if modal doesn't exist.

  // Refresh CSRF token when the modal is shown
  loginModal.addEventListener("show.bs.modal", function () {
    fetch("/get-csrf-token/") // Django view to fetch the CSRF token
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch CSRF token");
        }
        return response.json();
      })
      .then((data) => {
        // Update the CSRF token in the form
        const csrfInput = loginForm.querySelector(
          'input[name="csrfmiddlewaretoken"]'
        );
        if (csrfInput) {
          csrfInput.value = data.csrf_token;
        }
      })
      .catch((error) => console.error("Error refreshing CSRF token:", error));
  });

  // Handle form submission
  loginForm.addEventListener("submit", function (e) {
    e.preventDefault(); // Prevent default form submission
    console.log("Login form submission intercepted");

    const formData = new FormData(this);
    const url = this.action;

    fetch(url, {
      method: "POST",
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
      },
    })
      .then((response) => {
        if (!response.ok) {
          return response.json().then((data) => {
            throw data; // Pass errors to the catch block
          });
        }
        return response.json();
      })
      .then((data) => {
        if (data.success) {
          window.location.reload(); // Reload the page on success
        }
      })
      .catch((error) => {
        if (error.errors) {
          handleErrors(error.errors);
        } else {
          console.error("Unexpected error:", error);
        }
      });

    function handleErrors(errors) {
      const errorAlert = document.querySelector("#loginErrorAlert");

      // Display general error message (if any)
      if (errors.__all__) {
        errorAlert.textContent = errors.__all__[0].message;
        errorAlert.classList.remove("d-none");
      } else {
        errorAlert.classList.add("d-none");
      }

      // Display field-specific errors
      Object.keys(errors).forEach((field) => {
        const input = document.querySelector(`#id_${field}`);
        const feedback = input ? input.nextElementSibling : null;

        if (input && errors[field]) {
          input.classList.add("is-invalid");
          if (feedback) feedback.textContent = errors[field][0].message;
        } else if (input) {
          input.classList.remove("is-invalid");
          if (feedback) feedback.textContent = "";
        }
      });
    }
  });
});
