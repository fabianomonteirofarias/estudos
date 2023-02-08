# AULA 022 - Caixa de Mensagem

from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
import sqlite3

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser

# from PIL import ImageTk, Image
import base64

root = tix.Tk()


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

        if self.en_nome.get() == "":
            msg = "Insira um nome!"
            messagebox.showinfo("Aviso - Cadatro de Clientes", msg)

        else:
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

    def images_base64(self):
        self.bt_novo_base64 = "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"


class Application(Funcs, Relatorios):
    def __init__(self):
        self.root = root
        self.images_base64()
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
        self.abas = ttk.Notebook(self.frame1)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        # self.aba1.configure(background="gray")
        self.aba2.configure(background="lightgray")

        self.abas.add(self.aba1, text="Aba 1")
        self.abas.add(self.aba2, text="Aba 2")

        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        # tamanhão do botão padrão
        self.bt_width = 0.1
        self.bt_height = 0.13

        #moldura
        self.canvas_bt = Canvas(self.aba1, bd=0, bg="#1e2345",
                                highlightbackground="gray", highlightthickness=2)
        self.canvas_bt.place(relx=0.19, rely=0.03, relwidth=0.2275, relheight=0.17)

        # botão limpar
        self.bt_limpar = Button(self.aba1, text="LIMPAR",
                                bd=2, bg="#0a3eaa", fg="#ffffff",
                                font=("verdana", 9, "bold"), command=self.limpar_tela,
                                activeforeground="blue")
        self.bt_limpar.place(relwidth=self.bt_width, relheight=self.bt_height,
                             relx=0.2, rely=0.05)
        # botão buscar
        self.bt_buscar = Button(self.aba1, text="BUSCAR", bd=2, bg="#0a3eaa", fg="#ffffff",
                                font=("verdana", 9, "bold"), command=self.buscar_cliente,
                                activeforeground="blue")
        self.bt_buscar.place(relwidth=self.bt_width, relheight=self.bt_height,
                             relx=0.31, rely=0.05)
        text_bl_buscar = "Digite no campo o nome do cliente que deseja pesquisar"
        self.bl_buscar = tix.Balloon(self.aba1)
        self.bl_buscar.bind_widget(self.bt_buscar, balloonmsg=text_bl_buscar)

        # botão alterar
        self.bt_novo = Button(self.aba1, text="NOVO", bd=2, bg="#0a3eaa", fg="#ffffff",
                                 font=("verdana", 9, "bold"), command=self.add_cliente)
        self.bt_novo.place(relwidth=self.bt_width, relheight=self.bt_height,
                              relx=0.6, rely=0.05)

        # botão alterar
        self.bt_alterar = Button(self.aba1, text="ALTERAR", bd=2, bg="#0a3eaa", fg="#ffffff",
                                 font=("verdana", 9, "bold"), command=self.alterar_cliente)
        self.bt_alterar.place(relwidth=self.bt_width, relheight=self.bt_height,
                              relx=0.71, rely=0.05)
        # botão apagar
        self.bt_apagar = Button(self.aba1, text="APAGAR", bd=2, bg="#0a3eaa", fg="#ffffff",
                                font=("verdana", 9, "bold"), command=self.delete_cliente)
        self.bt_apagar.place(relwidth=self.bt_width, relheight=self.bt_height,
                             relx=0.82, rely=0.05)


        # label codigo
        self.lb_codigo = Label(self.aba1, text="Código",
                               fg="#1e2e3e")
        self.lb_codigo.place(relwidth=0.1, relheight=0.1,
                             relx=0.01, rely=0.05)
        # label nome
        self.lb_nome = Label(self.aba1, text="Nome", fg="#1e2e3e")
        self.lb_nome.place(relwidth=0.1, relheight=0.1,
                           relx=0.01, rely=0.3)
        # label telefone
        self.lb_telefone = Label(self.aba1, text="Telefone", fg="#1e2e3e")
        self.lb_telefone.place(relwidth=0.1, relheight=0.1,
                               relx=0.01, rely=0.6)
        # label cidade
        self.lb_cidade = Label(self.aba1, text="Cidade", fg="#1e2e3e")
        self.lb_cidade.place(relwidth=0.1, relheight=0.1,
                             relx=0.5,rely=0.6)


        # entry codigo
        self.en_codigo = Entry(self.aba1, fg="#1e2e3e")
        self.en_codigo.place(relwidth=0.1, relheight=0.08,
                             relx=0.02, rely=0.15)
        # entry nome
        self.en_nome = Entry(self.aba1, fg="#1e2e3e")
        self.en_nome.place(relwidth=0.9, relheight=0.1,
                             relx=0.02, rely=0.4)

        # entry telefone
        self.en_telefone = Entry(self.aba1, fg="#1e2e3e")
        self.en_telefone.place(relwidth=0.4, relheight=0.1,
                               relx=0.02, rely=0.7)
        # entry cidade
        self.en_cidade = Entry(self.aba1, fg="#1e2e3e")
        self.en_cidade.place(relwidth=0.4, relheight=0.1,
                             relx=0.51, rely=0.7)


        #### drop down button

        self.Tipvar = StringVar()
        self.Tipv = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)")
        self.Tipvar.set(self.Tipv[0])
        self. popupMenu = OptionMenu(self.aba2, self.Tipvar, *self.Tipv)
        self.popupMenu.place(relx=0.1, rely=0.1, relwidth=0.2,  relheight=0.15)
        self.estado_civil = self.Tipvar.get()
        print(self.estado_civil)

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
