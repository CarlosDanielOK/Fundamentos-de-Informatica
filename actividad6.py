total = 0
mayor95 = 0

dias = int(input("Cuantos dias vacaciono?: "))
while dias <= 0 or dias > 15:
    print("ERROR")
    dias = int(input("Cuantos dias vacaciono?: "))

for i in range(dias):
    monto = float(input("Cuanto gasto en el dia?: $"))
    while monto < 0:
        print("ERROR")
        monto = float(input("Cuanto gasto en el dia?: $"))
    total = total + monto
    
    if monto > 95000:
        mayor95 = mayor95 + 1

print("Total: $", total)
print("Porcentaje de dias que gasto mas de $95000: ", mayor95 * 100 / dias, "%")