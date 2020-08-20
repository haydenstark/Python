##!/usr/bin/python
# -*- coding: utf-8 -*-
#
#   Python          3.8.5
#
#   Author          Hayden Stark
#
#   written and tested on macOS

from tkinter import *
from tkinter import messagebox
import tkinter as tk

import student_tracker
import student_tracker_func


def load_gui(self):

    self.label_fname = tk.Label(self.master, text='First Name:', bg="#f0f0f0")
    self.label_fname.grid(row=3, column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.label_lname = tk.Label(self.master, text='Last Name:', bg="#f0f0f0")
    self.label_lname.grid(row=5, column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.label_phone = tk.Label(self.master, text='Phone Number:', bg="#f0f0f0")
    self.label_phone.grid(row=7, column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.label_email = tk.Label(self.master, text='Email:', bg="#f0f0f0")
    self.label_email.grid(row=9, column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.label_course = tk.Label(self.master, text='Course:', bg="#f0f0f0")
    self.label_course.grid(row=11, column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    self.label_list = tk.Label(self.master, text='Student Names:', bg="#f0f0f0")
    self.label_list.grid(row=0, column=3,padx=(0,0),pady=(10,0),sticky=N+W)
    self.label_display = tk.Label(self.master, text='Student Info:', bg="#f0f0f0")
    self.label_display.grid(row=0, column=0,padx=(20,0),pady=(10,0),sticky=N+W)
    

    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=4, column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_lname.grid(row=6, column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=8, column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=10, column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_course = tk.Entry(self.master,text='')
    self.txt_course.grid(row=12, column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: student_tracker_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=8,rowspan=8,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=3,rowspan=8,columnspan=4,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    self.lstDisplay = Listbox(self.master,exportselection=0)
    self.lstDisplay.grid(row=1,column=0,rowspan=2,columnspan=2,padx=(10,20),pady=(0,0),sticky=N+E+W)
    self.scrollbar2 = Scrollbar(self.master,orient=HORIZONTAL)
    self.scrollbar2.config(command=self.lstDisplay.xview)

    self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda: student_tracker_func.addToList(self))
    self.btn_add.grid(row=10,column=3,sticky=W)
    self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: student_tracker_func.onUpdate(self))
    self.btn_update.grid(row=10,column=5,sticky=W)
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: student_tracker_func.onDelete(self))
    self.btn_delete.grid(row=12,column=5,sticky=E)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Clear',command=lambda: student_tracker_func.onClear(self))
    self.btn_close.grid(row=12,column=3,sticky=E)

    student_tracker_func.create_db(self)
    student_tracker_func.onRefresh(self)




if __name__ == "__main__":
    pass
