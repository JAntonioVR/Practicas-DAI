$(function(){                          // jQuery function
    $('#formulario_anadir_capitulo').hide();
    $( ".formulario_modificar_episodio" ).hide();
    $('#anadir').click(function() {
      $('#formulario_anadir_capitulo').show();
    });

    $('#boton_anadir_capitulo').click(
      function(){
        form_data = $('#formulario_anadir_capitulo').serializeArray()
        nuevo_episodio = JSON.stringify({
          "name": form_data[0].value,
          "season": form_data[1].value,
          "number": form_data[2].value,
          "summary": form_data[3].value,
          "image": {
            "medium": form_data[4].value,
            "original": form_data[5].value
          }
        })
        $.ajax({
          url: "/episodio",
          data: nuevo_episodio,
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
    // FIXME
    $('#boton_buscar').click(
      function(){
        data = $('#input_buscar').val()
        $.ajax({
          url: "/consulta_api",
          data: JSON.stringify({
            "nombre": data
          }),
          type: "POST",
          dataType: "json",
          error : function(xhr, status) {
            alert('Disculpe, existió un problema\n' + xhr );
          },

          success : function(json) {
            $('#titulo_resultado_api').html("<h3>Resultados de la búsqueda con \"" + data + "\"</h3>")
            let salida = ""
            if (!('message' in json)) {
              salida = render_output_episodes(json)
            } else {
              $('#episodios_api').removeClass()  
              salida = "<p>" + json['message'] + "</p>"
            }
            $('#episodios_api').html(salida)
          }
        })
      }
    )

    let zoom = 100
    $('#boton_disminuir_tamano').click(
      function(){
        if(zoom > 30){
          zoom -= 5
          document.body.style.zoom = zoom.toString().concat("%")
        }
        
      }
    )
    $('#boton_aumentar_tamano').click(
      function(){
        if(zoom < 200){
          zoom += 5
          document.body.style.zoom = zoom.toString().concat("%")
        }
        
      }
    )

 });

function render_output_episodes(episodios){
  let salida = ""
  if(episodios.length > 0){
    for (let i = 0; i < episodios.length; i++) {
      const episodio = episodios[i];
      salida += 
      "<div class=\"col\">" +
        "<div class=\"episodio\">" +
          "<a href=\"" + episodio['url'] + "\">"
          if (episodio['image'] != null && episodio['image']['medium'] != null) {
            salida += "<img src=\""+ episodio['image']['medium'] + "\">"
          }
          salida += 
            "<p>" + episodio['name'] + "</p>" +
          "</a>" +
        "</div>" +
      "</div>"
    }
  }
  return salida
}

function mostrar_formulario(id){
  $('#formulario_modificar_capitulo_'.concat(id)).show()
}

function modify_cap(id){
  form_data = $('#formulario_modificar_capitulo_'.concat(id)).serializeArray()
  $.ajax({
    url: "/episodio",
    data: JSON.stringify({
        "id": parseInt(form_data[0].value),
        "name": form_data[1].value,
        "season": parseInt(form_data[2].value),
        "number": parseInt(form_data[3].value),
        "summary": form_data[4].value,
        "image": {
          "medium": form_data[5].value,
          "original": form_data[6].value
        }
    }),
    type: "PUT",
    dataType: "json",
    error : function(xhr, status) {
      alert('Disculpe, existió un problema\n' + xhr );
    },
    success : function(json) {
      $('#titulo_resultado_api').html("<h3>Resultado de la modificación:</h3>")
      let salida = ""
      if(!('message' in json)){
        $('#titulo_resultado_api').append("<p>Se ha modificado el siguiente episodio:</p>")
        salida = render_output_episodes([json])
      } else{
        $('#episodios_api').removeClass()  
        salida = "<p>" + json['message'] + "</p>"
      }
      $('#episodios_api').html(salida)
      $('html, body').animate({ scrollTop: 0 }, 'fast')
    }
  })
}

function delete_cap(id){
  $.ajax({
    url: "/episodio",
    data: JSON.stringify({
      "id": parseInt(id)
    }),
    type: "DELETE",
    dataType: "json",
    error : function(xhr, status) {
      alert('Disculpe, existió un problema\n' + xhr );
    },

    success : function(json) {
      alert(json)
      location.reload()
    }
  })
}



 $(document).ready(function(){

  // This code uses `localStorage` to save "user prefers color" persistently
  // This key used is `user-prefers-color`, and should be one of:
  //  0 = only used at first trigger, to indicate firts time selection
  //  1 = user wants light mode
  //  2 = user wants dark mode
  // the key can also be deleted to indicate user has no preference.

  // function to toggle the css
  function toggle_color_scheme_css($mode) {
    // amend the body classes
    if ($mode == 'dark') {
      $("html").removeClass('light').addClass("dark");
    } else {
      $("html").removeClass("dark").addClass('light');
    }
    // if on user prefers color then update stored value
    $upc = window.localStorage.getItem('user-prefers-color');
    if ($upc !== null) {
      if ($upc == 0) $("#css-save-btn").prop( "checked", true );  // first time click
      window.localStorage.setItem('user-prefers-color', ($mode == 'dark') ? 2 : 1);
    }
  }

  // function / listener action to toggle the button
  function update_color_scheme_css() {
    $upc = window.localStorage.getItem('user-prefers-color');
    if (($upc === null) || ($upc == 0)) {
      $mode = (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches) ? 'dark' : 'light';
    } else {
      $mode = ($upc == 2) ? 'dark' : 'light';
    }
    $("#css-toggle-btn").prop( "checked", ('dark' == $mode) );
    toggle_color_scheme_css($mode);
  }

  // initial mode discovery & update button
  update_color_scheme_css();
  if (window.localStorage.getItem('user-prefers-color') !== null)
    $("#css-save-btn").prop( "checked", true );

  // update every time it changes
  if (window.matchMedia) window.matchMedia("(prefers-color-scheme: dark)").addListener( update_color_scheme_css );

  // toggle button click code
  $("#css-toggle-btn").bind("click", function() {
    // disable further automatic toggles
    if (window.localStorage.getItem('user-prefers-color') === null)
      window.localStorage.setItem('user-prefers-color', 0);
    // get current mode, i.e. does body have the `.dark`` classname
    $mode = $("html").hasClass("dark") ? 'light' : 'dark';
    toggle_color_scheme_css($mode);
  });

  // toggle button click code
  $("#css-save-btn").bind("click", function() {
    $chk = $("#css-save-btn").prop("checked");
    if ($chk) {
      // user wants persistance, save current state
      $upc = $("html").hasClass("dark") ? 2 : 1;
      window.localStorage.setItem("user-prefers-color", $upc);
    } else {
      // user doesn't want pesistace, delete saved key
      window.localStorage.removeItem("user-prefers-color");
    }
  });

});