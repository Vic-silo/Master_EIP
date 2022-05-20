'''
Clases para creacion de la GUI Calculadora con PyQt
'''
# Imports PyQt5 para el desarrollo de la GUI
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

# Import para controlar los eventos de la GUI
from functools import partial

class CalcWindow(QMainWindow):
    '''
    Clase para instanciar la apariencia de la aplicacion
    '''
    def __init__(self):
        super().__init__()
        # Titulo y dimensiones de la ventana de la aplicación
        self.setWindowTitle('Calculadora')
        # Puesto que se trata de una calculadora simple,
        # no necesitamos que el usuario cambie su tamaño.
        self.setFixedSize(400, 350)

        # Objeto para albergar los elementos de la GUI:
        # Layout para los botones de la calculadora y display de operacion
        # Layouts nexados para mostrar ambos con alineaciones diferentes
        self.displayLayout = QHBoxLayout()
        self.genealLayout = QVBoxLayout()
        self.genealLayout.addLayout(self.displayLayout)
        # Añadir el layout al objeto central de la GUI
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.genealLayout)

        # Metodos para crear los elementos de la GUI
        self.__Display()
        self.__Buttons()

    def __Display(self):
        '''
        Metodo para crear el objeto display
        :return:
        '''
        # Elemento display
        self.display = QLineEdit()

        # Atributos del display
        self.display.setFixedSize(350, 50)
        self.display.setAlignment(Qt.AlignCenter)
        self.display.setReadOnly(True)

        # Añadir el display al Layout
        self.displayLayout.addWidget(self.display)


    def __Buttons(self):
        '''
        Metodo para crear la tabla con botones para interactuar
        :return:
        '''
        # Elemento botones
        self.buttons = dict()
        btnsLayout = QGridLayout()

        # Diccionario con los botones y posicion en tabla
        btnsDict = {
            '7':(0,0),
            '8':(0,1),
            '9':(0,2),
            '4':(1,0),
            '5':(1,1),
            '6':(1,2),
            '1':(2,0),
            '2':(2,1),
            '3':(2,2),
            ',':(3,0),
            '0':(3,1),
            'C':(3,2),
            '+':(0,3),
            '-':(0,4),
            '*':(1,3),
            '/':(1,4),
            '(':(2,3),
            ')':(2,4),
            '=':(3,3)
        }

        # Crear los botones y añadirlos al layout
        for label, pos in btnsDict.items():
            self.buttons[label] = QPushButton(label)
            self.buttons[label].setFixedSize(60,60)
            btnsLayout.addWidget(self.buttons[label],pos[0],pos[1])
            if label not in {'0', '1', '2', '3', '4', '5',
                             '6', '7', '8', '9', ','}:
                self.buttons[label].setStyleSheet('background-color : '
                                                  'grey')
            if label == 'C':
                self.buttons[label].setStyleSheet('background-color : '
                                                  'red')
            if label == '=':
                self.buttons[label].setStyleSheet('background-color : '
                                                  'orange')

        # Añadir botones al layout de la GUI
        self.genealLayout.addLayout(btnsLayout)

    def SetDisplay(self, oper):
        '''
        Añadir los numeros y calculos al display
        :return:
        '''
        self.display.setText(oper)
        self.display.setFocus()

    def GetDisplay(self):
        '''
        Obtener el texto del display
        :return:
        '''
        return self.display.text()

    def ClearDisplay(self):
        '''
        Eliminar el display
        :return:
        '''
        self.display.clear()

class CalcControl(CalcWindow):
    '''
    Clase para el control de los eventos
    '''
    def __init__(self, gui, exp):
        super().__init__()
        self.gui = gui
        self.eval = exp
        self.GuiConexion()

    def Calcular(self):
        '''
        Calculo de la expresion matematica
        :return:
        '''
        # Evaluacion de la expresión mediante CheckExpresion de main
        resultado = self.eval(expresion=self.gui.GetDisplay())
        self.gui.SetDisplay(resultado)

    def setMathExpr(self, mathExpr):
        '''
        Creacion de la operacion a partir de los datos instroducidos
        :param mathExpr: Expresion a tratar
        :return:
        '''
        if self.gui.GetDisplay() == 'OPERACION ERRONEA':
            self.gui.ClearDisplay()

        expression = self.gui.GetDisplay() + mathExpr
        self.gui.SetDisplay(expression)

    def KeyPressEvent(self, e):
        return print(e.text())

    def GuiConexion(self):
        '''
        Establecer conexion entre los botones de la calculadora y modelo
        :return:
        '''
        try:
            for label, btn in self.gui.buttons.items():
                # Capturar marcado de botones que no sea = o C
                if label not in {'=', 'C'}:
                    btn.clicked.connect(partial(self.setMathExpr, label))

                # Capturar marcado de C
                self.gui.buttons['C'].clicked.connect(self.gui.ClearDisplay)
                # Capturar marcado de = por boton o enter en teclado
                self.gui.display.returnPressed.connect(self.Calcular)
                self.gui.buttons['='].clicked.connect(self.Calcular)

        except Exception as e:
            print(e)