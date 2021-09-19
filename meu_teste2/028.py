
import sqlite3 as conector

# abertura de conexao e aquisicao de cursor
conexao = conector.connect('./026meu_banco.db')
cursor = conexao.cursor()

# execucao de um comando: SELECT... CREATE...
comando = '''
CREATE TABLE Veiculo (
    placa CHARACTER(7) NOT NULL,
    ano INTEGER NOT NULL,
    cor TEXT NOT NULL,
    proprietario INTEGER NOT NULL,
    marca INTEGER NOT NULL,
    PRIMARY KEY (placa),
    FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
    FOREIGN KEY(marca) REFERENCES Marca(id)
);
'''

cursor.execute(comando)

# efetivacao do comando
conexao.commit()

# fechamento das conexoes
cursor.close()
conexao.close()

