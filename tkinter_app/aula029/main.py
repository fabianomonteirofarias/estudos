# AULA 029 - PanedWindow - Widgets responsivos

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("PanedWindow")
root.geometry("320x240")

painel1 = PanedWindow(bd=4, relief="raised", bg="red")
painel1.pack(fill=BOTH, expand=1)

left_label = Label(painel1, text="PAINEL ESQUERDO")
painel1.add(left_label)

painel2 = PanedWindow(painel1, orient=VERTICAL, bd=4, relief="raised", bg="blue")
painel1.add(painel2)

top_label = Label(painel2, text="PAINEL TOP")
painel2.add(top_label)

bottom_label = Label(painel2, text="PAINEL BOTTOM")
painel2.add(bottom_label)

root.mainloop()
