from src.Model.database.connect import connect_database, close_database


def query_form_create_account(name, rg, cpf, email, telefone, password):
    connect = connect_database()

    if connect is not None:
        try:
            cursor = connect.cursor()

            # Verifique se algum dos campos já existe na tabela
            cursor.execute("SELECT COUNT(*) FROM logs_users WHERE email = %s OR rg = %s OR cpf = %s OR telefone = %s OR password = %s", (email, rg, cpf, telefone, password))
            count = cursor.fetchone()[0]

            if count > 0:
                existing_fields = []  # Inicialize uma lista para rastrear campos duplicados
                if cursor.execute("SELECT COUNT(*) FROM logs_users WHERE email = %s", (email,)):
                    existing_fields.append("email")
                if cursor.execute("SELECT COUNT(*) FROM logs_users WHERE rg = %s", (rg,)):
                    existing_fields.append("RG")
                if cursor.execute("SELECT COUNT(*) FROM logs_users WHERE cpf = %s", (cpf,)):
                    existing_fields.append("CPF")
                if cursor.execute("SELECT COUNT(*) FROM logs_users WHERE telefone = %s", (telefone,)):
                    existing_fields.append("telefone")

                error_message = f"Erro: Os seguintes campos já existem na tabela: {', '.join(existing_fields)}"
                print(error_message)
                return None

            query = """
                INSERT INTO logs_users(nome, rg, cpf, email, telefone, password)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (name, rg, cpf, email, telefone, password))
            connect.commit()

            # Obtenha o ID do usuário recém-criado
            user_id = cursor.lastrowid

            if user_id:
                print(f"Usuário cadastrado com sucesso. ID do usuário: {user_id}")
                return user_id
            else:
                return None
        except Exception as e:
            print(f"Erro: {str(e)}")
        finally:
            close_database(connect)
    else:
        print("Não foi possível conectar ao banco de dados.")


