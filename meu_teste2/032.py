
import sqlite3 as conector
from a032_modelo import Pessoa


# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# criacao de um objeto do tipo Pessoa
pessoa = Pessoa(10000000099, 'Maria', '1998-01-31', False)

# definicao de um comando com query parameter
comando = '''
INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?);
'''

cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))

# efetivacao do comando
conexao.commit()

# fechamento das conexoes
cursor.close()
conexao.close()






