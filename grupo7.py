#Ejercio 16 Crear una funcion para evaluar un numero y realizar una operacion

def diferencia(n):
    """ 
    Calcula la diferencia con el valor pasado en el argunento
    se debe seguir dos reglas
    """
    if n<=15:
        return 15 - n
    else:
        return (15 - n) * 2
    
print(diferencia(17))
print(diferencia(3))
print()

#Ejercicio 17 Crar una funcion para determinar si un numero es cercano a 1000 o a 2000
def cercania(n):
    return(abs(1000 - n ) < 100 or abs(2000 - n ) < 100)

print(cercania(1050))
print(cercania(980))
print(cercania(820))
print(cercania(1280))
print()

print(cercania(2050))
print(cercania(1980))
print(cercania(1820))
print(cercania(2280))

#Ejercicio 19 Calculr la sum de tres numeros e incluir una condicion de igualdad
def sumaNumeros(a, b, c):
    """
    Calcula la suma de tres numeros, si los numeros son iguales la suma se multiplica por 3
    """
    suma = a + b + c
    if a==b and b == c:
        suma = suma * 3
    return suma

print(sumaNumeros(2,3,7))
print(sumaNumeros(3,3,3))

#Ejercicio 19. Comprobar si una cadena termina con la extension .py, si no es asi agregarla

def validarNombreArchivo(nombre_archivo):
    """
    Valida si un nombre de archivo tiene la extension .py, si el archivo no la tiene la agrega 
    """
    if len(nombre_archivo)>=3 and nombre_archivo[-3:]=='.py':
        return nombre_archivo
    else:
        return nombre_archivo+'.py'

print(validarNombreArchivo('main.py'))
print(validarNombreArchivo('modulo'))

# Ejercicio 20 Emular el funcionamiento del producto de cadenas.
def productoCadena(cadena, veces):
    """
    Emula el funcionamiento del producto de cademans
    """
    resultado = ""
    for i in range(veces):
        resultado += cadena
    return resultado
    
print(productoCadena('Python', 3))


#Ejercicio 21 Generar los n primeros numeros pares positivos
def generarNumerosPares(n=100):
    """
    Genera los n primeros numeros pares positivos
    """
    pares = []
    contador = 0
    numero = 0
    while(contador<n):
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1
        numero += 1
    return pares

numerosSolicitados = input('Ingrese la cantidad de numeros pares que quiere generar: ')
numerosSolicitados = int(numerosSolicitados)
if numerosSolicitados>0:
    pares = generarNumerosPares(numerosSolicitados)
    print(pares)
    print('La cantidad de pares es: ', len(pares))     
else:
    print('El numero debe ser positivo')

