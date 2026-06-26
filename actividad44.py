import random


def pedir_datos():
    cantidad = int(input("Cuantos numeros quiere ingresar?: "))
    while cantidad < 2:
        cantidad = int(input("ERROR. Cuantos numeros quiere ingresar?: "))
    minimo = int(input("Ingrese el rango minimo?: "))
    while minimo < 5:
        minimo = int(input("ERROR. Ingrese el rango minimo?: "))
    maximo = int(input("Ingrese el rango maximo?: "))
    while maximo > 15:
        maximo = int(input("ERROR. Ingrese el rango maximo?: "))

    return cantidad, minimo, maximo


def cargar(cantidad, minimo, maximo):
    lista = []

    for i in range(cantidad):
        lista.append(random.randint(minimo, maximo))

    return lista


def comparar(lista1, lista2):
    lista3 = []

    for i in range(len(lista1)):
        if lista1[i] < lista2[i]:
            lista3.append(lista1[i])
        else:
            lista3.append(lista2[i])

    return lista3


cantidad, minimo, maximo = pedir_datos()
lista1 = cargar(cantidad, minimo, maximo)
lista2 = cargar(cantidad, minimo, maximo)
print(lista1)
print(lista2)
lista3 = comparar(lista1, lista2)
print(lista3)
