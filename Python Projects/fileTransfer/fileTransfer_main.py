# Python Ver:   3.7.3
#
# Author:       Tyler W. Johnson
#
# Purpose:      File Directory and transfer drill
#
# Tested OS:  This code was written and tested to work with Windows 10.

import os
import time
import datetime
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import filedialog
import shutil
from pathlib import Path
import datetime
import os.path

#connect to the database
con = sqlite3.connect('db_xfr.db')

#while the database is open, if the table dbl_fileTransfer isn't already a thing,
#make it one
with con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_fileTransfer( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file_name TEXT, \
        col_modification TEXT)')
    con.commit()
    con.close


class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(425,150))
        self.master.title("Transfer Files")
        self.master.config(bg='#F5F5F5')
        self.vartxtOne = StringVar()
        self.vartxtTwo = StringVar()
        self.vartxtThree = StringVar()

#function to set vartxtOne to the File Path 1
        def c_open_dir():
            rep = filedialog.askdirectory(initialdir='/tmp')
            self.vartxtOne.set(rep)
            
#function to set vartxtTwo to the File Path 2
        def setSource():
            rep = filedialog.askdirectory(initialdir='/tmp')
            self.vartxtTwo.set(rep)

#adds the results to the db and prints to the console
        def setLog():
            con = sqlite3.connect('db_xfr.db')
            with con:
                cur = con.cursor()
                for name in os.listdir(str(self.vartxtOne.get())):
                    path = os.path.join(self.vartxtOne.get(), name)
                    if path.endswith('.txt'):
                        file_time = time.ctime(os.path.getmtime(path))
                        #print log to the console
                        print(name + " was created on " + file_time + ".")
                        #add log to the db
                        cur.execute('INSERT INTO tbl_fileTransfer(col_file_name, col_modification) VALUES (?, ?)', (name, file_time))                     
                    con.commit()
            con.close()
            moveFiles()
            

#move .txt files from the source directory to the destination directory
#and setting the third text box to success or fail
        def moveFiles():
            try:
                for name in os.listdir(str(self.vartxtOne.get())):
                    path = os.path.join(self.vartxtOne.get(), name)
                    if path.endswith('.txt'):
                        shutil.move(path, self.vartxtTwo.get())
                        self.vartxtThree.set("Success!")
            except:
                self.vartxtThree.set("Failed")

#adds a label pointing the instructor to the text files to use for this drill
        self.Label = Label(self.master, text="Use directory '\\Python\\Python Projects\\A' as your source directory")
        self.Label.grid(padx=(10,0),row = 0,column=0, columnspan = 5,sticky=NW,)

#adds the buttons and commands
        self.btnBrowseOneButton = Button(self.master, text='Source Directory', width=18, height=1,command=lambda: c_open_dir())
        self.btnBrowseOneButton.grid(row = 1,column=0, columnspan=2, padx=(10,0),pady=(10,0), sticky=NW)

        self.btnBrowseTwoButton = Button(self.master, text='Destination Directory', width=18, height=1,command=lambda: setSource())
        self.btnBrowseTwoButton.grid(row = 2,column=0, columnspan=2, padx=(10,0),pady=(10,0), sticky=NW)

        self.btnBrowseThreeButton = Button(self.master, text='Transfer .txt Files', width=18, height=1,command=lambda: setLog())
        self.btnBrowseThreeButton.grid(row = 3,column=0, columnspan=2, padx=(10,0),pady=(10,0), sticky=NW)

#adds the text fields and puts the correct info in each one
        self.txtOne = Entry(self.master,text=self.vartxtOne, font=("Helvetica", 16), fg ='black', bg='white')
        self.txtOne.grid(row = 1,column=2, columnspan=3, padx=(20,10),pady=(10,0), sticky=E)

        self.txtTwo = Entry(self.master,text=self.vartxtTwo, font=("Helvetica", 16), fg ='black', bg='white')
        self.txtTwo.grid(row = 2,column=2, columnspan=3, padx=(20,10),pady=(10,0), sticky=E)

        self.txtThree = Entry(self.master,text=self.vartxtThree, font=("Helvetica", 16), fg ='black', bg='white')
        self.txtThree.grid(row = 3,column=2, columnspan=3, padx=(20,10),pady=(10,0), sticky=E)





        








        

if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
