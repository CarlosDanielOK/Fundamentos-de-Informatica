def crear_matriz(lista1, lista2, lista3):
    matriz = []
    for i in range(len(lista1)):
        matriz.append([lista1[i], lista2[i], lista3[i]])
    return matriz


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


a = ["a1", "b1"]
b = ["a2", "b2"]
c = ["a3", "b3"]

matriz = crear_matriz(a, b, c)
mostrar_matriz(matriz)
