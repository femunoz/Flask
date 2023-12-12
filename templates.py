from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('plantilla2.html', name=name)