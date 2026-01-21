# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=16335

### Sets ###

# Definición

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_other_set = {"Brais", "Moure", 35}
print(type(my_other_set))

print(len(my_other_set))

#Creating a set using range function 
s=set(range(5))
print(s)


# Inserción

my_other_set.add("MoureDev")

print(my_other_set)  # Un set no es una estructura ordenada

my_other_set.add("MoureDev")  # Un set no admite repetidos

print(my_other_set)

# Actualización
s = {10,20,30}
l = [40,50,60,10]
s.update(l)
print(s)


# Búsqueda

print("Moure" in my_other_set)
print("Mouri" in my_other_set)

# Eliminación

my_other_set.remove("Moure")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))

x={10,20,30,40}
y={30,40,50,60}
print(x.symmetric_difference(y))
print(x^y)


s={10,20,30}
s1=s.copy()
print(s1)

s = {40,10,30,20}
print(s)
print(s.pop())
print(s)


s={10,20,30}
s.discard(10)
print(s)

s= {1, 2, 3, "Sharuk"}
print(s)
print(1 in s)
print('S' in s)
print(2 not in s)

s = {x*x for x in range(5)}
print(s)

#remove duplicates elements in sets
l=[10,20,30,10,20,40]
s=set(l)
print(s)

#frozen sets
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print(fSet)
print(type(fSet))