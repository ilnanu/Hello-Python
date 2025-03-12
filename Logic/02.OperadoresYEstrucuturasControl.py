# Ejercicio Operadores + Estrucuturas de Control

my_number = 10

while my_number < 56:
    if (my_number % 2 == 0) and (my_number != 16) and (my_number % 3 != 0):
        print(my_number)
    my_number += 1

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)