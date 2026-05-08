def sumar():
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese un numero: "))
    print(num1 + num2)

def restar():
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese un numero: "))
    print(num1 - num2)

def multiplicacion():
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese un numero: "))
    print(num1 * num2)

def division():
    num1 = float(input("Ingrese un numero: "))
    num2 = float(input("Ingrese un numero: "))
    print(num1 / num2)

consulta = input("Que operacion quiere realizar?: ").lower()
while consulta != "suma" and consulta != "resta" and consulta != "multiplicacion" and consulta != "division":
    consulta = input("Que operacion quiere realizar?: ").lower()

if consulta == "suma":
    sumar()
elif consulta == "resta":
    restar()
elif consulta == "multiplicacion":
    multiplicacion()
else:
    division()