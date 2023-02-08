# AULA 007 - Adicionando função ao botão limpar

from tkinter import *
from tkinter import ttk

root = Tk()


class Funcs:
    def limpar_tela(self):
        self.en_codigo.delete(0, END)
        self.en_nome.delete(0, END)
        self.en_telefone.delete(0, END)
        self.en_cidade.delete(0, END)


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.lista_frame2()
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
                                font=("verdana", 9, "bold"))
        self.bt_buscar.place(relwidth=self.bt_width, relheight=self.bt_height,
                             relx=0.31, rely=0.05)
        # botão novo
        self.bt_novo = Button(self.frame1, text="NOVO", bd=2, bg="#0a3eaa", fg="#ffffff",
                              font=("verdana", 9, "bold"))
        self.bt_novo.place(relwidth=self.bt_width, relheight=self.bt_height,
                           relx=0.6, rely=0.05)
        # botão alterar
        self.bt_alterar = Button(self.frame1, text="ALTERAR", bd=2, bg="#0a3eaa", fg="#ffffff",
                                 font=("verdana", 9, "bold"))
        self.bt_alterar.place(relwidth=self.bt_width, relheight=self.bt_height,
                              relx=0.71, rely=0.05)
        # botão apagar
        self.bt_apagar = Button(self.frame1, text="APAGAR", bd=2, bg="#0a3eaa", fg="#ffffff",
                                font=("verdana", 9, "bold"))
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


if __name__ == "__main__":
    Application()
