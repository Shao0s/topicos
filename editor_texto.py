import tkinter as tk
from tkinter import filedialog, simpledialog, Menu

def abrir():
    pass  # Aquí irá el codigo para abrir un archivo

def salvar():
    pass  # Aquí irá el codigo para guardar el archivo

def limpiar_texto():
    text_area.delete(1.0, tk.END)

def cambiar_color():
    pass  # Aquí irá el codigo para cambiar el color del texto

def buscar_y_remplazar():
    pass  # Aquí irá el codigo para buscar y reemplazar

# Crear la ventana principal
Ventana = tk.Tk()
Ventana.title("Editor de Texto")
Ventana.geometry("600x400")

# Crear un área de texto
text_area = tk.Text(Ventana, wrap="word", font=("Arial", 12))
text_area.pack(expand=1, fill="both")

# Crear la barra de menú
menu_bar = Menu(Ventana)
Ventana.config(menu=menu_bar)

# Menú Archivo
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Abrir", accelerator="Ctrl+O", command=abrir())
file_menu.add_command(label="Guardar", accelerator="Ctrl+S", command=salvar())
file_menu.add_command(label="Borrar", accelerator="Ctrl+D", command=limpiar_texto())
menu_bar.add_cascade(label="Archivo", menu=file_menu)

# Menú Editar
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cambiar color de texto", command=cambiar_color())
edit_menu.add_command(label="Buscar y Reemplazar", command=buscar_y_remplazar())
menu_bar.add_cascade(label="Editar", menu=edit_menu)

# Atajos de teclado
Ventana.bind("<Control-o>", lambda event: abrir())
Ventana.bind("<Control-s>", lambda event: salvar())
Ventana.bind("<Control-d>", lambda event: limpiar_texto())

Ventana.mainloop()
