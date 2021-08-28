from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='App'

urlpatterns = [
    path('i',views.cargar, name='cargar'),
    path('leerCsv',views.leerCsv, name='leerCsv'),
    path('',views.leerExcel, name='leerExcel'),
    path('leerArchivo',views.leerArchivo, name='leerArchivo'),

]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )