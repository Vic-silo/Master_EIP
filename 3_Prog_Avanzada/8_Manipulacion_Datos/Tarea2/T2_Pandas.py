'''
    Trabajo con Dataframes
'''

import pandas as pd

class DataFrame:

    def __init__(self):
        self.__Presentation()
        name = input('Indique el nombre y ruta de su archivo si no esta en la raiz: \n'
                     'Ej: cotizacion_actualizado.csv\n'
                     '-> ')
        sep = input('Indique los separadores del archivo: ')
        index = input('Indique algun indice en su Dataframe. (Nombre la columna): ')

        self.__ImportFile_csv(name,sep,index)

    def GetMinimum(self):
        '''

        :return:
        '''

        print('\nEl minimo para cada una de las columnas del Dataframe es: \n')
        print(self.df.apply(self.__Minimum, axis=0))

    def GetMaximun(self):
        '''

        :return:
        '''

        print('\nEl maximo para cada una de las columnas del Dataframe es: \n')
        print(self.df.apply(self.__Maximun, axis= 0))

    def GetDataframe(self):
        '''

        :return:
        '''

        print('\nEl Dataframe es: \n')
        print(self.df)

    def GetAverage(self):
        '''

        :return:
        '''

        '''
        Old code
        '''
        '''
        # self.df['Final'] = self.df['Final'].str.replace(',', '.').astype(float)
        # pd.to_numeric(self.df['Final'], downcast="float")
        # print(self.df['Final'].mean())
        '''

        print('\nEl valor medio para cada una de las columnas del Dataframe es: \n')
        print (round(self.df.mean(axis = 0)))


    def __Presentation(self):
        '''
        Funcion que sirve de presentacion
        :return:
        '''

        return print('\nTAREA 2:\n'
                     'Trabajar con Pandas y Dataframes.\n'
                     'Tras importar un archivo .csv, se\n'
                     'realizará una serie de procesamientos\n'
                     'con el mismo.')

    def __ImportFile_csv (self, name, sep, index=None):
        '''
        Importar archivos csv a pandas
        :param name: Nombre del archivo deseado
        :param sep: Separador que tiene el archivo. Por defecto ','
        :param index: Por defecto vacio. Si se especifica indice será el indice del dataframe
        :return:
        '''

        filePath = 'Tarea2/' + name

        try:
            if index != None:
                # self.df = pd.read_csv(name, sep = sep).set_index(index)
                self.df = round(pd.read_csv(filePath, delimiter = sep, thousands = '.', decimal=',').set_index(index),2)

            else:
                self.df = pd.read_csv(filePath, delimiter=';', thousands='.', decimal=',')

            print ('Archivo .csv importado con èxito')
        except Exception as e:
            print(e)

        return self.df

    def __Minimum(self, x):
        '''

        :return:
        '''

        return min(x)

    def __Maximun(self, x):
        '''

        :param x:
        :return:
        '''

        return max(x)
