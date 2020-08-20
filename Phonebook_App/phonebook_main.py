#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#   Python Version      3.8.5
#
#   Author              Hayden Stark
#
#   Phonebook app, demonstrating OOP, Tkinter GUI, Tkinter parent/child relationships
#   Written and tested on macOS

from tkinter import *
from tkinter import messagebox
import tkinter as tk

import phonebook_gui
import phonebook_func

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #defining master frame configuration
        self.master = master
        self.master.minsize(600,400) #(h, w)
        self.master.maxsize(600,400)
        phonebook_func.center_window(self,600,400)      #centers window on user's screen
        self.master.title("Tkinter Phonebook App")
        self.master.configure(bg="#f0f0f0")
        #built-in method to catch user clicking 'x'
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master
        phonebook_gui.load_gui(self)

        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0,menu=filemenu)
        helpmenu = Menu(menubar,tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About this Phonebook App")          #add_command is child menubar of add_cascade parent
        menubar.add_cascade(label="Help", menu=helpmenu)                #add_cascade is parent item (visible heading)

        self.master.config(menu=menubar, borderwidth='1')



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
