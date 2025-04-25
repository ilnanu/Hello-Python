"""
/*
 * EJERCICIO:
 * GitHub ha publicado el Octoverse 2024, el informe
 * anual del estado de la plataforma:
 * https://octoverse.github.com
 *
 * Utilizando el API de GitHub, crea un informe asociado
 * a un usuario concreto.
 * 
 * - Se debe poder definir el nombre del usuario
 *   sobre el que se va a generar el informe.
 *   
 * - Crea un informe de usuario basándote en las 5 métricas
 *   que tú quieras, utilizando la información que te
 *   proporciona GitHub. Por ejemplo:
 *   - Lenguaje más utilizado
 *   - Cantidad de repositorios
 *   - Seguidores/Seguidos
 *   - Stars/forks
 *   - Contribuciones
 *   (lo que se te ocurra)
 */
"""
import requests
from collections import Counter

# Token personal opcional para más peticiones sin límites
GITHUB_TOKEN = None  # O pon tu token aquí como string

def get_headers():
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    return headers

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=get_headers())
    response.raise_for_status()
    return response.json()

def get_user_repos(username):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=get_headers())
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def generar_informe(username):
    try:
        user = get_user_info(username)
        repos = get_user_repos(username)

        lenguajes = Counter()
        estrellas = 0
        forks = 0

        for repo in repos:
            lenguaje = repo.get("language")
            if lenguaje:
                lenguajes[lenguaje] += 1
            estrellas += repo.get("stargazers_count", 0)
            forks += repo.get("forks_count", 0)

        lenguaje_principal = lenguajes.most_common(1)[0][0] if lenguajes else "Desconocido"
        
        print(f"\n🧾 Informe de GitHub para @{username}\n" + "-"*40)
        print(f"👤 Nombre: {user.get('name') or 'No disponible'}")
        print(f"📁 Repos públicos: {user.get('public_repos')}")
        print(f"🌍 Lenguaje más utilizado: {lenguaje_principal}")
        print(f"⭐ Total de estrellas recibidas: {estrellas}")
        print(f"🍴 Total de forks: {forks}")
        print(f"👥 Seguidores: {user.get('followers')} | Siguiendo: {user.get('following')}")
        print(f"🔗 Perfil: {user.get('html_url')}")
        print("-" * 40)

    except requests.HTTPError as e:
        print(f"❌ Error al recuperar datos de GitHub: {e}")

if __name__ == "__main__":
    username = input("Introduce el nombre de usuario de GitHub: ")
    generar_informe(username.strip())
