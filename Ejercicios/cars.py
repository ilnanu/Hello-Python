# 6. Crea un módulo que defina una clase llamada "Car" con propiedades como marca, modelo y año.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

