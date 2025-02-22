import tkinter as tk
from tkinter import messagebox

# Función para validar y enviar el formulario
def enviar_formulario():
    nombre = entry_nombre.get()
    correo = entry_correo.get()
    edad = entry_edad.get()
    escolaridad = escolaridad_var.get()

    # Validación de campos
    if not nombre:
        messagebox.showerror("Error", "El nombre no puede estar vacío.")
        return

        # Verificar que el nombre no contenga números
    if not nombre.isalpha():
        messagebox.showerror("Error", "El nombre no puede contener números.")
        return

    if "@" not in correo or "." not in correo:
        messagebox.showerror("Error", "El correo debe tener un formato válido.")
        return

    if not edad.isdigit():
        messagebox.showerror("Error", "La edad debe ser un número.")
        return

    if escolaridad == "" :
        messagebox.showerror("Error", "Debe seleccionar la escolaridad máxima.")
        return

    # Si todo es correcto, mostrar un mensaje de éxito
    messagebox.showinfo("Éxito", "Formulario enviado correctamente.")
    limpiar_formulario()


# Función para limpiar los campos
def limpiar_formulario():
    entry_nombre.delete(0, tk.END)
    entry_correo.delete(0, tk.END)
    entry_edad.delete(0, tk.END)
    escolaridad_var.set("")

def centrar_ventana(ventana, ancho, alto,desplazamiento_y=0):
    # Obtener las dimensiones de la pantalla
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    # Calcular las coordenadas para centrar la ventana
    posicion_x = (pantalla_ancho - ancho) // 2
    posicion_y = (pantalla_alto - alto) // 2 - desplazamiento_y

    # Establecer la geometría (tamaño + posición)
    ventana.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.configure(bg="lightgreen")

# Establecer el tamaño de la ventana
ancho = 320
alto = 155

# Llamar a la función para centrar la ventana
centrar_ventana(ventana, ancho, alto,desplazamiento_y=200)

# Etiquetas y campos de texto
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, sticky="e")
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Correo:").grid(row=1, column=0, sticky="e")
entry_correo = tk.Entry(ventana)
entry_correo.grid(row=1, column=1)

tk.Label(ventana, text="Edad:").grid(row=2, column=0, sticky="e")
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=2, column=1)

tk.Label(ventana, text="Escolaridad máxima:").grid(row=3, column=0, sticky="e")
escolaridad_var = tk.StringVar()
opciones_escolaridad = tk.OptionMenu(ventana, escolaridad_var, "Primaria", "Secundaria", "Preparatoria", "Universidad")
opciones_escolaridad.grid(row=3, column=1)

# Botones de enviar y limpiar
btn_enviar = tk.Button(ventana, text="Enviar", command=enviar_formulario)
btn_enviar.grid(row=4, column=0)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_formulario)
btn_limpiar.grid(row=4, column=1)

# Ejecutar la ventana
ventana.mainloop()