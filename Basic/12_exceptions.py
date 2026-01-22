# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=32030

### Exception Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

# Excepción base: try except

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error")

# Flujo completo de una excepción: try except else finally

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally:  # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)


# DotNetTutorials Examples
print('One')
print('Two')

try:
   print(10/0)
except ZeroDivisionError:
   print("Exception passed")
print('Four')
print('Five')


print('One')
print('Two')

"""
try:
   print(10/2)
   print("No Exception")
except ZeroDivisionError:
   print("Exception passed")
print('Four')
print('Five')

print(10/0)


try:
   print(10/2)
   print("No Exception")
except ZeroDivisionError:
   print("Exception passed")
print('Four')
print('Five')

print('One')
print('Two')
try:
   print(10/0)
   print("No Exception")
except ZeroDivisionError:
   print("Exception passed")
print('Four')
print('Five')


try:
   print(10/0)
   print("No Exception")
except TypeError:
   print("Exception passed")
print('Four')
print('Five')


try:
   x=int(input("Enter First Number: "))
   y=int(input("Enter Second Number: "))
   print(x/y)
except ZeroDivisionError:
   print("Can't Divide with Zero")
except ValueError:
   print("please provide int value only")

   
try:
   x=int(input("Enter First Number: "))
   y=int(input("Enter Second Number: "))
   print(x/y)
except (ZeroDivisionError,ValueError) as e:
   print("Please Provide valid numbers only and problem is: ", e)

try:
   x=int(input("Enter First Number: "))
   y=int(input("Enter Second Number: "))
   print(x/y)
except ZeroDivisionError:
   print("ZeroDivisionError: Can't divide with zero")
except:
   print("Default Except: Please provide valid input only")


  
"""

try:
   print("try block")
except:
   print("except block")
finally:
   print("finally block")


print("One")
print("Two")
try:
   print("try block")
   print(10/0)
except ZeroDivisionError:
   print("except block: Handling code")
finally:
   print("finally block: clean-up activities")
print("Four")

try:
   print("outer try block")
   print(10/0)
   try:
       print("Inner try block")
   except ZeroDivisionError:
       print("Inner except block")
   finally:
       print("Inner finally block")
except:
   print("outer except block")
finally:
   print("outer finally block")

try:
   print("try block")

except:
   print("except: Handling code")
else:
   print("else block")

class NegativeError(Exception):
   def __init__(self, data):
       self.data = data

"""
try:
   x = int(input("Enter a number between positive integer: "))
   if x < 0:
       raise NegativeError(x)
except NegativeError as e:
   print("You provided {}. Please provide positive integer values only".format(e))

"""
class TooYoungException(Exception):
   def __init__(self, arg):
       self.msg=arg
class TooOldException(Exception):
   def __init__(self, arg):
       self.msg=arg

age=int(input("Enter Age:"))
if age>60:
   raise TooOldException("Your age already crossed marriage age...no chance of getting marriage")
elif age<18:
   raise TooYoungException("Plz wait some more time you will get best match soon!!!")
else:
   print("You will get match details soon by email!!!")
   
