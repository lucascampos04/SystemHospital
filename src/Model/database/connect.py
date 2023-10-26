import mysql.connector

def connect_database():
    try:
        connection  = mysql.connector.connect(
            host="localhost",
            user="root",
            password="senha123456",
            database="hospitaldb"
        )
        print("Conexão realizada com sucesso")
        return connection
    except mysql.connector.Error as err:
        print("Erro ao conectar ao banco de dados:", err)
        return None

def close_database(connection ):
    if connection:
        connection.close()
