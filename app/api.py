import http.client  # Módulo para realizar operaciones HTTP
import math  # Módulo para realizar operaciones matemáticas

from flask import Flask  # Importa la clase Flask del framework Flask

from app import util  # Importa el módulo util desde el paquete app
from app.calc import Calculator  # Importa la clase Calculator desde el módulo calc del paquete app

CALCULATOR = Calculator()  # Instancia un objeto de la clase Calculator
api_application = Flask(__name__)  # Crea una instancia de la aplicación Flask
HEADERS = {"Content-Type": "text/plain", "Access-Control-Allow-Origin": "*"}  # Encabezados de la respuesta HTTP

# Ruta principal
@api_application.route("/")
def hello():
    return "Hello from The Calculator!\n"


#En todas las rutas se realiza la conversión del parámetro num a un número utilizando el método convert_to_number del módulo util. 
#En todas las rutas si ocurre algún error de tipo (TypeError), se captura y se devuelve una respuesta de error con el código HTTP 400 (BAD_REQUEST).

# Ruta para la operación de suma
@api_application.route("/calc/add/<op_1>/<op_2>", methods=["GET"])
def add(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.add(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

# Ruta para la operación de resta
@api_application.route("/calc/substract/<op_1>/<op_2>", methods=["GET"])
def substract(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.substract(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

# Ruta para la operación de multiplicación
@api_application.route("/calc/multiply/<op_1>/<op_2>", methods=["GET"])
def multiply(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.multiply(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

# Ruta para la operación de división
@api_application.route("/calc/divide/<op_1>/<op_2>", methods=["GET"])
def divide(op_1, op_2):
    try:
        num_1, num_2 = util.convert_to_number(op_1), util.convert_to_number(op_2)
        return ("{}".format(CALCULATOR.divide(num_1, num_2)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

# Ruta para la operación de potencia
@api_application.route("/calc/power/<base>/<exponent>", methods=["GET"])
def power(base, exponent):
    try:
        base, exponent = util.convert_to_number(base), util.convert_to_number(exponent)
        return ("{}".format(CALCULATOR.power(base, exponent)), http.client.OK, HEADERS)
    except TypeError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

# Ruta para la operación de raíz cuadrada
@api_application.route("/calc/square_root/<num>", methods=["GET"])
def square_root(num):
    try:
        num = util.convert_to_number(num)
        return ("{}".format(math.sqrt(num)), http.client.OK, HEADERS)
    except ValueError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

# Ruta para la operación de logaritmo
@api_application.route("/calc/logarithm/<num>", methods=["GET"])
def logarithm(num):
    try:
        num = util.convert_to_number(num)
        return ("{}".format(math.log10(num)), http.client.OK, HEADERS)
    except ValueError as e:
        return (str(e), http.client.BAD_REQUEST, HEADERS)

