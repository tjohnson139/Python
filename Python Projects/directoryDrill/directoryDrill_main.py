import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import filedialog

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__(self)

        def c_open_dir_old():
            rep = filedialog.askdirectory(initialdir='/tmp')
            self.vartxtOne.set(rep)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(352,50))
        self.master.title("File Path")
        self.master.config(bg='#F5F5F5')

        self.vartxtOne = StringVar()


        self.btnBrowse = tk.Button(self.master, text='Browse...', width=10, height=1,command=lambda: c_open_dir_old())
        self.btnBrowse.grid(row = 0,column=0, padx=(10,0),pady=(12,0), sticky=NW)

        self.txtOne = Entry(self.master,text=self.vartxtOne, font=("Helvetica", 16), fg ='black', bg='white')
        self.txtOne.grid(row = 0,column=1, columnspan=3, padx=(10,0),pady=(12,0), sticky=E)

if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
