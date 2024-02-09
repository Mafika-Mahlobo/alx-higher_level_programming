$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  type: 'GET',
  success: function (data) {
    const datalist = $('#list_movies');
    datalist.empty();

    data.results.forEach(function (item) {
      datalist.append($('<div>').text(item.title));
    });
  }
});
