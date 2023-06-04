import unittest  # Importa el módulo 'unittest' para realizar pruebas unitarias
from unittest.mock import patch  # Importa 'patch' de 'unittest.mock' para simular objetos en las pruebas
import pytest  # Importa el módulo 'pytest' para extender las capacidades de prueba
import app.util
# Clase de excepción que se utiliza para representar errores relacionados con permisos no válidos.


from app.calc import Calculator  # Importa la clase 'Calculator' desde el módulo 'app.calc'


def mocked_validation(*args, **kwargs):
    return True  # Define una función 'mocked_validation' que devuelve 'True'

def mocked_invalidation(*args, **kwargs):
    return False # Define una función 'mocked_validation' que devuelve 'True'


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    # Define una clase de prueba 'TestCalculate' que hereda de 'unittest.TestCase'

    def setUp(self):
        self.calc = Calculator()  # Crea una instancia de la clase 'Calculator' y la asigna a 'self.calc'

#En las pruebas de éxito, se utiliza self.assertEqual() para verificar que el resultado de los metodos sean el esperado en cada caso.
#En las pruebas de error, se utiliza self.assertRaises() para verificar que se lance la excepción TypeError esperada cuando se pasan parámetros no numéricos a los métodos

    def test_add_method_returns_correct_result(self):
        # Prueba que el método 'add' devuelve el resultado correcto para diferentes sumas.
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_fails_with_nan_parameter(self):
        # Prueba que el método 'add' falla cuando se le pasa un parámetro no numérico.
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_substract_method_returns_correct_result(self):
        # Prueba que el método 'substract' devuelve el resultado correcto para diferentes restas.
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(6, 2))
        self.assertEqual(-3, self.calc.substract(2, 5))

    def test_substract_method_fails_with_nan_parameter(self):
        # Prueba que el método 'substract' falla con parámetros no numéricos.
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    def test_divide_method_returns_correct_result(self):
        # Prueba que el método 'divide' devuelve el resultado correcto para diferentes divisiones.
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        # Prueba que el método 'divide' falla cuando se le pasa un parámetro no numérico.
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        # Prueba que el método 'divide' falla cuando se intenta dividir por cero.
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        # Prueba que el método 'multiply' devuelve el resultado correcto para diferentes multiplicaciones.
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_multiply_method_fails_with_nan_parameter(self):
        # Prueba que el método 'multiply' falla con parámetros no numéricos.
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    def test_power_method_returns_correct_result(self):
        # Prueba que el método 'power' devuelve el resultado correcto para diferentes potencias.
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(5, 0))
        self.assertEqual(16, self.calc.power(2, 4))

    def test_power_method_fails_with_nan_parameter(self):
        # Prueba que el método 'power' falla con parámetros no numéricos.
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())

    def test_square_root_method_returns_correct_result(self):
        # Prueba que el método 'square_root' devuelve el resultado correcto para diferentes raíces cuadradas.
        self.assertEqual(2, self.calc.square_root(4))
        self.assertEqual(3, self.calc.square_root(9))
        self.assertEqual(5, self.calc.square_root(25))

    def test_square_root_method_fails_with_negative_parameter(self):
        # Prueba que el método 'square_root' falla con parámetros negativos.
        self.assertRaises(ValueError, self.calc.square_root, -4)
        self.assertRaises(ValueError, self.calc.square_root, -9)
        self.assertRaises(ValueError, self.calc.square_root, -25)

    def test_square_root_method_fails_with_non_numeric_parameter(self):
        # Prueba que el método 'square_root' falla con parámetros no numéricos.
        self.assertRaises(ValueError, self.calc.square_root, "4")
        self.assertRaises(ValueError, self.calc.square_root, None)
        self.assertRaises(ValueError, self.calc.square_root, object())

    def test_logarithm_method_returns_correct_result(self):
        # Prueba que el método 'logarithm' devuelve el resultado correcto para diferentes logaritmos.
        self.assertAlmostEqual(0, self.calc.logarithm(1))
        self.assertAlmostEqual(1, self.calc.logarithm(10))
        self.assertAlmostEqual(2, self.calc.logarithm(100))

    def test_logarithm_method_fails_with_non_positive_parameter(self):
        # Prueba que el método 'logarithm' falla con parámetros no positivos.
        self.assertRaises(ValueError, self.calc.logarithm, 0)
        self.assertRaises(ValueError, self.calc.logarithm, -1)
        self.assertRaises(ValueError, self.calc.logarithm, -100)

    def test_logarithm_method_fails_with_non_numeric_parameter(self):
        # Prueba que el método 'logarithm' falla con parámetros no numéricos.
        self.assertRaises(ValueError, self.calc.logarithm, "10")
        self.assertRaises(ValueError, self.calc.logarithm, None)
        self.assertRaises(ValueError, self.calc.logarithm, object())

    def test_check_types_method_passes_with_numeric_parameters(self):
        # Prueba que el método 'check_types' pasa con parámetros numéricos.
        self.assertIsNone(self.calc.check_types(2, 3.5))
        self.assertIsNone(self.calc.check_types(-1, 0))

    def test_check_types_method_fails_with_non_numeric_parameters(self):
        # Prueba que el método 'check_types' falla con parámetros no numéricos.
        self.assertRaises(TypeError, self.calc.check_types, "2", 3)
        self.assertRaises(TypeError, self.calc.check_types, None, 3)
        self.assertRaises(TypeError, self.calc.check_types, 2, object())

    def test_check_types_method_fails_with_mixed_numeric_and_non_numeric_parameters(self):
        # Prueba que el método 'check_types' falla con parámetros mixtos numéricos y no numéricos.
        self.assertRaises(TypeError, self.calc.check_types, 2, "3")
        self.assertRaises(TypeError, self.calc.check_types, 2, None)
        self.assertRaises(TypeError, self.calc.check_types, 2, object())

    def test_check_type_method_passes_with_numeric_parameter(self):
        # Prueba que el método 'check_type' pasa con un parámetro numérico.
        self.assertIsNone(self.calc.check_type(2))
        self.assertIsNone(self.calc.check_type(-1.5))

    def test_check_type_method_fails_with_non_numeric_parameter(self):
        # Prueba que el método 'check_type' falla con un parámetro no numérico.
        self.assertRaises(ValueError, self.calc.check_type, "2")
        self.assertRaises(ValueError, self.calc.check_type, None)
        self.assertRaises(ValueError, self.calc.check_type, object())

if __name__ == "__main__":  # pragma: no cover
    unittest.main()

