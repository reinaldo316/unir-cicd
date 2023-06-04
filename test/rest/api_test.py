import http.client  # Importa el módulo http.client para realizar solicitudes HTTP
import os  # Importa el módulo os para acceder a variables de entorno y funcionalidades del sistema operativo
import unittest  # Importa el módulo unittest para pruebas unitarias
from urllib.request import urlopen  # Importa la función urlopen del módulo urllib.request para  solicitudes HTTP
from urllib.error import HTTPError
import pytest  # Importa el módulo pytest para extender las capacidades de prueba

BASE_URL = os.environ.get("BASE_URL")  # Obtiene el valor de la variable de entorno BASE_URL
DEFAULT_TIMEOUT = 2  # Define el tiempo de espera 

@pytest.mark.api  
class TestApi(unittest.TestCase):
    def setUp(self):
        # Configura el entorno de prueba antes de cada método de prueba
        self.assertIsNotNone(BASE_URL, "URL no configurada")  # Verifica que BASE_URL no sea None
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")  # Verifica que BASE_URL tenga una longitud mayor a 8

    def test_api_add(self):
        # Prueba el endpoint "/calc/add" de la API
        url = f"{BASE_URL}/calc/add/2/2"  # Construye la URL para la solicitud
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)  # Realiza una solicitud HTTP a la URL
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )  # Verifica que el estado de la respuesta sea 200 (OK)

    def test_api_substract(self):
        # Prueba el endpoint "/calc/substract" de la API
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        ) # Verifica que el estado de la respuesta sea 200 (OK)

    def test_api_multiply(self):
        # Prueba el endpoint "/calc/multiply" de la API
        url = f"{BASE_URL}/calc/multiply/4/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        ) # Verifica que el estado de la respuesta sea 200 (OK)

    def test_api_divide(self):
        # Prueba el endpoint "/calc/divide" de la API
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        ) # Verifica que el estado de la respuesta sea 200 (OK)

    def test_api_power(self):
        # Prueba el endpoint "/calc/power" de la API
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        ) # Verifica que el estado de la respuesta sea 200 (OK)

    def test_api_square_root(self):
        # Prueba el endpoint "/calc/square_root" de la API
        url = f"{BASE_URL}/calc/square_root/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        ) # Verifica que el estado de la respuesta sea 200 (OK)

    def test_api_logarithm(self):
        # Prueba el endpoint "/calc/logarithm" de la API
        url = f"{BASE_URL}/calc/logarithm/100"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        ) # Verifica que el estado de la respuesta sea 200 (OK)


    def test_api_add_1(self):
        # Prueba el endpoint "/calc/add" de la API para la operación de suma
        url = f"{BASE_URL}/calc/add/'2'/dos"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_substract_1(self):
        # Prueba el endpoint "/calc/substract" de la API para la operación de resta
        url = f"{BASE_URL}/calc/substract/cinco/3"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_multiply_1(self):
        # Prueba el endpoint "/calc/multiply" de la API para la operación de multiplicación
        url = f"{BASE_URL}/calc/multiply/a/2"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_divide_1(self):
        # Prueba el endpoint "/calc/divide" de la API para la operación de división
        url = f"{BASE_URL}/calc/divide/10/0"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_power_1(self):
        # Prueba el endpoint "/calc/power" de la API para la operación de potencia
        url = f"{BASE_URL}/calc/power/a/3"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_square_root_1(self):
        # Prueba el endpoint "/calc/square_root" de la API para la operación de raíz cuadrada
        url = f"{BASE_URL}/calc/square_root/-16"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")

    def test_api_logarithm_1(self):
        # Prueba el endpoint "/calc/logarithm" de la API para la operación de logaritmo
        url = f"{BASE_URL}/calc/logarithm/0"
        with self.assertRaises(HTTPError) as context:
            urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(context.exception.code, http.client.BAD_REQUEST, f"Error en la petición API a {url}")


    if __name__ == "__main__":
        unittest.main()    