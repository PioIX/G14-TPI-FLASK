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
    boton = "/sorry"

  elif ods == 5:
    juego = "'ODS 5 - verdadero o falso'"
    enlace = "https://www.un.org/sustainabledevelopment/es/wp-content/uploads/sites/3/2016/10/5_Spanish_Why_it_Matters.pdf"
    boton = "/verdaderoOFalso"  

  else:
    juego = "'ODS 7 - sopa de letras'"
    enlace = "https://www.un.org/sustainabledevelopment/es/wp-content/uploads/sites/3/2016/10/7_Spanish_Why_it_Matters.pdf"
    boton = "/sorry"
  
  return render_template('pantallaBloqueo.html', tituloJuego=juego, pdf=enlace, url=boton)

@app.route('/verdaderoOFalso')
def verdaderoOFalso():  
  conn = sqlite3.connect('ODSGames.db')

  extraerLeyendas = '''SELECT leyenda FROM consignas WHERE ods=5'''
  leyendas = conn.execute(extraerLeyendas).fetchall()

  extraerRespuestas = '''SELECT respuesta FROM consignas WHERE ods=5'''
  respuestas = conn.execute(extraerRespuestas).fetchall()
  
  return render_template('verdaderoOFalso.html', leyendaUno=leyendas[0], respuestaUno=respuestas[0])
  
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