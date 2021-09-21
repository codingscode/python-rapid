
import sqlite3 as conector

# abertura de conexao e aquisicao de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# execucao de um comando: SELECT... CREATE...
comando = '''
INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
    VALUES (12345678900, 'João', '2000-01-31', 1);
'''

cursor.execute(comando)


# efetivacao do comando
conexao.commit()

# fechamento das conexoes
cursor.close()
conexao.close()

