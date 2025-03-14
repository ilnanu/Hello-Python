#función palindromo
def palindromo (cadena1, cadena2) -> str:
    if cadena1.upper() == cadena2.upper()[::-1]:
        return "Es un palindromo"
    return "No es un palindromo"

print(palindromo("oso", "perro"))
print(palindromo("oso", "oso"))

#función anagrama
def anagrama (cadena1, cadena2) -> str:
    if sorted(cadena1.upper()) == sorted(cadena2.upper()):
        return "Es un anagrama"
    return "No es un anagrama"
print(anagrama("pozo", "oso"))
print(anagrama("pozo", "zopo"))

#función isograma
def isograma (cadena) -> str:
    cadena_sin_espacios = cadena.replace(" ", "")
    cadena_sin_repetidos = "".join(set(cadena_sin_espacios))
    if cadena_sin_espacios == cadena_sin_repetidos:
        return "Es un isograma"
    return "No es un isograma"

print(isograma("oso"))
print(isograma("murcielago"))

# Unificada

def check (word: str, word2: str) -> str:
    #palindromo
    print(f"¿{word} es un palindromo? {word.upper() == word2.upper()[::-1]}")

    #anagrama
    print(f"¿{word} es un anagrama de {word2}? {sorted(word.upper()) == sorted(word2.upper())}")

    #isograma
    word_sin_espacios = word.replace(" ", "")
    word_sin_repetidos = "".join(set(word_sin_espacios))
    print(f"¿{word} es un isograma? {word_sin_espacios == word_sin_repetidos}") 

check("oso", "oso")
check("oso", "perro")
check("pozo", "oso")
check("pozo", "zopo")
check("oso", "oso")
check("murcielago", "murcielago")
