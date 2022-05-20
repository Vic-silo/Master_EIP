'''
    ACTIVIDAD LECCION 8
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Trabajar con ficheros & Pandas.
        1-  Abrir fichero '.txt'
            Escribir en el fichero
            Mostrar el contenido por pantalla
        2-  Cargar fichero '.csv'
            Crear Dataframe con Pandas
            Mostrar el máximo y media de cada columna

'''

# TAREA 1:
from Tarea1.T1_Ficheros import Ficheros

# 1º:  Creacion del fichero
f = Ficheros()

# 2º: Escritura en el fichero
def CreateMessage():
    print('\nA continuación, escriba su mensaje.\n'
          'Instrucciones: - Puede usar saltos de linea si lo prefiere.\n'
          '               - Una vez haya terminado, escriba fin para asi hacerlo saber.\n'
          'Escriba aqui su mensaje: ')

    cmdInput = ''
    message = ''
    while cmdInput.upper() != 'FIN':
        cmdInput = input()
        if cmdInput.upper() != 'FIN':
            message  += cmdInput + '\n'

    return message

f.WriteFile(CreateMessage())

# 3º Imprimir por pantalla el fichero.
f.PrintFile()

# TAREA 2
from Tarea2.T2_Pandas import DataFrame

try:
    df = DataFrame()

except Exception as e:
    print('Class was not created: ', e)
    exit()

try:
    df.GetDataframe()
    print('\n')
    df.GetMinimum()
    print('\n')
    df.GetMaximun()
    print('\n')
    df.GetAverage()

except Exception as e:
    print('Something went wrong: ', e)