suma = 0

print("Bienvenido al restaurante")

dias = int(input("Ingrese cuantos dias trabajo en Febrero: "))

for i in range(dias):
    ganancia = float(input("Ingrese cuanto gano en el dia: $"))
    suma = suma + ganancia

promedio = suma / dias
print("En el mes de Febrero ganaste en total: $", suma)
print("En promedio ganaste: $", promedio)

if dias < 11 or promedio < 38750:
    print("REQUIERE MAYOR ESFUERZO")