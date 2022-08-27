from flask import Flask, render_template
import sqlite3

app=Flask(__name__)

@app.route('/')
def index():
  conn = sqlite3.connect('ODSGames.db')
  
  a = '''SELECT titulo FROM juegos WHERE ods=2'''
  aa = '''SELECT comoSeJuega FROM juegos WHERE ods=2'''
  b = '''SELECT titulo FROM juegos WHERE ods=5'''
  bb = '''SELECT comoSeJuega FROM juegos WHERE ods=5'''
  c = '''SELECT titulo FROM juegos WHERE ods=7'''
  cc = '''SELECT comoSeJuega FROM juegos WHERE ods=7'''
    
  return render_template('index.html', tituloODSDos=conn.execute(a).fetchone()[0], comoSeJuegaODSDos=conn.execute(aa).fetchone()[0], tituloODSCinco=conn.execute(b).fetchone()[0], comoSeJuegaODSCinco=conn.execute(bb).fetchone()[0], tituloODSSiete=conn.execute(c).fetchone()[0], comoSeJuegaODSSiete=conn.execute(cc).fetchone()[0])

@app.route('/advertencia/<int:ods>')
def advertencia(ods):
  if ods == 2:
    juego = "'ODS 2 - crucigrama'"
    enlace = "https://www.un.org/sustainabledevelopment/es/wp-content/uploads/sites/3/2016/10/2_Spanish_Why_it_Matters.pdf"
    boton = "/crucigrama"

  elif ods == 5:
    juego = "'ODS 5 - verdadero o falso'"
    enlace = "https://www.un.org/sustainabledevelopment/es/wp-content/uploads/sites/3/2016/10/5_Spanish_Why_it_Matters.pdf"
    boton = "/verdaderoOFalso"  

  else:
    ods == 7
    juego = "'ODS 7 - sopa de letras'"
    enlace = "https://www.un.org/sustainabledevelopment/es/wp-content/uploads/sites/3/2016/10/7_Spanish_Why_it_Matters.pdf"
    boton = "/sopaDeLetras"
  
  return render_template('pantallaBloqueo.html', tituloJuego=juego, pdf=enlace, url=boton)

@app.route('/verdaderoOFalso')
def verdaderoOFalso():  
  conn = sqlite3.connect('ODSGames.db')

  extraerLeyendas = '''SELECT leyenda FROM consignas WHERE ods=5'''
  leyendas = conn.execute(extraerLeyendas).fetchall()

  extraerRespuestas = '''SELECT respuesta FROM consignas WHERE ods=5'''
  respuestas = conn.execute(extraerRespuestas).fetchall()
  
  return render_template('verdaderoOFalso.html', leyendaUno=leyendas[0][0], respuestaUno=respuestas[0],leyendaDos=leyendas[1][0], respuestaDos=respuestas[1], leyendaTres=leyendas[2][0], respuestaTres=respuestas[2], leyendaCuatro=leyendas[3][0], respuestaCuatro=respuestas[3], leyendaCinco=leyendas[4][0], respuestaCinco=respuestas[4],leyendaSeis=leyendas[5][0], respuestaSeis=respuestas[5],leyendaSiete=leyendas[6][0], respuestaSiete=respuestas[6])


@app.route('/sopaDeLetras')
def sopaDeLetras():
  conn = sqlite3.connect('ODSGames.db')
  extraerPalaras = '''SELECT respuesta FROM consignas WHERE ods=7'''
  palabras = conn.execute(extraerPalaras).fetchall()
  ## aunque se consuta a la base por las palabras no pudieron ser agregadas de esa manera devido a como se explica en el html el plugin utilizado para hacer la sopa de letras no reconoce correctamente las palabras
  return render_template('sopaDeLetras.html', palabraUno=palabras[0][0], palabraDos=palabras[1][0], palabraTres=palabras[2][0], palabraCuatro=palabras[3][0], palabraCinco=palabras[4][0], palabraSeis=palabras[5][0], palabraSiete=palabras[6][0], palabraOcho=palabras[7][0], palabraNueve=palabras[8][0], palabraDiez=palabras[9][0], PalabraOnce=palabras[10][0])

@app.route('/crucigrama')
def crucigrama():
  ## generacion de tablero, no funciono pero nos dio el codigo para hacer la tabla
  ## tablero = ""
  ## for i in range(26):
  ##  tablero += "<tr>"
  ##  for a in range(23):
  ##    tablero += f'<td><input class="casilla" type="text" maxlength="1" id="fila{i+1}C{a+1}"/></td>'
  ##  tablero += "</tr>"
  conn = sqlite3.connect('ODSGames.db')

  extraerLeyendas = '''SELECT leyenda FROM consignas WHERE ods=2'''
  leyendas = conn.execute(extraerLeyendas).fetchall()
  return render_template('crucigrama.html',leyendaUno=leyendas[0][0], leyendaDos=leyendas[1][0], leyendaTres=leyendas[2][0], leyendaCuatro=leyendas[3][0], leyendaCinco=leyendas[4][0], leyendaSeis=leyendas[5][0], leyendaSiete=leyendas[6][0], leyendaOcho=leyendas[7][0],leyendaNueve=leyendas[8][0])

@app.route('/sorry')
def paginaNoCreada():
  return render_template('paginaNoCreada.html') 

## ↓ en desuso ↓ 
@app.route('/loginin')
def iniciarSesion():
  return render_template('inicioSesion.html')

@app.route('/singin')
def registrarse():
  return render_template('registrarse.html')

app.run(host='0.0.0.0', port=81)