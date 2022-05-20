'''
    Funcion básica
'''
from time import sleep
from math import sqrt

def Pitagoras (cateto1 = None, cateto2 = None, hipotenusa = None):

    print('Empiezo...')
    # Retraso de la funcion de modo que se pueda apreciar el uso del Thread en su llamada
    sleep(1)

    if hipotenusa is None:
        resultado = sqrt(cateto1**2 + cateto2**2)
    elif cateto1 is None:
        resultado = sqrt(hipotenusa**2 - cateto2**2)
    else:
        resultado = sqrt(hipotenusa**2 - cateto1**2)


    return print(f'El calculo del lado restante es: {resultado:.2f}')