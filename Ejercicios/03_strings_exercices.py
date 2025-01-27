# 1. Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len().
text = "Aprendiendo Python"
print(len(text))

# 2. Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
text2 = "Hola " + "Python"
print(text2)

# 3. Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
text_salto = "Hola\nPython"
print(text_salto)

# 4. Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
nombre, apellido, edad = "Brais", "Moure", 37
print(f"Mi nombre es {nombre} {apellido} y tengo {edad} años")

# 5. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
language_slice = "Python"
a, b, c, d, e, f = language_slice
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# 6. Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
lenguaje = "Programación"
language_slice = lenguaje[3:7]
print(language_slice)

# 7. Invierte la cadena “Python” usando slicing y muestra el resultado.
reverse_language = lenguaje[::-1]
print(reverse_language)

# 8. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
cadena = "aprendiendo python"
print(cadena.upper())

# 9. Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
cadena2 = "Programación en Python"
print(cadena2.count("n"))

# 10. Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
cadena3 = "12345"
print(cadena3.isnumeric())
