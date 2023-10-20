from src.Model.database.connect import connect_database, close_database

def query_form_create_account(name, rg, cpf, email, telefone, password):
    connect = connect_database()
    if connect is not None:
        try:
            cursor = connect.cursor()
            query = """
                INSERT INTO logs_users(nome, rg, cpf, email, telefone, password)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, rg, cpf, email, telefone, password))
            result = cursor.fetchone()

            if result:
                print("Usuario cadastrado com sucesso")
                return result
            else:
                print("Houve erro")
                return None
        except Exception as e:
            print(f"Erro durante a criação de usuario :  {str(e)}")
        finally:
            close_database(connect)
    else:
        print("Não foi possível conectar ao banco de dados.")

