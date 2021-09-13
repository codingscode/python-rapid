
arquivo = open('003.txt', 'r')


print('--------- inicio ---------')

conteudo = arquivo.read()

print('todo o conteudo do arquivo:')
print(repr(conteudo), '\n')

conteudo_releitura = arquivo.read()
print('releitura de todo o conteudo do arquivo')
print(repr(conteudo_releitura), '\n')

arquivo.close()

print('\n-------------\n')

arquivo_reaberto = open('003.txt', 'r')
conteudo_reaberto = arquivo_reaberto.read()
print('todo o conteudo do arquivo novamente')
print(repr(conteudo_reaberto), '\n')

arquivo_reaberto.seek(0)
conteudo_seek = arquivo_reaberto.read()
print('Todo o conteudo do arquivo após o Seek')
print(repr(conteudo_seek))

arquivo_reaberto.close()

print('---------- fim -----------')



"""
--------- inicio ---------
todo o conteudo do arquivo:
'Vinicios de Morais - A casa\n*\nEra uma casa muito engraÃ§ada\nNÃ£o tinha teto, nÃ£o tinha nada\nNinguÃ©m podia entra nela nÃ£o\nPorque na casa nÃ£o tinha chÃ£o\nNinguÃ©m podia dormir na rede\nPorque na casa nÃ£o tinha parede\nNinguÃ©m podia fazer pipi\nPorque pinico nÃ£o tinha ali\nMas era feita com muito esmero\nNa Rua dos Bobos, nÃºmero zero\nMas era feita com muito esmero\nNa Rua dos Bobos, nÃºmero zero'

releitura de todo o conteudo do arquivo
''


-------------

todo o conteudo do arquivo novamente
'Vinicios de Morais - A casa\n*\nEra uma casa muito engraÃ§ada\nNÃ£o tinha teto, nÃ£o tinha nada\nNinguÃ©m podia entra nela nÃ£o\nPorque na casa nÃ£o tinha chÃ£o\nNinguÃ©m podia dormir na rede\nPorque na casa nÃ£o tinha parede\nNinguÃ©m podia fazer pipi\nPorque pinico nÃ£o tinha ali\nMas era feita com muito esmero\nNa Rua dos Bobos, nÃºmero zero\nMas era feita com muito esmero\nNa Rua dos Bobos, nÃºmero zero'

Todo o conteudo do arquivo após o Seek
'Vinicios de Morais - A casa\n*\nEra uma casa muito engraÃ§ada\nNÃ£o tinha teto, nÃ£o tinha nada\nNinguÃ©m podia entra nela nÃ£o\nPorque na casa nÃ£o tinha chÃ£o\nNinguÃ©m podia dormir na rede\nPorque na casa nÃ£o tinha parede\nNinguÃ©m podia fazer pipi\nPorque pinico nÃ£o tinha ali\nMas era feita com muito esmero\nNa Rua dos Bobos, nÃºmero zero\nMas era feita com muito esmero\nNa Rua dos Bobos, nÃºmero zero'
---------- fim -----------

"""

