var preguntasVF = 1;
var aciertosVF = 0;
var agregarJustificacion = document.getElementById("listadoErroresVF") 
function corroborar(respuesta) {
  /*busca pregunta para saber que hacer*/
  if(document.getElementById("leyendaUnoVF").hidden==false){
    var respuestaCorrecta=document.getElementById("respuestaUnoVF")
    var justificacion="Verdadero, El 35% de las mujeres en todo el mundo ha sufrido violencia de genero, ya sea violencia fisica o sexual."
    var elementoAOcultarVF=("leyendaUnoVF")
    var elementoAMostrarVF=("resultadosFinales")
  }

  /*compara con los datos recopilados y agrega con los mismos*/
  if(respuestaCorrecta.innerHTML.includes(respuesta)){
    aciertosVF++
    document.getElementById([elementoAOcultarVF]).hidden=true
    document.getElementById([elementoAMostrarVF]).hidden=false
  } else {
    document.getElementById([elementoAOcultarVF]).hidden=true
    document.getElementById("errores").hidden=false
    agregarJustificacion.innerHTML += `<li>${justificacion}</li>`
    document.getElementById([elementoAMostrarVF]).hidden=false
  }

  /*actializa datos pestaña final*/
  if(document.getElementById("resultadosFinales").hidden==false){
    document.getElementById("puntajeVF").innerHTML += ` ${aciertosVF}/${preguntasVF}`
    document.getElementById("botonesVF").hidden = true
  }
}