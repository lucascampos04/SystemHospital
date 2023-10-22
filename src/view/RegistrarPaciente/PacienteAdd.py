from tkinter import Tk, Label, Entry, Button, Frame
from src.Model.query.pacienteQuery import add_paciente


global nome_entry, cpf_entry, email_entry, rg_entry, telefone_entry, window

def adicionar_paciente():
    nome = nome_entry.get()
    cpf = cpf_entry.get()
    email = email_entry.get()
    rg = rg_entry.get()
    telefone = telefone_entry.get()

    verificacao = add_paciente(nome, cpf, email, rg, telefone)

    if verificacao:
        window.destroy()
        return True;



def WindowAddPaciente():
    global nome_entry, cpf_entry, email_entry, rg_entry, telefone_entry, window

    window = Tk()
    window.title("Adicionar Paciente")
    window.geometry("400x300")
    window.resizable(False, False)

    title = Label(window, text="Adicionar", font=("Arial 25 bold"))
    title.place(x=100, y=10)

    nome_label = Label(window, text="Nome : ", font=("Arial 15 bold"))
    nome_label.place(x=30, y=60)
    nome_entry = Entry(window)
    nome_entry.place(x=150, y=65)

    cpf_label = Label(window, text="Cpf : ", font=("Arial 15 bold"))
    cpf_label.place(x=30, y=95)
    cpf_entry = Entry(window)
    cpf_entry.place(x=150, y=100)

    email_label = Label(window, text="Email : ", font=("Arial 15 bold"))
    email_label.place(x=30, y=125)
    email_entry = Entry(window)
    email_entry.place(x=150, y=130)

    rg_label = Label(window, text="Rg : ", font=("Arial 15 bold"))
    rg_label.place(x=30, y=160)
    rg_entry = Entry(window)
    rg_entry.place(x=150, y=165)

    telefone_label = Label(window, text="Telefone : ", font=("Arial 15 bold"))
    telefone_label.place(x=30, y=195)
    telefone_entry = Entry(window)
    telefone_entry.place(x=150, y=200)

    btn_add = Button(window, text="Adicionar", font=("Ivy 20 bold"), command=adicionar_paciente)
    btn_add.place(x=120, y=240)

    window.bind('<Return>', lambda event=None: btn_add.invoke())
    window.mainloop()
