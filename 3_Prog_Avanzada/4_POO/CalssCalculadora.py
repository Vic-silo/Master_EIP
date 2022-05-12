# Clase de tipo calculadora

class Calculadora:
    # Atributos de la clase
    num1: float
    num2: float

    # Metodo de inicialización
    def __init__(self, inputNum1, inputNum2):
        self.num1 = inputNum1
        self.num2 = inputNum2

    def suma(self):
        return self.num1+self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2