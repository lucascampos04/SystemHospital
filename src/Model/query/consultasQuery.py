from src.Model.database.connect import connect_database, close_database
from tkinter import messagebox

def id_medico_existe(id_medico):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM medicos WHERE id = %s", (id_medico,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            return result is not None
        except Exception as err:
            print(f"Erro ao verificar a existência do ID do médico: {str(err)}")
    return False

def id_paciente_existe(id_paciente):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM pacientes WHERE id = %s", (id_paciente,))
            result = cursor.fetchone()
            cursor.close()
            conn.close()
            return result is not None
        except Exception as err:
            print(f"Erro ao verificar a existência do ID do paciente: {str(err)}")
    return False

def add_consulta(tipo, data, horario, endereco, id_medico, id_paciente):
    if tipo and data and horario and endereco and id_medico and id_paciente:
        if id_medico_existe(id_medico) and id_paciente_existe(id_paciente):
            conn = connect_database()
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    query = "INSERT INTO consultas (tipo_consulta, dataConsulta, horario, endereco, id_medico, id_paciente) VALUES (%s, %s, %s, %s, %s, %s)"
                    values = (tipo, data, horario, endereco, id_medico, id_paciente)
                    cursor.execute(query, values)
                    conn.commit()
                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Sucesso", "Consulta adicionada com sucesso")
                    return True
                except Exception as err:
                    messagebox.showerror("Erro", "Erro ao inserir consulta no banco de dados")
                    print(f"Erro ao inserir consulta no banco de dados: {str(err)}")
        else:
            messagebox.showerror("Erro", "ID de médico ou paciente não existe.")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        return False

def listar_consultas():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT id, tipo_consulta, dataConsulta, horario, endereco, id_medico, id_paciente FROM consultas"
            cursor.execute(query)
            consultas = cursor.fetchall()
            cursor.close()
            conn.close()
            print("Consulta de consultas com sucesso")
            return consultas
        except Exception as err:
            print(f"Erro ao consultar o banco de dados de consultas: {str(err)}")

def atualizar_tabelaID(id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT id, tipo_consulta, dataConsulta, horario, endereco, id_medico, id_paciente FROM consultas WHERE id = %s"
            cursor.execute(query, (id,))
            consulta = cursor.fetchall()
            cursor.close()
            conn.close()
            print("Consulta de consulta com sucesso")
            return consulta
        except Exception as err:
            print(f"Erro ao consultar o banco de dados de consultas: {str(err)}")



def query_remove_consulta(consulta_id):
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            if not consulta_id:
                # Verifique se o campo de ID da consulta está vazio
                messagebox.showerror("Erro", "ID da consulta está vazio.")
                return False

            # Consulte a consulta com o ID fornecido
            cursor.execute("SELECT id FROM consultas WHERE id = %s", (consulta_id,))
            consulta = cursor.fetchone()

            if consulta:
                # Exclua a consulta com o ID especificado
                cursor.execute("DELETE FROM consultas WHERE id = %s", (consulta_id,))
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Sucesso", "Consulta removida com sucesso")
                return True
            else:
                cursor.close()
                conn.close()
                messagebox.showerror("Erro", "Consulta não encontrada.")
                return False
        except Exception as err:
            messagebox.showerror("Erro", f"Erro ao excluir consulta: {str(err)}")
    return False







