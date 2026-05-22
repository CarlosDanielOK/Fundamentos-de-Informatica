def cargar_lista():
    lista = []
    for i in range(6):
        num = float(input("Ingrese un numero real: "))
        while num < 1.55 or num > 2.15:
            num = float(input("Error - Ingrese un numero real: "))
        lista.append(num)
    print(lista)


cargar_lista()
