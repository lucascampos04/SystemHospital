from tkinter import Frame, Button, Label, Entry, Tk, messagebox

from src.Model.query.Login.LoginQuery import query_login
from src.view.PerfilUser.PerfilUser import WindowPerfilUser

global input_password, input_email
def on_entry_click(event, entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end")  # Remove o texto de orientação
        entry.configure(fg="black")  # Altera a cor do texto para preto

def on_focusout(event, entry, placeholder_text):
    if not entry.get():
        entry.insert(0, placeholder_text)  # Coloca o texto de orientação
        entry.configure(fg="gray")  # Altera a cor do texto para cinza

def login(event=None):
    global window
    email = input_email.get()
    password = input_password.get()

    authenticated_user = query_login(email, password)
    if authenticated_user:
        user_id = authenticated_user[0]
        if user_id is not None:
            print(f"Usuário autenticado. ID do usuário: {user_id}")
        else:
            print("ID do usuário não encontrado.")
        window.destroy()
        WindowPerfilUser()
    else:
        messagebox.showerror("Falha", "Falha na autenticação. Credenciais inválidas.")
        print("Falha na autenticação. Credenciais inválidas.")

def WindowLogin():
    global input_password, input_email, window
    blue = "#3b80d4"
    groove = "#8a9099"
    blackLight = "#343638"
    body_light_blue = "#737f91"
    bluePlus = "#0845a1"

    window = Tk()
    window.geometry("1100x400")
    window.resizable(False, False)
    window.title("Login")
    window.configure(background=body_light_blue)

    # header
    header = Frame(window, width=1050, height=370, bg=groove)
    header.grid(row=0, column=0, padx=20, pady=10)

    # card of create Account
    CardAccount = Frame(window, width=1080, height=320, bg=blackLight, highlightbackground="white", highlightcolor="white", highlightthickness=2)
    CardAccount.place(x=10, y=30)

    label_login = Label(CardAccount, text="LOGIN", font=("Arial 40 bold"), bg=blackLight, fg="white")
    label_login.place(x=50, y=30)

    # Campo de entrada de email
    input_email = Entry(CardAccount, font=("Arial 20 bold"), fg="gray")
    input_email.insert(0, "Digite seu email")
    input_email.bind("<FocusIn>", lambda event, entry=input_email: on_entry_click(event, entry, "Digite seu email"))
    input_email.bind("<FocusOut>", lambda event, entry=input_email: on_focusout(event, entry, "Digite seu email"))
    input_email.bind("<Return>", login)
    input_email.place(x=50, y=120)

    # Campo de entrada de senha
    input_password = Entry(CardAccount, font=("Arial 20 bold"), fg="gray")
    input_password.insert(0, "Digite sua senha")
    input_password.bind("<FocusIn>", lambda event, entry=input_password: on_entry_click(event, entry, "Digite sua senha"))
    input_password.bind("<FocusOut>", lambda event, entry=input_password: on_focusout(event, entry, "Digite sua senha"))
    input_password.bind("<Return>", login)
    input_password.place(x=50, y=180)

    # Botão de login
    login_button = Button(CardAccount, text="Login", command=login, bg=blue, fg="white", font=("Arial 16 bold"), width=10)
    login_button.place(x=50, y=240)

    window.mainloop()

