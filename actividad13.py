suma = 0
maximo = -9999
minimo = 9999

invitados = int(input("Cuantos invitados asistiran a su graduación: "))
while invitados < 1 or invitados > 7:
    invitados = int(input("Cuantos invitados asistiran a su graduación: "))

for i in range(invitados):
    edad = int(input("Ingresar la edad del invitado: "))
    while edad < 0 or edad > 105:
        edad = int(input("Ingresar la edad del invitado: "))
    
    if edad < 13 or edad > 55:
        print("ASIENTO")
    else:
        print("PARADO")
    
    if edad > maximo:
        maximo = edad
    if edad < minimo:
        minimo = edad

    suma = suma + edad

print("PROMEDIO:", suma / invitados)
print("La mayor edad es:", maximo, "años")
print("La menor edad es:", minimo, "años")