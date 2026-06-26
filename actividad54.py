import random


def cargar():
    lista = []

    n = random.randint(-1, 100)
    while n != -1:
        lista.append(n)
        n = random.randint(-1, 100)

    return lista


def busquedaLineal(lista, n):
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == n:
            posiciones.append(i)
    return posiciones


lista = cargar()
print(lista)
print("Cantidad de elementos de la lista:", len(lista))

buscar = int(input("Ingrese un numero: "))
while buscar < 0 or buscar > 100:
    buscar = int(input("ERROR. Ingrese un numero: "))

posiciones = busquedaLineal(lista, buscar)
if len(posiciones) == 0:
    print("No existe el elemento")
else:
    print("El elemento se encuentra en las posiciones:", posiciones)
