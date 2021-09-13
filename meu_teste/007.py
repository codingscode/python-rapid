
arquivo_escrita = open('007_arquivo.txt', 'w')

linhas = [
   'o rato roeu\n', 'a roupa do rei\n', 'de roma'
]

print('--------- inicio ----------')

arquivo_escrita.writelines(linhas)
arquivo_escrita.close()

print('---------- fim ------------')
# conteudo escrito

"""
--------- inicio ----------
---------- fim ------------

"""

