$(document).ready(() => {
  const URL = 'https://hellosalut.stefanbohacek.dev/';

  $('#btn_translate').click(() => {
    const lang = $('#language_code').val();
    const API = `${URL}?lang=${lang}`

    $.ajax({
      url: `${URL}?lang=${lang}`,
      success: (res) => {
        $('#hello').text(res.hello);
      }
    });

    $('#language_code').val('');
  });
});
