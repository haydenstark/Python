


import shutil, os, time
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk

import file_transfer_main

#dsktp = os.path.expanduser("~/Desktop")
#origindir = "CompanyFiles"
#newdir = "New&Modified"

#path1 = os.path.join(dsktp, origindir)
#path2 = os.path.join(dsktp, newdir)

#def createDirs():       #creates CompanyFiles folder and New&Modified if folders do not already exist
#    if not os.path.exists(path1):
#        os.mkdir(path1)
#
#    if not os.path.exists(path2):
#        os.mkdir(path2)

def sourcedir(self):
    source = tk.filedialog.askdirectory(parent=self, initialdir=sys.path[0],mustexist=tk.TRUE)
    self.entry1.delete(0,END)
    self.entry1.insert(0,source)

def destdir(self):
    dest = tk.filedialog.askdirectory(parent=self, initialdir=sys.path[0],mustexist=tk.TRUE)
    self.entry2.delete(0,END)
    self.entry2.insert(0,dest)


def go(self):
    source = self.entry1.get()
    dest = self.entry2.get()
    if not source or not dest:
        messagebox.showerror("Missing information","Please select both a source folder and a destination folder")
    else:
        for file in os.listdir(source):
            os.chdir(source)
            filetime = os.path.getmtime(file)
            epoch = time.time()
            result = epoch - filetime
            if (result < 86400):
                cf = os.path.join(source, file)      #'cf' meaning copied file
                shutil.copy(cf, dest)


def remove(self):
    if messagebox.askokcancel("WARNING: Removing older files","This will remove all files from your destination folder that are older than 24 hours.\n Continue?"):
        dest = self.entry2.get()
        if not dest:
            messagebox.showerror("Missing destination folder","Please make sure your destination folder is selected in the second search box.")
        else:
            for file in os.listdir(dest):
                os.chdir(dest)
                filetime = os.path.getmtime(file)
                epoch = time.time()
                result = epoch - filetime
                if (result > 86400):
                    old = os.path.join(dest, file)
                    os.remove(old)
            


if __name__ == "__main__":
    pass
