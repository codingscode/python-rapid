
import sqlite3 as conector
from a032_modelo import Veiculo, Marca

# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# definicao de comandos
comando = '''
SELECT * FROM Veiculo JOIN Marca ON Marca.id = Veiculo.marca;
'''
cursor.execute(comando)

# recuperacao dos registros
registros = cursor.fetchall()
for registro in registros:
    print(registro)
    marca = Marca(*registro[6:])
    veiculo = Veiculo(*registro[:5], marca)
    print(f'Placa: {veiculo.placa}, Marca: {veiculo.marca.nome}')

# fechamento das conexoes
cursor.close()
conexao.close()

"""
('AAA0001', 2001, 'Prata', 1.0, 10000000099, 1, 1, 'Marca A', 'MA')
Placa: AAA0001, Marca: Marca A
('BAA0002', 2002, 'Preto', 1.4, 10000000099, 1, 1, 'Marca A', 'MA')
Placa: BAA0002, Marca: Marca A
('CAA0003', 2003, 'Branco', 2.0, 20000000099, 2, 2, 'Marca B', 'MB')
Placa: CAA0003, Marca: Marca B
('DAA0004', 2004, 'Azul', 2.2, 30000000099, 2, 2, 'Marca B', 'MB')
Placa: DAA0004, Marca: Marca B

"""