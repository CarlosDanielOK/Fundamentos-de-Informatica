import random

ventas = int(input("Cuantas ventas realizo?: "))
while ventas < 1:
    ventas = int(input("Cuantas ventas realizo?: "))


def cargar(n):
    lista1 = []
    lista2 = []
    lista3 = []

    for i in range(n):
        lista1.append(i + 1)
        lista2.append(random.randint(1, 2))
        lista3.append(random.randint(250, 1500))

    return lista1, lista2, lista3


def crear_matriz(lista1, lista2, lista3):
    matriz = []
    for i in range(len(lista1)):
        matriz.append([lista1[i], lista2[i], lista3[i]])
    return matriz


def mostrar_matriz(lista):
    for i in range(len(lista)):
        print(lista[i])


def modificar_matriz(lista):
    for i in range(len(lista)):
        if lista[i][1] == 1:
            lista[i][1] = "biscochos"
        elif lista[i][1] == 2:
            lista[i][1] = "chipá"
    return lista


def calcular_cantidad(lista):
    sumaBiscochos = 0
    sumaChipas = 0
    for i in range(len(lista)):
        if lista[i][1] == "biscochos":
            sumaBiscochos = sumaBiscochos + lista[i][2]
        elif lista[i][1] == "chipá":
            sumaChipas = sumaChipas + lista[i][2]
    return sumaBiscochos, sumaChipas


numeros, tipo, gramos = cargar(ventas)  # crea y carga las listas
print(numeros, tipo, gramos)
matriz = crear_matriz(numeros, tipo, gramos)
mostrar_matriz(matriz)
print(matriz)
matriz = modificar_matriz(matriz)
print(matriz)
gramosBiscochos, gramosChipas = calcular_cantidad(matriz)
print(
    "Se vendieron",
    gramosBiscochos,
    "gramos de biscochos y",
    gramosChipas,
    "gramos de chipás",
)
