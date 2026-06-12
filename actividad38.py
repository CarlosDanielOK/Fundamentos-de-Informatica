def bubble_sort(lista1, lista2):
    for i in range(len(lista1)):
        for j in range(len(lista1) - i - 1):
            if lista1[j] > lista1[j + 1]:
                aux = lista1[j]
                lista1[j] = lista1[j + 1]
                lista1[j + 1] = aux
                aux = lista2[j]
                lista2[j] = lista2[j + 1]
                lista2[j + 1] = aux
    return lista1, lista2


codigo = [3, 4, 2, 5, 1]
equipo = ["tv", "reloj", "tostadora", "heladera", "monitor"]

print(bubble_sort(codigo, equipo))
