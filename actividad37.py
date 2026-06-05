import random


def cargar(cantidad, minimo, maximo):
    lista = []

    for i in range(cantidad):
        lista.append(random.randint(minimo, maximo))

    return lista


def crearLista(lista1, lista2):
    lista = []
    for i in range(len(lista1)):
        if lista1[i] <= lista2[i]:
            lista.append(lista1[i])
        else:
            lista.append(lista2[i])
    return lista


cantidad = int(input("Ingrese la cantidad de elementos: "))
while cantidad < 2:
    cantidad = int(input("ERROR. Ingrese la cantidad de elementos: "))
minimo = int(input("Ingrese el rango minimo:"))
while minimo < 5:
    minimo = int(input("ERROR. Ingrese el rango minimo:"))
maximo = int(input("Ingrese el rango maximo:"))
while maximo > 15:
    maximo = int(input("ERROR. Ingrese el rango maximo:"))

num1, num2 = cargar(cantidad, minimo, maximo), cargar(cantidad, minimo, maximo)
print(num1, num2)

listaNueva = crearLista(num1, num2)
print(listaNueva)
