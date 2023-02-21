$(document).ready(function() {
      // function to fetch and display translation
      function fetchTranslation() {
        var languageCode = $('#language_code').val();
        $.getJSON('https://www.fourtonfish.com/hellosalut/?lang=' + languageCode, function(data) {
          $('#hello').text(data.hello);
        });
      }

      // bind click event to translate button
      $('#btn_translate').on('click', function() {
        fetchTranslation();
      });

      // bind enter key event to language code input
      $('#language_code').on('keydown', function(event) {
        if (event.keyCode == 13) {
          fetchTranslation();
          return false;
        }
      });
    });
