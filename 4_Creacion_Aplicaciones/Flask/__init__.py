'''
    ACTIVIDAD LECCION 8
    Autor: Victor Simo Lozano
    Descripción:
       TAREA: Crear una API REST empleando FLASK
        Metodos a emplear: PUT, GET, PUT, DELETE

'''

# TAREA:

# Importacion de 'Flask' para crear aplicacion
# Importacion de 'request' para realizar la peticion
from flask import Flask, request
import pandas as pd
import json, csv
from Flaskr import ML_Iris

# Crear nuestra variable para ejecucion de la app
app = Flask(__name__)

# Mediante decorador creamos la funcion con url y metodo definidos
@app.route('/')
def home():
    msg = (f'Bienvenido a una applicacion Flask para MachineLearning. '
           f'En la presente aplicacion se ha entrenado la aplicacion con el'
           f' iris Dataset, obteniendo una precision del {ML_Iris.predictResult()} ')
    return msg

@app.route('/iris/')
def irisData():
    '''
    Funcion que nos da la información básica de los datos de iris.csv
    :return:
    '''
    # Crear Dataframe del documento csv para los datos de iris
    df = pd.read_csv('iris.csv')
    # Obtener la informacion del dataframe en json y cargarlo posteriormente
    describe = df.describe().to_json(orient='index')
    describe = json.loads(describe)
    return describe


@app.route('/insertData/', methods=['GET', 'POST'])
def insertData():
    '''
    Funcion que nos permite añadir un valor a nuestro documento.
    :return:
    '''
    # Recogemos los datos que vienen del request
    frontData = request.data
    frontData = json.loads(frontData)
    # Evaluamos la specie con Machine Learning
    specie = [[frontData['sepal_length'],frontData['sepal_width'],
               frontData['petal_length'],frontData['petal_width']]]
    specie = ML_Iris.predictSpecie(specie)
    # Añadir ('a') datos en csv en la ultima posicion (newline = '')
    with open('iris.csv', 'a', newline='') as file:
        columnNames = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
        # Creamos la variable escritora en el csv y le pasamos los valores en formato de diccionario
        writer = csv.DictWriter(file, fieldnames=columnNames)
        writer.writerow(dict(
            sepal_length=frontData['sepal_length'],
            sepal_width=frontData['sepal_width'],
            petal_length=frontData['petal_length'],
            petal_width=frontData['petal_width'],
            species=specie
        ))
    return frontData


@app.route('/updateData/', methods=['GET', 'PUT'])
def updateData():
    '''
    Funcion que nos permite actualizar un valor especifico
    :return:
    '''
    # Recogemos los datos que vienen del frontend y lo pasamos a json
    frontData = request.data
    frontData = json.loads(frontData)
    # Cargamos el archivo csv para actualizar el valor deseado
    index = frontData['index']
    df = pd.read_csv('iris.csv')
    df.loc[df.index[index], 'sepal_length'] = frontData['sepal_length']
    df.loc[df.index[index], 'sepal_width'] = frontData['sepal_width']
    df.loc[df.index[index], 'petal_length'] = frontData['petal_length']
    df.loc[df.index[index], 'petal_width'] = frontData['petal_width']
    df.loc[df.index[index], 'species'] = frontData['species']
    # Guardar el Dataframe para guardar el cambio
    df.to_csv('iris.csv', index=False)
    result = df.iloc[index].to_json(orient='index')
    return result


@app.route('/deleteData/', methods=['GET', 'DELETE'])
def deleteData():
    input = 'index: '
    input = json.loads(input)
    # Capturamos el indice que queremos actualizar
    frontData = request.data
    frontData = json.loads(frontData)
    index = frontData['index']
    # Cargamos el Dataframe y eliminamos el elemento deseado
    df = pd.read_csv('iris.csv')
    df.drop(df.index[index], inplace=True)
    df.to_csv('iris.csv', index=False)
    result = 'Registro eliminado'
    return result


if __name__ == '__main__':
    app.run(debug=True)
