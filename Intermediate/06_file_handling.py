# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=15524

### File Handling ###

import xml
import csv
import json
import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("Intermediate/my_file.txt", "w+")

txt_file.write(
    "Mi nombre es Brais\nMi apellido es Moure\n35 años\nY mi lenguaje preferido es Python"
)

# print(txt_file.read())
print(txt_file.read(10))
print(txt_file.readline())
print(txt_file.readline())
for line in txt_file.readlines():
    print(line)

txt_file.write("\nAunque también me gusta Kotlin")
print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("Intermediate/my_file.txt")

# Clase en vídeo (03/11/22): https://www.twitch.tv/videos/1642512950

# .json file


json_file = open("Intermediate/my_file.json", "w+")

json_test = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev",
}

json.dump(json_test, json_file, indent=2)

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file


csv_file = open("Intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

# ¿Te atreves a practicar cómo trabajar con este tipo de ficheros?

# Ejercicios File Handling
# 1. Crea un archivo de texto y escribe en él la frase "Hola desde Python".
file_fer_txt = open("Intermediate/fer.txt", "w+")
file_fer_txt.write("Hola desde Python")
file_fer_txt.close()

# 2. Abre un archivo y lee todo su contenido.
file_fer_txt = open("Intermediate/fer.txt", "r")
print(file_fer_txt.read())
file_fer_txt.close()

# 3. Añade una nueva línea al final del archivo con el texto "Línea añadida".
file_fer_txt = open("Intermediate/fer.txt", "a")
file_fer_txt.write("\nLínea añadida")
file_fer_txt.close()

# 4. Lee solo los primeros 10 caracteres del archivo.
file_fer_txt = open("Intermediate/fer.txt", "r")
print(file_fer_txt.read(10))
file_fer_txt.close()

# 5. Usa seek para volver al inicio del archivo y leer desde ahí.
file_fer_txt = open("Intermediate/fer.txt", "r")
file_fer_txt.seek(0)
print(file_fer_txt.read())
file_fer_txt.close()

# 6. Lee e imprime el contenido línea por línea usando readline.
file_fer_txt = open("Intermediate/fer.txt", "r")
print(file_fer_txt.readline())
print(file_fer_txt.readline())
print(file_fer_txt.readline())
file_fer_txt.close()

# 7. Lee todas las líneas del archivo en una lista y recórrelas con un bucle.
file_fer_txt = open("Intermediate/fer.txt", "r")
lines = file_fer_txt.readlines()
for line in lines:
    print(line)
file_fer_txt.close()

# 8. Crea un archivo nuevo que sobrescriba si ya existe, y escribe varias líneas.
file_fer_txt = open("Intermediate/fer.txt", "w+")
file_fer_txt.write("Línea 1\nLínea 2\nLínea 3")
file_fer_txt.close()


# 9. Usa una función para abrir un archivo, escribir texto y cerrarlo automáticamente con with.
def write_to_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)


write_to_file("Intermediate/fer.txt", "Texto escrito con función")

# 10. Lee un archivo línea por línea y muestra solo las que contienen la palabra "Python".
file_fer_txt = open("Intermediate/fer.txt", "r")
for line in file_fer_txt:
    if "Python" in line:
        print(line)
file_fer_txt.close()
# 11. Crea un archivo CSV y escribe varias filas de datos en él.
csv_file = open("Intermediate/fer.csv", "w+")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])
csv_file.close()

# 12. Lee un archivo CSV y muestra su contenido.
csv_file = open("Intermediate/fer.csv", "r")
csv_reader = csv.reader(csv_file)
for row in csv_reader:
    print(row)
csv_file.close()

# 13. Crea un archivo JSON y escribe un diccionario en él.
json_file = open("Intermediate/fer.json", "w+")
json_test = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://moure.dev",
}
json.dump(json_test, json_file, indent=2)
json_file.close()
# 14. Lee un archivo JSON y muestra su contenido.
json_file = open("Intermediate/fer.json", "r")
json_dict = json.load(json_file)
print(json_dict)
print(type(json_dict))
print(json_dict["name"])
json_file.close()
# 15. Crea un archivo XML y escribe un documento XML básico en él.
xml_file = open("Intermediate/fer.xml", "w+")
xml_file.write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<root>\n\t<name>Brais</name>\n\t<surname>Moure</surname>\n\t<age>35</age>\n</root>'
)
xml_file.close()
# 16. Lee un archivo XML y muestra su contenido.
xml_file = open("Intermediate/fer.xml", "r")
xml_content = xml_file.read()
print(xml_content)
xml_file.close()


##DotNetTutorials Examples
f = open("abc.txt", "w")
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Readable: ", f.readable())
print("Is File Writable: ", f.writable())
print("Is File Closed : ", f.closed)
f.close()
print("Is File Closed : ", f.closed)

f = open("wish.txt", "w")
f.write("Welcome\n")
f.write("to\n")
f.write("python world\n")
print("Data written to the file successfully")
f.close()

f = open("wish.txt", "a")
f.write("Welcome\n")
f.write("to\n")
f.write("python world\n")
print("Data written to the file successfully")
f.close()

f = open("wish.txt", "a")
f.write("Welcome ")
f.write("to ")
f.write("python world")
print("Data written to the file successfully")
f.close()

f = open("names.txt", "w")
list = ["Ramesh\n", "Arjun\n", "Senthil\n", "Vignesh"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()

f = open("abc.txt", "r")
data = f.read()
print(data)
f.close()

f = open("abc.txt", "r")
line1 = f.readline()
print(line1, end="")
line2 = f.readline()
print(line2, end="")
line3 = f.readline()
print(line3, end="")
f.close()

f = open("abc.txt", "r")
lines = f.readlines()
for line in lines:
    print(line, end="")
f.close()

with open("test.txt", "w") as f:
    f.write("Welcome\n")
    f.write("to\n")
    f.write("Python\n")
    print("Is File Closed: ", f.closed)
print("Is File Closed: ", f.closed)

f = open("test.txt", "r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())

data = "SampurneshBabu movie is excellent"
f = open("abc.txt", "w")
f.write(data)
with open("abc.txt", "r+") as f:
    text = f.read()
    print(text)
    print("The Current Cursor Position: ", f.tell())
    f.seek(24)
    print("The Current Cursor Position: ", f.tell())
    f.write("Britania Bisket")
    f.seek(0)
    text = f.read()
    print("Data After Modification:")
    print(text)

"""
import os, sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
   print("File exists:", fname)
   f=open(fname, "r")
else:
   print("File does not exist:", fname)
   sys.exit(0)
print("The content of file is:")
data=f.read()
print(data)

import os, sys
fname=input("Enter File Name: ")
if os.path.isfile(fname):
   print("File exists:", fname)
   f=open(fname, "r")
else:
   print("File does not exist:", fname)
   sys.exit(0)
lcount=wcount=ccount=0
for line in f:
   lcount=lcount+1
   ccount=ccount+len(line)
   words=line.split()
   wcount=wcount+len(words)
print("The number of Lines:", lcount)
print("The number of Words:", wcount)
print("The number of Characters:", ccount)
"""

##Binary
f1 = open("thor.jpeg", "rb")
f2 = open("newpic.jpeg", "wb")
bytes = f1.read()
f2.write(bytes)
print("New Image is available with the name: newpic.jpg")

import csv

with open("emp.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["EMP NO", "EMP NAME", "EMP SAL", "EMP ADDR"])
    n = int(input("Enter Number of Employees:"))
    for i in range(n):
        eno = input("Enter Employee No:")
        ename = input("Enter Employee Name:")
        esal = input("Enter Employee Salary:")
        eaddr = input("Enter Employee Address:")
        w.writerow([eno, ename, esal, eaddr])
print("Total Employees data written to csv file successfully")

from zipfile import *

f = ZipFile("files.zip", "w", ZIP_DEFLATED)
f.write("abc.txt")
f.write("thor.jpeg")
f.write("names.txt")
f.close()
print("files.zip file created successfully")

from zipfile import *

f = ZipFile("files.zip", "r", ZIP_STORED)
names = f.namelist()
for name in names:
    print("File Name: ", name)


import os

cwd = os.getcwd()
print("Current Working Directory:", cwd)

import os

os.mkdir("mysub")
print("mysub directory created in current working directory")

import os

os.makedirs("sub1/sub2/sub3")
print("sub1 and in that sub2 and in that sub3 directories created")

import os

os.removedirs("sub1/sub2/sub3")
print("All 3 directories sub1,sub2 and sub3 removed")

import pickle


class Employee:
    def __init__(self, eno, ename, esal, eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr

    def display(self):
        print(self.eno, "\t", self.ename, "\t", self.esal, "\t", self.eaddr)


with open("emp.dat", "wb") as f:
    e = Employee(100, "Nireekshan", 1000, "Hyd")
    pickle.dump(e, f)
    print("Pickling of Employee Object completed...")
with open("emp.dat", "rb") as f:
    obj = pickle.load(f)
    print("Printing Employee Information after unpickling")
    obj.display()
