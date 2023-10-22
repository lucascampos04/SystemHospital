from tkinter import Tk, Label, Entry, Button, Frame
from src.Model.query.consultasQuery import query_remove_consulta

global id_entry

def confirm_remove():
    id_evento = id_entry.get()
    query_remove_consulta(id_evento)

def WindowConsultaRemove():
    global id_entry

    window = Tk()
    window.title("Remover")
    window.geometry("400x300")
    window.resizable(False, False)

    title = Label(window, text="Remover", font=("Arial 25 bold"))
    title.place(x=100, y=10)

    id_label = Label(window, text="ID : ", font=("Arial 15 bold"))
    id_label.place(x=30, y=95)
    id_entry = Entry(window, font=("Arial 15 bold"))
    id_entry.place(x=100, y=100)

    btn_remove = Button(window, text="Remove", font=("Ivy 20 bold"), bg="red", fg="white", command=confirm_remove)
    btn_remove.place(x=120, y=180)

    window.bind('<Return>', lambda event=None: btn_remove.invoke())

    window.mainloop()
