from tkinter import Label, Entry, Button, Frame, ttk, Tk
from tkinter import messagebox
from tkcalendar import DateEntry

from src.Model.query.consultasQuery import add_consulta

global tipo_consulta_combobox, data_entry, horario_entry, endereco_entry, id_medico_entry, id_paciente_entry, window

def adicionar_consulta():
    tipo_consulta = tipo_consulta_combobox.get()
    data = data_entry.get()
    horario = horario_entry.get()
    endereco = endereco_entry.get()
    id_medico = id_medico_entry.get()
    id_paciente = id_paciente_entry.get()

    # Verifique se todos os campos estão preenchidos
    if tipo_consulta and data and horario and endereco and id_medico and id_paciente:
        verificacao = add_consulta(tipo_consulta, data, horario, endereco, id_medico, id_paciente)

        if verificacao:
            window.destroy()
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

def WindowAddConsulta():
    global tipo_consulta_combobox, data_entry, horario_entry, endereco_entry, id_medico_entry, id_paciente_entry, window
    window = Tk()
    window.title("Adicionar Consulta")
    window.geometry("400x400")
    window.resizable(False, False)

    title = Label(window, text="Adicionar Consulta", font=("Arial 20 bold"))
    title.place(x=100, y=10)

    tipo_consulta_label = Label(window, text="Tipo de Consulta:", font=("Arial 15 bold"))
    tipo_consulta_label.place(x=30, y=60)
    tipo_consulta_values = ["Consulta de Rotina", "Consulta de Emergência", "Outro"]
    tipo_consulta_combobox = ttk.Combobox(window, values=tipo_consulta_values)
    tipo_consulta_combobox.place(x=200, y=65)

    data_label = Label(window, text="Data:", font=("Arial 15 bold"))
    data_label.place(x=30, y=95)
    data_entry = DateEntry(window, date_pattern="yyyy-mm-dd")  # Use DateEntry para selecionar a data
    data_entry.place(x=200, y=100)

    horario_label = Label(window, text="Horário:", font=("Arial 15 bold"))
    horario_label.place(x=30, y=125)
    horario_entry = Entry(window)
    horario_entry.place(x=200, y=130)

    endereco_label = Label(window, text="Endereço:", font=("Arial 15 bold"))
    endereco_label.place(x=30, y=155)
    endereco_entry = Entry(window)
    endereco_entry.place(x=200, y=160)

    id_medico_label = Label(window, text="ID Médico:", font=("Arial 15 bold"))
    id_medico_label.place(x=30, y=185)
    id_medico_entry = Entry(window)
    id_medico_entry.place(x=200, y=190)

    id_paciente_label = Label(window, text="ID Paciente:", font=("Arial 15 bold"))
    id_paciente_label.place(x=30, y=215)
    id_paciente_entry = Entry(window)
    id_paciente_entry.place(x=200, y=220)

    btn_add = Button(window, text="Adicionar Consulta", font=("Arial 15 bold"), command=adicionar_consulta)
    btn_add.place(x=120, y=250)

    window.bind('<Return>', lambda event=None: btn_add.invoke())
    window.mainloop()

