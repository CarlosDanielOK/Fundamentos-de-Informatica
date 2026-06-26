import random


def cargar():
    lista = []
    for i in range(10):
        lista.append(random.randint(18, 45))
    return lista


def busquedaLineal(lista, n):
    for i in range(len(lista)):
        if lista[i] == n:
            return i
    return -1


lista = cargar()
print(lista)

edad = int(input("Ingrese la edad que desee buscar: "))
pos = busquedaLineal(lista, edad)

if pos == -1:
    print("El numero no esta en la lista.")
else:
    print("El numero", edad, "esta en la posicion", pos)
