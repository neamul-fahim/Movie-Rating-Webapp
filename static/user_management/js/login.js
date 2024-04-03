const loginForm = document.getElementById("login-form");
loginForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const data = {
    email,
    password,
  };

  fetch("/login-API/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
  .then((response) => {
    if (!response.ok) {
      throw new Error(`Something went wrong`);
    }
    return response.json();
  })
  .then((data) => {
    localStorage.setItem("authToken", data.token);
    window.location.href = `/movie/home-page/`;
  })
    .catch((error) => {

      alert(error); 
    });
});
