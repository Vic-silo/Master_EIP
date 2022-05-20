'''
API PyWebIO
'''

from pywebio import *
import cutecharts.charts as ctc
import pandas as pd

MEDIA_ROOT = 'media/vehiculos.jpg'


class API_PyWebIO():
    def __init__(self):
        self.__Wellcome()
        self.__Logging()
        self.__ShowAPI()

    def __Wellcome(self):
        '''
        "Gracioso" mensaje de bienvenida
        :return:
        '''
        html = '''
        <body style="background-color:orange;">
            <h3 title='Tipico mensaje agradable...' style="font-family:verdana;
            color:blue;">
                Enhorabuena!
            </h3>
            <p>Ha sido seleccionado para visitar esta PyWebIO</p>
        </body>
        '''

        output.popup('SOPRESA!!', [
            output.put_html(html),
            output.put_button('Genial', onclick=lambda: output.close_popup())
        ])

    def __Logging(self):
        '''
        Logeo del usuario
        :return:
        '''
        loggin = input.input_group('LÓGUESE SI ES TAN AMABLE', [
            input.input('Nombre de visitante', name='visitante',
                        placeholder='Aqui tu nombre',
                        required=True),
            input.input('Justificacion del acceso', name='motivo',
                        placeholder='Veamos tu motivo...',
                        required=True)
        ])

        self.visitante = loggin['visitante']

    def __ShowAPI(self):
        '''
        Estructura principal de la API
        :return:
        '''
        # Obtencion de datos para API
        self.__GetDataFrame()

        output.popup('Loggin ok!', [
            f'{self.visitante}, veras aqui un pequeño analisis de vehiculos',
            output.put_button('Vale PyWebIO',
                              onclick=lambda: output.close_popup())
        ])

        # Estilo de la tab
        output.put_row([
            output.put_tabs([
                {'title': 'TOTAL DE VEHICULOS',
                 'content': output.put_scrollable(self.__GraficoCoches(),
                                                  height=750)},
                {'title': 'RESUMEN',
                 'content': self.__Resumen()}
            ]),
            output.put_image(open(MEDIA_ROOT, 'rb').read(),
                             title='Una imagen de coches en una API de coches',
                             position=output.Position.MIDDLE)
        ],
            size='80% 20%')

    def __GetDataFrame(self):
        '''
        Crea dataframe y variables de uso en la aplicacion
        :return:
        '''
        MPG_TO_LKM = 235.21
        self.df = pd.read_csv('data/automobile.csv', index_col=False)

        # Seleccion de columnas de estudio
        self.df = self.df[['make', 'fuel-type', 'horsepower', 'city-mpg',
                           'highway-mpg']]

        # Conversion de datos de consumo de MPG a L/100km
        self.df['city-mpg'] = round(MPG_TO_LKM / self.df['city-mpg'], 2)
        self.df['highway-mpg'] = round(MPG_TO_LKM / self.df['highway-mpg'], 2)

        # Definicion de datos del dataframe
        marcas = self.df['make'].unique()
        self.combustible = self.df['fuel-type'].unique()

        # Obtencion de dataframe con coches por marca
        totCoches = dict(marca=[], numero=[])

        for marca in marcas:
            totCoches['marca'].append(marca)
            totCoches['numero'].append(
                self.df[self.df['make'] == marca]['make'].count())

        self.nCoches = pd.DataFrame.from_dict(totCoches)


    def __GraficoCoches(self):
        '''
        Inserta gráfico en tab 1
        :return:
        '''
        html = output.put_html('''
        <h1>Info grafico:</h1>
        <h4>En esta seccion se muestra el total de vehiculos por marca para 
        los datos del dataframe existente en el backend</h4>
        ''')

        chart = ctc.Bar('Total de vehiculos', width='800px', height='400px')
        chart.set_options(
            labels=list(self.nCoches['marca']),
            x_label='Marcas',
            y_label='numero',
            colors=['#1EAFAE' for i in range(len(self.nCoches))]
        )
        chart.add_series('Numero', list(self.nCoches['numero']))

        myChart = output.put_html(chart.render_notebook())

        return [html, myChart]

    def __Resumen(self):
        '''
        Pequeña despedida
        :return:
        '''

        html = output.put_html('''
        <div>
            <h1 style="background-color:rgba(255, 99, 71, 0.5);">Resumen:</h1>
            <h4>Una vez finalizada esta tab, esta finalizada esta actividad
            en el framework <i>PyWebIO</i> con el que he podido 
            <mark>aprender</mark> aun más, aunque en mi opinion, no es de mi agrado 
            ya que he querido salir de hacer un formulario y resulta todo muy 
            laborioso.</h4>
        </div>
        ''')

        return html
