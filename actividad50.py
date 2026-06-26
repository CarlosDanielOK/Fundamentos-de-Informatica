import random


def cargar():
    legajo = []
    nombre = []

    while len(legajo) < 5:
        n = random.randint(400, 450)
        if esValido(legajo, n) == True:
            legajo.append(n)

    for i in range(5):
        n = input("Ingrese un nombre: ")
        nombre.append(n)

    return legajo, nombre


def bubbleSort(lista1, lista2):
    for i in range(len(lista1)):
        for j in range(len(lista1) - i - 1):
            if lista1[j] > lista1[j + 1]:
                lista1[j], lista1[j + 1] = lista1[j + 1], lista1[j]
                lista2[j], lista2[j + 1] = lista2[j + 1], lista2[j]

    return lista1, lista2


def crearMatriz(lista1, lista2):
    matriz = []
    for i in range(len(lista1)):
        matriz.append([lista1[i], lista2[i]])

    return matriz


def busquedaLineal(lista, buscar):
    for i in range(len(lista)):
        if lista[i] == buscar:
            return i
    return -1


def busquedaLinealMatriz(matriz, buscar):
    for i in range(len(matriz)):
        if matriz[i][0] == buscar:
            return i
    return -1


def esValido(lista, buscar):
    for i in range(len(lista)):
        if lista[i] == buscar:
            return False
    return True


legajo, nombre = cargar()
print(legajo, nombre)
legajo, nombre = bubbleSort(legajo, nombre)
print(legajo, nombre)
matriz = crearMatriz(legajo, nombre)
print(matriz)

n = int(input("Ingrese un numero de legajo para buscar: "))
while n < 400 or n > 450:
    n = int(input("ERROR. Ingrese un numero de legajo para buscar: "))

pos = busquedaLineal(legajo, n)

if pos == -1:
    print("El legajo no existe.")
else:
    print("El legajo", n, "pertenece a", matriz[pos])

pos = busquedaLinealMatriz(matriz, n)

if pos == -1:
    print("El legajo no existe")
else:
    print("El legajo", n, "pertenece a", matriz[pos][0], matriz[pos][1])
