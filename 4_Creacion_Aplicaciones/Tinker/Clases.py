'''
Clase con los atributos y metodos de la GUI para Iris Dataset
'''
import tkinter as tk
from PIL import ImageTk, Image
import joblib

BACKG_ROOT = 'media/iris_background.png'

# Cargar modelo Machine Learning guardado
ML_IRIS = joblib.load('data/ML_Iris_Dataset')

class Gui(tk.Frame):

    def __init__(self, parent=None):
        '''
        Creacion del objeto GUI
        '''
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.__initGUI()

    def __initGUI(self):
        '''
        Definición de las caracteristicas y widgets de la GUI
        :return:
        '''
        # Definicion de caracteristicas gráficas
        # Fondo de pantalla temático
        self.img = ImageTk.PhotoImage(Image.open(BACKG_ROOT))
        self.canvas = tk.Canvas(self.parent, width=1000, height=500)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')
        self.canvas.pack(fill='both', expand=False)

        # Titulo de la GUI
        self.parent.title('IRIS DATASET')
        # Atributos varios
        self.parent.resizable(False, False)

        # Widgets GUI
        # Titulo herramienta
        self.h1 = tk.Label(self.parent,
                           text='INDIQUE LOS PARAMETROS DE SU FLOR IRIS',
                           foreground='blue')
        # Labels indicar campo de entrada
        self.l1 = tk.Label(self.parent, text='Longitud Petalo (cm)')
        self.l2 = tk.Label(self.parent, text='Anchura Petalo (cm)')
        self.l3 = tk.Label(self.parent, text='Longitud Sepalo (cm)')
        self.l4 = tk.Label(self.parent, text='Anchura  Sepalo (cm)')
        # Boton de prediccion
        self.btn1 = tk.Button(self.parent, text='Predecir', bg='light blue',
                              command=self.__Predict)
        # Boton de cierre de GUI
        self.btnExit = tk.Button(self.parent, text='SALIR', bg='red',
                                 fg='white', command=self.__Exit)
        # Campos de entrada
        self.in1 = tk.Entry(self.parent)
        self.in1.insert(0,'escribe aqui')
        self.in2 = tk.Entry(self.parent)
        self.in2.insert(0,'escribe aqui')
        self.in3 = tk.Entry(self.parent)
        self.in3.insert(0,'escribe aqui')
        self.in4 = tk.Entry(self.parent)
        self.in4.insert(0,'escribe aqui')
        # Posicionado de los elementos
        self.h1.place(x=650, y=20)
        self.l1.place(x=520, y=50)
        self.in1.place(x=650, y=50)
        self.l2.place(x=520, y=70)
        self.in2.place(x=650, y=70)
        self.l3.place(x=520, y=90)
        self.in3.place(x=650, y=90)
        self.l4.place(x=520, y=110)
        self.in4.place(x=650, y=110)
        self.btn1.place(x=730, y=150)
        self.btnExit.place(x=950, y=475)

    def __Predict(self):
        '''
        Predecir el tipo de flor IRIS
        :return:
        '''
        # Reiniciamos el label de resultado
        try:
            self.lPred.destroy()
        except Exception:
            pass
        self.lPred = tk.Label(self.parent, text='')

        # Evaluamos la specie con Machine Learning
        data = [[self.in3.get(), self.in4.get(),
                 self.in1.get(), self.in2.get()]]
        try:
            especie = ML_IRIS.predict(data)

            if especie == 0:
                especie = 'setosa'
            elif especie == 1:
                especie = 'versicolor'
            else:
                especie = 'virginica'

            # Label de resultado de prediccion
            self.lPred = tk.Label(self.parent, fg='orange', bg='white',
                                  text=f'Se trata de Iris {especie}')
        except Exception:
            # Label de resultado de prediccion
            self.lPred = tk.Label(self.parent, fg='red', bg='white',
                                  text='ERROR con los parametros')

        self.lPred.place(x=800, y=75)

    def __Exit(self):
        '''
        Cierre de la aplicacion
        :return:
        '''
        self.parent.quit()
        self.parent.destroy()
