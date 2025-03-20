
# Crea una función que sea capaz de procesar parámetros, pero que también pueda lanzar 3 tipos diferentes de excepcions 
# (una de ellas tiene que corresponderse con un tipo de excepción creada por nosotros de manera personalizada, 
# y debe ser lanzada de manera manual) en caso de error.
#  Captura todas las excepciones desde el lugar donde llamas a la función.
# Imprime el tipo de error.
# Imprime si no se ha producido ningún error.
# Imprime que la ejecución ha finalizado.

# 1. Definición de excepción personalizada
class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)

# 2. Función que procesa parámetros
def procesar_parametro(param):
    if not isinstance(param, int):
        raise TypeError("El parámetro debe ser un entero")
    elif param < 0:
        raise ValueError("El parámetro no puede ser negativo")
    elif param == 0:
        raise CustomError("El parámetro no puede ser cero")  # Excepción personalizada
    return param * 2

# 3. Bloque de ejecución y manejo de excepciones
try:
    resultado = procesar_parametro(0)  # Prueba con diferentes valores
    print(f"Resultado: {resultado}")
except CustomError as ce:
    print(f"Error personalizado: {type(ce).__name__} - {ce}")
except TypeError as te:
    print(f"Error de tipo: {type(te).__name__} - {te}")
except ValueError as ve:
    print(f"Error de valor: {type(ve).__name__} - {ve}")
except Exception as e:
    print(f"Error inesperado: {type(e).__name__} - {e}")
else:
    print("No se produjeron errores")
finally:
    print("Ejecución finalizada")
