# Programe un par de funciones de ordenación de matrices (UNIDIMENSIONALES) de números distintas 
# (burbuja, selección, inserción, mezcla, montículos...). Realice un programa que genere 
# aleatoriamente matrices de números aleatorios y use dicho métodos para comparar el tiempo que 
# tardan en ejecutarse.

import random
n = 50
list = [random.randint(0,100) for i in range(n)]
print("Lista sin ordenar: ")
print(list)
for numPasada in range(len(list)-1,0,-1):
    for i in range(numPasada):
        if list[i]>list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
print("Lista ordenada: ")
print(list)
