import os

arquivo = open('001.txt')


print('-------- inicio ------------')
print(arquivo)

print(f'nome do arquivo: {arquivo.name}')
print(f'modo do arquivo: {arquivo.mode}')
print(f'arquivo fechado: {arquivo.closed}')

arquivo.close()

print(f'arquivo fechado: {arquivo.closed}')


print('-------- fim ------------')

"""
-------- inicio ------------
<_io.TextIOWrapper name='001.txt' mode='r' encoding='cp1252'>
nome do arquivo: 001.txt
modo do arquivo: r
arquivo fechado: False
arquivo fechado: True
-------- fim ------------

"""





