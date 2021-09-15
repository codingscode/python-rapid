import os


print('----------- inicio -------------')

try:
    os.mkdir('novo_diretorio')
    print('diretório criado!')
except PermissionError as erro:
    print('sem permissao para criar diretório')
    print(f'descricao: {erro}')
except FileExistsError as erro:
    print('diretório já existente')
    print(f'descricao: {erro}')


print('------------- fim -------------')

"""
----------- inicio -------------
diretório criado!
------------- fim -------------

"""
