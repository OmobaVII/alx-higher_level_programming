// Fetches from url and displays the value from the hello to div #hello

$(document).ready(function () {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, function (data, status) {
    $('#hello').text(data.hello);
  });
});
