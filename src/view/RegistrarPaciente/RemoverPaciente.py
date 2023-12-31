from tkinter import Tk, Label, Entry, Button, Frame

from src.Model.query.pacienteQuery import query_remove_paciente

global cpf_entry
def confirm_remove():
    cpf_paciente = cpf_entry.get()
    query_remove_paciente(cpf_paciente)
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
def WindowPacienteRemove():
    global cpf_entry

    window = Tk()
    window.title("Adicionar Paciente")
    center_window(window, 400, 300)
    window.resizable(False, False)

    title = Label(window, text="Remover", font=("Arial 25 bold"))
    title.place(x=100, y=10)

    cpf_label = Label(window, text="Cpf : ", font=("Arial 15 bold"))
    cpf_label.place(x=30, y=95)
    cpf_entry = Entry(window, font=("Arial 15 bold"))
    cpf_entry.place(x=100, y=100)

    btn_remove = Button(window, text="Remove", font=("Ivy 20 bold"), bg="red", fg="white", command=confirm_remove)
    btn_remove.place(x=120, y=180)

    window.bind('<Return>', lambda event=None: btn_remove.invoke())

    window.mainloop()
