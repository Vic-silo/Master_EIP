'''
    ACTIVIDAD LECCION 11
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Crear una GUI sencilla con el Framework PyQt5

'''
from Clases import *
from PyQt5.QtWidgets import QApplication
import sys

def CheckExpresion(expresion):
    '''
    Evaluacion de la expresión a calcular
    :param expresion:
    :return:
    '''
    try:
        return str(eval(expresion, {}, {}))
    except Exception:
        return 'OPERACION ERRONEA'

guiApp = QApplication(sys.argv)

# Instancia de la GUI
view = CalcWindow()
view.show()
# Instancia de la conexión con la GUI
exp = CheckExpresion
CalcControl(gui=view, exp=exp)

# Ejecucion de la aplicacion en loop
sys.exit(guiApp.exec())