import sqlite3
from contextlib import closing

with sqlite3.connect("cadastro.db") as conexao:
	with closing(conexao.cursor()) as cursor:
		cursor.execute('''
			create table cadastro(
				codigo integer primary key autoincrement,
				nome text not null,
				telefone text not null,
				cidade text)
				''')
conexao.commit()
cursor.close()
conexao.close()