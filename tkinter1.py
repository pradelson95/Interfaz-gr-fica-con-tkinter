from tkinter import *
import datetime 

root = Tk()
root.title("_python.py_")
root.geometry('350x200')

lbl = Label(root, text="Hello", fg="red")
lbl.grid(column=False, row=False)


def clicked():

  x = datetime.datetime.now()

  print(x.year)  
  lbl.configure(text=x)

btn = Button(root, bg="cyan", text="Click Me", command=clicked)

btn.grid(column=1, row=0)

root.mainloop()