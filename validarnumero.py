import random


def esValido(lista, n):
    for i in range(len(lista)):
        if lista[i] == n:
            return False
    return True


def cargar():
    lista = []

    while len(lista) < 6:
        n = random.randint(1, 6)
        if esValido(lista, n) == True:
            lista.append(n)
    return lista


numeros = cargar()
print(numeros)
