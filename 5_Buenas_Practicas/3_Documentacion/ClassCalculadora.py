'''
# NOTAS DEL AUTOR

<div style="background-color:lightgray; border:2px solid Tomato">
<p>En esta página se muestra la documentación para un módulo de Python el cual ha
sido desarrollada con <a href="https://pdoc.dev/docs/pdoc.html">Pdoc</a>.<br></p>
<p>A lo largo de los métodos documentados y en general se podrá ver el propio codido
fuente del módulo, con lo que el visitante podrá
comprobar la sencillez para generar esta documentación pues para estos comentarios
se puede emplear el sencillo lenguaje de <b>html</b>.</p>
</div>

<hr>

# the `calculadoooora`© Info

Se trata de un pequeño modulo desarrollado en la Actividad 4 de la asignatura
de Python Avanzado.

***Nota:*** Este codigo es de muy bajo nivel, y el unico propósito de mostrarlo
es para la documentación con Pdoc.

¿En que consiste esta clase? Pues una serie de métodos que ayudan al usuario a
conocer varias operaciones matematicas entre dos numeros.

- `Suma`
- `Resta`
- `Multiplicación`
- `Division`

# CALCULADORA
'''

class Calculadora:
    '''
    Contenido de la clase.
    '''

    num1: float
    '''Variable numerica 1'''
    num2: float
    '''Variable numerica 2'''


    def __init__(self, inputNum1: float, inputNum2: float):
        '''

        :param inputNum1: Primer valor con el que realizar calculos.
        :param inputNum2: Segundo valor con el que realizar calculos.
        '''
        self.num1 = inputNum1
        self.num2 = inputNum2

    def suma(self):
        '''
        Funcion suma
        :return: Devuelve la suma de dos numeros
        '''
        return self.num1+self.num2

    def resta(self):
        '''
        Funcion resta
        :return: Devuelve la diferencia de dos numeros
        '''
        return self.num1 - self.num2

    def multiplicacion(self):
        '''
        Funcion multiplicacion
        :return: Devuelve el producto de dos numeros
        '''
        return self.num1 * self.num2

    def division(self):
        '''
        Funcion division
        :return: Devuelve el cociente de dos numeros
        '''
        return self.num1 / self.num2

