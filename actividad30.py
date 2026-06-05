def cargar(lista, cantidad):
    for i in range(cantidad):
        num = int(input("Ingrese un numero: "))
        lista.append(num)

def recorrer(lista):
    suma = 0
    for i in range(len(lista)):
        suma += lista[i]
        
    if suma < 50:
        print("Poco")
    else:
        print("Mucho")
        
cantidad = int(input("Ingrese un numero: "))
while cantidad < 2 or cantidad > 8:
    cantidad = int(input("ERROR. Ingrese un numero: "))

lista = []
cargar(lista, cantidad)
recorrer(lista)