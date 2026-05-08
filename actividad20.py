def numero_maximo():
    maximo = -9999
    for i in range(7):
        num = float(input("Ingrese un numero: "))
        if num > maximo:
            maximo = num
    
    print("El numero maximo es", maximo)

def numero_minimo():
    minimo = 9999
    for i in range(4):
        num = float(input("Ingrese un numero: "))
        if num < minimo:
            minimo = num
    
    print("El numero minimo es", minimo)

opcion = int(input("Ingrese 1 o 2: "))
while opcion != 1 and opcion != 2:
    opcion = int(input("Ingrese 1 o 2: "))

if opcion == 1:
    numero_maximo()
else:
    numero_minimo()