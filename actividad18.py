def opcionA(num):
    print(round(num,2))

def opcionB(num):
    print(round(num,5))

def opcionC(num):
    print(num)

pi = 3.14159265359

opcion = input("Ingrese una opcion (A, B, C): ").upper()
while opcion != "A" and opcion != "B" and opcion != "C":
    opcion = input("Ingrese una opcion (A, B, C): ").upper()

if opcion == "A":
    opcionA(pi)
elif opcion == "B":
    opcionB(pi)
else:
    opcionC(pi)