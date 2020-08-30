from tkinter import *
root = Tk()

e = Entry(root, width= 50, bg= "pink")
e.pack()
e.insert(0, "Name")


def deb():
    myLabel = Label(root, text = "Hello " + e.get() + " !," + " welcome to Mark PLC.")
    myLabel.pack()

myButton = Button(root, text = "Enter your name", command=deb)
myButton.pack()
root.mainloop()