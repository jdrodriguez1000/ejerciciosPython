#Ejercicio 5 imprimir una caden de caracteres de forma inversa
cadena = 'Python'

for i in range(len(cadena)-1, -1, -1):
    print(cadena[i], end='')
    
print()
print(cadena[::-1]) #Es mejor esta forma para obtener la cadena de forma inversa

#Ejercicio 6 Obtener un conjunto de numeros separados por coma y crer una lista
entrada = input('Escriba varios numeros separados por coma: ')
print()
print(entrada)
print(type(entrada))
numeros = entrada.split(',')
print(numeros)
print(type(numeros))
