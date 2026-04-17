# Introducción a la algoritmia - Trabajo práctico UADE - Casa y muebles

print("""Bienvenido a Casa & Muebles!
¿Estás buscando algo en particular? A continuación te muestro todos nuestros productos y servicios disponibles:

1. SILLAS
2. MESAS
3. ROPEROS""")

opcion = int(input("\nElige una opción (1, 2 o 3): "))

if opcion == 1:
    print("\nTIPOS DE SILLAS Y SUS PRECIOS:")
    print("1. De plástico = $30.000")
    print("2. De metal = $40.000")
    print("3. De madera = $50.000")
