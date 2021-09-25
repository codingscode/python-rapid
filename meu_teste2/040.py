
import sqlite3 as conector
from a032_modelo import Pessoa

# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db', detect_types=conector.PARSE_DECLTYPES)
cursor = conexao.cursor()

# funcoes conversoras
def conv_bool(dado):
    return True if dado == 1 else False

# registro de conversores
conector.register_converter('BOOLEAN', conv_bool)


# definicao de comandos
comando = '''
SELECT * FROM Pessoa WHERE oculos=:usa_oculos;
'''
cursor.execute(comando, {'usa_oculos': True})

# recuperacao dos registros
registros = cursor.fetchall()

for registro in registros:
    pessoa = Pessoa(*registro)
    print(f'cpf: {type(pessoa.cpf)} {pessoa.cpf}')
    print(f'nome: {type(pessoa.nome)} {pessoa.nome}')
    print(f'nascimento: {type(pessoa.data_nascimento)} {pessoa.data_nascimento}')
    print(f'oculos: {type(pessoa.usa_oculos)} {pessoa.usa_oculos}')


# fechamento das conexoes
cursor.close()
conexao.close()

"""
cpf: <class 'int'> 10000000099
nome: <class 'str'> Maria
nascimento: <class 'datetime.date'> 1998-01-31
oculos: <class 'bool'> False
"""