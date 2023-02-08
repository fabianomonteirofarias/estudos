# AULA 001 - Criação e Configuração de Janela

from tkinter import *

root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background="#1e4234")
        self.root.geometry("640x480")
        # self.root.resizable(False, False)
        self.root.maxsize(width=700, height=500)
        self.root.minsize(width=600, height=400)


Application()
