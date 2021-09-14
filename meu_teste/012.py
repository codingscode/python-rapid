

print('----------- inicio --------------')

with open('012_texto.txt', 'r') as arquivo:
    texto = arquivo.read()
    contador = texto.count('algo')
    print(f'total de algo: {contador}')


print('------------- fim --------------')

"""
----------- inicio --------------
total de algo: 4
------------- fim --------------
"""
