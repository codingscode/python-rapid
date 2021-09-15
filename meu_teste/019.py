import os


print('---------- inicio -------------')

try:
    os.remove('019_arquivo.txt')
    print('arquivo removido!')
except FileNotFoundError as erro:
    print('Arquivo inexistente')
    print(f'descricao: {erro}')
except PermissionError as erro:
    print('Sem permissão para acessar o arquivo')
    print(f'descricao: {erro}')
except IsADirectoryError as erro:
    print('Remove serve apenas para arquivos')
    print(f'descricao: {erro}')

print('------------ fim -------------')

"""
---------- inicio -------------
arquivo removido!
------------ fim -------------


---------- inicio -------------
Arquivo inexistente
descricao: [WinError 2] O sistema não pode encontrar o arquivo especificado: '019_arquivo.txt'
------------ fim -------------


"""
