import random


def cargar():
    lista = []
    for i in range(8):
        lista.append(random.randint(12, 25))
    print(lista)
    return lista


def promedio(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    return suma / len(lista)


def porcentaje(lista):
    menores, mayores = 0, 0
    for i in range(len(lista)):
        if lista[i] < 18:
            menores += 1
        else:
            mayores += 1

    porcentajeMenores = (menores * 100) / len(lista)
    porcentajeMayores = (mayores * 100) / len(lista)

    return porcentajeMenores, porcentajeMayores


def edadMasAlta(lista):
    maximo = -9999
    posicion = 0
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            posicion = i
    return maximo, posicion


edades = cargar()
prom = promedio(edades)
porcMenores, porcMayores = porcentaje(edades)
edadMaxima, posicionEdad = edadMasAlta(edades)

print("El promedio de edad es:", prom)
print(
    "El porcentaje de menores es:",
    porcMenores,
    "%",
    "Y el de mayores es:",
    porcMayores,
    "%",
)
print("La edad mas alta es:", edadMaxima, "Y esta en la posicion:", posicionEdad)
