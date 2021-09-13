
arquivo1 = open('003.txt', 'r')
arquivo2 = open('003.txt', 'r')
arquivo3 = open('003.txt', 'r')

print('-------- inicio ------------')

conteudo = arquivo1.read()

print(f'tipo de conteudo: {type(conteudo)}')

print('conteudo retornado pelo read:')
print(repr(conteudo))

arquivo1.close()

print('\n--------\n')
conteudo2 = arquivo2.readline()

print(f'tipo do conteudo2: {type(conteudo2)}')
print('conteudo retornado pelo readline:')
print(repr(conteudo2))

proximo_conteudo2 = arquivo2.readline()
print('proximo conteudo retornado:')
print(repr(proximo_conteudo2))

proximo_conteudo2 = arquivo2.readline()
print('proximo conteudo retornado:')
print(repr(proximo_conteudo2))

arquivo2.close()

print('\n--------\n')
conteudo3 = arquivo3.readlines()

print(f'tipo do conteudo3: {type(conteudo3)}')
print('conteudo retornado pelo readlines:')
print(repr(conteudo3))


arquivo3.close()
print('-------- fim ------------')

"""
-------- inicio ------------
tipo de conteudo: <class 'str'>
conteudo retornado pelo read:
'Vinicios de Morais - A casa\n*\nEra uma casa muito engraÃ§ada\nNÃ£o tinha teto, nÃ£o tinha nada\nNinguÃ©m podia entra nela nÃ£o\nPorque na casa nÃ£o tinha chÃ£o\nNinguÃ©m podia dormir na rede\nPorque na casa nÃ£o tinha parede\nNinguÃ©m podia fazer pipi\nPorque pinico nÃ£o tinha ali\nMas era feita com muito esmero\nNa Rua dos Bobos, nÃºmero zero\nMas era feita com muito esmero\nNa Rua dos Bobos, nÃºmero zero'

--------

tipo do conteudo2: <class 'str'>
conteudo retornado pelo readline:
'Vinicios de Morais - A casa\n'
proximo conteudo retornado:
'*\n'
proximo conteudo retornado:
'Era uma casa muito engraÃ§ada\n'

--------

tipo do conteudo3: <class 'list'>
conteudo retornado pelo readlines:
['Vinicios de Morais - A casa\n', '*\n', 'Era uma casa muito engraÃ§ada\n', 'NÃ£o tinha teto, nÃ£o tinha nada\n', 'NinguÃ©m podia entra nela nÃ£o\n', 'Porque na casa nÃ£o tinha chÃ£o\n', 'NinguÃ©m podia dormir na rede\n', 'Porque na casa nÃ£o tinha parede\n', 'NinguÃ©m podia fazer pipi\n', 'Porque pinico nÃ£o tinha ali\n', 'Mas era feita com muito esmero\n', 'Na Rua dos Bobos, nÃºmero zero\n', 'Mas era feita com muito esmero\n', 'Na Rua dos Bobos, nÃºmero zero']
-------- fim ------------

"""
