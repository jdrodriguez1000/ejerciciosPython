#Ejercicio 11 obtener la documentacion de funciones incorporadas

from math import sin
from datetime import datetime

print(abs.__doc__)

print()

print(int.__doc__)

print()

print(sin.__doc__)

print()
print(datetime.now.__doc__)

#Ejercicio 12 Imprimir el calendario para un año y mes especifico
import calendar 
anno = int(input('Ingrese el año:  '))
mes = int(input('Ingrese el mes:  '))

print(calendar.month(anno, mes))

