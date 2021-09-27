
import sqlite3 as conector
from a032_modelo import Pessoa
from a044_b import recuperar_veiculos

# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# definicao de comandos
comando = '''
SELECT * FROM Pessoa;
'''
cursor.execute(comando)

# recuperacao dos registros
pessoas = []
reg_pessoas = cursor.fetchall()
for reg_pessoa in reg_pessoas:
    pessoa = Pessoa(*reg_pessoa)
    pessoa.veiculos = recuperar_veiculos(conexao, pessoa.cpf)
    pessoas.append(pessoa)

for pessoa in pessoas:
    print(pessoa.nome)
    for veiculo in pessoa.veiculos:
        print(f'\t {veiculo.placa} {veiculo.marca.nome}')

# fechamento das conexoes
cursor.close()
conexao.close()

"""
Maria
         AAA0001 Marca A
         BAA0002 Marca A
José
         CAA0003 Marca B
Silva
         DAA0004 Marca B

"""