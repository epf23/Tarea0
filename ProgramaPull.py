#Importar Clases
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
#Importar Clases

#Inicializar variables
txtvar1=""
txtvar2=""
txtvar3=""
txtvar4=""
txtvar5=""
txtvar6=""
txtvar7=""
txtvar8=""
txtvar9=""
txtvar10=""
RNCEmp=""
Numero_Cuenta_Transferencia=""
Fecha_Pago=""
Fecha_Transferencia=""
Numero_Transaccion=""
Numero_Cuenta_Deposito=""
Monto=""
Motivo=""
Cantidad_Transacciones=""
Monto_Total=""
#Inicializar variables

window=Tk()
window.title("Programa Pull")
messagebox.showinfo("Programa Pull", "Elija el archivo que desee utilizar.")

#Selección de Archivo
nombre_archivo = askopenfilename()
obj_Archivo = open(nombre_archivo,"r")
string_archivo = obj_Archivo.readline()
s= string_archivo.split(",")
#Selección de Archivo

#Asignación de Valores
RNCEmp = s[0]
Numero_Cuenta_Transferencia = s[1]
Fecha_Pago = s[2]
Fecha_Transferencia = s[3]
Numero_Transaccion = s[4]
Numero_Cuenta_Deposito = s[5]
Monto = s[6]
Motivo = s[7]
Cantidad_Transacciones = s[8]
Monto_Total = s[9]
#Asignación de Valores

## Encabezado
l1=Label(window, text="Encabezado", font='Timesnewroman 11 bold')
l1.grid(row=2,column=0)
#RNC de la Empresa
name1=Entry(window, textvariable=txtvar1, font='Timesnewroman 9 bold')
name1.grid(row=3,column=1)
name1.insert(0, RNCEmp)
name1.config(state='disabled')
l2=Label(window, text="RNC De la empresa")
l2.grid(row=3,column=0)
#Número de Cuenta
name2=Entry(window, textvariable=txtvar2, font='Timesnewroman 9 bold')
name2.grid(row=4,column=1)
name2.insert(0, Numero_Cuenta_Transferencia)
name2.config(state='disabled')
l3=Label(window, text="Número de Cuenta")
l3.grid(row=4,column=0)
#Fecha de Pago
name3=Entry(window, textvariable=txtvar3, font='Timesnewroman 9 bold')
name3.grid(row=5,column=1)
name3.insert(0, Fecha_Pago)
name3.config(state='disabled')
l4=Label(window, text="Fecha de Pago")
l4.grid(row=5,column=0)
#Fecha de Transferencia
name4=Entry(window, textvariable=txtvar4, font='Timesnewroman 9 bold')
name4.grid(row=6,column=1)
name4.insert(0, Fecha_Transferencia)
name4.config(state='disabled')
l5=Label(window, text="Fecha de Transferencia")
l5.grid(row=6,column=0)
## Encabezado

## Detalle
l6=Label(window, text="Detalle", font='Timesnewroman 11 bold')
l6.grid(row=7,column=0)
#Número de Transacción
name5=Entry(window, textvariable=txtvar5, font='Timesnewroman 9 bold')
name5.grid(row=8,column=1)
name5.insert(0, Numero_Transaccion)
name5.config(state='disabled')
l7=Label(window, text="Número de Transacción")
l7.grid(row=8,column=0)
#Número de Cuenta
name6=Entry(window, textvariable=txtvar6, font='Timesnewroman 9 bold')
name6.grid(row=9,column=1)
name6.insert(0, Numero_Cuenta_Deposito)
name6.config(state='disabled')
l8=Label(window, text="Número de cuenta")
l8.grid(row=9,column=0)
#Monto
name7=Entry(window, textvariable=txtvar7, font='Timesnewroman 9 bold')
name7.grid(row=10,column=1)
name7.insert(0, Monto)
name7.config(state='disabled')
l9=Label(window, text="Monto")
l9.grid(row=10,column=0)
#Motivo
name8=Entry(window, textvariable=txtvar8, font='Timesnewroman 9 bold')
name8.grid(row=11,column=1)
name8.insert(0, Motivo)
name8.config(state='disabled')
l10=Label(window, text="Motivo")
l10.grid(row=11,column=0)
## Detalle

## Sumario
l11=Label(window, text="Sumario", font='Timesnewroman 11 bold')
l11.grid(row=12,column=0)
#Cantidad de Transacciones
name9=Entry(window, textvariable=txtvar9, font='Timesnewroman 9 bold')
name9.grid(row=13,column=1)
name9.insert(0, Cantidad_Transacciones)
name9.config(state='disabled')
l12=Label(window, text="Cantidad de Transacciones")
l12.grid(row=13,column=0)
#Monto Total
name10=Entry(window, textvariable=txtvar10, font='Timesnewroman 9 bold')
name10.grid(row=14,column=1)
name10.insert(0, Monto_Total)
name10.config(state='disabled')
l13=Label(window, text="Monto Total")
l13.grid(row=14,column=0)
## Sumario

window.mainloop()
