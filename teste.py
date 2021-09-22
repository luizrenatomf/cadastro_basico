import sqlite3
from contextlib import closing
import tkinter as tk
from tkinter import *
from tkinter import ttk

class principal:
	def __init__(self, master):
            self.master = master
            self.frame = tk.Frame(self.master)		
            self.cabecalho = tk.Label(self.frame, text = 'Cadastro de clientes', font = 'Times 25 bold', bd = 3, relief = 'solid', width = 20, height = 2).pack()#place(x = 50, y = 20)
            self.labelNomeCliente = tk.Label(self.frame, text= 'Nome do cliente', font="Times 15 bold", width=15, anchor = CENTER).pack()#place(x=10,y=150) )
            self.entryNomeCliente = tk.Entry(self.frame, width = 25, bg = 'white', font = 'Times 15').pack()
            self.labelTelefone = tk.Label(self.frame, text = 'Telefone', font = 'Times 15 bold', width = 15, anchor = CENTER).pack()
            self.entryTelefone = tk.Entry(self.frame, width = 25, bg = 'white', font = 'Times 15').pack()
            self.labelCidade = tk.Label(self.frame, text = 'Cidade', font = 'Times 15 bold', width = 15, anchor = CENTER).pack()
            self.comboboxCidade = ttk.Combobox(self.frame, width = 23, font = 'Time 15', values = ['Uberaba','Uberlândia','Araxá']).pack()
            self.buttonPesquisar = tk.Button(self.frame, text = 'Pesquisar', font = 'Times 15', width = 25, command = self.pesquisar).pack()#place(x = 100, y = 320)
            self.frame.pack()

	def pesquisar(self):
            self.pesquisar = tk.Toplevel(self.master)
            nome = str(entryNomeCliente.get())

            with sqlite3.connect("cadastro.db") as conexao:
                with closing(conexao.cursor()) as cursor:
                    cursor.execute(f'select * from cadastro where nome = ?',(nome,))
                    x = 0
                    while True:
                        resultado = cursor.fetchone()
                        informacoesCliente()
                        if resultado is None:
                            if x == 0:
                                print("Nada encontrado.")
                            break
                        print(f"Código: {resultado[0]}\nNome: {resultado[1]}\nTelefone: {resultado[2]}\nCidade: {resultado[3]}")
                        x += 1
            self.app = pesquisar(self.pesquisar)

class pesquisar:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.labelResultado1 = tk.Label(self.frame, text = 'nome')
        self.frame.pack()

    def pesquisa(self):
        self.master.destroy()

root = Tk()

root.title("window")

root.geometry("500x600+990+540")

cls = principal(root)

root.mainloop()