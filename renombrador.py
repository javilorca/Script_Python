import csv
import shutil
from tkinter import messagebox as MessageBox

# Renombra cada pdf con los datos que haya en la primera columna + el dato de la segunda columa del CSV + fecha,
# si alguna fila está vacia, continua renombrando el pdf con el ultimo dato de la fila que no estaba vacia

arcsv='./renombrador/reno.csv'
aperfu= open(arcsv, newline='', encoding='utf-8')
aperfusa = csv.reader(aperfu)
fecha=()
vant=()

try:

    for a in aperfusa:
        if a[2] != "":
            fecha=a[2]
        #print(a)
        print("fecha:", fecha)

        if a[0]!="":
            vant=a[0]
        extra="./renombrador/entrada/"+vant+".pdf"
        desti="./renombrador/salida/"+fecha+"-"+a[1]+".pdf"
        shutil.copyfile(extra,desti)
    MessageBox.showinfo("Renombrador", "Proceso finalizado")
except FileNotFoundError as e:
    error=a[0]
    print(error)
    print(f"Error:{ e.strerror}")
    MessageBox.showerror("Error", "El nombre del PDF " +"'"+error+"'"+ " es incorrecto o no existe en entrada")

aperfu.close()