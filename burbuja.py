def burbujeo(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j + 1]
                lista[j + 1] = lista[j]
                lista[j] = aux
    return lista


numeros = [3, 1, 5, 4, 2]

print(burbujeo(numeros))
