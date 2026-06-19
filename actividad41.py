import random


def bubble_sort(legajo, nombre):
    for i in range(len(legajo)):
        for j in range(len(legajo) - i - 1):
            if legajo[j] > legajo[j + 1]:
                aux = legajo[j]
                legajo[j] = legajo[j + 1]
                legajo[j + 1] = aux
                aux = nombre[j]
                nombre[j] = nombre[j + 1]
                nombre[j + 1] = aux
    return legajo, nombre


def cargar():
    legajo = []
    nombre = []

    for i in range(5):
        legajo.append(random.randint(400, 450))

    for i in range(5):
        n = input("Ingrese un nombre: ")
        nombre.append(n)

    return legajo, nombre


def crear_matriz(lista1, lista2):
    matriz = []
    for i in range(len(lista1)):
        matriz.append([lista1[i], lista2[i]])
    return matriz


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


legajos, nombres = cargar()
print(legajos, nombres)
legajos, nombres = bubble_sort(legajos, nombres)
print(legajos, nombres)
matriz = crear_matriz(legajos, nombres)
mostrar_matriz(matriz)

buscar = int(input("Ingrese el numero de legajo a buscar: "))
while buscar < 400 or buscar > 450:
    buscar = int(input("ERROR. Ingrese el numero de legajo a buscar: "))

resultado = busqueda_lineal(legajos, buscar)
if resultado != -1:
    print("El legajo corresponde a", matriz[resultado])
else:
    print("El legajo no existe")
