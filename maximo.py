maximo = -9999

cant = int(input("Ingrese cantidad: "))
while cant < 1:
    cant = int(input("Ingrese cantidad: "))

for i in range(cant):
    num = int(input("Ingrese un numero: "))
    if num > maximo:
        maximo = num
print("El numero mas alto es", maximo)