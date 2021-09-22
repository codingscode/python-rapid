
import sqlite3 as conector


# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db')
conexao.execute('PRAGMA foreign_keys = on')
cursor = conexao.cursor()

# definicao de comandos
comando = '''
DELETE FROM Pessoa WHERE cpf=12345678900;
'''
cursor.execute(comando)


# efetivacao do comando
conexao.commit()

# fechamento das conexoes
cursor.close()
conexao.close()


"""

"""