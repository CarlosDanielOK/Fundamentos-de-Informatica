cont_1 = 0
cont_2 = 0
cont_3 = 0
suma = 0

for i in range(8):
    tiempo = int(input("Ingrese el tiempo de su carrera en minutos: "))
    while tiempo < 0:
        print("ERROR")
        tiempo = int(input("Ingrese el tiempo de su carrera en minutos: "))

    if tiempo < 48:
        cont_1 = cont_1 + 1
        suma = suma + tiempo
    elif tiempo >= 48 and tiempo <= 105:
        cont_2 = cont_2 + 1
        suma = suma + tiempo
    else:
        cont_3 = cont_3 + 1
        suma = suma + tiempo

print("Porcentaje que tardo menos de 48 minutos:", cont_1 * 100 / 8)
print("Porcentaje que tardo entre 45 y 105 minutos:", cont_2 * 100 / 8)
print("Porcentaje que tardo mas de 145 minutos:", cont_3 * 100 / 8)