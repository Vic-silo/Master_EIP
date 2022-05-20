'''
    ACTIVIDAD LECCION 12
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Crear una aplicación  con Dash.
            - Obtencion de datos de internet
            - Creacion de aplicacion Dash
'''

from DashApp import *

APP = DashAPI()

@APP.callback(
    Output(component_id='graph-Precios_Marginales', component_property='children'),
    Input(component_id='Hora_Mercado', component_property='value'),
    Input(component_id='Mercado', component_property='value')
)
def GphPrecios(horaMercado, mercado):
    '''
    Crear gráfica de precio del MWh
    :param mercado: Hora del dia a mostrar precio
    :return:
    '''
    try:
        if mercado == 'PRICE_SP':
            df = APP.dfPrecios[APP.dfPrecios['CONCEPT'] == mercado]
            labelMercado = 'Español'
        else:
            df = APP.dfPrecios[APP.dfPrecios['CONCEPT'] == mercado]
            labelMercado = 'Portugues'

        return dcc.Graph(
            id='Spain-Prices',
            figure={
                'data': [
                    {'x': df.DATE,
                     'y': df[horaMercado],
                     'type': 'line'},
                ],
                'layout': {'title': f'Precio electricidad mercado {labelMercado} (€/MWh)'}
            }
        )
    except Exception:
        pass


if __name__ == '__main__':

    APP.run_server(debug=True)
