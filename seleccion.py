def seleccion(lista):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista


numeros = [3, 1, 5, 4, 2]
print(seleccion(numeros))
