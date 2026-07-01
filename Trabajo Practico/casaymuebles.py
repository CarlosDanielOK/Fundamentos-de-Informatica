# Variable generales y contadores

numeroFactura = 1
recaudacionTotal = 0
maximoRecaudado = 0
contadorEnvio = 0
contadorEfectivo = 0

# Se realizaron 3 procesos de venta

for venta in range(3):
    total = 0
    precioNormal = 0
    descuento = 0
    recargo = 0
    costoEnvio = 7000
    costoInstalacion = 10000
    producto = ""
    materialDeConstruccion = ""
    envio = False
    instalacion = False
    efectivo = False
    credito = False
    pagoElegido = ""

    # Solicita los datos del cliente

    print("""
Bienvenido a Casa & Muebles!
Ingrese sus datos para registrarlo en nuestra base de datos y así podrá empezar a comprar:
""")

    nombre = input("Nombre y apellido: ").title()
    confirmacion = input("Tu nombre es", nombre, "¿Es correcto? (SI/NO): ").upper()
    while confirmacion != "SI":
        nombre = input("Nombre y apellido: ").title()
        confirmacion = input("Tu nombre es", nombre, "¿Es correcto? (SI/NO): ").upper()

    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        print(
            "ERROR. Debe ser mayor de 18 años. Ingrese la edad de un adulto responsable."
        )
        edad = int(input("Ingrese su edad: "))

    confirmacion = input("Tu edad es", edad, "¿Es correcta? (SI/NO): ").upper()
    while confirmacion != "SI":
        edad = int(input("Ingrese su edad: "))
        while edad < 18:
            print(
                "ERROR. Debe ser mayor de 18 años. Ingrese la edad de un adulto responsable."
            )
            edad = int(input("Ingrese su edad: "))
        confirmacion = input("Tu edad es", edad, "¿Es correcta? (SI/NO): ").upper()

    # Validacion del dni

    dni = input("DNI: ")
    while len(dni) != 8:  # Poner limite de 8
        print("ERROR. El DNI debe tener 8 números.")
        dni = input("DNI: ")

    confirmacion = input("Tu DNI es", dni, "¿Es correcto? (SI/NO): ").upper()
    while confirmacion != "SI":
        dni = input("DNI: ")

        while len(dni) != 8:
            print("ERROR. El DNI debe tener 8 números.")
            dni = input("DNI: ")
        confirmacion = input("Tu DNI es", dni, "¿Es correcto? (SI/NO): ").upper()

    direccion = input("Ingrese su direccion: ").capitalize()
    while len(direccion) < 5:
        print("ERROR. La dirección debe tener mínimo 5 caracteres.")
        direccion = input("Dirección: ").capitalize()

    confirmacion = input(
        "Tu dirección es", direccion, "¿Es correcta? (SI/NO): "
    ).upper()
    while confirmacion != "SI":
        direccion = input("Dirección: ").capitalize()
        while len(direccion) < 5:
            print("ERROR. La dirección debe tener mínimo 5 caracteres.")
            direccion = input("Dirección: ").capitalize()
        confirmacion = input(
            "Tu dirección es", direccion, "¿Es correcta? (SI/NO): "
        ).upper()

    telefono = input("Número de teléfono: ")
    while len(telefono) < 8:
        print("ERROR. Número inválido.")
        telefono = input("Número de teléfono: ")

    confirmacion = input(
        "Tu número de teléfono es", telefono, "¿Es correcto? (SI/NO): "
    ).upper()
    while confirmacion != "SI":
        telefono = input("Número de teléfono: ")
        while len(telefono) < 8:
            print("ERROR. El número debe tener mas de 8 números.")
            telefono = input("Número de teléfono: ")

        confirmacion = input(
            "Tu número de teléfono es", telefono, "¿Es correcto? (SI/NO): "
        ).upper()

    # Productos disponibles

    print("""
Registrando...
Registro exitoso.

A continuación te muestro todos nuestros productos y servicios disponibles:
1. SILLAS
2. MESAS
3. ROPEROS
""")

    # PIDE Y VALIDA LA OPCIÓN CORRECTA
    opcion = int(input("Elige una opción (1, 2 o 3): "))
    while opcion != 1 and opcion != 2 and opcion != 3:
        print("ERROR. Vuelva a intentar.")
        opcion = int(input("Elige una opción (1, 2 o 3): "))

    # SILLAS
    if opcion == 1:
        producto = "SILLAS"

        print("\nMATERIALES DE CONSTRUCCIÓN DE SILLAS Y SUS PRECIOS:")
        print("1. Plástico = $30.000")
        print("2. Metal = $40.000")
        print("3. Madera = $50.000\n")

        material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))
        while material != 1 and material != 2 and material != 3:
            print("ERROR. Vuelva a intentar.")
            material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))

        cantidad = int(input("¿Cuántas sillas desea comprar?: "))
        while cantidad <= 0:
            print("ERROR. Vuelva a intentar.")
            cantidad = int(input("¿Cuántas sillas desea comprar?: "))

        if material == 1:
            precioNormal = cantidad * 30000
            materialDeConstruccion = "Plástico"

        elif material == 2:
            precioNormal = cantidad * 40000
            materialDeConstruccion = "Metal"

        elif material == 3:
            precioNormal = cantidad * 50000
            materialDeConstruccion = "Madera"

    # MESAS
    elif opcion == 2:
        producto = "MESAS"

        print("\nMATERIALES DE CONSTRUCCIÓN DE MESAS Y SUS PRECIOS:")
        print("1. Melamina = $80.000")
        print("2. Roble = $90.000")
        print("3. Mármol = $100.000")

        material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))
        while material != 1 and material != 2 and material != 3:
            print("ERROR. Vuelva a intentar.")
            material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))

        cantidad = int(input("¿Cuántas mesas desea comprar?: "))
        while cantidad <= 0:
            print("ERROR. Vuelva a intentar.")
            cantidad = int(input("¿Cuántas mesas desea comprar?: "))

        if material == 1:
            precioNormal = cantidad * 80000
            materialDeConstruccion = "Melamina"

        elif material == 2:
            precioNormal = cantidad * 90000
            materialDeConstruccion = "Roble"

        elif material == 3:
            precioNormal = cantidad * 100000
            materialDeConstruccion = "Mármol"

    # ROPEROS
    elif opcion == 3:
        producto = "ROPEROS"

        print("\nMATERIALES DE CONSTRUCCIÓN DE ROPEROS Y SUS PRECIOS:")
        print("1. Melamina = $200.000")
        print("2. Plywood = $220.000")
        print("3. Roble = $250.000")

        material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))
        while material != 1 and material != 2 and material != 3:
            print("ERROR. Vuelva a intentar.")
            material = int(input("¿Cuál desea comprar? (1, 2 o 3): "))

        cantidad = int(input("¿Cuántos roperos desea comprar?: "))
        while cantidad <= 0:
            print("ERROR. Vuelva a intentar.")
            cantidad = int(input("¿Cuántos roperos desea comprar?: "))

        if material == 1:
            precioNormal = cantidad * 200000
            materialDeConstruccion = "Melamina"

        elif material == 2:
            precioNormal = cantidad * 220000
            materialDeConstruccion = "Plywood"

        elif material == 3:
            precioNormal = cantidad * 250000
            materialDeConstruccion = "Roble"

    total = precioNormal

    # ENVÍO
    print("\nSERVICIO DE ENVÍO - Costo: $7.000")
    envio = input("¿Desea que lo enviemos a su dirección? (SI/NO): ").upper()
    while envio != "SI" and envio != "NO":
        envio = input("¿Desea que lo enviemos a su dirección? (SI/NO): ").upper()
    if envio == "SI":
        total = total + costoEnvio
        envio = True
        contadorEnvio = contadorEnvio + 1

    else:
        envio = False

    direccion = input("Ingrese su direccion: ").capitalize()
    while len(direccion) < 5:
        print("ERROR. La dirección debe tener mínimo 5 caracteres.")
        direccion = input("Ingrese su direccion: ").capitalize()

    confirmacion = input(
        "Tu dirección es", direccion, "¿Es correcta? (SI/NO): "
    ).upper()
    while confirmacion != "SI":
        direccion = input("Dirección: ").capitalize()
        while len(direccion) < 5:
            print("ERROR. La dirección debe tener mínimo 5 caracteres.")
            direccion = input("Dirección: ").capitalize()
        confirmacion = input(
            "Tu dirección es", direccion, "¿Es correcta? (SI/NO): "
        ).upper()

    # INSTALACIÓN
    print("\nSERVICIO DE INSTALACIÓN - Costo: $10.000")
    instalacion = input(
        "¿Desea contratar el servicio de instalación? (SI/NO): "
    ).upper()

    while instalacion != "SI" and instalacion != "NO":
        instalacion = input(
            "¿Desea contratar el servicio de instalación? (SI/NO): "
        ).upper()

    if instalacion == "SI":
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

    medioDePago = int(input("Elija su medio de pago (1, 2, 3 o 4): "))

    while (
        medioDePago != 1 and medioDePago != 2 and medioDePago != 3 and medioDePago != 4
    ):
        print("ERROR. Vuelva a intentar.")
        medioDePago = int(input("Elija su medio de pago (1, 2, 3 o 4): "))

    if medioDePago == 1:
        descuento = round(total * 0.15, 2)
        total = total - descuento
        efectivo = True
        pagoElegido = "EFECTIVO (15% DE DESCUENTO)"
        contadorEfectivo = contadorEfectivo + 1

    elif medioDePago == 2:
        recargo = round(total * 0.10, 2)
        total = total + recargo
        credito = True
        pagoElegido = "TARJETA DE CRÉDITO (10% DE RECARGO)"

    elif medioDePago == 3:
        pagoElegido = "TARJETA DE DÉBITO"

    elif medioDePago == 4:
        pagoElegido = "TRANSFERENCIA"

    # ACUMULADORES Y MÁXIMO
    recaudacionTotal = recaudacionTotal + total

    if total > maximoRecaudado:
        maximoRecaudado = total

    # FACTURA
    print("""
FACTURA FINAL
""")

    print("Número de factura:", numeroFactura)

    print("""
DATOS DEL NEGOCIO
Empresa: Casa & Muebles
Dirección: Palermo, Guatemala 5999
CUIT: 30-61025233-4
MAIL: muebles@gmail.com
Teléfono: 1159536085
""")

    print("DATOS DEL CLIENTE")
    print("Nombre y apellido:", nombre)
    print("DNI:", dni)
    print("Dirección:", direccion)
    print("Número de teléfono:", telefono)

    print("\nDETALLES DE COMPRA")
    print("Producto:", producto)
    print("Material de construcción:", materialDeConstruccion)
    print("Cantidad:", cantidad)

    if envio:
        print("Servicio de envío: $", costoEnvio)

    if instalacion:
        print("Servicio de instalación: $", costoInstalacion)

    print("Medio de pago:", pagoElegido)

    if efectivo:
        print("Precio sin descuentos: $", precioNormal)
        print("Descuento por pagar en efectivo: $", descuento)

    if credito:
        print("Precio sin descuentos: $", precioNormal)
        print("Recargo por pagar con tarjeta de crédito: $", recargo)

    print("\nTOTAL: $", round(total, 2))

    numeroFactura = numeroFactura + 1


promedioVentas = recaudacionTotal / 3
porcentajeEnvio = (contadorEnvio * 100) / 3
porcentajeEfectivo = (contadorEfectivo * 100) / 3

print("""

RESULTADO FINAL

""")

print("Total recaudado: $", round(recaudacionTotal, 2))
print("Máximo recaudado en una venta: $", round(maximoRecaudado, 2))
print("Promedio de ventas: $", round(promedioVentas, 2))
print("Porcentaje de clientes con envío:", round(porcentajeEnvio, 2), "%")
print("Porcentaje de pagos en efectivo:", round(porcentajeEfectivo, 2), "%")
