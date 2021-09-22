import sqlite3
from contextlib import closing

def pesquisar (nome):
	with sqlite3.connect("cadastro.db") as conexao:
		with closing(conexao.cursor()) as cursor:
			cursor.execute(f'select * from cadastro where nome = ?',(nome,))
			x = 0
			while True:
				resultado = cursor.fetchone()
				if resultado is None:
					if x == 0:
						print("Nada encontrado.")
					break
				print(f"Código: {resultado[0]}\nNome: {resultado[1]}\nTelefone: {resultado[2]}\nCidade: {resultado[3]}")
				x += 1

def incluir (nome, telefone, cidade):
	with sqlite3.connect("cadastro.db") as conexao:
		with closing(conexao.cursor()) as cursor:
			cursor.execute('''insert into cadastro (nome, telefone, cidade) values (?,?,?)''',(nome,telefone,cidade))
			conexao.commit()
			print("Cadastro realizado.")

def editar (nome, campo, atual):
	with sqlite3.connect("cadastro.db") as conexao:
		with closing(conexao.cursor()) as cursor:
			cursor.execute('select * from cadastro where nome = ?', (nome,))
			x = 0
			while True:
				resultado = cursor.fetchone()
				if resultado is None:
					if x == 0:
						print("Cadastro não encontrado.")
					break
				x += 1

				if resultado:
					cursor.execute(f'update cadastro set {campo} = {atual} where nome = ?',(nome,))
					print("Registros alterados: ", cursor.rowcount)
					if cursor.rowcount == 1:
						conexao.commit()
						print("Alteração realizada.")
						break
					else:
						conexao.rollback()
						print("Alteração abortada.")
				

def desativar (nome):
	with sqlite3.connect("cadastro.db") as conexao:
		with closing(conexao.cursor()) as cursor:
			cursor.execute("delete from cadastro where nome = ?",(nome,))
			print("Registros alterados: ",cursor.rowcount)
			if cursor.rowcount == 1:
				conexao.commit()
				print("Alteração realizada.")
			else:
				conexao.rollback()
				print("Alteração abortada.")

print("1 - Pesquisar")
print("2 - Incluir")
print("3 - Editar")
print("4 - Desativar")
print("5 - Encerrar")
opcao = int(input("Qual a sua escolha? "))

while opcao != 5:
	if opcao == 1:
	 	nome = input("Informe o nome a ser consultado: ")
	 	pesquisar(nome)

	if opcao == 2:
		nome = input("Nome: ")
		telefone = input("Telefone: ")
		cidade = input("Cidade:")
		incluir(nome, telefone, cidade)

	if opcao == 3:
		nome = input("Informe o nome do cadastro para alterar: ")
		campo = input("Informe o campo a atualizar: ")
		atual = input(f"Digite {campo} atualizado: ")
		editar(nome, campo, atual)

	if opcao == 4:
		nome = input("Informe o nome do cadastro a ser desativado: ")
		desativar(nome)

	print("1 - Pesquisar")
	print("2 - Incluir")
	print("3 - Editar")
	print("4 - Desativar")
	print("5 - Encerrar")
	opcao = int(input("Qual a sua escolha? "))
