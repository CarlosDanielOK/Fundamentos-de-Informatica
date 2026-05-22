lista = []

cantidad = int(input("Cuantos elementos tendra la lista?: "))
while cantidad < 3 or cantidad > 8:
    cantidad = int(input("Cuantos elementos tendra la lista?: "))

for i in range(cantidad):
    animal = input("Ingrese un nombre de animal: ")
    lista.append(animal)

print(lista)
lista.pop(2)
print(lista)
