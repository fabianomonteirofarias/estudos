from aula030.controllers.Funcs import Funcs
from aula030.controllers.Relatorios import Relatorios
from aula030.controllers.Validadores import Validadores
from aula030.view.GradientFrame import GradientFrame
from tkinter import *
from tkinter import tix, ttk

root = tix.Tk()


class Application(Funcs, Relatorios, Validadores):
    def __init__(self):
        self.root = root
        self.images_base64()
        self.validaEntradas()
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
        self.aba2 = GradientFrame(self.abas)

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
                                font=("verdana", 9, "bold"), command=self.janela2,
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
        self.en_codigo = Entry(self.aba1, fg="#1e2e3e", validate="key", validatecommand=self.vcmd2)
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
        self.popupMenu.place(relx=0.05, rely=0.1, relwidth=0.2,  relheight=0.15)
        self.estado_civil = self.Tipvar.get()
        print(self.estado_civil)

        # calendar
        self.bt_calendario = Button(self.aba2, text="Data", command=self.calendario_)
        self.bt_calendario.place(relx=0.3, rely=0.1, relwidth=self.bt_width, relheight=self.bt_height)
        self.en_data = Entry(self.aba2, width=10)
        self.en_data.place(relx=0.4, rely=0.1, relwidth=self.bt_width + 0.01, relheight=self.bt_height)

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

    def janela2(self):
        self.root2 = Toplevel()
        self.root2.title("Janela 2")
        self.root2.configure(bg="lightblue")
        self.root2.geometry("320x240")
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

    def validaEntradas(self):
        self.vcmd2 = (self.root.register(self.validate_entry2), "%P")

