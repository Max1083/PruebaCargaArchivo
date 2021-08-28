from django.shortcuts import render, HttpResponse
from django.conf import settings
from .models import Document,Datos
import pandas as pd
import os, csv, openpyxl

current_directory = os.getcwd()
# Create your views here.
def cargar(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = Document.objects.all()

    return render(request, "cargar.html", context = {
        "files": documents
    })

def leerCsv(request):

    with open(current_directory+'/prueba.csv', 'r') as file:
        prueba = csv.reader(file)
    print(prueba)
    return HttpResponse('Prueba lectura csv')

def leerExcel(request):

    wb = openpyxl.load_workbook(current_directory+'/prueba.xlsx')
    sheet = wb.worksheets[0]
    f = pd.DataFrame(sheet.values)
    print("file openpyxl ",f)
    print('*******************')
    excel_data_df = pd.read_excel(current_directory + settings.MEDIA_URL+'/cargar.xlsx', sheet_name='Centro')
    # print whole sheet data
    print(excel_data_df)

    return HttpResponse('Prueba lectura Excel')

def leerArchivo(request):
    datos = read_file('prueba.xlsx')
    print(datos.describe())
    return HttpResponse('Prueba leer Archivo')

def read_file(filename, **kwargs):

    """Read file with **kwargs; files supported: xls, xlsx, csv, csv.gz, pkl"""

    read_map = {'xls': pd.read_excel, 'xlsx': pd.read_excel, 'csv': pd.read_csv,
                'gz': pd.read_csv, 'pkl': pd.read_pickle}

    ext = os.path.splitext(filename)[1].lower()[1:]
    assert ext in read_map, "Formato de archivo incorrecto, puede se xls, xlsx, csv, csv.gz, pkl; current format '{0}'".format(ext)
    assert os.path.isfile(filename), "File Not Found Exception '{0}'.".format(filename)

    return read_map[ext](filename, **kwargs)