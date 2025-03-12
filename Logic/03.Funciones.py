def imprimir_numeros(texto1, texto2) -> int:
    num_veces = 0;
    texto_devolver = texto1 + texto2;
    for number in range(1, 101):
        texto_devolver = validar_numero(number, texto1, texto2);
        if texto_devolver != "":
            print(texto_devolver);
            num_veces+=1;
    return num_veces;

def validar_numero(num, texto1, texto2):
    texto_devolver = "";
    es_multiplo_3 = num % 3 == 0;
    es_multiplo_5 = num % 5 == 0;

    if es_multiplo_3:
        texto_devolver = texto1;
    if es_multiplo_5:
        texto_devolver = texto2;
    if es_multiplo_3 and es_multiplo_5:
        texto_devolver = texto1 + " " + texto2;
    return texto_devolver;


print(f"Se han impreso {imprimir_numeros("Fizz", "Buzz")} veces los textos");

