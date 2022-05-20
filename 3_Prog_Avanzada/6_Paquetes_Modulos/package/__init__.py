'''
    Modulo de inicialización de los diferentes subpaquetes y modulos del paquete padre.
'''

# Al inicializar importamos los paquetes y modulos que se desea.
# Ejemplo de importación de diferentes modos.
from package.sub_package1 import mod1,  mod2
from sub_package2.mod3 import nameMe_mod3
from sub_package2 import mod4

# Al tratarse de un modulo más, pese a sus caracteristicas, también se podrá ejecutar comandos
print('-> Package importado con exito.')