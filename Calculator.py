from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Interest Calculator")
window.geometry("400x400")

frame = Frame(master=window, height=140, width=360, bg="#d0efff")

lbl1 = Label(frame, text="Principal", bg="#3895D3", fg="white", width=12)
lbl2 = Label(frame, text="Time (years)", bg="#3895D3", fg="white", width=12)
lbl3 = Label(frame, text="Rate (%)", bg="#3895D3", fg="white", width=12)

principal_entry = Entry(frame)
time_entry = Entry(frame)
rate_entry = Entry(frame)


def Calculate():

    principal = float(principal_entry.get())
    time = float(time_entry.get())
    rate = float(rate_entry.get())

    simple_interest = (principal * rate * time) / 100
    compound_interest = principal * ((1 + rate / 100) ** time) - principal

    textbox.insert(END, "Simple Interest = " + str(round(simple_interest, 2)))
    textbox.insert(END, "\nCompound Interest = " + str(round(compound_interest, 2)))


textbox = Text(bg="#BEBEBE", fg="black")

btn = Button(window, text="Calculate", command=Calculate, bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
lbl2.place(x=20, y=60)
lbl3.place(x=20, y=100)
principal_entry.place(x=150, y=20)
time_entry.place(x=150, y=60)
rate_entry.place(x=150, y=100)
btn.place(x=150, y=140)
textbox.place(y=200)

window.mainloop()