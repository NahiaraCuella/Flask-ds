from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"""<p>Hello, World!</p>
    <a href="{ url_for('nombre') }">Una ruta sencilla</a><br>
    <a href="{url_for('apellido')}">Una ruta sencilla</a><br>
    <a href="{url_for('saludar',nombre = "Angeles")}">Una ruta con argumento</a><br>
    <a href="{url_for('edad', numero = "18")}">Una ruta con argumento</a>   
"""


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