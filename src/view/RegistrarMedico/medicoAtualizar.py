from tkinter import Label, Entry, Button, Frame, ttk, Tk, messagebox
from tkinter.simpledialog import askstring

from src.Model.query.medicosQuery import atualizar_tabelaID, atualizar_coluna_consulta


global consultas, tabela_medicos, id_valor_entry, idV, coluna_combobox, atualizar_button, colunas

colunas = ["nome", "cpf", "rg", "email", "telefone", "formacao", "setor"]

def listar_tabela():
    id = id_valor_entry.get()
    colunavalue = coluna_combobox.get()

    if not id or not colunavalue:
        messagebox.showerror("Erro", "Por favor, preencha os campos ID e Coluna.")
        return

    consulta = atualizar_tabelaID(id)

    for row in tabela_medicos.get_children():
        tabela_medicos.delete(row)

    if consulta:
        for row in consulta:
            tabela_medicos.insert("", "end", values=row)

        if colunavalue in colunas:
            while True:
                newValueColumn = askstring("Novo valor", f"Altere o valor da coluna '{colunavalue}':")
                if newValueColumn is None:
                    break
                elif newValueColumn.strip():
                    atualizar_coluna_consulta(id, colunavalue, newValueColumn)
                    listar_tabela()
                    break
    else:
        messagebox.showerror("Erro", "Nenhuma consulta encontrada com o ID fornecido")

def atualizar_tabela():
    listar_tabela()

def WindowUpdateMedico():
    global coluna_combobox, id_valor_entry, window, consultas, tabela_medicos, idV, atualizar_button

    window = Tk()
    window.title("Atualizar Consulta")
    window.geometry("800x400")
    window.resizable(False, False)

    title = Label(window, text="Atualizar Consulta", font=("Arial 20 bold"))
    title.place(x=300, y=10)

    coluna_label = Label(window, text="Coluna para Atualizar:", font=("Arial 12"))
    coluna_label.place(x=30, y=90)

    colunas = ["nome", "cpf", "rg", "email", "telefone", "formacao", "setor"]
    coluna_combobox = ttk.Combobox(window, values=colunas)
    coluna_combobox.place(x=190, y=90)

    id_valor_label = Label(window, text="ID da consulta:", font=("Arial 12"))
    id_valor_label.place(x=30, y=60)

    id_valor_entry = Entry(window, font=("Arial 12"))
    id_valor_entry.place(x=190, y=60)

    atualizar_button = Button(window, text="Atualizar", font=("Arial 14 bold"), bg="green", fg="white", command=atualizar_tabela)
    atualizar_button.place(x=350, y=60)

    # Tabela
    tabela_medicos = ttk.Treeview(window, columns=("ID", "NOME", "CPF", "RG", "EMAIL", "TELEFONE", "FORMAÇÃO", "SETOR"),
                                  show="headings")
    tabela_medicos.heading('#1', text="ID", anchor='center')
    tabela_medicos.heading('#2', text="NOME", anchor='center')
    tabela_medicos.heading('#3', text="CPF", anchor='center')
    tabela_medicos.heading('#4', text="RG", anchor='center')
    tabela_medicos.heading('#5', text="EMAIL", anchor='center')
    tabela_medicos.heading('#6', text="TELEFONE", anchor='center')
    tabela_medicos.heading('#7', text="FORMAÇÃO", anchor='center')
    tabela_medicos.heading('#8', text="SETOR", anchor='center')

    # Ajustar a largura das colunas
    tabela_medicos.column('#1', width=50, anchor='center')
    tabela_medicos.column('#2', width=150, anchor='center')
    tabela_medicos.column('#3', width=80, anchor='center')
    tabela_medicos.column('#4', width=80, anchor='center')
    tabela_medicos.column('#5', width=150, anchor='center')
    tabela_medicos.column('#6', width=100, anchor='center')
    tabela_medicos.column('#7', width=150, anchor='center')
    tabela_medicos.column('#8', width=150, anchor='center')

    style = ttk.Style()
    style.configure("Treeview", rowheight=30, borderwidth=1)

    tabela_medicos.place(x=30, y=150, width=740, height=200)
    window.mainloop()

