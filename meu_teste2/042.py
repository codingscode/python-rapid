
import sqlite3 as conector
from a032_modelo import Veiculo

# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# definicao de comandos
comando = '''
SELECT Veiculo.placa, Veiculo.ano, Veiculo.cor, Veiculo.motor, Veiculo.proprietario, Marca.nome FROM Veiculo JOIN Marca ON Marca.id = Veiculo.marca;
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
Placa: AAA0001, Marca: Marca A
Placa: BAA0002, Marca: Marca A
Placa: CAA0003, Marca: Marca B
Placa: DAA0004, Marca: Marca B

"""