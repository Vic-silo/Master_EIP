'''
    ACTIVIDAD LECCION 10
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Crear una GUI con el Framework TKinter. Esta aplicacion ha de
        ser de mayor complejidad que su homologa con el Framework PyQt5 de
        la siguiente lección.
    Fuente y documentación:
        https://guia-tkinter.readthedocs.io/es/develop/index.html
'''

from Clases import *

if __name__ == '__main__':
    # Creación de la instancia de la aplicación
    ROOT = tk.Tk()
    APP = Gui(ROOT)
    APP.mainloop()
    ROOT.destroy()
