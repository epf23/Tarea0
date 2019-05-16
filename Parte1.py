import csv
from tkinter import *

window = Tk()
window.title('Programa Push')

#RNC
L1 = Label(window, text='RNC')
L1.grid(row=3, column=0)
var1 = str()
textbox1 = Entry(window, textvariable=var1)
textbox1.grid(row=3, column=1)
textbox1.focus_set()

#Numero de cuenta
L2 = Label(window, text='Numero de cuenta')
L2.grid(row=4, column=0)
var2 = str()
textbox2 = Entry(window, textvariable=var2)
textbox2.grid(row=4, column=1)
textbox2.focus_set()

#Fecha de pago
L3 = Label(window, text='Fecha de pago')
L3.grid(row=5, column=0)
var3 = str()
textbox3 = Entry(window, textvariable=var3)
textbox3.grid(row=5, column=1)
textbox3.focus_set()

#Fecha de transferencia
L4 = Label(window, text='Fecha de transferencia')
L4.grid(row=6, column=0)
var4 = str()
textbox4 = Entry(window, textvariable=var4)
textbox4.grid(row=6, column=1)
textbox4.focus_set()

#Numero de transaccion
L5 = Label(window, text='Numero de Transaccion')
L5.grid(row=8, column=0)
var5 = str()
textbox5 = Entry(window, textvariable=var5)
textbox5.grid(row=8, column=1)
textbox5.focus_set()

#Numero de cuenta
L6 = Label(window, text='Numero de cuenta')
L6.grid(row=9, column=0)
var6 = str()
textbox6 = Entry(window, textvariable=var6)
textbox6.grid(row=9, column=1)
textbox6.focus_set()

#Monto
L7 = Label(window, text='Monto')
L7.grid(row=10, column=0)
var7 = str()
textbox7 = Entry(window, textvariable=var7)
textbox7.grid(row=10, column=1)
textbox7.focus_set()

#Motivo
L8 = Label(window, text='Motivo')
L8.grid(row=11, column=0)
var8 = str()
textbox8 = Entry(window, textvariable=var8)
textbox8.grid(row=11, column=1)
textbox8.focus_set()

#Cantidad de transacciones
L9 = Label(window, text='Transacciones')
L9.grid(row=13, column=0)
var9 = str()
textbox9 = Entry(window, textvariable=var9)
textbox9.grid(row=13, column=1)
textbox9.focus_set()

#Monto Total
L10 = Label(window, text='Total')
L10.grid(row=14, column=0)
var10 = str()
textbox10 = Entry(window, textvariable=var10)
textbox10.grid(row=14, column=1)
textbox10.focus_set()

def escribir():
    fh = open("archivo.txt", "w")
    datos = textbox1.get()+","+textbox2.get()+","+textbox3.get()+","+textbox4.get()+","+textbox5.get()+","+textbox6.get()+","+textbox7.get()+","+textbox8.get()+","+textbox9.get()+","+textbox10.get()
    print(datos)
    fh.write(datos)
    fh.close()


b = Button(window, text="Ingresar", command=escribir)
b.grid(row= 15, column= 0)
window.mainloop()