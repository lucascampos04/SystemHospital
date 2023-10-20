from tkinter import Frame, Button, Label, Entry, Tk

from src.view.Login.Login import WindowLogin
from src.view.CreateAccount.CreateAccount import WindowRegister

def router_login():
    window.destroy()
    WindowLogin()

def rouetr_CreateAccount():
    window.destroy()
    WindowRegister()

# colors
blue = "#3b80d4"

window = Tk()
window.geometry("1200x600")
window.resizable(False, False)
window.title("Hospital")

# Header
header = Frame(window, width=1280, height=150, bg=blue)
header.grid(row=0, column=0)

# Main
main = Frame(window, width=1280, height=420, bg=blue)
main.grid(row=1, column=0)

# Footer
footer = Frame(window, width=1280, height=100, bg="black")
footer.grid(row=2, column=0)

# header
title_header = Label(header, text="HOSPITAL.COM", font=("Arial 70 bold"), bg=blue, fg="white")
title_header.place(x=30, y=20)

button_login = Button(header, text=("Login"), font=("Ivy 20 bold"), command=router_login)
button_login.place(x=1070, y=10)

button_CreateAccount = Button(header, text=("Criar conta"), font=("Ivy 20 bold"), command=rouetr_CreateAccount)
button_CreateAccount.place(x=880, y=10)

# main

h1_consults = Label(main, text="Consultas disponíveis", font=("Ivy 20 bold"), fg="black", bg=blue)
h1_consults.place(x=420, y=10)

# Estilo para os cartões
card_style = {
    'width': 300,
    'height': 200,
    'bg': "white",
    'highlightbackground': "black",
    'highlightcolor': "blue",
    'highlightthickness': 2
}

# cards
card_odontologia = Frame(main, **card_style)
card_odontologia.place(x=50, y=50)

# Título do cartão Odontologia
label_title_odontologia = Label(card_odontologia, text="Odontologia", font=("Arial 16 bold"))
label_title_odontologia.place(x=10, y=10)

# Conteúdo do cartão Odontologia
label_horario_odontologia = Label(card_odontologia, text="Horário: 9:00 AM", font=("Arial 12"))
label_horario_odontologia.place(x=10, y=40)

label_local_odontologia = Label(card_odontologia, text="Local: Sala 101", font=("Arial 12"))
label_local_odontologia.place(x=10, y=70)

label_medico_odontologia = Label(card_odontologia, text="Médico: Dr. Silva", font=("Arial 12"))
label_medico_odontologia.place(x=10, y=100)

# Botão "Agendar Consulta" no cartão Odontologia
button_agendar_odontologia = Button(card_odontologia, text="Agendar Consulta", font=("Arial 12"))
button_agendar_odontologia.place(x=10, y=150)

card_oftamologista = Frame(main, **card_style)
card_oftamologista.place(x=450, y=50)

# Título do cartão Oftalmologista
label_title_oftalmologista = Label(card_oftamologista, text="Oftalmologia", font=("Arial 16 bold"))
label_title_oftalmologista.place(x=10, y=10)

# Conteúdo do cartão Oftalmologista
label_horario_oftalmologista = Label(card_oftamologista, text="Horário: 2:30 PM", font=("Arial 12"))
label_horario_oftalmologista.place(x=10, y=40)

label_local_oftalmologista = Label(card_oftamologista, text="Local: Sala 202", font=("Arial 12"))
label_local_oftalmologista.place(x=10, y=70)

label_medico_oftalmologista = Label(card_oftamologista, text="Médico: Dr. Torres", font=("Arial 12"))
label_medico_oftalmologista.place(x=10, y=100)

# Botão "Agendar Consulta" no cartão Oftalmologista
button_agendar_oftalmologista = Button(card_oftamologista, text="Agendar Consulta", font=("Arial 12"))
button_agendar_oftalmologista.place(x=10, y=150)

card_cardiaco = Frame(main, **card_style)
card_cardiaco.place(x=850, y=50)

# Título do cartão Cardíaco
label_title_cardiaco = Label(card_cardiaco, text="Cardiologia", font=("Arial 16 bold"))
label_title_cardiaco.place(x=10, y=10)

# Conteúdo do cartão Cardíaco
label_horario_cardiaco = Label(card_cardiaco, text="Horário: 4:00 PM", font=("Arial 12"))
label_horario_cardiaco.place(x=10, y=40)

label_local_cardiaco = Label(card_cardiaco, text="Local: Sala 301", font=("Arial 12"))
label_local_cardiaco.place(x=10, y=70)

label_medico_cardiaco = Label(card_cardiaco, text="Médico: Dr. Rodrigues", font=("Arial 12"))
label_medico_cardiaco.place(x=10, y=100)

# Botão "Agendar Consulta" no cartão Cardíaco
button_agendar_cardiaco = Button(card_cardiaco, text="Agendar Consulta", font=("Arial 12"))
button_agendar_cardiaco.place(x=10, y=150)

# Footer content
footer_label = Label(footer, text="© 2023 Hospital.com. Todos os direitos reservados.", font=("Arial 12"), bg="black", fg="white")
footer_label.place(x=400, y=5)

window.mainloop()
