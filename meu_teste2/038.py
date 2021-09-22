
import sqlite3 as conector


# abertura de conexão e aquisição de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# definicao de comandos
comando = '''
SELECT nome, oculos FROM Pessoa;
'''
cursor.execute(comando)

# recuperacao dos dados
registros = cursor.fetchall()
print(f'Tipo retornado pelo fetchall(): {type(registros)}')

for registro in registros:
    print(f'Tipo: {type(registro)} - Conteudo: {registro}')

# fechamento das conexoes
cursor.close()
conexao.close()


"""
Tipo retornado pelo fetchall(): <class 'list'>
Tipo: <class 'tuple'> - Conteudo: ('Maria', 1)
Tipo: <class 'tuple'> - Conteudo: ('José', 0)
Tipo: <class 'tuple'> - Conteudo: ('Silva', 0)
"""