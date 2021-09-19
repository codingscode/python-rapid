

import sqlite3 as conector

# abertura de conexao e aquisicao de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# execucao de um comando: SELECT... CREATE...
comando1 = '''
DROP TABLE Veiculo;
'''

cursor.execute(comando1)

comando2 = '''
CREATE TABLE Veiculo (
    placa CHARACTER(7) NOT NULL,
    ano INTEGER NOT NULL,
    cor TEXT NOT NULL,
    motor REAL NOT NULL,
    proprietario INTEGER NOT NULL,
    marca INTEGER NOT NULL,
    PRIMARY KEY (placa),
    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
    FOREIGN KEY(marca) REFERENCES Marca(id)
);
'''

cursor.execute(comando2)

# efetivacao do comando
conexao.commit()

# fechamento das conexoes
cursor.close()
conexao.close()

