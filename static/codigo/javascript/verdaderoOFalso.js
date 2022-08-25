var preguntasVF = 7;
var aciertosVF = 0;
var agregarJustificacion = document.getElementById("listadoErroresVF");
var respuestaCorrecta="";
var justificacion="";
var elementoAOcultarVF="";
var elementoAMostrarVF="";

function corroborar(respuesta) {
  /*busca pregunta para saber que hacer*/
  if(document.getElementById("leyendaUnoVF").hidden==false){
    respuestaCorrecta=document.getElementById("respuestaUnoVF")
    justificacion="- Verdadero, El 35% de las mujeres en todo el mundo ha sufrido violencia de genero, ya sea violencia fisica o sexual."
    elementoAOcultarVF=("leyendaUnoVF")
    elementoAMostrarVF=("leyendaDosVF")
    
  } else if(document.getElementById("leyendaDosVF").hidden==false){
    respuestaCorrecta=document.getElementById("respuestaDosVF")
    justificacion="- Verdadero, La desigualdad de genero provoca el estancamiento social."
    elementoAOcultarVF=("leyendaDosVF")
    elementoAMostrarVF=("leyendaTresVF")
    
  } else if(document.getElementById("leyendaTresVF").hidden==false){
    respuestaCorrecta=document.getElementById("respuestaTresVF")
    justificacion="- Falso, las niñas no poseen un acceso a esto, por lo que hace que aumente la tasa de mortalidad"
    elementoAOcultarVF=("leyendaTresVF")
    elementoAMostrarVF=("leyendaCuatroVF")
    
  } else if(document.getElementById("leyendaCuatroVF").hidden==false){
    respuestaCorrecta=document.getElementById("respuestaCuatroVF")
    justificacion="- Falso, miles de mujeres menores contraen matrimonio cada año"
    elementoAOcultarVF=("leyendaCuatroVF")
    elementoAMostrarVF=("leyendaCincoVF")
  
  }else if(document.getElementById("leyendaCincoVF").hidden==false){
    respuestaCorrecta=document.getElementById("respuestaCincoVF")
    justificacion="- Verdadero, El casamiento joven afecta la educaciòn de las niñas."
    elementoAOcultarVF=("leyendaCincoVF")
    elementoAMostrarVF=("leyendaSeisVF")
  
  }else if(document.getElementById("leyendaSeisVF").hidden==false){
    respuestaCorrecta=document.getElementById("respuestaSeisVF")
    justificacion="- Falso, En Asia,Africa subsahariana y Oceania tienen dificultados para matricularse tanto en escuelas primaraias como secundarias."
    elementoAOcultarVF=("leyendaSeisVF")
    elementoAMostrarVF=("leyendaSieteVF")
  
  } else {
  respuestaCorrecta=document.getElementById("respuestaSieteVF")
  justificacion="- Verdadero, En promedio al rededor del mundo las mujeres ganan un 24% menos que los hombres."
  elementoAOcultarVF=("leyendaSieteVF")
  elementoAMostrarVF=("resultadosFinales")
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