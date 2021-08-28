import pandas as pd
import os
archivo = 'D:\\PYTHON CURSO\\PruebaCargaArchivo\\PruebaCarga\\Archivos\\Archivo\\DATOS_PARA_CARGAR.xlsx'
datos = pd.read_excel(archivo,sheet_name='Centro',header=0)
print(datos.describe())