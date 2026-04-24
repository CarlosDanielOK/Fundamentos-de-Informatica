suma = 0
cat1 = 0
cat2 = 0
cat1500 = 0
cat1suma = 0
cat2suma = 0

n = int(input("Ingrese la cantidad de empleados: "))
while n < 0:
    print("ERROR")
    n = int(input("Ingrese la cantidad de empleados: "))

for i in range(n):
    categoria = int(input("Ingrese su categoria (1 o 2): "))
    salario = float(input("Ingrese su salario: $"))

    if categoria == 1:
        cat1 = cat1 + 1
        cat1suma = cat1suma + salario

    if categoria == 1 and salario > 500:
        cat1500 = cat1500 + 1

    if categoria == 2:
        cat2 = cat2 + 1
        cat2suma = cat2suma + salario

    suma = suma + salario # o tambien podria sumar cat1suma + cat2suma

print("Salario total pagado por la empresa: $", suma)
print("Cantidad de empleados que son categoria 1 y ganan mas de $500: ", cat1500)
print("Porcentaje de empleados que son categoria 1 y ganan mas de $500: ", cat1500 * 100 / n, "%")
print("Salario promedio de categoria 1: $", cat1suma / cat1)
print("Salario promedio de categoria 2: $", cat2suma / cat2)