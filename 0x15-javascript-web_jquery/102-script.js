$(document).ready(function () {
  $('#btn_translate').click(function () {
    const code = $('#language_code').val();
    const apiurl = 'https://hellosalut.stefanbohacek.dev/' + '?lang=' + code;
    $.ajax({
      url: apiurl,
      type: 'GET',
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  });
});
