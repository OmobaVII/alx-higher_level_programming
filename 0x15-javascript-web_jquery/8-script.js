// Fetches and lists the title for all movies in a url

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url,
  function (data, status) {
    const movies = data.results;
    for (const a in movies) {
      $('UL#list_movies').append('<li>' + movies[a].title + '</li>');
    }
  }
);
