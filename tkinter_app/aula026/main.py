# AULA 026 - Processos de BIND

from tkinter import *
from tkinter import ttk

root = Tk()

l = ttk.Label(root, text="Começando...")
l.grid()

l.bind("<Enter>", lambda e: l.configure(text="MOUSE IN"))
l.bind("<Leave>", lambda e: l.configure(text="MOUSE OUT"))
l.bind("<1>", lambda e: l.configure(text="LEFT BUTTON"))
l.bind("<Double-1>", lambda e: l.configure(text="DOUBLE CLICK LEFT"))
l.bind("<B3-Motion>", lambda e: l.configure(text=f"MOVE BUTTON RIGHT x:{e.x}, y{e.y}"))

root.mainloop()