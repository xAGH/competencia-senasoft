from string import printable
from random import choice

cadena = ""
print(printable)

for i in range(120):
    cadena += choice(printable).replace('"', "-").replace("'", "-").replace("\n", "_").replace(" ", "_").replace("\t", "_").replace("\\", "_")

print(cadena)