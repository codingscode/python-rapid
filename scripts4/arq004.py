
import psycopg2


conn = psycopg2.connect(database = "postgres", user = "postgres", password = "din1", host = "127.0.0.1", port = "5432")

print ("Conexão com o Banco de Dados aberta com sucesso!")

cur = conn.cursor()
cur.execute("""select * from public."AGENDA" where "id" = 1""")
registro = cur.fetchone()

print(registro)

conn.commit()

print("Seleção realizada com sucesso!");

conn.close()


"""
deixar psql ligado
python arq004.py

Conexão com o Banco de Dados aberta com sucesso!
(1, 'teste 1', '02199999999 ')
Seleção realizada com sucesso!

"""
