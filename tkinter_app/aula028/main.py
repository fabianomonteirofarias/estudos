# AULA 028 - Progress Bar

from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title("Progress Bar")
root.geometry("320x240")


def step():
    # progress1["value"] += 10
    # progress1.start(10)
    for x in range(10):
        progress1["value"] += 10
        root.update_idletasks()
        time.sleep(1)


def stop():
    progress1.stop()


progress1 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode="determinate")
progress1.pack(pady=20)

button = Button(root, text="Progresso", command=step)
button.pack(pady=5)

button2 = Button(root, text="Stop", command=stop)
button2.pack(pady=5)

root.mainloop()
