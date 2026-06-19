import random


def cargar():
    lista = []
    numero = random.randint(5, 50)
    while numero != 25:
        lista.append(numero)
        numero = random.randint(5, 50)
    lista.append(numero)
    return lista


def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def calcular_porcentaje(lista):
    mayor = 0
    menor = 0
    for i in range(len(lista)):
        if lista[i] >= 25:
            mayor += 1
        else:
            menor += 1
    return mayor, menor


numeros = cargar()
print(numeros)
numeros = bubble_sort(numeros)
print(numeros)
calcular_porcentaje(numeros)
mayor, menor = calcular_porcentaje(numeros)
print("Numeros mayores o iguales a 25:", mayor * 100 / len(numeros), "%")
print("Numeros menores a 25:", menor * 100 / len(numeros), "%")
