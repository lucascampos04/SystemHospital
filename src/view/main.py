from tkinter import Tk, Label, Entry, Button
from PIL import Image, ImageTk

from src.view.RegistrarPaciente.tablePacientes import WindowTablePaciente
from src.view.RegistrarConsulta.tableConsultas import WindowTableConsultas
from src.view.RegistrarMedico.tableMedicos import WindowTableMedicos

def set_window_background(window, gradient_color1, gradient_color2):
    width, height = window.winfo_width(), window.winfo_height()
    image = Image.new("RGB", (width, height))
    for y in range(height):
        r = int(gradient_color1[0] + (y / height) * (gradient_color2[0] - gradient_color1[0]))
        g = int(gradient_color1[1] + (y / height) * (gradient_color2[1] - gradient_color1[1]))
        b = int(gradient_color1[2] + (y / height) * (gradient_color2[2] - gradient_color1[2]))
        for x in range(width):
            image.putpixel((x, y), (r, g, b))
    photo = ImageTk.PhotoImage(image)
    label = Label(window, image=photo)
    label.image = photo
    label.place(x=0, y=0, relwidth=1, relheight=1)

def router_paciente():
    WindowTablePaciente()
def router_medicos():
    WindowTableMedicos()
def router_consultas():
    WindowTableConsultas()

azul = "#66adbd"
verde = "#32a852"
roxo =  "#5c5685"
def WindowMain():
    window = Tk()
    window.geometry("500x500")
    window.title("Pagina Inicial")
    window.resizable(False, False)

    btnPaciente = Button(window, text="PACIENTES", font=("Arial 20 bold"), command=router_paciente, bg=verde, fg="white")
    btnPaciente.place(x=40, y=180)

    btnMedico = Button(window, text="MEDICOS", font=("Arial 20 bold"), command=router_medicos, bg=azul, fg="white")
    btnMedico.place(x=270, y=180)

    btnConsultas = Button(window, text="CONSULTAS", font=("Arial 20 bold"), command=router_consultas, bg=roxo, fg="white")
    btnConsultas.place(x=150, y=250)

    window.mainloop()

WindowMain()