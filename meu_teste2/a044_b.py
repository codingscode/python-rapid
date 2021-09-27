from a032_modelo import Veiculo, Marca


def recuperar_veiculos(conexao, cpf):
    # aquisicao de cursor
    cursor = conexao.cursor()

    # definicao dos comandos
    comando = '''
    SELECT * FROM Veiculo JOIN Marca ON Marca.id = Veiculo.marca WHERE Veiculo.proprietario = ?;
    '''
    cursor.execute(comando, (cpf,))

    # recuperacao dos registros
    veiculos = []
    registros = cursor.fetchall()
    for registro in registros:
        marca = Marca(*registro[6:])
        veiculo = Veiculo(*registro[:5], marca)
        veiculos.append(veiculo)

    # fechamento do cursor
    cursor.close()
    return veiculos