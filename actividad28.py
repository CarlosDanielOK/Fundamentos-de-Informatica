def cargar(lista, cantidad):
    for i in range(cantidad):
        num = int(input("Ingrese un numero: "))
        lista.append(num)


def mostrar(lista):
    for i in range(len(lista)):
        print(lista[i])


cantidad = int(input("Ingrese la cantidad: "))
while cantidad < 3:
    cantidad = int(input("Ingrese la cantidad: "))

numeros = []
cargar(numeros, cantidad)
mostrar(numeros)
