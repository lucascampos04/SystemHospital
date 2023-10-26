from tkinter import Tk, Label, Frame, Button, Entry

from src.view.RegistrarPaciente.tablePacientes import WindowTablePaciente
from src.view.RegistrarConsulta.tableConsultas import WindowTableConsultas
from src.view.RegistrarMedico.tableMedicos import WindowTableMedicos

azul = "#2f5694"
azul_poggers = "#080d8a"
verde = "#15800f"
vermelho = "#ff0000"

def router_paciente():
    WindowTablePaciente()
def router_medicos():
    WindowTableMedicos()
def router_consultas():
    WindowTableConsultas()


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def main():
    window = Tk()
    window.title("Janela Centralizada")
    center_window(window, 800, 400)

    # Frames
    frame_top = Frame(window, width=800, height=120, bg=azul)
    frame_top.grid(row=0, column=0)

    frame_main = Frame(window, width=800, height=380)
    frame_main.grid(row=1, column=0)

    # titule
    title = Label(frame_top, text="Hospital.com", bg=azul, fg="white", font=("Ivy 60 bold"))
    title.place(x=200, y=10)

    # Botões e Labels
    btn_add_paciente = Button(frame_main,
                              text="PACIENTES",
                              font=("Arial 25 bold"),
                              relief='ridge',
                              bg=verde,
                              fg="white",
                              activebackground=verde,
                              activeforeground="white",
                              command=router_paciente)  # Usando 'command' para definir a função a ser chamada
    btn_add_paciente.place(x=40, y=70)

    btn_add_consultas = Button(frame_main,
                              text="CONSULTAS",
                              font=("Arial 25 bold"),
                              relief='ridge',
                              bg="white",
                              fg=azul_poggers,
                              activeforeground=azul_poggers,
                              command=router_consultas)  # Usando 'command' para definir a função a ser chamada
    btn_add_consultas.place(x=300, y=70)

    btn_add_medicos = Button(frame_main,
                               text="MÉDICOS",
                               font=("Arial 25 bold"),
                               relief='ridge',
                               bg=azul_poggers,
                               fg='white',
                               activeforeground="white",
                               activebackground=azul_poggers,
                               command=router_medicos)  # Usando 'command' para definir a função a ser chamada
    btn_add_medicos.place(x=570, y=70)

    window.mainloop()

main()
