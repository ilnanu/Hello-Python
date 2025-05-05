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
# 1. Importa el módulo math y muestra el valor de pi.
import math
print(math.pi)

# 2. Crea un array de números usando numpy y multiplícalo por 3.
import numpy as np
array = np.array([1, 2, 3, 4, 5])
print(array * 3)

# 3. Muestra la versión instalada de numpy.
print(numpy.__version__)

# 4. Realiza una petición HTTP con requests a una API pública y muestra el código de estado.
response = requests.get("https://api.github.com")
print(response.status_code)

# 5. Importa una función llamada sum_two_values desde un paquete personalizado mypackage.arithmetics y utilízala.
from mypackage.arithmetics import sum_two_values
result = sum_two_values(5, 10)
print(result)

# 6. Usa pandas para crear un DataFrame con nombres en español.
import pandas as pd
data = {'Nombre': ['Juan', 'Ana', 'Pedro'], 'Edad': [28, 22, 35]}
df = pd.DataFrame(data)
print(df)

# 7. Ejecuta el comando para instalar el paquete requests desde la terminal.
# pip install requests

# 8. Usa requests para obtener datos de una API y extrae solo los nombres de los primeros Pokémon.
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10")
data = response.json()
pokemon_names = [pokemon['name'] for pokemon in data['results']]
print(pokemon_names)

# 9. Muestra todos los paquetes instalados con pip desde la terminal.
# pip list
# pip freeze
# pip show requests
# pip show pandas
# 10. Escribe una línea de código que muestre la ayuda sobre el paquete numpy desde Python.
help(numpy)
# 11. Crea un entorno virtual y activa el entorno.
# python -m venv myenv
# source myenv/bin/activate (Linux/Mac)
# myenv\Scripts\activate (Windows)
# 12. Instala un paquete en el entorno virtual.
# pip install requests
# 13. Desactiva el entorno virtual.
# deactivate
# 14. Elimina el entorno virtual.
# rm -rf myenv (Linux/Mac)
# 15. Crea un archivo requirements.txt con los paquetes instalados.
# pip freeze > requirements.txt
# 16. Instala los paquetes desde requirements.txt.
# pip install -r requirements.txt
# 17. Actualiza un paquete específico.
# pip install --upgrade requests
# 18. Desinstala un paquete.
# pip uninstall requests
# 19. Busca un paquete en PyPI.
# pip search requests
# 20. Muestra la documentación de un paquete.
# pip show -f requests
# 21. Usa pipenv para crear un entorno virtual y gestionar dependencias.
# pip install pipenv
# pipenv install requests
# pipenv shell
# 22. Usa poetry para gestionar dependencias y crear un entorno virtual.
# pip install poetry
# poetry new myproject
# cd myproject
# poetry add requests
# poetry install
# 23. Usa conda para crear un entorno virtual y gestionar dependencias.q

