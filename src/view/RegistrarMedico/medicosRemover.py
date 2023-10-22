from tkinter import Tk, Label, Entry, Button, Frame
from src.Model.query.medicosQuery import query_remove_medico

global cpf_entry

def confirm_remove():
    cpf_medico = cpf_entry.get()
    query_remove_medico(cpf_medico)

def WindowMedicosRemove():
    global cpf_entry

    window = Tk()
    window.title("Remover")
    window.geometry("400x300")
    window.resizable(False, False)

    title = Label(window, text="Remover", font=("Arial 25 bold"))
    title.place(x=100, y=10)

    cpf_label = Label(window, text="CPF : ", font=("Arial 15 bold"))
    cpf_label.place(x=30, y=95)
    cpf_entry = Entry(window, font=("Arial 15 bold"))
    cpf_entry.place(x=100, y=100)

    btn_remove = Button(window, text="Remove", font=("Ivy 20 bold"), bg="red", fg="white", command=confirm_remove)
    btn_remove.place(x=120, y=180)

    window.bind('<Return>', lambda event=None: btn_remove.invoke())

    window.mainloop()
