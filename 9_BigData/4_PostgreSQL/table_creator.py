from psycopg2 import sql, connect, Error

# Connect to existing database
conn = connect(database='actividad',
               user='admin', password='admin',
               host='localhost', port=5432)

# Create cursor to operate
cur = conn.cursor()
cur.execute('BEGIN;')
# Create tables
# Exta info: sql.SQL and sql.Identifier to avoid SQL injection
try:
    try:
        # notas table
        cur.execute(sql.SQL("CREATE TABLE notas ({} serial primary key, "
                            "{} varchar, {} int, {} real, {} int);")
                    .format(sql.Identifier('ID notas'),sql.Identifier('name'),
                    sql.Identifier('age'),sql.Identifier('grades'),
                    sql.Identifier('ID edic')))
        print(f'Table "notas" succesfully created.')
    except Error as e:
        conn.rollback()
        print(f'Table "notas" create error: {e}')

    try:
        # edicion table
        cur.execute(sql.SQL('CREATE TABLE edicion ({} serial primary key, '
                            '{} varchar);').format(sql.Identifier('ID edic'),
                                                   sql.Identifier('num')
        ))
        print(f'Table "edicion" succesfully created.')
    except Error as e:
        conn.rollback()
        print(f'Table "edicion" create error: {e}')

finally:
    if conn:
        # Close communication
        conn.commit()
        cur.close()
        conn.close()
