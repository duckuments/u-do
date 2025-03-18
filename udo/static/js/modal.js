// TODO : send data to view for save in data toLowerCase()


document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("createProjectForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(form);
        const url = form.getAttribute("action");

        fetch(url, {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
            },
        })
        .then(response => response.json()) 
        .then(data => {
            if (data.success) {
                document.getElementById("successMessage").style.display = "block";
                form.reset(); // Reset form after successful submission
            } else {
                document.getElementById("errorMessage").style.display = "block";
            }
        })
        .catch(error => {
            document.getElementById("errorMessage").style.display = "block";
        });
    });
});

