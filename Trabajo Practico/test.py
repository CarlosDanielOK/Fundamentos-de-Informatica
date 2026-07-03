# GRUPO N°: 03
# INTEGRANTES:
# - Candela Nuñez
# - Carlos Lazo
# - Lizbeth Alejo

import random
# Precios de servicios
precio_servicios = [7000, 10000] #envio | instalacion
# Precios de los productos
precio_sillas = [30000, 40000, 50000]
precio_mesas = [80000, 90000, 100000]
precio_roperos = [200000, 220000, 250000]

#Nombre de material
nombres_sillas = ["Plástico", "Metal", "Madera"]
nombres_mesas = ["Melamina", "Roble", "Mármol"]
nombres_roperos = ["Melamina", "Plywood", "Roble"]
     
# Contadores y acumuladores del negocio
total_ventas = 0
monto_maximo = 0
monto_minimo = 999999999
votos_envio = 0
votos_instalacion = 0

# Listas principales
facturas = []
nombres = []
dnis = []
totales = []

def validar_nombre():
    nombre = input("Nombre y apellido: ").title()
    print("Tu nombre es", nombre)
    confirmar = input("¿Es correcto? (SI/NO): ").upper()
    while confirmar != "SI":
        nombre = input("Nombre y apellido: ").title()
        print("Tu nombre es", nombre)
        confirmar = input("¿Es correcto? (SI/NO): ").upper()
    return nombre

def validar_edad():
    edad = int(input("Ingrese su edad: "))
    while edad < 18:
        print("Lo sentimos. La edad mínima permitida para realizar compras es de 18 años.")
        edad = int(input("Ingrese su edad: "))
    
    print("Tu edad es", edad)
    confirmar = input("¿Es correcto? (SI/NO): ").upper()
    while confirmar != "SI":
        edad = int(input("Ingrese su edad: "))
        while edad < 18:
            print("Lo sentimos. La edad mínima permitida para realizar compras es de 18 años.")
            edad = int(input("Ingrese su edad: "))
        print("Tu edad es", edad, ". ¿Es correcta? (SI/NO): ")
        confirmar = input("¿Es correcta? (SI/NO): ").upper() 
        
    return edad

def validar_dni():
    dni = input("DNI: ")
    while len(dni) != 8:
        print("ERROR. El DNI debe tener 8 números.")
        dni = input("DNI: ")
    
    print("Tu DNI es:", dni)
    confirmar = input("¿Es correcto? (SI/NO): ").upper()
    while confirmar != "SI":
        dni = input("DNI: ")
        while len(dni) != 8:
            print("ERROR. El DNI debe tener 8 números.")
            dni = input("DNI: ")
        print("Tu DNI es:", dni)
        confirmar = input("¿Es correcto? (SI/NO): ").upper()
    return dni

def generar_factura(existentes):
    repetido = 1
    while repetido == 1:
        num = random.randint(1000, 9999)
        encontrado = 0
        for i in range(len(existentes)):
            if existentes[i] == num:
                encontrado = 1
        if encontrado == 0:
            repetido = 0
    return num

# Validar opciones
def materiales_opciones(minimo, maximo):
    opcion = int(input("Elige una opción (1, 2 o 3): "))
            
    while opcion < minimo or opcion > maximo:
        print("ERROR. Opción inválida.")
        opcion = int(input("Elige una opción (1, 2 o 3): "))
    return opcion

def validar_cantidad():
    cantidad = int(input("¿Cuántos roperos desea?: "))
    while cantidad <= 0:
        print("ERROR. La cantidad debe ser mayor a 0.")
        cantidad = int(input("¿Cuántos roperos desea?: "))
    return cantidad
        
def procesar_compra():
    subtotal = 0
    mas_productos = "SI"
    
    while mas_productos == "SI":
        print("""
--- CATÁLOGO DE PRODUCTOS DISPONIBLES ---
1. SILLAS
2. MESAS
3. ROPEROS
""")     
        opcion = materiales_opciones(1,3)
# SILLAS
        precio = 0
        if opcion == 1:
            print("MATERIALES DE SILLAS:")
            print("1. Plástico = $", precio_sillas[0])
            print("2. Metal = $", precio_sillas[1])
            print("3. Madera = $", precio_sillas[2])
            
            material = materiales_opciones(1,3)

            cantidad = validar_cantidad()
            
            precio = cantidad * precio_sillas[material - 1]       
# MESAS
        elif opcion == 2:
            print("MATERIALES DE MESAS:")
            print("1. Melamina = $", precio_mesas[0])
            print("2. Roble = $", precio_mesas[1])
            print("3. Mármol = $", precio_mesas[2])
            
            material = materiales_opciones(1,3)
            
            cantidad = validar_cantidad()
            
            precio = cantidad * precio_mesas[material - 1] 
# ROPEROS
        elif opcion == 3:
            print("MATERIALES DE ROPEROS:")
            print("1. Melamina = $", precio_roperos[0])
            print("2. Plywood = $", precio_roperos[1])
            print("3. Roble = $", precio_roperos[2])
            
            material = materiales_opciones(1,3)
            
            cantidad = validar_cantidad()    
            
            precio = cantidad * precio_roperos[material - 1] 
        
        subtotal = subtotal + precio
        print("Subtotal acumulado en carrito: $", subtotal)
        
        mas_productos = input("¿Desea agregar otro tipo de producto a esta misma compra? (SI/NO): ").upper()
            
    return subtotal

# PROGRAMA PRINCIPAL

for venta in range(3):
    print("BIENVENIDO A CASA & MUEBLES - VENTA NRO:", venta + 1)
    
    nombre_cliente = validar_nombre()
    edad_cliente = validar_edad()
    dni_cliente = validar_dni()
    
    monto_carrito = procesar_compra()
    
    print()
    print("---PRECIOS DE SERVICIOS---")
    print("Disponemos de servicio de Envío a domicilio por un valor fijo de: $", precio_servicios[0])
    print("Disponemos de servicio de Instalación premium por un valor fijo de: $", precio_servicios[1])
    
    quiere_envio = input("¿Desea contratar el servicio de envío? (SI/NO): ").upper()
    if quiere_envio == "SI":
        monto_carrito = monto_carrito + precio_servicios[0]
        votos_envio = votos_envio + 1

    quiere_instalacion = input("¿Desea contratar el servicio de instalación? (SI/NO): ").upper()
    if quiere_instalacion == "SI":
        monto_carrito = monto_carrito + precio_servicios[1]
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
    nombres.append(nombre_cliente)
    dnis.append(dni_cliente)
    totales.append(monto_final)

matriz = []
for i in range(3):
    fila = [facturas[i], nombres[i], dnis[i], totales[i]]
    matriz.append(fila)

# Burbujeo
for i in range(len(matriz) - 1):
    for j in range(len(matriz) - 1 - i):
        if matriz[j] > matriz[j+1]:
            temporal = matriz[j]
            matriz[j] = matriz[j+1]
            matriz[j+1] = temporal

print()
print("----FACTURA----")
for i in range(len(matriz)):
    print("Factura:", matriz[i][0], " | Cliente:", matriz[i][1], " | DNI:", matriz[i][2], " | Total: $", matriz[i][3])

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
            print("El DNI ingresado no coincide con ninguna de nuestras 3 ventas. Vuelva a intentar.")
    
    buscar_otro = input("\n¿Desea buscar a otro cliente? (SI/NO): ").upper()
print("¡Gracias por su compra!")

if len(facturas) > 0:
    facturas.pop()