from django.db import models

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length = 200)
    uploadedFile = models.FileField(upload_to = "Archivo/")
    dateTimeOfUpload = models.DateTimeField(auto_now = True)

class Datos(models.Model):
    id_centro	= models.IntegerField()
    Nom_Centro	= models.CharField(max_length =100)
    Region	    = models.CharField(max_length =100)
    Zona_Centro	= models.CharField(max_length =100)
    Cod_Encargado = models.IntegerField()
