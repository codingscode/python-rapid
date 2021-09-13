arquivo = open('003.txt', 'r')


print('iterando sobre o arquivo')
for i, cada in enumerate(arquivo):
    print(f'{i}: {repr(cada)}')

arquivo.close()

"""
iterando sobre o arquivo
0: 'Vinicios de Morais - A casa\n'
1: '*\n'
2: 'Era uma casa muito engraÃ§ada\n'
3: 'NÃ£o tinha teto, nÃ£o tinha nada\n'
4: 'NinguÃ©m podia entra nela nÃ£o\n'
5: 'Porque na casa nÃ£o tinha chÃ£o\n'
6: 'NinguÃ©m podia dormir na rede\n'
7: 'Porque na casa nÃ£o tinha parede\n'
8: 'NinguÃ©m podia fazer pipi\n'
9: 'Porque pinico nÃ£o tinha ali\n'
10: 'Mas era feita com muito esmero\n'
11: 'Na Rua dos Bobos, nÃºmero zero\n'
12: 'Mas era feita com muito esmero\n'
13: 'Na Rua dos Bobos, nÃºmero zero'


"""

