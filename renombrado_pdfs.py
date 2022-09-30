# Renombra todos los archivos que hayan en la carpeta PDFS
# Mantiene el nombre y le añade -G-ANYO-MES
import os
from datetime import datetime
from tkinter import messagebox

# Renombra los PDFS añadiendole +G+AÑO+MES

date = datetime.now()
year = date.strftime("%Y")
mes = date.strftime("%m")

os.chdir('pdfs/')

try:
   for f in os.listdir():
      nombre, extension = os.path.splitext(f) # separa el nombre y la extension
      nombre_nuevo=nombre+"-"+"G"+"-"+year+"-"+mes+extension # añade el nuevo nombre y la extension
      remplazar = nombre.replace(nombre, nombre_nuevo)
      print(remplazar)
      os.rename(f, nombre_nuevo) # ejecuta el renombrado
   messagebox.showinfo(message="Proceso finalizado", title="Renombrador PDFS")

except Exception as e:
    messagebox.showerror(message="e", title="Renombrador PDFS")