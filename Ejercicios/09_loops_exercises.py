# 1. Usa un bucle while para imprimir los números del 1 al 10.
i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Usa un bucle for para recorrer la lista[10, 20, 30, 40, 50] e imprime cada número.
my_lista = [10, 20, 30, 40, 50]
for number in my_lista:
    print(number)

# 3. Escribe un programa que use un bucle while para sumar los números del 1 al 100 e imprime el resultado.
i_number = 1
sum_number = 0
while i_number <= 100:
    sum_number += i_number
    i_number += 1
print(sum_number)

# 4. Escribe un bucle for que imprima cada carácter de la cadena "Python".
for letter in "Python":
    print(letter)   

# 5. Usa un bucle while para encontrar el primer número divisible por 7 entre 1 y 50.
i_number = 1
while i_number <= 50:
    if i_number % 7 == 0:
        print(i_number)
        break
    i_number += 1

# 6. Usa un bucle for para recorrer el diccionario {"name": "Brais", "age": 37, "country": "Galicia"} e imprime las claves.
for key in {"name": "Brais", "age": 37, "country": "Galicia"}:
    print(key)  

# 7. Escribe un programa que use un bucle while para imprimir los números pares entre 1 y 20.
i_number = 1
while i_number <= 20:
    if i_number % 2 == 0:
        print(i_number)
    i_number += 1

# 8. Usa un bucle for con la función range() para imprimir los números del 1 al 10 en orden inverso.
for i in range(10, 0, -1):
    print(i)

# 9. Escribe un programa que use un bucle for para contar cuántas veces aparece el número 30 en la lista[30, 10, 30, 20, 30, 40].
count_number = 0
for number in [30, 10, 30, 20, 30, 40]:
    if number == 30:
        count_number += 1
print(count_number)   
        
# 10. Usa un bucle for para recorrer una lista de nombres y detener el bucle cuando se encuentre el nombre "Brais".
my_lista = ["Ana", "Carlos", "Brais", "David", "Elena"]
for name in my_lista:
    print(name)
    if name == "Brais":
        break
    