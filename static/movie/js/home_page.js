async function fetchMovies(){
    try{
      const userToken = localStorage.getItem("authToken");
        const response= await fetch("/movie/movies-API/",
          {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              Authorization: `Token ${userToken}`,
      
            },
          }

        );
        if (!response.ok){
            throw new Error("Failed to fetch movies");
        }

        const movies= await response.json();
        return movies;
    }catch(error){
        console.error("Error fetching movies",error);
        return null;
    }

}

async function getUser(){
  try{
    const userToken = localStorage.getItem("authToken");
    const response= await fetch('/get_user/',
    {
      method:'GET',
      headers:{
        "Content-Type": "application/json",
        Authorization: `Token ${userToken}`,
      }
    }
    );
   if(!response.ok){
    throw new Error("Not Authenticated")
   }    
    const userData= await response.json();

    return userData.user;
  }catch(error){
    console.error("Error fetching movies",error);
    window.location.href = '/'
  }
}

async function displayMovies(){
    const movieContainer= document.getElementById("movie-container");
    const loginContainer = document.getElementById("login-username");
    const navbar=document.querySelector(".navbar-menu")

    const movies = await fetchMovies();
    const user = await getUser();
    console.log("userid--------",user)
    
    if(movies && movies.length > 0){
        movies.forEach((movie)=>{
            const movieCard=document.createElement("div");
            movieCard.setAttribute('class','movie-card');
            const formattedDate = new Date(movie.release_date)
          .toISOString()
          .split("T")[0];
            movieCard.innerHTML=`
              <div class="movie-header">
               <h2>Movie name: ${movie.name}</h2>
               <p class="article-title"> Genre: ${movie.genre}</p>
               <p class="article-date">Release_date: ${formattedDate} </p>
               <p class="article-date">Rating: ${movie.rating} </p>
               <a href="/movie/rate-movie-page/${movie.id}/${user.id}/" class="rate-movie-btn">Rate Movie</a>  </div>

            `;
            movieContainer.appendChild(movieCard);
        })
    }




    loginContainer.innerHTML = "";

    if (user && user.name) {
      // If user is authenticated, show user's name and logout button
      const usernameContainer = document.createElement("div");
      usernameContainer.classList.add("username-container");
  
      const usernameLink = document.createElement("a");
      usernameLink.textContent = user.name;
      usernameLink.classList.add("username");
      usernameLink.href = "/user_profile_page/"; // Link to user profile page
  
      const logoutButton = document.createElement("button");
      logoutButton.textContent = "Logout";
      logoutButton.classList.add("logout-btn");
      logoutButton.onclick = function() {
          localStorage.removeItem('authToken');
          window.location.href="/"
      };
  
      usernameContainer.appendChild(usernameLink);
      usernameContainer.appendChild(logoutButton);
  
      loginContainer.appendChild(usernameContainer);
  }else{
    const usernameContainer = document.createElement("div");
    usernameContainer.classList.add("username-container");

    const usernameLink = document.createElement("a");
    usernameLink.textContent = "User";
  }
}

document.addEventListener('DOMContentLoaded',displayMovies);