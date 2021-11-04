import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import PySpammer

bg = "#5A4955"
Buttons = "#FFA500"

#5A4955
#808080
#808080
#454545

window = tk.Tk()

window.geometry("500x600")

window.title('PySpammer')

fontStyle = tkFont.Font(size=30)

window.configure(background=bg)

label1 = tk.Label(text="ᑭYᔕᑭᗩᗰᗰEᖇ V2", font=fontStyle, bg=bg)
label1.pack()

space3 = tk.Label(text=" ", bg=bg)
space3.pack()

B = tk.Button(text ="paste", width=50, height=2, compound="c", bg="#FFA500", borderwidth="2.5", command = PySpammer.paste)
B.pack()

e = Entry(window, width=50)
e.pack()

def test():
    PySpammer.say(e.get())

B2 = tk.Button(text ="start spamming", width=50, height=2, compound="c", bg=Buttons, command = test)
B2.pack()

space1 = tk.Label(text=" ", bg=bg)

space2 = tk.Label(text=" ", bg=bg)
space1.pack()
space2.pack()

B3 = tk.Button(text ="random int", width=50, height=2, compound="c", bg=Buttons, command = PySpammer.say_random)
B3.pack()

window.mainloop()
