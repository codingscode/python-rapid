
import os

print('----------- inicio ---------------')

try:
    entradas = os.scandir('024_diretorio')  # se fosse ele mesmo seria '.'

    for obj in entradas:
        print(obj)
        print(f'Nome: {obj.name}')
        print(f'Caminho: {obj.path}')
        print(f'É diretório: {obj.is_dir()}')
        print(f'É arquivo: {obj.is_file()}')
        
        if obj.is_file():
            print(f'Tamanho: {obj.stat().st_size}B')
        print('======================')

except FileNotFoundError:
    print('o caminho não existe.')
except NotADirectoryError:
    print('o caminho não é de um diretório.')

print('-------------- fim ---------------')

"""
----------- inicio ---------------
<DirEntry 'a.txt'>
Nome: a.txt
Caminho: 024_diretorio\a.txt
É diretório: False
É arquivo: True
Tamanho: 0B
======================
<DirEntry 'b.txt'>
Nome: b.txt
Caminho: 024_diretorio\b.txt
É diretório: False
É arquivo: True
Tamanho: 43B
======================
<DirEntry 'c.py'>
Nome: c.py
Caminho: 024_diretorio\c.py
É diretório: False
É arquivo: True
Tamanho: 0B
======================
<DirEntry 'outro_diretorio'>
Nome: outro_diretorio
Caminho: 024_diretorio\outro_diretorio
É diretório: True
É arquivo: False
======================
-------------- fim ---------------
"""
