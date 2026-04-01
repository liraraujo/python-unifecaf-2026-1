# Desenvolva um algoritmo capaz de ordenar uma lista de inteiros, sem utilizar .sort() ou sorted()

lista = [5, 4, 3, 2, 6, 7, 8]

for i, l1 in enumerate(lista):
    for j, l2 in enumerate(lista):
        if (i > j and l1 > l2):
            lista 