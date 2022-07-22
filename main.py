from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sorry')
def paginaNoCreada():
  return render_template('paginaNoCreada.html')
app.run(host='0.0.0.0', port=81)