#Ejercicio 7 Obtener la extension de un archivo ingresado por el usuario
nombre_archivo = input('Ingrese el nombre del archivo con la extension: ')

separacion_archivo = nombre_archivo.split('.')
extension_archivo = separacion_archivo[-1]
print('La extension es:',format(extension_archivo))