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
    
  return render_template('index.html', tituloODSDos=conn.execute(a).fetchone()[0], comoSeJuegaODSDos=conn.execute(aa).fetchone()[0], tituloODSCinco=conn.execute(b).fetchone()[0], comoSeJuegaODSCinco=conn.execute(bb).fetchone()[0], tituloODSSiete=conn.execute(c).fetchone()[0])

@app.route('/loginin')
def iniciarSesion():
  return render_template('inicioSesion.html')

@app.route('/singin')
def registrarse():
  return render_template('registrarse.html')
  
@app.route('/sorry')
def paginaNoCreada():
  return render_template('paginaNoCreada.html')
app.run(host='0.0.0.0', port=81)