import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(400,175))
        self.master.title("Check Files")
        self.master.config(bg='#F5F5F5')

        self.vartxtOne = StringVar()
        self.vartxtTwo = StringVar()

        self.btnBrowseOneButton = Button(self.master, text='Browse...', width=15, height=1)
        self.btnBrowseOneButton.grid(row = 0,column=0, columnspan=2, padx=(10,0),pady=(40,0), sticky=NW)

        self.btnBrowseTwoButton = Button(self.master, text='Browse...', width=15, height=1)
        self.btnBrowseTwoButton.grid(row = 1,column=0,columnspan=2,padx=(10,0),pady=(10,0), sticky=NW)

        self.txtOne = Entry(self.master,text=self.vartxtOne, font=("Helvetica", 16), fg ='black', bg='white')
        self.txtOne.grid(row = 0,column=2, columnspan=3, padx=(20,10),pady=(40,0), sticky=E)

        self.txtTwo = Entry(self.master,text=self.vartxtTwo, font=("Helvetica", 16), fg ='black', bg='white')
        self.txtTwo.grid(row = 1,column=2, columnspan=3, padx=(20,10),pady=(10,0), sticky=E)

        self.btnCheckFiles = Button(self.master, text='Check for files...', width=15, height=2)
        self.btnCheckFiles.grid(row = 2,column=0, padx=(10,0),pady=(10,0), sticky=NW)

        self.btnClose = Button(self.master, text='Close Program', width=15, height=2)
        self.btnClose.grid(row = 2,column=4, padx=(0,10),pady=(10,0), sticky=E)


if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
