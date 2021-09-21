
import sqlite3 as conector
from a032_modelo import Pessoa


# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# criacao de um objeto do tipo Pessoa
pessoa = Pessoa(20000000099, 'José', '1990-02-28', False)

# definicao de um comando com query parameter
comando = '''
INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (:cpf, :nome, :data_nascimento, :usa_oculos);
'''

cursor.execute(comando, {'cpf': pessoa.cpf,'nome': pessoa.nome,'data_nascimento': pessoa.data_nascimento,'usa_oculos': pessoa.usa_oculos})

# efetivacao do comando
conexao.commit()

# fechamento das conexoes
cursor.close()
conexao.close()






