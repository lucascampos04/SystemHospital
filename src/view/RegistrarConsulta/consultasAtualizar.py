from tkinter import Label, Entry, Button, Frame, ttk, Tk

def atualizar_consulta():
    coluna_selecionada = coluna_combobox.get()
    novo_valor = novo_valor_entry.get()
    print(f"Atualizando consulta na coluna {coluna_selecionada} com o novo valor {novo_valor}")

def WindowUpdateConsulta():
    global coluna_combobox, novo_valor_entry, window

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

    novo_valor_label = Label(window, text="ID da consulta:", font=("Arial 12"))
    novo_valor_label.place(x=30, y=60)

    novo_valor_entry = Entry(window, font=("Arial 12"))
    novo_valor_entry.place(x=190, y=60)

    atualizar_button = Button(window, text="Atualizar", font=("Arial 14 bold"), bg="green", fg="white", command=atualizar_consulta)
    atualizar_button.place(x=350, y=300)

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

    # Ajustar a largura das colunas
    tabela_consultas.column('#1', width=50, anchor='center')
    tabela_consultas.column('#2', width=150, anchor='center')
    tabela_consultas.column('#3', width=80, anchor='center')
    tabela_consultas.column('#4', width=80, anchor='center')
    tabela_consultas.column('#5', width=150, anchor='center')
    tabela_consultas.column('#6', width=100, anchor='center')
    tabela_consultas.column('#7', width=100, anchor='center')

    style = ttk.Style()
    style.configure("Treeview", rowheight=30, borderwidth=1)

    # Posição da tabela
    tabela_consultas.place(x=30, y=150, width=740, height=200)
    window.mainloop()

WindowUpdateConsulta()
