import random


def cargar():
    lista = []
    for i in range(10):
        lista.append(random.randint(18, 45))
    return lista


def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


lista = cargar()
print(lista)
buscar = int(input("Ingrese el numero que quiere buscar: "))
resultado = busqueda_lineal(lista, buscar)
if resultado != -1:
    print("El elemento", lista[resultado], "esta en la posicion", resultado)
else:
    print("Elemento no encontrado")
