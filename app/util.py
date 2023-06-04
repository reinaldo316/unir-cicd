# pylint: disable=no-else-return

def convert_to_number(operand):
    try:
        if "." in operand:
            return float(operand)  # Convierte el operando a un número de punto flotante si contiene un punto decimal.
        else:
            return int(operand)  # Convierte el operando a un número entero si no contiene un punto decimal.

    except ValueError:
        raise TypeError("Operator cannot be converted to number")
        # Lanza una excepción de TypeError si el operando no se puede convertir a número.

def InvalidConvertToNumber(operand):
    try:
        if "." in operand:
            return (float(operand))  # Convierte el operando a un número de punto flotante si contiene un punto decimal.

        return int(operand)  # Convierte el operando a un número entero si no contiene un punto decimal.

    except ValueError:
        raise TypeError("Operator cannot be converted to number")
        # Lanza una excepción de TypeError si el operando no se puede convertir a número.

def validate_permissions(operation, user):
    print(f"checking permissions of {user} for operation {operation}")  # Imprime un mensaje para verificar los permisos de un usuario para una operación.
    return user == "user1"  # Devuelve True si el usuario tiene permisos ("user1"), de lo contrario, devuelve False.

