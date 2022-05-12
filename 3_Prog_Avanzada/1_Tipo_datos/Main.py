'''
    ACTIVIDAD LECCION 1
    Autor: Victor Simo Lozano
    Descripción: Programa de Python que pida por pantalla 2 cadenas de texto y las muestre por pantalla de forma
        concatenada así como su longitud.
'''

string1 = input ("Ingresa la primera palabra: ")
string2 = input('Ingresa la segunda palabra: ')
concatenadas = string1 + " " + string2

print (f'Se ha escrito: {concatenadas}.\n'
       f'Tiene una longitud de {len(concatenadas)} caracteres.')
