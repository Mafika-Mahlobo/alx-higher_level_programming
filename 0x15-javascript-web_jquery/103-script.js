$(document).ready(function () {
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      Translate();
    }
  });

  $('#btn_translate').click(function () {
    Translate();
  });

  function Translate () {
    const code = $('#language_code').val();
    const apiurl = 'https://hellosalut.stefanbohacek.dev/' + '?lang=' + code;

    $.ajax({
      url: apiurl,
      type: 'GET',
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  }
});
