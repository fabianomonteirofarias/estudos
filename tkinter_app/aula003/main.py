# AULA 003 - Criação dos Botões

from tkinter import *

root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_tela()
        self.botoes()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="#1e4234")
        self.root.geometry("640x480")
        # self.root.resizable(False, False)
        self.root.maxsize(width=700, height=500)
        self.root.minsize(width=600, height=400)

    def frame_tela(self):
        self.frame1 = Frame(self.root)
        self.frame1.place(relwidth=0.95, relheight=0.45,
                          relx=0.025, rely=0.025)
        self.frame2 = Frame(self.root)
        self.frame2.place(relwidth=0.95, relheight=0.45,
                          relx=0.025, rely=0.5)

    def botoes(self):
        # botão limpar
        self.bt_limpar = Button(self.root, text="LIMPAR")
        self.bt_limpar.place(relwidth=0.1, relheight=0.05,
                             relx=0.2, rely=0.05)
        # botãp buscar
        self.bt_buscar = Button(self.root, text="BUSCAR")
        self.bt_buscar.place(relwidth=0.1, relheight=0.05,
                             relx=0.305, rely=0.05)
        # botão novo
        self.bt_novo = Button(self.root, text="NOVO")
        self.bt_novo.place(relwidth=0.1, relheight=0.05,
                           relx=0.6, rely=0.05)
        # botão alterar
        self.bt_alterar = Button(self.root, text="ALTERAR")
        self.bt_alterar.place(relwidth=0.1, relheight=0.05,
                              relx=0.705, rely=0.05)
        # botão apagar
        self.bt_apagar = Button(self.root, text="APAGAR")
        self.bt_apagar.place(relwidth=0.1, relheight=0.05,
                             relx=0.81, rely=0.05)


if __name__ == "__main__":
    Application()
