print('iterando sobre o arquivo')

with open ('009_texto.txt', 'r') as arquivo:
    print(type(arquivo))
    for linha in list(arquivo):
        print(linha)
    print(f'*** fim do arquivo {arquivo.name} ***')

"""
iterando sobre o arquivo
Vinicios de Morais - A casa

*

Era uma casa muito engraÃ§ada

NÃ£o tinha teto, nÃ£o tinha nada

NinguÃ©m podia entra nela nÃ£o

Porque na casa nÃ£o tinha chÃ£o

NinguÃ©m podia dormir na rede

Porque na casa nÃ£o tinha parede

NinguÃ©m podia fazer pipi

Porque pinico nÃ£o tinha ali

Mas era feita com muito esmero

Na Rua dos Bobos, nÃºmero zero

Mas era feita com muito esmero

Na Rua dos Bobos, nÃºmero zero
*** fim do arquivo 009_texto.txt ***

"""
