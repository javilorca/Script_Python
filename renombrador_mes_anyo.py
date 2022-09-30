import csv
import os
from datetime import datetime
from tkinter import messagebox
from tkinter import *
from distutils.dir_util import copy_tree
import shutil
from os import remove

# Script que coge los datos que haya en la primera columna de un CSV
# Obtiene el archivo .pdf que haya en la carpeta "ori" y hace tantas copias del archivo .pdf
# como filas con informacion haya en la primera columna del .CSV.
# Renombra cada una de las copias del .PDF con el dato que haya en la primera columna del .CSV + _Com_Emp_+mes+año

aperfu= open('exce5.csv', newline='', encoding='utf-8')
aperfusa = csv.reader(aperfu)

dic={}
dic2={}

date = datetime.now()
mes_actual = date.strftime("%m")
day = date.day
year = date.year
anyo = date.year
anyo_str = str(anyo)


ventana = Tk()
ventana.title("Renombador PDF")
ventana.geometry('300x100')


def actual_mes():
    DIRECTORIO_ORIGEN = './ori/'
    DIRECTORIO_SALIDA = './salida/'
    copy_tree(DIRECTORIO_ORIGEN, DIRECTORIO_SALIDA)
    os.chdir('ori/')
    try:
        for f in os.listdir():
            os.chdir('../salida/')
            for a in aperfusa:
                #duplicado = shutil.copy(f, "copia.pdf")
                print(a)
                if len(a) != 0:
                    if a[0] not in dic:
                        dic[a[0]] = []  # OBTIENE COLUMNA DE LOS CODIGOS DE EMPLEADOS
                        print(a[0])
                        # dic[a[0]].append(a[1])

                        codigo = str(a[0])
                        duplicado = shutil.copy(f, "copia.pdf")
                        nombre, extension = os.path.splitext(duplicado)  # separa el nombre y la extension
                        print(nombre)

                        nombre_nuevo = codigo + "_Com_Emp_" + mes_actual + "_" + anyo_str + extension  # añade el nuevo nombre y la extension
                        remplazar = nombre.replace(nombre, nombre_nuevo)
                        print(remplazar)
                        os.rename(duplicado, nombre_nuevo)  # ejecuta el renombrado

        remove(f)

        messagebox.showinfo(message="Proceso finalizado", title="Renombrador PDFS")

    except OSError as err:
        messagebox.showerror(message="OS error: {0}".format(err), title="Error")
        shutil.rmtree('../tmp/')


# BOTONES
l = Label(ventana, text = "Código empleado")
l.config(font =("Arial", 12))
Button(ventana, text="Renombrar pdfs",bg='white', command=actual_mes).place(x=110,y=60)
l.pack()
ventana.mainloop()