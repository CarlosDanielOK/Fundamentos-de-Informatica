mas_grande = -9999
mas_baja = 9999

for i in range(5):
    altura = float(input("Ingrese su altura: "))
    while altura < 1.40 or altura > 2.25:
        altura = float(input("Ingrese su altura: "))
    if altura > mas_grande:
        mas_grande = altura
    if altura < mas_baja:
        mas_baja = altura

print("La altura mas grande es", mas_grande, "metros")
print("La altura mas baja es", mas_baja, "metros")