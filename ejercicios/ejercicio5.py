# Cree un programa que:
#       Genere aleatoriamente una cadena de [ y ].
#       Compruebe mediante una función si dicha secuencia está balanceada, es decir, que se 
#       componga de parejas de corchetes de apertura y cierre correctamente anidados.
import random
str = ""
nparentesis = 0
balanceada = False
cerradoSinAbrir = False
for i in range(6):
    if(random.randint(0,2)):
        car = "["
        nparentesis += 1
    else:
        car = "]"
        nparentesis -= 1
    str += car
    if(nparentesis < 0):
        balanceada = False
        cerradoSinAbrir = True
    elif (nparentesis == 0):
        balanceada = True
    else:
        balanceada = False

print(str)
if(balanceada and not cerradoSinAbrir):
    print("La expresion está balanceada")
else:
    print("La expresion no está balanceada")
    

