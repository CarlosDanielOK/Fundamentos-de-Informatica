total = 0
consultas = 0
basica = 0
vacunacion = 0
operacion = 0

for i in range(7):
    cantidad = int(input("Cuantos perros trato hoy?: "))
    while cantidad < 0:
        print("ERROR")
        cantidad = int(input("Cuantos perros trato hoy?: "))
    
    consultas = consultas + cantidad

    for j in range(cantidad):
        tipo = input("La consulta fue BASICA, VACUNACION O OPERACION?: ").upper()
        while tipo != "BASICA" and tipo != "VACUNACION" and tipo != "OPERACION":
            tipo = input("La consulta fue BASICA, VACUNACION O OPERACION?: ").upper()

        if tipo == "BASICA":
            basica = basica + 1
            total = total + 27000
        elif tipo == "VACUNACION":
            vacunacion = vacunacion + 1
            total = total + 33500
        elif tipo == "OPERACION":
            operacion = operacion + 1
            total = total + 50000
        else:
            print("Algo salio mal, no deberia llegar aca.")
        
print("TOTAL RECAUDADO EN LA SEMANA: $", total)
print("Porcentaje de basicas: ", basica * 100 / consultas)
print("Porcentaje de vacunaciones: ", vacunacion * 100 / consultas)
print("Porcentaje de operaciones: ", operacion * 100 / consultas)