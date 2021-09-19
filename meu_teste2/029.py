
import sqlite3 as conector

# abertura de conexao e aquisicao de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# execucao de um comando: SELECT... CREATE...
comando = '''
ALTER TABLE Veiculo
    ADD motor REAL;

'''

cursor.execute(comando)

# efetivacao do comando
conexao.commit()

# fechamento das conexoes
cursor.close()
conexao.close()
















