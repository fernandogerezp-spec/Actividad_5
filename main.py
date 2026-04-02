import tkinter as tk

def capturar_credenciales():
    print("Botón presionado")

ventana = tk.Tk()
ventana.title("Login")
ventana.geometry("300x200")


tk.Label(ventana, text="Usuario:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_usuario = tk.Entry(ventana)
entry_usuario.grid(row=0, column=1, padx=10, pady=5)


tk.Label(ventana, text="Contraseña:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_password = tk.Entry(ventana, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)


boton = tk.Button(ventana, text="Validar Acceso", command=capturar_credenciales)
boton.grid(row=2, column=0, columnspan=2, pady=10)


label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=3, column=0, columnspan=2)
ventana.mainloop()
