
import psycopg2


conn = psycopg2.connect(database = "postgres", user = "postgres", password = "din1", host = "127.0.0.1", port = "5432")

print ("Conexão com o Banco de Dados aberta com sucesso!")

cur = conn.cursor()
cur.execute("""INSERT INTO public."AGENDA" ("id", "nome", "telefone") VALUES (1, 'Pessoa 1', '02199999999')""")
conn.commit()

print("Inserção realizada com sucesso!");

conn.close()


"""
deixar psql ligado
python arq003.py

Conexão com o Banco de Dados aberta com sucesso!
Inserção realizada com sucesso!

"""
