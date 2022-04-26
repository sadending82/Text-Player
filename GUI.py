# import space
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


# -------------------------------------------------------------------------------------------------
# class space


class TextPlayer:
    def __init__(self):

        self.list_size = 0
        self.is_playing = False
        self.playing_index = -1
        self.support_extension = ['txt']
        self.text = None

        self.window = Tk()
        self.window.title("Text Player")
        self.window.geometry("640x640")

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
        self.play_listbox.bind('<<ListboxSelect>>', self.list_box_selected)

        self.button_frame = LabelFrame(self.window, text="function", labelanchor="n")
        self.button_frame.pack(side=TOP, expand=NO, fill=NONE)

        self.prev_button = Button(self.button_frame, text="<<", command=self.prev).pack(side=LEFT, padx=10, pady=10)
        self.play_button = Button(self.button_frame, text="▶", command=self.play).pack(side=LEFT, padx=10, pady=10)
        self.stop_button = Button(self.button_frame, text="■", command=self.stop).pack(side=LEFT, padx=10, pady=10)
        self.next_button = Button(self.button_frame, text=">>", command=self.next).pack(side=LEFT, padx=10, pady=10)

        self.slider_frame = Frame(self.window)
        self.slider_frame.pack()

        self.vol_label = Label(self.slider_frame, text="Volume")
        self.vol_label.pack(side=LEFT, padx=10, pady=10)
        self.vol_scale = Scale(self.slider_frame)
        self.vol_scale.pack(side=LEFT, padx=10, pady=10)

        self.menu = Menu()
        self.menu_File = Menu(self.menu, tearoff=False)
        self.menu_File.add_command(label="Open", accelerator='Ctrl+O', command=self.open_file)
        self.menu_File.add_command(label="Quit", accelerator='Ctrl+Q', command=self.quit)
        self.menu.add_cascade(label="File", underline=True, menu=self.menu_File)

        self.window.config(menu=self.menu)

    def stop(self):
        if self.text is not None:
            self.is_playing = False
            do_tts.stop()

    def play(self):
        if self.text is not None:
            self.is_playing = True
            self.window.after(25, self.play_sound)

    def next(self):
        if self.text is not None:
            if self.is_playing:
                do_tts.stop()
                self.play_listbox.selection_clear(0, END)
                self.play_listbox.selection_set(self.playing_index)
                self.play_sound()
            else:
                self.playing_index += 1
                self.play_listbox.selection_clear(0, END)
                self.play_listbox.selection_set(self.playing_index)
        self.play_listbox.see(self.playing_index + 4)

    def prev(self):
        if self.text is not None:
            if self.is_playing:
                do_tts.stop()
                self.playing_index -= 2
                self.play_listbox.selection_clear(0, END)
                self.play_listbox.selection_set(self.playing_index)
                self.play_sound()
            else:
                if self.playing_index > 0:
                    self.playing_index -= 1
                self.play_listbox.selection_clear(0, END)
                self.play_listbox.selection_set(self.playing_index)
        self.play_listbox.see(self.playing_index + 4)

    def open_file(self):
        self.init_basic_value()
        file_name = filedialog.askopenfilename(title='Select text files', filetypes=(("text files (.txt)", "*.txt"),
                                                                                     ("all files", "*.*")))
        if file_name == '':
            return
        if file_name[-3:] not in self.support_extension:
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
        self.play_listbox.delete(0, END)
        for sentence in self.text:
            self.play_listbox.insert(self.list_size, sentence)
            self.list_size += 1
        self.play_listbox.selection_set(0, 0)

    def list_box_selected(self, event):
        do_tts.stop()
        selected = self.play_listbox.curselection()
        for num in selected:
            if num != self.playing_index:
                self.playing_index = selected[0] - 1
                break
        self.play_listbox.selection_clear(0, END)
        self.play_listbox.selection_set(self.playing_index + 1, self.playing_index + 1)
        self.window.after(25, self.play_sound)

    def init_basic_value(self):
        self.list_size = 0
        self.is_playing = False
        self.playing_index = -1
        self.support_extension = ['txt']
        if self.text is not None:
            self.text.clear()

    def clear(self):
        self.is_playing = False
        pass

    def quit(self):
        self.is_playing = False
        if do_tts.is_busy():
            do_tts.stop()
        self.window.quit()

    def play_sound(self):
        if self.is_playing:
            if not do_tts.is_busy():
                self.playing_index += 1
                if self.playing_index >= len(self.text) - 1:
                    self.stop()
                if self.text[self.playing_index] != '':
                    do_tts.speak(self.text[self.playing_index])
                    self.play_listbox.selection_clear(0, END)
                    self.play_listbox.selection_set(self.playing_index, self.playing_index)
                    self.play_listbox.see(self.playing_index + 4)
        self.window.after(25, self.play_sound)

    def get_text(self):
        selected = self.play_listbox.curselection()
        if self.playing_index == 0:
            return self.text[selected[0]]
        pass

    def set_text(self):
        pass

    def update(self):
        self.window.mainloop()

# -------------------------------------------------------------------------------------------------
# main


app = TextPlayer()
app.update()


