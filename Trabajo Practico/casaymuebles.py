# Introducción a la algoritmia - Trabajo práctico UADE - Casa y muebles

total = 0
precioNormal = 0
descuento = 0
recargo = 0
costoEnvio = 7000
costoInstalacion = 10000
precioFinal = 0
producto = ""
materialDeConstruccion = ""
envio = False
instalacion = False
efectivo = False
credito = False
pagoElegido = ""

print("""Bienvenido a Casa & Muebles!
Ingrese sus datos para regitrarlo en nuestra base de datos y así podrá empezar a comprar:""")

nombre = input("Nombre y apellido: ").title()
dni = input("DNI: ")
direccion = input("Dirección: ").capitalize()
telefono = input("Número de teléfono: ")

print("""
Registrando...
Registro exitoso.
   
A continuación te muestro todos nuestros productos y servicios disponibles:
1. SILLAS
2. MESAS
3. ROPEROS  
""")

# PIDE Y VALIDAD LA OPCIÓN CORRECTA
opcion = int(input("Elige una opción (1, 2 o 3): "))
while opcion != 1 and opcion != 2 and opcion != 3: # si opcion no es ni 1 ni 2 ni 3
    print("ERROR. Vuelva a intentar.")
    opcion = int(input("Elige una opción (1, 2 o 3): ")) # vuelve a pedir la opcion

# PROCESO DE COMPRA
# SILLAS
if opcion == 1:
    # guardo el producto elegido para mostrarlo en la factura
    producto = "SILLAS"

    # pide y valida tipo de material de construcción
    print("\nMATERIALES DE CONSTRUCCIÓN DE SILLAS Y SUS PRECIOS:")
    print("1. Plástico = $30.000")
    print("2. Metal = $40.000")
    print("3. Madera = $50.000\n")

    material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))
    while material != 1 and material != 2 and material != 3:
        print("ERROR. Vuelva a intentar.")
        material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))
    
    # pide y valida la cantidad a comprar
    cantidad = int(input("¿Cuantas sillas desea comprar?: "))
    while cantidad < 0: # si es un numero negativo vuelve a pedir
        print("ERROR. Vuelva a intentar.")
        cantidad = int(input("¿Cuantas sillas desea comprar?: "))

    # calcula el precio normal sin descuentos
    if material == 1:
        # calcula el precio
        precioNormal = cantidad * 30000
        # guarda el material de construcción para luego mostrarlo en la factura
        materialDeConstruccion = "Plástico"
    elif material == 2:
        # calcula el precio
        precioNormal = cantidad * 40000
        # guarda el material de construcción para luego mostrarlo en la factura
        materialDeConstruccion = "Metal"
    if material == 3:
        # calcula el precio
        precioNormal = cantidad * 50000
        # guarda el material de construcción para luego mostrarlo en la factura
        materialDeConstruccion = "Madera"

# MESAS
elif opcion == 2:
    # guardo el producto elegido para mostrarlo en la factura
    producto = "MESAS"

    # pide y valida tipo de material de construcción
    print("\nMATERIALES DE CONSTRUCCIÓN DE MESAS Y SUS PRECIOS:")
    print("1. Melamina = $80.000 (PROMOCIÓN 10% DE DESCUENTO)")
    print("2. Roble = $90.000")
    print("3. Mármol = $100.000")

    material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))
    while material != 1 and material != 2 and material != 3:
        print("ERROR. Vuelva a intentar.")
        material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))
    
    # pide y valida la cantidad a comprar
    cantidad = int(input("¿Cuantas mesas desea comprar?: "))
    while cantidad < 0: # si es un numero negativo vuelve a pedir
        print("ERROR. Vuelva a intentar.")
        cantidad = int(input("¿Cuantas mesas desea comprar?: "))

    # calcula el precio normal sin descuentos
    if material == 1:
        # calcula el precio
        precioNormal = cantidad * 80000
        # guarda el material de construcción para luego mostrarlo en la factura
        materialDeConstruccion = "Melamina"
    elif material == 2:
        # calcula el precio
        precioNormal = cantidad * 90000
        # guarda el material de construcción para luego mostrarlo en la factura
        materialDeConstruccion = "Roble"
    if material == 3:
        # calcula el precio
        precioNormal = cantidad * 100000
        # guarda el material de construcción para luego mostrarlo en la factura
        materialDeConstruccion = "Mármol"

# ROPEROS
if opcion == 3:
    # guardo el producto elegido para mostrarlo en la factura
    producto = "ROPEROS"

    # pide y valida tipo de material de construcción
    print("\nMATERIALES DE CONSTRUCCIÓN DE ROPEROS Y SUS PRECIOS:")
    print("1. Melamina = $200.000 (PROMOCIÓN 10% DE DESCUENTO)")
    print("2. Plywood = $220.000")
    print("3. Roble = $250.000")

    material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))
    while material != 1 and material != 2 and material != 3:
        print("ERROR. Vuelva a intentar.")
        material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))
    
    # pide y valida la cantidad a comprar
    cantidad = int(input("¿Cuantos roperos desea comprar?: "))
    while cantidad < 0: # si es un numero negativo vuelve a pedir
        print("ERROR. Vuelva a intentar.")
        cantidad = int(input("¿Cuantos roperos desea comprar?: "))

    # calcula el precio normal sin descuentos
    if material == 1:
        # calcula el precio
        precioNormal = cantidad * 200000
        # guarda el material de construcción para luego mostrarlo en la factura
        materialDeConstruccion = "Melamina"
    elif material == 2:
        # calcula el precio
        precioNormal = cantidad * 220000
        # guarda el material de construcción para luego mostrarlo en la factura
        materialDeConstruccion = "Plywood"
    if material == 3:
        # calcula el precio
        precioNormal = cantidad * 250000
        # guarda el material de construcción para luego mostrarlo en la factura
        materialDeConstruccion = "Roble"

# Pregunta si quiere contratar el envio o no y valida la respuesta
envio = input("¿Desea que lo enviemos a su dirección? (SI/NO): ").upper()
while envio != "SI" and envio != "NO":
    envio = input("¿Desea que lo enviemos a su dirección? (SI/NO): ").upper()

if envio == "SI":
    total = precioNormal + costoEnvio
    envio = True
else:
    envio = False

# Pregunta si quiere contratar nuestro servicio de instalacion o no y valida la respuesta
envio = input("¿Desea contratar el servicio de instalación? (SI/NO): ").upper()
while envio != "SI" and envio != "NO":
    envio = input("¿Desea contratar el servicio de instalación? (SI/NO): ").upper()

if envio == "SI":
    total = total + costoInstalacion
    instalacion = True
else:
    instalacion = False

# MEDIOS DE PAGO
print("""
MEDIOS DE PAGO - Conozca nuestras promociones y descuentos:
1. EFECTIVO (15% DE DESCUENTO)
2. TARJETA DE CRÉDITO (10% DE RECARGO)
3. TARJETA DE DÉBITO
4. TRANSFERENCIA
""")

# pide y verifica un medio de pago correcto
medioDePago = int(input("Elija su medio de pago (1, 2, 3 o 4): "))
while medioDePago != 1 and medioDePago != 2 and medioDePago != 3 and medioDePago != 4:
    print("ERROR. Vuelva a intentar.")
    medioDePago = int(input("Elija su medio de pago (1, 2, 3 o 4): "))

# verifica la opcion elegida y aplica descuentos segun corresponda
if medioDePago == 1:
    descuento = total * 0.15 # calcula el 15% del total
    total = total - descuento # aplica el 15% de descuento al total
    efectivo = True
    pagoElegido = "EFECTIVO (15% DE DESCUENTO)"
elif medioDePago == 2:
    recargo = total * 0.10 # calcula el 10% del total
    total = total + recargo # aplica el 10% de recargo
    credito = True
    pagoElegido = "TARJETA DE CRÉDITO (10% DE RECARGO)"
elif medioDePago == 3:
    pagoElegido = "TARJETA DE DÉBITO"
elif medioDePago == 4:
    pagoElegido = "TRANSFERENCIA"


# IMPRIME LA FACTURA FINAL DE COMPRA
print("""
FACTURA FINAL - 123456789890

DATOS DEL NEGOCIO
Empresa: Casa & Muebles
Dirección: Palermo, Guatemala 5999
CUIT: 30-61025233-4
MAIL: muebles@gmail.com
Teléfono: 1159536085

DATOS DEL CLIENTE""")

print("Nombre y apellido:", nombre)
print("DNI:", dni)
print("Dirección:", direccion)
print("Número de teléfono:", telefono)

print("\nDETALLES DE COMPRA")
print("Producto:", producto)
print("Material de construcción:", materialDeConstruccion)
print("Cantidad:", cantidad)

# envio e instalacion son de tipo bool por lo tanto evalua si es True o False
if envio:
    print("Servicio de envio: $", costoEnvio)
if instalacion:
    print("Servicio de instalación: $", costoInstalacion)

print("Medio de pago:", pagoElegido)

# evalua si paga selecciono pagar en efectivo o credito para mostrar sus valores correspondientes
if efectivo:
    print("Precio sin descuentos: $", precioNormal)
    print("Descuento por pagar en efectivo: $", descuento)
if credito:
    print("Precio sin descuentos: $", precioNormal)
    print("Recargo por pagar con tarjeta de crédito: $", recargo)

print("\nTOTAL: $", total)