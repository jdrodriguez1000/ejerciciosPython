# Ejercicio 22 Crear una subcadena de n caracteres replicada n cantidad de veces
def replicarSubcadena(cadena, n):
    numCaracteres = n
    if numCaracteres > len(cadena):
        numCaracteres = len(cadena)
    suCadena = cadena[:numCaracteres]
    resultado = ""
    for i in range(n):
        resultado += suCadena
    return resultado

print(replicarSubcadena('Python', 2))
print(replicarSubcadena('Python', 10))
print(replicarSubcadena('Python', 0))


# Ejercicio 23 Comprobar si un caracter especifico es una vocal
def comprobarVocal(c):
    """
    Comprueba si un caracter es un vocal
    """
    lista_vocales = ['a', 'e', 'i', 'o', 'u']
    c = c.lower() 
    
    return c in lista_vocales
   
print(comprobarVocal('a'))
print(comprobarVocal('ae'))
print(comprobarVocal('A'))
print(comprobarVocal('b'))
print()


#Ejercicio 24 Simular el funcionmiento del operador in
print(5 in [1,2,3,4,5,6])
print('k' in 'fork')
print('i' in 'fork')
print()

def emularOperadorIn(lista, elemento):
    for e in lista:
        if elemento == e:
            return True
    return False

print(emularOperadorIn([1,2,3,4,5,6], 5))
print(emularOperadorIn('fork', 'k'))
print(emularOperadorIn('fork', 'i'))


# Ejercicio 25 Crear un histograma a partir de uan lista de enteros
def crearHistograma(lista, caracter='*'):
    for e in lista:
        print(caracter*e)
      
lista1 =[2,3,7,8,4,1]  
crearHistograma(lista1, '*')