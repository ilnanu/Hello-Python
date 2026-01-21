# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35, 1: "Python"}

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77,
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

d = dict()
print(d)
print(type(d))

d = dict({1: "Ramesh", 2: "Suresh", 3: "Mahesh"})
print(d)

d = dict([(1, "Ramesh"), (2, "Arjun")])
print(d)


# Búsqueda

print(my_dict[1])
print(my_dict["Nombre"])

print("Moure" in my_dict)
print("Apellido" in my_dict)

# Inserción

my_dict["Calle"] = "Calle MoureDev"
print(my_dict)

# Actualización

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

# Eliminación

del my_dict["Calle"]
print(my_dict)

# Otras operaciones

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "MoureDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))

d = {1: "Ramesh", 2: "Suresh", 3: "Mahesh"}
print("Before clearing dictionary: ", d)
d.clear()
print("After cleared entries in dictionary: ", d)

d = {1: "Ramesh", 2: "Suresh", 3: "Mahesh"}
print("Before delete dictionary: ", d)
del d

d = dict([(1, "Ramesh"), (2, "Arjun")])
print("length of dictionary is: ", len(d))

d = {1: "Ramesh", 2: "Suresh", 3: "Mahesh"}
print(d.get(1))
print(d.get(100))

d = {1: "Ramesh", 2: "Suresh", 3: "Mahesh"}
print(d.get(1))
print(d.get(100, "No key found"))

d = {1: "Ramesh", 2: "Suresh", 3: "Mahesh"}
print("Before pop:", d)
d.pop(1)
print("After pop:", d)

# This method removes an arbitrary item(key-value) from the dictionary and returns it.
d = {1: "Ramesh", 2: "Suresh", 3: "Mahesh"}
print("Before popitem:", d)
d.popitem()
print("After popitem:", d)

d1 = {1: "Ramesh", 2: "Suresh", 3: "Mahesh"}
d2 = d1.copy()
print(d1)
print(d2)

squares = {a: a * a for a in range(1, 6)}
print(squares)
