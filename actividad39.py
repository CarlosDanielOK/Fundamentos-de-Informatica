def bubble_sort(lista1, lista2, lista3):
    for i in range(len(lista1)):
        for j in range(len(lista1) - i - 1):
            if lista1[j] > lista1[j + 1]:
                aux = lista1[j]
                lista1[j] = lista1[j + 1]
                lista1[j + 1] = aux
                aux = lista2[j]
                lista2[j] = lista2[j + 1]
                lista2[j + 1] = aux
                aux = lista3[j]
                lista3[j] = lista3[j + 1]
                lista3[j + 1] = aux
    return lista1, lista2, lista3


def crear_matriz(lista1, lista2, lista3):
    matriz = []
    for i in range(len(lista1)):
        matriz.append([lista1[i], lista2[i], lista3[i]])
    return matriz


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])

""""""
def mostrar_alto(lista):
    maximo = -9999
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = i
    return maximo # retorna la posicion del numero mas alto    


camiseta = [10, 23, 7, 22, 13]
jugador = ["Messi", "E. Martinez", "De Paul", "L. Martinez", "Romero"]
posicion = ["delantero", "arquero", "centrocampista", "delantero", "defensor"]

print(bubble_sort(camiseta, jugador, posicion))
matriz = crear_matriz(camiseta, jugador, posicion)
mostrar_matriz(matriz)
pos = mostrar_alto(camiseta)
print("El numero de camiseta mas alto lo tiene:", matriz[pos])