# La Criba de Eratóstenes es un sencillo algoritmo que permite encontrar todos los números 
# primos menores de un número natural dado. Prográmelo.
import math
n = 18
list = [i for i in range(2, n)]
for i in range(2, int(math.sqrt(n))):
    for j in range(int(n/i)):
        if(i*j in list):
            list.remove(i*j)
print(list)