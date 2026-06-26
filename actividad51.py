import random


def esValido(lista, n):
    for i in range(len(lista)):
        if lista[i] == n:
            return False
    return True


def cargar():
    codigo = []
    servicio = ["rojo", "azul", "verde", "violeta", "rosa", "naranja"]
    precio = []

    while len(codigo) < 6:
        n = random.randint(1, 100)
        if esValido(codigo, n) == True:
            codigo.append(n)
    while len(precio) < 6:
        p = random.randint(400000, 1750000)
        if esValido(precio, p) == True:
            precio.append(p)

    return codigo, servicio, precio


def bubbleSort(lista1, lista2, lista3):
    for i in range(len(lista1)):
        for j in range(len(lista1) - i - 1):
            if lista1[j] > lista1[j + 1]:
                lista1[j], lista1[j + 1] = lista1[j + 1], lista1[j]
                lista2[j], lista2[j + 1] = lista2[j + 1], lista2[j]
                lista3[j], lista3[j + 1] = lista3[j + 1], lista3[j]
    return lista1, lista2, lista3


def crearMatriz(lista1, lista2, lista3):
    matriz = []
    for i in range(len(lista1)):
        matriz.append([lista1[i], lista2[i], lista3[i]])
    return matriz


def imprimirMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def masBarato(precio):
    minimo = 2000000
    pos = 0
    for i in range(len(precio)):
        if precio[i] < minimo:
            minimo = precio[i]
            pos = i
    return pos


codigo, servicio, precio = cargar()
print(codigo, servicio, precio)
codigo, servicio, precio = bubbleSort(codigo, servicio, precio)
matriz = crearMatriz(codigo, servicio, precio)
imprimirMatriz(matriz)
pos = masBarato(precio)
print("El servicio mas barato es:", matriz[pos])
