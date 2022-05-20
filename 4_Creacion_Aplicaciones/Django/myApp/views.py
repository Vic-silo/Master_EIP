from django.shortcuts import render
# TODO: importar login requerido
# TODO: importar el formulario
# TODO: importar login
# TODO: importar reverse y redirect


# TODO: Añadir que la autentificación es obligatoria para acceder
def home(request):
    return render(request,
                  'home.html',
                  context={'sepal_length': 5.1, 'sepal_width': 3.5,
                           'petal_length': 1.4, 'petal_width': 0.2,
                           'class': "Iris Setosa"})


def register(request):
    if request.method == "GET":
        # TODO: pasar el formulario a la plantilla de registro
        pass
    elif request.method == "POST":
        # TODO: Guardar el usuario siguiendo el formulario
        pass
