def crearMatriz(lista1, lista2, lista3):
    matriz = []
    for i in range(len(lista1)):
        matriz.append([lista1[i], lista2[i], lista3[i]])
    return matriz


def mostrarMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


codigos = [100, 101, 102]
herramientas = ["martillo", "amoladora", "destornillador"]
precios = [68000, 230000, 25000]
matriz = crearMatriz(codigos, herramientas, precios)
mostrarMatriz(matriz)
print(matriz[2][1])