def cargar_lista(lista):
    for i in range(4):
        nombre = input("Ingrese un nombre: ")
        while len(nombre) < 3 or len(nombre) > 12:
            nombre = input("ERROR - Ingrese un nombre: ")
        lista.append(nombre)


nombres1 = []
nombres2 = []
nombres3 = []
cargar_lista(nombres1)
print(nombres1)
cargar_lista(nombres2)
print(nombres2)
cargar_lista(nombres3)
print(nombres3)
