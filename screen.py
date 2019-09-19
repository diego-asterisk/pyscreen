#!/usr/bin/env python3
from tkinter import *
from tkinter import filedialog, messagebox
import pyautogui


def captura():
    captura = pyautogui.screenshot()
    captura.save(texto.get())
    messagebox.showinfo("Exito", "Captura Guardada")

def navegar():
    archivoNombre = filedialog.asksaveasfilename(title="Guardar como",
                                                        initialdir="~/Documentos",
                                                        defaultextension=".png",
                                                        filetypes=(("Archivo Png", "*.png"), ("Todos Archivos", "*")))
    texto.delete(0,END)
    texto.insert(INSERT, archivoNombre)


ventana = Tk()
ventana.title("Copy Screen")

guardar = Label(ventana, text="Guardar como: ", font=("", 10, "bold"))
guardar.grid(row=1, column=0, pady=5, padx=5)
texto = Entry(ventana, width=30)
texto.grid(row=1, column=1, pady=5, padx=5)
boton = Button(ventana, text="Explorar", width=10, command=navegar)
boton.grid(row=1, column=2, pady=5, padx=5)
capturar = Button(ventana, text="Captura", width=10, command=captura)
capturar.grid(row=2, column=1, pady=5, padx=5, stick=W+E)

ventana.mainloop()
