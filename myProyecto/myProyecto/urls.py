"""myProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include #agregue la libreria de 'include'
from django.conf.urls.static import static #importar uso de direcciones estaticas
from django.conf import settings #importo el archivo de configuracion (variables MEDIA)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cine.urls')), # indicar que utilice el archivo URSL.py de Cine
    path('accounts/', include('django.contrib.auth.urls')),
]
#incluira en el interior del "path" la ubicacion de los directorio MEDIA
#if settings.DEBUG:
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)





