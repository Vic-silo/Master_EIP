from django.conf.urls import url
from myApp import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    # TODO: Añadir las urls para accounts
    # TODO: Añadir las urls para register
    # TODO: Añadir las urls para iris
    # TODO: Añadir las urls para insertData
    # TODO: Añadir las urls para updateData
    # TODO: Añadir las urls para deleteData
]
