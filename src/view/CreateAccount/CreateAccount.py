from tkinter import Frame, Button, Label, Entry, Tk, Checkbutton, IntVar
from tkinter import messagebox

from src.Model.query.CreateAccount.FormCreateAccount import query_form_create_account

from src.view.Login.Login import WindowLogin

def on_entry_click(event, entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end")
        entry.configure(fg="black")

def on_focusout(event, entry, placeholder_text):
    if not entry.get():
        entry.insert(0, placeholder_text)
        entry.configure(fg="gray")

def register():
    global input_email, input_password, input_nome, input_rg, input_cpf, input_telefone, window
    nome = input_nome.get()
    rg = input_rg.get()
    cpf = input_cpf.get()
    telefone = input_telefone.get()
    email = input_email.get()
    password = input_password.get()

    # Verifique se algum campo está vazio ou não foi modificado
    if nome == "Digite seu nome" or rg == "Digite seu RG" or cpf == "Digite seu CPF" or telefone == "Digite seu telefone" or email == "Digite seu email" or password == "Digite sua senha":
        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos corretamente.")
        return

    # Verifique se RG, CPF e telefone contêm apenas números
    if not rg.isdigit() or not cpf.isdigit() or not telefone.isdigit():
        messagebox.showerror("Erro", "RG, CPF e Telefone devem conter apenas números.")
        return

    # Verifica se o Nome só contem letras
    if not nome.isalpha():
        messagebox.showerror("Erro", "O campo de nome deve conter apenas letras.")
        return

    # Insert banco de dados
    query_form_create_account(nome, rg, cpf, email, telefone, password)

    print("Usuário registrado com sucesso")
    print(f"Nome: {nome}, RG: {rg}, CPF: {cpf}, Telefone: {telefone}, Email: {email}, Senha: {password}")


    window.destroy()
    WindowLogin()

def toggle_password():
    if show_password_var.get() == 1:
        input_password.config(show="")
    else:
        input_password.config(show="*")


def WindowRegister():
    global input_email, input_password, input_nome, input_rg, input_cpf, input_telefone, show_password_var, window
    blue = "#3b80d4"
    groove = "#8a9099"
    blackLight = "#343638"
    body_light_blue = "#737f91"

    window = Tk()
    window.geometry("1100x500")
    window.resizable(False, False)
    window.title("Registro de Conta")
    window.configure(background=body_light_blue)

    # header
    header = Frame(window, width=1050, height=370, bg=blackLight)
    header.grid(row=0, column=0, padx=20, pady=10)

    # card de registro de conta
    CardRegister = Frame(window, width=1080, height=370, bg=blackLight, highlightbackground="white", highlightcolor="white", highlightthickness=2)
    CardRegister.place(x=10, y=30)

    label_register = Label(CardRegister, text="REGISTRO DE CONTA", font=("Arial 40 bold"), bg=blackLight, fg="white")
    label_register.place(x=50, y=30)

    # Campo de entrada de nome
    input_nome = Entry(CardRegister, font=("Arial 20 bold"), fg="gray")
    input_nome.insert(0, "Digite seu nome")
    input_nome.bind("<FocusIn>", lambda event, entry=input_nome: on_entry_click(event, entry, "Digite seu nome"))
    input_nome.bind("<FocusOut>", lambda event, entry=input_nome: on_focusout(event, entry, "Digite seu nome"))
    input_nome.place(x=50, y=120)

    # Campo de entrada de RG
    input_rg = Entry(CardRegister, font=("Arial 20 bold"), fg="gray")
    input_rg.insert(0, "Digite seu RG")
    input_rg.bind("<FocusIn>", lambda event, entry=input_rg: on_entry_click(event, entry, "Digite seu RG"))
    input_rg.bind("<FocusOut>", lambda event, entry=input_rg: on_focusout(event, entry, "Digite seu RG"))
    input_rg.place(x=50, y=180)

    # Campo de entrada de CPF
    input_cpf = Entry(CardRegister, font=("Arial 20 bold"), fg="gray")
    input_cpf.insert(0, "Digite seu CPF")
    input_cpf.bind("<FocusIn>", lambda event, entry=input_cpf: on_entry_click(event, entry, "Digite seu CPF"))
    input_cpf.bind("<FocusOut>", lambda event, entry=input_cpf: on_focusout(event, entry, "Digite seu CPF"))
    input_cpf.place(x=50, y=240)

    # Campo de entrada de telefone
    input_telefone = Entry(CardRegister, font=("Arial 20 bold"), fg="gray")
    input_telefone.insert(0, "Digite seu telefone")
    input_telefone.bind("<FocusIn>", lambda event, entry=input_telefone: on_entry_click(event, entry, "Digite seu telefone"))
    input_telefone.bind("<FocusOut>", lambda event, entry=input_telefone: on_focusout(event, entry, "Digite seu telefone"))
    input_telefone.place(x=50, y=300)

    # Campo de entrada de email
    input_email = Entry(CardRegister, font=("Arial 20 bold"), fg="gray")
    input_email.insert(0, "Digite seu email")
    input_email.bind("<FocusIn>", lambda event, entry=input_email: on_entry_click(event, entry, "Digite seu email"))
    input_email.bind("<FocusOut>", lambda event, entry=input_email: on_focusout(event, entry, "Digite seu email"))
    input_email.place(x=450, y=120)

    # Campo de entrada de senha
    input_password = Entry(CardRegister, font=("Arial 20 bold"), fg="gray", show="*")
    input_password.insert(0, "Digite sua senha")
    input_password.bind("<FocusIn>", lambda event, entry=input_password: on_entry_click(event, entry, "Digite sua senha"))
    input_password.bind("<FocusOut>", lambda event, entry=input_password: on_focusout(event, entry, "Digite sua senha"))
    input_password.place(x=450, y=180)

    # Caixa de seleção para mostrar a senha
    show_password_var = IntVar()
    show_password_checkbox = Checkbutton(CardRegister, text="Mostrar Senha", variable=show_password_var, command=toggle_password, font=("Arial 12"))
    show_password_checkbox.place(x=450, y=220)

    # Botão de registro
    register_button = Button(CardRegister, text="Registrar", command=register, bg=blue, fg="white", font=("Arial 16 bold"), width=10)
    register_button.place(x=450, y=290)

    window.mainloop()

