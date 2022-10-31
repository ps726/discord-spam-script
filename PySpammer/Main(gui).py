import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import PySpammer

bg = "#181818"
Buttons = "#FFA500"

#5A4955
#808080
#808080
#454545

window = tk.Tk()

window.geometry("500x650")

window.title('PySpammer')

fontStyle = tkFont.Font(size=30)

window.configure(background=bg)

label1 = tk.Label(text="ᑭYᔕᑭᗩᗰᗰEᖇ V2", font=fontStyle, bg=bg, foreground="white")
label1.pack()

space3 = tk.Label(text=" ", bg=bg)
space2 = tk.Label(text=" ", bg=bg)
space2.pack()
space3.pack()


e = Entry(window, width=50, borderwidth=5)
e.pack()

space8 = tk.Label(text=" ", bg=bg)
space8.pack()

def get_user_input():
    PySpammer.say(e.get())

B2 = tk.Button(text ="start spamming", width=50, height=2, compound="c", bg=Buttons, command = get_user_input)
B2.pack()

space1 = tk.Label(text=" ", bg=bg)
space1.pack()

B = tk.Button(text ="paste", width=50, height=2, compound="c", bg="#FFA500", borderwidth="2.5", command = PySpammer.paste)
B.pack()

space2 = tk.Label(text=" ", bg=bg)
space2.pack()

B3 = tk.Button(text ="random int", width=50, height=2, compound="c", bg=Buttons, command = PySpammer.say_random)
B3.pack()

space6 = tk.Label(text=" ", bg=bg)
space6.pack()

B4 = tk.Button(text ="bee movie ;)", width=50, height=2, compound="c", bg=Buttons, command = PySpammer.read_file)
B4.pack()

space10 = tk.Label(text=" ", bg=bg)
space10.pack()

B4 = tk.Button(text ="custom file", width=50, height=2, compound="c", bg=Buttons, command = PySpammer.read_custom_file)
B4.pack()

space10 = tk.Label(text=" ", bg=bg)
space10.pack()

B45 = tk.Button(text="AutoClicker",width=50, height=2, compound="c", bg=Buttons, command = PySpammer.read_custom_file )
B45.pack()

space2 = tk.Label(text=" ", bg=bg)
space2.pack()

B45 = tk.Button(text="mee6 bot farm",width=50, height=2, compound="c", bg=Buttons, command = PySpammer.mee6_bot_farm )
B45.pack()

space2 = tk.Label(text=" ", bg=bg)
space2.pack()

b5 = tk.Button(text ="exit", width=25, height=2, compound="c", bg="#CC0000", command = exit)
b5.pack()

window.mainloop()
