from tkinter import Label, Entry, Button, Frame, ttk, Tk, messagebox
from tkinter.simpledialog import askstring

from src.Model.query.consultasQuery import atualizar_tabelaID
from src.Model.query.consultasQuery import atualizar_coluna_consulta

global consultas, tabela_consultas, id_valor_entry, idV, coluna_combobox, atualizar_button, colunas

colunas = ["tipo_consulta", "dataConsulta", "horario", "endereco", "id_medico", "id_paciente"]

def listar_tabela():
    id = id_valor_entry.get()
    colunavalue = coluna_combobox.get()

    if not id or not colunavalue:
        messagebox.showerror("Erro", "Por favor, preencha os campos ID e Coluna.")
        return

    consulta = atualizar_tabelaID(id)

    for row in tabela_consultas.get_children():
        tabela_consultas.delete(row)

    if consulta:
        for row in consulta:
            tabela_consultas.insert("", "end", values=row)

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

def WindowUpdateConsulta():
    global coluna_combobox, id_valor_entry, window, consultas, tabela_consultas, idV, atualizar_button

    window = Tk()
    window.title("Atualizar Consulta")
    window.geometry("800x400")
    window.resizable(False, False)

    title = Label(window, text="Atualizar Consulta", font=("Arial 20 bold"))
    title.place(x=300, y=10)

    coluna_label = Label(window, text="Coluna para Atualizar:", font=("Arial 12"))
    coluna_label.place(x=30, y=90)

    colunas = ["tipo_consulta", "dataConsulta", "horario", "endereco", "id_medico", "id_paciente"]
    coluna_combobox = ttk.Combobox(window, values=colunas)
    coluna_combobox.place(x=190, y=90)

    id_valor_label = Label(window, text="ID da consulta:", font=("Arial 12"))
    id_valor_label.place(x=30, y=60)

    id_valor_entry = Entry(window, font=("Arial 12"))
    id_valor_entry.place(x=190, y=60)

    atualizar_button = Button(window, text="Atualizar", font=("Arial 14 bold"), bg="green", fg="white", command=atualizar_tabela)
    atualizar_button.place(x=350, y=60)

    # Tabela
    tabela_consultas = ttk.Treeview(window, columns=("ID", "TIPO", "DATA", "HORÁRIO", "ENDEREÇO", "MÉDICO", "PACIENTE"),
                                    show="headings")
    tabela_consultas.heading('#1', text="ID", anchor='center')
    tabela_consultas.heading('#2', text="TIPO", anchor='center')
    tabela_consultas.heading('#3', text="DATA", anchor='center')
    tabela_consultas.heading('#4', text="HORÁRIO", anchor='center')
    tabela_consultas.heading('#5', text="ENDEREÇO", anchor='center')
    tabela_consultas.heading('#6', text="ID MÉDICO", anchor='center')
    tabela_consultas.heading('#7', text="ID PACIENTE", anchor='center')

    tabela_consultas.column('#1', width=50, anchor='center')
    tabela_consultas.column('#2', width=150, anchor='center')
    tabela_consultas.column('#3', width=80, anchor='center')
    tabela_consultas.column('#4', width=80, anchor='center')
    tabela_consultas.column('#5', width=150, anchor='center')
    tabela_consultas.column('#6', width=100, anchor='center')
    tabela_consultas.column('#7', width=100, anchor='center')

    style = ttk.Style()
    style.configure("Treeview", rowheight=30, borderwidth=1)

    tabela_consultas.place(x=30, y=150, width=740, height=200)
    window.mainloop()

