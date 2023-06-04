import app  # Importa el módulo app
import math  # Módulo para realizar operaciones matemáticas

# Clase de excepción que se utiliza para representar errores relacionados con permisos no válidos.
class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)  # Verifica los tipos de x e y
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)  # Verifica los tipos de x e y
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):  # Verifica los permisos utilizando una función de app.util
            raise InvalidPermissions('User has no permissions')  # Lanza una excepción de InvalidPermissions si no se tienen permisos suficientes

        self.check_types(x, y)  # Verifica los tipos de x e y
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)  # Verifica los tipos de x e y
        if y == 0:
            raise TypeError("Division by zero is not possible")  # Lanza una excepción de TypeError si el denominador es cero

        return x / y

    def power(self, x, y):
        self.check_types(x, y)  # Verifica los tipos de x e y
        return x ** y

    def square_root(self, x):
        self.check_type(x)  # Verifica el tipo de x
        if x < 0:
            raise ValueError("Square root of a negative number is not possible")  # Lanza una excepción de TypeError si el número es negativo
        return x ** 0.5

    def logarithm(self, x):
        self.check_type(x)  # Verifica el tipo de x
        if x <= 0:
            raise ValueError("Logarithm of a non-positive number is not possible")  # Lanza una excepción de TypeError si el número es no positivo
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):  # Verifica si x e y son instancias de int o float
            raise TypeError("Parameters must be numbers")  # Lanza una excepción de TypeError si los parámetros no son números

    def check_type(self, x):
        if not isinstance(x, (int, float)):  # Verifica si x es una instancia de int o float
            raise ValueError("Parameter must be a number")  # Lanza una excepción de TypeError si el parámetro no es un número



if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()  # Crea una instancia de la clase Calculator
    result = calc.add(2, 2)  # Llama al método add de la instancia calc con los argumentos 2 y 2
    print(result)  # Imprime el resultado de la suma
