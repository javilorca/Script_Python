from PyPDF2 import PdfFileMerger
import csv
import os
from datetime import datetime
from tkinter import messagebox
from tkinter import *
from distutils.dir_util import copy_tree
import shutil

# Coge los datos de la primera columna de un CSV y renombra cada PDF que haya en la carpeta "ori" que coincida el nombre
# con el dato de la segunda columna del CSV. Al finalizar, hace una copia de esos archivos, renombra la copia de los archivos
# añadiendole +G+AÑO+MES y junta todos los archivos



# SI LA CARPETA TMP NO EXISTE, CREALA
if os.path.exists('tmp/') is False:
    os.mkdir('tmp/')


aperfu= open('exce.csv', newline='', encoding='utf-8')
aperfusa = csv.reader(aperfu)

dic={}
dic2={}

####################################################################################################

date = datetime.now()
mes_actual = date.strftime("%m")
months = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
day = date.day
month = months[date.month]
year = date.year
mes_siguiente = "{}".format(month)
anyo = date.year
anyo_siguiente = date.year+1

print(mes_actual)

ventana = Tk()
ventana.title("Renombador PDF")
ventana.geometry('300x100')

mes_siguiente_str = str(mes_siguiente)
mes_str = str(mes_actual)
anyo_str = str(anyo)
anyo_str=(str(anyo))
anyo_siguiente_str = str(anyo_siguiente)


def actual_mes():
    try:
        for a in aperfusa:
            print(a)
            if a[0] not in dic:
                dic[a[0]] = []
            dic[a[0]].append(a[1])

        # print(dic)

        # Añade .pdf
        for a in dic:
            extra = "./ori/" + a + ".pdf"
            dic2[extra] = []
            for b in dic[a]:
                dic2[extra].append("./comp/" + b + ".pdf")

        # print(dic2)
        for a in dic2:
            salidanom = "./salida/" + a[6:]
            print(salidanom)
            fusionador = PdfFileMerger()
            fusionador.append(open(a, 'rb'))
            for b in dic2[a]:
                fusionador.append(open(b, 'rb'))
            with open(salidanom, 'wb') as salida:
                fusionador.write(salida)
            salida.close()


        DIRECTORIO_ORIGEN = './salida/'
        DIRECTORIO_DESTINO = './tmp/'
        copy_tree(DIRECTORIO_ORIGEN, DIRECTORIO_DESTINO)

        os.chdir('./tmp/')
        for f in os.listdir():

            nombre, extension = os.path.splitext(f)  # separa el nombre y la extension
            nombre_nuevo = nombre + "-" + "G" + "-" + anyo_str + "-" + mes_actual + extension  # añade el nuevo nombre y la extension
            remplazar = nombre.replace(nombre, nombre_nuevo)
            print(remplazar)
            os.rename(f, nombre_nuevo)  #ejecuta el renombrado
        messagebox.showinfo(message="Recuerde dejar vacia la carpeta SALIDA", title="Proceso finaizado")

    except OSError as err:
        messagebox.showerror(message="OS error: {0}".format(err), title="Error")
        shutil.rmtree('../tmp/')

    cwd = os.getcwd()
    print("la ruta es" + cwd)
    archivos_origen = '../tmp/'
    archivos_destino = '../salida'

    ficheros = os.listdir('../tmp/')

    for g in ficheros:
        shutil.move(archivos_origen + g, archivos_destino)


def siguiente_mes():
    try:
        for a in aperfusa:
            print(a)
            if a[0] not in dic:
                dic[a[0]] = []
            dic[a[0]].append(a[1])

        # print(dic)

        # Añade .pdf
        for a in dic:
            extra = "./ori/" + a + ".pdf"
            dic2[extra] = []
            for b in dic[a]:
                dic2[extra].append("./comp/" + b + ".pdf")

        # print(dic2)
        for a in dic2:
            salidanom = "./salida/" + a[6:]
            print(salidanom)
            fusionador = PdfFileMerger()
            fusionador.append(open(a, 'rb'))
            for b in dic2[a]:
                fusionador.append(open(b, 'rb'))
            with open(salidanom, 'wb') as salida:
                fusionador.write(salida)
            salida.close()


        DIRECTORIO_ORIGEN = './salida'
        DIRECTORIO_DESTINO = './tmp/'
        copy_tree(DIRECTORIO_ORIGEN, DIRECTORIO_DESTINO)

        os.chdir('./tmp/')
        # SI EL MES ACTUAL ES DICIEMBRE, SUMA UN AÑO MAS
        if mes_actual == '12':
            for f in os.listdir():
                nombre, extension = os.path.splitext(f)  # separa el nombre y la extension
                nombre_nuevo = nombre + "-" + "G" + "-" + anyo_siguiente_str + "-" + mes_siguiente_str + extension  # añade el nuevo nombre y la extension
                remplazar = nombre.replace(nombre, nombre_nuevo)
                print(remplazar)
                os.rename(f, nombre_nuevo)  #ejecuta el renombrado
            messagebox.showinfo(message="Recuerde dejar vacia la carpeta SALIDA", title="Renombrador PDFS")

    except OSError as err:
        messagebox.showerror(message="OS error: {0}".format(err), title="Error")
        shutil.rmtree('../tmp/')

    # SI EL MES ACTUAL NO ES DICIEMBRE, MANTEN EL AÑO ACTUAL
    else:

        try:
            for f in os.listdir():
                nombre, extension = os.path.splitext(f)  # separa el nombre y la extension
                nombre_nuevo = nombre + "-" + "G" + "-" + anyo_str + "-" + mes_siguiente_str + extension  # añade el nuevo nombre y la extension
                remplazar = nombre.replace(nombre, nombre_nuevo)
                print(remplazar)
                os.rename(f, nombre_nuevo)  # ejecuta el renombrado
            messagebox.showinfo(message="Recuerde dejar vacia la carpeta SALIDA", title="Renombrador PDFS")

        except OSError as err:
            messagebox.showerror(message="OS error: {0}".format(err), title="Error")
            shutil.rmtree('../tmp/')

    archivos_origen = '../tmp/'
    archivos_destino = '../salida'

    ficheros = os.listdir('../tmp/')

    for g in ficheros:
        shutil.move(archivos_origen + g, archivos_destino)


# BOTONES
l = Label(ventana, text = "Escoja un mes")
l.config(font =("Arial", 12))
Button(ventana, text="Mes actual",bg='white', command=actual_mes).place(x=50,y=60)
Button(ventana, text="Mes siguiente",bg='white', command=siguiente_mes).place(x=150,y=60)
l.pack()
ventana.mainloop()