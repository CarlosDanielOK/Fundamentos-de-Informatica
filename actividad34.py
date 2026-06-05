import random


def cargar(lista, cantidad):
    for i in range(cantidad):
        n = random.randint(5, 50)
        lista.append(n)
    print(lista)


def calcularPromedio(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    print("El promedio es:", suma / len(lista))


lista = []

cantidad = int(input("Ingrese la cantidad: "))
while cantidad < 4 or cantidad > 10:
    cantidad = int(input("ERROR. Ingrese la cantidad: "))

cargar(lista, cantidad)
calcularPromedio(lista)
