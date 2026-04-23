suma = 0
menores = 0
mayores = 0

for i in range(30):
    edad = int(input("Ingrese su edad: "))
    suma = suma + edad
    if edad < 18:
        menores = menores + 1
    else:
        mayores = mayores + 1

promedio = suma / 30
porcentajeMenores = menores * 100 / 30
porcentajeMayores = mayores * 100 / 30

print("Promedio:", promedio)
print("Porcentaje de menores de edad:", porcentajeMenores)
print("Porcentaje de mayores de edad:", porcentajeMayores)