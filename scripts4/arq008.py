
from faker import Faker
import psycopg2


conn = psycopg2.connect(database = "postgres", user="postgres", password="din1", host="127.0.0.1", port="5432")

print("Conexão aberta com sucesso!")
cursor = conn.cursor()
fake = Faker('pt_BR')

n = 10

for i in range(n):
    codigo = i + 10
    nome = 'produto_' + str(i+1)
    preco = fake.pyfloat(left_digits=3, right_digits=2, positive=True, min_value=5, max_value=1000)
    print(preco)
    print(nome)

    comandoSQL = """INSERT INTO PRODUTO(CODIGO, NOME, PRECO) VALUES (%s, %s, %s) """

    registro = (codigo, nome, preco)
    cursor.execute(comandoSQL, registro)

conn.commit()
print("Inserção realizada com sucesso!")
conn.close()


"""

python arq008.py


Conexão aberta com sucesso!
204.9
produto_1
796.97
produto_2
372.69
produto_3
459.7
produto_4
505.7
produto_5
555.22
produto_6
966.44
produto_7
439.51
produto_8
513.44
produto_9
915.15
produto_10
Inserção realizada com sucesso!



"""
