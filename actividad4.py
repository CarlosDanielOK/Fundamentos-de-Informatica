opcion = int(input("Ingrese una opcion: "))
while opcion != 1 and opcion != 2 and opcion != 3:
    print("ERROR.")
    opcion = int(input("Ingrese una opcion: "))

if opcion == 1:
    print("OPCIÓN 1 - FUTBOL")
elif opcion == 2:
    print("OPCIÓN 2 - TENIS")
elif opcion == 3:
    print("OPCIÓN 3 - GOLF")