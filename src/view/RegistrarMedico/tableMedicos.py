from tkinter import Tk, Label, Button, Frame, ttk, messagebox

from src.Model.query.medicosQuery import listar_medicos, query_remove_medico

from src.view.RegistrarMedico.addMedicos import WindowAddMedico
from src.view.RegistrarMedico.medicosRemover import WindowMedicosRemove

global tabela_medicos, medicos

def router_addMedico():
    WindowAddMedico()
def router_RemoveMedico():
    WindowMedicosRemove()

cinza = "#5e4f4c"

def atualizar_tabela():
    medicos = listar_medicos()
    tabela_medicos.delete(*tabela_medicos.get_children())
    for medico in medicos:
        tabela_medicos.insert("", "end", values=(medico[0], medico[1], medico[2], medico[3], medico[4], medico[5], medico[6], medico[7]))

def preencher_tabela():
    global tabela_medicos
    medicos = listar_medicos()

    for medico in medicos:
        tabela_medicos.insert("", "end", values=(medico[0], medico[1], medico[2], medico[3], medico[4], medico[5], medico[6], medico[7]))

def remover_medico_selecionado():
    selected_item = tabela_medicos.selection()
    if selected_item:
        medico_id = tabela_medicos.item(selected_item, "values")[0]
        if medico_id:
            confirmar = messagebox.askokcancel("Confirmar", "Você tem certeza que deseja remover este médico?")
            if confirmar:
                if query_remove_medico(medico_id):
                    messagebox.showinfo("Sucesso", "Médico removido com sucesso.")
                    atualizar_tabela()
        else:
            messagebox.showerror("Erro", "Selecione um médico para remover.")
    else:
        messagebox.showerror("Erro", "Selecione um médico para remover.")

def WindowTableMedicos():
    global tabela_medicos, medicos

    window = Tk()
    window.title("Médicos")
    window.geometry("1000x600")
    window.resizable(False, False)

    frameT = Frame(window, width=1080, height=100, bg="blue")
    frameT.grid(row=0, column=0)

    frameM = Frame(window, width=1080, height=500)
    frameM.grid(row=1, column=0)

    title_medicos = Label(frameT, text="TABELA DE MÉDICOS", font=("Arial 50 bold"), bg="blue", fg="white")
    title_medicos.place(x=180, y=10)

    # Tabela
    tabela_medicos = ttk.Treeview(frameM, columns=("ID", "NOME", "CPF", "RG", "EMAIL", "TELEFONE", "FORMAÇÃO", "SETOR"),
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

    tabela_medicos.place(x=10, y=50)
    preencher_tabela()

    btnAdd = Button(frameM, text="Adicionar", font=("Arial 15 bold"), bg="green", fg="white", command=router_addMedico)
    btnAdd.place(x=80, y=400)

    btnRemove = Button(frameM, text="Remover", font=("Arial 15 bold"), bg="red", fg="white", command=router_RemoveMedico)
    btnRemove.place(x=210, y=400)

    btnAtualizar = Button(frameM, text="Atualizar Tabela", font=("Arial 15 bold"), command=atualizar_tabela, bg=cinza, fg="white")
    btnAtualizar.place(x=765, y=400)

    window.mainloop()

WindowTableMedicos()
