import tkinter as tk
from tkinter import ttk, messagebox

class RestarauntManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Stationary Shop")


        self.stationary_items = {"Pencil": 2, "Color Pencil": 2, "Pen": 3, "Eraser": 4, "Marker": 2.5, "Highlighter": 1 }

        self.exchange_rate = 82

        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame,text="Stationary Order System", font=("Arial", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)

        self.stationary_labels = {}

        self.stationary_quantities = {}

        for i, (item, price) in enumerate(self.stationary_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=10)
            self.stationary_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.sationary_quantities[item] = quantity_entry

        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(
            row=len(self.menu_items) + 1,
            column=0,
            padx=10,
            pady=5
        )

        currency_dropdown = ttk.Combobox(frame, textcariable=self.currency_var, state="readyonly", width=18, values=("USD", "PKR"))
        currency_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            padx=10,
            pady=5
        )
        currency_dropdown.current(0)
        self.currency_var.trace("w", self.update_stationary_prices)
        


                  

