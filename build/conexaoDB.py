# Importanto as bibliotecas do SQLITE 3
import sqlite3
from sqlite3 import Error

# Função para se conectar ao banco de dados
def conexaoDB():
    conn = None # conn recebe o valor nulo

    # Tratamento de erro
    try:
        conn = sqlite3.connect("BancoDeDados.db") # Receber o banco de dados
    except Error as e:  # Se não executa, mostra a mensagem de erro
        print(e)
    return conn # Retorna o valor de conn

# Função para buscar a tabela no banco de dados
def buscarBanco():
    conn = conexaoDB() # variavel recebe a função que conecta com o banco de dados
    cursor = conn.cursor()

    # Variavel data que recebe o cursor.execute que seria executa o comando SELECT * FROM User | SELECT = SELECIONAR | * = TUDO | FROM = DE | User = Tabela User
    data  = cursor.execute("SELECT * FROM User;").fetchall()
    return data # retorna os valores da tabela

# Função que vai inserir um determinado dados na tabela
def inserirDados(data, emocao, nota): # Adicionando variavel data, emocao, nota : Conforme tem no banco de dados
    conn = conexaoDB() # variavel conn recebe a função conexaoDB que seria o banco de dados
    cursor = conn.cursor()
    # cursor.execute faz a execução do comando INSERT INTO User(DATE,EMOCAO,NOTA)
    cursor.execute(f"INSERT INTO User(DATE,EMOCAO,NOTA) VALUES('{data}', '{emocao}','{nota}' )")
    conn.commit()   # Faça um commit no banco de dados                                                                                                                                                            # INTO = EM | User = Tabela
    return cursor.lastrowid