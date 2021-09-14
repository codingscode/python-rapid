

print('------------ inicio --------------')

minha_lista = ['monitor', 'mouse', 'gabinete', 'cadeira', 'teclado']

conector = ', '

texto1 = conector.join(minha_lista)

with open('015_texto1.txt', 'w') as arquivo:
    arquivo.write(texto1)


texto2 = '\n'.join(minha_lista)

with open('015_texto2.txt', 'w') as arquivo:
    arquivo.write(texto2)

print('------------- fim ----------------')

# cria, escreve arquivos

"""
------------ inicio --------------
------------- fim ----------------
"""