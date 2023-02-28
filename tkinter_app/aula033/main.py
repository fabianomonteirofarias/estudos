# AULA 033 - Tipos de Messagebox

from tkinter import *
from tkinter import messagebox

root = Tk()


def display():
    messagebox.showinfo("Info", "Informações aqui")
    messagebox.showwarning("Perigo", "Melhor ter cuidado")
    messagebox.showerror("Erro", "Algo errado!")

    okcancel = messagebox.askokcancel("O que você acha?", "Devemos ir em frente?")
    print(okcancel)

    yesno = messagebox.askyesno("O que você acha?", "Porfavor decida.")
    print(yesno)

    retrycancel = messagebox.askretrycancel("O que você acha?", "Qual sua resposta")
    print(retrycancel)

    answer = messagebox.askquestion("O que você acha?", "Por favor decida.")


b1 = Button(root, text="Exibir Dialogo", command=display)
b1.pack()


root.mainloop()
