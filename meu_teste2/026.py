import sqlite3 as conector

try:
    # abertura de conexao e aquisicao de cursor
    conexao = conector.connect('./026meu_banco.db')
    cursor = conexao.cursor()

    # execucao de um comando: SELECT... CREATE...
    comando = '''
        CREATE TABLE Pessoa (
            cpf INTEGER NOT NULL,
            nome TEXT NOT NULL,
            nascimento DATE NOT NULL,
            oculos BOOLEAN NOT NULL,
            PRIMARY KEY (cpf)
        );
    '''

    cursor.execute(comando)

except conector.DatabaseError as err:
    print('Erro de banco de dados', err)

finally:
    # fechamento das conexoes
    if conexao:
        cursor.close()
        conexao.close()









