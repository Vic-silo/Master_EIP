import pandas as pd
import matplotlib.pyplot as plt
import os
import logging
# DataLength: Control de longitud de archivo
from Excepciones import DataLength
# MonthEmpty: Control de columna mes vacia
from Excepciones import MonthEmpty
# ValueError:  Control de una conversion erronea a valor numerico
from Excepciones import ConvertError

# STATICS
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_ROOT = os.path.join(ROOT_DIR, r'data\finanzas2020[1].csv')
# CSV_ROOT_2 = os.path.join(ROOT_DIR, 'data/finanzas2020[2].csv')
PLOT_ROOT = os.path.join(ROOT_DIR, r'media\Ahorro anual 2020.png')
LOG_FILES = os.path.join(ROOT_DIR, r'logs\exceptions')

# VARS
# Diccionario de listas para almacenar los datos de cada mes
dictMeses = dict(
    mes=[],
    gasto=[],
    ingreso=[],
    ahorro=[]
)

# Configuracion logs
logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILES,
                    filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - '
                           '%(message)s')


# CREACION DATAFRAME
# Control en bucle hasta la correcta lectura del fichero deseado.
while True:
    try:
        # Probamos a generar el dataframe con el archivo segun nuestra variable
        dfGastos = pd.read_csv(CSV_ROOT, sep='\t')
        # Si creación OK
        logging.info('Fichero: OK.')
        break
    except IOError:
        # Error con el CSV_ROOT
        print(
            f'\nError en la lectura del archivo. Asegurese de que existe en '
            f'la ruta "{CSV_ROOT}" o introduzca una nueva ruta.')
        # Control de usuario.
        choice = input('¿Desea indicar una nueva ruta? Yes[Y]/No[N]: ')
        if choice.upper() == 'Y':
            CSV_ROOT = input(r'Nueva Ruta (asegurese de no introducir ""): ')
        if choice.upper() == 'N':
            logging.warning('Fichero: Fail.')
            break

try:
    def CheckDataLength(df=dfGastos):
        # Comprobacion del tamaño del dataframe
        try:
            # Comprobar si el numero de columnas es igual a 12
            if not len(list(df)) == 12:
                raise DataLength
                # df = ''
            else:
                logging.info('Dataframe generado con exito. '
                             'Sus columnas son correctas')
                if __name__ == '__main__':
                    print('Dataframe generado con exito. '
                          'Sus columnas son correctas')
                    print(df)
                return 12

        except DataLength as e:
            logging.warning(e)

except NameError as e:
    # print('Not possible to check')
    logging.error(f'{e}\nDataframe not exists.')


try:
    def CheckEmpty(df=dfGastos):
        check = ''
        # Recorrer los meses/columnas del dataframe
        for col in df:
            values = pd.Series(df[col])
            try:
                # Si esta sin datos la columna, levantamos la excepcion
                # con argumento el nombre de la columna
                if values.dropna().empty:
                    print('Aviso: ')
                    raise MonthEmpty(col)

            except MonthEmpty as e:
                logging.warning(e)
                check = 'Fail'

        # Si todas las columnas tienen datos 'Succes'
        if check == '':
            logging.info(f'CheckEmpty: Meses completos.')
            return 'Success'
        else:
            return check

except NameError as e:
    # print('Not possible to check')
    logging.error(f'{e}\nDataframe not exists.')

try:
    def CheckValues(df=dfGastos):
        global dfGastos
        # Se recorre todas las columnas del dataframe
        for col in df:
            # Se recorre las filas del dataframe para verificar el tipo de dato
            for i in range(len(df)):
                valor = df.loc[i, col]
                try:
                    valor = int(valor)
                    dfGastos.loc[i, col] = valor
                except Exception:
                    try:
                        raise ConvertError(valor, col)
                    except ConvertError as e:
                        while True:
                            try:
                                print(e)
                                newValue = int(input(
                                    f'Introduzca un nuevo valor o 0 '
                                    f'si lo descarta: '))
                                print('\n')
                                dfGastos.loc[i, col] = newValue
                                break
                            except ValueError as e:
                                print(f'\nAviso: {e}')

        return 'Success'


except NameError as e:
    # print('Not possible to check')
    logging.error(f'{e}\nDataframe not exists.')

# Ejecutar comprobaciones del Dataframe
print('COMPROBACIONES: ')
print('En curso...')
print('CheckDataLength...')
CheckDataLength()
print('... finished.\n')
print('CheckEmpty...')
CheckEmpty()
print('... finished.\n')
print('CheckValues...')
CheckValues()
print('... finished.\n')
print('... COMPROBACIONES DONE.')

# Crear dataframe auxiliar para saber ahorros, gastos...
try:
    for col in dfGastos:
        gasto = 0
        ingreso = 0
        ahorro = 0
        # Rellenar la lista con el nombre del mes
        dictMeses['mes'].append(col)

        # Convertir valores a numero sustituyendo los NaN encontrados por 0
        # dfGastos[col] = pd.to_numeric(dfGastos[col], errors='coerce')
        # dfGastos[col] = dfGastos[col].fillna(int(0))

        # Recorrer las filas del mes e ir sumando los valores
        for i in range(len(dfGastos)):
            valor = dfGastos.loc[i, col]
            # Almacenar los valores negativos, es decir, son un gasto
            if valor < 0:
                valor *= -1
                gasto += valor
            # Almacenar los valores positivos, es decir, son un ingreso
            elif valor > 0:
                ingreso += valor

        gasto = int(gasto)
        ingreso = int(ingreso)
        ahorro = ingreso - gasto
        # Añadir datos al mes en bucle
        dictMeses['gasto'].append(gasto)
        dictMeses['ingreso'].append(ingreso)
        dictMeses['ahorro'].append(ahorro)

    # Convertir a Dataframe el diccionario creado
    dfMeses = pd.DataFrame(dictMeses)

except Exception as e:
    logging.error(f'{e}')

try:
    def MayorGasto(df=dfMeses):
        # Meses ordenados por gasto
        df = df.sort_values(by='gasto', ascending=False)
        return df.iloc[0]['mes']

except NameError as e:
    # print('Function impossible to execute.')
    logging.error(f'{e}\nDataframe not exists.')

try:
    def MayorAhorro(df=dfMeses):
        # Meses ordenador por ahorro
        df = df.sort_values(by='ahorro', ascending=False)
        return df.iloc[0]['mes']

except NameError as e:
    # print('Function impossible to execute.')
    logging.error(f'{e}\nDataframe not exists.')

try:
    def MediaGasto(df=dfMeses):
        return df['gasto'].mean()

except NameError as e:
    # print('Function impossible to execute.')
    logging.error(f'{e}\nDataframe not exists.')


try:
    def GastoTotal(df=dfMeses):
        return df['gasto'].sum()

except NameError as e:
    # print('Function impossible to execute.')
    logging.error(f'{e}\nDataframe not exists.')


try:
    def IngresoTotal(df=dfMeses):
        return df['ingreso'].sum()
except NameError as e:
    # print('Function impossible to execute.')
    logging.error(f'{e}\nDataframe not exists.')


try:
    def IngresosPlot(df=dfMeses):
        # Definicion del set de datos a plotear
        x = df['mes']
        y = df['ingreso']

        plt.figure(figsize=(15, 5))

        plt.bar(x, y)

        plt.suptitle('Ahorro año 2020')

        # Guardar gráfico y mostrar
        plt.savefig(PLOT_ROOT, bbox_inches='tight')
        plt.show()

except NameError as e:
    # print('Not possible to plot.')
    logging.error(f'{e}\nDataframe not exists.')


if __name__ == '__main__':
    try:
        print('\nRESPUESTAS: ')
        print(f'Respuestas en base a: \n{dfMeses}\n')
        print(f'El mes con mayor gasto se trata de: {MayorGasto()}')
        print(f'El mes con mayor ahorro se trata de: {MayorAhorro()}')
        print(f'La media de gasto para 2020 ha sido de: {MediaGasto():0.2f}')
        print(f'El gasto total para 2020 ha sido de: {int(GastoTotal())}')
        print(f'El ingreso total para 2020 ha sido de: {int(IngresoTotal())}')
        IngresosPlot()

    except NameError:
        print('Error de lectura de fichero.')
        logging.error('Fichero .csv no cargado con exito.')
