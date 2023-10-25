#Ejercicio 13 Crear una cadena de caracteres multilinea


cadena = "afdadf adfadfa asfasdf sdfa sdf asfad asdfasdfa asdfadfadf asdfasf asfasfasdfa asdfasf sdfsd sdfadsfasdf asdfasdfassfasdfasdf asdfasfadfa asdf asdf asdf sdfadfasdfasfasdfasdf asfadfafasdfasdf" #Se logro presionando ALT + z

cadena1 = """adasfsdf dsf asdfasdfasf asdfasdfafafdads fadfasdfasdfasdf
sfsdfasdfasdfasd
fasfasdfasfasdfadsfdsfsdfa
sadfsdf asdgdfagdfg dfsdfhdfsgdsf
sgsdfgsdfgdsfgdfsg
""" # SE utiliza la comilla triple para un docstring

print(cadena)
print()
print(cadena1)
print()

#Ejercicio 14: Calcular la diferencia entre dos fechas
from datetime import date

fecha1 = date(2023,10,1)
fecha2 = date(2022,9,30)

delta_fechas = fecha1 - fecha2
print(delta_fechas)
print(delta_fechas.days)

#Ejercicio 15 Calcular el volumen de una esfera a partir de un radio dado
from math import pi

radio=int(input('Ingrese el radio de la esfera: '))
volumen = 4/3 *pi *radio**3
print('El volumen es: {}'.format(volumen))