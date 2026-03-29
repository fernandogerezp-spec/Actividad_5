import tkinter as tk
import os
from dotenv import load_dotenv

load_dotenv(".env")

APP_USER = os.getenv("APP_USER")
APP_PASSWORD = os.getenv("APP_PASSWORD")

def capturar_credenciales():
    user = entry_usuario.get()
    password = entry_password.get()
    validar_credenciales(user, password)

def validar_credenciales(usuario, password):
    if usuario == APP_USER and password == APP_PASSWORD:
        mostrar_mensaje("Acceso correcto", "green")
    else:
        mostrar_mensaje("Usuario o contraseña incorrecta", "red")

def mostrar_mensaje(texto, color):
    label_resultado.config(text= texto, fg= color)

ventana = tk.Tk()
ventana.title("Practica 1: Validacion")
ventana.geometry("400x400")

tk.Label(ventana, text= "Usuario:").pack()
entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

tk.Label(ventana, text= "Contraseña:").pack()
entry_password = tk.Entry(ventana)
entry_password.pack()

boton = tk.Button(ventana, text = "Validar Acceso", command=capturar_credenciales)
boton.pack()

label_resultado = tk.Label(ventana, text = "")
label_resultado.pack()

ventana.mainloop()