def cargar_reales(lista):
    for i in range(5):
        numero = float(input("Ingrese un numero real: "))
        lista.append(numero)

numeros = []
cargar_reales(numeros)
print(numeros)