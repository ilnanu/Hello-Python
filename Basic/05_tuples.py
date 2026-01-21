# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=14711

### Tuples ###

# Definición

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_other_tuple = (35, 60, 30)

# Parenthesis is optional for tuple
one_more_tuple = 35, 60, 30

print(my_tuple)
print(type(my_tuple))
print(my_other_tuple)
print(one_more_tuple)

# Acceso a elementos y búsqueda

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError


print(my_tuple.count("Brais"))
print(my_tuple.index("Moure"))
print(my_tuple.index("Brais"))

# my_tuple[1] = 1.80 'tuple' object does not support item assignment

# Concatenación

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# Subtuplas

print(my_sum_tuple[3:6])

# Tupla mutable con conversión a lista

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "MoureDev"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined

# Operaciones

## Multiplication
t1 = (10, 20, 30)
t2 = t1 * 3
print(t2)

## Longitud
t = (10, 20, 30, 40)
print(len(t))

## Count
t = (10, 20, 10, 10, 20)
print(t.count(10))

## Index
t = (10, 20, 10, 10, 20)
print(t.index(10))
# print(t.index(30))#     #  ValueError

## Sort
t = (40, 10, 30, 20)
t1 = sorted(t)
print(t)
print(t1)

## Min y Max
t = (40, 10, 30, 20)
print(min(t))  # 10
print(max(t))  # 40

# tuple packing
a = 10
b = 20
c = 30
d = 40
t = a, b, c, d
print(t)

# tuple unpacking
t = (10, 20, 30, 40)
a, b, c, d = t
print("a=", a, "b=", b, " c=", c, "d=", d)

# Tuple comprehension
t= ( x**2 for x in range(1,6))
print(type(t))
for x in t:
   print(x)
   