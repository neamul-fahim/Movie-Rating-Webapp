const movieId = document.getElementById("movieId").value; // Extract movie ID from H1
const userId = document.getElementById("userId").value; // Extract movie ID from H1
console.log('movie_id',userId)
const movieDetailsEl = document.getElementById('movie-details');
const ratingForm = document.getElementById('rating-form');
const messageEl = document.getElementById('message');

// Fetch movie details using the movie ID (replace with your actual API endpoint URL)
const userToken = localStorage.getItem("authToken");
fetch(`/movie/movie-API/${movieId}/`,
{
    method:'GET',
    headers:{
      "Content-Type": "application/json",
      Authorization: `Token ${userToken}`,
    }
  }
).then(response => {
    if (!response.ok) {
        throw new Error('Failed to fetch movie details');
      }
      return  response.json()

}).then(data => {
    const movieDetails = `
      <p>Title: ${data.name}</p>
      <p>Genre: ${data.genre}</p>
      <p>Release Date: ${data.release_date}</p>
      <p>Average Rating: ${data.average_rating}</p>
    `;

    movieDetailsEl.innerHTML = movieDetails;
  }).catch(error => {
    console.error('Error fetching movie details:', error);
    window.location.href = "/"
  });

ratingForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const ratingValue = document.getElementById('rating').value;

  try {
    const userToken = localStorage.getItem("authToken");
    const response = await fetch('/movie/add-rating-API/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${userToken}`,

      },
      body: JSON.stringify({ movie: movieId, user: userId,rating: ratingValue })
    });

    if (!response.ok) {
      throw new Error('Failed to submit rating');
    }

    messageEl.textContent = 'Rating submitted successfully!';
    location.reload();
} catch (error) {
    messageEl.textContent = 'Error submitting rating: ' + error.message;
    window.location.href='/'
  }
});
