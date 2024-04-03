
const signupForm = document.getElementById("signup-form");
signupForm.addEventListener("submit", (event) => {
  event.preventDefault(); 

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const phone = document.getElementById("phone").value;
  const password = document.getElementById("password").value;

  const data = {
    name,
    email,
    phone,
    password,
  };

  fetch("/signup-API/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json", 
    },
    body: JSON.stringify(data), 
  }).then((response)=>{
     if (!response.ok){
      throw new Error("Something went wrong");
     }
     window.location.href='/'
  }).catch((error) => {
      alert(error); 
    });
});
