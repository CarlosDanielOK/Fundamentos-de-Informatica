import random


def pedir():
    filas = int(input("Cantidad de filas de la matriz: "))
    while filas < 0:
        filas = int(input("ERROR. Cantidad de filas de la matriz: "))
    columnas = int(input("Cantidad de columnas de la matriz: "))
    while columnas < 0:
        columnas = int(input("ERROR. Cantidad de columnas de la matriz: "))

    return filas, columnas


def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(0, 1))
        matriz.append(fila)

    return matriz

def reemplazar(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                matriz[i][j] = "LIBRE"
            else:
                matriz[i][j] = "OCUPADO"
    return matriz

filas, columnas = pedir()
matriz = crear_matriz(filas, columnas)
print(matriz)
matriz = reemplazar(matriz)
print(matriz)