import os
import errno

print('----------- inicio ------------')

try:
    os.rmdir('meu_diretorio2')
    print('diretório removido!')
except OSError as erro:
    print(erro.errno)
    if erro.errno == errno.ENOTEMPTY:
        print('o diretório não está vazio')
    else:
        print('erro inesperado')
    print(f'descricao: {erro}')

print('------------- fim ------------')

"""
----------- inicio ------------
diretório removido!
------------- fim ------------


----------- inicio ------------
41
o diretório não está vazio
descricao: [WinError 145] A pasta não está vazia: 'meu_diretorio2'
------------- fim ------------


----------- inicio ------------
2
erro inesperado
descricao: [WinError 2] O sistema não pode encontrar o arquivo especificado: 'meu_diretorio2'
------------- fim ------------

"""
