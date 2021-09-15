
print('---------- inicio --------------')

print('abrindo um arquivo')

try:
    open('naoexiste.txt', 'r')
    print('arquivo aberto!')
except FileNotFoundError as erro1:
    print('houve um erro.')
    print(f'erro: {erro}')

print('------------ fim --------------')
"""
---------- inicio --------------
abrindo um arquivo
houve um erro.
erro: [Errno 2] No such file or directory: 'naoexiste.txt'
------------ fim --------------
"""
