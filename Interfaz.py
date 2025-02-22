import tkinter as tk

class VentanaEventos:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("Eventos de Mouse y Teclado")
        self.windows.geometry("300x200")

        # Etiqueta para mostrar eventos
        self.label = tk.Label(self.windows, text="Esperando eventos...", font=("Arial", 14))
        self.label.pack(pady=20)

        # Configuración del evento de clic del ratón
        self.windows.bind("<Button-1>", self.clic_mouse)  # Clic derecho
        self.windows.bind("<Button-2>", self.clic_izquierdo)  # Clic izquierdo
        self.windows.bind("<Motion>", self.movimiento_mouse)  # Movimiento del ratón
        self.windows.bind("<Double-1>", self.doble_clic)  # Doble clic

        # Configuración de eventos del teclado
        self.windows.bind("<KeyPress>", self.tecla_presionada)
        self.windows.bind("<space>", self.limpiar_texto)  # Barra espaciadora

        # Variable para el color de fondo
        self.color_fondo = "lightgreen"
        self.windows.config(bg=self.color_fondo)

    def clic_mouse(self, event):
        texto = f"Clic derecho en ({event.x}, {event.y})"
        self.label.config(text=texto)

    def clic_izquierdo(self, event):
        texto = f"Clic izquierdo en ({event.x}, {event.y})"
        self.label.config(text=texto)

    def movimiento_mouse(self, event):
        texto = f"Moviendo mouse a ({event.x}, {event.y})"
        self.label.config(text=texto)

    def doble_clic(self, event):
        texto = f"Doble clic en ({event.x}, {event.y})"
        self.label.config(text=texto)

    def tecla_presionada(self, event):
        texto = f"Tecla presionada: {event.char}"
        self.label.config(text=texto)

    def limpiar_texto(self, event):
        # Limpiar el texto de la etiqueta cuando se presiona la barra espaciadora
        self.label.config(text="Texto limpiado")


# Crear la ventana principal
Windows = tk.Tk()
ventana = VentanaEventos(Windows)

# Ejecutar la ventana
Windows.mainloop()