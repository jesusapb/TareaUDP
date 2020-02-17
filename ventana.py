#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Las dos líneas siguientes son necesaias para hacer
# compatible el interfaz Tkinter con los programas basados
# en versiones anteriores a la 8.5, con las más recientes.
#liberias de sistema
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)
from tkinter import filedialog as FileDialog

#librerias personales
from valores import *


# Define la ventana principal de la aplicación





raiz = Tk()
raiz.geometry('300x200') # anchura x altura

#raiz.title('Aplicación')


direccionIp= StringVar()
NomArchivo=StringVar()


# frame del archivo
frame1 = Frame(raiz)
frame1.pack()
# frame1.config(relief="sunken")
frame1.config(bd=15)


def buscar():
    fichero = FileDialog.askopenfilename(title="Abrir un fichero",
                                         filetypes=(("Fichero de texto", "*.txt"),))
    # se usa el metodo str para convertir la direccion en una varible tipo String
    cadenafichero = str(fichero)
    val.Archivo= cadenafichero
    NomArchivo.set(val.Archivo)
    # Nota: falla si no le damos una direccion de Archivo valida
    if val.Archivo !="":
        print(val.Archivo)
    else:
        print("Dirección de Archivo no válida")
        NomArchivo.set("")

def enviar():
    if direccionIp.get()!="":
        print(direccionIp.get())
        #print(val.is_valid_ipv4_address(direccionIp.get()))
        if val.is_valid_ipv4_address(direccionIp.get())==True and NomArchivo!="":
            print("direccion valida")
        else:
            print("direccion no valida")
            #aqui debe mandar una alerta de que no se ingreso bien la direccion ip

    else:
        print("caja vacia")





## son los witgests para la caja de la ubicacion del archivo
BuscarArchCaja = Entry(frame1, textvar=NomArchivo, justify="right", width=40).pack()
buscarArch = Button(frame1, text="Buscar Archivo", command=buscar).pack()

##para la direccion IP

dirccionCaja = ttk.Entry(frame1,textvar= direccionIp ).pack()

EnviarCaja = Button(frame1, text="Enviar", command=enviar).pack()



val = valores()
raiz.mainloop()
