$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function(data) {
  var titles = data.results.map(function(movie) {
    return "<li>" + movie.title + "</li>";
  });
  $("<ul/>", {
    id: "list_movies",
    html: titles.join("")
  }).appendTo("body");
});
