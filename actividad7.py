puntos = 0
ganados = 0
empatados = 0
perdidos = 0
total = 0

partidos = int(input("Cuantos partidos jugo?: "))
while partidos < 4 or partidos > 20:
    print("ERROR")
    partidos = int(input("Cuantos partidos jugo?: "))

for i in range(partidos):
    resultado = input("Ingrese GANO, EMPATO O PERDIO: ").upper()
    while resultado != "GANO" and resultado != "EMPATO" and resultado != "PERDIO":
        print("ERROR")
        resultado = input("Ingrese GANO, EMPATO O PERDIO: ").upper()
    
    if resultado == "GANO":
        ganados = ganados + 1
        puntos = puntos + 3
    elif resultado == "EMPATO":
        empatados = empatados + 1
        puntos = puntos + 1
    else:
        perdidos = perdidos + 1

porcentajeGanados = ganados * 100 / partidos
porcentajePerdidos = perdidos * 100 / partidos
porcentajeEmpatados = empatados * 100 / partidos

print("TOTAL DE PUNTOS:", puntos)
print("Ganados:", porcentajeGanados, "%")
print("Empatados:", porcentajeEmpatados, "%")
print("Perdidos:", porcentajePerdidos, "%")