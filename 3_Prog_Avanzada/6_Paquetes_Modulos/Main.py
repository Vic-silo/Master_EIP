'''
    ACTIVIDAD LECCION 6
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Crear una estructura de subpaquetes y modulos.
'''

# TAREA
from package import sub_package2, sub_package1

print('\nTAREA:\n'
      'A continuación se va a mostrar el resultado de\n'
      'la llamada a una serie de metodos dentro del\n'
      'paquete al que se llama en este modulo.\n')

mod1 = sub_package1.mod1.nameMe_mod1()
mod2 = sub_package1.mod2.nameMe_mod2()
mod3 = sub_package2.nameMe_mod3()
mod4 = sub_package2.mod4.nameMe_mod4()

print (f'1: {mod1}\n'
       f'2: {mod2}\n'
       f'3: {mod3}\n'
       f'4: {mod4}')
