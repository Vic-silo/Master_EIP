'''
Compresion de listas
'''

# Numeros cuadrados del 1 al 10

# numeros = [1, 2, 3, 4, 5, 6,7,8,9,10]

def Cuadrados():
    '''
    Compresion de listas para calcular los cuadrados de os numeros del 1 al 10
    :return:
    '''
    '''
    Como que queremos los valores del 1 al 10, en nuestro rango de 11, 
    se le pasa los numeros del 0 al 10 asi que añadimos la codicion de si es
    diferente el numero de 0.
    
    Equivalencia del codigo:
    
    cuadrados = []
    for num in range(11):
        if num != 0:
            cuadrados.append(num**2)
            
    ¿Que conseguimos con la compresion de listas?
    Una compresion de listas genéricas es tal que: 
    listResult = [expresion(i) for i in list if condition]
    Lo que conseguimos con esto es que a "listResult" se le añada un valor "i" 
    de la lista "list" si cumple una "condition" determinada.
    
    '''
    cuadrados = [num ** 2 for num in range(11) if num != 0]

    return cuadrados

def Cuadrados_If_Else():
    '''
    Compresión de lista con condiciones anidadas
    :return:
    '''

    res = [num if ((num ** 2) > 50 and num != 0) else 0 for num in range (11) ]

    return res

print(Cuadrados())
print(Cuadrados_If_Else())
