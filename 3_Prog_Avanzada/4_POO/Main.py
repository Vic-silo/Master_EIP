'''
    ACTIVIDAD LECCION 4
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Crear una clase calculadora que sume, reste, divida y multiplique dos numeros.
'''

# TAREA
from CalssCalculadora import Calculadora

print('TAREA:\n'
      'A continuación se va a pedir que se\n'
      'ingrese dos valores numéricos\n'
      'de modo que se pueda mostrar los metodos\n'
      'de la clase calculadora.\n')

num1 = float(input('Escribe un valor numérico: '))
num2 = float(input('Escribe un segundo valor numerico: '))

calculadora1 = Calculadora(num1,num2)

print (f'\n1: El  metodo suma da como resultado: {calculadora1.suma()}.\n'
       f'2: El metodo resta da como resultado: {calculadora1.resta()}.\n'
       f'3: El metodo division da como resultado: {calculadora1.division()}.\n'
       f'4: El metodo multiplicacion da como resultado: {calculadora1.multiplicacion()}.')
