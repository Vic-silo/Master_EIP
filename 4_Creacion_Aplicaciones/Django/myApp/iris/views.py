from rest_framework.decorators import api_view
# TODO: importar status
# TODO: render y redirect
# TODO: importar settings
# TODO: importar pandas, csv y json
# TODO: importar Response


@api_view(['GET'])
def irisData(request):
    if request.method == 'GET':
        # TODO: mostrar los datos de Iris dataset
        pass


@api_view(['GET', 'POST'])
def insertData(request):
    if request.method == 'GET':
        # TODO: mostrar la plantilla insert.html
        pass
    elif request.method == 'POST':
        # TODO: insertar el dato al final del csv usando la librería csv
        pass


@api_view(['GET', 'PUT', 'POST'])
def updateData(request):
    if request.method == 'GET':
        # TODO: mostrar el último dato del dataset update.html
        pass
    # Lo probamos usando POSTMAN:
    elif request.method == 'PUT':
        # TODO: actualizar el último dato del csv
        pass
    # Lo mismo que el método PUT pero a través del front-end:
    elif request.method == 'POST':
        # TODO: actualizar el último dato del csv
        pass


@api_view(['GET', 'DELETE', 'POST'])
def deleteData(request):
    if request.method == 'GET':
        # TODO: mostrar el último dato del dataset en la plantilla delete.html
        pass
    # Lo probamos usando POSTMAN:
    elif request.method == 'DELETE':
        # TODO: eliminar el último dato del csv
        pass
    # Lo mismo que el método DELETE pero a través del front-end:
    elif request.method == 'POST':
        # TODO: eliminar el último dato del csv
        pass
