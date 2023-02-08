# AULA 014 - Criando função do botão Buscar

from tkinter import *
from tkinter import ttk
import sqlite3

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser


root = Tk()


class Relatorios:
    def printCliente(self):
        webbrowser.open("cliente.pdf")

    def gerarRelatorioCliente(self):
        self.c = canvas.Canvas("cliente.pdf")

        self.codigoRelatorio = self.en_codigo.get()
        self.nomeRelatorio = self.en_nome.get()
        self.telefoneRelatorio = self.en_telefone.get()
        self.cidadeRelatorio = self.en_cidade.get()

        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(200, 790, "Ficha do Cliente")

        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, "Código: ")
        self.c.drawString(50, 670, "Nome: ")
        self.c.drawString(50, 640, "Telefone: ")
        self.c.drawString(50, 610, "Cidade: ")

        self.c.setFont("Helvetica", 18)
        self.c.drawString(140, 700, self.codigoRelatorio)
        self.c.drawString(140, 670, self.nomeRelatorio)
        self.c.drawString(140, 640, self.telefoneRelatorio)
        self.c.drawString(140, 610, self.cidadeRelatorio)

        self.c.rect(20, 550, 550, 5, fill=True, stroke=False)

        self.c.showPage()
        self.c.save()
        self.printCliente()


class Funcs:
    def limpar_tela(self):
        self.en_codigo.delete(0, END)
        self.en_nome.delete(0, END)
        self.en_telefone.delete(0, END)
        self.en_cidade.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor()
        print("Conectando ao banco de dados...")

    def desconecta_db(self):
        self.conn.close()
        print("Banco de dados desconectado...")

    def montaTabelas(self):
        self.conecta_bd()
        ### tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit()
        print("Banco de dados criado!")
        self.desconecta_db()

    def variaveis(self):
        self.codigo = self.en_codigo.get()
        self.nome = self.en_nome.get()
        self.telefone = self.en_telefone.get()
        self.cidade = self.en_cidade.get()

    def add_cliente(self):
        self.variaveis()

        self.conecta_bd()
        self.cursor.execute("""
            INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES(?, ?, ?)
        """, (self.nome, self.telefone, self.cidade))

        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpar_tela()

    def select_lista(self):
        self.listCli.delete(*self.listCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""
        SELECT cod, nome_cliente, telefone, cidade FROM clientes
        ORDER BY nome_cliente ASC;
        """)
        for i in lista:
            self.listCli.insert("", END, values=i)

        self.desconecta_db()

    def OnDoubleClick(self, event):
        self.limpar_tela()
        self.listCli.selection()

        for n in self.listCli.selection():
            col1, col2, col3, col4 = self.listCli.item(n, 'values')
            self.en_codigo.insert(END, col1)
            self.en_nome.insert(END, col2)
            self.en_telefone.insert(END, col3)
            self.en_cidade.insert(END, col4)

    def delete_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute("""
            DELETE FROM clientes WHERE cod = ?
        """, (self.codigo))

        self.conn.commit()

        self.desconecta_db()
        self.limpar_tela()
        self.select_lista()

    def alterar_cliente(self):
        self.variaveis()
        self.conecta_bd()

        self.cursor.execute("""
                UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
                WHERE cod = ?
            """, (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpar_tela()

    def buscar_cliente(self):
        self.conecta_bd()

        self.listCli.delete(*self.listCli.get_children())
        self.en_nome.insert(END, '%')
        nome = self.en_nome.get()
        self.cursor.execute(
            f""" 
                SELECT cod, nome_cliente, telefone, cidade FROM clientes 
                WHERE nome_cliente LIKE '{nome}' ORDER BY nome_cliente ASC
            """)
        buscaNomeCli = self.cursor.fetchall()
        for i in buscaNomeCli:
            self.listCli.insert("", END, values=i)

        self.limpar_tela()
        self.desconecta_db()


class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.menu_horizontal()
        mainloop()

    def tela(self):
        self.root.title("Registrar Clientes")
        self.root.configure(background="#1e4392")
        self.root.geometry("640x480")
        # self.root.resizable(False, False)
        self.root.maxsize(width=700, height=500)
        self.root.minsize(width=600, height=400)

    def frames(self):
        self.frame1 = Frame(self.root)
        self.frame1.place(relwidth=0.95, relheight=0.45,
                          relx=0.025, rely=0.025)

        self.frame2 = Frame(self.root)
        self.frame2.place(relwidth=0.95, relheight=0.45,
                          relx=0.025, rely=0.5)

    def widgets_frame1(self):
        # tamanhão do botão padrão
        self.bt_width = 0.1
        self.bt_height = 0.13
        # botão limpar
        self.bt_limpar = Button(self.frame1, text="LIMPAR",
                                bd=2, bg="#0a3eaa", fg="#ffffff",
                                font=("verdana", 9, "bold"), command=self.limpar_tela)
        self.bt_limpar.place(relwidth=self.bt_width, relheight=self.bt_height,
                             relx=0.2, rely=0.05)
        # botão buscar
        self.bt_buscar = Button(self.frame1, text="BUSCAR", bd=2, bg="#0a3eaa", fg="#ffffff",
                                font=("verdana", 9, "bold"), command=self.buscar_cliente)
        self.bt_buscar.place(relwidth=self.bt_width, relheight=self.bt_height,
                             relx=0.31, rely=0.05)
        # botão novo
        self.bt_novo = Button(self.frame1, text="NOVO", bd=2, bg="#0a3eaa", fg="#ffffff",
                              font=("verdana", 9, "bold"), command=self.add_cliente)
        self.bt_novo.place(relwidth=self.bt_width, relheight=self.bt_height,
                           relx=0.6, rely=0.05)
        # botão alterar
        self.bt_alterar = Button(self.frame1, text="ALTERAR", bd=2, bg="#0a3eaa", fg="#ffffff",
                                 font=("verdana", 9, "bold"), command=self.alterar_cliente)
        self.bt_alterar.place(relwidth=self.bt_width, relheight=self.bt_height,
                              relx=0.71, rely=0.05)
        # botão apagar
        self.bt_apagar = Button(self.frame1, text="APAGAR", bd=2, bg="#0a3eaa", fg="#ffffff",
                                font=("verdana", 9, "bold"), command=self.delete_cliente)
        self.bt_apagar.place(relwidth=self.bt_width, relheight=self.bt_height,
                             relx=0.82, rely=0.05)


        # label codigo
        self.lb_codigo = Label(self.frame1, text="Código",
                               fg="#1e2e3e")
        self.lb_codigo.place(relwidth=0.1, relheight=0.1,
                             relx=0.01, rely=0.05)
        # label nome
        self.lb_nome = Label(self.frame1, text="Nome", fg="#1e2e3e")
        self.lb_nome.place(relwidth=0.1, relheight=0.1,
                           relx=0.01, rely=0.3)
        # label telefone
        self.lb_telefone = Label(self.frame1, text="Telefone", fg="#1e2e3e")
        self.lb_telefone.place(relwidth=0.1, relheight=0.1,
                               relx=0.01, rely=0.6)
        # label cidade
        self.lb_cidade = Label(self.frame1, text="Cidade", fg="#1e2e3e")
        self.lb_cidade.place(relwidth=0.1, relheight=0.1,
                             relx=0.5,rely=0.6)


        # entry codigo
        self.en_codigo = Entry(self.frame1, fg="#1e2e3e")
        self.en_codigo.place(relwidth=0.1, relheight=0.08,
                             relx=0.02, rely=0.15)
        # entry nome
        self.en_nome = Entry(self.frame1, fg="#1e2e3e")
        self.en_nome.place(relwidth=0.9, relheight=0.1,
                             relx=0.02, rely=0.4)

        # entry telefone
        self.en_telefone = Entry(self.frame1, fg="#1e2e3e")
        self.en_telefone.place(relwidth=0.4, relheight=0.1,
                               relx=0.02, rely=0.7)
        # entry cidade
        self.en_cidade = Entry(self.frame1, fg="#1e2e3e")
        self.en_cidade.place(relwidth=0.4, relheight=0.1,
                             relx=0.51, rely=0.7)

    def lista_frame2(self):
        self.listCli = ttk.Treeview(self.frame2, height=3, columns=("col1", "col2", "col3", "col4"))
        self.listCli.heading("#0", text="")
        self.listCli.heading("#1", text="Código")
        self.listCli.heading("#2", text="Nome")
        self.listCli.heading("#3", text="Telefone")
        self.listCli.heading("#4", text="Cidade")

        self.listCli.column("#0", width=1)
        self.listCli.column("#1", width=50)
        self.listCli.column("#2", width=200)
        self.listCli.column("#3", width=125)
        self.listCli.column("#4", width=125)

        self.listCli.place(relwidth=1, relheight=1, relx=0, rely=0)

        self.scrolList = Scrollbar(self.frame2, orient="vertical")
        self.listCli.configure(yscrollcommand=self.scrolList.set)
        self.scrolList.place(relx=0.98, rely=0, relwidth=0.2, relheight=1)

        self.listCli.bind("<Double-1>", self.OnDoubleClick)

    def menu_horizontal(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Relatório", menu=filemenu2)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu.add_command(label="Limpar Cliente", command=self.limpar_tela)

        filemenu2.add_command(label="Ficha do Cliente", command=self.gerarRelatorioCliente)


if __name__ == "__main__":
    Application()
