# Función que calcula el factorial de un número
def factorial(number:int) -> int:
    if number == 0:
        return 1
    else:
        return number * factorial(number-1) 

print(factorial(5))

# Funcion que calcula el valor de un elemento concreto (según su posición) en la sucesión de Fibonacci
def fibonacci(number:int) -> int:
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(5))
  
    