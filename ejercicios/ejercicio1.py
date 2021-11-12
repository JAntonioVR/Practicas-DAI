# Programe un mini-juego de "adivinar" un número (entre 1 y 100) que el ordenador establezca 
# al azar. El usuario puede ir introduciendo números y el ordenador le responderá con 
# mensajes del estilo "El número buscado el mayor / menor". El programa debe finalizar cuando 
# el usuario adivine el número (con su correspondiente mensaje de felicitación) o bien cuando 
# el usuario haya realizado 10 intentos incorrectos de adivinación.

import random as random

number = random.randint(0, 100)
print(number)
found = False
currentNumber = -1
nIntentos = 10
while(not found and nIntentos > 0):
    currentNumber = input("Introduce un numero: ")
    currentNumber = int(currentNumber)
    nIntentos-=1
    if(currentNumber == number):
        found = True
    elif(currentNumber < number):
        print("El número es mayor")
    else:
        print("El número es menor")

if(nIntentos > 0):
    print("Eres un grande")
else:
    print("Se acabaron los intentos, F")

