def bubble_sort(lista1, lista2, lista3):
    for i in range(len(lista1)):
        for j in range(len(lista1) - i - 1):
            if lista3[j] > lista3[j + 1]:
                lista1[j], lista1[j + 1] = lista1[j + 1], lista1[j]
                lista2[j], lista2[j + 1] = lista2[j + 1], lista2[j]
                lista3[j], lista3[j + 1] = lista3[j + 1], lista3[j]

    return lista1, lista2, lista3


matricula = [34403, 34417, 34423]
alumno = ["Perez", "Lopez", "Silva"]
nota = [8, 6, 10]

matricula, alumno, nota = bubble_sort(matricula, alumno, nota)
print(matricula)
print(alumno)
print(nota)
