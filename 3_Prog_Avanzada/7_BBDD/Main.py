'''
    ACTIVIDAD LECCION 7
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Crear BBDD y  modificarla.
        Crear una BBDD Sqlite3.
        Crear una funcion que genere una tabla de 4 y 2 campos
        Crear una funcion para cada una de las siguientes sentencias:
            Insertar
            Actualizar
            Listar
            Borrar
'''
import sqlite3 as sql
from claseTablas import myDB

# TAREA
print('\nTAREA:\n'
      'A continuación se va a mostrar el resultado de\n'
      'la llamada a una serie de metodos dentro del\n'
      'paquete al que se llama en este modulo.\n')

# 1º: Crear base de datos
con = myDB('actividad7.db')
print(f'TAREA 1:\nConexión con la base de datos "{con}" creada con exito.')

# 2º: Funcion para generar tabla de 2 y 4 campos
tabla1 = myDB('actividad7.db')
tabla2 = myDB('actividad7.db')

print('\nTAREA 2:')
try:
    tabla1.CrearTabla2Campos('Tabla_Corta')
    tabla2.CrearTabla4Campos('Tabla_Larga')
    print('Tablas de 2 y 4 campos creadas con éxito.')
except Exception as e:
    print('Error al crear las tablas -> ', e)

# 3º: Operar sobre las tablas creadas
print('\nTAREA 3:')
def DoTransaccion(tabla,opcion,shortcut):
    if opcion == '1':
        print('\nINSERTAR DATOS')
        tabla.InsertarDatos(shortcut)
    if opcion == '2':
        print('\nACTUALIZAR DATOS')
        tabla.ActualizarDatos(shortcut)
    if opcion == '3':
        print('\nLISTAR DATOS')
        tabla.ListarDatos(shortcut)
    if opcion == '4':
        print('\nBORRAR DATOS')
        tabla.EliminarRegistros(shortcut)


# Ejecucion de bucle opciones a trabajar
opcion = ''
while opcion != '0':
    # Tabla con la que se desea operar
    opcion = input('Indique la transacción:\n'
                   '1: Insertar datos.\n'
                   '2: Actualizar datos.\n'
                   '3: Listar datos.\n'
                   '4: Borrar datos.\n'
                   '0: Salir\n'
                   '\nOpcion: ')
    if opcion == '0':
        exit()

    tabla = input('Indique tabla para operar (C o L): ')

    if not ((tabla.upper() == 'C') or (tabla.upper() == 'L')):
        print('Error al seleccionar tabla.')

    elif tabla.upper() == 'C':

        DoTransaccion(tabla1, opcion, tabla.upper())

        # tabla1.InsertarDatos(tabla.upper())

    elif tabla.upper() == 'L':

        DoTransaccion(tabla2, opcion, tabla.upper())

        # tabla2.InsertarDatos(tabla.upper())

