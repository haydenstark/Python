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

import student_tracker_gui
import student_tracker_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #defining master frame configuration
        self.master = master
        self.master.minsize(500,550) #(w, h)
        self.master.maxsize(500,550)
        self.master.title("Student Tracker")
        self.master.configure(bg="#f0f0f0")
        arg = self.master
        student_tracker_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

