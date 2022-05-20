'''
    ACTIVIDAD LECCION 9
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Trabajar con paquete Threading
            - Ejecutar una funcion con diferentes hilos.

'''

# TAREA:
print('TAREA:\n'
      'A continuacion se va a mostrar una serie\n'
      'de calculos que se ejecutaran mediante\n'
      'THREADING y de forma secuencial de modo\n'
      'que se pueda apreciar la diferencia entre\n'
      'los mismos.\n')

from threading import Thread
import FuncionGenérica as FG
from time import perf_counter

triangulos = dict(
    # info=['c1','c2','h']
    t1=[2,3,None],
    t2=[None,4,7],
    t3=[2,None,5]
)

# CODIGO CON THREAD
listaProcesos = []
print('EJECUCION DE CODIGO MEDIANTE THREADING:\n')
startTime1 = perf_counter()
# Inicio de los procesos
for i in triangulos.values():
    task = Thread(target=FG.Pitagoras, args=(i[0],i[1],i[2]))
    listaProcesos.append(task)
    task.start()

# Finalizacion de los procesos
for i in listaProcesos:
    task.join()

endTime1 = perf_counter()
print(f'Elapsed time Threaded = {endTime1-startTime1:0.5f}\n')

# CODIGO SECUENCIAL
print('EJECUCION DE CODIGO DE FORMA SECUENCIAL:\n')
startTime2 = perf_counter()
FG.Pitagoras(4,5,None)
FG.Pitagoras(None,3,8)
FG.Pitagoras(4,None,7)

endTime2 = perf_counter()
print(f'Elapsed time Not Threaded= {endTime2-startTime2:0.5f}\n')



