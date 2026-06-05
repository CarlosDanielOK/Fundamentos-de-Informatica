def cargar(lista):
    for i in range(5):
        nombre = input("Ingrese un nombre: ")
        lista.append(nombre)
    print(lista)


def recorrer(lista):
    maximo = -9999
    largo = ""
    posicion = 0
    for i in range(len(lista)):
        if len(lista[i]) > maximo:
            maximo = len(lista[i])
            largo = lista[i]
            posicion = i
    print(
        "El nombre mas largo es:",
        largo,
        "Y tiene:",
        maximo,
        "caracteres.",
        "Esta en la posicion:",
        posicion,
    )


lista = []
cargar(lista)
recorrer(lista)
