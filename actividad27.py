def cargar_lista(lista, cantidad):
    for i in range(cantidad):
        num = int(input("Ingrese un numero: "))
        lista.append(num)


def mostrar_negativos(lista):
    for i in range(len(lista)):
        if lista[i] < 0:
            print(lista[i])


lista1 = []
lista2 = []

cargar_lista(lista1, 8)
cargar_lista(lista2, 5)
mostrar_negativos(lista1)
mostrar_negativos(lista2)
