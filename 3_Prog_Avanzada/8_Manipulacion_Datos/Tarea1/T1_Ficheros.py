'''
    Trabajo con ficheros
'''

class Ficheros:

    def __Presentation(self):
        '''
        Funcion que sirve de presentacion
        :return:
        '''

        return print('\nTAREA 1:\n'
              'Trabajar con ficheros de modo que\n'
              'se cree un archivo, se escriba en este\n'
              'y por ultimo lo mostremos por pantalla.\n')

    def __init__(self):
        '''
        Creacion del fichero que se desea
        :param name: Nombre del archivo con extension
        :return:
        '''
        self.__Presentation()

        path = 'Tarea1/'
        fName = input('Indique el nombre del archivo: ')
        fName = path + fName

        self.file = fName

        # Creacion del fichero si este no existe
        try:
            f = open(fName,'x')
            print(f'\nFichero {fName} creado con éxito.')
        except Exception as e:
            print('Ya existe el fichero: ', e)


    def WriteFile(self, message, tipo = 'a'):
        '''
        Escritura en el fichero
        :param message: Mensaje deseado
        :param tipo: Formato de escritura. Por defecto 'a'
        :return:
        '''

        # Escritura del archivo en el metodo escogido
        with open(self.file,tipo) as f:
            f.write(message)

        return print('\nMensaje escrito con éxito.')

    def PrintFile(self):
        '''
        Mostrar fichero por pantalla
        :return:
        '''

        # Mostrar fichero
        with open(self.file, 'r') as f:
            return print(f.read())

