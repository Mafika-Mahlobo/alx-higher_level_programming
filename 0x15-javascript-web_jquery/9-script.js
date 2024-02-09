$(document).ready(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    success: function (data) {
      console.log(data);
      $('#hello').text(data.hello);
    }
  });
});
