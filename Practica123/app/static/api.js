//
// ──────────────────────────────────────────────────────────────
//   :::::: api.js : :  :   :    :     :        :          :
// ──────────────────────────────────────────────────────────────
// 
// Autor: Juan Antonio Villegas Recio
// Curso 2021-2022
// Universidad de Granada

// Fichero de JavaScript que maneja la interacción entre las vistas de la app
// y la API RESTFULL. Incluye:
// - Codigo para cambiar al modo nocturno/diurno
// - Codigo para aumentar el tamaño de la letra
// - Codigo del front-end de la API RESTFULL

// Funcion que se ejecuta en cada recarga, contiene las funciones que ejecutan
// los distintos botones y otras funcionalidades necesarias desde el momento
// de la primera recarga.
$(function(){                          // jQuery function

  // Ocultar formularios mientras no se pulse el boton correspondiente
  $('#formulario_anadir_capitulo').hide();
  $( ".formulario_modificar_episodio" ).hide();

  // Mostrar formulario para añadir episodio
  $('#anadir').click(function() {
    $('#formulario_anadir_capitulo').show();
  });

  //
  // ─── AUMENTAR O DISMINUIR TAMANO DE LETRA ───────────────────────────────────────
  //

  let zoom = 100

  // Reducir tamano de letra al pulsar el boton correspondiente
  $('#boton_disminuir_tamano').click(
    function(){
      if(zoom > 30){
        zoom -= 5
        document.body.style.zoom = zoom.toString().concat("%")
      } 
    }
  )

  // Aumentar tamano de letra al pulsar el boton correspondiente
  $('#boton_aumentar_tamano').click(
    function(){
      if(zoom < 200){
        zoom += 5
        document.body.style.zoom = zoom.toString().concat("%")
      }
    }
  )
  
  //
  // ──────────────────────────────────────────────────────────────────────────── I ──────────
  //   :::::: F U N C I O N E S   F R O N T E N D : :  :   :    :     :        :          :
  // ──────────────────────────────────────────────────────────────────────────────────────
  //
  
  // A partir de aquí se mostraran las funciones que implementan el frontend de la API REST

  //
  // ────────────────────────────────────────────────────────────────────────────────────────────── II ──────────
  //   :::::: F R O N T E N D   D E   A N A D I R   Y   B U S C A R : :  :   :    :     :        :          :
  // ────────────────────────────────────────────────────────────────────────────────────────────────────────
  //

  //
  // ─── FRONTEND DE AÑADIR EPISODIO ────────────────────────────────────────────────
  // Al pulsar el boton 'añadir' del formulario para añadir episodio se ejecuta
  // esta funcion, la cual toma los valores del formulario y mediante una llamada
  // a ajax utiliza la API REST para insertar el nuevo episodio. En caso de exito
  // se visualiza un resumen del episodio introducido.

  $('#boton_anadir_capitulo').click(
    function(){

      // Obtencion de datos introducidos por el usuario
      form_data = $('#formulario_anadir_capitulo').serializeArray()

      // Llamada a ajax
      $.ajax({
        url: "/episodio",
        data: JSON.stringify({
          "name": form_data[0].value,
          "season": parseInt(form_data[1].value),
          "number": parseInt(form_data[2].value)                                                                                                                                                                                                                                                                                          ,
          "summary": form_data[3].value,
          "url": form_data[4].value,
          "image": {
            "medium": form_data[5].value,
            "original": form_data[6].value
          }
        }),
        type: "POST",
        dataType: "json",
        error : function(xhr, status) {
          alert('Disculpe, existió un problema\n' + xhr );
        },
        success : function(json) {    // Visualizacion del episodio insertado
          $('#titulo_resultado_api').html("<h3>Resultado de la inserción:</h3>")
          let salida = ""
          if(!('message' in json)){
            $('#episodios_api').addClass('row row-cols-3')
            $('#titulo_resultado_api').append("<p>Se ha añadido el siguiente episodio:</p>")
            salida = episodes_html_code([json])
          } else{
            $('#episodios_api').removeClass()  
            salida = "<p>" + json['message'] + "</p>"
          }
          $('#episodios_api').html(salida)
        }
      })
    }
  )
  
  //
  // ─── FRONTEND DE BUSCAR EPISODIOS ───────────────────────────────────────────────
  // Al pulsar el boton de  'Buscar' del buscador de episodios se ejecuta esta
  // funcion, la cual mediante una llamada a ajax utiliza la API REST para buscar
  // todos los episodios que contengan la cadena introducida en el buscador en el 
  // nombre del episodio. En caso de exito en la operacion, la funcion muestra en
  // pantalla los episodios encontrados.

  $('#boton_buscar').click(
    function(){

      // Obtencion de la cadena introducida
      data = $('#input_buscar').val()

      if(data != ''){
        // Llamada a ajax
        $.ajax({
          url: "/episodio",
          data: {
            'nombre': data
          },
          type: "GET",
          dataType: "json",
          error : function(xhr, status) {
            alert('Disculpe, existió un problema\n' + xhr );
          },

          success : function(json) {  // Visualizacion de los capitulos devueltos por la api
            $('#titulo_resultado_api').html("<h3>Resultados de la búsqueda con \"" + data + "\"</h3>")
            let salida = ""
            if (!('message' in json)) {
              $('#episodios_api').addClass('row row-cols-3')
              salida = episodes_html_code(json)
            } else {
              $('#episodios_api').removeClass()  
              salida = "<p>" + json['message'] + "</p>"
            }
            $('#episodios_api').html(salida)
          }
        })
      }
      
    }
  )
}); // Fin de la funcion que se ejecuta en cada carga

//
// ──────────────────────────────────────────────────────────────────────────────────────────────────── II ──────────
//   :::::: F R O N T E N D   D E   M O D I F I C A R   Y   B O R R A R : :  :   :    :     :        :          :
// ──────────────────────────────────────────────────────────────────────────────────────────────────────────────
//

//
// ─── FRONTEND DE MODIFICAR EPISODIO ─────────────────────────────────────────────
// Al pulsar el boton 'Modificar' del formulario de edicion de un episodio se 
// ejecuta esta funcion, la cual, especificado el campo 'id' del episodio 
// que se va a editar, obtiene los nuevos datos del episodio y mediante una
// llamada a ajax utiliza la API REST para modificar el episodio del id indicado
// con los nuevos datos. Si hay exito en la modificacion se muestra información
// del episodio modificado.

function modify_cap(id){

  // Obtencion de datos introducidos por el usuario
  form_data = $('#formulario_modificar_capitulo_'.concat(id)).serializeArray()

  // Llamada a ajax
  $.ajax({
    url: "/episodio",
    data: JSON.stringify({
        "id": parseInt(form_data[0].value),
        "name": form_data[1].value,
        "season": parseInt(form_data[2].value),
        "number": parseInt(form_data[3].value),
        "summary": form_data[4].value,
        "url": form_data[5].value,
        "image": {
          "medium": form_data[6].value,
          "original": form_data[7].value
        }
    }),
    type: "PUT",
    dataType: "json",
    error : function(xhr, status) {
      alert('Disculpe, existió un problema\n' + xhr );
    },
    success : function(json) {    // Visualizacion del capitulo modificado
      $('#titulo_resultado_api').html("<h3>Resultado de la modificación:</h3>")
      let salida = ""
      if(!('message' in json)){
        $('#episodios_api').addClass('row row-cols-3')
        $('#titulo_resultado_api').append("<p>Se ha modificado el siguiente episodio:</p>")
        salida = episodes_html_code([json])
      } else{
        $('#episodios_api').removeClass()  
        salida = "<p>" + json['message'] + "</p>"
      }
      $('#episodios_api').html(salida)
      $('html, body').animate({ scrollTop: 0 }, 'fast')
    }
  })
}

//
// ─── FRONTEND DE ELIMINAR EPISODIO ──────────────────────────────────────────────
// Al pulsar el boton 'Borrar' de un episodio se ejecuta esta funcion, la cual
// a partir del campo 'id' del episodio y mediante una llamada a ajax utiliza la
// API REST para eliminar de la base de datos el episodio seleccionado. Si hay
// exito se muestra un mensaje de alerta-.

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
      alert(json['message'])
      location.reload()
    }
  })
}

// Fin de las funciones de frontend
// ────────────────────────────────────────────────────────────────────────────────

//
// ─── FUNCIONES AUXILIARES ───────────────────────────────────────────────────────
//

// Genera el codigo HTML necesario para visualizar una lista de episodios
function episodes_html_code(episodios){
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

// Mostrar el formulario para editar un episodio cuando se pulsa el boton
// 'Editar' de un episodio
function mostrar_formulario(id){
  $('#formulario_modificar_capitulo_'.concat(id)).show()
}

//
// ─── MODO NOCTURNO ──────────────────────────────────────────────────────────────
// Código que implementa el modo nocturno
// Fuente: https://vinorodrigues.github.io/bootstrap-dark/test-nightshade.html

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