def cargar(lista):
    for i in range(10):
        num = int(input("Ingrese un numero: "))
        while num < 0:
            num = int(input("Ingrese un numero: "))
        lista.append(num)


def recorrer(lista):
    mayores = 0
    for i in range(len(lista)):
        if lista[i] > 10:
            mayores += 1
            print(lista[i])
    print("Cantidad de numeros mayores a 10: ", mayores)


lista = []
cargar(lista)
recorrer(lista)
