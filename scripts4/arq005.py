
import psycopg2


conn = psycopg2.connect(database = "postgres", user = "postgres", password = "din1", host = "127.0.0.1", port = "5432")

print ("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()

print("Consulta antes da atualização")
cur.execute("""select * from public."AGENDA" where "id" = 1""")
registro = cur.fetchone()

print(registro)

#Atualização de um único registro
cur.execute("""Update public."AGENDA" set "telefone" = '02188888888' where "id" = 1""")
conn.commit()

print("Registro Atualizado com sucesso! ")
cur = conn.cursor()

print("Consulta depois da atualização")
cur.execute("""select * from public."AGENDA" where "id" = 1""")
registro = cur.fetchone()

print(registro)
conn.commit()
print("Seleção realizada com sucesso!");
conn.close()


"""
deixar psql ligado
python arq005.py


Conexão com o Banco de Dados aberta com sucesso!
Consulta antes da atualização
(1, 'teste 1', '02199999999 ')
Registro Atualizado com sucesso!
Consulta depois da atualização
(1, 'teste 1', '02188888888 ')
Seleção realizada com sucesso!


"""
