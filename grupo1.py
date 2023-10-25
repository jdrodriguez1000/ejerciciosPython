# Ejercicio 1 Mostrar la version actual instalada de Python
import sys

print(sys.version)

print(sys.version_info) #Vesion semantica

# Ejercico 2. Exposicion del uso basico de la funcion print()
print() # Imprime una linea sin informacion
print("Este es un ejemplo basico") # la funcion print agrega siemrpe un salto de linea

print()
print("Este es un ejemplo basico.", end="") # Sin salto de linea
print("Este es un ejemplo basico.", end="")


print()
print("Python", "es", "tremendo!") #Impresion de varios textos

print()
print('Python', 'es', 'tremendo!', sep='-') # Impresion de varios textos con separador

print()
print('{} es {}!'.format('Python', 'tremendo')) # Utilizando placeholders

print()
numeros = [2, 4, 5, 6, 7, 7, 8,] 
print(numeros) #Impresion de variables

print()
capitales = {
    'Colombia':'Bogotá',
    'Perú':'Lima'
}
print(capitales)
print()


# Ejercicio 3: Obtener fecha y hora actual del sistema
import datetime

ahora = datetime.datetime.now()
print(ahora)

print()
print(type(ahora)) # Tipo de variable

print()
ahora_formateo = ahora.strftime('%d/%m/%Y %H:%M:%S')
print(ahora_formateo)
