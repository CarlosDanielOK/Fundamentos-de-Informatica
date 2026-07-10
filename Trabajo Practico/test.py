def bubble_sort(l1, l2, l3, l4):
    for i in range(len(l1)):
        for j in range(len(l1) - i - 1):
            if l1[j] > l1[j+1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]
                l2[j], l2[j+1] = l2[j+1], l2[j]
                l3[j], l3[j+1] = l3[j+1], l3[j]
                l4[j], l4[j+1] = l4[j+1], l4[j]
    return l1, l2, l3, l4

facturas = [4521, 7890, 3300]
nombres  = ["Juan Perez", "Ana Lopez", "Naruto Uzumaki"]
dnis     = ["12345678", "87654321", "11223344"]
totales  = [70000, 120000, 95000]

facturas, nombres, dnis, totales = bubble_sort(facturas, nombres, dnis, totales)

matriz_final = []
for i in range(len(facturas)):
    matriz_final.append([facturas[i], nombres[i], dnis[i], totales[i]])

print(matriz_final)

for i in range(len(matriz_final)):
    print(matriz_final[i])