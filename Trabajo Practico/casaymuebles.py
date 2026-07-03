import random

productos = ["Sillas", "Mesas", "Roperos"]

silla_materiales = ["Plastico", "Metal", "Madera"]
silla_precio = [30000, 40000, 50000]
silla_cantidad = [0, 0, 0]

mesa_materiales = ["Melamina", "Roble", "Marmol"]
mesa_precio = [80000, 90000, 100000]
mesa_cantidad = [0, 0, 0]

ropero_materiales = ["Melamina", "Plywood", "Roble"]
ropero_precio = [200000, 220000, 250000]
ropero_cantidad = [0, 0, 0]

precio_envio = 7000
precio_instalacion = 10000


# Listas principales
facturas = []
nombres = []
dnis = []
totales = []




def presentacion():
    print("Número de grupo: 3")
    print("Integrantes: Candela Nuñez, Lizbeth Alejo, Carlos Lazo")


def pedir_datos_cliente():
    print("Le pediremos sus datos para registrarlo en nuestra base de datos.")

    nombre = validar_nombre()
    edad = validar_edad()
    dni = validar_dni()
    telefono = validar_telefono()
    direccion = validar_direccion()

    return nombre, edad, dni, telefono, direccion


# VALIDACIONES DE DATOS DEL CLIENTE
def validar_nombre():
    nombre = input("Ingrese su nombre y apellido: ").title()
    confirmar = input("Tu nombre es " + nombre + ". ¿Es correcto? (SI/NO): ").upper()
    while confirmar != "SI":
        nombre = input("Ingrese su nombre y apellido: ").title()
        confirmar = input(
            "Tu nombre es " + nombre + ". ¿Es correcto? (SI/NO): "
        ).upper()

    return nombre


def validar_edad():
    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        print(
            "Lo sentimos. La edad mínima permitida para realizar compras es de 18 años."
        )
        edad = int(input("Ingrese su edad: "))

    confirmar = input("Tu edad es " + str(edad) + ". ¿Es correcto? (SI/NO): ").upper()
    while confirmar != "SI":
        edad = int(input("Ingrese su edad: "))
        while edad < 18:
            print(
                "Lo sentimos. La edad mínima permitida para realizar compras es de 18 años."
            )
            edad = int(input("Ingrese su edad: "))
        confirmar = input(
            "Tu edad es " + str(edad) + ". ¿Es correcto? (SI/NO): "
        ).upper()

    return edad


def validar_dni():
    dni = input("Ingrese su DNI: ")
    while len(dni) != 8:
        print("ERROR. El DNI debe tener 8 dígitos.")
        dni = input("Ingrese su DNI: ")

    confirmar = input("Tu DNI es " + dni + ". ¿Es correcto? (SI/NO): ").upper()
    while confirmar != "SI":
        dni = input("Ingrese su DNI: ")
        while len(dni) != 8:
            print("ERROR. El DNI debe tener 8 dígitos.")
            dni = input("Ingrese su DNI: ")
        confirmar = input("Tu DNI es " + dni + ". ¿Es correcto? (SI/NO): ").upper()

    return dni


def validar_telefono():
    telefono = input("Ingrese su número de teléfono: ")
    while len(telefono) != 10:
        print("ERROR. El número de teléfono debe tener 10 dígitos.")
        telefono = input("Ingrese su número de teléfono: ")

    confirmar = input("Tu número es " + telefono + ". ¿Es correcto? (SI/NO): ").upper()
    while confirmar != "SI":
        telefono = input("Ingrese su número de teléfono: ")
        while len(telefono) != 10:
            print("ERROR. El número de teléfono debe tener 10 dígitos.")
            telefono = input("Ingrese su número de teléfono: ")
        confirmar = input(
            "Tu número es " + telefono + ". ¿Es correcto? (SI/NO): "
        ).upper()

    return telefono


def validar_direccion():
    direccion = input("Ingrese su dirección: ").title()
    confirmar = input("Tu dirección es " + direccion + ". ¿Es correcto? (SI/NO): ").upper()
    while confirmar != "SI":
        direccion = input("Ingrese su dirección: ").title()
        confirmar = input("Tu dirección es " + direccion + ". ¿Es correcto? (SI/NO): ").upper()

    return direccion


# GENERAR FACTURAS
def esValido(lista, n):
    for i in range(len(lista)):
        if lista[i] == n:
            return False
    return True

def generar_numero_factura():
    lista = []
    while len(lista) < 3:
        n = random.randint(1000, 9999)
        if esValido(lista, n) == True:
            lista.append(n)
    return lista

def servicios(subtotal):
    cantidad_envios = 0
    cantidad_instalaciones = 0

    print("---PRECIOS DE SERVICIOS---")
    print("Disponemos de servicio de Envío a domicilio por un valor fijo de: $", precio_envio)
    print("Disponemos de servicio de Instalación premium por un valor fijo de: $", precio_instalacion)

    quiere_envio = input("¿Desea contratar el servicio de envío? (SI/NO): ").upper()
    if quiere_envio == "SI":
        subtotal = subtotal + precio_envio
        cantidad_envios = cantidad_envios + 1
    
    quiere_instalacion = input("¿Desea contratar el servicio de instalación? (SI/NO): ").upper()
    if quiere_instalacion == "SI":
        subtotal = subtotal + precio_instalacion
        cantidad_instalaciones = cantidad_instalaciones + 1
    
    return subtotal, cantidad_envios, cantidad_instalaciones

def procesar_compra():
    comprar_mas = "SI"
    carrito = []

    while comprar_mas == "SI":
        print()
        print("--- CATÁLOGO DE PRODUCTOS DISPONIBLES ---")
        print("1. SILLAS")
        print("2. MESAS")
        print("3. ROPEROS")

        opcion = int(input("Elige una opción (1, 2 o 3): "))
        while opcion != 1 and opcion != 2 and opcion != 3:
            print("ERROR. Vuelva a intentar.")
            opcion = int(input("Elige una opción (1, 2 o 3): "))
        print()

        if opcion == 1:
            print("MATERIALES DE SILLAS:")
            for i in range(len(silla_materiales)):
                print(str(i+1) + ". " + silla_materiales[i] + " = $" + str(silla_precio[i]))

            material = int(input("Seleccione material (1, 2 o 3): "))
            while material != 1 and material != 2 and material != 3:
                print("ERROR. Opción inválida. Vuelva a intentar.")
                material = int(input("Seleccione material (1, 2 o 3): "))

            cantidad = int(input("¿Cuántas sillas desea?: "))
            while cantidad <= 0:
                print("ERROR. La cantidad debe ser mayor a 0.")
                cantidad = int(input("¿Cuántas sillas desea?: "))
            
            # AGREGO AL CARRITO NOMBRE DEL PRODUCTO, MATERIAL, PRECIO Y CANTIDAD
            if material == 1:
                silla_cantidad[0] = cantidad
                carrito.append([productos[0], silla_materiales[0], silla_precio[0], silla_cantidad[0]])
            elif material == 2:
                silla_cantidad[1] = cantidad
                carrito.append([productos[0], silla_materiales[1], silla_precio[1], silla_cantidad[1]])
            elif material == 3:
                silla_cantidad[2] = cantidad
                carrito.append([productos[0], silla_materiales[2], silla_precio[2], silla_cantidad[2]])

        elif opcion == 2:
            print("MATERIALES DE MESAS:")
            for i in range(len(mesa_materiales)):
                print(str(i+1) + ". " + mesa_materiales[i] + " = $" + str(mesa_precio[i]))

            material = int(input("Seleccione material (1, 2 o 3): "))
            while material != 1 and material != 2 and material != 3:
                print("ERROR. Opción inválida. Vuelva a intentar.")
                material = int(input("Seleccione material (1, 2 o 3): "))

            cantidad = int(input("¿Cuántas mesas desea?: "))
            while cantidad <= 0:
                print("ERROR. La cantidad debe ser mayor a 0.")
                cantidad = int(input("¿Cuántas mesas desea?: "))
            
            # AGREGO AL CARRITO NOMBRE DEL PRODUCTO, MATERIAL, PRECIO Y CANTIDAD
            if material == 1:
                mesa_cantidad[0] = cantidad
                carrito.append([productos[1], mesa_materiales[0], mesa_precio[0], mesa_cantidad[0]])
            elif material == 2:
                mesa_cantidad[1] = cantidad
                carrito.append([productos[1], mesa_materiales[1], mesa_precio[1], mesa_cantidad[1]])
            elif material == 3:
                mesa_cantidad[2] = cantidad
                carrito.append([productos[1], mesa_materiales[2], mesa_precio[2], mesa_cantidad[2]])

        elif opcion == 3:
            print("MATERIALES DE ROPEROS:")
            for i in range(len(ropero_materiales)):
                print(str(i+1) + ". " + ropero_materiales[i] + " = $" + str(ropero_precio[i]))

            material = int(input("Seleccione material (1, 2 o 3): "))
            while material != 1 and material != 2 and material != 3:
                print("ERROR. Opción inválida. Vuelva a intentar.")
                material = int(input("Seleccione material (1, 2 o 3): "))

            cantidad = int(input("¿Cuántas roperos desea?: "))
            while cantidad <= 0:
                print("ERROR. La cantidad debe ser mayor a 0.")
                cantidad = int(input("¿Cuántos roperos desea?: "))
            
            # AGREGO AL CARRITO NOMBRE DEL PRODUCTO, MATERIAL, PRECIO Y CANTIDAD
            if material == 1:
                ropero_cantidad[0] = cantidad
                carrito.append([productos[2], ropero_materiales[0], ropero_precio[0], ropero_cantidad[0]])
            elif material == 2:
                ropero_cantidad[1] = cantidad
                carrito.append([productos[2], ropero_materiales[1], ropero_precio[1], ropero_cantidad[1]])
            elif material == 3:
                ropero_cantidad[2] = cantidad
                carrito.append([productos[2], ropero_materiales[2], ropero_precio[2], ropero_cantidad[2]])
                
        comprar_mas = input("¿Desea agregar otro tipo de producto a esta misma compra? (SI/NO): ").upper()
    

    # CALCULAR EL SUBTOTAL DE ESTA COMPRA
    subtotal = 0
    for i in range(len(carrito)):
        subtotal = subtotal + (carrito[i][2] * carrito[i][3])

    return subtotal, carrito


# PROGRAMA PRINCIPAL

for venta in range(3):
    print("BIENVENIDO A CASA & MUEBLES - VENTA NRO:", venta + 1)

    nombre, edad, dni, telefono, direccion = pedir_datos_cliente()

    print()
    subtotal, carrito = procesar_compra()

    print()
    subtotal, cantidad_envios, cantidad_instalaciones = servicios(subtotal)
    
    numero_factura = generar_numero_factura()

    """
    print(
        "Disponemos de servicio de Envío a domicilio por un valor fijo de: $",
        precio_envio,
    )
    print(
        "Disponemos de servicio de Instalación premium por un valor fijo de: $",
        precio_instalacion,
    )

    quiere_envio = input("¿Desea contratar el servicio de envío? (SI/NO): ").upper()
    if quiere_envio == "SI":
        monto_carrito = monto_carrito + precio_envio
        votos_envio = votos_envio + 1

    quiere_instalacion = input(
        "¿Desea contratar el servicio de instalación? (SI/NO): "
    ).upper()
    if quiere_instalacion == "SI":
        monto_carrito = monto_carrito + precio_instalacion
        votos_instalacion = votos_instalacion + 1

    monto_final = round(monto_carrito, 2)
    total_ventas = total_ventas + monto_final

    # Máximo y mínimo manuales
    if monto_final > monto_maximo:
        monto_maximo = monto_final

    if monto_final < monto_minimo:
        monto_minimo = monto_final

    num_factura = generar_factura(facturas)
    facturas.append(num_factura)
    #nombres.append(nombre_cliente)
    #dnis.append(dni_cliente)
    totales.append(monto_final)

matriz = []
for i in range(3):
    fila = [facturas[i], nombres[i], dnis[i], totales[i]]
    matriz.append(fila)

# Burbujeo
for i in range(len(matriz) - 1):
    for j in range(len(matriz) - 1 - i):
        if matriz[j] > matriz[j + 1]:
            temporal = matriz[j]
            matriz[j] = matriz[j + 1]
            matriz[j + 1] = temporal

print()
print("----FACTURA----")
for i in range(len(matriz)):
    print(
        "Factura:",
        matriz[i][0],
        " | Cliente:",
        matriz[i][1],
        " | DNI:",
        matriz[i][2],
        " | Total: $",
        matriz[i][3],
    )

# Estadísticas finales
promedio = round(total_ventas / 3, 2)
porcentaje_envio = round((votos_envio / 3) * 100, 2)
porcentaje_instal = round((votos_instalacion / 3) * 100, 2)

print()
print("--- REPORTES Y ESTADÍSTICAS GENERALES ---")
print("Total Recaudado general:       $", total_ventas)
print("Máximo monto recaudado:        $", monto_maximo)
print("Mínimo monto recaudado:        $", monto_minimo)
print("Promedio de recaudación:       $", promedio)
print("Porcentaje de uso de Envíos:   ", porcentaje_envio, "%")
print("Porcentaje de Instalaciones:   ", porcentaje_instal, "%")
print()

# Buscador secuencial de clientes
print("---BUSCADOR DE CLIENTES---")
"""
buscar_otro = "SI"

while buscar_otro == "SI":
    exito_busqueda = 0

    while exito_busqueda == 0:
        entrada_dni = input("Ingrese el DNI del cliente para verificar su registro: ")
        indice = -1

        for i in range(len(dnis)):
            if dnis[i] == entrada_dni:
                exito_busqueda = 1
                indice = i

        if exito_busqueda == 1:
            print("¡Cliente localizado con éxito! Ficha de compra:")
            print("Nombre:", nombres[indice])
            print("DNI:", dnis[indice])
            print("Factura Asignada:", facturas[indice])
            print("Total Facturado: $", totales[indice])
        else:
            print(
                "El DNI ingresado no coincide con ninguna de nuestras 3 ventas. Vuelva a intentar."
            )

    buscar_otro = input("\n¿Desea buscar a otro cliente? (SI/NO): ").upper()
print("¡Gracias por su compra!")

if len(facturas) > 0:
    facturas.pop()
