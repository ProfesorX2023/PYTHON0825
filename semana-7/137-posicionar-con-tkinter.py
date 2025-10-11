import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana princial")


# Cargar la imagen
imagen = Image.open("fondo.png")
imagen = imagen.resize((800,600))
imagen_fondo = ImageTk.PhotoImage(imagen)

# crear un canvas
canvas = tk.Canvas(ventana, width=800, height=600)
canvas.pack(fill='both', expand=True)

# colocar imagen en el canvas
canvas.create_image(400,0, image=imagen_fondo, anchor='n')

# Colocar otros widgets en el canvas
label = tk.Label(ventana, text="Texto en la ventana", bg="white")
label_window = canvas.create_window(400,300, window=label)

# ciclo raiz

ventana.mainloop()