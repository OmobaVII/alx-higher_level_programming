// Fetches the character name from a url and displays the name in a the tag character
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url,
  function (data, status) {
    $('DIV#character').append(data.name);
  }
);
