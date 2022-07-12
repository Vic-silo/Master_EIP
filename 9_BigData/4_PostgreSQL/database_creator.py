from psycopg2 import sql, connect, Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

DATABASE_NAME = sys.argv[1]

# Connect to database
conn = connect(user='admin', password='admin',
               host='localhost', port=5432)

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Create cursor to operate
cur = conn.cursor()

# Create database
# Exta info: sql.SQL and sql.Identifier to avoid SQL injection
try:
    cur.execute(sql.SQL('CREATE DATABASE {};').format(
        sql.Identifier(DATABASE_NAME)
    ))
    print(f'Database "{DATABASE_NAME}" succesfully create.')
except Error as e:
    print(f'Database create error: {e}')

# Close communication
cur.close()
conn.close()
