$(function(){                          // jQuery function
    $('#formulario_anadir_capitulo').hide();
    $('#anadir').click(function() {
      $('#formulario_anadir_capitulo').show();
    });

    $('#boton_anadir_capitulo').click(
      function(){
        form_data = $('#formulario_anadir_capitulo').serializeArray()
        $.ajax({
          url: "/episodio",
          data: JSON.stringify({
              "name": form_data[0].value,
              "season": form_data[1].value,
              "number": form_data[2].value,
              "summary": form_data[3].value,
              "image": {
                "medium": form_data[4].value,
                "original": form_data[5].value
              }
          }),
          type: "POST",
          dataType: "json",
          error : function(xhr, status) {
            alert('Disculpe, existió un problema\n' + xhr );
          },

          success : function(json) {
            console.log(json)
          }
        })
      }
    )
 });