
import sqlite3 as conector
#from a032_modelo import Marca, Veiculo


# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db')
conexao.execute('PRAGMA foreign_keys = on')
cursor = conexao.cursor()

# definicao de comandos
comando1 = '''
UPDATE Pessoa SET oculos=1;
'''
cursor.execute(comando1)

comando2 = '''
UPDATE Pessoa SET oculos= ? WHERE cpf=30000000099;
'''
cursor.execute(comando2, (False,))

comando3 = '''
UPDATE Pessoa SET oculos= :usa_oculos WHERE cpf= :cpf;
'''
cursor.execute(comando3, {'usa_oculos': False, 'cpf': 20000000099})


# efetivacao do comando
conexao.commit()

# fechamento das conexoes
cursor.close()
conexao.close()


"""

"""