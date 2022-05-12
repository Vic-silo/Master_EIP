'''
    ACTIVIDAD LECCION 2
    Autor: Victor Simo Lozano
    Descripción:
       TAREA 1: Ingresar un numero por pantalla y mostrar todos los numeros desde 0 hasta dicho valor.
       TAREA 2: Crear un diccionario y mostrar mediante un for sus valores.
'''

# TAREA 1
print('TAREA 1: \n'
      'A continuación se pedirà ingresar un numero \nque se desee y se mostrarà todos los numeros\ninferiores a este'
      'desde 0.')

randomNum = int(input('Ingresa un numero: '))
numbers = []
# Almacenamos los valores en una lista "numbers" vacia.
for infNum in range(randomNum):
    numbers.append(infNum)
# Imprimimos ordenadamente todos los valores inferiores
print(f'Todos los numeros inferiores son: {numbers}')

# TAREA 2
print('\nTAREA 2:\n'
      'A continuacion se va a pedir ingresar 5 \nvalores que serán almacenador en un diccionario\npara posteriormente'
      'mostrarlos por pantalla.')

myDictionary = {}
# Mediante un for almacenamos los valores ingresados por el usuario en nuestro diccionario vacio.
print('Ingrese a continuación la serie de valores del diccionario.')
for i in range(5):
    myDictionary[i + 1] = input(f'Inserta el valor {i + 1} :')

# Recorremos todos los Items de nuestro diccionario. Este devuelve el conjunto clave-valor y por ello hay dos indices.
print(f'Los valores del diccionario [{type(myDictionary)}] son:')
for key, value in myDictionary.items():
    print(f'El valor {key} del diccionario contiene: {value}')

input()