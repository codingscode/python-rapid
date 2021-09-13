
print('----------- inicio --------------')

with open ('010_texto.txt', 'r') as arquivo1:
    print('representação original da linha')
    for linha in arquivo1:
        print(repr(linha))

print('---------------------------------')

with open('010_texto.txt', 'r') as arquivo2:
    print('representação da linha após strip')
    for linha in arquivo2:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))

print('----------- fim --------------')

"""
----------- inicio --------------
representação original da linha
'O rato roeu\n'
'        a roupa do \n'
'rei de Roma.      \n'
'   A rua de pedra\n'
'do centro Ã© bonita.\n'
'\n'
'\n'
---------------------------------
representação da linha após strip
'O rato roeu'
'a roupa do'
'rei de Roma.'
'A rua de pedra'
'do centro Ã© bonita.'
''
''
----------- fim --------------
"""
