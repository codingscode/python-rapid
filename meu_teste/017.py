
print('---------- inicio --------------')

print('abrindo um arquivo')

try:
    open('naoexiste.txt', 'r')
    print('arquivo aberto!')
except:
    print('houve um erro.')

print('------------ fim --------------')
"""
---------- inicio --------------
abrindo um arquivo
houve um erro.
------------ fim --------------
"""
