"""
/*
 * EJERCICIO:
 * Cada 1 de septiembre, el Hogwarts Express parte hacia la escuela
 * de programación de Hogwarts para magos y brujas del código.
 * En ella, su famoso sombrero seleccionador ayuda a los programadores
 * a encontrar su camino...
 * Desarrolla un programa que simule el comportamiento del sombrero.
 * Requisitos:
 * 1. El sombrero realizará 10 preguntas para determinar la casa del alumno.
 * 2. Deben existir 4 casas. Por ejemplo: Frontend, Backend, Mobile y Data.
 *    (Puedes elegir las que quieras)
 * Acciones:
 * 1. Crea un programa que solicite el nombre del alumno y realice 10
 *    preguntas, con cuatro posibles respuestas cada una.
 * 2. Cada respuesta asigna puntos a cada una de las casas (a tu elección).
 * 3. Una vez finalizado, el sombrero indica el nombre del alumno 
 *    y a qué casa pertenecerá (resuelve el posible empate de manera aleatoria,
 *    pero indicándole al alumno que la decisión ha sido complicada).
 */
"""
import random

# Definición de casas
casas = {
    "Frontend": 0,
    "Backend": 0,
    "Mobile": 0,
    "Data": 0
}

# Preguntas y respuestas con puntuación
preguntas = [
    {
        "texto": "¿Qué parte de un proyecto disfrutas más?",
        "respuestas": {
            "a": ("Diseñar interfaces llamativas", "Frontend"),
            "b": ("Optimizar bases de datos", "Backend"),
            "c": ("Construir apps nativas", "Mobile"),
            "d": ("Analizar grandes volúmenes de datos", "Data")
        }
    },
    {
        "texto": "¿Cuál es tu herramienta favorita?",
        "respuestas": {
            "a": ("Figma", "Frontend"),
            "b": ("PostgreSQL", "Backend"),
            "c": ("Flutter", "Mobile"),
            "d": ("Jupyter Notebook", "Data")
        }
    },
    {
        "texto": "¿Qué te motiva a programar?",
        "respuestas": {
            "a": ("Crear experiencias bonitas", "Frontend"),
            "b": ("Resolver problemas complejos", "Backend"),
            "c": ("Innovar en dispositivos móviles", "Mobile"),
            "d": ("Descubrir patrones en los datos", "Data")
        }
    },
    {
        "texto": "¿Qué lenguaje prefieres?",
        "respuestas": {
            "a": ("JavaScript", "Frontend"),
            "b": ("Python", "Backend"),
            "c": ("Kotlin", "Mobile"),
            "d": ("R", "Data")
        }
    },
    {
        "texto": "¿Cuál sería tu hechizo favorito?",
        "respuestas": {
            "a": ("Lumos: iluminar interfaces", "Frontend"),
            "b": ("Alohomora: desbloquear lógica", "Backend"),
            "c": ("Accio: invocar apps", "Mobile"),
            "d": ("Legilimens: leer datos", "Data")
        }
    },
    {
        "texto": "¿Qué tipo de bugs odias más?",
        "respuestas": {
            "a": ("Desalineación de elementos", "Frontend"),
            "b": ("Problemas de concurrencia", "Backend"),
            "c": ("Errores de compatibilidad", "Mobile"),
            "d": ("Errores estadísticos", "Data")
        }
    },
    {
        "texto": "¿Dónde te gustaría trabajar?",
        "respuestas": {
            "a": ("Agencia de diseño web", "Frontend"),
            "b": ("Startup de IA", "Backend"),
            "c": ("Empresa de wearables", "Mobile"),
            "d": ("Laboratorio de datos", "Data")
        }
    },
    {
        "texto": "¿Qué superpoder querrías tener?",
        "respuestas": {
            "a": ("Crear belleza visual al instante", "Frontend"),
            "b": ("Resolver algoritmos imposibles", "Backend"),
            "c": ("Adaptarte a cualquier dispositivo", "Mobile"),
            "d": ("Predecir el futuro con datos", "Data")
        }
    },
    {
        "texto": "¿Qué prefieres en tu tiempo libre?",
        "respuestas": {
            "a": ("Explorar webs creativas", "Frontend"),
            "b": ("Ver documentales de tecnología", "Backend"),
            "c": ("Probar nuevas apps", "Mobile"),
            "d": ("Leer sobre ciencia y datos", "Data")
        }
    },
    {
        "texto": "¿Con qué personaje te identificas más?",
        "respuestas": {
            "a": ("Hermione: brillante y detallista", "Frontend"),
            "b": ("Snape: estratega y profundo", "Backend"),
            "c": ("Harry: valiente e intuitivo", "Mobile"),
            "d": ("Dumbledore: sabio y analítico", "Data")
        }
    }
]

def preguntar(nombre):
    print(f"\n🎩 Bienvenido/a, {nombre}. El Sombrero Seleccionador hablará...")
    print("Responde las siguientes preguntas eligiendo a, b, c o d:\n")

    for i, pregunta in enumerate(preguntas):
        print(f"{i + 1}. {pregunta['texto']}")
        for clave, (texto, _) in pregunta["respuestas"].items():
            print(f"   {clave}) {texto}")
        while True:
            respuesta = input("Tu elección: ").lower()
            if respuesta in pregunta["respuestas"]:
                casa = pregunta["respuestas"][respuesta][1]
                casas[casa] += 1
                break
            else:
                print("Por favor, elige a, b, c o d.")
        print()

def determinar_casa(nombre):
    max_puntos = max(casas.values())
    ganadoras = [casa for casa, puntos in casas.items() if puntos == max_puntos]

    print(f"🧙 El sombrero ha analizado tus respuestas, {nombre}...")
    if len(ganadoras) == 1:
        print(f"✅ ¡Has sido asignado a la casa: {ganadoras[0]}!")
    else:
        seleccionada = random.choice(ganadoras)
        print("🤔 Hmm... ¡Qué decisión tan difícil!")
        print(f"✅ Finalmente, el sombrero ha decidido: ¡{seleccionada}!")

# ---- Ejecución principal ----

if __name__ == "__main__":
    nombre = input("🎓 ¿Cuál es tu nombre, joven aprendiz? ")
    preguntar(nombre)
    determinar_casa(nombre)
