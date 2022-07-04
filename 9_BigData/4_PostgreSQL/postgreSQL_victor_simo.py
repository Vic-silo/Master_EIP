from psycopg2 import sql, connect, Error


def connection(data_base):
    """
    :param data_base: Data base name
    :return: Conection to database
    """

    # Connect to existing database
    conn = connect(database=data_base,
                   user='admin', password='admin',
                   host='localhost', port=5432)
    return conn


def insert(cursor):
    """
    Inserts in tables from data base de initial data
    :param cursor: Cursor from database
    """
    # SQL instruction
    SQL_NOTAS = 'SELECT count(*) FROM notas;'
    SQL_EDIC = 'SELECT count(*) FROM edicion;'
    SQL_INSERT_NOTAS = 'INSERT INTO {}({}, {}, {}, {}) VALUES (%s, %s, %s, %s);'
    SQL_INSERT_EDIC = 'INSERT INTO {}({}) VALUES (%s);'

    # Table values
    NOTAS_VALUES = dict(
        id_1=['Isabel Maniega', 30, 5.6, 1],
        id_2=['José Manuel Peña', 30, 7.8, 1],
        id_3=['Pedro López', 25, 5.2, 2],
        id_4=['Julia Garcia', 22, 7.3, 1],
        id_5=['Amparo Mayora', 28, 8.4, 3],
        id_6=['Juan Martínez', 30, 6.8, 3],
        id_7=['Fernando López', 35, 6.1, 2],
        id_8=['María Castro', 41, 5.9, 3])
    EDICION_VALUES = dict(id_1="Uno", id_2="Dos", id_3="Tres")

    # Insert control -> Only if empty tables
    cursor.execute(SQL_NOTAS)
    rows_notas = cursor.fetchone()
    cursor.execute(SQL_EDIC)
    rows_edic = cursor.fetchone()

    if rows_notas[0] == 0 and rows_edic[0] == 0:
        cursor.execute('BEGIN;')
        # Restart Pkey
        cur.execute(sql.SQL("SELECT setval('{}', 1, false);")
                    .format(sql.Identifier("notas_ID notas_seq")))
        cur.execute(sql.SQL("SELECT setval('{}', 1, false);")
                    .format(sql.Identifier("edicion_ID edic_seq")))

        # INSERT table notas
        try:
            for value in NOTAS_VALUES.keys():
                cur.execute(
                    sql.SQL(SQL_INSERT_NOTAS).format(sql.Identifier('notas'),
                                                     sql.Identifier('name'),
                                                     sql.Identifier('age'),
                                                     sql.Identifier('grades'),
                                                     sql.Identifier('ID edic')),
                    (NOTAS_VALUES[value][0], NOTAS_VALUES[value][1],
                     NOTAS_VALUES[value][2], NOTAS_VALUES[value][3]))

            print(f'Table "notas" succesfully INSERT.')
        except Error as e:
            conn.rollback()
            print(f'WARNING: Rollback done.\nERROR: Table "notas" INSERT: {e}')

        # INSERT table edicion
        try:
            for value in EDICION_VALUES.keys():
                print(EDICION_VALUES[value])
                cur.execute(
                    sql.SQL(SQL_INSERT_EDIC).format(sql.Identifier('edicion'),
                                                    sql.Identifier('num')),
                    (EDICION_VALUES[value],))

            print(f'Table "edicion" succesfully INSERT.')
        except Error as e:
            conn.rollback()
            print(
                f'WARNING: Rollback done.\nERROR: Table "edicion" INSERT: {e}')
    else:
        print('Tablas con datos ya insertados.')


def update(cursor):
    """
    Updates in tables
    :param cursor: Cursor to operate from conection
    """
    # SQL Instruction
    SQL_UPDATE = "UPDATE {} SET {}=%s WHERE {}=%s;"
    SQL_SELECT = "SELECT * FROM {} WHERE {} IN (%s, %s)"

    # UPDATE
    cursor.execute("BEGIN;")
    try:
        # Data before UPDATE
        cursor.execute(sql.SQL(SQL_SELECT).format(sql.Identifier('notas'),
                                                  sql.Identifier('ID notas')),
                       (3, 8))
        result = cursor.fetchall()
        print('\nDatos antes de cambios:')
        for tuple in result:
            print(tuple)

        # UPDATEs
        cursor.execute(sql.SQL(SQL_UPDATE).format(sql.Identifier('notas'),
                                                  sql.Identifier('grades'),
                                                  sql.Identifier('ID notas')),
                       (6.4, 3))
        print('"ID notas=3" UPDATED.')
        cursor.execute(sql.SQL(SQL_UPDATE).format(sql.Identifier('notas'),
                                                  sql.Identifier('grades'),
                                                  sql.Identifier('ID notas')),
                       (5.2, 8))
        print('"ID notas=8" UPDATED.')

        # Data after UPDATE
        cursor.execute(sql.SQL(SQL_SELECT).format(sql.Identifier('notas'),
                                                  sql.Identifier('ID notas')),
                       (3, 8))
        result = cursor.fetchall()
        print('\nDatos tras cambios:')
        for tuple in result:
            print(tuple)

    except Error as e:
        conn.rollback()
        print(f'WARNING: Rollback done.\nERROR: Table "notas" UPDATE: {e}')


def select(cursor):
    """
    Visualize data in tables
    :param cursor: Cursor to operate changes
    """

    def select_print(table_name):
        """
        Show data from tables
        :param sql: SQL query to operate
        :param cursor: Cursor to operate
        :param table_name: Name of the table to operate
        """

        # SQL instruction
        SQL_SELECT = "SELECT * FROM {}"

        cursor.execute(sql.SQL(SQL_SELECT).format(sql.Identifier(table_name)))
        column_names = [name[0] for name in cursor.description]

        # Show info
        print(f'\n Datos para tabla {table_name}:\n{column_names}')
        result = cursor.fetchall()
        for tuple in result:
            print(tuple)

    # Print all data in tables
    select_print('notas')
    select_print('edicion')


def print_data(info, table_name, data, columns):
    """
    :param info: Text to display
    :param table_name: Name from the table to print
    :param data: Result from de query
    :param columns: Name of the table columns
    """
    print(f'\n{info}\nTabla: {table_name}\n{columns}')
    # print(f'\n Datos para tabla {table_name}:\n{columns}')
    for tuple in data:
        print(tuple)


def query_4(cursor):
    """
    Find data where 5 < grade < 6.5
    :param cursor: Cursor to operate in database
    """
    # SQL query
    SQL_QUERY = "SELECT * FROM {} WHERE {} BETWEEN %s AND %s"

    # Query execution
    cursor.execute(sql.SQL(SQL_QUERY).format(sql.Identifier('notas'),
                                             sql.Identifier('grades')),
                   (5, 6.5))

    # Get table info
    column_names = [name[0] for name in cursor.description]
    INFO = 'Notas entre 5 y 6.5'

    print_data(INFO, 'notas', cursor.fetchall(), column_names)


def query_5(cursor):
    """
    Find student in edition "Dos"
    :param cursor: Cursor to operate in database
    """
    # SQL query
    SQL_QUERY = '''
    SELECT {}
    FROM {}
    JOIN {} 
        ON notas.{} = edicion.{} AND edicion.{} = %s;
    '''

    EDICION = 'Dos'

    # Query execution
    cursor.execute(sql.SQL(SQL_QUERY).format(sql.Identifier('name'),
                                             sql.Identifier('notas'),
                                             sql.Identifier('edicion'),
                                             sql.Identifier('ID edic'),
                                             sql.Identifier('ID edic'),
                                             sql.Identifier('num')),
                   (EDICION,))

    # Get table info
    column_names = [name[0] for name in cursor.description]
    INFO = 'Alumnos de la edicion "Dos"'

    print_data(INFO, 'notas', cursor.fetchall(), column_names)


def delete(cursor):
    """
    Delete student
    :param cursor: Cursor to operate in database
    """
    # SQL Instruction
    SQL_DELETE = 'DELETE FROM {} WHERE {} LIKE %s;'

    STUDENT = 'Pedro López'

    # Query execution
    cursor.execute(sql.SQL(SQL_DELETE).format(sql.Identifier('notas'),
                                              sql.Identifier('name')),
                   (STUDENT,))


if __name__ == '__main__':
    # Create connection
    conn = connection('actividad')
    # Create cursor to operate
    cur = conn.cursor()
    # INSERT data in tables
    insert(cur)
    # UPDATE data in tables
    update(cur)
    # SELECT data in tables
    select(cur)
    # Query 4
    query_4(cur)
    # Query 5
    query_5(cur)
    # DELETE
    delete(cur)

    if conn:
        # Close communication
        conn.commit()
        cur.close()
        conn.close()
