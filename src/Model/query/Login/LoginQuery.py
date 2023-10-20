from src.Model.database.connect import connect_database, close_database

def query_login(email, password):
    connect = connect_database()
    if connect is not None:
        try:
            cursor = connect.cursor()
            query = "SELECT * FROM logs_users WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            result = cursor.fetchall()

            if result:
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

