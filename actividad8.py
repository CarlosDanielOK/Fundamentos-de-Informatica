menos48 = 0
entre48105 = 0
mas105 = 0
suma = 0

for i in range(8):
    tiempo = int(input("Ingrese el tiempo de su carrera en minutos: "))
    while tiempo < 0:
        print("ERROR")
        tiempo = int(input("Ingrese el tiempo de su carrera en minutos: "))

    if tiempo < 48:
        menos48 = menos48 + 1
    elif tiempo >= 48 and tiempo <= 105:
        entre48105 = entre48105 + 1
    elif tiempo > 105:
        mas105 = mas105 + 1
    
    suma = suma + tiempo

print("Porcentaje que tardo menos de 48 minutos:", menos48 * 100 / 8, "%")
print("Porcentaje que tardo entre 48 y 105 minutos:", entre48105 * 100 / 8, "%")
print("Porcentaje que tardo mas de 105 minutos:", mas105 * 100 / 8, "%")

promedio = suma / 8

if promedio < 101:
    print("NUEVO RECORD")