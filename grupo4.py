# Ejercicio 8 Obtener el primer y ultimo numero de una lista

lista_lenguajes = ['Python', 'C++', 'Java', 'PHP']

primer_elemento = lista_lenguajes[0]
ultimo_elemento = lista_lenguajes[-1]

print(primer_elemento)
print(ultimo_elemento)

#Ejercicio 9 Mostrar la fecha de un evento almacenada en una tupla
fecha_evento = (2023, 9, 14)
print()
print(type(fecha_evento))
print(fecha_evento)

print()
print('El evento sera para la fecha: ', fecha_evento)

print()
print('El evento sera para la fecha: %i/%i/%i' % fecha_evento)

print()
ano, mes, dia = fecha_evento
print('El evento sera para la fecha: {}/{}/{}'.format(ano, mes, dia))

#Ejercicio 10 Solicitar al usuario un numero n y calcular n+nn+nnn
n=input('Ingrese el numero n: ')

nn = int('{}{}'.format(n,n))
nnn = int('{}{}{}'.format(n,n,n))
n = int(n)

suma = n + nn + nnn
print()
print(suma)