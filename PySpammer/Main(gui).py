import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import tkinter
import PySpammer

window = tk.Tk()

window.geometry("500x600")

fontStyle = tkFont.Font(size=30)

label1 = tk.Label(text="ᑭYᔕᑭᗩᗰᗰEᖇ", font=fontStyle)
label1.pack()

space3 = tk.Label(text=" ")
space4 = tk.Label(text=" ")
space3.pack()
space4.pack()

B = tk.Button(text ="paste", width=50, height=2, compound="c", command = PySpammer.paste)
B.pack()

canvas1 = tk.Canvas(window, width = 400, height = 200)
canvas1.pack()

entry1 = tk.Entry (window) 
canvas1.create_window(200, 140, window=entry1)

B2 = tk.Button(text ="start spamming", width=50, height=2, compound="c", command = PySpammer.paste)
B2.pack()

space1 = tk.Label(text=" ")
space2 = tk.Label(text=" ")
space1.pack()
space2.pack()

B3 = tk.Button(text ="Hello", width=50, height=2, compound="c", command = PySpammer)
B3.pack()

window.mainloop()

