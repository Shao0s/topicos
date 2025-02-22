import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    mensaje=entrada.get()
    messagebox.showinfo("mensaje",mensaje)

def cerrar_app():
    ventana.destroy()

#crear ventana
ventana=tk.Tk()
ventana.title("Elementos basicos")
ventana.geometry("300x200")
ventana.configure(bg="lightgreen")

#Agregar etiqueta
etiqueta=tk.Label(ventana,text="Bienvenido",font=("Arial",14),bg="lightblue")
etiqueta.pack(pady=10)

#Agregar cuadro de texto
entrada = tk.Entry(ventana,width=30)
entrada.pack(pady=5)

#Boton
boton_mostrar =tk.Button(ventana,text="Mostrar mensaje", command=mostrar_mensaje)
boton_mostrar.pack(pady=10)

#Exit
boton_cerrar=tk.Button(ventana,text="Salir",command=cerrar_app)
boton_cerrar.pack(pady=5)

#Iniciar el bucle de la app
ventana.mainloop()