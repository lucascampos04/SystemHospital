from tkinter import Frame, Button, Label, Entry, Tk

from src.Model.query.Login.LoginQuery import query_other_info
# colors
blue = "#3b80d4"
def MarcaConsulta():
    window = Tk()
    window.geometry("600x600")
    window.resizable(False, False)
    window.title("Hospital")

    # Header
    header = Frame(window, width=1280, height=400, bg=blue)
    header.grid(row=0, column=0)

    # Main
    main = Frame(window, width=1280, height=420, bg=blue)
    main.grid(row=1, column=0)

    # Footer
    footer = Frame(window, width=1280, height=100, bg="black")
    footer.grid(row=2, column=0)


    # header

    dados_user_title = Label(header, text="DADOS PACIENTE", font=("Arial 30 bold"), bg=blue, fg="white")
    dados_user_title.place(x=100, y=10)

    info_name = Label(header, text=f'Nome : ', font=("Arial 20 bold"), bg=blue, fg="white")
    info_name.place(x=30, y=70)

    info_cpf = Label(header, text=f'CPF ', font=("Arial 20 bold"), bg=blue, fg="white")
    info_cpf.place(x=30, y=130)

    info_email = Label(header, text=f'EMAIL :', font=("Arial 20 bold"), bg=blue, fg="white")
    info_email.place(x=30, y=180)

    info_email = Label(header, text=f'ID : ', font=("Arial 20 bold"), bg=blue, fg="white")
    info_email.place(x=420, y=70)

    window.mainloop()

