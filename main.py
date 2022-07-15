from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/juego1')
def juego1():
  
app.run(host='0.0.0.0', port=81)
