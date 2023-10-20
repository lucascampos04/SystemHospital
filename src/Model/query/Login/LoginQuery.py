from src.Model.database.connect import connect_database, close_database

def query_login(email, password):
    connect = connect_database()
    if connect is not None:
        try:
            cursor = connect.cursor()
            query = "SELECT * FROM logs_users WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            result = cursor.fetchone()

            if result:
                user_id = result[0]
                print("A autenticação foi bem-sucedida")
                return result
            else:
                print("Não há correspondências para o email e senha fornecidos")
                return None
        except Exception as e:
            print(f"Erro durante a consulta de login: {str(e)}")
        finally:
            close_database(connect)
    else:
        print("Não foi possível conectar ao banco de dados.")

def query_other_info(user_id):
    connect = connect_database()
    if connect is not None:
        try:
            cursor = connect.cursor()
            query = "SELECT nome, rg, cpf, email FROM logs_users WHERE id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchall()

            if result:
                if result:
                    nome, rg, cpf, email = result
                    user_info = {
                        "nome": nome,
                        "rg": rg,
                        "cpf": cpf,
                        "email": email
                    }
                return user_info
            else:
                print("Nenhum resultado encontrado na consulta de outras informações")
                return None
        except Exception as e:
            print(f"Erro durante a consulta de outras informações: {str(e)}")
        finally:
            close_database(connect)
    else:
        print("Não foi possível conectar ao banco de dados.")




