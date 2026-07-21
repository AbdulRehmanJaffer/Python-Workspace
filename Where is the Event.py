"""from tkinter import *

window = Tk()
def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)
window.mainloop()"""

"""from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("200x200")

def msg():
    messagebox.askyesno("Question Box", "Do you wish to Continue Exiting this Program?")

button = Button(window, text="Exit", command=msg)
button.place(x=40, y=80)
window.mainloop()"""
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Leng Converter")
window.geometry("300x300")

name_entry = Entry(window)

float_val = float(2.54)

def Converter():

    inch = float(name_entry.get())
    centimetre = inch*float_val
    textbox.insert(END, centimetre)

textbox = Text(bg="#BEBEBE", fg="black")

button = Button(window, text="Convert to Cm", command=Converter)
button.place(x=100, y=50)
name_entry.place(x=85,y=100)
textbox.place(y=250)

window.mainloop()
