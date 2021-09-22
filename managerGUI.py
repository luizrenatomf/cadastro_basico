import sqlite3
from contextlib import closing
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#inicio da interface gráfica
menuInicial = Tk()

def pesquisar():
	nome = str(nomeDoCliente.get())
	telefone = str(telefoneDoCliente.get())

	if nome != '':
		with sqlite3.connect("cadastro.db") as conexao:
			with closing(conexao.cursor()) as cursor:
				cursor.execute(f'select * from cadastro where nome = ?',(nome,))
				x = 0
				while True:
					resultado = cursor.fetchone()
					if resultado is None:
						if x == 0:
							messagebox.showwarning("Aviso!",'Cadastro não encontrado!')
						break				
					codigo = resultado[0]
					nome = resultado[1]
					telefone = resultado[2]
					cidade = resultado[3]
					x += 1
					resposta(codigo,nome,telefone,cidade)
	elif telefone != '':
		with sqlite3.connect("cadastro.db") as conexao:
			with closing(conexao.cursor()) as cursor:
				cursor.execute(f'select * from cadastro where telefone = ?',(telefone,))
				x = 0
				while True:
					resultado = cursor.fetchone()
					if resultado is None:
						if x == 0:
							messagebox.showwarning("Aviso!",'Cadastro não encontrado!')
						break
					codigo = resultado[0]
					nome = resultado[1]
					telefone = resultado[2]
					cidade = resultado[3]
					x += 1
					resposta(codigo,nome,telefone,cidade)

	nomeDoCliente.delete(0, 'end')
	telefoneDoCliente.delete(0, 'end')
	cidadeDoCliente.delete(0, 'end')

def incluir ():
	nome = str(nomeDoCliente.get())
	telefone = str(telefoneDoCliente.get())
	cidade = str(cidadeDoCliente.get())

	with sqlite3.connect("cadastro.db") as conexao:
		with closing(conexao.cursor()) as cursor:
			cursor.execute("insert into cadastro (nome, telefone, cidade) values (?,?,?)",(nome,telefone,cidade))
			conexao.commit()
			messagebox.showinfo("Cadastro de clientes",'Cadastro realizado.')

	nomeDoCliente.delete(0, 'end')
	telefoneDoCliente.delete(0, 'end')
	cidadeDoCliente.delete(0, 'end')

def editar ():
	nome = str(nomeDoCliente.get())
	telefone = str(telefoneDoCliente.get())
	cidade = str(cidadeDoCliente.get())

	with sqlite3.connect("cadastro.db") as conexao:
		with closing(conexao.cursor()) as cursor:
			cursor.execute('select * from cadastro where nome = ?', (nome,))
			x = 0
			while True:
				resultado = cursor.fetchone()
				if resultado is None:
					if x == 0:
						messagebox.showwarning("Aviso!",'Cadastro não encontrado!')
					break
				x += 1

				if resultado:
					cursor.execute(f'update cadastro set telefone = {telefone} where nome = ?',(nome,))
					if cursor.rowcount == 1:
						conexao.commit()
						messagebox.showinfo("Cadastro de clientes",'Cadastro atualizado com sucesso.')
						break
					else:
						conexao.rollback()
						messagebox.showwarning("Aviso!",'Alteração cadastral não realizada.')

	nomeDoCliente.delete(0, 'end')
	telefoneDoCliente.delete(0, 'end')
	cidadeDoCliente.delete(0, 'end')
	nomeDoCliente.focus()

def desativar ():
	nome = str(nomeDoCliente.get())

	with sqlite3.connect("cadastro.db") as conexao:
		with closing(conexao.cursor()) as cursor:
			cursor.execute("delete from cadastro where nome = ?",(nome,))
			if cursor.rowcount == 1:
				conexao.commit()
				messagebox.showinfo("Cadastro de clientes",'Cadastro removido com sucesso.')
			else:
				conexao.rollback()
				messagebox.showwarning("Aviso!",'Alteração cadastral não realizada.')

	nomeDoCliente.delete(0, 'end')
	telefoneDoCliente.delete(0, 'end')
	cidadeDoCliente.delete(0, 'end')

def sair ():
	menuInicial.destroy()

def resposta(codigo,nome,telefone,cidade):
	resposta = tk.Toplevel(menuInicial)
	resposta.title("Cliente: " + nome)
	resposta.resizable(True, False)
	resposta.iconbitmap("imagens/icon.ico")

#dimensões da janela e posicionamento
	largura = 300
	altura = 120
	larguraScreen = menuInicial.winfo_screenwidth() #resolução do sistema
	alturaScreen = menuInicial.winfo_screenheight() #resolução do sistema
	posx = int(larguraScreen/2 - largura/2) #posicionamento da janela
	posy = int(alturaScreen/2 - altura/2) #posicionamento da janela
	resposta.geometry(f"{largura}x{altura}+{posx}+{posy}") 
	
	label10 = Label(
		resposta,
		text='Código: ' + str(codigo),
		font="Times 15",
		width=25,
		anchor=CENTER
	).pack()
	label11 = Label(
		resposta,
		text='Nome: ' + nome,
		font="Times 15",
		width=25,
		anchor=CENTER
	).pack()
	label12 = Label(
		resposta,
		text='Telefone: ' + telefone,
		font="Times 15",
		width=25,
		anchor=CENTER
	).pack()
	label13 = Label(
		resposta,
		text='Cidade: ' + cidade,
		font="Times 15",
		width=25,
		anchor=CENTER
	).pack()

#configuração da interface básica
menuInicial.title("Cadastro de clientes")
menuInicial.resizable(False, False)
menuInicial.iconbitmap("imagens/icon.ico")

#dimensões da janela e posicionamento
largura = 500
altura = 600
larguraScreen = menuInicial.winfo_screenwidth() #resolução do sistema
alturaScreen = menuInicial.winfo_screenheight() #resolução do sistema
posx = int(larguraScreen/2 - largura/2) #posicionamento da janela
posy = int(alturaScreen/2 - altura/2) #posicionamento da janela
menuInicial.geometry(f"{largura}x{altura}+{posx}+{posy}") 


#label
label0 = Label(
	menuInicial,
	text="Cadastro de clientes",
	font="Times 25 bold",
	bd=3,
	relief="raised",
	width=20,
	height=2,
).place(x = 50, y = 20)

label1 = Label(
	menuInicial,
	text="Nome do cliente",
	font="Times 15 bold",
	width=15,
	anchor=CENTER
).place(x=10,y=150)

label2 = Label(
	menuInicial,
	text="Telefone",
	font="Times 15 bold",
	width=15,
	anchor=CENTER
).place(x=10,y=190)

label3 = Label(
	menuInicial,
	text="Cidade",
	font="Times 15 bold",
	width=15,
	anchor=CENTER
).place(x= 10,y=230)

label4 = Label(
	menuInicial,
	text="Projeto realizado por Luiz Renato Miranda Ferreira",
	font="Times 10",
	width=60,
	anchor=CENTER
).place(x= 50,y=550)

label5 = Label(
	menuInicial,
	text="Concorrência a vaga de estágio na empresa Cândido Empresarial",
	font="Times 10",
	width=60,
	anchor=CENTER
).place(x= 50,y=570)

#entry
nomeDoCliente = Entry(
	menuInicial, 
	width=25,
	bg='white',
	font="Times 15"
)
nomeDoCliente.place(x=200,y=150)

telefoneDoCliente = Entry(
	menuInicial,
	width=25,
	bg='white',
	font='Times 15'
)
telefoneDoCliente.place(x=200,y=190)

cidadeDoCliente = ttk.Combobox(
	menuInicial,
	width=23,
	font='Times 15',
	values=[
			"Uberaba",
			"Uberlândia",
			"Araxá"])
cidadeDoCliente.place(x=200,y=230)

label3 = Label(menuInicial, text="Cidade")

#botões
btn1 = Button(
	menuInicial,
	text="Pesquisar",
	width=25,
	font="Times 15",
	command=pesquisar
).place(x=115,y=290)

btn2 = Button(
	menuInicial, 
	text="Incluir", 
	width=25,
	font="Times 15",
	command=incluir
).place(x=115,y=340)

btn3 = Button(
	menuInicial, 
	text="Editar", 
	width=25,
	font="Times 15",
	command=editar
).place(x=115,y=390)

btn4 = Button(
	menuInicial, 
	text="Desativar", 
	width=25,
	font="Times 15",
	command=desativar
).place(x=115,y=440)

btn5 = Button(
	menuInicial, 
	text="Sair", 
	width=25,
	font="Times 15",
	command=sair
).place(x=115,y=490)

nomeDoCliente.focus()
menuInicial.mainloop()
