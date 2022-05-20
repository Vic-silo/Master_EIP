'''
    Clase constructora de la API
'''

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd

BG_IMAGE = 'assets/background.png'
MARGINAL_PRICES = 'data/MarginalPrice.csv'
COLORS = {
    'ocre': '#E2D365',
    'aguaMarina': '#35A4BE',
    'rojo': '#DB3622',
    'rojoGrisaceo': '#EAD7D5'
}


class DashAPI(dash.Dash):
    def __init__(self, parent=None):
        '''
        Creacion del objeto Dash
        :param parent:
        '''
        super().__init__()
        self.app = parent
        self.__InitApi()

    def __InitApi(self):
        '''
        Definicion caracteristicas iniciales de la API
        :return:
        '''
        # Creacion de layouts de la API
        self.__SetPresentation()
        self.__SetInputs()
        self.__SetOutputs()

        # DataFrame de precios marginales
        self.dfPrecios = self.__GetDF(MARGINAL_PRICES)

        self.layout = html.Div(
            html.Div(children=[
                html.Div(children=[
                    self.apiHeader]
                ),
                html.Div(children=[
                    self.inputs,
                    self.grpPrecios]
                ),
                html.Div(
                    html.Img(
                        src=BG_IMAGE
                    )
                )
            ])
        )

    def __SetPresentation(self):

        self.apiHeader = html.Div(
            style={'backgroundColor':COLORS['rojoGrisaceo']},
            children=[
                # Titlo API
                html.H1(
                    children='MERCADO IBERICO ELECTRICO',
                    style={
                        'textAlign': 'center',
                        'color': COLORS['ocre']
                    }
                ),
            ]
        )

    def __SetInputs(self):
        '''
        Define los insputs de la API
        :return:
        '''

        inputHoraMercado = html.Div(children=[
            # Input para la seleccion de franja horaria
            html.Label('Hora de visualización:'),
            dcc.Dropdown(
                id='Hora_Mercado',
                options=[{'label': '01:00', 'value': 'H1'},
                         {'label': '02:00', 'value': 'H2'},
                         {'label': '03:00', 'value': 'H3'},
                         {'label': '04:00', 'value': 'H4'},
                         {'label': '05:00', 'value': 'H5'},
                         {'label': '06:00', 'value': 'H6'},
                         {'label': '07:00', 'value': 'H7'},
                         {'label': '08:00', 'value': 'H8'},
                         {'label': '09:00', 'value': 'H9'},
                         {'label': '10:00', 'value': 'H10'},
                         {'label': '11:00', 'value': 'H11'},
                         {'label': '12:00', 'value': 'H12'},
                         {'label': '13:00', 'value': 'H13'},
                         {'label': '14:00', 'value': 'H14'},
                         {'label': '15:00', 'value': 'H15'},
                         {'label': '16:00', 'value': 'H16'},
                         {'label': '17:00', 'value': 'H17'},
                         {'label': '18:00', 'value': 'H18'},
                         {'label': '19:00', 'value': 'H19'},
                         {'label': '20:00', 'value': 'H20'},
                         {'label': '21:00', 'value': 'H21'},
                         {'label': '22:00', 'value': 'H22'},
                         {'label': '23:00', 'value': 'H23'},
                         {'label': '24:00', 'value': 'H24'}],
                placeholder='Selecciona una hora...',
                searchable=True,
                clearable=False),
            html.Br(),
            # Input para la seleccion del mercado
            html.Label('Mercado de visualizacion:'),
            dcc.RadioItems(
                id='Mercado',
                options=[{'label':'Español', 'value': 'PRICE_SP'},
                         {'label': 'Portugues', 'value': 'PRICE_PT'}])
        ], style={'padding':10, 'flex': 1})

        # Conjunto final Layout
        self.inputs = html.Div(children=[
            html.H4(children='Datos de precio MWh en el mercado iberico'),
            inputHoraMercado,
            ])

    def __SetOutputs(self):
        '''
        Define los outputs de la API
        :return:
        '''
        self.grpPrecios = html.Div(id='graph-Precios_Marginales')

    def __GetDF(self, path):
        '''
        Abrir csv y crear DataFrame
        :param path: Ruta al archivo csv
        :return:
        '''

        return pd.read_csv(path)
