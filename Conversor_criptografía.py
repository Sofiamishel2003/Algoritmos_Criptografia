# Documentación
# Autor: Sofía Velásquez
# Fecha de creación: 15/06/2024

import math
from os import read
from tkinter import *
from tkinter import filedialog, messagebox, ttk
from typing import Match


class forma(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("500x400")
        self.config(bg="thistle")
        self.lb=Label(self, text="Conversor de binario", font="Arial 15 underline", bg="thistle")
        self.lb.place(x=100,y=10)
        self.lb1=Label(self, text="Valor", font="Arial 10", bg="thistle")
        self.lb1.place(x=50,y=80)
        #self.lb2=Label(self, text="Base", font="Arial 10", bg="thistle")
        #self.lb2.place(x=219,y=80)
        self.c1=Text(self, height = 5, width = 40)
        self.c1.place(x=50,y=100)
        ##self.e1=Entry(self, width=5)
        ##self.e1.place(x=220,y=100)
        self.r1=StringVar()
        self.r2=StringVar()
        self.c2=Text(self,height = 5, width = 40, state=DISABLED)
        self.c2.place(x=50,y=200)
        ##self.e2=Entry(self, width=5, state=DISABLED, textvariable=self.r2)
        ##self.e2.place(x=220,y=150)
        self.combo1=ttk.Combobox(self, width=10)
        self.combo1.place(x=400,y=100)
        self.combo1["values"]=["Binario","Texto"]
        self.combo2=ttk.Combobox(self, width=10)
        self.combo2.place(x=400,y=200)
        self.combo2["values"]=["Binario","Texto"]
        self.bt1=Button(self,text="CONVERTIR", command=self.bina)
        self.bt1.place(x=180,y=300)
        self.mainloop()

    def binario_a_texto(self, binario):
        texto = ""
        binario = binario.replace(" ", "")  # Eliminar espacios si los hay
        for i in range(0, len(binario), 8):
            byte = binario[i:i+8]
            caracter = chr(int(byte, 2))
            texto += caracter
        return texto
    def texto_a_binario(self, texto):
        binario = ""
        for caracter in texto:
            byte = format(ord(caracter), '08b') # Esto convierte un carácter en su representación binaria de 8 bits
            binario += byte + " "
        return binario
    def bina(self):
        self.c2.delete("1.0", "end")
        if(self.combo1.get()=="Binario"):
            n=(self.c1.get("1.0", "end-1c"))
            texto=self.binario_a_texto(n)
            self.r1.set(texto)
            self.c2.config(state='normal')
            self.c2.insert("1.0", texto)
            self.c2.config(state=DISABLED)
        elif(self.combo1.get()=="Texto"): 
            n=(self.c1.get("1.0", "end-1c"))
            binario=self.texto_a_binario(n)
            self.r1.set(binario)
            self.c2.config(state='normal')
            self.c2.insert("1.0", binario)
            self.c2.config(state=DISABLED)

app=forma()
