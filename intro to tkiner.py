from tkinter import *

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text="Product = " + str(product))
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

root = Tk()
root.title("Product Calculator")
root.geometry("300x220")

Label(root, text="Enter First Number").pack(pady=5)
entry1 = Entry(root)
entry1.pack()

Label(root, text="Enter Second Number").pack(pady=5)
entry2 = Entry(root)
entry2.pack()

Button(root, text="Calculate Product", command=calculate_product).pack(pady=10)

result_label = Label(root, text="Product = ")
result_label.pack()

root.mainloop()