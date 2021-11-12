import re
from typing import Pattern

str = input ("Introduce una cadena: ")
# Palabra + letra mayúscula
#patron = "\w+\s[A-Z]\s"

# Correo electrónico
#patron = "\w+@(hotmail|gmail|ugr|outlook)\.(com|es)"

# Número de cuenta
patron = "[0-9]{4}(-|\s)[0-9]{4}(-|\s)[0-9]{4}(-|\s)[0-9]{4}"
result = re.match(patron, str)


if(result != None):
    print("Ha colado")
else:
    print("No ha colado :(")