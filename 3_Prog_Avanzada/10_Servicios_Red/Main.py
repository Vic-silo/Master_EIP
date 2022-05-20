'''
    ACTIVIDAD LECCION 10
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Trabajar con aplicaciones web.
            - Crear una basica pagina web con Flask

'''

# TAREA:
print('TAREA:\n'
      'A continuacion se va a mostrar los parametros\n'
      'de conexion de enlace a la web local creada\n'
      'con Flask.')

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hola mundo con Flask"


# Codigos .cmd
#set "FLASK_APP=Main.py"
#set "FLASK_ENV=development"
#python -m flask run


