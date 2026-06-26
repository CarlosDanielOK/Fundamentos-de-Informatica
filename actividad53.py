import random


def pedir():
    print("¿Cuantas bauleras existen?")

    filas = int(input("Ingrese la cantidad de filas: "))
    while filas < 1:
        filas = int(input("ERROR. Ingrese la cantidad de filas: "))

    columnas = int(input("Ingrese la cantidad de columnas: "))
    while columnas < 1:
        columnas = int(input("ERROR. Ingrese la cantidad de columnas: "))

    return filas, columnas


def crearMatriz(filas, columnas):
    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(1, 3))
        matriz.append(fila)

    return matriz


def imprimir(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def reemplazar(matriz, filas, columnas):
    dueno, alquilada, libre = 0, 0, 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                matriz[i][j] = "DUEÑO"
                dueno += 1
            elif matriz[i][j] == 2:
                matriz[i][j] = "ALQUILADA"
                alquilada += 1
            elif matriz[i][j] == 3:
                matriz[i][j] = "LIBRE"
                libre += 1

    porcentajeDueno = round((dueno * 100) / (filas * columnas), 2)
    porcentajeAlquilada = round((alquilada * 100) / (filas * columnas), 2)
    porcentajeLibre = round((libre * 100) / (filas * columnas), 2)

    return matriz, porcentajeDueno, porcentajeAlquilada, porcentajeLibre


filas, columnas = pedir()
matriz = crearMatriz(filas, columnas)
imprimir(matriz)
matriz, dueno, alquilada, libre = reemplazar(matriz, filas, columnas)
imprimir(matriz)

print("Porcentaje de bauleras con dueño directo:", dueno, "%")
print("Porcentaje de bauleras alquiladas:", alquilada, "%")
print("Porcentaje de bauleras libres:", libre, "%")
