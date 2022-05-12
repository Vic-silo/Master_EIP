'''
    ACTIVIDAD LECCION 3
    Autor: Victor Simo Lozano
    Descripción:
       TAREA 1: Crear una funcion que tome dos valores y devuelva su suma y resta. Emplear excepciones.
       TAREA 2: Crear una funcion cuyo segundo parámetro sea uno predeterminado.
'''

# TAREA 1
print('TAREA 1:\n'
      'A continuación se va a pedir que se\n'
      'ingrese dos valores numéricos\n'
      'de modo que se pueda mostrar su suma\n'
      'y resta.\n')


# Creamos funcion que recibe dos valores numericos.
def Operation(num1, num2):
    add = num1 + num2
    minus = num1 - num2
    # Generamos variables de resultado para facilidad de entendimiento de resultado.
    printAdd = (f'La suma es: {add}')
    printMinus = (f'La resta es: {minus}')

    return (printAdd, printMinus)


# Creamos función que nos asigne a variable dos numeros que queremos que sea enteros.
def UserParametres():
    int1 = int(input('Dime un numero: '))
    int2 = int(input('Dime otro numero: '))

    return print(Operation(int1, int2))


# Manejo de excepciones.
# Ejecución del codigo. si no ha habido fallo, slaimos del manejo de excepciones.
try:
    UserParametres()
# Si obtenemos un error de tipo de dato en el input. Avisamos de que queremos y reejecutamos userParameters.
except ValueError:
    print('\nERROR: Ingrese numeros enteros.')
    UserParametres()

input()
# -*-*-*-*-*-*-*-*
# TAREA 2
#

print('\nTAREA 2:\n'
      'A continnuación se le va a pedir\n'
      'ingresar una serie de respuestas.\n')

def RandomFunction (numero, charmy=None):
    print(f'\nBonito numero el {numero}')

    if charmy != None:
        print('Hasta luego educado desconocido!')
    else:
        print('Vaya mal educado...')


usernumber = input('Dime un numero: ')
userCharmy = input('¿Ayudarias a un anciano a cruzar la calle? (Si/No): ')

if 'SI' == userCharmy.upper():
    RandomFunction(usernumber,'usuario educado')
else:
    RandomFunction(usernumber)

