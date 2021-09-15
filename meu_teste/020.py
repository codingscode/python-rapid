import os


print('------------- inicio ---------------')

try:
    os.rename('020_arquivo.txt', '020_arquivo2.txt')
    print('arquivo renomeado!')
except FileNotFoundError as erro:
    print('arquivo inexistente')
    print(f'descricao: {erro}')
except PermissionError as erro:
    print('sem permissão para acessar o arquivo')
    print(f'descricao: {erro}')
except FileExistsError as erro:
    print('arquivo destino já existe')
    print(f'descricao: {erro}')

print('--------------- fim ---------------')
    
"""
------------- inicio ---------------
arquivo renomeado!
--------------- fim ---------------


------------- inicio ---------------
arquivo destino já existe
descricao: [WinError 183] Não é possível criar um arquivo já existente: '020_arquivo.txt' -> '020_arquivo2.txt'
--------------- fim ---------------


------------- inicio ---------------
arquivo inexistente
descricao: [WinError 2] O sistema não pode encontrar o arquivo especificado: '020_arquivo.txt' -> '020_arquivo2.txt'
--------------- fim ---------------


"""