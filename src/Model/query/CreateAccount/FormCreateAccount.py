from src.Model.database.connect import connect_database, close_database

def query_form_create_account(name, rg, cpf, email, telefone, password):
    connect = connect_database()
    user_id = None

    if connect is not None:
        try:
            cursor = connect.cursor()
            query = """
                INSERT INTO logs_users(nome, rg, cpf, email, telefone, password)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, rg, cpf, email, telefone, password))
            connect.commit()
            id = cursor.fetchall()

            if cursor.rowcount > 0:
                # Recupere o ID do usuário inserido
                cursor.execute("SELECT LAST_INSERT_ID()")
                user_id = cursor.fetchone()[0]

                print(f"Usuário cadastrado com sucesso (ID: {user_id})")
                return user_id
            else:
                print("Houve erro")
                return user_id
        except Exception as e:
            print(f"Erro durante a criação de usuário: {str(e)}")
        finally:
            close_database(connect)
    else:
        print("Não foi possível conectar ao banco de dados.")
        return user_id
