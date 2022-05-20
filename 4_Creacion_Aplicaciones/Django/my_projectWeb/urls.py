"""my_projectWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
# Incluir la aplicacion al proyecto
from django.conf.urls import include, url
# Convocar a las ulrs de las settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r"^", include("myApp.urls")),
    # TODO: nombrar las url de admin
    # TODO: nombrar la url de traducción
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
