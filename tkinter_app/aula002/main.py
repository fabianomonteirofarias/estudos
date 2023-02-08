# AULA 002 - Criação e configuração de Frames
from tkinter import *

root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_tela()
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


if __name__ == "__main__":
    Application()
