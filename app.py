from flask import Flask
import sqlite3

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

db = None


def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}


def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory


def cerrarConexion():
   global db
   db.close()
   db = None


@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
   res = cursor.fetchone()
   registros = res["cant"]
   cerrarConexion()
   return f"Hay {registros} registros en la tabla usuarios"


@app.route("/nombre-db")
def nombreDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT usuario, email FROM usuarios; ")
   res = cursor.fetchall()
   
   emails = res["email"]
   cerrarConexion()
   return f"Los nombres y los email de los usuarios son:{emails} "
