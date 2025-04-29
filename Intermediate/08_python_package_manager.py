# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=24010

### Python Package Manager ###

# PIP https://pypi.org

# pip install pip
# pip --version

# pip install numpy
import pandas
from mypackage import arithmetics
import requests
import numpy

print(numpy.version.version)

numpy_array = numpy.array([35, 24, 62, 52, 30, 30, 17])
print(type(numpy_array))

print(numpy_array * 2)

# pip install pandas

# pip list
# pip uninstall pandas
# pip show numpy

# pip install requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

# Arithmetics Package


print(arithmetics.sum_two_values(1, 4))

#EJERCICIOS Manejo de paquetes
#1. Importa el módulo math y muestra el valor de pi.
# 2. Crea un array de números usando numpy y multiplícalo por 3.
# 3. Muestra la versión instalada de numpy.
# 4. Realiza una petición HTTP con requests a una API pública y muestra el código de estado.
# 5. Importa una función llamada sum_two_values desde un paquete personalizado mypackage.arithmetics y utilízala.
# 6. Usa pandas para crear un DataFrame con nombres en español.
# 7. Ejecuta el comando para instalar el paquete requests desde la terminal.
# 8. Usa requests para obtener datos de una API y extrae solo los nombres de los primeros Pokémon.
# 9. Muestra todos los paquetes instalados con pip desde la terminal.
# 10. Escribe una línea de código que muestre la ayuda sobre el paquete numpy desde Python.
