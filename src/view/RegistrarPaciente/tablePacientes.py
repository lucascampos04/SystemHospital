from tkinter import Tk, Label, Entry, Button, Frame, ttk, messagebox

from src.Model.query.pacienteQuery import listar_pacientes
from src.view.RegistrarPaciente.RemoverPaciente import WindowPacienteRemove
from src.view.RegistrarPaciente.pacienteAtualizar import WindowUpdatePacientes
from src.view.RegistrarPaciente.PacienteAdd import WindowAddPaciente

global tabela_pacientes, pacientes

cinxa = "#5e4f4c"

def router_addPaciente():
    WindowAddPaciente()

def router_RemovePaciente():
    WindowPacienteRemove()

def router_attPaciente():
    WindowUpdatePacientes()
def atualizar_tabela():
    pacientes = listar_pacientes()
    tabela_pacientes.delete(*tabela_pacientes.get_children())
    for paciente in pacientes:
        tabela_pacientes.insert("", "end", values=(paciente[0], paciente[1], paciente[2], paciente[5], paciente[4], paciente[3]))

def preencher_tabela():
    global tabela_pacientes
    pacientes = listar_pacientes()

    for paciente in pacientes:
        tabela_pacientes.insert("", "end", values=(paciente[0], paciente[1], paciente[2], paciente[5], paciente[4], paciente[3]))

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def WindowTablePaciente():
    global tabela_pacientes, pacientes

    window = Tk()
    window.title("Pacientes")
    center_window(window, 800, 580)
    window.resizable(False, False)

    frameT = Frame(window, width=1080, height=100, bg="blue")
    frameT.grid(row=0, column=0)

    frameM = Frame(window, width=1080, height=500)
    frameM.grid(row=1, column=0)

    title_pacientes = Label(frameT, text="TABELA DE PACIENTES", font=("Arial 40 bold"), bg="blue", fg="white")
    title_pacientes.place(x=100, y=20)

    # Tabela
    tabela_pacientes = ttk.Treeview(frameM, columns=("ID", "NOME", "CPF", "RG", "EMAIL", "TELEFONE"), show="headings")
    tabela_pacientes.heading('#1', text="ID", anchor='center')
    tabela_pacientes.heading('#2', text="NOME", anchor='center')
    tabela_pacientes.heading('#3', text="CPF", anchor='center')
    tabela_pacientes.heading('#4', text="RG", anchor='center')
    tabela_pacientes.heading('#5', text="EMAIL", anchor='center')
    tabela_pacientes.heading('#6', text="TELEFONE", anchor='center')

    # Ajustar a largura das colunas
    tabela_pacientes.column('#1', width=100, anchor='center')
    tabela_pacientes.column('#2', width=100, anchor='center')
    tabela_pacientes.column('#3', width=100, anchor='center')
    tabela_pacientes.column('#4', width=120, anchor='center')
    tabela_pacientes.column('#5', width=120, anchor='center')
    tabela_pacientes.column('#6', width=120, anchor='center')

    style = ttk.Style()
    style.configure("Treeview", rowheight=30, borderwidth=1)

    tabela_pacientes.place(x=80, y=50)
    preencher_tabela()

    btnAdd = Button(frameM, text="Adicionar", font=("Arial 15 bold"), bg="green", fg="white", command=router_addPaciente)
    btnAdd.place(x=80, y=400)

    btnRemove = Button(frameM, text="Remove", font=("Arial 15 bold"), bg="red", fg="white",command=router_RemovePaciente)
    btnRemove.place(x=210, y=400)

    btnAtualizar = Button(frameM, text="Atualizar Tabela", font=("Arial 15 bold"), command=atualizar_tabela, bg=cinxa, fg="white")
    btnAtualizar.place(x=575, y=400)

    btnEditar = Button(frameM, text="Editar", font=("Arial 15 bold"), bg="blue", fg="white", command=router_attPaciente)
    btnEditar.place(x=350, y=400)

    window.mainloop()



