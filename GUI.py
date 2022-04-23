import do_tts
from tkinter import *
from tkinter.ttk import *
from tkinter.font import *


class TextPlayer:

    def __init__(self):

        self.is_playing = False
        self.text = []

        self.window = Tk()
        self.window.title("Text Player")
        self.window.geometry("640x480")

        self.title_font = Font(family="Century Gothic", size=20, weight="bold")
        self.title = Label(text="Text Player", font=self.title_font)
        self.title.pack(pady=20)

        self.listbox_frame = LabelFrame(text="Text", labelanchor="n")
        self.listbox_frame.pack(fill="x", padx=20, pady=20)

        self.listbox_scroll = Scrollbar(self.listbox_frame)
        self.listbox_scroll.pack(side="right", fill="y")

        self.play_listbox = Listbox(self.listbox_frame, selectmode="extended", height=9, justify="center",
                                    yscrollcommand=self.listbox_scroll.set)
        self.play_listbox.pack(fill="x", padx=20, pady=20)

        self.listbox_scroll.config(command=self.play_listbox.yview)

        self.button_frame = LabelFrame(self.window, text="function", labelanchor="n")
        self.button_frame.pack(side=TOP, expand=NO, fill=NONE)

        self.prev_button = Button(self.button_frame, text="<<", command=self.prev).pack(side=LEFT, padx=10, pady=10)
        self.play_button = Button(self.button_frame, text="▶", command=self.play).pack(side=LEFT, padx=10, pady=10)
        self.stop_button = Button(self.button_frame, text="■", command=self.stop).pack(side=LEFT, padx=10, pady=10)
        self.next_button = Button(self.button_frame, text=">>", command=self.next).pack(side=LEFT, padx=10, pady=10)

        self.menu = Menu()
        self.menu_File = Menu(self.menu, tearoff=False)
        self.menu_File.add_command(label="Open", accelerator='Ctrl+O', command=self.open_file)
        self.menu_File.add_command(label="Quit", accelerator='Ctrl+Q', command=self.quit)
        self.menu.add_cascade(label="File", underline=True, menu=self.menu_File)

        self.window.config(menu=self.menu)

    def stop(self):
        pass

    def play(self):
        pass

    def next(self):
        pass

    def prev(self):
        pass

    def open_file(self):
        pass

    def file_to_text(self, file):
        pass

    def quit(self):
        pass

    def make_sound(self):
        pass

    def update(self):
        self.window.mainloop()


app = TextPlayer()
app.update()


