import tkinter

import do_tts
from tkinter import *
from tkinter.ttk import *
from tkinter.font import *

window = Tk()
window.title("Text Player")
window.geometry("640x480")

title_font = Font(family="Century Gothic", size=20, weight="bold")
title = Label(text="Text Player", font=title_font)
title.pack(pady=20)

listbox_frame = LabelFrame(text="Text", labelanchor="n")
listbox_frame.pack(fill="x", padx=20, pady=20)


listbox_scroll = Scrollbar(listbox_frame)
listbox_scroll.pack(side="right", fill="y")


play_listbox = Listbox(listbox_frame, selectmode="extended", height=9, justify="center", yscrollcommand=listbox_scroll.set)
play_listbox.pack(fill="x", padx=20, pady=20)

listbox_scroll.config(command=play_listbox.yview)

button_frame = LabelFrame(window, text="function", labelanchor="n")
button_frame.pack(side=TOP, expand=NO, fill=NONE)

prev_button = Button(button_frame, text="<<").pack(side=LEFT, padx=10, pady=10)
play_button = Button(button_frame, text="▶").pack(side=LEFT, padx=10, pady=10)
stop_button = Button(button_frame, text="■").pack(side=LEFT, padx=10, pady=10)
next_button = Button(button_frame, text=">>").pack(side=LEFT, padx=10, pady=10)

# prev_button = tkinter.Button(button_frame, text="<<", width=12, height=2).pack(side=LEFT, padx=10, pady=5)
# play_button = tkinter.Button(button_frame, text="▶", width=12, height=2).pack(side=LEFT, padx=10, pady=5)
# stop_button = tkinter.Button(button_frame, text="❚❚", width=12, height=2).pack(side=LEFT, padx=10, pady=5)
# next_button = tkinter.Button(button_frame, text=">>", width=12, height=2).pack(side=LEFT, padx=10, pady=5)

menu = Menu()
menu_File = Menu(menu, tearoff=False)
menu_File.add_command(label="Open", accelerator='Ctrl+O')
menu_File.add_command(label="Quit", accelerator='Ctrl+Q')
menu.add_cascade(label="File", underline=True, menu=menu_File)

window.config(menu=menu)

window.mainloop()


