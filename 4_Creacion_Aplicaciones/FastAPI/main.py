'''
    ACTIVIDAD LECCION 9
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Crear una API REST empleando FastAPI
        Metodos a emplear: PUT, GET, PUT, DELETE

'''

# TAREA:

# Importacion de 'FastAPI' para crear aplicacion
from fastapi import FastAPI
import pandas as pd
import json, csv
import ML_Iris
from models import Insert, ClaseIris

MEDIA_ROOT = ('iris.csv')

# Crear nuestra variable para ejecucion de la app
app = FastAPI()

# Mediante decorador creamos la funcion con url y metodo definidos
@app.get('/')
async def home():
    msg = (f'Bienvenido a una applicacion FastAPI para MachineLearning. '
           f'En la presente aplicacion se ha entrenado la aplicacion con el'
           f' iris Dataset, obteniendo una precision del {ML_Iris.predictResult()} ')
    return msg

@app.get('/iris_Dataset/')
async def irisData():
    '''
    Funcion que nos da la información básica de los datos de iris.csv
    :return:
    '''
    # Crear Dataframe del documento csv para los datos de iris
    df = pd.read_csv(MEDIA_ROOT)
    # Obtener la informacion del dataframe en json y cargarlo posteriormente
    describe = df.describe().to_json(orient='index')
    describe = json.loads(describe)
    return describe


@app.post('/insertData/')
async def insertData(item: Insert):
    '''
    Funcion que nos permite añadir un valor a nuestro documento.
    :return:
    '''
    with open(MEDIA_ROOT, 'a', newline='') as file:
        # Conocer los campos del archivo
        fieldnames = ['sepal_length', 'sepal_width', 'petal_length',
                      'petal_width', 'species']

        # Evaluamos la specie con Machine Learning
        specie = [[item.sepal_length, item.sepal_width,
                   item.petal_length, item.petal_width]]
        specie = ML_Iris.predictSpecie(specie)
        # Definir un writer del archivo con los campos definidos
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'sepal_length': item.sepal_length,
                         'sepal_width': item.sepal_width,
                         'petal_length': item.petal_length,
                         'petal_width': item.petal_width,
                         'species': specie})
        return item


@app.put('/updateData/')
async def updateData(item: ClaseIris, index: int):
    '''
    Funcion que nos permite actualizar un valor especifico
    :return:
    '''
    # Cargamos el archivo csv para actualizar el valor deseado
    df = pd.read_csv(MEDIA_ROOT)
    df.loc[df.index[index], 'sepal_length'] = item.sepal_length
    df.loc[df.index[index], 'sepal_width'] = item.sepal_width
    df.loc[df.index[index], 'petal_length'] = item.petal_length
    df.loc[df.index[index], 'petal_width'] = item.petal_width
    df.loc[df.index[index], 'species'] = item.species
    # Guardar el Dataframe para guardar el cambio
    df.to_csv(MEDIA_ROOT, index=False)
    result = df.iloc[index].to_json(orient='index')
    return result


@app.delete('/deleteData/')
async def deleteData(index: int):
    # Cargamos el Dataframe y eliminamos el elemento deseado
    df = pd.read_csv(MEDIA_ROOT)
    df.drop(df.index[index], inplace=True)
    df.to_csv(MEDIA_ROOT, index=False)
    result = 'Registro eliminado'
    return result