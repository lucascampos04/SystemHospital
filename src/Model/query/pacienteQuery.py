from src.Model.database.connect import connect_database, close_database
from tkinter import messagebox


def add_paciente(nome, cpf, email, telefone, rg):
    if nome and cpf and email and rg:
        conn = connect_database()
        if conn is not None:
            try:
                cursor = conn.cursor()

                # Verificar se o CPF já existe
                cursor.execute("SELECT cpf FROM pacientes WHERE cpf = %s", (cpf,))
                cpf_result = cursor.fetchone()

                # Verificar se o RG já existe
                cursor.execute("SELECT rg FROM pacientes WHERE rg = %s", (rg,))
                rg_result = cursor.fetchone()

                # Verificar se o email já existe
                cursor.execute("SELECT email FROM pacientes WHERE email = %s", (email,))
                email_result = cursor.fetchone()

                # Verificar se o telefone já existe
                cursor.execute("SELECT telefone FROM pacientes WHERE telefone = %s", (telefone,))
                telefone_result = cursor.fetchone()

                cursor.close()
                conn.close()

                if cpf_result:
                    messagebox.showerror("Erro", "Este CPF já está registrado.")
                    return False

                if rg_result:
                    messagebox.showerror("Erro", "Este RG já está registrado.")
                    return False

                if email_result:
                    messagebox.showerror("Erro", "Este Email já está registrado.")
                    return False

                if telefone_result:
                    messagebox.showerror("Erro", "Este Telefone já está registrado.")
                    return False

                # Se nenhum campo existe, prossegue com a inserção
                query = "INSERT INTO pacientes (nome, cpf, email, telefone, rg) VALUES (%s, %s, %s, %s, %s)"
                values = (nome, cpf, email, telefone, rg)

                conn = connect_database()
                if conn is not None:
                    cursor = conn.cursor()
                    cursor.execute(query, values)
                    conn.commit()
                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Sucesso", "Paciente adicionado com sucesso")
                    return True
            except Exception as err:
                messagebox.showerror("Erro", "Erro ao inserir paciente no banco de dados")
                print(f"Erro ao inserir paciente no banco de dados: {str(err)}")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return False


def listar_pacientes():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT id, nome, cpf, rg, email, telefone FROM pacientes"
            cursor.execute(query)
            pacientes = cursor.fetchall()
            cursor.close()
            conn.close()
            print("Consulta com sucesso")
            return pacientes
        except Exception as err:
            print(f"Erro ao consultar o banco de dados: {str(err)}")


from tkinter import messagebox

def query_remove_paciente(cpf):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            if not cpf:
                # Verifique se o campo de CPF está vazio
                messagebox.showerror("Erro", "Campo CPF está vazio.")
                return False

            # Consulte o paciente com o CPF fornecido
            cursor.execute("SELECT id FROM pacientes WHERE cpf = %s", (cpf,))
            paciente = cursor.fetchone()

            if paciente:
                # Exclua o paciente com o ID especificado
                cursor.execute("DELETE FROM pacientes WHERE cpf = %s", (cpf,))
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Sucesso", "Paciente Deletado com sucesso")
                return True
            else:
                cursor.close()
                conn.close()
                messagebox.showerror("Erro", "Paciente não encontrado.")
                return False
        except Exception as err:
            messagebox.showerror("Erro", f"Erro ao excluir paciente: {str(err)}")
    return False


def atualizar_tabelaID(id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT id, nome, cpf, rg, email, telefone FROM pacientes WHERE id = %s"
            cursor.execute(query, (id,))
            consulta = cursor.fetchall()
            cursor.close()
            conn.close()
            print("Consulta de consulta com sucesso")
            return consulta
        except Exception as err:
            print(f"Erro ao consultar o banco de dados de consultas: {str(err)}")


def atualizar_coluna_consulta(id, coluna, novo_valor):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            colunas_seguras = ["nome", "cpf", "rg", "email", "telefone"]
            if coluna not in colunas_seguras:
                raise ValueError("Coluna inválida")

            query = f"UPDATE pacientes SET {coluna} = %s WHERE id = %s"
            values = (novo_valor, id)

            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as err:
            print(f"Erro ao atualizar coluna de consulta: {str(err)}")
    return False

