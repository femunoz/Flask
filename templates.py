from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def bienvenida():
    return "<html><body><h2>Bienvenid@!</h2></body><html>"

@app.route('/hello/')
def hello2():
    return render_template('plantilla2.html', name="NN")
@app.route('/hello/<name>')
def hello(name="Juanito"):
    return render_template('plantilla2.html', name=name)