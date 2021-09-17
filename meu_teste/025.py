import sqlite3 as conector


# abertura de conexão
conexao = conector.connect('URL SQLite')

# aquisição de um cursor
cursor = conexao.cursor()

# execução comandos: SELECT..CREATE
cursor.execute('...')
cursor.fetchall()

# efetivação do comando
conexao.commit()

# fechamento das conexoes
cursor.close()
conexao.close()









