
import sqlite3 as conector
from a032_modelo import Pessoa


# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# criacao de um objeto do tipo Pessoa
pessoa = Pessoa(30000000099, 'Silva', '1990-03-30', True)

# definicao de um comando com query parameter
comando = '''
INSERT INTO Pessoa VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);
'''

cursor.execute(comando, vars(pessoa))
print(vars(pessoa))

# efetivacao do comando
conexao.commit()

# fechamento das conexoes
cursor.close()
conexao.close()

"""
{'cpf': 30000000099, 'nome': 'Silva', 'data_nascimento': '1990-03-30', 'usa_oculos': True}

"""