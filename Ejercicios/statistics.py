# 8. Crea un módulo llamado "statistics" que tenga funciones para calcular la media y la mediana de una lista de números.

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    return numbers[mid]
