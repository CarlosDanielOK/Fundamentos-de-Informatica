def cargar_lista(cantidad, lista):
    for i in range(cantidad):
        num = int(input("Ingrese un numero entero: "))
        lista.append(num)


cantidad = int(input("Ingrese la cantidad de elementos: "))
while cantidad < 2:
    cantidad = int(input("Ingrese la cantidad de elementos: "))

numeros = []
cargar_lista(cantidad, numeros)
print(numeros)
