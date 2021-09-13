import os

arquivo = open('001.txt')

a = 12

print('-------- inicio ------------')
print(f'a é {a}')
print(arquivo)

print(os.path.relpath(arquivo.name))
print(os.path.abspath(arquivo.name))

print('-------- fim ------------')

"""

a é 12
<_io.TextIOWrapper name='001.txt' mode='r' encoding='cp1252'>
001.txt
C:\Meus_Arquivos\Superior\Estacio\3 periodo\desenvolvimento rapido de aplicacoes em python\programa\meu_teste\001.txt

"""
