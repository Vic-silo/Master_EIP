'''
    ACTIVIDAD LECCION 14
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Crear una aplicación con PyWebIO
'''

from PyWebIO_API import API_PyWebIO as API
from pywebio import start_server

def main():
    API()

if __name__ == '__main__':
    start_server(main, port=8080, debug=True)