$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (res) {
      const movies = res.results;

      for (let movie of movies) {
        $('#list_movies').append(`<li>${movie.title}</li>`);
      }
    }
  });
});
