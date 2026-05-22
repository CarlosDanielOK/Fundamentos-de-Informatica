def cargar_lista(lista):
    for i in range(8):
        num = int(input("Ingrese un numero: "))
        lista.append(num)


def sumar(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
    print(suma)


lista = []

cargar_lista(lista)
print(lista)
sumar(lista)