
print('------------ inicio -------------')

frase1 = 'a ida foi uma boa partida, a vida veio seguida.'
print(f"contagem direta {frase1.count('ida')}")

contador = 0
lista_termos = frase1.split()
for palavra in lista_termos:
    if palavra == 'ida':
        contador += 1

print(f'contagem correta: {contador}')

print('-------------- fim -------------')

"""
------------ inicio -------------
contagem direta 4
contagem correta: 1
-------------- fim -------------
"""
