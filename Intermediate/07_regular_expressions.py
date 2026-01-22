# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=19762

### Regular Expressions ###

import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string))

# search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall)

# split

print(re.split(":", my_string))

# sub

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Clase en vídeo (09/11/22): https://www.twitch.tv/videos/1648023317

### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com

pattern = r"[lL]ección"
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones"
print(re.findall(pattern, my_string))

pattern = r"[0-9]"
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d"
print(re.findall(pattern, my_string))

pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))

# Ejercicios Regular Expressions
# 1. Busca si una cadena empieza por "Hola".
cadena = "Hola, ¿cómo estás?"
pattern = r"^Hola"
print(re.match(pattern, cadena))

# 2. Busca la palabra "Python" en una cadena aunque esté en minúsculas.
cadena = "Me encanta programar en python"
pattern = r"python"
print(re.search(pattern, cadena, re.I))

# 3. Encuentra todas las apariciones de la palabra "curso" en una cadena.
cadena = "Este curso es genial. El curso de Python es el mejor curso."
pattern = r"curso"
print(re.findall(pattern, cadena))

# 4. Reemplaza todas las apariciones de "lección" por "LECCIÓN".
cadena = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
pattern = r"lección"
print(re.sub(pattern, "LECCIÓN", cadena, flags=re.I))

# 5. Divide un texto en partes separadas por comas.
cadena = "manzana,pera,plátano,naranja"
pattern = r","
print(re.split(pattern, cadena))

# 6. Busca la primera palabra que comience con "A" o "a".
cadena = "Aprender Python es asombroso"
pattern = r"\b[Aa]\w*"
print(re.search(pattern, cadena))

# 7. Encuentra todas las palabras en una cadena que terminen en "ción".
cadena = "La educación es la clave para la evolución y la revolución."
pattern = r"\b\w*ción\b"
print(re.findall(pattern, cadena))

# 8. Verifica si una cadena contiene solo números.
cadena = "1234567890"
pattern = r"^\d+$"
print(re.match(pattern, cadena))

# 9. Reemplaza todos los números de una cadena por el texto "[número]".
cadena = "El año es 2023 y tengo 30 años."
pattern = r"\d+"
print(re.sub(pattern, "[número]", cadena))
cadena = "El año es 2023 y tengo 30 años."
pattern = r"\d+"
print(re.sub(pattern, "[número]", cadena))

# 10. Encuentra todas las palabras de 4 letras exactas en una cadena.
cadena = "Este es un texto con varias palabras de cuatro letras."
pattern = r"\b\w{4}\b"
print(re.findall(pattern, cadena))
# 11. Busca si una cadena contiene un número de teléfono en formato (XXX) XXX-XXXX.
cadena = "(123) 456-7890"
pattern = r"\(\d{3}\) \d{3}-\d{4}"
print(re.match(pattern, cadena))

# DotNetTutorials Examples

import re

count = 0
pattern = re.compile("ab")
matcher = pattern.finditer("abaababa")
for match in matcher:
    count += 1
    print(match.start(), "...", match.end(), "...", match.group())
    print("The number of occurrences: ", count)

import re

count = 0
matcher = re.finditer("ab", "abaababa")
for match in matcher:
    count += 1
    print(match.start(), "...", match.end(), "...", match.group())
    print("The number of occurrences: ", count)


import re

matcher = re.finditer("[abc]", "a7b@k9z")
for match in matcher:
    print(match.start(), "......", match.group())


import re

matcher = re.finditer("[^abc]", "a7b@k9z")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("[a-z]", "a7b@k9z")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("[0-9]", "a7b@k9z")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("[a-zA-Z0-9]", "a7b@k9z")
for match in matcher:
    print(match.start(), "......", match.group())


import re

matcher = re.finditer("[^a-zA-Z0-9]", "a7b@k9z")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("\s", "a7b @k9z")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("\S", "a7b @k9z")
for match in matcher:
    print(match.start(), "......", match.group())


import re

matcher = re.finditer("\d", "a7b @k9z")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("\D", "a7b @k9z")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("\w", "a7b @k9z")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("\W", "a7b @k9z")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer(".", "a7b @k9z")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("a", "abaabaaab")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("a+", "abaabaaab")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("a*", "abaabaaab")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("a?", "abaabaaab")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("a{3}", "abaabaaab")
for match in matcher:
    print(match.start(), "......", match.group())

import re

matcher = re.finditer("a{2,4}", "abaabaaab")
for match in matcher:
    print(match.start(), "......", match.group())

# match

import re

s = input("Enter pattern to check: ")
m = re.match(s, "abcabdefg")
if m != None:
    print("Match is available at the beginning of the String")
    print("Start Index:", m.start(), "and End Index:", m.end())
else:
    print("Match is not available at the beginning of the String")

# fullmatch():


import re

s = input("Enter pattern to check: ")
m = re.fullmatch(s, "ababab")
if m != None:
    print("Full String Matched")
else:
    print("Full String not Matched")

# search():


import re

s = input("Enter pattern to check: ")
m = re.search(s, "abaaaba")
if m != None:
    print("Match is available")
    print(
        "First Occurrence of match with start index:",
        m.start(),
        "and end index:",
        m.end(),
    )
else:
    print("Match is not available")

# findall():

import re

l = re.findall("[0-9]", "a7b9c5kz")
print(l)


# finditer():


import re

itr = re.finditer("[a-z]", "a7b9c5k8z")
for m in itr:
    print(m.start(), "...", m.end(), "...", m.group())

# sub():
re.sub(regex, replacement, targetstring)


import re

s = re.sub("[a-z]", "#", "a7b9c5k8z")
print(s)

# subn():

import re

t = re.subn("[a-z]", "#", "a7b9c5k8z")
print(t)
print("The Result String:", t[0])
print("The number of replacements:", t[1])

# split():

import re

l = re.split(",", "KGF,BB1,BB2")
print(l)
for t in l:
    print(t)

import re

s = "Learning Python is Very Easy"
res = re.search("^Learn", s)
if res != None:
    print("Target String starts with Learn")
else:
    print("Target String Not starts with Learn")

import re

s = "Learning Python is Very Easy"
res = re.search("Easy$", s)
if res != None:
    print("Target String ends with Easy")
else:
    print("Target String Not ends with Easy")

import re

s = "Learning Python is Very Easy"
res = re.search("easy$", s, re.IGNORECASE)
if res != None:
    print("Target String ends with Easy by ignoring case")
else:
    print("Target String Not ends with Easy by ignoring case")

import re

s = input("Enter string:")
m = re.fullmatch("[a-k][0369][a-zA-Z0-9#]*", s)
if m != None:
    print(s, "Entered regular expression is matched")
else:
    print(s, " Entered regular expression is not matched ")


import re

n = input("Enter number:")
m = re.fullmatch("[7-9]\d{9}", n)
if m != None:
    print("Valid Mobile Number")
else:
    print("Please enter valid Mobile Number")

import re

f1 = open("input.txt", "r")
f2 = open("output.txt", "w")
for line in f1:
    items = re.findall("[7-9]\d{9}", line)
    for n in items:
        f2.write(n + "\n")
print("Extracted all Mobile Numbers into output.txt")
f1.close()
f2.close()

import re

s = input("Enter Mail id:")
m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
if m != None:
    print("Valid Mail Id")
else:
    print("Invalid Mail id")
