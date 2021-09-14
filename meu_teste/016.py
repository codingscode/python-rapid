from datetime import datetime

print('----------- inicio ------------')

frutas = ['jabuticaba', 'laranja', 'ata', 'jaca', 'graviola']

for cada in frutas:
    minha_fruta = f'Nome: {cada:12} - número de letras: {len(cada): 3}'
    print(minha_fruta)

print()

pi = 3.14159265359

meu_numero = f'o numero pi é: {pi:.1f}'
meu_numero_deslocado = f'o numero pi deslocado é: {pi:6.1f}'
meu_numero_preciso = f'o numero pi mais preciso é: {pi:.4f}'
print(meu_numero_deslocado)
print(meu_numero_preciso)

print()

data = datetime.now()
minha_data = f'a data de hoje é {data}'
minha_data_formatada = f'a data de hoje formatada é {data:%d/%m/%Y}'
print(minha_data)
print(minha_data_formatada)

print('------------- fim ------------')

"""
----------- inicio ------------
Nome: jabuticaba   - número de letras:  10
Nome: laranja      - número de letras:   7
Nome: ata          - número de letras:   3
Nome: jaca         - número de letras:   4
Nome: graviola     - número de letras:   8

o numero pi deslocado é:    3.1
o numero pi mais preciso é: 3.1416

a data de hoje é 2021-09-14 11:25:02.539982
a data de hoje formatada é 14/09/2021
------------- fim ------------
"""