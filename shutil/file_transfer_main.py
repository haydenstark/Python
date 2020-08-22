

from tkinter import *
from tkinter import messagebox
import tkinter as tk
import file_transfer_func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #defining master frame configuration
        self.master = master
        self.master.minsize(500,250) #(w, h)
        self.master.maxsize(500,250)
        self.master.title("File Transfer")
        self.master.configure(bg="#f0f0f0")

        self.lbl_note = tk.Label(self.master,text='Please select your source folder and destination folder...', bg="#f0f0f0")
        self.lbl_note.grid(row=0,column=0)

        self.lbl_note = tk.Label(self.master,text='Source folder (to be checked for new files):', bg="#f0f0f0")
        self.lbl_note.grid(row=1,column=0)
        self.entry1 = tk.Entry(self.master,text='')
        self.entry1.grid(row=2, column=0,rowspan=1,columnspan=2,pady=(10,10),sticky=E+W)
        
        self.lbl_note = tk.Label(self.master,text='Destination folder (where the files will be copied to):', bg="#f0f0f0")
        self.lbl_note.grid(row=3,column=0)
        self.entry2 = tk.Entry(self.master,text='')
        self.entry2.grid(row=4, column=0,rowspan=1,columnspan=2,pady=(10,10),sticky=E+W)

        self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: file_transfer_func.sourcedir(self))
        self.btn_browse1.grid(row=2,column=2,padx=(10,10),pady=(0,0),sticky=N+S)
        self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda: file_transfer_func.destdir(self))
        self.btn_browse2.grid(row=4,column=2,padx=(10,10),pady=(0,0),sticky=N+S)
        self.btn_go = tk.Button(self.master,width=12,height=3,text='GO!',command=lambda: file_transfer_func.go(self))
        self.btn_go.grid(row=5,column=2,padx=(10,10),pady=(10,10),sticky=E)
        self.btn_go.configure(bg="DodgerBlue2", highlightbackground="DodgerBlue2")
        self.btn_remove = tk.Button(self.master,width=20,height=2,text='Refresh destination folder',command=lambda: file_transfer_func.remove(self))
        self.btn_remove.grid(row=5,column=0,padx=(10,10),pady=(10,10),sticky=W)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
