'''
Conjunto de clases para la gestion de excepciones definidas.
'''

class DataLength(Exception):
    '''
    Raise cuando exista error en tamaño de dataframe
    '''
    __classMsg = 'Dataframe con longitud incorrecta'

    def __init__(self):
        self.msg = self.__classMsg

    def __str__(self):
        return (self.msg)

class MonthEmpty(Exception):
    '''
    Raise cuando una de las columnas esta vacia
    '''
    __classMsg = 'El mes de {} no tiene datos.'

    def __init__(self, mes):
        self.msg = self.__classMsg.format(mes)
        super().__init__(self.msg)

class ConvertError(Exception):
    '''
    Raise cuando un valor no se ha podido convertir a valor numerico
    '''
    __classMsg = 'Atención! El valor "{}" del mes de {} ' \
                 'no se ha convertido a valor numerico.'

    def __init__(self, valor, mes):
        self.msg = self.__classMsg.format(valor, mes)
        super().__init__(self.msg)


#
# try:
#     if not 12 == 13:
#         raise DataLength()
#     else:
#         print('Dataframe generado con exito. Sus columnas son correctas')
#
# except DataLength as err:
#     print(err.args)
#     print(err.msg)

# try:
#     raise MonthEmpty('enero')
# except MonthEmpty as e:
#     print(e)