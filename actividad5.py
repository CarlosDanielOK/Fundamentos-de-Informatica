intentos = 0

numero = int(input("Ingrese un número no menor a -30: "))
while numero <= -30 or numero >= 0:
    print("ERROR.")
    numero = int(input("Ingrese un número no menor a -30: "))
    intentos = intentos + 1

print("Intentos: ", intentos)