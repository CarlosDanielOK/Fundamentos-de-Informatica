import random


def cargar(lista):
    for i in range(20):
        n = random.randint(1, 100)
        lista.append(n)
    print(lista)


def calcularMinimo(lista):
    minimo = 9999
    for i in range(len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]

    print("El numero mas bajo es:", minimo)


lista = []
cargar(lista)
calcularMinimo(lista)
