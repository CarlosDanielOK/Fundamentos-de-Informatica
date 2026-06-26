matriz = []

for i in range(2):  # matriz con 2 filas
    fila = []
    for i in range(3):  # y 3 columnas
        numero = int(input("Ingrese un numero: "))
        fila.append(numero)  # añade el numero a la lista que representa la fila
    matriz.append(fila)  # añade la fila a la matriz

for i in range(len(matriz)):
    print(matriz[i])
