
import sqlite3 as conector
from a032_modelo import Marca, Veiculo


# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db')
conexao.execute('PRAGMA foreign_keys = on')
cursor = conexao.cursor()

# insercao de dados na tabela Marca
comando1 = ''' 
INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);
'''

marca1 = Marca('Marca A', 'MA')
cursor.execute(comando1, vars(marca1))
marca1.id = cursor.lastrowid

marca2 = Marca('Marca B', 'MB')
cursor.execute(comando1, vars(marca2))
marca2.id = cursor.lastrowid

# insercao de dados na tabela Veiculo
comando2 = '''
INSERT INTO Veiculo VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);
'''

veiculo1 = Veiculo('AAA0001', 2001, 'Prata', 1.0, 10000000099, marca1.id)
veiculo2 = Veiculo('BAA0002', 2002, 'Preto', 1.4, 10000000099, marca1.id)
veiculo3 = Veiculo('CAA0003', 2003, 'Branco', 2.0, 20000000099, marca2.id)
veiculo4 = Veiculo('DAA0004', 2004, 'Azul', 2.2, 30000000099, marca2.id)

cursor.execute(comando2, vars(veiculo1))
cursor.execute(comando2, vars(veiculo2))
cursor.execute(comando2, vars(veiculo3))
cursor.execute(comando2, vars(veiculo4))

# efetivacao do comando
conexao.commit()

# fechamento das conexoes
cursor.close()
conexao.close()


"""

"""