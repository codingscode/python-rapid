
import sqlite3 as conector
from a032_modelo import Veiculo

# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# definicao de comandos
comando = '''
SELECT * FROM Veiculo;
'''
cursor.execute(comando)

# recuperacao dos registros
reg_veiculos = cursor.fetchall()
for reg_veiculo in reg_veiculos:
    veiculo = Veiculo(*reg_veiculo)
    print(f'Placa: {veiculo.placa}, Marca: {veiculo.marca}')

# fechamento das conexoes
cursor.close()
conexao.close()

"""
Placa: AAA0001, Marca: 1
Placa: BAA0002, Marca: 1
Placa: CAA0003, Marca: 2
Placa: DAA0004, Marca: 2

"""