maximo = -9999
nombreMasLargo = ""
caracteresDelNombre = 0

cantidad = int(input("Ingrese la cantidad de participantes: "))
for i in range(cantidad):
    nombre = input("Ingrese el nombre del participante: ")
    caracteres = len(nombre)
    if caracteres > maximo:
        maximo = caracteres
        nombreMasLargo = nombre
        caracteresDelNombre = caracteres

print("El nombre mas largo es", nombreMasLargo, "y tiene", caracteresDelNombre, "caracteres")