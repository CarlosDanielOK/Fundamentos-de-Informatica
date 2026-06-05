def cargar(lista):
    for i in range(7):
        n = int(input("Ingrese un numero: "))
        while n < 1 or n > 10:
            n = int(input("ERROR. Ingrese un numero: "))
        lista.append(n)


def calcular_maximo(lista):
    maximo = -9999
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]

    print("El numero mas alto es", maximo)


lista = []
cargar(lista)
calcular_maximo(lista)
