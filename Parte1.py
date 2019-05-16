import csv
from tkinter import *

window = Tk()
window.title('Programa Push')
Label(window, text='Banco Popular').pack(pady=20,padx=50)

#RNC
Label(window, text='RNC').pack(pady=10,padx=50)
var1 = str()
textbox = Entry(window, textvariable=var1)
textbox.pack(pady=10, padx=10)

#Numero de cuenta
Label(window, text='Numero de cuenta').pack(pady=20,padx=50)
var2 = str()
textbox = Entry(window, textvariable=var2)
textbox.pack(pady=10, padx=10)

#Fecha de pago
Label(window, text='Fecha de pago').pack(pady=20,padx=50)
var3 = str()
textbox = Entry(window, textvariable=var3)
textbox.pack(pady=10, padx=10)

#Fecha de transferencia
Label(window, text='Fecha de transferencia').pack(pady=20, padx=50)
var4 = str()
textbox = Entry(window, textvariable=var4)
textbox.pack(pady=10, padx=10)


def escribir():
    fh = open("archivo.csv", "w")
    string = 'var1, var2, var3, var4'
    datos = string
    fh.write(datos)
    fh.close()


b = Button(window, text="Ingresar", command=escribir)
b.pack()

window.mainloop()