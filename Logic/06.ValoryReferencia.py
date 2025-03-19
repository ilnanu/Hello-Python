valor1 = 3
valor2 = 5

def programValor(paramValor1: int, paramValor2:int):
    tempValor = paramValor2
    paramValor2 = paramValor1
    paramValor1 = tempValor

print("Programa por Valor:")
print(f"valor1 {valor1}, valor2 {valor2}")
programValor(valor1,valor2)
print(f"valor1 {valor1}, valor2 {valor2}")

valorRef1 = [3]
valorRef2 = [5]


def programReferencia(paramValor1: list, paramValor2:list):
    tempValor = paramValor2
    paramValor2 = paramValor1
    paramValor1 = tempValor
    paramValor1.append(10)
    paramValor2.append(20)


print("Programa por Referencia:")
print(f"valor1 {valorRef1}, valor2 {valorRef2}")
programReferencia(valorRef1, valorRef2)
print(f"valor1 {valorRef1}, valor2 {valorRef2}")

