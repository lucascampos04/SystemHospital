import tkinter as tk
from tkinter import Label, Entry, Button, Frame, ttk

from src.Model.query.medicosQuery import add_medico

global nome_entry, cpf_entry, email_entry, rg_entry, telefone_entry, formacao_combobox, setor_combobox, window

# Dicionário mapeando formações a setores correspondentes
formacao_setor_mapping = {
    "Medicina Geral": ["Setor 1", "Setor 2", "Setor 3"],
    "Cardiologia": ["Cardiologia Setor 1", "Cardiologia Setor 2", "Cardiologia Setor 3"],
    "Ortopedia": ["Ortopedia Setor 1", "Ortopedia Setor 2", "Ortopedia Setor 3"],
    "Dermatologia": ["Dermatologia Setor 1", "Dermatologia Setor 2"],
    "Neurologia": ["Neurologia Setor 1", "Neurologia Setor 2", "Neurologia Setor 3"],
    "Ginecologia": ["Ginecologia Setor 1", "Ginecologia Setor 2"],
    "Pediatria": ["Pediatria Setor 1", "Pediatria Setor 2"],
    "Urologia": ["Urologia Setor 1", "Urologia Setor 2"],
    "Oftalmologia": ["Oftalmologia Setor 1", "Oftalmologia Setor 2"],
    "Oncologia": ["Oncologia Setor 1", "Oncologia Setor 2", "Oncologia Setor 3"],
    "Endocrinologia": ["Endocrinologia Setor 1", "Endocrinologia Setor 2"],
    "Reumatologia": ["Reumatologia Setor 1", "Reumatologia Setor 2", "Reumatologia Setor 3"],
    "Infectologia": ["Infectologia Setor 1", "Infectologia Setor 2"],
}


def adicionar_medico():
    nome = nome_entry.get()
    cpf = cpf_entry.get()
    email = email_entry.get()
    rg = rg_entry.get()
    telefone = telefone_entry.get()
    formacao = formacao_combobox.get()
    setor = setor_combobox.get()

    verificacao = add_medico(nome, cpf, email, rg, telefone, formacao, setor)

def update_setor_combobox(event):
    formacao_selecionada = formacao_combobox.get()
    setores = formacao_setor_mapping.get(formacao_selecionada, [])
    setor_combobox['values'] = setores
    setor_combobox.set("")

def WindowAddMedico():
    global nome_entry, cpf_entry, email_entry, rg_entry, telefone_entry, formacao_combobox, setor_combobox, window
    window = tk.Tk()
    window.title("Adicionar Médico")
    window.geometry("400x400")
    window.resizable(False, False)

    title = Label(window, text="Adicionar", font=("Arial 25 bold"))
    title.place(x=100, y=10)

    nome_label = Label(window, text="Nome:", font=("Arial 15 bold"))
    nome_label.place(x=30, y=60)
    nome_entry = Entry(window)
    nome_entry.place(x=150, y=65)

    cpf_label = Label(window, text="CPF:", font=("Arial 15 bold"))
    cpf_label.place(x=30, y=95)
    cpf_entry = Entry(window)
    cpf_entry.place(x=150, y=100)

    email_label = Label(window, text="Email:", font=("Arial 15 bold"))
    email_label.place(x=30, y=125)
    email_entry = Entry(window)
    email_entry.place(x=150, y=130)

    rg_label = Label(window, text="RG:", font=("Arial 15 bold"))
    rg_label.place(x=30, y=160)
    rg_entry = Entry(window)
    rg_entry.place(x=150, y=165)

    telefone_label = Label(window, text="Telefone:", font=("Arial 15 bold"))
    telefone_label.place(x=30, y=195)
    telefone_entry = Entry(window)
    telefone_entry.place(x=150, y=200)

    formacao_label = Label(window, text="Formação:", font=("Arial 15 bold"))
    formacao_label.place(x=30, y=225)
    formacao_values = list(formacao_setor_mapping.keys())

    formacao_combobox = ttk.Combobox(window, values=formacao_values)
    formacao_combobox.place(x=150, y=230)
    formacao_combobox.bind("<<ComboboxSelected>>", update_setor_combobox)

    setor_label = Label(window, text="Setor:", font=("Arial 15 bold"))
    setor_label.place(x=30, y=255)
    setor_values = []

    setor_combobox = ttk.Combobox(window, values=setor_values)
    setor_combobox.place(x=150, y=260)

    btn_add = Button(window, text="Adicionar", font=("Ivy 20 bold"), command=adicionar_medico)
    btn_add.place(x=120, y=300)

    window.bind('<Return>', lambda event=None: btn_add.invoke())
    window.mainloop()

WindowAddMedico()
