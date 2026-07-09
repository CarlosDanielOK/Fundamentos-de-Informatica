# GRUPO N°: 03
# INTEGRANTES:
# - Candela Nuñez
# - Carlos Lazo
# - Lizbeth Alejo

import random


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

    etiquetas_cliente = ["Nombre: ", "Edad: ", "DNI: ", "Teléfono: ", "Dirección: "]
    datos_cliente = [nombre, edad, dni, telefono, direccion]

    return etiquetas_cliente, datos_cliente


# VALIDACIONES DE DATOS DEL CLIENTE
def validar_nombre():
    nombre = input("Ingrese su nombre y apellido: ").title()
    confirmar = input("Tu nombre es " + nombre + ". ¿Es correcto? (SI/NO): ").upper()
    while confirmar != "SI":
        nombre = input("Ingrese su nombre y apellido: ").title()
        confirmar = input("Tu nombre es " + nombre + ". ¿Es correcto? (SI/NO): ").upper()

    return nombre


def validar_edad():
    edad = int(input("Ingrese su edad: "))
    while edad < 0 or edad > 100:
        print("Error. Edad no valida.")
        edad = int(input("Ingrese su edad: "))

    confirmar = input("Tu edad es " + str(edad) + ". ¿Es correcto? (SI/NO): ").upper()
    while confirmar != "SI":
        edad = int(input("Ingrese su edad: "))
        while edad < 0 or edad > 100:
            print("Error. Edad no valida.")
            edad = int(input("Ingrese su edad: "))
        confirmar = input("Tu edad es " + str(edad) + ". ¿Es correcto? (SI/NO): ").upper()

    return str(edad)


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
        confirmar = input("Tu número es " + telefono + ". ¿Es correcto? (SI/NO): ").upper()

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

def generar_numero_factura(lista_facturas):
    n = random.randint(1000, 9999)
    valido = 0
    if esValido(lista_facturas, n) == True:
        valido = 1

    while valido == 0:
        n = random.randint(1000, 9999)
        valido = 0
        if esValido(lista_facturas, n) == True:
            valido = 1
    return n

def servicios(subtotal, precio_envio, precio_instalacion):
    servicios_contratados = ""
    cantidad_envios = 0
    cantidad_instalaciones = 0

    print("---PRECIOS DE SERVICIOS---")

    quiere_envio = input("¿Desea contratar el servicio de envío ($" + str(precio_envio) + ")? (SI/NO): ").upper()
    if quiere_envio == "SI":
        subtotal = subtotal + precio_envio
        cantidad_envios = cantidad_envios + 1
        servicios_contratados = servicios_contratados + "Servicio de envío: $" + str(precio_envio)
    
    quiere_instalacion = input("¿Desea contratar el servicio de instalación ($" + str(precio_instalacion) + ") (SI/NO): ").upper()
    if quiere_instalacion == "SI":
        subtotal = subtotal + precio_instalacion
        cantidad_instalaciones = cantidad_instalaciones + 1
        servicios_contratados = servicios_contratados + "\nServicio de instalación: $" + str(precio_instalacion)
    
    return servicios_contratados, subtotal, cantidad_envios, cantidad_instalaciones

def procesar_compra(
    productos,
    silla_materiales,
    silla_precio,
    silla_cantidad,
    mesa_materiales,
    mesa_precio,
    mesa_cantidad,
    ropero_materiales,
    ropero_precio,
    ropero_cantidad,
):
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
                carrito.append([productos[0], silla_materiales[0], silla_cantidad[0], silla_precio[0]])
            elif material == 2:
                silla_cantidad[1] = cantidad
                carrito.append([productos[0], silla_materiales[1], silla_cantidad[1], silla_precio[1]])
            elif material == 3:
                silla_cantidad[2] = cantidad
                carrito.append([productos[0], silla_materiales[2], silla_cantidad[2], silla_precio[2]])

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
                carrito.append([productos[1], mesa_materiales[0], mesa_cantidad[0], mesa_precio[0]])
            elif material == 2:
                mesa_cantidad[1] = cantidad
                carrito.append([productos[1], mesa_materiales[1], mesa_cantidad[1], mesa_precio[1]])
            elif material == 3:
                mesa_cantidad[2] = cantidad
                carrito.append([productos[1], mesa_materiales[2], mesa_cantidad[2], mesa_precio[2]])

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
                carrito.append([productos[2], ropero_materiales[0], ropero_cantidad[0], ropero_precio[0]])
            elif material == 2:
                ropero_cantidad[1] = cantidad
                carrito.append([productos[2], ropero_materiales[1], ropero_cantidad[1], ropero_precio[1]])
            elif material == 3:
                ropero_cantidad[2] = cantidad
                carrito.append([productos[2], ropero_materiales[2], ropero_cantidad[2], ropero_precio[2]])
                
        comprar_mas = input("¿Desea agregar otro tipo de producto a esta misma compra? (SI/NO): ").upper()
    

    # CALCULAR EL SUBTOTAL DE ESTA COMPRA
    subtotal = 0
    for i in range(len(carrito)):
        subtotal = subtotal + (carrito[i][2] * carrito[i][3])

    return subtotal, carrito

def generar_factura(numero_factura, etiquetas_negocio, datos_negocio, etiquetas_cliente, datos_cliente, carrito, servicios_contratados, subtotal, matriz):
    print("\n---FACTURA FINAL---")
    print("Número de factura:", numero_factura)

    print("\nDATOS DEL NEGOCIO")
    for i in range(len(datos_negocio)):
        print(etiquetas_negocio[i] + datos_negocio[i])
    
    print("\nDATOS DEL CLIENTE")
    for i in range(len(datos_cliente)):
        print(etiquetas_cliente[i] + datos_cliente[i])

    print("\nPRODUCTOS COMPRADOS")
    print("Producto | Material | Cantidad | Precio x unidad")
    for i in range(len(carrito)):
        print(carrito[i])
    
    print(servicios_contratados)

    print("TOTAL A PAGAR: $", subtotal)
    
    matriz.append([numero_factura, datos_cliente[0], datos_cliente[2], subtotal])

    return matriz

def factura_final(matriz):
    print("Nro factura | Nombre cliente | DNI cliente | TOTAL A PAGAR")
    for i in range(len(matriz)):
        print(matriz[i])

def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def calcular_estadisticas(totales, contador_envio, contador_instalacion):
    total_recaudado = 0
    monto_maximo = 0
    monto_minimo = 999999999

    for i in range(len(totales)):
        total_recaudado = total_recaudado + totales[i]
        if totales[i] > monto_maximo:
            monto_maximo = totales[i]
        if totales[i] < monto_minimo:
            monto_minimo = totales[i]

    promedio = total_recaudado / len(totales)
    porcentaje_envio = (contador_envio * 100) / len(totales)
    porcentaje_instalacion = (contador_instalacion * 100) / len(totales)

    return total_recaudado, monto_maximo, monto_minimo, promedio, porcentaje_envio, porcentaje_instalacion


def buscar_cliente_lineal(dnis, nombres, facturas, totales):
    print()
    print("--- BUSCADOR DE CLIENTES ---")
    seguir_busqueda = "SI"

    while seguir_busqueda == "SI":
        dni_buscar = input("Ingrese un DNI para buscar al cliente: ")
        indice = 0
        encontrado = 0

        while indice < len(dnis) and encontrado == 0:
            if dnis[indice] == dni_buscar:
                encontrado = 1
            else:
                indice = indice + 1

        if encontrado == 1:
            print("\nCliente encontrado:")
            print("Nombre:", nombres[indice])
            print("DNI:", dnis[indice])
            print("Factura:", facturas[indice])
            print("Total facturado: $", totales[indice])
        else:
            print("El DNI no coincide con ningún cliente. Vuelva a intentar.")

        seguir_busqueda = input("\n¿Desea buscar otro cliente? (SI/NO): ").upper()


# PROGRAMA PRINCIPAL

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

etiquetas_negocio = ["Nombre: ", "Dirección: ", "CUIT: ", "Email: ", "Teléfono: "]
datos_negocio = ["Casa & Muebles", "Palermo, Guatemala 5999" ,"30-61025233-4", "muebles@gmail.com", "1159536085"]

# Listas principales
facturas = []
nombres = []
dnis = []
totales = []
contador_envio = 0
contador_instalacion = 0

for venta in range(3):
    print("\nBIENVENIDO A CASA & MUEBLES - VENTA NRO:", venta + 1)

    etiquetas_cliente, datos_cliente = pedir_datos_cliente()

    print()
    subtotal, carrito = procesar_compra(
        productos,
        silla_materiales,
        silla_precio,
        silla_cantidad,
        mesa_materiales,
        mesa_precio,
        mesa_cantidad,
        ropero_materiales,
        ropero_precio,
        ropero_cantidad,
    )

    print()
    servicios_contratados, subtotal, cantidad_envios, cantidad_instalaciones = servicios(
        subtotal, precio_envio, precio_instalacion
    )
    contador_envio = contador_envio + cantidad_envios
    contador_instalacion = contador_instalacion + cantidad_instalaciones
    
    numero_factura = generar_numero_factura(facturas)

    matriz = []
    matriz_factura_final = generar_factura(numero_factura, etiquetas_negocio, datos_negocio, etiquetas_cliente, datos_cliente, carrito, servicios_contratados, subtotal, matriz)

    facturas.append(numero_factura)
    nombres.append(datos_cliente[0])
    dnis.append(datos_cliente[2])
    totales.append(subtotal)

matriz_final = []
for i in range(len(facturas)):
    matriz_final.append([facturas[i], nombres[i], dnis[i], totales[i]])

bubble_sort(matriz_final)

print()
print("--- MATRIZ FINAL ORDENADA POR NÚMERO DE FACTURA ---")
factura_final(matriz_final)

total_recaudado, monto_maximo, monto_minimo, promedio, porcentaje_envio, porcentaje_instalacion = calcular_estadisticas(
    totales, contador_envio, contador_instalacion
)

print()
print("--- REPORTES Y ESTADÍSTICAS GENERALES ---")
print("Total recaudado: $", total_recaudado)
print("Máximo monto recaudado: $", monto_maximo)
print("Mínimo monto recaudado: $", monto_minimo)
print("Promedio de recaudación: $", round(promedio, 2))
print("Porcentaje de uso de envío:", round(porcentaje_envio, 2), "%")
print("Porcentaje de uso de instalación:", round(porcentaje_instalacion, 2), "%")

buscar_cliente_lineal(dnis, nombres, facturas, totales)

print("¡Gracias por su compra!")