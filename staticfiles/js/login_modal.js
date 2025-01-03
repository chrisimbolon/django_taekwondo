document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.querySelector("#loginModalForm");
  if (!loginForm) return; // Guard clause if modal doesn't exist.

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
