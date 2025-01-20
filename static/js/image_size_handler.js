document.addEventListener("DOMContentLoaded", function () {
  // Handle the form submission via AJAX
  const form = document.getElementById("update-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent default form submission
    const url = form.getAttribute("action");
    const formData = new FormData(form);

    fetch(url, {
      method: "POST",
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value,
      },
    })
      .then((response) => {
        if (!response.ok) {
          return response.json().then((data) => {
            throw new Error(data.error || "An unknown error occurred.");
          });
        }
        return response.json();
      })
      .then((data) => {
        // Inject messages into the existing structure
        const messageContainer = document.querySelector(".container");
        messageContainer.innerHTML = ""; // Clear existing messages

        if (data.messages && Array.isArray(data.messages)) {
          data.messages.forEach((msg) => {
            const alertDiv = document.createElement("div");
            alertDiv.className = `alert alert-${msg.tags} alert-dismissible fade show`;
            alertDiv.setAttribute("role", "alert");
            alertDiv.innerHTML = `
              ${msg.message}
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="alert"
                aria-label="Close"
              ></button>
            `;
            messageContainer.appendChild(alertDiv);
          });
        } else {
          console.warn("No messages found in the response.");
        }

        console.log("Update successful!", data);

        // Redirect to the detail page if redirect_url is provided
        if (data.redirect_url) {
          window.location.href = data.redirect_url;
        }
      })

      .catch((error) => {
        console.error("AJAX Error:", error.message);

        const errorModalBody = document.getElementById("errorModalBody");
        errorModalBody.textContent = error.message;

        const errorModal = new bootstrap.Modal(
          document.getElementById("errorModal")
        );
        errorModal.show();
      });
  });
});
