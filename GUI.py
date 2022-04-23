import do_tts
import re
import copy
import chardet
import multiprocessing
from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
import tkinter.messagebox as messagebox
from tkinter import filedialog
import time


class TextPlayer:
    def __init__(self):

        self.list_size = 0
        self.is_playing = False
        self.playing_index = 0
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

        self.play_listbox = Listbox(self.listbox_frame, selectmode="extended", height=9, justify="left",
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
        self.is_playing = False
        pass

    def play(self):
        self.is_playing = True
        self.window.after(25, self.play_sound)
        pass

    def next(self):
        self.playing_index += 1
        self.play_listbox.selection_set(self.playing_index)
        pass

    def prev(self):
        self.playing_index -= 1
        self.play_listbox.selection_set(self.playing_index)
        pass

    def open_file(self):
        file_name = filedialog.askopenfilename(title='Select text files', filetypes=(("text files (.txt)", "*.txt"),
                                                                                     ("all files", "*.*")))
        if file_name == '':
            return
        if file_name[-3:] != 'txt':
            messagebox.showwarning('경고', '현재는 txt 이외의 확장자를 지원하지 않습니다.')
            return
        file = open(file_name, encoding="utf-8")
        my_str = file.read()
        pattern = '[.\n]'
        pattern_str = re.split(pattern, my_str)

        self.text = copy.copy(pattern_str)
        file.close()
        self.insert_text()

    def insert_text(self):
        self.play_listbox.delete(0, self.list_size)
        for sentence in self.text:
            self.play_listbox.insert(self.list_size, sentence)
            self.list_size += 1
        self.play_listbox.selection_set(0)

    def clear(self):
        pass

    def quit(self):
        pass

    def play_sound(self):
        if self.is_playing:
            selected = self.play_listbox.curselection()
            if self.text[selected[0]] != '':
                if not do_tts.is_busy():
                    do_tts.speak(self.text[selected[0]])
                else:
                    self.window.after(25, self.play_sound)
                    return
            self.play_listbox.selection_clear(0, self.playing_index)
            self.playing_index += 1
            self.play_listbox.selection_set(self.playing_index)
            self.window.after(25, self.play_sound)

    def update(self):
        self.window.mainloop()

app = TextPlayer()
app.update()


