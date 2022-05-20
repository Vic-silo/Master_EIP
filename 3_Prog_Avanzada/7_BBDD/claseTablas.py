'''
    Clase con las funciones recurrentes para base de datos
'''
import sqlite3


class myDB:

    def __GetTable(self,tablaShortcut):
        '''
        Metodo privado para seleccionar tabla de trabajo
        :param tablaShortcut: Indice de la tabla segun input usuario
        :return: Conexion con la tabla
        '''
        if tablaShortcut == 'C':
            return self.tableC
        elif tablaShortcut == 'L':
            return self.tableL

    def __GetHeaders(self, tablaShortcut):
        '''
        Metodo privado imprimir headers
        :param tabla: Conexion con la tabla
        :return: Impresion de las cabeceras
        '''
        targetTable = self.__GetTable(tablaShortcut)
        headers = []

        # Sentencia
        data = self.cursor.execute('''SELECT * FROM {}'''.format(targetTable))

        # Imprimir los headers
        for header in data.description:
            headers.append(header[0])

        return print(headers)

    def __GetColumn(self, columnaAdress, tablaShortcut):
        '''
        Metodo privado imprimir columna
        :param tabla: Conexion de la tabla
        :return: Impresion de columna
        '''
        targetTable = self.__GetTable(tablaShortcut)

        data = self.cursor.execute('''SELECT {} FROM {}'''.format(columnaAdress,targetTable))

        print(data.fetchall())




    # 1º: Crear base de datos
    def __init__(self, conectionName):
        self.con = sqlite3.connect(conectionName)
        self.cursor = self.con.cursor()
        self.tableC = ''
        self.tableL = ''

    # 2º: Funcion para generar tabla de 2 y 4 campos
    def CrearTabla2Campos(self, tableName):
        self.cursor.execute("begin")
        self.tableC = tableName
        try:
            self.cursor.execute('''create table if not exists {} (
                                   id integer primary key, 
                                   nombre varchar(50)
                                   )'''.format(tableName))
            self.con.commit()
            # print('     Tabla de 2 campos creada con exito.')
        except Exception as e:
            print('Error Tabla 4 campos -> ', e)
            self.cursor.execute("rollback")

    def CrearTabla4Campos(self, tableName):
        self.cursor.execute("begin")
        self.tableL = tableName
        try:
            self.cursor.execute('''create table if not exists {} (
                                   id integer primary key, 
                                   nombre varchar(50),
                                   apellido varchar(50),
                                   sexo varchar(6)
                                   )'''.format(tableName))
            self.con.commit()
            # print('     Tabla de 2 campos creada con exito.')
        except Exception as e:
            print('Error Tabla 4 campos -> ', e)
            self.cursor.execute("rollback")

    # 3º: Funciones para operar con las tablas
    def InsertarDatos(self, tabla):
        # Consulta que se desea hacer:
        queryInsert2 = '''INSERT INTO {} VALUES  (?,?)'''
        queryInsert4 = '''INSERT INTO {} VALUES  (?,?,?,?)'''
        querySelect = '''SELECT * FROM {}'''

        # Funcion para indicar al usuario que datos ha de introducir
        def PrintColumns(data):
            for column in data.description:
                print(f'->  {column[0]}')

            print('Introduzca de forma ordenada los datos deseados: ')

        # Funcion para tomar los datos ingresados por el usuario
        def TomaDatos(n):
            i = 1
            datos = []
            while i <= n:
                datos.append(input(f'Dato {i}: '))
                i += 1
            return datos

        targetTable = self.__GetTable(tabla)
        self.cursor.execute('begin')
        try:
            # Obtener datos de la tabla e imprimir por pantalla sus nombre de columna
            data = self.cursor.execute(querySelect.format(targetTable))
            PrintColumns(data)
            # Obtener los datos a ingresar por el usuario
            if tabla == 'C':
                datosInsertar = TomaDatos(2)
                query = queryInsert2
            else:
                datosInsertar = TomaDatos(4)
                query = queryInsert4

            # Ejecutar la consulta para insertar
            self.cursor.execute(query.format(targetTable), (datosInsertar))

            '''
            Old code
            '''
            '''
            if tabla == 'C':
                # Obtener datos de la tabla e imprimir por pantalla sus nombre de columna
                data = self.cursor.execute(querySelect.format(self.tableC))
                PrintColumns(data)
                # Obtener los datos a ingresar por el usuario
                datosInsertar = TomaDatos(2)
                # Ejecutar la consulta para insertar
                # self.cursor.execute(queryInsert2.format(self.tableC), (datosInsertar[0], datosInsertar[1]))
                self.cursor.execute(queryInsert2.format(self.tableC), (datosInsertar))

            elif tabla == 'L':
                # Obtener datos de la tabla e imprimir por pantalla sus nombre de columna
                data = self.cursor.execute(querySelect.format(self.tableL))
                PrintColumns(data)
                # Obtener los datos a ingresar por el usuario
                datosInsertar = TomaDatos(4)
                # Ejecutar la consulta para insertar
                # self.cursor.execute(queryInsert4.format(self.tableL),
                #                     (datosInsertar[0], datosInsertar[1], datosInsertar[2], datosInsertar[3]))
                self.cursor.execute(queryInsert4.format(self.tableL), (datosInsertar))
            '''

            # Aplicar transacciones
            self.con.commit()
            print('Datos insertados correctamente.\n')

        except Exception as e:
            print('Error al insertar valores en la tabla -> ', e)
            self.cursor.execute('roll3back')

    def ActualizarDatos(self, tabla):
        # Consulta que se desea hacer:
        queryUpdate = '''UPDATE {} SET {} = ? WHERE id = ?'''

        # Obtener columna e Id a actualizar
        def UpdateParams():

            parametros = []
            # Campo
            parametros.append(input('Indique el campo a actualizar: '))
            parametros.append(input('Indique el nuevo valor: '))
            # Id
            parametros.append(input('Indique el ID sobre el que actualizar: '))

            return parametros

        def UpdateTable(tabla, parametros):
            # Sentencia
            self.cursor.execute(queryUpdate.format(tabla, parametros[0]), (parametros[1], parametros[2]))

        targetTable = self.__GetTable(tabla)
        self.__GetHeaders(tabla)
        parametros = UpdateParams()

        self.cursor.execute('begin')
        try:
            # Actualizar datos
            UpdateTable(targetTable, parametros)

            '''
            Old code
            '''
            '''
            if tabla == 'C':
                # Actualizar datos
                # self.cursor.execute('UPDATE ' + self.tableC + ' SET ' + parametros[0] + ' = ? WHERE ID = ?',
                #                     (parametros[1],parametros[2]))
                UpdateTable(self.tableC, parametros)

            elif tabla == 'L':
                # Actualizar datos
                # self.cursor.execute(queryUpdate.format(self.tableL),(parametros))
                UpdateTable(self.tableL, parametros)
            '''

            # Aplicar transacciones
            self.con.commit()
            print('Datos actualizados correctamente.\n')

        except Exception as e:
            print('Error al actualizar valores en la tabla -> ', e)
            self.cursor.execute('rollback')

    def ListarDatos(self, tabla):
        # Consulta que se desea hacer
        queryShow = '''SELECT * FROM {}'''

        # Referenciar a tabla deseada
        targetTable = self.__GetTable(tabla)

        try:
            # Sentencia
            self.cursor.execute(queryShow.format(targetTable))
            # Leer datos de la base de datos
            registros = self.cursor.fetchall()

            # Imprimir los registros
            self.__GetHeaders(tabla)
            for registro in registros:
                print(registro)

            '''
            Old code
            '''
            '''
            # Referenciar a tabla deseada
            if tabla == 'C':
                tabla = self.tableC
            else:
                tabla = self.tableL
        
                try:
                    headers = []
                    # Sentencia
                    data = self.cursor.execute(queryShow.format(tabla))
                    # Leer datos de la base de datos
                    registros = self.cursor.fetchall()
                    # Imprimir los registros
                    for header in data.description:
                        headers.append(header[0])
                    print(headers)
                    for registro in registros:
                        print(registro)
            '''

            print('\n')

        except Exception as e:
            print('Error al listar los datos -> ', e)

    def EliminarRegistros(self,tabla):
        # Consulta que se desea hacer
        queryDelete = '''DELETE FROM {} WHERE id = {}'''

        targetTable = self.__GetTable(tabla)
        self.cursor.execute('begin')
        try:
            self.__GetColumn('id',tabla)
            targetId = input('Indique el registro a eliminar: ')

            self.cursor.execute(queryDelete.format(targetTable, targetId))
            # self.cursor.execute('''DELETE FROM Tabla_larga WHERE id = 20''')
            self.con.commit()

            print('Registro eliminado.\n')
        except Exception as e:
            print('Error al eliminar registro -> ', e)
