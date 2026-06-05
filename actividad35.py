import random


def cargar(lista, minimo, maximo):
    for i in range(12):
        n = random.randint(minimo, maximo)
        lista.append(n)
    print(lista)


def calcularPorcentaje(lista):
    negativos = 0
    positivos = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            negativos += 1
        elif lista[i] > 0:
            positivos += 1

    print("El porcentaje de numeros negativos es:", (negativos * 100) / len(lista))
    print("El porcentaje de numeros positivos es:", (positivos * 100) / len(lista))


lista = []

minimo = int(input("Ingrese el rango minimo (negativo): "))
while minimo > 0:
    minimo = int(input("ERROR. Ingrese el rango minimo (negativo): "))

maximo = int(input("Ingrese el rango maximo (positivo): "))
while maximo < 0:
    maximo = int(input("ERROR. Ingrese el rango maximo (positivo): "))

cargar(lista, minimo, maximo)
calcularPorcentaje(lista)
