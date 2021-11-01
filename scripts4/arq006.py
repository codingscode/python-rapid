import psycopg2


conn = psycopg2.connect(database = "postgres", user = "postgres", password = "din1", host = "127.0.0.1", port = "5432")

print ("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute("""Delete from public."AGENDA" where "id" = 1""")
conn.commit()
cont = cur.rowcount

print(cont, "Registro excluído com sucesso! ")
print("Exclusão realizada com sucesso!")

conn.close()


"""
deixar psql ligado
python arq006.py

Conexão com o Banco de Dados aberta com sucesso!
2 Registro excluído com sucesso!
Exclusão realizada com sucesso!

"""
