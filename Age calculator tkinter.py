from tkinter import *

def age():
    name = e1.get()
    year = int(e4.get())

    current_year = 2026
    age = current_year - year

    l6.config(text="Hello " + name + "!\nYour age is " + str(age) + " years.")

root = Tk()
root.title("Age Calculator App")
root.geometry("400x400")

l1 = Label(root, text="Name")
l1.grid(row=0, column=0)

e1 = Entry(root)
e1.grid(row=0, column=1)

l4 = Label(root, text="Year")
l4.grid(row=3, column=0)

e4 = Entry(root)
e4.grid(row=3, column=1)

b1 = Button(root, text="Calculate Age", command=age)
b1.grid(row=4, column=0, columnspan=2)

l6 = Label(root, text="")
l6.grid(row=5, column=0, columnspan=2)

root.mainloop()