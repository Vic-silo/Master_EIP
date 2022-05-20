'''
MACHINE LEARNING PARA IRIS DATASET
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# Cargamos el dataframe con los valores de iris
df = pd.read_csv('data/iris.csv')

# Igualacion de especies a valores numericos para la evaluacion de resultados
df.species = df.species.map({'setosa':0,'versicolor':1,'virginica':2})

# Asignacion de X e y a los datos del dataframe
X = df.drop(['species'], axis=1)
X = X.values
y = df.species
y = y.values

# Definicion de set de entrenamiento y test: 75% y 25%
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# Entrenar y crear predicciones
# clasificador:
clf = DecisionTreeClassifier()
# entrenamiento del modelo
clf.fit(X_train, y_train)
# realizamos la prediccion
y_pred = clf.predict(X_test)

# Guardado del modelo
joblib.dump(clf, 'data/ML_Iris_Dataset')

