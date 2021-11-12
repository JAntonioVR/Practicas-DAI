# Cree un programa que lea de un fichero de texto un número entero n y escriba en otro fichero 
# de texto el n-ésimo número de la sucesión de Fibonacci.

f = open("numero.txt", "r")
number = int(f.read())
f.close()

def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

res = fibonacci(number)
f = open("salida.txt", "w")
f.write(str(res))
f.close()
