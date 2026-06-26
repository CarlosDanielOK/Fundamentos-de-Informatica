import random


def cargar():
    legajo = []

    while len(legajo) < 10:
        n = random.randint(100, 115)
        if esValido(legajo, n) == True:
            legajo.append(n)

    return legajo


def esValido(lista, n):
    for i in range(len(lista)):
        if lista[i] == n:
            return False
    return True


def busquedaLineal(lista, n):
    for i in range(len(lista)):
        if lista[i] == n:
            return i
    return -1


legajo = cargar()
print(legajo)
numero = int(input("Numero de legajo a buscar: "))
pos = busquedaLineal(legajo, numero)

if pos == -1:
    print("El legajo no existe")
else:
    print("El legajo", numero, "esta en la posicion", pos)
