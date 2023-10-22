from tkinter import Tk, Label, Button, Frame, ttk, messagebox

from src.Model.query.consultasQuery import listar_consultas

from src.view.RegistrarConsulta.removeConculta import WindowConsultaRemove

global tabela_consultas, consultas

def router_remover():
    WindowConsultaRemove()

def atualizar_tabela_consultas():
    global consultas
    consultas = listar_consultas()
    tabela_consultas.delete(*tabela_consultas.get_children())
    for consulta in consultas:
        tabela_consultas.insert("", "end", values=(consulta[0], consulta[1], consulta[2], consulta[3], consulta[4], consulta[5]))

def preencher_tabela_consultas():
    global consultas
    global tabela_consultas
    consultas = listar_consultas()
    for consulta in consultas:
        tabela_consultas.insert("", "end", values=(consulta[0], consulta[1], consulta[2], consulta[3], consulta[4], consulta[5], consulta[6]))


def WindowTableConsultas():
    global tabela_consultas, consultas

    window = Tk()
    window.title("Consultas")
    window.geometry("900x600")
    window.resizable(False, False)

    frameT = Frame(window, width=1080, height=100, bg="blue")
    frameT.grid(row=0, column=0)

    frameM = Frame(window, width=1080, height=500)
    frameM.grid(row=1, column=0)

    title_consultas = Label(frameT, text="TABELA DE CONSULTAS", font=("Arial 50 bold"), bg="blue", fg="white")
    title_consultas.place(x=50, y=10)

    # Tabela
    tabela_consultas = ttk.Treeview(frameM,columns=("ID", "TIPO", "DATA", "HORÁRIO", "ENDEREÇO", "MÉDICO", "PACIENTE"),
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

    tabela_consultas.place(x=100, y=50)

    btnAdd = Button(frameM, text="Adicionar", font=("Arial 15 bold"), bg="green", fg="white")
    btnAdd.place(x=100, y=400)

    btnRemove = Button(frameM, text="Remover", font=("Arial 15 bold"), bg="red", fg="white", command=router_remover)
    btnRemove.place(x=250, y=400)

    btnAtualizar = Button(frameM, text="Atualizar Tabela", font=("Arial 15 bold"),fg="black", command=atualizar_tabela_consultas)
    btnAtualizar.place(x=650, y=400)

    preencher_tabela_consultas()
    window.mainloop()


WindowTableConsultas()
