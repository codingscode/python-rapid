import os


print('----------- inicio -------------')

try:
    os.rmdir('novo_diretorio')
    print('diretório removido!')
except PermissionError as erro:
    print('sem permissao para remover diretório')
    print(f'descricao: {erro}')
except FileNotFoundError as erro:
    print('diretório inexistente')
    print(f'descricao: {erro}')
except OSError as erro:
    print('outro erro.')
    print('o diretório está vazio?.')
    print(f'descricao: {erro}')

print('------------- fim -------------')

"""
----------- inicio -------------
diretório removido!
------------- fim -------------


----------- inicio -------------
diretório inexistente
descricao: [WinError 2] O sistema não pode encontrar o arquivo especificado: 'novo_diretorio'
------------- fim -------------


"""
