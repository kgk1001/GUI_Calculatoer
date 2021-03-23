from tkinter import *
if __name__ == '__main__':
    root = Tk()
    #creating a lable widget
    title = Label(root,text = "Calculator")
    creator = Label(root, text="Created by Nettie")
    #this packs it into root
    #title.pack()
    #grid let you position lables
    title.grid(row=0, column= 0)
    creator.grid(row=0, column= 1)



    root.mainloop()