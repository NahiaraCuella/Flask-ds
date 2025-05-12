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


@app.route("/saludar/<nombre>")
def saludar(nombre):
    return f"<p>Hola, {nombre}!</p>"


@app.route("/edad/<int:numero>")
def edad(numero):
    return f"<p> Edad {numero}!</p>"