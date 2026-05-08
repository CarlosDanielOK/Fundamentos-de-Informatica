nombre = input("Ingrese su nombre: ")

def muyCorto():
    print("muy corto")

def comun():
    print("comun")

def muyLargo():
    print("muy largo")

if len(nombre) < 5:
    muyCorto()
elif len(nombre) <= 8:
    comun()
else:
    muyLargo()