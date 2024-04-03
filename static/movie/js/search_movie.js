document
        .getElementById("search-form")
        .addEventListener("submit", function (event) {
          event.preventDefault();
          const searchInput = document.getElementById("search-input").value;
          const userToken = localStorage.getItem("authToken");
          fetch(
            `/movie/search-movie-API/?name=${encodeURIComponent(searchInput)}`,
            {
                method:'GET',
                headers:{
                  "Content-Type": "application/json",
                  Authorization: `Token ${userToken}`,
                }
              }
          )
            .then((response) =>{
                if(!response.ok){
                    throw new Error("Something Went wrong")
                }
             return response.json();
            })
            .then((data) => {
              const resultsContainer =
                document.getElementById("search-results");
              resultsContainer.innerHTML = "";
              data.forEach((movie) => {
                resultsContainer.innerHTML += `
                            <div>
                                <h3>${movie.name}</h3>
                                <p>Genre: ${movie.genre}</p>
                                <p>Rating: ${movie.rating}</p>
                                <p>Release Date: ${movie.release_date}</p>
                                <p>Average Rating: ${movie.average_rating}</p>
                            </div>
                        `;
              });
            })
            .catch((error) => {
                console.error("Error:", error)
                window.location.href="/"
            });
        });
