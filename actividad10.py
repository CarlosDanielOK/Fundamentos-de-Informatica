# 1. Pedimos el número
numero = int(input("Ingrese un número: "))

# Variables iniciales
invertido = 0
es_negativo = False

# 2. Manejamos el signo negativo
if numero < 0:
    es_negativo = True
    numero = numero * -1  # Lo volvemos positivo para trabajar cómodos

# 3. El bucle mágico para invertir
while numero > 0:
    ultimo_digito = numero % 10  # Sacamos el último número (La R en tu Casio)
    invertido = (invertido * 10) + ultimo_digito  # Lo agregamos al nuevo número
    numero = int(numero / 10)  # Le quitamos el último número al original (La C en tu Casio)

# 4. Le devolvemos el signo si era necesario
if es_negativo:
    invertido = invertido * -1

# 5. Mostramos el resultado
print("El número invertido es:", invertido)
