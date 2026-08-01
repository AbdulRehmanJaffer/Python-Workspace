

import tkinter as tk
from tkinter import messagebox


def open_planner_window():


    planner_window = tk.Toplevel(root)
    planner_window.title("Reading Schedule Planner")
    planner_window.geometry("400x300")
    planner_window.configure(bg="#f0f4f8")
    planner_window.resizable(False, False)


    title_label = tk.Label(
        planner_window,
        text="Plan Your Reading Schedule",
        font=("Helvetica", 14, "bold"),
        bg="#f0f4f8",
        fg="#2c3e50",
    )
    title_label.pack(pady=(15, 10))

    pages_label = tk.Label(
        planner_window,
        text="Total number of pages in the book:",
        bg="#f0f4f8",
        anchor="w",
    )
    pages_label.pack(fill="x", padx=30)

    pages_entry = tk.Entry(planner_window, width=20)
    pages_entry.pack(pady=(0, 10))

    per_day_label = tk.Label(
        planner_window,
        text="Pages you plan to read each day:",
        bg="#f0f4f8",
        anchor="w",
    )
    per_day_label.pack(fill="x", padx=30)

    per_day_entry = tk.Entry(planner_window, width=20)
    per_day_entry.pack(pady=(0, 10))

    result_label = tk.Label(
        planner_window,
        text="",
        bg="#f0f4f8",
        fg="#16a085",
        font=("Helvetica", 11, "bold"),
        justify="left",
    )
    result_label.pack(pady=(10, 10))



    def calculate_schedule():
        try:
            total_pages = int(pages_entry.get())
            pages_per_day = int(per_day_entry.get())

            if total_pages <= 0 or pages_per_day <= 0:
                raise ValueError("Numbers must be greater than zero.")

            complete_days = total_pages // pages_per_day
            leftover_pages = total_pages % pages_per_day

            result_label.config(
                text=(
                    f"Complete reading days: {complete_days}\n"
                    f"Pages left after those days: {leftover_pages}"
                )
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter whole numbers greater than zero for both fields.",
            )


    calculate_button = tk.Button(
        planner_window,
        text="Calculate",
        command=calculate_schedule,
        bg="#3498db",
        fg="white",
        activebackground="#2980b9",
        font=("Helvetica", 10, "bold"),
        padx=10,
        pady=5,
    )
    calculate_button.pack(pady=(5, 15))



root = tk.Tk()
root.title("Reading Schedule Planner - Home")
root.geometry("350x200")
root.configure(bg="#ffffff")

welcome_label = tk.Label(
    root,
    text="Welcome to the\nReading Schedule Planner!",
    font=("Helvetica", 13, "bold"),
    bg="#ffffff",
)
welcome_label.pack(pady=(30, 15))

open_button = tk.Button(
    root,
    text="Open Planner",
    command=open_planner_window,
    bg="#e74c3c",
    fg="white",
    activebackground="#c0392b",
    font=("Helvetica", 11, "bold"),
    padx=15,
    pady=8,
)
open_button.pack()

root.mainloop()