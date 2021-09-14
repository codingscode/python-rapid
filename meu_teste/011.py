
print('----------- inicio --------------')

with open ('010_texto.txt', 'r') as arquivo1:
    print('total de linhas no arquivo')
    contador = 0
    for linha in arquivo1:
        if linha:
            contador += 1
    print(f'total: {contador}') 

print('---------------------------------')

with open('010_texto.txt', 'r') as arquivo2:
    print('total real de linhas no arquivo')
    contador2 = 0 
    for linha in arquivo2:
        if linha.strip():
            contador2 += 1
    print(f'total real: {contador2}')

print('----------- fim --------------')

"""
----------- inicio --------------
total de linhas no arquivo
total: 7
---------------------------------
total real de linhas no arquivo
total real: 5
----------- fim --------------

"""
