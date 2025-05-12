from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/nombre")
def nombre():
    return "<p>Nahiara</p>"


@app.route("/apellido")
def apellido():
    return "<p>Cuella</p>"
