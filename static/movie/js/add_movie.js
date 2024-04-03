const movieForm = document.getElementById('movie-form');
const messageEl = document.getElementById('message');

movieForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const name = document.getElementById('name').value;
  const genre = document.getElementById('genre').value;
  const rating = document.getElementById('rating').value;
  const releaseDate = document.getElementById('release_date').value;

  const movieData = {
    name,
    genre,
    rating,
    release_date: releaseDate,
  };

  try {
    const userToken = localStorage.getItem("authToken");
    const response = await fetch('/movie/add-movie-API/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${userToken}`,

      },
      body: JSON.stringify(movieData)
    });

    if (!response.ok) {
      throw new Error('Failed to create movie');
    }

    messageEl.textContent = 'Movie created successfully!';
    movieForm.reset(); // Clear form after successful creation
  } catch (error) {
    window.location.href="/"
  }
});
