from tkinter import *
root = Tk()
root.geometry()
a = Label(root, text="Enter Your Name:")
a.grid(row=0, column=0)
b = Entry(root)
b.grid(row=0, column=1)
def Click():
    d = Label(root,text=b.get())
    d.grid(row=1,column=1)


d = Label(root, text="None")
d.grid(row=1, column=1)
c = Button(root, text="Submit",command=Click)
c.grid(row=2, column=1)
root.mainloop()

