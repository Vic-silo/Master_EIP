'''
    ACTIVIDAD LECCION 5
    Autor: Victor Simo Lozano
    Descripción:
       TAREAs: Trabajar con listas y diccionarios.
       TAREA_1: Con una lista almacenar numeros del 1 al 10 y mostrarla en orden inverso
       TAREA_2: Crear un diccionario de 4 valores. Mostrarlos. Modificar el tercer valor. Añadir un valor tipo lista.
'''

# TAREA 1
print('\nTAREA 1:\n'
      'A continuación se va a mostrar\n'
      'una lista con los valores del 1 al 10\n'
      'en orden inverso.')

miLista = []
i = 1
while i <= 10:
    miLista.append(i)
    i += 1

miLista.sort(reverse=True)

print(miLista)

# TAREA 2
print('\nTAREA 2:\n'
      'A continuación se va a mostrar\n'
      'un diccionario de 4 valores con una\n'
      'serie de modificaciones posteriores.')

miDiccionario = dict(
    nombre='Victor',
    edad=27,
    nacionalidad='Española',
    sexo='Masculino'
)

# Mostrar diccionario
print(f'\nEl diccionario: {type(miDiccionario)}\n'
      f'{miDiccionario}')

# Modificar el tercer valor
print(f'\nTras modificar el tercer valor vea las diferencias:\n'
      f'{miDiccionario}')
miDiccionario[list(miDiccionario)[2]] = 'Americana'
print(f'{miDiccionario}')

# Añadir un valor tipo lista
miDiccionario['estudios'] = ['Grado Ing. Elecrtrica','Master Automatizacion Industrial',
                             'Master programacion Avanzada Python']
print(f'\nTras añadir un nuevo valor tipo lista:{list(miDiccionario.keys())[4]} {type(miDiccionario["estudios"])}\n'
      f'{miDiccionario}')

input()