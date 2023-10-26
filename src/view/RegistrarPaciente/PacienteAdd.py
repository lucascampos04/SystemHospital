from tkinter import Tk, Label, Entry, Button, Frame, ttk
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
        return True
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


def WindowAddPaciente():
    global nome_entry, cpf_entry, email_entry, rg_entry, telefone_entry, window

    window = Tk()
    window.title("Adicionar Paciente")
    center_window(window, 790, 350)
    window.resizable(False, False)

    title = Label(window, text="Adicionar", font=("Arial 30 bold"))
    title.place(x=250, y=10)

    nome_label = Label(window, text="Nome : ", font=("Arial 15 bold"))
    nome_label.place(x=30, y=80)
    nome_entry = Entry(window, font=("Ivy 15 bold"), bd=2)  # Altere o valor de "bd" para a largura da borda desejada
    nome_entry.place(x=150, y=85)

    cpf_label = Label(window, text="Cpf : ", font=("Arial 15 bold"))
    cpf_label.place(x=30, y=130)
    cpf_entry = Entry(window, font=("Ivy 15 bold"), bd=2)
    cpf_entry.place(x=150, y=135)

    email_label = Label(window, text="Email : ", font=("Arial 15 bold"))
    email_label.place(x=30, y=180)
    email_entry = Entry(window, font=("Ivy 15 bold"), bd=2)
    email_entry.place(x=150, y=185)

    rg_label = Label(window, text="Rg : ", font=("Arial 15 bold"))
    rg_label.place(x=420, y=130)
    rg_entry = Entry(window, font=("Ivy 15 bold"), bd=2)
    rg_entry.place(x=530, y=135)

    telefone_label = Label(window, text="Telefone : ", font=("Arial 15 bold"))
    telefone_label.place(x=420, y=80)
    telefone_entry = Entry(window, font=("Ivy 15 bold"), bd=2)
    telefone_entry.place(x=530, y=85)

    btn_add = Button(window, text="Adicionar", font=("Ivy 20 bold"), command=adicionar_paciente, bg="blue", fg="white",
                     width=18, activebackground="blue", activeforeground="white")
    btn_add.place(x=250, y=250)

    window.bind('<Return>', lambda event=None: btn_add.invoke())
    window.mainloop()

